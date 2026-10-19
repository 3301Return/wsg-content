#!/usr/bin/env python3
"""Numbers behind "Growth Equity Interview Guide for Undergrads" (WSG, October 5, 2026).

Plain Python, no dependencies. Prints every table the article shows, as Markdown pipe
tables, so the figures in the draft can be pasted straight from this output and the image
agent can rebuild the same tables in Excel.

The company, Harborline, is fictional: a vertical SaaS business selling dispatch and billing
software to freight brokers. Every number here is invented for the article.

Blocks, in article order:

  1. Harborline's ARR bridge (beginning ARR, churn, expansion, new logos, ending ARR) and the
     growth and retention metrics that come out of it. Used in the metrics question bank
     (section 7) and the investment screen (section 11).
  2. Unit economics: gross margin, CAC, CAC payback, LTV to CAC, magic number, burn multiple,
     Rule of 40. Same two sources.
  3. The proposed deal: $100 million of new preferred stock at a $600 million post-money
     valuation, the pre-money, the ownership, the price per share and a simple cap table
     before and after the round (section 9 and section 11).
  4. Three exit scenarios five years out (Bear, Base, Bull): ARR, exit multiple, equity value,
     and the payout to the preferred shown three ways: as plain common (no preference), with a
     1x non-participating preference, and with a 1x participating preference. MOIC and IRR for
     each (section 11, with the preference walk reused in section 9).
  5. The valuation question numbers: entry EV to ARR, growth-adjusted multiple (section 8).

Conventions: $ millions unless a line says otherwise. Percentages are shown to one decimal.
MOIC is money back divided by money in. IRR over a five-year hold with one cash out and one
cash in is MOIC to the power of one fifth, minus one. The screen ignores debt and cash at
exit (equity value equals enterprise value), later funding rounds, and option pool top-ups;
the article says so.

Run from the repo root:
    python3 scripts/images/models/numbers_growth-equity-interview-guide-undergrads.py
"""


# --------------------------------------------------------------------------------------
# formatting helpers
# --------------------------------------------------------------------------------------
def m(x, d=1):
    """$ millions, parentheses for negatives, d decimals."""
    s = f"{abs(x):,.{d}f}"
    return f"(${s})" if x < 0 else f"${s}"


def dollars(x):
    """Whole dollars with commas."""
    return f"${x:,.0f}"


def pct(x, d=1):
    """A decimal fraction shown as a percentage, parentheses for negatives."""
    s = f"{abs(x) * 100:.{d}f}%"
    return f"({s})" if x < 0 else s


def mult(x, d=1):
    return f"{x:.{d}f}x"


def table(headers, rows):
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        print("| " + " | ".join(r) + " |")
    print()


# --------------------------------------------------------------------------------------
# Block 0: the outside-view descriptors the sample pitch uses (section 6, section 14)
# --------------------------------------------------------------------------------------
# What a candidate can see about Harborline from LinkedIn and its website before any call.
# Not financial inputs; listed here so every figure in the article has a line in this file.
HEADCOUNT_TODAY = 150
HEADCOUNT_YEAR_AGO = 100
OPEN_SALES_AND_CS_ROLES = 12          # "a dozen open roles in sales and customer success"
headcount_growth = HEADCOUNT_TODAY / HEADCOUNT_YEAR_AGO - 1   # 50%

print("# Block 0: outside-view descriptors for the sample pitch (section 6)\n")
table(
    ["Descriptor", "Value"],
    [
        ["Employees today (LinkedIn)", f"about {HEADCOUNT_TODAY}"],
        ["Employees a year ago", f"about {HEADCOUNT_YEAR_AGO}"],
        ["Headcount growth", pct(headcount_growth, 0)],
        ["Open sales and customer success roles", f"about {OPEN_SALES_AND_CS_ROLES} (a dozen)"],
    ],
)

