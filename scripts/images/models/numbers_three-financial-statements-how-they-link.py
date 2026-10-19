#!/usr/bin/env python3
"""Numbers behind "The Three Financial Statements: How They Link and How to Explain It".

Plain Python, no dependencies. Prints every table the article shows, as Markdown pipe
tables, so the figures in the draft can be pasted straight from this output and the image
agent can rebuild the same tables in Excel.

Three blocks:

  1. The $10 of depreciation walk at a 25 percent tax rate (plus the 40 percent column
     older guides use), through the income statement, cash flow statement and balance sheet.
  2. Ten more three-statement scenarios, each worked the same way, each with a balance
     check that must come to zero.
  3. Lantern Bikes Co., a fictional bicycle maker: a Year 1 balance sheet, a Year 2 income
     statement, a Year 2 cash flow statement and a Year 2 balance sheet, with the six links
     labeled. The script asserts the Year 2 balance sheet balances (check = 0) and that
     ending cash from the cash flow statement equals cash on the balance sheet. A fast-growth
     variant of Year 2 shows positive net income with negative cash from operations.
  4. The small side calculations the prose mentions (straight-line depreciation on a $100
     machine, the interest follow-up on $100 of debt, the loss-on-sale mirror case), so that
     every number in the article traces back to this file.

Sign convention in every table: a positive number means the line went UP, a negative
number (shown in parentheses) means it went DOWN. On the cash flow statement a positive
number is cash coming in and a negative number is cash going out. "Balance check" is
(change in total assets) minus (change in total liabilities plus equity) and must be 0.

Run from the repo root:
    python3 scripts/images/models/numbers_three-financial-statements-how-they-link.py
"""

TAX = 0.25        # the tax rate the article uses throughout
OLD_TAX = 0.40    # the rate older interview guides used (35 percent federal plus state)


def fmt(x):
    """Format a number the way the article shows it: parentheses for negatives, no
    trailing .0, one decimal when needed, a dash for zero."""
    if abs(x) < 1e-9:
        return "0"
    s = f"{abs(x):,.2f}".rstrip("0").rstrip(".")
    return f"({s})" if x < 0 else s


def table(headers, rows):
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        print("| " + " | ".join(r) + " |")
    print()


# --------------------------------------------------------------------------------------
# Block 1: walk me through $10 of depreciation
# --------------------------------------------------------------------------------------
def depreciation_walk(dep=10.0, tax=TAX):
    """Return a dict of every line that moves when depreciation rises by `dep`."""
    pretax = -dep                    # pre-tax income falls by the full expense
    taxes = pretax * tax             # the company owes less tax (a negative change)
    ni = pretax - taxes              # net income falls by the after-tax amount
    cfo = ni + dep                   # start from net income, add the non-cash expense back
    cash = cfo                       # nothing happens in investing or financing
    ppe = -dep                       # accumulated depreciation rises, so net PP&E falls
    assets = cash + ppe
    re = ni                          # retained earnings move with net income
    le = re
    return {
        "pretax": pretax, "taxes": taxes, "ni": ni, "cfo": cfo, "cash": cash,
        "ppe": ppe, "assets": assets, "re": re, "le": le, "check": assets - le,
    }


def print_depreciation():
    print("=" * 78)
    print("BLOCK 1: WALK ME THROUGH $10 OF DEPRECIATION")
    print("=" * 78)
    print()
    w25 = depreciation_walk(10, TAX)
    w40 = depreciation_walk(10, OLD_TAX)
    assert abs(w25["check"]) < 1e-9 and abs(w40["check"]) < 1e-9

    print("Table 1a. The $10 depreciation walk, 25 percent tax rate (the 40 percent column is")
    print("what older guides show)")
    print()
    rows = [
        ["Income statement: depreciation expense", fmt(10), fmt(10)],
        ["Income statement: pre-tax income", fmt(w25["pretax"]), fmt(w40["pretax"])],
        ["Income statement: taxes", fmt(w25["taxes"]), fmt(w40["taxes"])],
        ["Income statement: net income", fmt(w25["ni"]), fmt(w40["ni"])],
        ["Cash flow statement: net income (top line)", fmt(w25["ni"]), fmt(w40["ni"])],
        ["Cash flow statement: add back depreciation", fmt(10), fmt(10)],
        ["Cash flow statement: cash from operations", fmt(w25["cfo"]), fmt(w40["cfo"])],
        ["Cash flow statement: net change in cash", fmt(w25["cash"]), fmt(w40["cash"])],
        ["Balance sheet: cash", fmt(w25["cash"]), fmt(w40["cash"])],
        ["Balance sheet: net PP&E", fmt(w25["ppe"]), fmt(w40["ppe"])],
        ["Balance sheet: total assets", fmt(w25["assets"]), fmt(w40["assets"])],
        ["Balance sheet: retained earnings", fmt(w25["re"]), fmt(w40["re"])],
        ["Balance sheet: total liabilities and equity", fmt(w25["le"]), fmt(w40["le"])],
        ["Balance check (assets minus liabilities and equity)", fmt(w25["check"]), fmt(w40["check"])],
    ]
    table(["Line", "25% tax rate", "40% tax rate"], rows)

    # The tax shield in one line: depreciation times the tax rate.
    print(f"Tax shield at 25 percent: 10 x 0.25 = {fmt(10 * TAX)} of cash saved")
    print(f"Tax shield at 40 percent: 10 x 0.40 = {fmt(10 * OLD_TAX)} of cash saved")
    print()


