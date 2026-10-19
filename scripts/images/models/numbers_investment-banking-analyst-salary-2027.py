#!/usr/bin/env python3
"""
numbers_investment-banking-analyst-salary-2027.py

Every number in the WSG article "Investment Banking Analyst Salary 2027: What
You Actually Take Home" comes from this script. Run it and paste the printed
tables into the article. The image agent rebuilds the same model in Excel
from this file, so every assumption is a named constant with its source.

Plain Python, no imports beyond the standard library.

Tax year used: 2026 (the latest brackets published when the article was
written, October 2026). Filing status: single, no dependents, standard
deduction, no other income, no credits beyond the ones named below.

Sources (all tagged [VERIFY] in the article):
  Federal brackets and standard deduction ... IRS Rev. Proc. 2025-32
  Social Security wage base ................. SSA (ssa.gov/oact/cola/cbb.html)
  FICA rates, supplemental withholding ...... IRS Publication 15 (2026)
  New York State rates, standard deduction,
    and the tax computation worksheets ...... Form IT-2105-I (2026), tax.ny.gov
  New York City resident rates .............. Form IT-2105-I (2026), tax.ny.gov
  NYS and NYC supplemental withholding ...... NYS-50-T-NYS and NYS-50-T-NYC (1/26)
  North Carolina rate and deduction ......... ncdor.gov (3.99% for 2026; $12,750)
  California 2026 schedule, deduction, credit  FTB Tax News, 2026 indexing
  California SDI rate ....................... EDD rates page (1.3% for 2026)
  Texas ..................................... no state income tax
  401(k) limit .............................. IRS Notice 2025-67 ($24,500)
  Health premium ............................ KFF 2025 Employer Health Benefits
                                              Survey ($1,440 a year, single)
"""

INF = float("inf")

# ---------------------------------------------------------------------------
# 1. Tax parameters (2026, single filer)
# ---------------------------------------------------------------------------

# Federal. Each tuple is (top of bracket, rate). Rev. Proc. 2025-32.
FED_BRACKETS = [
    (12_400, 0.10),
    (50_400, 0.12),
    (105_700, 0.22),
    (201_775, 0.24),
    (256_225, 0.32),
    (640_600, 0.35),
    (INF, 0.37),
]
FED_STD_DED = 16_100  # single, 2026

# FICA. IRS Pub 15 (2026) and SSA.
SS_RATE = 0.062
SS_WAGE_BASE = 184_500       # 2026
MEDICARE_RATE = 0.0145
ADDL_MEDICARE_RATE = 0.009
ADDL_MEDICARE_THRESHOLD = 200_000  # single filer, not indexed

# Supplemental (bonus) withholding rates. Pub 15; NYS-50-T-NYS; NYS-50-T-NYC.
FED_SUPP_WITHHOLDING = 0.22
NYS_SUPP_WITHHOLDING = 0.1170
NYC_SUPP_WITHHOLDING = 0.0425

# New York State, single, 2026. Form IT-2105-I (2026), page 10.
NYS_BRACKETS = [
    (8_500, 0.039),
    (11_700, 0.044),
    (13_900, 0.0515),
    (80_650, 0.054),
    (215_400, 0.059),
    (1_077_550, 0.0685),
    (5_000_000, 0.0965),
    (25_000_000, 0.103),
    (INF, 0.109),
]
NYS_STD_DED = 8_000  # single, cannot be claimed as a dependent

# New York City resident, single, 2026. Same form, page 10.
NYC_BRACKETS = [
    (12_000, 0.03078),
    (25_000, 0.03762),
    (50_000, 0.03819),
    (INF, 0.03876),
]

# New York's "tax computation" worksheets for single filers (IT-2105-I 2026,
# worksheets 7 and 8). Once New York adjusted gross income passes $107,650 the
# state phases out the benefit of the lower brackets over the next $50,000, so
# by $157,650 the whole taxable income is taxed at a flat 5.9 percent. Above
# $215,400 of NYAGI a second phase-out pushes everything toward 6.85 percent.
NYS_RECAPTURE_START = 107_650
NYS_RECAPTURE_WIDTH = 50_000
NYS_FLAT_RATE_1 = 0.059
NYS_TIER2_START = 215_400
NYS_TIER2_RECAPTURE_BASE = 567        # worksheet 8, line 4
NYS_TIER2_INCREMENTAL_BENEFIT = 2_047 # worksheet 8, line 5

# North Carolina (Charlotte). Flat rate 3.99% for tax years after 2025 (ncdor.gov).
NC_RATE = 0.0399
NC_STD_DED = 12_750  # single (2025 figure; 2026 not yet posted)

