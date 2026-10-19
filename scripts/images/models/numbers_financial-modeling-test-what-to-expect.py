#!/usr/bin/env python3
"""Numbers for the WSG article "Financial Modeling Test: What to Expect and How to Practice"
(October 5, 2026), section 5: a two-hour DCF-based modeling test on Torvik Flow Systems, a
fictional mid-cap industrial with three segments (Pumps; Valves and Controls; Aftermarket Parts
and Service). Every company, peer, number and label here is invented for the article.

Plain Python, no dependencies. Run from the repo root:
    python3 scripts/images/models/numbers_financial-modeling-test-what-to-expect.py

It prints every table the article shows, in build order, each one headed by a comment naming
the table and the article section it sits in. The image agent rebuilds the workbook from these
inputs; the tables below are the targets its recalculated cells must match.

Layout the workbook follows (tabs): Cover (scenario switch), Inputs (historicals, segment build,
assumptions block), Schedules (working capital by days, PP&E roll-forward), Cost of debt, Beta,
WACC, DCF, Sensitivity. $ millions except per-share data. Fiscal year ends December 31.
Valuation date December 31, 2025 (the last fiscal year end), mid-year convention on the
projected cash flows, terminal value discounted from the end of FY2030.

Rounding: the model carries full precision; tables display one decimal (percentages one
decimal, share prices two decimals). Re-adding a displayed column by hand can land 0.1 off.
"""

# ----------------------------------------------------------------------------- helpers
from decimal import Decimal, ROUND_HALF_UP

HIST = ["2023A", "2024A", "2025A"]
PROJ = ["2026E", "2027E", "2028E", "2029E", "2030E"]
ALL = HIST + PROJ


def rnd(x, d):
    """Round half away from zero on the 15-digit decimal value, the way Excel displays a cell."""
    q = Decimal(1).scaleb(-d)
    return float(Decimal(repr(round(x, 12))).quantize(q, rounding=ROUND_HALF_UP))


def f1(x):
    """One decimal, parentheses for negatives, as the workbook displays."""
    if x is None:
        return ""
    r = rnd(x, 1)
    return f"({abs(r):,.1f})" if r < 0 else f"{r:,.1f}"


def pct(x, d=1):
    """Percent, parentheses for negatives (never a bare hyphen as a minus sign)."""
    r = rnd(x * 100, d)
    return f"({abs(r):.{d}f}%)" if r < 0 else f"{r:.{d}f}%"


def money2(x):
    r = rnd(x, 2)
    return f"(${abs(r):,.2f})" if r < 0 else f"${r:,.2f}"


def table(title, header, rows, note=None):
    """Print a pipe table the article can paste. rows: list of (label, [cells...])."""
    print()
    print(f"### {title}")
    print()
    print("| " + " | ".join(header) + " |")
    print("|" + "|".join(["---"] * len(header)) + "|")
    for label, cells in rows:
        print("| " + " | ".join([label] + [str(c) for c in cells]) + " |")
    if note:
        print()
        print(note)


# ============================================================================= INPUTS
# --- Table 1 (section 5, step 1): historical income statement from the case pack, $ millions
seg_hist = {
    "Pumps": [530.0, 548.0, 570.0],
    "Valves and Controls": [385.0, 406.0, 430.0],
    "Aftermarket Parts and Service": [295.0, 322.0, 350.0],
}
revenue_h = [sum(seg_hist[s][i] for s in seg_hist) for i in range(3)]   # 1,210 / 1,276 / 1,350
cogs_h = [-810.0, -845.0, -884.0]
sga_h = [-250.0, -260.0, -270.0]
interest_h = [-24.0, -24.0, -24.0]          # $400m of debt at about 6 percent
TAX_RATE = 0.25                             # effective rate, historical and projected
da_h = [40.0, 42.0, 44.0]                   # from the cash flow statement
capex_h = [48.0, 50.0, 54.0]                # from the cash flow statement
basic_shares = 58.5
diluted_shares = 60.0

gp_h = [revenue_h[i] + cogs_h[i] for i in range(3)]
ebit_h = [gp_h[i] + sga_h[i] for i in range(3)]
ebt_h = [ebit_h[i] + interest_h[i] for i in range(3)]
tax_h = [-ebt_h[i] * TAX_RATE for i in range(3)]
ni_h = [ebt_h[i] + tax_h[i] for i in range(3)]
eps_h = [ni_h[i] / diluted_shares for i in range(3)]
ebitda_h = [ebit_h[i] + da_h[i] for i in range(3)]