# --------------------------------------------------------------------------------------
# Block 2: ten more scenarios
# --------------------------------------------------------------------------------------
def scenario(title, is_lines, cfs_lines, bs_asset_lines, bs_le_lines):
    """Print one scenario table and assert its balance check is zero.

    is_lines:        [(label, change)] on the income statement, ending in net income
    cfs_lines:       [(label, change)] on the cash flow statement, ending in net change in cash
    bs_asset_lines:  [(label, change)] asset-side balance sheet lines
    bs_le_lines:     [(label, change)] liability and equity lines
    """
    assets = sum(v for _, v in bs_asset_lines)
    le = sum(v for _, v in bs_le_lines)
    check = assets - le
    assert abs(check) < 1e-9, f"{title}: balance check is {check}, not 0"
    # Cash on the balance sheet must equal the net change in cash on the cash flow statement
    cfs_cash = cfs_lines[-1][1]
    bs_cash = next((v for l, v in bs_asset_lines if l.lower() == "cash"), 0.0)
    assert abs(cfs_cash - bs_cash) < 1e-9, f"{title}: cash does not tie"

    print(f"{title}")
    print()
    rows = []
    rows += [[f"Income statement: {l}", fmt(v)] for l, v in is_lines] or [["Income statement", "no change"]]
    rows += [[f"Cash flow statement: {l}", fmt(v)] for l, v in cfs_lines]
    rows += [[f"Balance sheet: {l}", fmt(v)] for l, v in bs_asset_lines]
    rows += [["Balance sheet: total assets", fmt(assets)]]
    rows += [[f"Balance sheet: {l}", fmt(v)] for l, v in bs_le_lines]
    rows += [["Balance sheet: total liabilities and equity", fmt(le)]]
    rows += [["Balance check", fmt(check)]]
    table(["Line", "Change"], rows)