# California (San Francisco). 2026 indexed schedule X, FTB Tax News.
CA_BRACKETS = [
    (11_456, 0.01),
    (27_157, 0.02),
    (42_861, 0.04),
    (59_498, 0.06),
    (75_197, 0.08),
    (384_109, 0.093),
    (460_927, 0.103),
    (768_213, 0.113),
    (INF, 0.123),
]
CA_STD_DED = 5_900          # single, 2026
CA_EXEMPTION_CREDIT = 158   # single, 2026 (a credit against tax, not a deduction)
CA_SDI_RATE = 0.013         # 2026, no wage ceiling

# Texas (Houston): no state income tax.

# Pre-tax deductions used in the "with deductions" case.
K401_LIMIT = 24_500           # 2026 elective deferral limit
HEALTH_PREMIUM_SINGLE = 1_500 # a year; KFF 2025 average worker share is $1,440

# Pay inputs (latest confirmed: the 2026 analyst class and the Summer 2026
# bonus season). Bases from the Wall Street Oasis 2026 analyst bonus thread
# (per-bank reports), Mergers & Inquisitions' February 2026 report, and the
# 2021 raise coverage (Banking Dive, eFinancialCareers). Bonus buckets are
# the low / middle / high of the 2026 first-year reports. All tagged in the
# article.
PAY_SCALE = {
    # tier: (AN1 base, AN2 base, AN3 base, AN1 bonus low, AN1 bonus mid, AN1 bonus high)
    "Bulge bracket":   (110_000, 125_000, 135_000, 45_000, 75_000, 100_000),
    "Elite boutique":  (120_000, 130_000, 140_000, 50_000, 80_000, 110_000),
    "Middle market":   (105_000, 115_000, 125_000, 35_000, 55_000, 75_000),
    "Regional boutique": (90_000, 100_000, 110_000, 15_000, 30_000, 50_000),
}
SIGNING_BONUS = (10_000, 15_000)   # typical range at large banks
RELOCATION = (5_000, 10_000)       # typical range, often a lump sum

# Social Security wage base history (SSA, ssa.gov/oact/cola/cbb.html) and the
# employee OASDI rate (ssa.gov/oact/progdata/taxRates.html).
WAGE_BASE_HISTORY = [(1937, 3_000, 0.01), (1960, 4_800, 0.03), (1980, 25_900, 0.0508),
                     (2000, 76_200, 0.062), (2020, 137_700, 0.062), (2026, 184_500, 0.062)]


# ---------------------------------------------------------------------------
# 2. Helpers
# ---------------------------------------------------------------------------

def bracket_tax(taxable, brackets):
    """Return (total tax, list of (lower, upper, rate, tax in this slice))."""
    taxable = max(0.0, taxable)
    lines = []
    lower = 0.0
    total = 0.0
    for upper, rate in brackets:
        if taxable <= lower:
            break
        slice_top = min(taxable, upper)
        slice_amt = slice_top - lower
        slice_tax = slice_amt * rate
        lines.append((lower, slice_top, rate, slice_tax))
        total += slice_tax
        lower = upper
    return total, lines


def federal_income_tax(taxable):
    return bracket_tax(taxable, FED_BRACKETS)


def fica(fica_wages):
    """Social Security capped at the wage base; Medicare uncapped plus the
    0.9 percent additional Medicare tax above $200,000."""
    ss = SS_RATE * min(fica_wages, SS_WAGE_BASE)
    medicare = MEDICARE_RATE * fica_wages
    addl = ADDL_MEDICARE_RATE * max(0.0, fica_wages - ADDL_MEDICARE_THRESHOLD)
    return ss, medicare, addl


def nys_tax(nyagi, taxable):
    """New York State tax for a single filer, including the worksheets that
    phase out the lower brackets for higher earners."""
    schedule, _ = bracket_tax(taxable, NYS_BRACKETS)
    if nyagi <= NYS_RECAPTURE_START:
        return schedule, "rate schedule"
    if taxable <= NYS_TIER2_START:
        # Worksheet 7
        flat = NYS_FLAT_RATE_1 * taxable
        if nyagi >= NYS_RECAPTURE_START + NYS_RECAPTURE_WIDTH:
            return flat, "flat 5.9% (worksheet 7)"
        frac = round((nyagi - NYS_RECAPTURE_START) / NYS_RECAPTURE_WIDTH, 4)
        return schedule + (flat - schedule) * frac, "worksheet 7 phase-in"
    if nyagi > NYS_TIER2_START and taxable <= 1_077_550:
        # Worksheet 8
        excess = min(nyagi - NYS_TIER2_START, NYS_RECAPTURE_WIDTH)
        frac = round(excess / NYS_RECAPTURE_WIDTH, 4)
        return (schedule + NYS_TIER2_RECAPTURE_BASE
                + NYS_TIER2_INCREMENTAL_BENEFIT * frac), "worksheet 8"
    return schedule, "rate schedule (above the ranges modeled)"