# --------------------------------------------------------------------------------------
# Block 1: the ARR bridge and retention
# --------------------------------------------------------------------------------------
BEGIN_ARR = 40.0        # ARR at the start of the year (Year 0 means today)
CHURNED_ARR = 4.0       # ARR lost from customers that cancelled or shrank
EXPANSION_ARR = 6.0     # extra ARR from existing customers buying more seats or modules
NEW_LOGO_ARR = 18.0     # ARR from brand-new customers signed this year
END_ARR = BEGIN_ARR - CHURNED_ARR + EXPANSION_ARR + NEW_LOGO_ARR   # 60.0

growth = END_ARR / BEGIN_ARR - 1                          # 50.0%
gross_retention = (BEGIN_ARR - CHURNED_ARR) / BEGIN_ARR   # 90.0%
net_retention = (BEGIN_ARR - CHURNED_ARR + EXPANSION_ARR) / BEGIN_ARR   # 105.0%
net_new_arr = END_ARR - BEGIN_ARR                         # 20.0
gross_new_arr = NEW_LOGO_ARR + EXPANSION_ARR              # 24.0

assert abs(END_ARR - 60.0) < 1e-9

print("# Block 1: Harborline ARR bridge (section 7, section 11)\n")
table(
    ["Line", "$ millions", "How it is calculated"],
    [
        ["Beginning ARR (start of year)", m(BEGIN_ARR), "given"],
        ["Minus churned ARR", m(-CHURNED_ARR), "customers that left or downgraded"],
        ["Plus expansion ARR", m(EXPANSION_ARR), "existing customers buying more"],
        ["Plus new logo ARR", m(NEW_LOGO_ARR), "brand-new customers"],
        ["Ending ARR (today)", m(END_ARR), "40.0 minus 4.0 plus 6.0 plus 18.0"],
        ["Net new ARR", m(net_new_arr), "60.0 minus 40.0"],
        ["Gross new ARR (new plus expansion)", m(gross_new_arr), "18.0 plus 6.0"],
    ],
)

print("## Growth and retention from the bridge\n")
table(
    ["Metric", "Value", "Arithmetic"],
    [
        ["ARR growth", pct(growth), "60.0 divided by 40.0, minus 1"],
        ["Gross revenue retention", pct(gross_retention), "(40.0 minus 4.0) divided by 40.0"],
        ["Net revenue retention", pct(net_retention), "(40.0 minus 4.0 plus 6.0) divided by 40.0"],
    ],
)

# --------------------------------------------------------------------------------------
# Block 2: unit economics
# --------------------------------------------------------------------------------------
REVENUE = 50.0          # GAAP revenue this year (ARR ramps from 40 to 60 during the year)
GROSS_MARGIN = 0.76     # hosting, support and implementation cost eat 24 cents per dollar
gross_profit = REVENUE * GROSS_MARGIN                      # 38.0
SALES_MARKETING = 20.0  # sales and marketing spend this year
NET_BURN = 5.0          # cash out the door this year, net of cash in
fcf_margin = -NET_BURN / REVENUE                           # (10.0%)
ARR_PER_CUSTOMER = 0.060   # $60,000 a year per customer, in $ millions
customers_end = END_ARR / ARR_PER_CUSTOMER                 # 1,000 customers today
new_customers = NEW_LOGO_ARR / ARR_PER_CUSTOMER            # 300 signed this year
customers_begin = customers_end - new_customers            # 700 a year ago (ignores logo churn count)

cac = SALES_MARKETING * 1e6 / new_customers                # $66,667 per new customer
annual_logo_churn = CHURNED_ARR / BEGIN_ARR                # 10% of ARR a year walks out
ltv = ARR_PER_CUSTOMER * 1e6 * GROSS_MARGIN / annual_logo_churn   # $456,000
ltv_to_cac = ltv / cac                                     # 6.8x

cac_payback_years = SALES_MARKETING / (gross_new_arr * GROSS_MARGIN)
cac_payback_months = cac_payback_years * 12                # 13.2 months

magic_number = net_new_arr / SALES_MARKETING               # 1.0x
burn_multiple = NET_BURN / net_new_arr                     # 0.25x
rule_of_40 = growth + fcf_margin                           # 40.0