def print_scenarios():
    print("=" * 78)
    print("BLOCK 2: TEN MORE SCENARIOS, 25 PERCENT TAX RATE")
    print("=" * 78)
    print()

    # 1. Inventory up $10, paid in cash. Nothing hits the income statement until it sells.
    scenario(
        "Table 2a. Inventory up $10, paid in cash",
        [],
        [("change in inventory (asset up, cash out)", -10), ("cash from operations", -10),
         ("net change in cash", -10)],
        [("cash", -10), ("inventory", 10)],
        [("(no change)", 0)],
    )

    # 2. Inventory up $10 on credit. Supplier is paid later, so payables rise instead of cash falling.
    scenario(
        "Table 2b. Inventory up $10, bought on credit",
        [],
        [("change in inventory (asset up, cash out)", -10),
         ("change in accounts payable (liability up, cash in)", 10),
         ("cash from operations", 0), ("net change in cash", 0)],
        [("cash", 0), ("inventory", 10)],
        [("accounts payable", 10)],
    )

    # 3. $100 of capex paid in cash. Investing outflow; PP&E up; income statement waits for depreciation.
    scenario(
        "Table 2c. $100 of capex, paid in cash",
        [],
        [("cash from operations", 0), ("capital expenditures (investing)", -100),
         ("net change in cash", -100)],
        [("cash", -100), ("net PP&E", 100)],
        [("(no change)", 0)],
    )

    # 4. Raise $100 of debt. Financing inflow; cash and debt both up.
    scenario(
        "Table 2d. Raise $100 of debt",
        [],
        [("cash from operations", 0), ("debt issued (financing)", 100),
         ("net change in cash", 100)],
        [("cash", 100)],
        [("long-term debt", 100)],
    )

    # 5. Buy back $50 of stock. Financing outflow; cash down; treasury stock reduces equity.
    scenario(
        "Table 2e. Buy back $50 of stock",
        [],
        [("cash from operations", 0), ("share repurchases (financing)", -50),
         ("net change in cash", -50)],
        [("cash", -50)],
        [("treasury stock (reduces equity)", -50)],
    )

    # 6. $20 of deferred revenue collected. Cash now, revenue later.
    scenario(
        "Table 2f. $20 of deferred revenue collected",
        [],
        [("change in deferred revenue (liability up, cash in)", 20),
         ("cash from operations", 20), ("net change in cash", 20)],
        [("cash", 20)],
        [("deferred revenue", 20)],
    )

    # 7. $50 write-down of PP&E, assumed tax deductible for the walk.
    wd = 50.0
    wd_tax = -wd * TAX
    wd_ni = -wd - wd_tax
    scenario(
        "Table 2g. $50 write-down of PP&E (treated as tax deductible)",
        [("write-down expense", wd), ("pre-tax income", -wd), ("taxes", wd_tax), ("net income", wd_ni)],
        [("net income", wd_ni), ("add back write-down (non-cash)", wd),
         ("cash from operations", wd_ni + wd), ("net change in cash", wd_ni + wd)],
        [("cash", wd_ni + wd), ("net PP&E", -wd)],
        [("retained earnings", wd_ni)],
    )

    # 8. $10 dividend. No income statement effect; financing outflow; retained earnings down.
    scenario(
        "Table 2h. $10 dividend paid",
        [],
        [("cash from operations", 0), ("dividends paid (financing)", -10),
         ("net change in cash", -10)],
        [("cash", -10)],
        [("retained earnings", -10)],
    )

    # 9. Accrued expenses up $10: the expense is recognized now, paid later.
    ae = 10.0
    ae_tax = -ae * TAX
    ae_ni = -ae - ae_tax
    scenario(
        "Table 2i. Accrued expenses up $10",
        [("operating expense", ae), ("pre-tax income", -ae), ("taxes", ae_tax), ("net income", ae_ni)],
        [("net income", ae_ni), ("change in accrued expenses (liability up, cash in)", ae),
         ("cash from operations", ae_ni + ae), ("net change in cash", ae_ni + ae)],
        [("cash", ae_ni + ae)],
        [("accrued expenses", ae), ("retained earnings", ae_ni)],
    )

    # 10. Sell equipment with a $30 book value for $40 cash: a $10 gain.
    book, price = 30.0, 40.0
    gain = price - book
    gain_tax = gain * TAX
    gain_ni = gain - gain_tax
    scenario(
        "Table 2j. Sell equipment with a $30 book value for $40",
        [("gain on sale", gain), ("pre-tax income", gain), ("taxes", -gain_tax), ("net income", gain_ni)],
        [("net income", gain_ni), ("subtract gain on sale (non-cash)", -gain),
         ("cash from operations", gain_ni - gain), ("proceeds from sale of equipment (investing)", price),
         ("net change in cash", gain_ni - gain + price)],
        [("cash", gain_ni - gain + price), ("net PP&E", -book)],
        [("retained earnings", gain_ni)],
    )