def nyc_tax(taxable):
    total, _ = bracket_tax(taxable, NYC_BRACKETS)
    return total


def ca_tax(agi):
    taxable = max(0.0, agi - CA_STD_DED)
    gross_tax, _ = bracket_tax(taxable, CA_BRACKETS)
    return max(0.0, gross_tax - CA_EXEMPTION_CREDIT)


def nc_tax(agi):
    return NC_RATE * max(0.0, agi - NC_STD_DED)


def money(x):
    """$123,456 style, rounded to the dollar."""
    return f"${x:,.0f}"


def pct(x):
    return f"{x * 100:.1f}%"


# ---------------------------------------------------------------------------
# 3. The take-home engine
# ---------------------------------------------------------------------------

def take_home(base, bonus, city="NYC", k401_pct=0.0, health=0.0):
    """Full-year take-home for a single filer. Returns a dict of every line.

    Order of operations, which is the order a payroll system uses:
      gross = base + bonus
      401(k) deferral comes out of income-taxable wages but NOT out of FICA wages
      a Section 125 health premium comes out of both
    """
    gross = base + bonus
    k401 = min(k401_pct * gross, K401_LIMIT)
    taxable_wages = gross - k401 - health          # Box 1 wages
    fica_wages = gross - health                    # Boxes 3 and 5 wages
    fed_taxable = max(0.0, taxable_wages - FED_STD_DED)
    fed, fed_lines = federal_income_tax(fed_taxable)
    ss, med, addl = fica(fica_wages)

    state = 0.0
    local = 0.0
    sdi = 0.0
    state_note = ""
    if city == "NYC":
        nyagi = taxable_wages
        ny_taxable = max(0.0, nyagi - NYS_STD_DED)
        state, state_note = nys_tax(nyagi, ny_taxable)
        local = nyc_tax(ny_taxable)
    elif city == "Charlotte":
        state = nc_tax(taxable_wages)
        state_note = "NC flat 3.99%"
    elif city == "Houston":
        state = 0.0
        state_note = "no state income tax"
    elif city == "San Francisco":
        state = ca_tax(taxable_wages)
        sdi = CA_SDI_RATE * fica_wages
        state_note = "CA schedule X less $158 exemption credit"
    else:
        raise ValueError(city)

    total_tax = fed + ss + med + addl + state + local + sdi
    net = gross - k401 - health - total_tax
    return {
        "base": base, "bonus": bonus, "gross": gross, "k401": k401, "health": health,
        "taxable_wages": taxable_wages, "fica_wages": fica_wages,
        "fed_taxable": fed_taxable, "fed": fed, "fed_lines": fed_lines,
        "ss": ss, "medicare": med, "addl_medicare": addl,
        "state": state, "local": local, "sdi": sdi, "state_note": state_note,
        "total_tax": total_tax, "net": net,
        "eff_rate": total_tax / gross,
        "net_monthly": net / 12,
    }


def print_table(headers, rows):
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join([" --- "] * len(headers)) + "|")
    for r in rows:
        print("| " + " | ".join(str(c) for c in r) + " |")
    print()


# ---------------------------------------------------------------------------
# 4. Tables the article shows
# ---------------------------------------------------------------------------

def table_0_pay_inputs():
    """Section 2, the base salary by tier table, and the Social Security history."""
    print("TABLE 0. Analyst base salary and first-year bonus by firm tier (latest confirmed, 2026 class)")
    rows = []
    for tier, (b1, b2, b3, lo, mid, hi) in PAY_SCALE.items():
        rows.append([tier, money(b1), money(b2), money(b3), f"{money(lo)} to {money(hi)}", f"{money(b1 + lo)} to {money(b1 + hi)}"])
    print_table(["Tier", "First-year base", "Second-year base", "Third-year base", "First-year bonus range", "First-year all-in range"], rows)

    print("TABLE 0b. Social Security wage base and employee rate, selected years")
    rows = [[str(y), money(wb), pct(rate), money(wb * rate)] for y, wb, rate in WAGE_BASE_HISTORY]
    print_table(["Year", "Wage base", "Employee rate", "Maximum employee tax"], rows)