print("# Block 2: Harborline unit economics (section 7, section 11)\n")
table(
    ["Input", "Value"],
    [
        ["Revenue this year", m(REVENUE)],
        ["Gross margin", pct(GROSS_MARGIN)],
        ["Gross profit", m(gross_profit)],
        ["Sales and marketing spend", m(SALES_MARKETING)],
        ["Net burn (cash out minus cash in)", m(NET_BURN)],
        ["ARR per customer", dollars(ARR_PER_CUSTOMER * 1e6)],
        ["Customers today", f"{customers_end:,.0f}"],
        ["New customers signed this year", f"{new_customers:,.0f}"],
    ],
)

table(
    ["Metric", "Value", "Arithmetic"],
    [
        ["CAC (cost to win one customer)", dollars(cac), "$20.0M divided by 300 new customers"],
        ["CAC payback", f"{cac_payback_months:.1f} months", "$20.0M divided by ($24.0M times 76%), times 12"],
        ["LTV (lifetime gross profit per customer)", dollars(ltv), "$60,000 times 76%, divided by 10% churn"],
        ["LTV to CAC", mult(ltv_to_cac), f"{dollars(ltv)} divided by {dollars(cac)}"],
        ["Magic number", mult(magic_number, 2), "$20.0M net new ARR divided by $20.0M S&M"],
        ["Burn multiple", mult(burn_multiple, 2), "$5.0M net burn divided by $20.0M net new ARR"],
        ["Free cash flow margin", pct(fcf_margin), "negative $5.0M divided by $50.0M"],
        ["Rule of 40 score", f"{rule_of_40 * 100:.0f}", "50.0% growth plus (10.0%) margin"],
    ],
)

# --------------------------------------------------------------------------------------
# Block 3: the deal and the cap table
# --------------------------------------------------------------------------------------
INVESTMENT = 100.0
POST_MONEY = 600.0
pre_money = POST_MONEY - INVESTMENT                         # 500.0
ownership = INVESTMENT / POST_MONEY                         # 16.667%
entry_ev_to_arr = POST_MONEY / END_ARR                      # 10.0x (no debt, cash ignored)
PRE_SHARES = 50_000_000
price_per_share = pre_money * 1e6 / PRE_SHARES              # $10.00
new_shares = INVESTMENT * 1e6 / price_per_share             # 10,000,000
post_shares = PRE_SHARES + new_shares                       # 60,000,000

assert abs(new_shares / post_shares - ownership) < 1e-12

# who owned what before the round (fully diluted, including the option pool)
pre_cap = [("Founders", 0.60), ("Earlier venture investors", 0.30), ("Employee option pool", 0.10)]

print("# Block 3: the proposed round (section 9, section 11)\n")
table(
    ["Term", "Value", "Arithmetic"],
    [
        ["New money in", m(INVESTMENT), "given"],
        ["Post-money valuation", m(POST_MONEY), "given (10.0x ending ARR)"],
        ["Pre-money valuation", m(pre_money), "600.0 minus 100.0"],
        ["Ownership bought", pct(ownership, 2), "100.0 divided by 600.0"],
        ["Entry EV to ARR", mult(entry_ev_to_arr), "600.0 divided by 60.0"],
        ["Shares before the round", f"{PRE_SHARES:,}", "given"],
        ["Price per share", f"${price_per_share:.2f}", "$500.0M divided by 50,000,000"],
        ["New shares issued", f"{new_shares:,.0f}", "$100.0M divided by $10.00"],
        ["Shares after the round", f"{post_shares:,.0f}", "50,000,000 plus 10,000,000"],
    ],
)

print("## Cap table before and after\n")
rows = []
for name, stake in pre_cap:
    sh = stake * PRE_SHARES
    rows.append([name, f"{sh:,.0f}", pct(stake), f"{sh:,.0f}", pct(sh / post_shares, 2)])
rows.append(["New growth investor (Series C preferred)", "0", "0.0%", f"{new_shares:,.0f}", pct(new_shares / post_shares, 2)])
rows.append(["Total", f"{PRE_SHARES:,}", "100.0%", f"{post_shares:,.0f}", "100.00%"])
table(["Holder", "Shares before", "% before", "Shares after", "% after"], rows)
founders_after = 0.60 * PRE_SHARES / post_shares
print(f"Founders' stake falls from 60.0% to {founders_after*100:.2f}%: 60.0% times (500 divided by 600).\n")

