# DCF workbook structure (reference layout, October 2026)

A structural reference for the DCF-based modeling-test example in the "Financial Modeling Test" article and for the workbook its screenshots come from. This is a layout, not a template to copy: every company, number, label, color and formula in our workbook is ours. Nothing in this file or in our workbook names a source.

## Tab order (left to right)

1. **Cover.** Company name, one-line description, valuation date, a scenario switch cell (Bear / Base / Bull) that every growth and margin assumption reads through, a table of contents, the color key.
2. **Inputs.** Three years of historical income statement collapsed to the lines the model needs (revenue, cost of sales, gross profit, SG&A, other operating, EBIT, interest, pretax, taxes, net income, basic and diluted shares, EPS). Under it: growth rates and margins computed from the historicals (revenue growth, gross margin, SG&A as a percent of revenue, effective tax rate). Then EBITDA (EBIT plus D&A pulled from the cash flow statement). Then a segment build (revenue by segment and by geography, each with growth and mix percentages). Then the assumptions block: for each segment and each margin, three rows (Bear, Base, Bull) across the projection years, with the live row chosen by the scenario switch.
3. **Schedules.** Working capital by line (receivables, inventory, payables, accrued and deferred) each shown as beginning, change, ending, then as a percent of revenue or cost of sales and as days (DSO, DIO, DPO). Total net working capital and the (increase) / decrease line that feeds free cash flow. Then PP&E: beginning, plus capex, minus depreciation, ending, with capex as a percent of revenue and depreciation as a percent of capex (or of beginning PP&E). Intangibles the same way if the company has them.
4. **Cost of debt.** Each tranche with principal and rate, weight by principal, weighted average pre-tax cost of debt.
5. **Comps data.** Price, shares, market cap, debt, minority interest, preferred, cash, enterprise value, LTM and forward EBITDA and EPS for five to eight peers plus the subject. Low, high, mean, median rows.
6. **Beta.** Peer betas, debt and equity, tax rates; unlever each (beta divided by one plus (one minus tax) times debt over equity); take the median unlevered beta; relever at the subject's own debt to equity.
7. **WACC.** Risk-free rate, equity risk premium, relevered beta, cost of equity by CAPM; pre-tax cost of debt from the cost of debt tab; after-tax cost of debt; equity and debt weights from market values; WACC.
8. **DCF.** Revenue, cost of sales, gross profit, operating expenses, EBIT, taxes on EBIT, NOPAT, plus D&A, minus capex, plus or minus the change in working capital, unlevered free cash flow, across historical and projected years. Present value of each projected year's cash flow discounted from the valuation date (a year fraction from the valuation date to each fiscal year end, or the mid-year convention; the article says which and why). Terminal value by exit multiple on final-year EBITDA, discounted, with a Gordon growth cross-check and the implied growth or implied multiple shown. Enterprise value, minus net debt, minus minority interest, equals equity value; divided by diluted shares equals implied share price; compared with the current price for the implied return.
9. **Sensitivity.** A two-way data table: WACC down the side, exit multiple across the top, implied share price in the body, with a step size cell for each axis so the grid re-centers on the base case.
10. **Football field.** Low and high implied share price from each method (comps on EV/EBITDA, comps on P/E, DCF bear / base / bull, 52-week range) feeding a floating bar chart.
11. **Raw data.** The three statements as filed, plus the capital structure table, so every input on the calculation tabs traces to a cell here with a green cross-sheet link.

## Conventions the layout uses

- Column A is a narrow margin column; labels in column B; years across the top from column C; each block has its own year header row so it reads on its own.
- Blue hardcodes, black formulas, green cross-sheet links; one formula per row copied across; no hardcodes inside formulas; units stated once per block header ("Stated in $ millions, except per share data").
- Historical columns pull from the raw data tabs; projected columns reference the assumptions block, never a typed number.
- Signs follow the statement: costs are shown negative and subtotals are SUMs, so a reader can audit any subtotal by adding the column.
- The scenario switch is one cell on the cover; the assumptions block reads it with a lookup so Bear / Base / Bull can be flipped without touching a formula.
- The sensitivity grid is built with a data table so the body stays live.

## How our modeling-test workbook differs from this reference

- One fictional company of our own, with our own segments and numbers, built by `scripts/images/models/build_{name}.py` and asserted against the article tables.
- The house palette from `scripts/images/wsg_viz.py` (navy section bars, pale yellow input cells, blue inputs, black formulas, green links), not any other scheme.
- A two-hour test does not need the football field or the full comps tab; the article's worked example builds Inputs, Schedules, WACC, DCF and Sensitivity, and says what a longer take-home version adds.
- Workbook author metadata is "Wall Street Guide".