def table_1_base_case():
    """Section 4, Table 1: one first-year analyst, NYC, $120,000 base plus
    $80,000 bonus, single, standard deduction, no pre-tax deductions."""
    r = take_home(120_000, 80_000, "NYC")
    print("TABLE 1. Federal income tax by bracket, $200,000 gross, NYC, single, 2026 rules")
    rows = []
    for lower, upper, rate, tax in r["fed_lines"]:
        rows.append([f"{money(lower)} to {money(upper)}", pct(rate), money(upper - lower), money(tax)])
    rows.append(["Total federal income tax", "", money(r["fed_taxable"]), money(r["fed"])])
    print_table(["Taxable income slice", "Rate", "Dollars in slice", "Tax"], rows)

    print("TABLE 2. Gross to net, line by line")
    rows = [
        ["Base salary", money(r["base"])],
        ["Year-end bonus", money(r["bonus"])],
        ["Gross pay", money(r["gross"])],
        ["Minus federal standard deduction", money(FED_STD_DED)],
        ["Federal taxable income", money(r["fed_taxable"])],
        ["Federal income tax (from Table 1)", money(r["fed"])],
        [f"Social Security, 6.2% of the first {money(SS_WAGE_BASE)}", money(r["ss"])],
        ["Medicare, 1.45% of all wages", money(r["medicare"])],
        ["Additional Medicare, 0.9% above $200,000", money(r["addl_medicare"])],
        ["New York taxable income (gross minus $8,000 NY standard deduction)", money(r["taxable_wages"] - NYS_STD_DED)],
        [f"New York State tax ({r['state_note']})", money(r["state"])],
        ["New York City resident tax", money(r["local"])],
        ["Total taxes", money(r["total_tax"])],
        ["Take-home pay", money(r["net"])],
        ["Take-home as a share of gross", pct(r["net"] / r["gross"])],
        ["Effective tax rate", pct(r["eff_rate"])],
        ["Take-home per month", money(r["net_monthly"])],
    ]
    print_table(["Line", "Amount"], rows)
    return r


def table_3_nyc_detail(r):
    """New York City tax by bracket, for the same analyst."""
    print("TABLE 3. New York City resident tax by bracket")
    ny_taxable = r["taxable_wages"] - NYS_STD_DED
    total, lines = bracket_tax(ny_taxable, NYC_BRACKETS)
    rows = [[f"{money(lo)} to {money(hi)}", f"{rate*100:.3f}%", money(hi - lo), money(tax)] for lo, hi, rate, tax in lines]
    rows.append(["Total NYC tax", "", money(ny_taxable), money(total)])
    print_table(["NYC taxable income slice", "Rate", "Dollars in slice", "Tax"], rows)

    # What the plain NY rate schedule would have given, versus the flat 5.9 percent.
    sched, sched_lines = bracket_tax(ny_taxable, NYS_BRACKETS)
    print(f"NY State check: plain rate schedule on {money(ny_taxable)} = {money(sched)}; "
          f"flat 5.9% (worksheet 7, NYAGI over $157,650) = {money(0.059 * ny_taxable)}; "
          f"difference (the phased-out bracket benefit) = {money(0.059 * ny_taxable - sched)}")
    print()


def table_4_with_deductions():
    """Same analyst with a 6 percent 401(k) deferral and a $1,500 health premium."""
    a = take_home(120_000, 80_000, "NYC")
    b = take_home(120_000, 80_000, "NYC", k401_pct=0.06, health=HEALTH_PREMIUM_SINGLE)
    print("TABLE 4. Same analyst, with a 6% 401(k) contribution and a $1,500 health premium")
    rows = [
        ["Gross pay", money(a["gross"]), money(b["gross"])],
        ["401(k) deferral (6% of gross)", money(a["k401"]), money(b["k401"])],
        ["Health premium (pre-tax)", money(a["health"]), money(b["health"])],
        ["Wages subject to income tax", money(a["taxable_wages"]), money(b["taxable_wages"])],
        ["Wages subject to Social Security and Medicare", money(a["fica_wages"]), money(b["fica_wages"])],
        ["Federal income tax", money(a["fed"]), money(b["fed"])],
        ["Social Security", money(a["ss"]), money(b["ss"])],
        ["Medicare (including additional)", money(a["medicare"] + a["addl_medicare"]), money(b["medicare"] + b["addl_medicare"])],
        ["New York State tax", money(a["state"]), money(b["state"])],
        ["New York City tax", money(a["local"]), money(b["local"])],
        ["Total taxes", money(a["total_tax"]), money(b["total_tax"])],
        ["Cash in your checking account", money(a["net"]), money(b["net"])],
        ["Cash plus 401(k) balance", money(a["net"] + a["k401"]), money(b["net"] + b["k401"])],
        ["Take-home per month", money(a["net_monthly"]), money(b["net_monthly"])],
    ]
    print_table(["Line", "No deductions", "6% 401(k) + health"], rows)
    tax_saved = a["total_tax"] - b["total_tax"]
    cost = a["net"] - b["net"]
    print(f"The $12,000 deferral plus $1,500 premium cut taxes by {money(tax_saved)}, "
          f"so checking-account cash fell by only {money(cost)} while $12,000 went into the 401(k).")
    print(f"Each $1,000 put in the 401(k) costs about {money(1000 * (1 - (a['total_tax'] - take_home(120_000, 80_000, 'NYC', k401_pct=0.06).get('total_tax')) / 12_000))} of take-home.")
    print()
    return a, b