# --------------------------------------------------------------------------------------
# Block 4: three exits, with and without the preference
# --------------------------------------------------------------------------------------
HOLD_YEARS = 5
PREF_MULTIPLE = 1.0
pref_amount = INVESTMENT * PREF_MULTIPLE                    # 100.0

scenarios = [
    # name, ARR in year 5, exit EV to ARR multiple
    ("Bear", 90.0, 3.0),
    ("Base", 240.0, 7.0),
    ("Bull", 360.0, 9.0),
]


def irr(moic, years=HOLD_YEARS):
    """Annual return that turns 1.0 into `moic` over `years` with one cash in and one out."""
    return moic ** (1.0 / years) - 1.0


print("# Block 4: exit scenarios five years out (section 11, section 9)\n")
print("## Scenario inputs and equity value at exit\n")
rows = []
results = {}
for name, arr5, mult5 in scenarios:
    cagr = (arr5 / END_ARR) ** (1.0 / HOLD_YEARS) - 1.0
    equity = arr5 * mult5
    results[name] = {"arr5": arr5, "mult5": mult5, "cagr": cagr, "equity": equity}
    rows.append([name, m(arr5), pct(cagr), mult(mult5), m(equity), m(equity * ownership)])
table(["Scenario", "ARR in year 5", "ARR CAGR from $60.0M", "Exit EV to ARR", "Equity value at exit", "Our 16.67% as common"], rows)

print("## Payout to the preferred, three ways\n")
rows = []
for name, r in results.items():
    equity = r["equity"]
    as_common = equity * ownership                          # convert and take our share
    non_part = max(pref_amount, as_common)                  # take the bigger of the two
    if equity < pref_amount:
        non_part = equity                                   # can't get more than exists
    # participating: take the preference first, then share in what is left as if converted
    participating = min(pref_amount, equity) + max(equity - pref_amount, 0.0) * ownership
    r.update({"as_common": as_common, "non_part": non_part, "participating": participating})
    chosen = "preference" if pref_amount > as_common else "convert to common"
    rows.append([name, m(equity), m(as_common), m(pref_amount), m(non_part), chosen, m(participating)])
table(
    ["Scenario", "Equity value", "As common (no preference)", "1x preference amount",
     "1x non-participating payout", "Which the investor picks", "1x participating payout"],
    rows,
)

print("## MOIC and IRR on the $100.0M\n")
rows = []
for name, r in results.items():
    rows.append([
        name,
        mult(r["as_common"] / INVESTMENT, 2), pct(irr(r["as_common"] / INVESTMENT)),
        mult(r["non_part"] / INVESTMENT, 2), pct(irr(r["non_part"] / INVESTMENT)),
        mult(r["participating"] / INVESTMENT, 2), pct(irr(r["participating"] / INVESTMENT)),
    ])
table(
    ["Scenario", "MOIC as common", "IRR as common", "MOIC with 1x non-participating",
     "IRR with 1x non-participating", "MOIC with 1x participating", "IRR with 1x participating"],
    rows,
)

print("## What the common holders get in each scenario (non-participating preferred)\n")
rows = []
for name, r in results.items():
    to_common = r["equity"] - r["non_part"]
    rows.append([name, m(r["equity"]), m(r["non_part"]), m(to_common), pct(to_common / r["equity"])])
table(["Scenario", "Equity value", "To preferred", "To founders, VCs and employees", "Their share"], rows)