# --------------------------------------------------------------------------------------
# Block 3: Lantern Bikes Co., Year 1 to Year 2
# --------------------------------------------------------------------------------------
def lantern_bikes(ar_change=10.0, inv_change=5.0, debt_change=-20.0, dividends=12.0,
                  label="Table 3", print_tables=True):
    """Build the Year 2 statements from the Year 1 balance sheet and the Year 2 drivers.
    All figures in $ millions. `debt_change` is negative for a repayment and positive for a
    draw. Returns the key figures so the caller can check them."""

    # Year 1 ending balance sheet (the starting point)
    y1 = {
        "cash": 40.0, "ar": 60.0, "inventory": 80.0, "ppe": 300.0,
        "ap": 50.0, "accrued": 20.0, "debt": 200.0,
        "common": 100.0, "re": 110.0,
    }
    y1_assets = y1["cash"] + y1["ar"] + y1["inventory"] + y1["ppe"]
    y1_liab = y1["ap"] + y1["accrued"] + y1["debt"]
    y1_equity = y1["common"] + y1["re"]
    assert abs(y1_assets - (y1_liab + y1_equity)) < 1e-9

    # Year 2 income statement drivers
    revenue = 500.0
    cogs = 300.0
    sga = 100.0
    da = 30.0
    interest_rate = 0.05                     # on the beginning debt balance
    interest = y1["debt"] * interest_rate    # 200 x 5% = 10
    gross = revenue - cogs
    ebit = gross - sga - da
    pretax = ebit - interest
    taxes = pretax * TAX
    ni = pretax - taxes

    # Year 2 balance sheet movements that drive the cash flow statement
    capex = 40.0
    ap_change = 6.0
    accrued_change = 2.0

    # Cash flow statement (indirect method)
    cfo = ni + da - ar_change - inv_change + ap_change + accrued_change
    cfi = -capex
    cff = debt_change - dividends
    net_change = cfo + cfi + cff
    ending_cash = y1["cash"] + net_change

    # Year 2 ending balance sheet
    y2 = {
        "cash": ending_cash,
        "ar": y1["ar"] + ar_change,
        "inventory": y1["inventory"] + inv_change,
        "ppe": y1["ppe"] + capex - da,
        "ap": y1["ap"] + ap_change,
        "accrued": y1["accrued"] + accrued_change,
        "debt": y1["debt"] + debt_change,
        "common": y1["common"],
        "re": y1["re"] + ni - dividends,
    }
    y2_assets = y2["cash"] + y2["ar"] + y2["inventory"] + y2["ppe"]
    y2_liab = y2["ap"] + y2["accrued"] + y2["debt"]
    y2_equity = y2["common"] + y2["re"]
    check = y2_assets - (y2_liab + y2_equity)
    assert abs(check) < 1e-9, f"Lantern Bikes Year 2 does not balance: {check}"
    assert abs(y2["cash"] - ending_cash) < 1e-9
    assert ending_cash >= 0, "a real balance sheet never shows negative cash"

    result = {
        "ni": ni, "da": da, "cfo": cfo, "cfi": cfi, "cff": cff, "net_change": net_change,
        "ending_cash": ending_cash, "y2": y2, "check": check, "interest": interest,
        "ebit": ebit, "pretax": pretax, "taxes": taxes, "gross": gross,
        "ar_change": ar_change, "inv_change": inv_change, "ap_change": ap_change,
        "accrued_change": accrued_change, "debt_change": debt_change, "dividends": dividends,
        "capex": capex,
    }
    if not print_tables:
        return result

    print(f"{label}a. Lantern Bikes Co., Year 2 income statement ($ millions)")
    print()
    table(["Line", "Year 2", "Where it goes"], [
        ["Revenue", fmt(revenue), ""],
        ["Cost of goods sold", fmt(-cogs), ""],
        ["Gross profit", fmt(gross), ""],
        ["SG&A", fmt(-sga), ""],
        ["Depreciation and amortization", fmt(-da), "Link 2: added back on the CFS, reduces PP&E"],
        ["EBIT (operating profit)", fmt(ebit), ""],
        ["Interest expense (5% on beginning debt of 200)", fmt(-interest), "Computed off the Year 1 debt balance"],
        ["Pre-tax income", fmt(pretax), ""],
        ["Taxes (25%)", fmt(-taxes), ""],
        ["Net income", fmt(ni), "Link 1: top of the CFS and into retained earnings"],
    ])

    print(f"{label}b. Lantern Bikes Co., Year 2 cash flow statement ($ millions)")
    print()
    table(["Line", "Year 2", "Where it comes from or goes"], [
        ["Net income", fmt(ni), "Link 1: from the income statement"],
        ["Plus: depreciation and amortization", fmt(da), "Link 2: non-cash, added back"],
        ["Less: increase in accounts receivable", fmt(-ar_change), "Link 4: balance sheet AR 60 to " + fmt(y2["ar"])],
        ["Less: increase in inventory", fmt(-inv_change), "Link 4: inventory 80 to " + fmt(y2["inventory"])],
        ["Plus: increase in accounts payable", fmt(ap_change), "Link 4: payables 50 to " + fmt(y2["ap"])],
        ["Plus: increase in accrued expenses", fmt(accrued_change), "Link 4: accrued 20 to " + fmt(y2["accrued"])],
        ["Cash from operations", fmt(cfo), ""],
        ["Capital expenditures", fmt(cfi), "Link 3: raises PP&E"],
        ["Cash from investing", fmt(cfi), ""],
        ["Debt repaid", fmt(debt_change), "Link 5: debt 200 to " + fmt(y2["debt"])],
        ["Dividends paid", fmt(-dividends), "Reduces retained earnings"],
        ["Cash from financing", fmt(cff), ""],
        ["Net change in cash", fmt(net_change), ""],
        ["Beginning cash", fmt(y1["cash"]), "Year 1 balance sheet"],
        ["Ending cash", fmt(ending_cash), "Link 6: becomes cash on the Year 2 balance sheet"],
    ])

    print(f"{label}c. Lantern Bikes Co., balance sheet, Year 1 to Year 2 ($ millions)")
    print()
    table(["Line", "Year 1", "Year 2", "Change", "Why"], [
        ["Cash", fmt(y1["cash"]), fmt(y2["cash"]), fmt(y2["cash"] - y1["cash"]), "Link 6: ending cash from the CFS"],
        ["Accounts receivable", fmt(y1["ar"]), fmt(y2["ar"]), fmt(ar_change), "Link 4"],
        ["Inventory", fmt(y1["inventory"]), fmt(y2["inventory"]), fmt(inv_change), "Link 4"],
        ["Net PP&E", fmt(y1["ppe"]), fmt(y2["ppe"]), fmt(capex - da), "Links 2 and 3: plus capex 40, minus D&A 30"],
        ["Total assets", fmt(y1_assets), fmt(y2_assets), fmt(y2_assets - y1_assets), ""],
        ["Accounts payable", fmt(y1["ap"]), fmt(y2["ap"]), fmt(ap_change), "Link 4"],
        ["Accrued expenses", fmt(y1["accrued"]), fmt(y2["accrued"]), fmt(accrued_change), "Link 4"],
        ["Long-term debt", fmt(y1["debt"]), fmt(y2["debt"]), fmt(debt_change), "Link 5: repaid 20"],
        ["Total liabilities", fmt(y1_liab), fmt(y2_liab), fmt(y2_liab - y1_liab), ""],
        ["Common stock", fmt(y1["common"]), fmt(y2["common"]), fmt(0), "No shares issued or bought back"],
        ["Retained earnings", fmt(y1["re"]), fmt(y2["re"]), fmt(ni - dividends), "Link 1: plus net income " + fmt(ni) + ", minus dividends " + fmt(dividends)],
        ["Total equity", fmt(y1_equity), fmt(y2_equity), fmt(y2_equity - y1_equity), ""],
        ["Total liabilities and equity", fmt(y1_liab + y1_equity), fmt(y2_liab + y2_equity), fmt((y2_liab + y2_equity) - (y1_liab + y1_equity)), ""],
        ["Balance check (assets minus L+E)", fmt(y1_assets - y1_liab - y1_equity), fmt(check), "", "Must be 0"],
    ])

    return result