def table_5_bonus_check():
    """What the $80,000 bonus check looks like after supplemental withholding,
    versus the tax the bonus actually adds to the year's bill."""
    bonus = 80_000
    base = 120_000
    # Withholding on the bonus check. Assume the bonus is paid in a month when
    # year-to-date wages are still under the Social Security wage base, which
    # is true for an $80,000 bonus on a $120,000 base paid any time in the year
    # (120,000 + 80,000 = 200,000 > 184,500, so the last $15,500 of the year's
    # wages escape Social Security; we show that in the "actual" column).
    fed_w = FED_SUPP_WITHHOLDING * bonus
    ss_w = SS_RATE * bonus
    med_w = MEDICARE_RATE * bonus
    nys_w = NYS_SUPP_WITHHOLDING * bonus
    nyc_w = NYC_SUPP_WITHHOLDING * bonus
    total_w = fed_w + ss_w + med_w + nys_w + nyc_w
    net_check = bonus - total_w

    # The true marginal tax on the bonus: year with bonus minus year without.
    with_b = take_home(base, bonus, "NYC")
    without_b = take_home(base, 0, "NYC")
    actual = {
        "fed": with_b["fed"] - without_b["fed"],
        "ss": with_b["ss"] - without_b["ss"],
        "med": (with_b["medicare"] + with_b["addl_medicare"]) - (without_b["medicare"] + without_b["addl_medicare"]),
        "nys": with_b["state"] - without_b["state"],
        "nyc": with_b["local"] - without_b["local"],
    }
    actual_total = sum(actual.values())
    print("TABLE 5. The $80,000 bonus check: what is withheld versus what the bonus really costs in tax")
    rows = [
        ["Federal income tax", f"22.0% = {money(fed_w)}", money(actual["fed"])],
        ["Social Security", f"6.2% = {money(ss_w)}", money(actual["ss"])],
        ["Medicare", f"1.45% = {money(med_w)}", money(actual["med"])],
        ["New York State", f"11.70% = {money(nys_w)}", money(actual["nys"])],
        ["New York City", f"4.25% = {money(nyc_w)}", money(actual["nyc"])],
        ["Total", f"{pct(total_w / bonus)} = {money(total_w)}", f"{pct(actual_total / bonus)} = {money(actual_total)}"],
        ["Bonus you keep", money(net_check), money(bonus - actual_total)],
    ]
    print_table(["Item", "Withheld from the check", "Actual tax the bonus adds"], rows)
    print(f"Over-withheld on the bonus: {money(total_w - actual_total)} (comes back as a refund or lower withholding elsewhere).")
    print(f"Note: the Social Security line is lower in the actual column because base plus bonus "
          f"({money(base + bonus)}) passes the {money(SS_WAGE_BASE)} wage base, so {money(base + bonus - SS_WAGE_BASE)} "
          f"of the year's wages owe no Social Security tax.")
    print()


def table_6_four_cities():
    """Same $200,000 gross in four cities, no deductions."""
    print("TABLE 6. The same $200,000 ($120,000 base + $80,000 bonus) in four cities, single, no pre-tax deductions")
    cities = ["NYC", "Charlotte", "Houston", "San Francisco"]
    results = {c: take_home(120_000, 80_000, c) for c in cities}
    rows = []
    labels = [
        ("Federal income tax", "fed"),
        ("Social Security + Medicare", None),
        ("State income tax", "state"),
        ("City income tax", "local"),
        ("State disability insurance", "sdi"),
        ("Total taxes", "total_tax"),
        ("Take-home pay", "net"),
        ("Take-home per month", "net_monthly"),
    ]
    for label, key in labels:
        row = [label]
        for c in cities:
            r = results[c]
            if key is None:
                row.append(money(r["ss"] + r["medicare"] + r["addl_medicare"]))
            else:
                row.append(money(r[key]))
        rows.append(row)
    rows.append(["Effective tax rate"] + [pct(results[c]["eff_rate"]) for c in cities])
    rows.append(["Gap versus New York (a year)"] + [money(results[c]["net"] - results["NYC"]["net"]) for c in cities])
    print_table(["Line", "New York", "Charlotte", "Houston", "San Francisco"], rows)
    return results