# ============================================================================= SEGMENTS
# --- Table 2 (section 5, step 2): segment revenue build, historical growth and mix
seg_growth_h = {s: [None] + [seg_hist[s][i] / seg_hist[s][i - 1] - 1 for i in (1, 2)] for s in seg_hist}
seg_mix_h = {s: [seg_hist[s][i] / revenue_h[i] for i in range(3)] for s in seg_hist}
rev_growth_h = [None, revenue_h[1] / revenue_h[0] - 1, revenue_h[2] / revenue_h[1] - 1]

# ============================================================================= ASSUMPTIONS
# --- Table 3 (section 5, step 3): the scenario block. Three rows per driver; the switch picks one.
SCEN = {
    "Bear": {
        "Pumps": [0.01, 0.00, 0.01, 0.02, 0.02],
        "Valves and Controls": [0.02, 0.01, 0.02, 0.03, 0.03],
        "Aftermarket Parts and Service": [0.05, 0.04, 0.04, 0.04, 0.04],
        "gm": [0.340, 0.340, 0.340, 0.340, 0.340],
        "sga": [0.205, 0.205, 0.205, 0.205, 0.205],
    },
    "Base": {
        "Pumps": [0.04, 0.04, 0.035, 0.035, 0.03],
        "Valves and Controls": [0.06, 0.055, 0.05, 0.045, 0.04],
        "Aftermarket Parts and Service": [0.08, 0.075, 0.07, 0.06, 0.05],
        "gm": [0.348, 0.350, 0.352, 0.354, 0.355],
        "sga": [0.200, 0.199, 0.198, 0.198, 0.198],
    },
    "Bull": {
        "Pumps": [0.06, 0.06, 0.05, 0.05, 0.04],
        "Valves and Controls": [0.08, 0.08, 0.07, 0.06, 0.05],
        "Aftermarket Parts and Service": [0.10, 0.10, 0.09, 0.08, 0.07],
        "gm": [0.350, 0.355, 0.360, 0.365, 0.365],
        "sga": [0.195, 0.194, 0.193, 0.192, 0.192],
    },
}
# Drivers that do not change with the scenario (the pack gives them; a test rarely flexes them)
DA_PCT = 0.033       # D&A as a percent of revenue (2025A: 44 / 1,350 = 3.3 percent)
CAPEX_PCT = 0.040    # capex as a percent of revenue (2025A: 54 / 1,350 = 4.0 percent)
DSO, DIO, DPO = 60.0, 90.0, 45.0            # days of revenue, days of cost of sales
ACCRUED_PCT = 0.04   # accrued liabilities as a percent of revenue
DEFREV_PCT = 0.02    # deferred revenue as a percent of revenue
DAYS = 365.0

# ============================================================================= WORKING CAPITAL
# --- Table 5 (section 5, step 5): historical balances at each fiscal year end, $ millions.
# 2022A ending balances are the opening balances for the 2023A change.
wc_hist = {  # 2022A, 2023A, 2024A, 2025A
    "Accounts receivable": [190.0, 199.0, 210.0, 222.0],
    "Inventory": [195.0, 200.0, 208.0, 218.0],
    "Accounts payable": [97.0, 100.0, 104.0, 109.0],
    "Accrued liabilities": [46.0, 48.0, 51.0, 54.0],
    "Deferred revenue": [23.0, 24.0, 26.0, 27.0],
}
# --- PP&E (section 5, step 6): 2022A ending net PP&E, then beginning + capex minus D&A
PPE_2022 = 384.0

# ============================================================================= CAPITAL STRUCTURE
# --- Cost of debt (section 5, step 7)
TRANCHES = [("Term loan B", 250.0, 0.0575), ("Senior notes", 150.0, 0.0650)]
CASH = 95.0
NCI = 10.0                      # noncontrolling interest
PRICE = 38.00                   # share price on the valuation date, $
# --- Beta (section 5, step 8): fictional peers, labeled as such in the article
PEERS = [  # name, levered beta, debt, equity market value, tax rate
    ("Peer A (large-cap pumps)", 1.20, 600.0, 3000.0, 0.25),
    ("Peer B (valves)", 1.05, 300.0, 2500.0, 0.25),
    ("Peer C (industrial controls)", 1.35, 1200.0, 4000.0, 0.25),
    ("Peer D (flow equipment, small cap)", 0.95, 200.0, 1800.0, 0.25),
    ("Peer E (fluid handling)", 1.15, 900.0, 3600.0, 0.25),
]
# --- WACC (section 5, step 9): the pack gives these two
RISK_FREE = 0.045
ERP = 0.050
# --- Terminal value (section 5, step 11)
EXIT_MULTIPLE = 9.5
TERMINAL_G = 0.025              # Gordon growth cross-check
# --- Sensitivity (section 5, step 12)
WACC_STEP = 0.005
MULT_STEP = 0.5