def print_lantern():
    print("=" * 78)
    print("BLOCK 3: LANTERN BIKES CO., YEAR 1 TO YEAR 2")
    print("=" * 78)
    print()
    base = lantern_bikes()

    # The six links, each with its Year 2 number, as one summary table
    print("Table 3d. The six links in Lantern Bikes' Year 2, in one table")
    print()
    table(["Link", "Year 2 figure", "Income statement", "Cash flow statement", "Balance sheet"], [
        ["1. Net income", fmt(base["ni"]), "Bottom line", "Top line", "Retained earnings up " + fmt(base["ni"]) + " before dividends"],
        ["2. D&A", fmt(base["da"]), "Expense", "Added back", "Net PP&E down " + fmt(base["da"])],
        ["3. Capex", fmt(40), "Not here", "Investing outflow", "Net PP&E up 40"],
        ["4. Working capital", fmt(-7), "Not here", "Net " + fmt(-7) + " in operations", "AR up 10, inventory up 5, payables up 6, accrued up 2"],
        ["5. Debt", fmt(-20), "Interest only", "Financing outflow 20", "Debt 200 to 180"],
        ["6. Ending cash", fmt(base["ending_cash"]), "Not here", "Last line", "Cash line"],
    ])

    # A cash bridge: why cash fell 4 in a year with 45 of net income
    print("Table 3e. Why Lantern Bikes' cash fell by 4 in a year it earned 45")
    print()
    table(["Step", "Amount", "Running total"], [
        ["Net income", fmt(base["ni"]), fmt(base["ni"])],
        ["Add back D&A (non-cash)", fmt(base["da"]), fmt(base["ni"] + base["da"])],
        ["Working capital build (AR 10 and inventory 5 out, payables 6 and accrued 2 in)", fmt(-7), fmt(base["ni"] + base["da"] - 7)],
        ["Capex", fmt(-40), fmt(base["cfo"] - 40)],
        ["Debt repaid", fmt(-20), fmt(base["cfo"] - 40 - 20)],
        ["Dividends", fmt(-12), fmt(base["net_change"])],
    ])

    # Fast-growth variant: same income statement, but receivables and inventory balloon.
    # Cash from operations turns negative, so the company draws 60 on a revolver instead of
    # repaying 20, and skips the dividend. Net income is unchanged; the cash story is not.
    fast = lantern_bikes(ar_change=60.0, inv_change=50.0, debt_change=60.0, dividends=0.0,
                         print_tables=False)
    assert fast["ni"] == base["ni"]
    assert fast["cfo"] < 0
    assert abs(fast["check"]) < 1e-9
    print("Table 3f. Fast-growth variant: same net income, receivables up 60 and inventory up 50")
    print()
    table(["Line", "Base Year 2", "Fast-growth Year 2"], [
        ["Net income", fmt(base["ni"]), fmt(fast["ni"])],
        ["Plus: D&A", fmt(base["da"]), fmt(fast["da"])],
        ["Less: increase in accounts receivable", fmt(-base["ar_change"]), fmt(-fast["ar_change"])],
        ["Less: increase in inventory", fmt(-base["inv_change"]), fmt(-fast["inv_change"])],
        ["Plus: increase in accounts payable", fmt(base["ap_change"]), fmt(fast["ap_change"])],
        ["Plus: increase in accrued expenses", fmt(base["accrued_change"]), fmt(fast["accrued_change"])],
        ["Cash from operations", fmt(base["cfo"]), fmt(fast["cfo"])],
        ["Capital expenditures", fmt(-base["capex"]), fmt(-fast["capex"])],
        ["Debt repaid (base) or revolver drawn (fast)", fmt(base["debt_change"]), fmt(fast["debt_change"])],
        ["Dividends paid", fmt(-base["dividends"]), fmt(-fast["dividends"])],
        ["Net change in cash", fmt(base["net_change"]), fmt(fast["net_change"])],
        ["Ending cash", fmt(base["ending_cash"]), fmt(fast["ending_cash"])],
        ["Ending debt", fmt(base["y2"]["debt"]), fmt(fast["y2"]["debt"])],
        ["Balance check", fmt(base["check"]), fmt(fast["check"])],
    ])