def table_7_by_bucket():
    """First-year all-in by firm tier and bonus bucket, NYC, no deductions."""
    print("TABLE 7. First-year analyst take-home by tier and bucket, New York City, 2026 rules, no pre-tax deductions")
    cases = [
        ("Bulge bracket, bottom bucket", 110_000, 45_000),
        ("Bulge bracket, middle bucket", 110_000, 75_000),
        ("Bulge bracket, top bucket", 110_000, 100_000),
        ("Elite boutique, middle bucket", 120_000, 80_000),
        ("Elite boutique, top bucket", 120_000, 110_000),
        ("Middle market, middle bucket", 105_000, 55_000),
        ("Regional boutique", 90_000, 30_000),
    ]
    rows = []
    for label, base, bonus in cases:
        r = take_home(base, bonus, "NYC")
        rows.append([label, money(base), money(bonus), money(r["gross"]), money(r["total_tax"]), money(r["net"]), pct(r["eff_rate"]), money(r["net_monthly"])])
    print_table(["Case", "Base", "Bonus", "All-in", "Total taxes", "Take-home", "Effective rate", "Per month"], rows)


def table_8_three_years():
    """Pay across the analyst years and the first associate year, NYC."""
    print("TABLE 8. Bulge bracket pay by year, New York City, middle-to-upper bucket, 2026 rules, no pre-tax deductions")
    cases = [
        ("First-year analyst", 110_000, 75_000),
        ("Second-year analyst", 125_000, 100_000),
        ("Third-year analyst", 135_000, 130_000),
        ("First-year associate (direct promote)", 175_000, 120_000),
    ]
    rows = []
    prev_net = None
    for label, base, bonus in cases:
        r = take_home(base, bonus, "NYC")
        step = "" if prev_net is None else money(r["net"] - prev_net)
        rows.append([label, money(base), money(bonus), money(r["gross"]), money(r["total_tax"]), money(r["net"]), pct(r["eff_rate"]), step])
        prev_net = r["net"]
    print_table(["Year", "Base", "Bonus", "All-in", "Total taxes", "Take-home", "Effective rate", "Take-home step up"], rows)


def table_9_comparison():
    """IB versus consulting, private credit and equity research, first year, NYC."""
    print("TABLE 9. First-year all-in and take-home across four entry jobs, New York City, 2026 rules, no pre-tax deductions")
    cases = [
        ("Investment banking analyst (bulge bracket, middle bucket)", 110_000, 75_000, 85),
        ("McKinsey business analyst", 112_000, 30_000, 60),
        ("Private credit analyst (first year, mid)", 140_000, 75_000, 65),
        ("Equity research associate (first year, mid)", 120_000, 40_000, 60),
    ]
    rows = []
    for label, base, bonus, hours in cases:
        r = take_home(base, bonus, "NYC")
        annual_hours = hours * 50
        rows.append([label, money(base), money(bonus), money(r["gross"]), money(r["net"]), f"{hours}", money(r["net"] / annual_hours) + "/hr"])
    print_table(["Job", "Base", "Bonus", "All-in", "Take-home", "Hours a week", "Take-home per hour"], rows)