print("## The IRR arithmetic, written out (Base case, non-participating)\n")
base = results["Base"]
print(f"Money back: {m(base['non_part'])} on {m(INVESTMENT)} in, so MOIC is {base['non_part']/INVESTMENT:.2f}x.")
print(f"IRR: {base['non_part']/INVESTMENT:.2f} to the power of (1 divided by 5) is {(base['non_part']/INVESTMENT)**0.2:.4f}, minus 1 is {pct(irr(base['non_part']/INVESTMENT))}.")
print(f"Check: {m(INVESTMENT)} growing at {pct(irr(base['non_part']/INVESTMENT))} a year for 5 years is {m(INVESTMENT*(1+irr(base['non_part']/INVESTMENT))**5)}.")
bull = results["Bull"]
bear = results["Bear"]
print(f"Bull: {bull['non_part']/INVESTMENT:.2f} to the power of one fifth is {(bull['non_part']/INVESTMENT)**0.2:.3f}, so IRR is {pct(irr(bull['non_part']/INVESTMENT))}.")
print(f"Bear as common: {bear['as_common']/INVESTMENT:.2f} to the power of one fifth is {(bear['as_common']/INVESTMENT)**0.2:.3f}, minus 1 is {pct(irr(bear['as_common']/INVESTMENT))}.")
print(f"Bear preference adds {m(bear['non_part'] - bear['as_common'])} over the as-common payout.")
print(f"Participating minus non-participating in the Base case: {m(base['participating'] - base['non_part'])}.\n")

print("## Price sensitivity: the same deal at a $500.0M post-money (section 11, step 6)\n")
ALT_POST = 500.0
alt_ownership = INVESTMENT / ALT_POST                        # 20.0%
alt_base_payout = max(pref_amount, base["equity"] * alt_ownership)
table(
    ["Item", "At $600.0M post", "At $500.0M post"],
    [
        ["Ownership", pct(ownership, 2), pct(alt_ownership, 2)],
        ["Base case payout (converts)", m(base["non_part"]), m(alt_base_payout)],
        ["Base case MOIC", mult(base["non_part"] / INVESTMENT, 2), mult(alt_base_payout / INVESTMENT, 2)],
        ["Base case IRR", pct(irr(base["non_part"] / INVESTMENT)), pct(irr(alt_base_payout / INVESTMENT))],
    ],
)
assert abs(alt_base_payout - 336.0) < 1e-9

# --------------------------------------------------------------------------------------
# Block 5: valuation question numbers
# --------------------------------------------------------------------------------------
growth_adjusted = entry_ev_to_arr / (growth * 100)          # 10.0x divided by 50 = 0.20x
public_median_ev_ntm = 4.0        # Clouded Judgement, September 11, 2026 (tagged in the article)
public_high_growth_ev_ntm = 17.1  # same source, companies projected to grow over 22%
public_median_growth = 0.13       # same source

print("# Block 5: valuation question numbers (section 8)\n")
table(
    ["Item", "Value", "Arithmetic or source"],
    [
        ["Harborline entry EV to ARR", mult(entry_ev_to_arr), "600.0 divided by 60.0"],
        ["Harborline ARR growth", pct(growth), "from the ARR bridge in section 7"],
        ["Growth-adjusted multiple", mult(growth_adjusted, 2), "10.0 divided by 50"],
        ["Public software median EV to NTM revenue", mult(public_median_ev_ntm), "Clouded Judgement, Sep 11, 2026"],
        ["Public high-growth bucket (over 22% growth)", mult(public_high_growth_ev_ntm), "same source"],
        ["Public median NTM growth", pct(public_median_growth, 0), "same source"],
        ["Public median growth-adjusted multiple", mult(public_median_ev_ntm / (public_median_growth * 100), 2), "4.0 divided by 13"],
    ],
)

# --------------------------------------------------------------------------------------
# Sanity checks the article relies on
# --------------------------------------------------------------------------------------
assert abs(growth - 0.50) < 1e-9
assert abs(gross_retention - 0.90) < 1e-9
assert abs(net_retention - 1.05) < 1e-9
assert abs(rule_of_40 - 0.40) < 1e-9
assert abs(burn_multiple - 0.25) < 1e-9
assert abs(magic_number - 1.0) < 1e-9
assert abs(ownership - 1 / 6) < 1e-12
assert abs(results["Bear"]["non_part"] - 100.0) < 1e-9          # preference binds in the Bear case
assert abs(results["Base"]["non_part"] - 280.0) < 1e-9          # converts in Base
assert abs(results["Bull"]["non_part"] - 540.0) < 1e-9          # converts in Bull
print("All checks passed.")