# ============================================================================= THE MODEL
def run(scenario):
    """Build the projection and the DCF for one scenario. Returns a dict of every line."""
    S = SCEN[scenario]
    m = {}
    # Segment revenue
    seg = {s: list(seg_hist[s]) for s in seg_hist}
    for s in seg_hist:
        for y in range(5):
            seg[s].append(seg[s][-1] * (1 + S[s][y]))
    revenue = [sum(seg[s][i] for s in seg) for i in range(8)]
    gm = [gp_h[i] / revenue_h[i] for i in range(3)] + S["gm"]
    sga_pct = [-sga_h[i] / revenue_h[i] for i in range(3)] + S["sga"]
    cogs = list(cogs_h) + [-revenue[i] * (1 - gm[i]) for i in range(3, 8)]
    gp = [revenue[i] + cogs[i] for i in range(8)]
    sga = list(sga_h) + [-revenue[i] * sga_pct[i] for i in range(3, 8)]
    ebit = [gp[i] + sga[i] for i in range(8)]
    da = list(da_h) + [revenue[i] * DA_PCT for i in range(3, 8)]
    ebitda = [ebit[i] + da[i] for i in range(8)]
    capex = list(capex_h) + [revenue[i] * CAPEX_PCT for i in range(3, 8)]
    # Working capital: balances 2022A..2030E (index 0 = 2022A)
    ar = list(wc_hist["Accounts receivable"]) + [revenue[i] * DSO / DAYS for i in range(3, 8)]
    inv = list(wc_hist["Inventory"]) + [-cogs[i] * DIO / DAYS for i in range(3, 8)]
    ap = list(wc_hist["Accounts payable"]) + [-cogs[i] * DPO / DAYS for i in range(3, 8)]
    accr = list(wc_hist["Accrued liabilities"]) + [revenue[i] * ACCRUED_PCT for i in range(3, 8)]
    defrev = list(wc_hist["Deferred revenue"]) + [revenue[i] * DEFREV_PCT for i in range(3, 8)]
    nwc = [ar[i] + inv[i] - ap[i] - accr[i] - defrev[i] for i in range(9)]
    d_nwc = [nwc[i] - nwc[i - 1] for i in range(1, 9)]          # 2023A..2030E, increase = use of cash
    # Days implied by the historical balances (for the table)
    dso_h = [ar[i + 1] / revenue[i] * DAYS for i in range(3)]
    dio_h = [inv[i + 1] / -cogs[i] * DAYS for i in range(3)]
    dpo_h = [ap[i + 1] / -cogs[i] * DAYS for i in range(3)]
    # PP&E roll-forward 2023A..2030E
    ppe_beg, ppe_end = [], []
    b = PPE_2022
    for i in range(8):
        ppe_beg.append(b)
        e = b + capex[i] - da[i]
        ppe_end.append(e)
        b = e
    # Unlevered free cash flow
    tax_on_ebit = [-ebit[i] * TAX_RATE for i in range(8)]
    nopat = [ebit[i] + tax_on_ebit[i] for i in range(8)]
    ufcf = [nopat[i] + da[i] - capex[i] - d_nwc[i] for i in range(8)]
    m.update(seg=seg, revenue=revenue, gm=gm, sga_pct=sga_pct, cogs=cogs, gp=gp, sga=sga, ebit=ebit,
             da=da, ebitda=ebitda, capex=capex, ar=ar, inv=inv, ap=ap, accr=accr, defrev=defrev,
             nwc=nwc, d_nwc=d_nwc, dso_h=dso_h, dio_h=dio_h, dpo_h=dpo_h, ppe_beg=ppe_beg,
             ppe_end=ppe_end, tax_on_ebit=tax_on_ebit, nopat=nopat, ufcf=ufcf)
    return m


# ---- Capital structure pieces shared by every scenario
total_debt = sum(t[1] for t in TRANCHES)
pretax_kd = sum(t[1] * t[2] for t in TRANCHES) / total_debt
aftertax_kd = pretax_kd * (1 - TAX_RATE)
market_cap = PRICE * diluted_shares
ev_now = market_cap + total_debt - CASH + NCI
net_debt = total_debt - CASH
unlevered = []
for name, beta, d, e, t in PEERS:
    unlevered.append(beta / (1 + (1 - t) * d / e))