def table_10_monthly_budget(net_monthly_with_deductions):
    """A monthly budget for the NYC first-year, using the with-deductions take-home.
    Three columns: a shared apartment on a careful budget, a shared apartment
    with typical first-year spending, and a studio with typical spending."""
    print("TABLE 10. A monthly budget for the New York first-year (take-home after 6% 401(k) and health premium)")
    rent_share = 2_500   # a bedroom in a shared two or three bedroom, Murray Hill / UES / FiDi
    rent_studio = 3_800  # a studio in the same neighborhoods
    transit = round(35 * 52 / 12)  # OMNY weekly cap, $35 x 52 weeks / 12 months
    columns = {
        "Shared, careful": {"Rent": rent_share, "Utilities, internet, phone": 200, "Transit (OMNY $35 weekly cap)": transit,
                            "Groceries and food the desk does not cover": 600, "Going out, gym, subscriptions": 400,
                            "Renter's insurance, laundry, household": 100, "Flights home, gifts, clothes (averaged)": 250},
        "Shared, typical": {"Rent": rent_share, "Utilities, internet, phone": 200, "Transit (OMNY $35 weekly cap)": transit,
                            "Groceries and food the desk does not cover": 900, "Going out, gym, subscriptions": 1_000,
                            "Renter's insurance, laundry, household": 100, "Flights home, gifts, clothes (averaged)": 400},
        "Studio, typical": {"Rent": rent_studio, "Utilities, internet, phone": 250, "Transit (OMNY $35 weekly cap)": transit,
                            "Groceries and food the desk does not cover": 900, "Going out, gym, subscriptions": 1_000,
                            "Renter's insurance, laundry, household": 100, "Flights home, gifts, clothes (averaged)": 400},
    }
    lines = list(next(iter(columns.values())).keys())
    rows = [["Take-home per month"] + [money(net_monthly_with_deductions)] * 3]
    for l in lines:
        rows.append([l] + [money(columns[c][l]) for c in columns])
    totals = {c: sum(columns[c].values()) for c in columns}
    rows.append(["Total spending"] + [money(totals[c]) for c in columns])
    rows.append(["Left over each month"] + [money(net_monthly_with_deductions - totals[c]) for c in columns])
    rows.append(["Savings rate on take-home (cash only)"] + [pct((net_monthly_with_deductions - totals[c]) / net_monthly_with_deductions) for c in columns])
    rows.append(["Savings rate counting the $1,000 a month 401(k) deferral"] + [pct((net_monthly_with_deductions - totals[c] + 1_000) / (net_monthly_with_deductions + 1_000)) for c in columns])
    rows.append(["Saved in a year (cash only)"] + [money(12 * (net_monthly_with_deductions - totals[c])) for c in columns])
    print_table(["Line"] + list(columns.keys()), rows)
    print(f"40x rule: a {money(rent_share)} room needs {money(40 * rent_share)} of income; a {money(rent_studio)} studio needs {money(40 * rent_studio)}.")
    print(f"Rent as a share of take-home: shared {pct(rent_share / net_monthly_with_deductions)}, studio {pct(rent_studio / net_monthly_with_deductions)}.")
    print()


def misc_numbers():
    """Loose numbers quoted in the body."""
    r = take_home(120_000, 80_000, "NYC")
    print("MISC NUMBERS")
    print(f"Hook: $200,000 gross keeps {money(r['net'])} ({pct(r['net'] / r['gross'])}); taxes {money(r['total_tax'])}.")
    hours = 85 * 50
    print(f"Hourly: {hours} hours a year at 85 a week. Gross {money(r['gross'] / hours)}/hr; take-home {money(r['net'] / hours)}/hr.")
    print(f"Marginal rate on the next dollar at $200,000 in NYC: federal 24% + NY 5.9% + NYC 3.876% + Medicare 1.45% + additional Medicare 0.9% = {pct(0.24 + 0.059 + 0.03876 + 0.0145 + 0.009)} (no Social Security, since $200,000 is past the wage base).")
    print(f"Marginal rate on a dollar between $157,650 and $184,500 of wages: federal 24% + NY 5.9% + NYC 3.876% + SS 6.2% + Medicare 1.45% = {pct(0.24 + 0.059 + 0.03876 + 0.062 + 0.0145)}.")
    nyc_only = r["local"]
    print(f"NYC resident tax on this analyst: {money(nyc_only)} a year, {money(nyc_only / 12)} a month. That is the number a Hoboken or Jersey City address avoids (New Jersey taxes you instead, with a credit for New York State tax).")
    # Half-year first calendar year for a July start: six months of base, no bonus yet.
    half = take_home(60_000, 0, "NYC")
    print(f"First calendar year (July start, six months of a $120,000 base, no bonus yet): gross {money(half['gross'])}, taxes {money(half['total_tax'])}, take-home {money(half['net'])}, effective rate {pct(half['eff_rate'])}.")
    print(f"Social Security in 1937: 1% of the first $3,000 = $30 a year. In 2026: 6.2% of the first $184,500 = {money(0.062 * 184_500)}.")
    print(f"$110,000 base over 26 paychecks = {money(110_000 / 26)} gross a paycheck; $120,000 = {money(120_000 / 26)}.")
    # Paycheck estimate for the $120,000 base alone (withholding on regular wages approximates the full-year tax on base only).
    base_only = take_home(120_000, 0, "NYC")
    print(f"If the base were the whole year's income: taxes {money(base_only['total_tax'])}, net {money(base_only['net'])}, per biweekly check about {money(base_only['net'] / 26)}.")
    # The biweekly deposit on the base alone (what the first twelve months look like), with and without
    # the 6 percent 401(k) and the health premium. Withholding on regular wages tracks the full-year tax
    # on the base closely, so the full-year net divided by 26 is a fair estimate of the deposit.
    for b in (110_000, 120_000):
        plain = take_home(b, 0, "NYC")
        ded = take_home(b, 0, "NYC", k401_pct=0.06, health=HEALTH_PREMIUM_SINGLE)
        print(f"Biweekly deposit on a {money(b)} base alone: no deductions {money(plain['net'] / 26)}; "
              f"with 6% 401(k) and health premium {money(ded['net'] / 26)} (gross per check {money(b / 26)}).")
    # Goldman Sachs full-year 2025 (4Q25 earnings release, SEC 8-K exhibit): net revenues $58.28bn,
    # compensation and benefits $18.906bn, investment banking fees $9.348bn (+21% vs 2024).
    gs_rev, gs_comp, gs_ib_fees = 58.28, 18.906, 9.348
    print(f"Goldman 2025 comp ratio: {gs_comp} / {gs_rev} = {pct(gs_comp / gs_rev)}; IB fees {gs_ib_fees}bn, up 21% on 2024.")
    # Tier-table arithmetic quoted in the body
    print(f"Same-base spread: BB top bucket minus BB bottom bucket = {money(100_000 - 45_000)} of bonus, "
          f"{money(take_home(110_000, 100_000, 'NYC')['net'] - take_home(110_000, 45_000, 'NYC')['net'])} of take-home.")
    bb_mid = take_home(110_000, 75_000, "NYC")
    print(f"BB middle bucket first-year: gross {money(bb_mid['gross'])}, take-home {money(bb_mid['net'])}, per month {money(bb_mid['net_monthly'])}.")
    # Derived figures quoted in the body
    budget_share_typical = 10_114 - 5_252   # Table 10, shared typical, left over
    budget_studio_typical = 10_114 - 6_602  # Table 10, studio typical, left over
    print(f"Studio versus share, typical spending: {money(budget_share_typical - budget_studio_typical)} a month less saved.")
    print(f"Complement of the $662 take-home cost per $1,000 deferred: {money(1_000 - 662)} of tax saved.")
    print(f"Keep on a $10,000 bigger bonus at the 36.1% marginal rate: {money(10_000 * (1 - 0.361))} (quoted as about $6,400).")
    print(f"Tax shares of the $200,000 case: federal {pct(r['fed'] / r['gross'])}, FICA {pct((r['ss'] + r['medicare']) / r['gross'])}, "
          f"NY State {pct(r['state'] / r['gross'])}, NYC {pct(r['local'] / r['gross'])}.")
    print()


