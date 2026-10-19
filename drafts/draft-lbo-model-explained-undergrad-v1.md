---
headline: "LBO Model Explained: What an Undergrad Actually Needs to Know"
byline: stephen-turban
target_keyword: lbo model
secondary_keywords: [lbo model explained, how to build an lbo model, lbo model for interviews, paper lbo]
format: ultimate-guide
hook_type: real-deal-story
word_count_target: ~2000-2500, guideline only, no cap
status: draft-v1
---

# LBO Model Explained: What an Undergrad Actually Needs to Know

**Meta description:** WSG founder Stephen Turban explains the LBO model step by step: where the inputs come from, how to lay it out, a worked example that ties, and the paper LBO.

The fastest way to understand what an LBO model does is to watch the most profitable one ever built play out in real life. On July 3, 2007, Blackstone agreed to buy Hilton Hotels for $47.50 a share, about $26 billion in total and a 40 percent premium to the prior day's close. Blackstone's funds put in roughly $5.7 billion of equity. Banks lent the other $20 billion or so [VERIFY: price and premium against Blackstone's July 3, 2007 release; equity and debt split against the Oxford Said case, 21.5 percent equity and 78.5 percent debt].

Fourteen months later Lehman Brothers failed, business travel dried up, and Blackstone wrote its Hilton stake down by about 70 percent. In April 2010 it had to put in another $819 million just to get Hilton's debt cut from $20 billion to $16 billion [VERIFY: writedown and 2010 restructuring figures against Blackstone's April 8, 2010 release and the Oxford Said case]. Then the cycle turned. Hilton went public again in December 2013 in the largest hotel IPO on record, and when Blackstone sold its last shares in May 2018, Bloomberg put its total profit at about $14 billion [VERIFY: $2.34 billion IPO and the $14 billion profit figure against Bloomberg's December 2013 and May 2018 coverage]. By that count, nobody has made more on a single private equity deal.

Every number in that story is a line in a spreadsheet, and that spreadsheet is the LBO model: the one piece of modeling an undergrad is most likely to face in a private equity interview and to be asked about in a banking one. I'm Stephen Turban, founder of WallStreetGuide. I went to Harvard and then McKinsey rather than a bank, and what I do now is watch undergrads go through PE and banking recruiting every cycle, including the modeling tests that decide the PE side. This guide goes deeper than the two-minute verbal answer: where every input comes from, how to lay the model out, how to build each block, a worked example where every number ties, the paper LBO, and what to say when the questions start.

## What is an LBO model?

An LBO model is a spreadsheet that tests whether a private equity firm can buy a company mostly with borrowed money, run it for about five years while the company's own cash flow pays down that debt, sell it, and earn a target return on the equity it put in. **The LBO model's real output is a price: the most a sponsor can pay and still hit a 20 to 25 percent annual return.** Its building blocks are the purchase price, a sources and uses table, a five-year operating forecast, a debt schedule, and a returns calculation, with sensitivity tables on top.

## Do undergrads need to build a full LBO model for interviews?

For investment banking interviews, no: you need to explain the logic in two minutes and work a paper LBO with round numbers in your head. For private equity internship and analyst interviews, yes. **Many PE interviews for undergrads include a timed modeling test, usually one to three hours, where you build a simplified LBO model from a short case pack.** [VERIFY: current test format at the funds that hire undergrads] The full model in Section 5 is the version you'd build in that test, and the paper LBO in Section 7 is the version you'd talk through in a banking superday.

## 1. An LBO model answers one question: what can we pay and still make our return?

Start with the deal itself, because the model only makes sense once you see the deal.

A private equity firm (the "sponsor") finds a company with steady cash flow. It buys the company using some of its own investors' money and a lot of borrowed money, usually more borrowed than owned. The company, not the sponsor, is responsible for the debt. If the company can't pay, the lenders end up owning it, and the sponsor's other funds aren't on the hook. For the next five to seven years, the company's cash flow goes to paying interest and paying down principal. Then the sponsor sells the company, pays off whatever debt is left, and keeps the rest.

The closest everyday version is buying a rental property with a 25 percent down payment, using the rent to pay the mortgage, and selling the building in five years. The tenant paid down your loan. You keep the equity.

Why borrow so much? Because debt makes the equity work harder. If you buy a $1,000 million company with $1,000 million of your own money and sell it for $1,300 million, you made 30 percent. If you buy it with $400 million of your own money and $600 million of debt, and sell it for $1,300 million, you pay off the $600 million and keep $700 million. Same company, same sale price, but your $400 million became $700 million. That's a 75 percent gain instead of 30. Leverage cuts the other way too, which is what Blackstone found out in 2009.

![Timeline of Blackstone's Hilton buyout from July 2007 to the May 2018 exit with six dated events](published/assets/images/lbo-model-explained-undergrad/01-hilton-timeline.png "Hilton went from a $26 billion buyout to a 70 percent writedown to a $14 billion profit in eleven years, and every step of that story is a line in the model.")

**Every LBO makes money in exactly three ways, and a good model lets you see how much of the return comes from each one.** Here they are with the same starting deal: buy a company with $100 million of EBITDA at 10.0x, so $1,000 million, funded with $600 million of debt and $400 million of equity, and sell after five years. (EBITDA is earnings before interest, taxes, depreciation and amortization, a rough measure of the cash the business throws off before financing and accounting choices. Our [EBITDA explainer](https://www.wallstreetguide.net/post/ebitda-explained-for-finance-interviews-what-they-actually-want-to-hear) walks through why buyers price companies off it.)

- **EBITDA grows.** EBITDA goes from $100 million to $130 million, the exit multiple stays at 10.0x, and no debt gets paid down. Exit value is $1,300 million. Pay off $600 million of debt and the equity is $700 million. That's 1.75 times the $400 million you put in.
- **Debt gets paid down.** EBITDA stays flat at $100 million and the multiple stays at 10.0x, so the company is still worth $1,000 million at exit. But five years of cash flow paid debt down from $600 million to $350 million. Equity is $1,000 million minus $350 million, or $650 million. That's about 1.63x.
- **The exit multiple is higher than the entry multiple.** EBITDA stays at $100 million and debt stays at $600 million, but a buyer pays 12.0x instead of 10.0x. Exit value is $1,200 million, equity is $600 million, 1.50x.

Put all three together (EBITDA $130 million, debt down to $350 million, exit at 12.0x) and the exit value is $1,560 million, the equity is $1,210 million, and the sponsor made about 3.0x its money, which over five years is roughly a 25 percent annual return.

The first two levers are things the sponsor can influence: grow the business, run it for cash, pay down the loan.

The third is a bet on the market.

**Interviewers trust a model that leans on EBITDA growth and debt paydown and distrust one that needs the exit multiple to bail it out.**

The industry's founders worked this out by trial and error. Jerome Kohlberg did the first "bootstrap" deals inside Bear Stearns in the 1960s, starting with a small family business called Stern Metals in 1965, bought with mostly borrowed money. Henry Kravis and George Roberts joined him at the firm, and the three left to form KKR in 1976. Their first institutional fund, raised in 1978, had about $30 million of commitments. By 1988 KKR was paying $109 a share, about $25 billion, for RJR Nabisco, a fight that became the book Barbarians at the Gate [VERIFY: RJR deal figures; $31 billion including assumed debt]. RJR was a thousand times the size of Stern Metals, and the mechanics were the same.

If you've never heard the verbal version, read our [walk me through an LBO](https://www.wallstreetguide.net/post/walk-me-through-an-lbo-the-6-step-answer-interviewers-want-to-hear) answer first. The rest of this guide is the spreadsheet behind that answer.

## 2. Where the numbers in an LBO model come from

A modeling test hands you a case pack. A real deal doesn't. **Knowing which document holds which input is half of what separates an intern who can build a model from one who can only fill in a template.** Here is where each number lives for a public target, then for a private one.

### Public target

- **The 10-K (annual report).** Item 8 holds the three financial statements. From the income statement you pull revenue, cost of goods sold, SG&A and operating income. From the cash flow statement you pull depreciation and amortization (it's the first add-back under operating activities) and capital expenditures (under investing activities, usually labeled "purchases of property and equipment"). From the balance sheet you pull cash, receivables, inventory, payables and accrued expenses for working capital, and total debt. The notes matter as much as the statements. The debt footnote lists every loan and bond, its interest rate, its maturity and a summary of its covenants (the promises the company made to lenders). The lease footnote tells you how much the company has committed to pay in rent. Since 2019 that commitment also sits on the balance sheet as a lease liability, and some buyers treat it like debt. The income tax footnote gives you the effective tax rate. The MD&A section gives management's own explanation of growth, margins and any guidance for next year.
- **The 10-Q (quarterly report).** You need the latest twelve months of results, not the last fiscal year, because the purchase price is set off LTM EBITDA (LTM means "last twelve months"). The math is last fiscal year, plus the year-to-date quarters from this year, minus the same quarters from last year. The 10-Q gives you the two year-to-date figures.
- **The proxy statement (DEF 14A) and the equity footnote.** The cover page of the 10-K or 10-Q gives you basic shares outstanding as of a recent date. The stock-based compensation note in the 10-K gives you options outstanding with their average strike price and unvested restricted stock units. The proxy gives you the ownership table and the change-of-control terms for executives, which tell you what gets paid out when the company is sold. You need all of it to go from an offer price per share to the total equity purchase price.
- **The 8-K and the press release.** Once a deal is announced, the 8-K carries the merger agreement as an exhibit and the press release states the headline terms: price per share, premium, total value, who is financing it and when it's expected to close. Blackstone's July 2007 Hilton release named the price, the premium and the five banks providing the debt.
- **The credit agreement.** This is the contract for the loans, filed as an exhibit to an 8-K or 10-K after a financing. It tells you the interest rate (a floating benchmark rate like SOFR, the overnight rate banks lend to each other at, plus a fixed spread that is the lender's margin, often with a floor under the benchmark), the required principal repayments each year, the maturity, the percentage of excess cash flow that must go to prepaying the loan, and the covenant levels. If you're modeling a company that already has an LBO-style loan, this document gives you the exact terms instead of a guess.
- **The deal databases.** S&P Capital IQ, FactSet, Bloomberg and PitchBook are the paid databases that give you trading comparables (what similar public companies trade for as a multiple of EBITDA), precedent transactions (what buyers paid for similar companies), the sponsor's own past deals and the trading prices of the target's existing debt. Your school's library may have one of them. In a model, they set the entry multiple and sanity-check the exit multiple.
- **Leveraged finance market data.** PitchBook LCD tracks how much debt the loan market is giving to buyouts. In 2025, large US buyouts financed in the syndicated loan market carried a little under 5.0x debt to EBITDA and sponsors put up about 46 percent of the price as equity on average [VERIFY: PitchBook LCD, 2025 figures; update with the latest LCD data]. That tells you how many "turns" of leverage (multiples of EBITDA) you can assume. A model that assumes 7.0x debt when the market is lending 5.0x is describing a deal that can't be financed.

### Private target (a modeling test or a PE internship)

- **The CIM (confidential information memorandum).** The sell-side bank's sales book. The financial section near the back has three to five years of history, management's projections and an "adjusted EBITDA" bridge that adds back things management says are one-time. Take the history. Treat the projections as the most optimistic case you'll ever see.
- **The management model.** The company's or the banker's Excel file with the projections behind the CIM. Use its revenue build (price times volume, stores times sales per store, whatever drives the business) so your model speaks the company's language, but build your own downside case.
- **The quality of earnings report.** An accounting firm's review of whether EBITDA is what the seller says it is. It gives you a normalized EBITDA figure, a list of the add-backs it accepted and rejected, and a monthly working capital analysis that sets the "peg" used to adjust the price at closing. For the model, the QoE's adjusted EBITDA replaces the CIM's.

In a modeling test the case pack already collapses all of this into a page or two of assumptions. Your job there is the mechanics. **If a test leaves an input out, state your assumption in a labeled cell and move on; nobody fails a modeling test for assuming a 25 percent tax rate, but people fail for stalling.**

## 3. How to lay out and input an LBO model

Before a single formula, decide where things go. **A model that a stranger can follow in two minutes is the goal, because in a test the stranger is your interviewer and in a job the stranger is a vice president at 11 pm.**

**Tabs.** A full model uses one tab per block, in the order the deal happens:

- Transaction Assumptions (entry multiple, LTM EBITDA, fees, debt terms, exit multiple, exit year)
- Sources and Uses
- Operating Model (the income statement down to cash available for debt repayment)
- Debt Schedule (one block per loan)
- Returns (exit value, equity value, MOIC, IRR)
- Sensitivities (data tables)

In a two-hour test, use one tab with those six blocks stacked top to bottom in the same order. Six tabs cost you ten minutes of clicking and make it harder for the grader to trace a formula.

**Color convention.** Blue font for hardcoded numbers you typed in (the entry multiple, the growth rate, the tax rate). Black for formulas. Green for formulas that pull from another tab. Some banks use red for links to other files. **Reviewers use the colors to find your assumptions in seconds, so a black cell that turns out to be a typed number reads as a hidden assumption.**

**Units in one place.** Put "$ in millions, fiscal year ending December 31" in the header of every block and never mix units. The most common unit error students describe to me is a thousands-versus-millions mismatch between a balance sheet pulled in thousands and an EBITDA typed in millions.

**Timeline.** Years run across the top, one column per year, and every block uses the same columns. Three years of history labeled "A" for actual, an LTM column, then five to seven projection years labeled "E" for estimate. The purchase happens at the end of the LTM column, so Year 1 is the first full year the sponsor owns the company.

**One assumption drives each row.** The projection formulas reference an assumptions block, never a typed number. Revenue in Year 2 is `=prior year × (1 + growth rate cell)`, not `=prior year × 1.06`. If you need to change growth, you change one cell and the whole model updates. If the 1.06 is buried in forty formulas, you're retyping forty cells and you will miss one.

**No hardcodes inside formulas.** The same rule from the other direction. `=B14*0.25` for taxes is wrong; `=B14*$C$6` with the tax rate sitting in C6 in blue is right.

**Pick a sign convention and hold it.** Either costs are negative everywhere and you sum the column, or costs are positive and you subtract them. Mixing the two is the fastest way to double-count an expense or add a cost instead of subtracting it.

**Checks live next to the thing they check.** A "sources minus uses" cell under the sources and uses table that should read zero. A "minimum cash shortfall" row under the cash line. A "debt below zero" flag under each loan. In a test, a visible check row that reads zero tells the grader you know what can go wrong before they ask.

**Round inputs in a test.** Use $100 million of EBITDA, 10.0x, 6.0x leverage, 25 percent tax. The grader is going to follow your logic by eye, and round numbers make that possible. Precision belongs in the formulas, not in the assumptions.

## 4. How to structure an LBO model, step by step

This is the part most guides compress into a list of six bullet points. Here is each step with the mechanism underneath it. The worked example in the next section runs these exact steps with numbers.

### Step 1: Purchase price

Enterprise value is what you pay for the whole business, debt and equity together. In an LBO it's set as a multiple of LTM EBITDA: $100 million of EBITDA at 10.0x is $1,000 million of enterprise value.

Equity purchase price is what the current owners actually receive. It's enterprise value minus the company's existing debt plus its existing cash, because the buyer takes over (or repays) the debt and gets to keep the cash. The combination of debt minus cash is called net debt. If the target has $150 million of debt and no spare cash, the owners get $1,000 million minus $150 million, or $850 million. Most private deals are written this way, as "cash-free, debt-free": the price is set on enterprise value, the seller's debt gets paid off at closing out of the proceeds, and the seller keeps any spare cash.

For a public company you build it from the other side. Offer price per share times diluted shares outstanding gives equity value. Diluted shares include options that are "in the money" (strike price below the offer price), counted using the treasury stock method: assume every in-the-money option is exercised, the company collects the strike prices, and it uses that cash to buy back shares at the offer price. The net new shares get added to the basic count. Add restricted stock units outright. Then add net debt to get enterprise value and back out the implied multiple.

Fees come in two kinds and the model treats them differently. Transaction fees (the M&A advisors, lawyers and accountants, typically 1 to 2 percent of enterprise value) are paid at close and expensed: they reduce equity on day one and never come back. Financing fees (what the banks charge to arrange the debt, typically 2 to 3 percent of the amount borrowed) are capitalized as an asset and amortized, meaning they're spread as a non-cash expense over the life of the loan, usually five to seven years. You'll see that amortization line in the worked example.

### Step 2: Sources and uses

The sources and uses table is a two-column ledger that answers two questions: what does the money get spent on, and where does it come from. The totals must be equal, because every dollar spent was a dollar raised.

Uses, in the usual order:

- Purchase of equity (the equity purchase price from Step 1)
- Repayment of existing debt (most loans have a clause that makes them due when the company is sold)
- Transaction fees
- Financing fees
- Cash to the balance sheet (the company needs a minimum operating cash balance to run payroll and pay suppliers, and if the deal is "cash-free," the buyer funds it)

Sources, in order of seniority:

- Revolver (a line of credit, almost always undrawn at close and listed at zero so the reader knows it exists)
- Term Loan B (a bank loan sold to institutional investors, floating rate, 1 percent a year of required repayment, seven-year maturity)
- Senior notes or high-yield bonds (fixed rate, a "bullet" repayment meaning the whole principal is due at maturity, and usually no prepayment allowed for the first few years)
- Second lien loan or mezzanine debt, if any (ranks behind the term loan, costs more)
- Rollover equity (shares the management team or the seller agrees to keep rather than cash out)
- Sponsor equity

**The sponsor's equity check is always the plug: total uses minus every other source.** Debt is sized first, as turns of EBITDA, because the lenders decide how much they'll lend. Whatever is left is what the sponsor has to write a check for. Below about 30 percent equity, lenders in today's market usually balk. Above about 55 percent, the returns rarely clear 20 percent. The average 2025 buyout landed in between, at about 46 percent [VERIFY: LCD equity contribution data for the current year].

### Step 3: The operating model, from revenue to cash available for debt repayment

Now you forecast the business for the hold period. Each line has one driver sitting in the assumptions block.

- **Revenue.** Prior year times one plus the growth rate. In a real model you build this bottom up (units times price, stores times revenue per store). In a test, a growth rate is fine.
- **EBITDA.** Revenue times an EBITDA margin. The margin can step up each year if the case says the sponsor has a cost plan.
- **Depreciation and amortization.** A percent of revenue, or a percent of beginning fixed assets if you built a fixed asset schedule. Subtract it from EBITDA to get EBIT (operating income).
- **Interest expense.** Pulled from the debt schedule in Step 4. This is where the two blocks connect.
- **Financing fee amortization.** The capitalized financing fees divided by the loan life. Subtract it with interest.
- **Pre-tax income, taxes, net income.** EBIT minus interest minus fee amortization is pre-tax income. Multiply by the tax rate. If pre-tax income is negative, taxes should be zero (use a MAX function), not a negative number that pretends the government sends a refund.

Then you convert net income into the cash that's actually available to pay lenders:

- Start with net income.
- Add back D&A and the financing fee amortization. Both reduced net income but neither was a cash payment this year.
- Subtract capital expenditures, the cash spent on equipment and buildings. Capex isn't on the income statement, so it has to come in here.
- Subtract the increase in net working capital. When a company grows, more cash gets tied up in receivables (customers who haven't paid yet) and inventory, partly offset by payables (suppliers the company hasn't paid yet). A growing company's working capital build eats cash even in a profitable year. A common shortcut is to hold net working capital at a fixed percentage of revenue, so the cash use each year is that percentage times the revenue increase.

The result is cash available for debt repayment. Some models call it free cash flow or levered free cash flow before debt paydown. Whatever the label, it's the number the lenders care about. **Cash available for debt repayment, not net income, is the line that drives an LBO model, because interest and principal get paid out of cash, not out of accounting profit.**

### Step 4: The debt schedule, one block per tranche

Each loan ("tranche" just means one layer of the debt) gets a block with the same four rows: beginning balance, additions, repayments, ending balance. Interest is calculated off the balance.

The repayment order follows seniority and cost. First, any revolver borrowing gets repaid, because it's meant to be short-term borrowing and the lenders expect it back as soon as cash allows. Second, the term loan takes its mandatory amortization (the scheduled 1 percent a year) and then absorbs the "cash sweep." Third, the notes just sit there collecting their coupon (the fixed interest payment) until maturity, because they don't allow early repayment without a penalty.

The cash sweep is the heart of the schedule. After mandatory payments, any cash above the minimum cash balance goes to prepaying the term loan. The formula is a MIN: pay the smaller of the cash you have left and the loan balance that's left. The MIN is what stops the loan from going negative in Year 6 when the cash flow is bigger than the remaining balance.

The revolver works in the other direction. If cash available after mandatory payments is negative (a bad year), the company draws on the revolver to cover the shortfall and keep cash at the minimum. The draw formula is `=MAX(0, shortfall)`; in a good year it reads zero.

Now the circularity. Interest for the year should really be calculated on the average of the beginning and ending debt balance, since the company pays down debt through the year, not all on December 31. But the ending balance depends on how much cash was swept, the cash swept depends on net income, and net income depends on the interest expense. Interest needs the ending balance, and the ending balance needs interest. Excel calls this a circular reference and refuses to calculate it by default.

There are two ways to handle it.

- **Enable iterative calculation and add a toggle.** Under File, Options, Formulas, tick "Enable iterative calculation." Excel will then loop the circle until the numbers stop changing, usually in a handful of passes. Put a cell called "Circ" in your assumptions with a 1 or a 0, and write the interest formula as `=IF(Circ=1, AVERAGE(beginning, ending), beginning) × rate`. If the model ever blows up into a cascade of #REF! or #VALUE! errors (it happens when one error enters the loop and feeds itself), set Circ to 0, let the model clear, and set it back to 1.
- **Use the beginning balance and skip the circle.** Interest equals beginning balance times rate. No loop, no toggle, no risk. It slightly overstates interest in years when debt is falling, so it's a touch conservative. In a one- to two-hour test this is the right call unless the prompt asks for average balance.

The worked example uses the beginning-balance method so you can recompute every line by hand, and then shows what the average-balance version changes in Year 1.

### Step 5: Returns

Exit enterprise value is the exit year's EBITDA times the exit multiple. The default assumption is that the exit multiple equals the entry multiple, so the model doesn't quietly bake in a market rally. Exit equity value is exit enterprise value minus the debt still outstanding plus the cash on hand at exit.

Two return measures come out of that:

- **MOIC (multiple on invested capital)** is exit equity divided by the equity the sponsor put in. 2.5x means the sponsor got $2.50 back for every dollar. MOIC ignores time.
- **IRR (internal rate of return)** is the annual compound rate that turns the money in into the money out over the hold period. With one check in at the start and one check out at the end, IRR is MOIC raised to the power of one over the number of years, minus one. 2.5x over five years is 2.5^(1/5) minus 1, about 20 percent a year. In Excel with dated cash flows (dividends along the way, an exit midyear), use XIRR with the cash flow range and the date range, with the initial equity entered as a negative number.

The rule of thumb table every PE interviewer expects you to know:

| MOIC | 3 years | 4 years | 5 years | 6 years | 7 years |
|---|---|---|---|---|---|
| 1.5x | 14.5% | 10.7% | 8.4% | 7.0% | 6.0% |
| 2.0x | 26.0% | 18.9% | 14.9% | 12.2% | 10.4% |
| 2.5x | 35.7% | 25.7% | 20.1% | 16.5% | 14.0% |
| 3.0x | 44.2% | 31.6% | 24.6% | 20.1% | 17.0% |
| 4.0x | 58.7% | 41.4% | 32.0% | 26.0% | 21.9% |

Memorize the five-year column at least: 2x is about 15 percent, 2.5x is about 20, 3x is about 25. **A sponsor's target of 20 to 25 percent IRR over five years means it needs to roughly 2.5x to 3x its equity, and that single fact lets you sanity-check any LBO model in ten seconds.**

### Step 6: Sensitivity tables

A sensitivity table reruns the model for a grid of two inputs at once and shows the output (usually IRR) in each cell. In Excel it's Data, What-If Analysis, Data Table, with one input across the top and one down the side. Two rules: both input cells have to be on the same sheet as the table, and the top-left corner cell has to link to the output you want (the IRR cell).

The two tables every LBO model carries:

- **Entry multiple versus exit multiple.** This is the one interviewers look at first, because it shows how much of the return is a bet on the market. The diagonal (buy at 10x, sell at 10x) is the honest case.
- **Leverage versus exit year.** More debt raises IRR as long as the cash flow can carry it. A longer hold raises MOIC but usually lowers IRR, because once leverage has come down the equity grows more slowly each year than it did in the early years of fast debt paydown.

Other common axes: revenue growth versus EBITDA margin, and purchase price versus the sponsor's required IRR (which backs into the maximum price).

### Step 7: Checks

Before you call the model done, four cells should read what they're supposed to:

- Sources minus uses equals zero.
- No debt balance is ever negative (the MIN in the sweep did its job).
- Cash never drops below the minimum (the revolver draw did its job).
- If you built a balance sheet, assets minus liabilities and equity equals zero in every year.

And three sanity checks that aren't formulas: the IRR sits somewhere between 15 and 30 percent for a plausible deal, interest coverage (EBITDA divided by cash interest) starts above about 2.0x, and leverage (debt divided by EBITDA) falls every year.

## 5. A full worked LBO model with numbers that tie

Here is a fictional company, call it TargetCo, built with the exact steps above. Every figure in these tables was checked in a separate calculation before it went in, so the lines add. Tables are rounded to one decimal, so a line may differ by 0.1 from the sum of the lines above it; the Year 1 walk-through underneath uses exact figures.

### Transaction assumptions

| Assumption | Value |
|---|---|
| LTM EBITDA | $100.0 million |
| LTM revenue | $500.0 million (20.0% margin) |
| Entry multiple | 10.0x LTM EBITDA |
| Enterprise value | $1,000.0 million |
| Existing debt (repaid at close) | $150.0 million |
| Existing excess cash | $0 (cash-free, debt-free deal) |
| Transaction fees (advisory, legal) | $20.0 million, expensed at close |
| Financing fees | $10.0 million, amortized over 5 years |
| Minimum cash funded at close | $20.0 million |
| Term Loan B | $450.0 million (4.5x), 8.0% interest, 1% annual amortization, 100% cash sweep |
| Senior notes | $150.0 million (1.5x), 9.0% fixed, bullet at maturity, no prepayment |
| Revolver | $75.0 million commitment, undrawn |
| Revenue growth | 6.0% a year |
| EBITDA margin | +0.5 percentage points a year (20.5% in Year 1 to 22.5% in Year 5) |
| D&A and capex | each 3.0% of revenue |
| Net working capital | 10.0% of revenue (so the cash use is 10% of each year's revenue increase) |
| Tax rate | 25.0% |
| Exit | end of Year 5 at 10.0x EBITDA |

### Sources and uses

| Uses | $ millions | Sources | $ millions |
|---|---|---|---|
| Purchase of equity (EV $1,000.0 less net debt $150.0) | 850.0 | Revolver (undrawn) | 0.0 |
| Repay existing debt | 150.0 | Term Loan B (4.5x) | 450.0 |
| Transaction fees | 20.0 | Senior notes (1.5x) | 150.0 |
| Financing fees | 10.0 | Sponsor equity (plug) | 450.0 |
| Cash to balance sheet | 20.0 | | |
| **Total uses** | **1,050.0** | **Total sources** | **1,050.0** |

![Excel screenshot of the TargetCo sources and uses table with the sponsor equity plug and a zero check cell](published/assets/images/lbo-model-explained-undergrad/02-sources-and-uses.png "Sponsor equity is the plug, so the check cell under the table reads 0.0 and the equity line moves whenever a fee or a loan does.")

Check: 1,050.0 minus 1,050.0 equals zero. Total debt is $600.0 million, or 6.0x LTM EBITDA. The sponsor's $450.0 million is 42.9 percent of total sources, a little below the 2025 market average, which is a fair place for a teaching example to sit [VERIFY: LCD average equity contribution for the current year].

Notice that the equity check ($450 million) is bigger than the quick "equity purchase price minus new debt" math ($850 million minus $600 million, or $250 million) would suggest. The $200 million difference is the old debt the sponsor had to repay plus $50 million of fees and minimum cash. Beginners miss this constantly. **Sponsor equity funds the whole enterprise value plus fees, minus whatever the lenders put in, and the share price is only part of that bill.**

### Operating model

| $ millions | Year 0 (LTM) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Revenue | 500.0 | 530.0 | 561.8 | 595.5 | 631.2 | 669.1 |
| Revenue growth |  | 6.0% | 6.0% | 6.0% | 6.0% | 6.0% |
| EBITDA margin | 20.0% | 20.5% | 21.0% | 21.5% | 22.0% | 22.5% |
| EBITDA | 100.0 | 108.7 | 118.0 | 128.0 | 138.9 | 150.6 |
| Less: D&A (3% of revenue) | (15.0) | (15.9) | (16.9) | (17.9) | (18.9) | (20.1) |
| EBIT | 85.0 | 92.8 | 101.1 | 110.2 | 119.9 | 130.5 |
| Less: Term Loan B interest (8% on beginning balance) |  | (36.0) | (33.6) | (30.6) | (26.8) | (22.3) |
| Less: Senior notes interest (9% on $150) |  | (13.5) | (13.5) | (13.5) | (13.5) | (13.5) |
| Less: Financing fee amortization ($10 over 5 years) |  | (2.0) | (2.0) | (2.0) | (2.0) | (2.0) |
| Pre-tax income |  | 41.3 | 52.0 | 64.1 | 77.6 | 92.7 |
| Less: Taxes (25%) |  | (10.3) | (13.0) | (16.0) | (19.4) | (23.2) |
| Net income |  | 30.9 | 39.0 | 48.1 | 58.2 | 69.5 |

![Excel screenshot of the TargetCo operating model from revenue to net income over five projected years](published/assets/images/lbo-model-explained-undergrad/03-operating-model.png "Revenue runs off one growth cell, EBITDA off a margin that steps up each year, and the two interest lines flow in from the debt schedule further down the sheet.")

Walk Year 1 with exact figures. Revenue is $500.0 million times 1.06, or $530.0 million. EBITDA is $530.0 million times 20.5 percent, or $108.65 million. D&A is 3 percent of $530.0 million, $15.9 million, so EBIT is $92.75 million. Interest on the term loan is 8 percent of the $450.0 million beginning balance, $36.0 million. Interest on the notes is 9 percent of $150.0 million, $13.5 million. Fee amortization is $10.0 million over five years, $2.0 million. Pre-tax income is $92.75 minus $36.0 minus $13.5 minus $2.0, or $41.25 million. Taxes at 25 percent are $10.31 million. Net income is $30.94 million.

### Cash flow to debt paydown

| $ millions | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Net income | 30.9 | 39.0 | 48.1 | 58.2 | 69.5 |
| Plus: D&A | 15.9 | 16.9 | 17.9 | 18.9 | 20.1 |
| Plus: Financing fee amortization (non-cash) | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| Less: Capex (3% of revenue) | (15.9) | (16.9) | (17.9) | (18.9) | (20.1) |
| Less: Increase in net working capital (10% of revenue growth) | (3.0) | (3.2) | (3.4) | (3.6) | (3.8) |
| Cash available for debt repayment | 29.9 | 37.8 | 46.7 | 56.6 | 67.7 |
| Less: Mandatory Term Loan B amortization (1% of $450) | (4.5) | (4.5) | (4.5) | (4.5) | (4.5) |
| Less: Cash sweep to Term Loan B | (25.4) | (33.3) | (42.2) | (52.1) | (63.2) |
| Change in cash | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Ending cash (minimum cash $20) | 20.0 | 20.0 | 20.0 | 20.0 | 20.0 |

![Excel screenshot of the cash flow block from net income to cash available for debt repayment and ending cash](published/assets/images/lbo-model-explained-undergrad/04-cash-flow-to-debt-paydown.png "Net income is not the cash: D&A and the fee amortization come back, capex and the working capital build come out, and the line that is left is what the lenders get.")

Year 1 again, exactly. Net income $30.94 million, plus D&A $15.9 million, plus fee amortization $2.0 million, minus capex $15.9 million, minus the working capital build of 10 percent of the $30.0 million revenue increase, $3.0 million. Cash available for debt repayment is $29.94 million. The term loan's scheduled 1 percent, $4.5 million, comes out first. The remaining $25.44 million sweeps to the term loan. Nothing is left over, so cash stays at the $20.0 million minimum. Notice that D&A and capex cancel each other in this example (both 3 percent of revenue), which is what a mature business looks like: the company spends on equipment at about the rate its old equipment wears out.

### Debt schedule

| $ millions | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Term Loan B, beginning | 450.0 | 420.1 | 382.2 | 335.5 | 278.9 |
| Less: Mandatory amortization | (4.5) | (4.5) | (4.5) | (4.5) | (4.5) |
| Less: Cash sweep | (25.4) | (33.3) | (42.2) | (52.1) | (63.2) |
| Term Loan B, ending | 420.1 | 382.2 | 335.5 | 278.9 | 211.2 |
| Senior notes (bullet, no prepayment) | 150.0 | 150.0 | 150.0 | 150.0 | 150.0 |
| Revolver (undrawn) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Total debt, ending | 570.1 | 532.2 | 485.5 | 428.9 | 361.2 |
| Total debt / EBITDA | 5.25x | 4.51x | 3.79x | 3.09x | 2.40x |
| EBITDA / cash interest | 2.19x | 2.50x | 2.90x | 3.44x | 4.20x |

![Excel screenshot of the TargetCo debt schedule by tranche with term loan paydown, notes, revolver and leverage ratios](published/assets/images/lbo-model-explained-undergrad/05-debt-schedule.png "Each tranche gets its own block: the term loan takes the mandatory 1 percent and then the whole sweep, the notes sit at $150.0 million collecting their coupon, and the revolver draw stays at zero because no year runs short.")

The term loan ends Year 1 at $450.0 minus $4.5 minus $25.44, or $420.06 million. Year 2's interest is 8 percent of that, $33.6 million, which is why the interest line falls every year and the cash available rises every year. Over five years the sponsor pays down $238.8 million of the $450.0 million term loan, and total debt drops from 6.0x EBITDA to 2.4x. Interest coverage climbs from 2.2x to 4.2x. Both trends are what a lender wants to see, and both are what an interviewer scans for first.

![Stacked bar chart of TargetCo term loan and senior notes balances falling from 600 to 361 over five years](published/assets/images/lbo-model-explained-undergrad/06-debt-balance-by-year.png "The notes never move, so every dollar of paydown comes out of the term loan and total debt falls from 6.0x to 2.4x EBITDA.")

If you used average-balance interest with the circularity switched on, Year 1 term loan interest would be about $34.8 million instead of $36.0 million, cash available would be about $30.9 million instead of $29.9 million, and the term loan would end Year 1 at about $419.1 million instead of $420.1 million. Those gaps are rounding in a test and real money on a $20 billion deal.

Here is the term loan block with its Year 1 formulas written out beside it, the Circ cell included.

![Excel close-up of the term loan block with Year 1 formulas for the cash sweep and the Circ interest toggle](published/assets/images/lbo-model-explained-undergrad/07-interest-formula-closeup.png "The sweep is a MIN against the balance left, and the interest line is an IF on the Circ cell that swaps the beginning balance for the average, which is what moves Year 1 interest from 36.0 to 34.8.")

### Returns

| Returns | $ millions |
|---|---|
| Year 5 EBITDA | 150.6 |
| Exit multiple | 10.0x |
| Exit enterprise value | 1,505.5 |
| Less: Total debt at exit | (361.2) |
| Plus: Cash at exit | 20.0 |
| Exit equity value | 1,164.3 |
| Sponsor equity invested | 450.0 |
| MOIC | 2.59x |
| IRR (5 years) | 20.9% |

![Excel screenshot of the returns block with exit value, exit equity, MOIC of 2.59x and IRR of 20.9 percent](published/assets/images/lbo-model-explained-undergrad/08-returns.png "Exit EBITDA times the same 10.0x, less the debt still outstanding, plus cash, is the equity; the MOIC formula and Excel's IRR function land on the same 20.9 percent.")

MOIC is $1,164.3 million divided by $450.0 million, 2.59x. IRR is 2.59 raised to the one-fifth power minus one, 20.9 percent. Check it against the rule of thumb table: 2.5x over five years is about 20 percent, and we're a bit above 2.5x. The deal clears a 20 percent hurdle (the minimum return the fund told its investors it would aim for) on the base case with the exit multiple flat.

Where did the $714.3 million of equity gain come from? EBITDA grew from $100.0 million to $150.6 million, and at a flat 10.0x that's worth $505.5 million. Debt fell from $600.0 million to $361.2 million, which is $238.8 million. The multiple added nothing. That sums to $744.3 million, and the $30.0 million gap is the transaction and financing fees the sponsor paid at close and never got back. **About two-thirds of this deal's return came from growing EBITDA and one-third from paying down debt, and none of it came from the exit multiple, which is exactly the profile an interviewer wants to see.**

![Waterfall chart bridging 450 of sponsor equity to 1,164 of exit equity through EBITDA growth, debt paydown and fees](published/assets/images/lbo-model-explained-undergrad/09-value-creation-bridge.png "EBITDA growth and debt paydown explain all of the $714.3 million gain, the exit multiple adds nothing, and the $30.0 million of fees never comes back.")

### Sensitivity: entry multiple versus exit multiple

IRR with leverage fixed at 6.0x and the same operating case. A higher entry price means a bigger equity check for the same debt, which is why the rows fall so fast.

| Entry \ Exit | 8.0x | 9.0x | 10.0x | 11.0x | 12.0x |
|---|---|---|---|---|---|
| 8.0x | 28.1% | 32.3% | 36.0% | 39.4% | 42.4% |
| 9.0x | 19.8% | 23.7% | 27.2% | 30.3% | 33.2% |
| 10.0x | 13.9% | 17.6% | 20.9% | 23.9% | 26.6% |
| 11.0x | 9.4% | 13.0% | 16.2% | 19.0% | 21.7% |
| 12.0x | 5.8% | 9.3% | 12.4% | 15.1% | 17.7% |

![Excel screenshot of the IRR sensitivity grid for entry multiple against exit multiple, 8.0x to 12.0x](published/assets/images/lbo-model-explained-undergrad/10-sensitivity-entry-exit.png "Read down the 10.0x column: paying one turn less at entry adds about six points of IRR, more than any operating lever in this model.")

Read the 10.0x row. Pay 10.0x and sell at 8.0x and the IRR drops to 13.9 percent; sell at 12.0x and it's 26.6 percent. Now read the 10.0x column. Pay 9.0x instead of 10.0x and the IRR jumps from 20.9 to 27.2 percent with nothing else changing. **Paying one turn less at entry adds about six points of IRR here, more than raising revenue growth from 6 to 8 percent (about three points) or doubling the margin expansion (about four), which is why sponsors fight over price and why the model's first job is to set the maximum one.**

### Sensitivity: leverage versus exit year

IRR with entry and exit both at 10.0x. At each leverage level the debt splits 75 percent term loan and 25 percent notes, financing fees scale with the debt, and the sweep pays down the term loan.

| Leverage \ Exit year | Year 3 | Year 4 | Year 5 | Year 6 | Year 7 |
|---|---|---|---|---|---|
| 4.0x | 17.7% | 17.5% | 17.3% | 17.0% | 16.6% |
| 5.0x | 19.4% | 19.2% | 18.8% | 18.4% | 18.0% |
| 6.0x | 21.9% | 21.5% | 20.9% | 20.4% | 19.9% |
| 7.0x | 25.5% | 24.8% | 24.0% | 23.2% | 22.4% |

![Excel screenshot of the IRR sensitivity grid for leverage from 4.0x to 7.0x against exit years three to seven](published/assets/images/lbo-model-explained-undergrad/11-sensitivity-leverage-exit-year.png "Each extra turn of leverage adds two to four points of IRR, while each extra year of holding trims it even as the MOIC keeps rising.")

Two things to notice. Each extra turn of leverage adds two to four points of IRR, because the sponsor is putting up less equity for the same company. And each extra year of holding lowers IRR slightly even though MOIC keeps rising (at 6.0x, MOIC goes from 1.81x in Year 3 to 3.55x in Year 7). That's the IRR-versus-MOIC tension PE firms live with: a quick exit flatters the annual rate, a long hold earns more dollars.

## 6. What to add and what to leave out, by setting

The same LBO model has three versions depending on where you're building it. Building the wrong version for the setting is the most common way a competent student runs out of time.

### A one- to three-hour modeling test

Build, in this order: transaction assumptions, sources and uses with a check, the operating model down to cash available for debt repayment, two or three debt tranches with mandatory amortization and a cash sweep, returns with MOIC and IRR, one sensitivity table, and the check cells. That's the complete model. Everything else is optional.

Skip unless the prompt asks:

- PIK interest (interest that accrues to the loan balance instead of being paid in cash; it needs its own rows and a non-cash add-back)
- Detailed tax schedules (net operating losses, deferred taxes)
- Management rollover and option pool mechanics (they change the sponsor's ownership percentage and need a waterfall, the order in which exit proceeds get split among the equity holders)
- Dividend recapitalizations (borrowing more later to pay the sponsor a dividend)
- Purchase price allocation and goodwill (the accounting that writes assets up to the price paid)
- A full balance sheet
- Quarterly periods

**PIK toggles, tax schedules, rollover mechanics and dividend recaps each eat a real slice of a two-hour test, and none of them changes the answer a modeling-test grader is looking for.**

**Graders open a modeling test at the IRR, then at the sources and uses check, then they click into the interest formula to see whether you understood the circularity.** A junior I worked with last spring, call him Marcus, had taken a two-hour test at an upper-middle-market fund before he came to WSG and spent his first 45 minutes on a purchase price allocation nobody asked for. He never got to a returns block. When we rebuilt his approach, he started every practice test by laying out the six blocks with headers in the first five minutes, then filling them top to bottom, so even an unfinished model had an IRR in it by the one-hour mark. His next test, at a growth-oriented fund, came back with an offer.

### A paper LBO on a whiteboard or over the phone

No spreadsheet. Round numbers, interest on the beginning balance, no working capital, D&A equal to capex unless told otherwise, exit multiple equal to entry. Five steps out loud, which the next section walks through. **A paper LBO is graded on your order of operations and your running totals, never on getting the IRR to a decimal.**

### A PE internship or analyst model

Now the extra pieces earn their place. A full three-statement build so the balance sheet balances, with ending cash from the cash flow statement feeding the balance sheet and net income feeding retained earnings. A management case and a sponsor case with a toggle between them. Covenant tests each year against the credit agreement. Rollover equity and a management option pool, so the sponsor's share of exit equity is right. A quarterly first year if the close is midyear. And a sources and uses that includes the actual fee quotes. The model you hand a vice president is 90 percent the same as the test model; it just has the edges filled in.

## 7. The paper LBO, the five-minute interview version

A paper LBO is the interview version of everything above, done out loud with a pen or nothing at all. Banks ask it in superdays. PE firms ask it in first rounds before they bother with a modeling test. Here's a full one.

The prompt: "A company has $100 million of EBITDA, growing $10 million a year. You buy it at 8.0x with 5.0x of debt at 8 percent interest. D&A and capex are both $20 million a year, taxes are 25 percent, and you sell at 8.0x after five years. What's your return?"

**Step 1: Purchase price and equity check.** $100 million times 8.0x is $800 million. Debt is 5.0x times $100 million, $500 million. Equity is $800 million minus $500 million, $300 million. Say all three numbers out loud so the interviewer can follow.

**Step 2: Year 1 cash flow.** EBITDA $110 million. Minus D&A $20 million is EBIT of $90 million. Interest is 8 percent of $500 million, $40 million. Pre-tax income $50 million. Taxes 25 percent, $12.5 million. Net income $37.5 million. Add back D&A $20 million, subtract capex $20 million, they cancel. Free cash flow $37.5 million, call it $40 million. All of it pays down debt: $500 million goes to $460 million.

**Step 3: Repeat for Years 2 to 5, rounding as you go.** Say your rounding rule once ("I'll round interest to the nearest million and cash flow to the nearest five") and the interviewer will accept it.

| Year | EBITDA | EBIT | Interest (8% of beginning debt) | Pre-tax | Net income (75%) | Free cash flow (rounded) | Debt, end of year |
|---|---|---|---|---|---|---|---|
| 1 | 110 | 90 | 40 | 50 | 37.5 | 40 | 460 |
| 2 | 120 | 100 | 37 | 63 | 47 | 45 | 415 |
| 3 | 130 | 110 | 33 | 77 | 58 | 60 | 355 |
| 4 | 140 | 120 | 28 | 92 | 69 | 70 | 285 |
| 5 | 150 | 130 | 23 | 107 | 80 | 80 | 205 |

![Excel screenshot of the paper LBO with purchase price, five years of rounded cash flow and the exit returns](published/assets/images/lbo-model-explained-undergrad/12-paper-lbo.png "The same five steps on one sheet: interest rounded to the nearest million, free cash flow to the nearest five, and the answer still lands within a tenth of a point of the exact 27.0 percent.")

**Step 4: Exit.** Year 5 EBITDA is $150 million. At 8.0x, exit enterprise value is $1,200 million. Minus about $205 million of remaining debt is $995 million of equity, call it $1,000 million.

**Step 5: Returns.** $1,000 million on $300 million is about 3.3x. From the MOIC-to-IRR table in Section 4, 3.0x over five years is about 25 percent, and 3.3x is a bit more, so call it 27 percent. (The exact answer, without rounding, is 3.30x and 27.0 percent. The rounded version landed within a tenth of a point.)

Then say the one sentence that shows you understand the deal as well as the arithmetic: "Most of the return came from EBITDA growing 50 percent and from paying down almost $300 million of debt; the multiple didn't help at all, so this works even if the market softens a little."

**Three things make a paper LBO go well: say every number as you compute it, state your simplifications before you make them, and know the MOIC-to-IRR table cold.** The interviewer wants to hear "3x in five years, about 25 percent" without a pause. Our [25 private equity interview questions](https://www.wallstreetguide.net/post/25-private-equity-interview-questions-that-actually-get-asked) covers the follow-ups that usually come next.

## 8. Mistakes that get otherwise good LBO models thrown out

These are the errors students describe to me when they come to WSG after a test that didn't go their way. Most of them take five seconds to prevent and fifteen minutes to find afterward.

- **Sources and uses don't balance.** Almost always because the equity was typed in as a number instead of calculated as the plug, or because a fee was added to uses after the equity was set. Make equity a formula and add a check cell.
- **A debt balance goes negative.** The cash sweep paid more than the loan had left. Wrap the sweep in a MIN against the remaining balance.
- **Cash piles up on the balance sheet while the term loan sits at its original balance.** The sweep isn't wired. If cash is growing and debt isn't shrinking, the model is leaving returns on the table and the grader will see it in ten seconds.
- **The circularity blows up.** A #REF! in one cell feeds the loop and every number turns into an error. Build the Circ toggle before you build the average-balance formula, not after, and use the beginning balance in a short test.
- **Interest is calculated on the wrong balance.** Term loan interest on the notes balance, or both tranches on total debt. One block per tranche, with its own rate cell, prevents it.
- **Net income is used as the cash flow.** Forgetting to add back D&A, forgetting capex, or forgetting the working capital build. The cash available for debt repayment line should be built as its own row with the five adjustments visible.
- **The working capital sign is flipped.** An increase in net working capital uses cash. If your model shows growth generating cash from working capital, the sign is backward.
- **Taxes are negative in a loss year.** Use MAX(0, pre-tax income × tax rate) or the model pays the company a refund it wouldn't get.
- **Hardcoded numbers inside formulas.** Any `*1.06` or `*0.25` buried in a formula. The grader changes the growth rate in your assumptions block, half the model doesn't move, and that's the end of the review.
- **The exit multiple is above the entry multiple with no reason given.** If you need a 12x exit to get to 20 percent, say so in a note and show the flat-multiple case next to it.
- **IRR is calculated with the IRR function on cash flows that aren't annual.** Excel's IRR assumes evenly spaced periods. Use XIRR with dates when the exit isn't on an anniversary, or just use the MOIC formula when there's one cash flow in and one out.
- **No units, no color coding, no check row.** None of these is a math error, and all of them signal that nobody taught you how models get reviewed.
- **Half a complex model instead of a whole simple one.** The single most common reason a strong candidate fails a two-hour test. **A finished model with three tranches and an IRR beats an unfinished one with a PIK toggle and a purchase price allocation every time.**

Two famous deals show what the model can't save you from. The 2007 buyout of the Texas utility TXU by KKR, TPG and Goldman Sachs's private equity arm, about $45 billion, was the largest LBO in history at the time [VERIFY: TXU deal size and consortium]. The model assumed natural gas prices would stay high, which would keep electricity prices and TXU's cash flow high. Shale drilling flooded the market with gas instead, electricity prices fell, and the company, renamed Energy Future Holdings, filed for bankruptcy in April 2014 with a plan to cut about $40 billion of debt [VERIFY: Energy Future Holdings bankruptcy filing, April 2014]. Every formula in that model was right. The revenue assumption wasn't. **A clean LBO model with a bad operating case is still a bad model, and interviewers will push on your growth and margin assumptions harder than on your formulas.**

The record TXU set stood until September 29, 2025, when Electronic Arts agreed to be taken private for $55 billion, or $210 a share, by a group made up of Saudi Arabia's Public Investment Fund, Silver Lake and Affinity Partners, with JPMorgan providing about $20 billion of debt and the buyers putting up roughly $36 billion of equity [VERIFY: EA deal terms; the deal closed August 4, 2026 and EA was delisted from Nasdaq, confirm against EA's completion release]. Look at that mix for a second: a bit over a third debt and almost two-thirds equity, closer to a cash purchase than to Hilton's 78 percent debt. The biggest LBO ever used less leverage, as a share of the price, than almost any other deal on this page. Higher interest rates and more cautious lenders show up right there, in the equity line of the sources and uses table.

## 9. LBO model templates worth downloading

I went looking for free LBO templates from sources bankers recognize and applied one test to each: does the file match the structure this guide teaches, and can you actually get it without a paywall surprise?

One clears the bar. **A Simple Model's free LBO workbook is the only template I found that is actually free, comes from a source finance people know, and matches the structure taught above.** [A Simple Model](https://www.asimplemodel.com/resources/quick-references/free-downloads) offers the "Simple LBO with Scenarios and Data Tables" file on its free downloads page [VERIFY: link live and file still free; the site emails the download link after you enter an email address]. I opened the file. It's a single tab laid out in the order Section 3 recommends: sources and uses at the top (purchase price as a multiple of EBITDA, senior and subordinated debt sized in turns, equity as the plug, transaction and financing fees), then an income statement with a three-scenario growth toggle, a balance sheet with a check row, a cash flow statement, a debt schedule with a revolver, subordinated debt and senior debt (interest on the average balance, with an on-off switch for the interest circularity), a fixed asset schedule, an exit analysis using XIRR, and two data tables for IRR against the exit multiple. It's the closest thing I found to a worked version of Section 5 that you can click through formula by formula.

The other usual suspects didn't make the cut for this article. Macabacus's LBO templates now sit behind a free trial signup rather than a plain download. Wall Street Prep's short-form LBO model is emailed after a form, and I wasn't able to open the file to check it against the structure here, so I'm not linking it. Corporate Finance Institute's free leveraged finance template requires an account and models IRR at different debt levels rather than a full LBO [VERIFY: each site's current download terms]. If you want to practice building rather than reading, the better use of an hour is to recreate the TargetCo tables above from a blank sheet and check your numbers against mine.

## 10. Say this, don't say that: the LBO model questions that come up

These are the questions students report most often from banking superdays and PE first rounds, with the answer that stalls and the answer that lands. **The answers that land name the mechanism and put a number on it; the answers that stall name the concept and stop.**

**Walk me through an LBO model.**
Don't say: "You buy a company with debt, pay it down and sell it."
Say: "Five blocks. Set the purchase price off LTM EBITDA and a multiple. Build sources and uses with the sponsor's equity as the plug. Project the operating model down to cash available for debt repayment. Run a debt schedule by tranche with a cash sweep, which feeds interest back into the income statement. Then take exit EBITDA times an exit multiple, subtract remaining net debt, and compute MOIC and IRR on the equity."

**Why do sponsors use so much debt?**
Don't say: "Because debt is cheaper than equity."
Say: "Because it shrinks the equity check for the same company. If I buy a $1,000 million business with $400 million of equity and $600 million of debt and the company is worth $1,300 million in five years with the debt paid down to $350 million, my $400 million became $950 million. With no debt, $1,000 million became $1,300 million. Same business, 2.4x instead of 1.3x. The cost is that a bad year can wipe the equity out, which is what nearly happened to Blackstone at Hilton in 2009."

**What makes a good LBO candidate?**
Don't say: "A stable company with good cash flow."
Say: "Predictable cash flow so it can carry 5 to 6 turns of debt, low capital spending needs so that cash goes to the lenders rather than to equipment, a reason EBITDA can grow or margins can improve, and an entry price below where comparable deals have traded. A hotel company in 2007 looked like all four; a utility whose cash flow depended on natural gas prices turned out not to be."

**How do you handle the circular reference in an LBO model?**
Don't say: "I just turn on iterative calculation."
Say: "Interest on the average debt balance depends on the ending balance, and the ending balance depends on cash flow, which depends on interest. Two fixes: enable iterative calculation with a toggle cell so I can break the loop if an error gets in, or calculate interest on the beginning balance and avoid the circle entirely, which is slightly conservative and what I'd do in a timed test."

**What's a reasonable IRR, and how do you get there from MOIC?**
Don't say: "Around 20 percent."
Say: "Most sponsors underwrite to 20 to 25 percent over about five years, so they need 2.5x to 3x their equity. The shortcut is MOIC to the power of one over the years, minus one. 2x over five years is about 15 percent, 3x is about 25."

**Should the exit multiple be higher than the entry multiple?**
Don't say: "Yes, because the company will be bigger and better."
Say: "The default is flat, so the returns don't depend on the market. If I have a specific reason to expect a higher multiple, say the company grew into a size bracket where buyers pay more, I'll show it as an upside case next to the flat case, never as the base."

**What drives returns in an LBO?**
Don't say: "Leverage."
Say: "Three things: EBITDA growth, debt paydown, and the change in multiple between entry and exit. In the model I'd build, about two-thirds of the equity gain comes from EBITDA growth and one-third from paying down debt, with the multiple flat. Leverage amplifies all three; it isn't a source of value by itself."

**How is an LBO model different from a DCF?**
Don't say: "A DCF values the company and an LBO values the deal."
Say: "A DCF discounts unlevered free cash flows at a weighted average cost of capital to say what the business is worth to anyone. An LBO model fixes the return a sponsor needs and backs into the price that delivers it with a specific debt package, so it tends to produce a lower number. So bankers show the LBO value as the floor on the valuation football field, the bar chart that lines up the value range from each method." Our [DCF walkthrough](https://www.wallstreetguide.net/post/walk-me-through-a-dcf-the-7-step-answer-that-works) has the other half of that comparison.

**If you could only sensitize two variables, which ones?**
Don't say: "Revenue growth and margin."
Say: "Entry multiple and exit multiple. Nothing else moves the IRR as much, and the table shows the interviewer immediately how much of the return is operating performance versus a bet on the market. Leverage versus exit year would be my third."

If the accounting underneath these answers feels shaky (why D&A gets added back, why working capital uses cash), our [50 accounting interview questions](https://www.wallstreetguide.net/post/50-accounting-interview-questions-that-you-should-practice-before-your-interview) covers the mechanics the LBO model assumes you already know.

## Build TargetCo this weekend

Reading about an LBO model is not the same as having built one. Open a blank workbook, type the transaction assumptions table from Section 5 in blue, and build the six blocks in order until your Year 5 total debt reads $361.2 million and your IRR reads 20.9 percent. Then switch the interest to average balance with a toggle and watch Year 1 move to $34.8 million. Then break something on purpose, a negative debt balance, a sweep that doesn't fire, and fix it. **Three hours building TargetCo from a blank sheet is the difference between recognizing the words in an interview and being the person who can say "the sponsor's equity is the plug" because you've watched it move.**

If you're targeting a PE internship rather than banking, our [guide to landing a private equity internship as an undergrad](https://www.wallstreetguide.net/post/the-ultimate-guide-to-landing-a-private-equity-internship-as-an-undergrad) covers the firms that hire undergrads and what their processes look like. Blackstone's Hilton model didn't look that different from TargetCo. The numbers were bigger, the hold was eleven years instead of five, and the middle years nearly wiped out the equity. The blocks in the model were the same ones you just built.