u_sorted = sorted(unlevered)
median_unlev = u_sorted[len(u_sorted) // 2]
mean_unlev = sum(unlevered) / len(unlevered)
de_subject = total_debt / market_cap
relevered = median_unlev * (1 + (1 - TAX_RATE) * de_subject)
cost_equity = RISK_FREE + relevered * ERP
w_e = market_cap / (market_cap + total_debt)
w_d = total_debt / (market_cap + total_debt)
WACC = w_e * cost_equity + w_d * aftertax_kd


def value(m, wacc=WACC, mult=EXIT_MULTIPLE, midyear=True):
    """Discount the projected UFCF and the terminal value. Returns a dict."""
    ufcf = m["ufcf"][3:]
    periods = [i + 1 for i in range(5)]                      # 1.0 .. 5.0 from the valuation date
    disc_period = [p - 0.5 for p in periods] if midyear else periods
    dfac = [1 / (1 + wacc) ** p for p in disc_period]
    pv = [ufcf[i] * dfac[i] for i in range(5)]
    tv = m["ebitda"][-1] * mult                               # sale at the end of FY2030
    tv_df = 1 / (1 + wacc) ** 5.0
    pv_tv = tv * tv_df
    ev = sum(pv) + pv_tv
    equity = ev - net_debt - NCI
    px = equity / diluted_shares
    # Gordon growth cross-check (end-of-year form, so it matches the exit-multiple timing)
    implied_g = (tv * wacc - ufcf[-1]) / (tv + ufcf[-1])
    tv_gordon = ufcf[-1] * (1 + TERMINAL_G) / (wacc - TERMINAL_G)
    implied_mult = tv_gordon / m["ebitda"][-1]
    ev_gordon = sum(pv) + tv_gordon * tv_df
    px_gordon = (ev_gordon - net_debt - NCI) / diluted_shares
    return dict(periods=periods, disc_period=disc_period, dfac=dfac, pv=pv, tv=tv, tv_df=tv_df,
                pv_tv=pv_tv, sum_pv=sum(pv), ev=ev, equity=equity, px=px, implied_g=implied_g,
                tv_gordon=tv_gordon, implied_mult=implied_mult, ev_gordon=ev_gordon,
                px_gordon=px_gordon, tv_share=pv_tv / ev)


base = run("Base")
V = value(base)

# ============================================================================= PRINT
print("TORVIK FLOW SYSTEMS (fictional): two-hour DCF modeling test, $ millions except per share")
print("Valuation date December 31, 2025. Scenario switch: Base. Mid-year convention on projected UFCF.")

# ---------- Table 1: historical income statement (section 5, step 1 "Inputs: the historicals")
rows = [
    ("Revenue", [f1(x) for x in revenue_h]),
    ("Cost of sales", [f1(x) for x in cogs_h]),
    ("Gross profit", [f1(x) for x in gp_h]),
    ("SG&A", [f1(x) for x in sga_h]),
    ("EBIT", [f1(x) for x in ebit_h]),
    ("Interest expense", [f1(x) for x in interest_h]),
    ("Pretax income", [f1(x) for x in ebt_h]),
    ("Taxes", [f1(x) for x in tax_h]),
    ("Net income", [f1(x) for x in ni_h]),
    ("Diluted shares (millions)", [f1(diluted_shares)] * 3),
    ("Diluted EPS ($)", [money2(x) for x in eps_h]),
    ("Revenue growth", ["" if g is None else pct(g) for g in rev_growth_h]),
    ("Gross margin", [pct(gp_h[i] / revenue_h[i]) for i in range(3)]),
    ("SG&A as a percent of revenue", [pct(-sga_h[i] / revenue_h[i]) for i in range(3)]),
    ("EBIT margin", [pct(ebit_h[i] / revenue_h[i]) for i in range(3)]),
    ("Effective tax rate", [pct(-tax_h[i] / ebt_h[i]) for i in range(3)]),
    ("D&A (from the cash flow statement)", [f1(x) for x in da_h]),
    ("EBITDA", [f1(x) for x in ebitda_h]),
    ("EBITDA margin", [pct(ebitda_h[i] / revenue_h[i]) for i in range(3)]),
    ("Capex (from the cash flow statement)", [f1(x) for x in capex_h]),
]
table("Table 1. Historical income statement and ratios (Inputs tab)", ["$ millions"] + HIST, rows)

# ---------- Table 2: segment build (section 5, step 2)
rows = []
for s in seg_hist:
    rows.append((s, [f1(x) for x in seg_hist[s]]))
rows.append(("Total revenue", [f1(x) for x in revenue_h]))
for s in seg_hist:
    rows.append((f"{s} growth", ["" if g is None else pct(g) for g in seg_growth_h[s]]))
for s in seg_hist:
    rows.append((f"{s} mix", [pct(x) for x in seg_mix_h[s]]))
table("Table 2. Segment revenue build, historical (Inputs tab)", ["$ millions"] + HIST, rows)

# ---------- Table 3: assumptions block (section 5, step 3)
rows = []
for s in seg_hist:
    for sc in ("Bear", "Base", "Bull"):
        rows.append((f"{s} growth, {sc}", [pct(x) for x in SCEN[sc][s]]))
for sc in ("Bear", "Base", "Bull"):
    rows.append((f"Gross margin, {sc}", [pct(x) for x in SCEN[sc]["gm"]]))
for sc in ("Bear", "Base", "Bull"):
    rows.append((f"SG&A as a percent of revenue, {sc}", [pct(x) for x in SCEN[sc]["sga"]]))
rows += [
    ("D&A as a percent of revenue (all cases)", [pct(DA_PCT)] * 5),
    ("Capex as a percent of revenue (all cases)", [pct(CAPEX_PCT)] * 5),
    ("Receivable days, DSO (all cases)", [f"{DSO:.0f}"] * 5),
    ("Inventory days, DIO (all cases)", [f"{DIO:.0f}"] * 5),
    ("Payable days, DPO (all cases)", [f"{DPO:.0f}"] * 5),
    ("Accrued liabilities as a percent of revenue", [pct(ACCRUED_PCT)] * 5),
    ("Deferred revenue as a percent of revenue", [pct(DEFREV_PCT)] * 5),
    ("Tax rate on EBIT (all cases)", [pct(TAX_RATE)] * 5),
]
table("Table 3. Assumptions block with the Bear / Base / Bull rows (Inputs tab; switch set to Base)",
      ["Driver"] + PROJ, rows)

# ---------- Table 4: projected segment revenue and income statement, Base (section 5, step 4)
rows = []
for s in seg_hist:
    rows.append((s, [f1(x) for x in base["seg"][s]]))
rows += [
    ("Total revenue", [f1(x) for x in base["revenue"]]),
    ("Revenue growth", [""] + [pct(base["revenue"][i] / base["revenue"][i - 1] - 1) for i in range(1, 8)]),
    ("Cost of sales", [f1(x) for x in base["cogs"]]),
    ("Gross profit", [f1(x) for x in base["gp"]]),
    ("Gross margin", [pct(x) for x in base["gm"]]),
    ("SG&A", [f1(x) for x in base["sga"]]),
    ("EBIT", [f1(x) for x in base["ebit"]]),
    ("EBIT margin", [pct(base["ebit"][i] / base["revenue"][i]) for i in range(8)]),
    ("D&A", [f1(x) for x in base["da"]]),
    ("EBITDA", [f1(x) for x in base["ebitda"]]),
    ("EBITDA margin", [pct(base["ebitda"][i] / base["revenue"][i]) for i in range(8)]),
    ("Capex", [f1(x) for x in base["capex"]]),
]
table("Table 4. Operating build, Base case (Inputs and DCF tabs)", ["$ millions"] + ALL, rows)

# ---------- Table 5: working capital schedule (section 5, step 5)
Y9 = ["2022A"] + ALL
rows = [
    ("Accounts receivable", [f1(x) for x in base["ar"]]),
    ("Inventory", [f1(x) for x in base["inv"]]),
    ("Accounts payable", [f1(x) for x in base["ap"]]),
    ("Accrued liabilities", [f1(x) for x in base["accr"]]),
    ("Deferred revenue", [f1(x) for x in base["defrev"]]),
    ("Net working capital", [f1(x) for x in base["nwc"]]),
    ("(Increase) / decrease in NWC", [""] + [f1(-x) for x in base["d_nwc"]]),
    ("DSO (days)", [""] + [f"{x:.1f}" for x in base["dso_h"]] + [f"{DSO:.1f}"] * 5),
    ("DIO (days)", [""] + [f"{x:.1f}" for x in base["dio_h"]] + [f"{DIO:.1f}"] * 5),
    ("DPO (days)", [""] + [f"{x:.1f}" for x in base["dpo_h"]] + [f"{DPO:.1f}"] * 5),
    ("NWC as a percent of revenue", [""] + [pct(base["nwc"][i + 1] / base["revenue"][i]) for i in range(8)]),
]
table("Table 5. Working capital schedule, Base case (Schedules tab)", ["$ millions"] + Y9, rows,
      note="Receivables are revenue times DSO over 365. Inventory and payables are cost of sales times "
           "DIO or DPO over 365. The (increase) / decrease line is the number that goes into free cash flow: "
           "when working capital grows, cash goes out, so the line is negative.")

# ---------- Table 6: PP&E roll-forward (section 5, step 6)
rows = [
    ("Beginning net PP&E", [f1(x) for x in base["ppe_beg"]]),
    ("Plus: capex", [f1(x) for x in base["capex"]]),
    ("Less: depreciation and amortization", [f1(-x) for x in base["da"]]),
    ("Ending net PP&E", [f1(x) for x in base["ppe_end"]]),
    ("Capex as a percent of revenue", [pct(base["capex"][i] / base["revenue"][i]) for i in range(8)]),
    ("D&A as a percent of revenue", [pct(base["da"][i] / base["revenue"][i]) for i in range(8)]),
]
table("Table 6. PP&E roll-forward, Base case (Schedules tab)", ["$ millions"] + ALL, rows)

# ---------- Table 7: cost of debt (section 5, step 7)
rows = []
for name, principal, rate in TRANCHES:
    rows.append((name, [f1(principal), pct(principal / total_debt), pct(rate, 2)]))
rows.append(("Total debt and weighted pre-tax cost", [f1(total_debt), pct(1.0), pct(pretax_kd, 2)]))
rows.append(("After-tax cost of debt at a 25% tax rate", ["", "", pct(aftertax_kd, 2)]))
table("Table 7. Cost of debt (Cost of debt tab)", ["Tranche", "Principal", "Weight", "Rate"], rows)

# ---------- Table 8: beta (section 5, step 8)
rows = []
for (name, beta, d, e, t), u in zip(PEERS, unlevered):
    rows.append((name, [f"{beta:.2f}", f1(d), f1(e), f"{rnd(d / e, 2):.2f}", pct(t, 0), f"{rnd(u, 3):.3f}"]))
rows.append(("Median unlevered beta", ["", "", "", "", "", f"{rnd(median_unlev, 3):.3f}"]))
rows.append(("Mean unlevered beta (for reference)", ["", "", "", "", "", f"{rnd(mean_unlev, 3):.3f}"]))
rows.append(("Torvik debt to equity (400.0 / market cap)", ["", f1(total_debt), f1(market_cap), f"{rnd(de_subject, 3):.3f}", pct(TAX_RATE, 0), ""]))
rows.append(("Torvik relevered beta", ["", "", "", "", "", f"{rnd(relevered, 3):.3f}"]))
table("Table 8. Peer betas, unlevered and relevered (Beta tab; peers are fictional)",
      ["Company", "Levered beta", "Debt", "Equity value", "D / E", "Tax rate", "Unlevered beta"], rows,
      note="Unlevered beta = levered beta divided by (1 + (1 minus tax rate) times debt over equity). "
           "Relevered beta = median unlevered beta times (1 + (1 minus tax rate) times Torvik's debt over equity).")

# ---------- Table 9: WACC (section 5, step 9)
rows = [
    ("Risk-free rate (from the pack)", [pct(RISK_FREE, 2)]),
    ("Equity risk premium (from the pack)", [pct(ERP, 2)]),
    ("Relevered beta", [f"{rnd(relevered, 3):.3f}"]),
    ("Cost of equity = risk-free + beta times ERP", [pct(cost_equity, 2)]),
    ("Pre-tax cost of debt", [pct(pretax_kd, 2)]),
    ("After-tax cost of debt", [pct(aftertax_kd, 2)]),
    ("Share price on the valuation date ($)", [money2(PRICE)]),
    ("Diluted shares (millions)", [f1(diluted_shares)]),
    ("Equity value (market cap)", [f1(market_cap)]),
    ("Total debt", [f1(total_debt)]),
    ("Equity weight", [pct(w_e)]),
    ("Debt weight", [pct(w_d)]),
    ("WACC", [pct(WACC, 2)]),
]
table("Table 9. WACC (WACC tab)", ["Line", "Value"], rows)

# ---------- Table 10: unlevered free cash flow and present values (section 5, step 10)
rows = [
    ("EBIT", [f1(x) for x in base["ebit"]]),
    ("Less: taxes on EBIT at 25%", [f1(x) for x in base["tax_on_ebit"]]),
    ("NOPAT", [f1(x) for x in base["nopat"]]),
    ("Plus: D&A", [f1(x) for x in base["da"]]),
    ("Less: capex", [f1(-x) for x in base["capex"]]),
    ("Less: increase in NWC", [f1(-x) for x in base["d_nwc"]]),
    ("Unlevered free cash flow", [f1(x) for x in base["ufcf"]]),
    ("Year fraction from the valuation date", ["", "", ""] + [f"{1.0:.2f}"] * 5),
    ("Discount period (mid-year)", ["", "", ""] + [f"{p:.2f}" for p in V["disc_period"]]),
    (f"Discount factor at {pct(WACC, 2)} WACC", ["", "", ""] + [f"{rnd(d, 4):.4f}" for d in V["dfac"]]),
    ("Present value of UFCF", ["", "", ""] + [f1(x) for x in V["pv"]]),
]
table("Table 10. Unlevered free cash flow and present value, Base case (DCF tab)", ["$ millions"] + ALL, rows,
      note="Mid-year convention: a year's cash comes in across the year, so it is discounted as if it "
           "arrived at the midpoint (0.5, 1.5, 2.5, 3.5, 4.5 years out). The year fraction is 1.00 "
           "because the valuation date is the fiscal year end; a mid-year valuation date would make the "
           "first fraction smaller and the first cash flow a stub.")

# ---------- Table 11: terminal value and the bridge (section 5, step 11)
V_eoy = value(base, midyear=False)
rows = [
    ("Sum of present values, FY2026E to FY2030E", [f1(V["sum_pv"])]),
    (f"FY2030E EBITDA", [f1(base["ebitda"][-1])]),
    (f"Exit multiple", [f"{EXIT_MULTIPLE:.1f}x"]),
    ("Terminal value at the end of FY2030", [f1(V["tv"])]),
    ("Discount factor, 5.0 years", [f"{rnd(V['tv_df'], 4):.4f}"]),
    ("Present value of terminal value", [f1(V["pv_tv"])]),
    ("Enterprise value", [f1(V["ev"])]),
    ("Terminal value as a share of enterprise value", [pct(V["tv_share"])]),
    ("Less: total debt", [f1(-total_debt)]),
    ("Plus: cash", [f1(CASH)]),
    ("Less: noncontrolling interest", [f1(-NCI)]),
    ("Equity value", [f1(V["equity"])]),
    ("Diluted shares (millions)", [f1(diluted_shares)]),
    ("Implied share price ($)", [money2(V["px"])]),
    ("Current share price ($)", [money2(PRICE)]),
    ("Implied upside / (downside)", [pct(V["px"] / PRICE - 1)]),
    ("Implied share price with end-of-year discounting ($)", [money2(V_eoy["px"])]),
    ("Gordon growth cross-check: implied perpetual growth in the 9.5x multiple", [pct(V["implied_g"], 2)]),
    (f"Gordon growth cross-check: terminal value at {pct(TERMINAL_G)} growth", [f1(V["tv_gordon"])]),
    ("Gordon growth cross-check: implied exit multiple", [f"{rnd(V['implied_mult'], 1):.1f}x"]),
    (f"Gordon growth cross-check: implied share price at {pct(TERMINAL_G)} growth ($)", [money2(V["px_gordon"])]),
    ("Current EV / LTM EBITDA (market, for reference)", [f"{rnd(ev_now / ebitda_h[-1], 1):.1f}x"]),
]
table("Table 11. Terminal value, enterprise value to equity value to share price, Base case (DCF tab)",
      ["Line", "Value"], rows,
      note="Implied growth = (terminal value times WACC minus final-year UFCF) divided by (terminal value "
           "plus final-year UFCF). Gordon terminal value = final-year UFCF times (1 + g) divided by (WACC minus g).")

# ---------- Table 12: sensitivity grid (section 5, step 12)
waccs = [WACC + k * WACC_STEP for k in (-2, -1, 0, 1, 2)]
mults = [EXIT_MULTIPLE + k * MULT_STEP for k in (-2, -1, 0, 1, 2)]
rows = []
for w in waccs:
    rows.append((pct(w, 2), [money2(value(base, wacc=w, mult=mu)["px"]) for mu in mults]))
table("Table 12. Sensitivity: implied share price, WACC (down) versus exit multiple (across), Base case (Sensitivity tab)",
      ["WACC (down) / exit multiple (across)"] + [f"{mu:.1f}x" for mu in mults], rows,
      note="Step sizes: 0.50% on WACC, 0.5x on the multiple. The center cell is the base case.")

# ---------- Table 13: scenario summary (section 5, the switch)
rows = []
for sc in ("Bear", "Base", "Bull"):
    m = run(sc)
    v = value(m)
    rows.append((sc, [f1(m["revenue"][-1]), pct(m["ebitda"][-1] / m["revenue"][-1]), f1(m["ebitda"][-1]),
                      f1(m["ufcf"][-1]), f1(v["ev"]), money2(v["px"]), pct(v["px"] / PRICE - 1)]))
table("Table 13. Flipping the scenario switch (Cover tab cell; everything else unchanged)",
      ["Scenario", "FY2030E revenue", "FY2030E EBITDA margin", "FY2030E EBITDA", "FY2030E UFCF",
       "Enterprise value", "Implied share price", "vs $38.00"], rows)

# ============================================================================= CHECKS
# The checks a grader would run, and the ties the article quotes in prose.
assert abs(revenue_h[2] - 1350.0) < 1e-9
assert abs(base["ppe_end"][2] - 410.0) < 1e-9, base["ppe_end"][2]        # 2025A ending PP&E
assert abs(base["nwc"][3] - 250.0) < 1e-9, base["nwc"][3]                # 2025A NWC
center = value(base, wacc=waccs[2], mult=mults[2])["px"]
assert abs(center - V["px"]) < 1e-9
for sc in ("Bear", "Base", "Bull"):
    m = run(sc)
    for i in range(8):
        assert abs(sum(m["seg"][s][i] for s in m["seg"]) - m["revenue"][i]) < 1e-9
        assert abs(m["ebit"][i] + m["da"][i] - m["ebitda"][i]) < 1e-9
print()
print("Prose figures the article quotes:")
print(f"  2025A EV = {market_cap:.1f} plus {total_debt:.1f} minus {CASH:.1f} plus {NCI:.1f} = {ev_now:.1f}; EV / LTM EBITDA {ev_now / ebitda_h[-1]:.2f}x")
print(f"  Net debt = {net_debt:.1f}")
print(f"  Base implied price {V['px']:.2f}; end-of-year discounting {V_eoy['px']:.2f}; "
      f"Gordon at {TERMINAL_G:.1%} {V['px_gordon']:.2f}")
print(f"  WACC components: Ke {cost_equity:.4%}, Kd after tax {aftertax_kd:.4%}, We {w_e:.4%}, Wd {w_d:.4%}, WACC {WACC:.4%}")
print(f"  Base 2030E UFCF {base['ufcf'][-1]:.2f}; TV {V['tv']:.1f}; PV TV {V['pv_tv']:.1f}; sum PV {V['sum_pv']:.1f}")
print(f"  Implied g {V['implied_g']:.4%}; Gordon TV {V['tv_gordon']:.1f}; implied multiple {V['implied_mult']:.2f}x")
# A deliberate error, for the mistakes section: forget to discount the terminal value
px_undiscounted_tv = (V["sum_pv"] + V["tv"] - net_debt - NCI) / diluted_shares
print(f"  Mistake check, terminal value left undiscounted: implied price {px_undiscounted_tv:.2f}")
# A deliberate error: working capital sign flipped (increase added instead of subtracted)
flipped = [base["nopat"][i] + base["da"][i] - base["capex"][i] + base["d_nwc"][i] for i in range(3, 8)]
pv_flipped = sum(flipped[i] * V["dfac"][i] for i in range(5))
px_flipped = (pv_flipped + V["pv_tv"] - net_debt - NCI) / diluted_shares
print(f"  Mistake check, NWC sign flipped: implied price {px_flipped:.2f}")
# A deliberate error: tax on pretax income instead of EBIT (interest 24.0 a year held flat)
tax_wrong = [-(base["ebit"][i] - 24.0) * TAX_RATE for i in range(3, 8)]
ufcf_wrong = [base["ebit"][i] + tax_wrong[i - 3] + base["da"][i] - base["capex"][i] - base["d_nwc"][i] for i in range(3, 8)]
pv_wrong = sum(ufcf_wrong[i] * V["dfac"][i] for i in range(5))
px_wrong = (pv_wrong + V["pv_tv"] - net_debt - NCI) / diluted_shares
print(f"  Mistake check, tax on pretax income instead of EBIT: implied price {px_wrong:.2f} "
      f"(each year's UFCF too high by {24.0 * TAX_RATE:.1f})")
# Debrief figure: cash released if DSO falls from 60 to 50 days in 2026E
dso_release = base["revenue"][3] * (DSO - 50.0) / DAYS
print(f"  Debrief: cash released in 2026E if DSO falls to 50 days: {dso_release:.1f}")
print("All checks passed.")