# --------------------------------------------------------------------------------------
# Block 4: side calculations mentioned in the prose
# --------------------------------------------------------------------------------------
def print_side_calcs():
    print("=" * 78)
    print("BLOCK 4: SIDE CALCULATIONS MENTIONED IN THE PROSE")
    print("=" * 78)
    print()
    # Section 1 and the capex follow-up: a $100 machine depreciated straight-line over ten years
    cost, life = 100.0, 10
    annual_dep = cost / life
    print(f"Straight-line depreciation: {fmt(cost)} machine over {life} years = {fmt(annual_dep)} a year")

    # Section 5, debt follow-up: $100 of debt at 5 percent, interest paid in cash, 25 percent tax
    debt, rate = 100.0, 0.05
    interest = debt * rate
    ni_change = -interest * (1 - TAX)
    cash_change = -interest + interest * TAX     # interest paid out, tax saved on it
    assert abs(ni_change - cash_change) < 1e-9   # interest is a cash expense, so the two match
    print(f"Interest follow-up: {fmt(debt)} of debt at {rate:.0%} = {fmt(interest)} of interest; "
          f"net income {fmt(ni_change)}; cash {fmt(cash_change)}")

    # Section 5, sale of equipment mirror case: $30 book value sold for $20, a $10 loss
    book, price = 30.0, 20.0
    loss = book - price
    print(f"Loss-on-sale mirror: book {fmt(book)} sold for {fmt(price)} = loss of {fmt(loss)}, "
          f"added back in operations, {fmt(price)} of proceeds in investing")
    print()


if __name__ == "__main__":
    print_depreciation()
    print_scenarios()
    print_lantern()
    print_side_calcs()
    print("All balance checks passed (every scenario and both Lantern Bikes years tie to zero).")