def research_inputs():
    """Figures quoted in the article that come from sources rather than from
    this model. Listed so the image agent and the editor can see them in one
    place; each carries a [VERIFY] tag in the draft."""
    print("RESEARCH INPUTS (sourced, not computed)")
    rows = [
        ("Manhattan studio asking rents, October 2026 (RentHop)", "Upper East Side $3,450; East Village $3,500; Hell's Kitchen $3,770; Murray Hill $3,900; Financial District $4,160"),
        ("Zumper cross-check, October 2026", "Upper East Side studio $3,775; Financial District studio $4,013"),
        ("Manhattan median asking rent, all sizes, May 2026 (StreetEasy)", "$4,927"),
        ("Room in a shared 2 or 3 bedroom (estimate)", "$2,200 to $3,000"),
        ("FARE Act average broker fee avoided, May 2026 (StreetEasy)", "$5,862; about $46 a month higher asking rent on affected listings"),
        ("MTA fare and OMNY weekly cap (mta.info)", "$3; $35 a week"),
        ("2021 raise wave", "JPMorgan $85,000 to $100,000 (June 2021); Goldman $85,000 to $110,000, second-year $125,000, associate $150,000 (Aug 3, 2021); Evercore $120,000 plus $15,000 signing; Jefferies and William Blair $110,000"),
        ("WSO company pay page averages, October 2026", "Centerview analysts $225,596 (42 submissions); Evercore analysts $180,124 (240 submissions)"),
        ("Stub bonuses reported on the WSO 2026 thread", "William Blair $22,500; JPMorgan $35,000"),
        ("Social Security wage base 2025 (SSA)", "$176,100"),
        ("Goldman Sachs 2021 analyst survey (CNN, March 18, 2021)", "13 analysts; more than 95 hours a week; about five hours of sleep"),
        ("Mergers & Inquisitions, February 2026", "analyst base $100,000 to $125,000; all-in $165,000 to $225,000; associate base $175,000 to $225,000; junior pay up about 5 percent"),
        ("Goldman Sachs 2025 (8-K exhibit)", "net revenues $58.28bn; compensation $18.906bn; IB fees $9.348bn, up 21 percent"),
    ]
    for k, v in rows:
        print(f"- {k}: {v}")
    print()


if __name__ == "__main__":
    table_0_pay_inputs()
    r = table_1_base_case()
    table_3_nyc_detail(r)
    a, b = table_4_with_deductions()
    table_5_bonus_check()
    table_6_four_cities()
    table_7_by_bucket()
    table_8_three_years()
    table_9_comparison()
    table_10_monthly_budget(b["net_monthly"])
    misc_numbers()
    research_inputs()
