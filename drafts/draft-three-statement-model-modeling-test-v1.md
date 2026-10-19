---
headline: "Three Statement Model: How to Build One for a Modeling Test"
byline: stephen-turban
target_keyword: three statement model
secondary_keywords: [3 statement model, three statement financial model, modeling test, how to build a three statement model]
format: ultimate-guide
hook_type: real-public-story
word_count_target: ~2000-2500, guideline only, no cap
status: draft-v1
---

# Three Statement Model: How to Build One for a Modeling Test

**Meta description:** WSG founder Stephen Turban walks through the three statement model for a modeling test: inputs, build order, the balance check, and a worked example that ties.

In early 2012, a cell in a JPMorgan risk spreadsheet divided by a sum when it should have divided by an average. The bank's own [task force report](https://elischolar.library.yale.edu/ypfs-documents/454), dated January 16, 2013, says the model ran on Excel files that "had to be completed manually, by a process of copying and pasting data from one spreadsheet to another," and that the formula error "likely had the effect of muting volatility by a factor of two." The portfolio it was measuring lost about $5.8 billion by the end of that June.

A three statement model is a far smaller spreadsheet than that one, and nobody loses billions on a two hour test. But the analyst grading yours has seen what one bad cell does, and that's why the first thing they open is your balance check. I'm Stephen Turban, founder of WallStreetGuide. I went to Harvard and through McKinsey's on-cycle recruiting before I started WSG, where I now spend my weeks advising undergrads through the banking pipeline. The modeling test is the round students ask me about with the most dread.

This guide walks the whole build: where each input lives in a 10-K, how to lay the inputs out, the order to build the three statements, what the balance check's error pattern tells you, the interest circularity and the toggle that keeps it from breaking, and a full worked model with three projected years that balances to zero. Then a two hour time budget, the errors that fail tests, and what the grader opens first.

## What is a three statement model?

A three statement model is a spreadsheet that projects a company's income statement, balance sheet and cash flow statement together, so that a change in one shows up correctly in the other two. **A three statement model is one connected machine, not three tables sitting side by side: revenue assumptions drive profit, profit and spending drive cash, and cash and debt land back on the balance sheet.** Banks use it as the base layer under a [DCF](https://www.wallstreetguide.net/post/walk-me-through-a-dcf-the-7-step-answer-that-works), an [LBO](https://www.wallstreetguide.net/post/walk-me-through-an-lbo-the-6-step-answer-interviewers-want-to-hear) and a merger model, and corporate finance teams run the same build for budgets. That's why it's the first thing a modeling test asks for.

## How long does a three statement modeling test take?

Most run between one and three hours, and 90 minutes or two hours are the formats I see most often for Summer Analyst and first-year roles. **A two hour three statement modeling test expects a working model that balances, with a simple debt schedule and a check row, not a fully built valuation.** A few firms send a take-home version with several hours and a short write-up, and private equity firms usually put an LBO on top. The prompt states the time limit, and your first job is to size the build to it.

## 1. The three statements connect through six links, and the test checks every one

Before you touch Excel, you need the links cold. Every three statement model, whether it's a 90 minute test build or a bank's merger model, runs on the same six connections. Here they are in the order they come up when you build.

**Link 1: net income goes to two places.** Net income is the last line of the income statement. It becomes the first line of the cash flow statement, because the cash flow statement starts from accounting profit and then adjusts it toward actual cash. It also flows into retained earnings on the balance sheet, which is the pile of past profits the company has kept rather than paid out. Retained earnings at year end equal retained earnings at the start, plus net income, minus dividends. Say a company earns $100 and pays a $25 dividend: the cash flow statement starts at 100, and retained earnings rise by 75.

**Link 2: depreciation and amortization cuts profit, comes back as cash, and shrinks PP&E.** Depreciation spreads the cost of a factory or a machine over the years it gets used. Amortization does the same for intangible assets like software or patents. Together they're D&A, and they show up three times. On the income statement D&A is an expense, so it lowers operating profit. On the cash flow statement it's added back to net income, because no cash left the building this year (the cash left when the asset was bought). On the balance sheet it lowers net PP&E (property, plant and equipment), the book value of the company's physical assets. If D&A is $44, operating profit falls by 44, the cash flow statement adds 44 back, and net PP&E drops by 44.

**Link 3: capex raises PP&E and uses cash, and skips the income statement.** Capital expenditure, or capex, is money spent buying or building long-lived assets. It's an outflow in the investing section of the cash flow statement, and it raises PP&E on the balance sheet by the same amount. It doesn't touch the income statement in the year you spend it. The expense arrives later, a slice at a time, through depreciation. Spend $55 on new equipment: investing cash flow shows negative 55, net PP&E goes up 55, and the income statement doesn't move. So each year, ending net PP&E equals beginning net PP&E plus capex minus D&A. That one equation is the whole PP&E schedule.

**Link 4: changes in working capital turn balance sheet movements into cash.** Working capital is the short-term stuff the business runs on: receivables (money customers owe you), inventory (product you've paid for but haven't sold), and payables (money you owe suppliers). When receivables grow, you booked revenue you haven't collected yet, so cash is lower than profit suggests, and the cash flow statement subtracts the increase. Same for inventory. When payables grow, you've used supplier money instead of your own, so the cash flow statement adds the increase. If receivables rise $10 and payables rise $4, the operating section shows negative 10 and positive 4.

**Link 5: debt moves through the financing section onto the balance sheet.** Borrow $100 and the financing section shows positive 100 while debt on the balance sheet rises 100. Repay $30 and both go the other way. The interest on that debt is a separate link: it's an expense on the income statement, computed off the debt balance on the balance sheet, which is where the circularity in section 7 comes from.

**Link 6: the cash flow statement's last line becomes the balance sheet's first.** Add up operating, investing and financing cash flows and you get the net change in cash. Beginning cash plus the net change equals ending cash, and that ending cash is the cash line on the balance sheet. If every other link is right, the balance sheet balances. If it doesn't balance, one of these six is broken.

Here's why that last sentence is true. Interviewers ask about this mechanism too. Every entry in the system has a partner. Profit raises retained earnings (equity) and, through the cash flow statement, raises cash (an asset). Capex lowers cash and raises PP&E, both assets, so total assets don't change. Borrowing raises cash and raises debt. Each link moves assets and the other side by matching amounts, so assets equal liabilities plus equity as long as every link is present and has the right sign. **A balance sheet that balances is proof the six links are complete, and one that doesn't tells you which link is missing.**

If the accounting behind these links feels shaky, work through our [50 accounting interview questions](https://www.wallstreetguide.net/post/50-accounting-interview-questions-that-you-should-practice-before-your-interview) first. The model gets much easier once "walk me through $10 of depreciation" feels automatic.

## 2. Every input for a three statement model lives in a predictable place in the 10-K

In a timed modeling test the inputs usually come from a case pack, which I'll cover at the end of this section. In a real model, and in most take-home tests, you start from the company's annual report to the SEC, the 10-K. Knowing where things sit saves twenty minutes of scrolling.

- **The three statements: Item 8, "Financial Statements and Supplementary Data."** The income statement (often titled the statement of operations), the balance sheet, the cash flow statement and the statement of shareholders' equity sit together here, with the notes right after. Pull three years of income statement and cash flow and two years of balance sheet, which is what one filing gives you. If you want a third balance sheet year, it's in the prior year's 10-K.
- **D&A: the cash flow statement, operating section.** Many companies bury depreciation inside cost of sales and SG&A, so the income statement may not have a D&A line at all. The cash flow statement always shows it as an add-back, usually labeled "depreciation and amortization." Take it from there.
- **Capex: the cash flow statement, investing section.** Labeled "purchases of property and equipment" or "capital expenditures." Some companies split it between property and capitalized software. Add the pieces.
- **Debt: the debt footnote.** A note titled "Debt" or "Borrowings." It lists each tranche (each separate loan or bond), its interest rate, its maturity, the size of the revolving credit facility and how much is drawn. Your interest rate assumption and your repayment schedule come from here. The note also has a table of principal due in each of the next five years. Those scheduled repayments are what bankers call amortization, and that table is your amortization row.
- **Share count: the cover page, then the EPS note.** The 10-K's cover page states shares outstanding as of a recent date, the number you want for equity value. The earnings per share note gives the weighted average shares, basic and diluted, which you need only if the test asks for EPS.
- **Tax rate: the income taxes footnote.** Find the effective tax rate reconciliation, a table that starts at the statutory rate (21 percent federal in the US [VERIFY: federal statutory corporate rate at publish]) and walks to the rate the company actually paid. Use the effective rate from a normal year, not one with a large one-time charge.
- **Working capital detail: the face of the balance sheet, plus the balance sheet components note.** Receivables, inventory and payables are on the balance sheet itself. The note breaks out prepaid expenses, accrued liabilities and deferred revenue if the test wants them.
- **Guidance and the story: Item 7, the MD&A.** MD&A stands for Management's Discussion and Analysis, the section where management tells you what drove revenue, what happened to margins, and what capex they plan next year. When a prompt says "use management's guidance," this is where it is. The latest earnings release and the 10-Q (the quarterly filing) update it.
- **Leases: the leases footnote.** Under current US accounting rules, operating leases sit on the balance sheet as a right-of-use asset and a lease liability. In a two hour test, hold them flat or grow them with revenue unless the prompt says otherwise.

**Where the test gives you a case pack instead.** Most timed tests hand you a PDF of three to five pages: a paragraph on the company, two or three years of summarized financials (often already collapsed to ten or fifteen lines), and a list of assumptions. "Revenue grows 8 percent a year, gross margin holds at 40 percent, capex is 5 percent of revenue, the company keeps $50 million of minimum cash." Some tests give you a 10-K excerpt and make you find the numbers yourself. That's the harder version, and the list above is how you do it fast. **Read the case pack twice and write down every output it asks for before you open Excel, because the most common way to fail a modeling test is to build the wrong thing well.**

## 3. Input historicals so you can trace every number back to the filing

Three habits for the historical columns, in order.

**Three years of history, collapsed to the lines you need.** A 10-K income statement can run 25 lines. Your model wants about a dozen: revenue, cost of goods sold, gross profit, SG&A, EBITDA, D&A, EBIT, interest expense, interest income, pre-tax income, taxes, net income. Fold the company's small lines into yours (research and development plus selling, general and administrative become one operating cost line if the prompt doesn't care about the split). Keep a notes column at the far right that says what you combined, so a grader who asks "where did 250 come from?" gets an answer in one click.

**Pick a sign convention and never break it.** Two ways work. Show costs as negative numbers and compute every subtotal as a plain SUM, or show costs as positive numbers and subtract them. Mixing the two is how a model ends up adding cost of goods sold to gross profit. I teach the first way for tests: negatives for anything that reduces profit or cash, SUM for every subtotal, so the sign is visible in the cell and the formula stays boring.

**One units line, one period line.** Put "$ in millions" once at the top and keep every number in millions, including share counts (millions of shares) and per share figures (dollars). Write the years across row 2 as 2025A, 2026E, 2027E, 2028E, with A for actual and E for estimate, and build every formula to reference that row rather than typing a year anywhere else. When you paste from a 10-K, check the units before anything else. A company reporting in thousands will hand you revenue of 1,000,000 where you want 1,000.

Two smaller things. Type historical numbers in blue, the convention for a hardcoded input (a number typed in rather than calculated). And once the historicals are in, add a check row under the historical balance sheet: total assets minus total liabilities and equity. **If the company's own filed balance sheet doesn't balance in your sheet, you've mistyped a number, and you want to know that before you build three years on top of it.**

## 4. The assumptions block drives the whole three statement model

Every projected number should trace back to a small block of assumptions at the top of the sheet. The grader reads this block second, right after the balance check, because it shows whether you understand the business or just extended lines. For each driver, compute the historical ratio first, then pick a projection.

- **Revenue growth.** Historical growth is this year's revenue divided by last year's, minus one. Project a rate per year, trending toward a steady number. In the worked example below: 10, 8 and 6 percent.
- **Gross margin.** Gross profit divided by revenue. Hold it flat unless the prompt gives you a reason to move it. Cost of goods sold is then revenue times one minus the margin.
- **SG&A as a percent of revenue.** Operating costs scale with the business. If the prompt gives you fixed and variable costs, split them. Otherwise one percentage is fine.
- **D&A as a percent of revenue, or of beginning PP&E.** Percent of revenue is faster and what most tests expect. Percent of beginning net PP&E is more correct, because depreciation comes from the assets you own, not the revenue you earn. Either way, check that D&A and capex make sense together. A company spending 12 percent of revenue on capex and depreciating 4 percent is growing its asset base fast, which is fine if that's the story and strange if it isn't.
- **Capex as a percent of revenue.** Historical capex (from the investing section) divided by revenue. Capex above D&A means the asset base is growing. Capex below D&A means it's shrinking.
- **Working capital through days.** Days sales outstanding (DSO) is receivables divided by revenue, times 365: the average number of days a customer takes to pay. Days inventory outstanding (DIO) is inventory divided by cost of goods sold, times 365: how many days of product sit on the shelf. Days payable outstanding (DPO) is payables divided by cost of goods sold, times 365: how long the company takes to pay suppliers. Compute each from the last historical year, round to a sensible number, and hold it. Projected receivables are then revenue times DSO divided by 365, and the same shape for the other two. If last year's receivables were 125 on revenue of 1,000, DSO is 45.6 days, and 45 is a defensible assumption.
- **Tax rate.** The effective rate from the tax footnote, applied to pre-tax income. If pre-tax income goes negative, taxes should go to zero rather than negative. Wrapping the formula in MAX(0, ...) handles it.
- **Interest rate on debt and on cash.** Debt rate from the debt footnote or the prompt. Cash earns something small; 2 percent is a common placeholder.
- **Debt repayment, dividends and buybacks.** Mandatory amortization from the debt footnote's maturity table. Dividends as a percent of net income (the payout ratio) or a flat dollar amount. Buybacks only if the prompt asks.
- **Minimum cash.** The balance the company must keep on hand to operate. The revolver (a credit line the company draws when cash runs short, built in section 5) exists to protect this number.

**Judgment shows in the assumptions block, so keep every projected driver in one place and make each one defensible in a sentence.** "Gross margin holds at 40 percent because the three historical years were 39.8, 40.1 and 40.0" is a sentence a grader believes.

## 5. Build the three statement model in this order: income statement, balance sheet without cash, cash flow statement, cash back to the balance sheet, then the revolver

Order matters because each statement needs something from the one before it. Build out of order and you'll find yourself referencing a cell that doesn't exist yet.

**Step 1: the income statement, down to net income.** Revenue is last year's times one plus growth. Cost of goods sold is revenue times one minus gross margin. Gross profit is the sum. SG&A is revenue times its percentage. EBITDA is gross profit minus SG&A (if EBITDA is new to you, our [EBITDA explainer](https://www.wallstreetguide.net/post/ebitda-explained-for-finance-interviews-what-they-actually-want-to-hear) covers what it does and doesn't tell you). D&A is revenue times its percentage. EBIT is EBITDA minus D&A. Interest expense, for now, is the rate times last year's ending debt, which gives a real number without a circularity. Interest income is the rate times last year's ending cash. Then pre-tax income, taxes at the rate, net income. Add a dividends line under net income so the retained earnings link has what it needs.

**Step 2: the two supporting schedules.** Two small tables under the income statement. PP&E: beginning balance (last year's ending), plus capex (revenue times the capex percent), minus D&A (from the income statement), equals ending. Working capital: receivables, inventory and payables from the days assumptions, with a line under each for the year-over-year change. Here's what those two schedules look like in the sheet, with each row's 2026 formula written out beside it.

![Excel PP&E and working capital schedules with the 2026 formulas shown beside each row](published/assets/images/three-statement-model-modeling-test/01-schedules.png "The two schedules under the income statement, with each row's 2026 formula beside it: the PP&E roll is beginning plus capex minus D&A, and receivables are revenue times DSO over 365.")

**Step 3: the balance sheet, except cash and the revolver.** Receivables, inventory and net PP&E link to the schedules. Payables link too. The term loan is last year's balance minus this year's amortization. Common stock stays flat unless there are buybacks or issuance. Retained earnings is beginning plus net income minus dividends, and you can fill it in now because net income exists. Leave cash and the revolver blank. They come from the cash flow statement.

**Step 4: the cash flow statement.** Operating section: net income, plus D&A, minus the increase in receivables, minus the increase in inventory, plus the increase in payables. Investing section: minus capex. Financing section: minus amortization, minus dividends, plus revolver draws, minus revolver repayments (leave the revolver lines at zero until step 6). Sum the three sections for the net change in cash.

**Step 5: cash back to the balance sheet.** Ending cash equals last year's cash plus the net change. Link the balance sheet cash cell to it. Now add the check row: total assets minus total liabilities and equity. It should read zero in every year. If it doesn't, stop and fix it before building anything else, using section 6.

![Close-up of the balance check row in Excel: total assets minus total liabilities and equity, 0.0 in every year](published/assets/images/three-statement-model-modeling-test/02-balance-check-row.png "The check row is one subtraction, total assets minus total liabilities and equity, and it reads 0.0 in every year before the revolver is even built.")

**Step 6: the revolver plug.** A revolver is a revolving credit line, a corporate credit card the company draws when cash runs short and repays when cash comes back. In the model it does one job: keeping cash from falling below the minimum. Three rows handle it. First, cash before the revolver: beginning cash plus everything on the cash flow statement except the revolver lines. Second, the draw: if cash before the revolver is below the minimum, draw the difference, otherwise zero. In Excel, =MAX(0, minimum cash minus cash before revolver). Third, the repayment: if cash before the revolver is above the minimum and a revolver balance is outstanding, repay the smaller of the excess and the balance, so =MIN(beginning revolver, MAX(0, cash before revolver minus minimum cash)). Ending revolver is beginning plus draw minus repayment, and it links to the balance sheet. The draw and repayment link into the financing section, which changes the net change in cash, which changes ending cash, which now lands exactly on the minimum in any year the revolver is used. Check row still zero? Then the model is built.

![Excel debt and revolver block showing cash before revolver, the MAX draw formula, the MIN repayment formula and ending balances](published/assets/images/three-statement-model-modeling-test/03-revolver-block.png "The revolver block in the sheet: cash before the revolver is 16.4 in 2027, so the MAX formula draws 33.6, and in 2028 the MIN formula repays 19.0 of it.")

A note on what "plug" means here, because interviewers ask. Cash is called the plug because it's the one balance sheet line you don't project directly. It's whatever the cash flow statement says it is. The revolver is the plug on the other side: whatever borrowing is needed to hold cash at the minimum. Neither is a fudge. Both are computed from everything else. **A plug the model computes is a link, and a plug you type in to force the balance sheet to balance is a failure that graders find in under a minute.**

## 6. The balance check row tells you what kind of mistake you made

The check row (total assets minus total liabilities and equity, every year) is the most useful cell in the model, and not only because the grader reads it first. The pattern of the error tells you where to look.

**A constant difference in every projected year means a one-time break, usually in the first year.** Say the check reads 12.0 in 2026, 12.0 in 2027 and 12.0 in 2028. Something happened once and the model has carried it forward. The usual causes: a historical balance typed wrong (which is why section 3 told you to check the filed balance sheet), first-year retained earnings linked to the wrong starting cell, or a one-time item in year one (a debt issuance, an asset sale) that hit the cash flow statement but not the balance sheet, or the reverse. Here's the pattern in a sheet where 2025 net PP&E was typed as 412.0 instead of 400.0.

![Balance sheet in Excel with net PP&E mistyped as 412.0, so the check row reads 12.0 in every year](published/assets/images/three-statement-model-modeling-test/04-error-constant.png "The constant pattern: 2025 net PP&E was typed as 412.0 instead of 400.0, and the check row carries the same 12.0 into every projected year.")

**A growing difference means a recurring link is missing or has the wrong sign.** If the check reads 44.0, then 91.5, then 141.9, a flow that happens every year isn't reaching one side. Look at the amounts. 44.0 is 2026's D&A. The D&A add-back is missing from the cash flow statement, or PP&E isn't being reduced by it. **When the first bad year's difference matches a line item exactly, that line is the missing link, and when it's exactly double a line item, the sign is wrong.** Double because adding 20.9 of dividends where you should have subtracted them moves cash 41.8 away from where it belongs. Here's the second of those two causes in a sheet: the PP&E roll adds capex but never subtracts D&A.

![Balance sheet in Excel where the PP&E roll never subtracts D&A, so the check row reads 44.0, 91.5 and 141.9](published/assets/images/three-statement-model-modeling-test/05-error-growing.png "The growing pattern: the PP&E roll never subtracts D&A, so the check row grows by each year's D&A, 44.0, then 91.5, then 141.9.")

**A difference that appears in one year and then stays flat is a one-off in that year.** If the 2027 expansion capex in the worked example had been typed into PP&E and never put on the cash flow statement, the check would jump to 142.6 in 2027 and sit at 142.6 in 2028: the constant pattern, starting late.

The procedure, in order. Read the check row and classify the pattern. Compare the first bad year's difference to each line on the cash flow statement. Press F2 on the suspect cell to see what it references. Fix the one link. Watch the check row. If the difference moves instead of disappearing, you had two errors, and you've just learned the second one's size.

![Line chart of two balance check patterns: a flat line at 12.0 and a rising line from 44.0 to 141.9](published/assets/images/three-statement-model-modeling-test/06-check-patterns.png "Read the shape before the number: a flat line means something broke once, and a line that climbs by about the same amount each year means a recurring link is missing.")

A junior I worked with last spring, call him T, sent me a practice model with a check row reading 20.9, 44.1, 68.7. He'd computed dividends under net income, subtracted them from retained earnings, and never put them on the cash flow statement. Growing pattern, first-year difference equal to one line item. Once he could read the pattern, the fix took about thirty seconds, and he passed the real thing, a two hour build at a middle market bank, six weeks later.

## 7. Interest on average debt creates a circularity, so build the toggle before you need it

Here's the loop. The most accurate way to compute interest is on the average of beginning and ending debt, because the company carries different balances through the year. But ending debt includes the revolver. The revolver depends on cash before the revolver. That depends on net income. Net income depends on interest. Interest depends on ending debt. The chain closes on itself. In Excel that's a circular reference: a formula that, several steps removed, depends on its own result.

Excel handles it two ways, and you should know both.

**Iterative calculation.** Under File, Options, Formulas, turn on "Enable iterative calculation." Excel then recalculates the loop over and over until the numbers stop changing (the default stops after 100 passes or when the change drops below 0.001). A three statement model converges in a handful of passes. The risk is what happens when any cell in the loop shows an error. A #REF! from a deleted row, a #DIV/0! from a zero denominator, a #VALUE! from a stray letter: the error circulates, and within one recalculation every cell in the loop shows an error too. Fixing the original cell doesn't clear it, because the errors now feed each other.

**The toggle.** Put a cell at the top of the assumptions block labeled "Circularity" with a 1 or a 0 in blue. Write interest expense as the rate times IF(toggle=1, AVERAGE(beginning debt, ending debt), beginning debt). With the toggle at 1, interest uses the average and the model is circular. With the toggle at 0, interest uses only beginning debt, which is last year's known number, so the loop is broken and no circular reference exists. When the model fills with errors, set the toggle to 0, let them clear, fix the broken cell, and set it back to 1. **The circularity toggle is the one piece of a three statement model you build before you need it, because by the time you need it the model is already full of errors.**

![Close-up of the circularity toggle cell set to 0 and the interest expense formula that reads it](published/assets/images/three-statement-model-modeling-test/07-toggle-closeup.png "The toggle sits at the top of the drivers block, and interest expense reads it: with a 0 in D5 the IF picks beginning debt and the model has no circular reference.")

How much does the average balance buy you? In the worked example below, 2026 interest expense is 18.0 on beginning debt (6 percent of 300) and 17.1 on the average (6 percent of 285, since the term loan amortizes 30 during the year). Net income moves by 0.7 on 83.7. That's the whole difference, and it's why plenty of bank templates run interest on beginning balances and skip the circularity. For a two hour test my advice is beginning balance by default, or average with the toggle built and set to 1 only after the check row reads zero.

Interest income on cash makes the same loop in the other direction (cash depends on income, which depends on interest income, which depends on cash), so apply the same choice there.

## 8. Formatting conventions a grader notices in the first thirty seconds

Formatting isn't decoration. **Formatting is how a grader tells inputs from calculations without clicking every cell, and it's how you catch your own mistakes before they do.**

- **Blue for hardcoded inputs, black for formulas, green for links to other sheets.** Every historical number and every assumption is blue. Every calculated cell is black. If your test uses one sheet, green won't appear. A grader who finds a black cell holding a typed number, or a blue cell holding a formula, stops trusting the color code and starts clicking everything.
- **One formula across each row.** Write the 2026 formula once and fill it right through 2028. Every year's cell in a row should carry the same formula, shifted one column. If one year differs, there's a reason or there's a mistake, and the grader assumes the mistake.
- **Years across the top, line items down the side.** Historical columns to the left of projected columns, and the assumptions block in the same column structure as the statements, so 2026's growth rate sits above 2026's revenue.
- **No hardcodes inside formulas.** =E12*1.08 is a hardcode: the grader can't see the 8 percent, can't change it and can't check it. =E12*(1+F5), with F5 holding 8 percent in blue, is the right form.
- **Totals as sums of what sits above them.** Gross profit is =SUM(revenue, COGS) with COGS negative, not revenue minus COGS with COGS positive in one place and negative in another. Total assets is a SUM of the asset lines. When a total is a SUM, you can see at a glance whether the range caught every line.
- **Round for display, never in the cell.** Show one decimal or whole numbers with Excel's number format and keep full precision underneath. Type a rounded number from one cell into another and the model stops tying, which is exactly the error the check row exists to catch.
- **A memo line beats a buried formula.** "Cash before revolver" deserves its own row. So does free cash flow (cash from operations minus capex). Rows are free, and a formula you can read beats one you have to decode.

Two numbers for perspective. Excel gives you [1,048,576 rows and 16,384 columns](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3) per worksheet. A complete three statement model with a debt schedule and a check row uses about 100 rows and ten columns. Graders aren't impressed by a big model. They're impressed by one they can read in ninety seconds.

And the spreadsheet itself was invented for exactly this job. Dan Bricklin came up with VisiCalc, the first spreadsheet program, as an MBA student at Harvard Business School in 1978, after watching a professor rework a financial model on a blackboard one number at a time. He and Bob Frankston released it for the Apple II in October 1979. Change one input and watch everything downstream recalculate: that was the whole pitch in 1979, and it's still what a three statement model does.

## 9. A full worked three statement model, with numbers that tie

Here's the whole build on a fictional company, in $ millions. I ran the numbers in a script before pasting them in, so every statement ties and the check row is zero in all three projected years. Figures are shown to one decimal. The model carries full precision underneath, so if you re-add a column by hand you'll occasionally land 0.1 off. That's rounding, not an error, and it's one more reason never to type a displayed number into another formula.

**The assumptions**

| Driver | 2025A (historical) | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| Revenue growth | n/a | 10% | 8% | 6% |
| Gross margin | 40.0% | 40% | 40% | 40% |
| SG&A, % of revenue | 25.0% | 25% | 25% | 25% |
| D&A, % of revenue | 4.0% | 4% | 4% | 4% |
| Capex, % of revenue | 5.0% | 5% | 12% | 5% |
| DSO (days, on revenue) | 45.6 | 45 | 45 | 45 |
| DIO (days, on COGS) | 60.8 | 60 | 60 | 60 |
| DPO (days, on COGS) | 30.4 | 30 | 30 | 30 |
| Tax rate | 20% | 20% | 20% | 20% |
| Interest rate on debt (beginning balance) | 6% | 6% | 6% | 6% |
| Interest rate on cash (beginning balance) | n/a | 2% | 2% | 2% |
| Term loan amortization | n/a | 30.0 | 30.0 | 30.0 |
| Dividend payout, % of net income | 25% | 25% | 25% | 25% |
| Minimum cash | n/a | 50.0 | 50.0 | 50.0 |
| Circularity toggle | n/a | 0 | 0 | 0 |

![Excel drivers block for the worked example: growth, margins, days, tax, interest rates, amortization, payout and minimum cash by year](published/assets/images/three-statement-model-modeling-test/08-drivers.png "The whole model hangs off this block: blue cells are typed assumptions, the 2025A column is the historical ratio each one is based on, and the toggle at the top stays at 0.")

The 2027 capex jump is on purpose: an expansion year, so you can watch the revolver work. Tax is 20 percent to keep the arithmetic easy to follow; in a real test use the company's effective rate. The historical column shows the implied ratios (receivables of 125 on revenue of 1,000 is a DSO of 45.6), which is how you'd justify the 45.

**Income statement**

| Line | 2025A | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| Revenue | 1,000.0 | 1,100.0 | 1,188.0 | 1,259.3 |
| Cost of goods sold | -600.0 | -660.0 | -712.8 | -755.6 |
| Gross profit | 400.0 | 440.0 | 475.2 | 503.7 |
| SG&A | -250.0 | -275.0 | -297.0 | -314.8 |
| EBITDA | 150.0 | 165.0 | 178.2 | 188.9 |
| D&A | -40.0 | -44.0 | -47.5 | -50.4 |
| EBIT | 110.0 | 121.0 | 130.7 | 138.5 |
| Interest expense | -18.0 | -18.0 | -16.2 | -16.4 |
| Interest income | 2.0 | 1.6 | 1.7 | 1.0 |
| Pre-tax income | 94.0 | 104.6 | 116.2 | 123.1 |
| Taxes (20%) | -18.8 | -20.9 | -23.2 | -24.6 |
| Net income | 75.2 | 83.7 | 93.0 | 98.5 |
| Dividends (25% payout) | -18.8 | -20.9 | -23.2 | -24.6 |

![Excel income statement for 2025A to 2028E from revenue of 1,000.0 down to net income of 98.5 and dividends](published/assets/images/three-statement-model-modeling-test/09-income-statement.png "The same income statement in the sheet: costs are negative, every subtotal is a SUM, and only the 2025A column is typed in blue.")

Walk the first projected year. Revenue: 1,000 times 1.10 is 1,100. COGS: 60 percent of 1,100 is 660. Gross profit 440. SG&A at 25 percent is 275, so EBITDA is 165. D&A at 4 percent is 44, so EBIT is 121. Interest expense is 6 percent of beginning debt (the 300 term loan, no revolver yet): 18.0. Interest income is 2 percent of beginning cash (80): 1.6. Pre-tax income is 121 minus 18 plus 1.6, or 104.6. Tax at 20 percent is 20.9. Net income 83.7. Dividends at 25 percent, 20.9.

Look at 2028's interest. It's 6 percent of 273.6, the 240 term loan plus the 33.6 of revolver outstanding at the end of 2027, which gives 16.4. That's last year's revolver draw showing up in this year's interest, exactly the way the links say it should.

**Balance sheet**

| Line | 2025A | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| Cash | 80.0 | 86.9 | 50.0 | 50.0 |
| Accounts receivable | 125.0 | 135.6 | 146.5 | 155.3 |
| Inventory | 100.0 | 108.5 | 117.2 | 124.2 |
| Net PP&E | 400.0 | 411.0 | 506.0 | 518.6 |
| Total assets | 705.0 | 742.0 | 819.7 | 848.1 |
| Accounts payable | 50.0 | 54.2 | 58.6 | 62.1 |
| Revolver | 0.0 | 0.0 | 33.6 | 14.6 |
| Term loan | 300.0 | 270.0 | 240.0 | 210.0 |
| Common stock | 100.0 | 100.0 | 100.0 | 100.0 |
| Retained earnings | 255.0 | 317.8 | 387.5 | 461.4 |
| Total liabilities and equity | 705.0 | 742.0 | 819.7 | 848.1 |
| Balance check (assets minus liabilities and equity) | 0.0 | 0.0 | 0.0 | 0.0 |

![Excel balance sheet for 2025A to 2028E with the revolver at 33.6 in 2027 and a 0.0 check row](published/assets/images/three-statement-model-modeling-test/10-balance-sheet.png "The balance sheet with the check row underneath: cash lands on the 50.0 minimum in 2027 and 2028 because the revolver is doing its job, and the check reads 0.0 across.")

The 2026 balance sheet, line by line. Receivables: revenue of 1,100 times 45 divided by 365 is 135.6. Inventory: COGS of 660 times 60 over 365 is 108.5. Payables: 660 times 30 over 365 is 54.2. Net PP&E: 400 plus capex of 55 minus D&A of 44 is 411.0. Term loan: 300 minus 30 is 270. Retained earnings: 255 plus 83.7 minus 20.9 is 317.8. Cash is whatever the cash flow statement says, which is next.

**Cash flow statement**

| Line | 2026E | 2027E | 2028E |
|---|---|---|---|
| Net income | 83.7 | 93.0 | 98.5 |
| Plus: D&A | 44.0 | 47.5 | 50.4 |
| Less: increase in receivables | -10.6 | -10.8 | -8.8 |
| Less: increase in inventory | -8.5 | -8.7 | -7.0 |
| Plus: increase in payables | 4.2 | 4.3 | 3.5 |
| Cash from operations | 112.8 | 125.3 | 136.6 |
| Capex | -55.0 | -142.6 | -63.0 |
| Cash from investing | -55.0 | -142.6 | -63.0 |
| Term loan amortization | -30.0 | -30.0 | -30.0 |
| Revolver draw | 0.0 | 33.6 | 0.0 |
| Revolver repayment | 0.0 | 0.0 | -19.0 |
| Dividends | -20.9 | -23.2 | -24.6 |
| Cash from financing | -50.9 | -19.6 | -73.6 |
| Net change in cash | 6.9 | -36.9 | 0.0 |
| Memo: cash before revolver | 86.9 | 16.4 | 69.0 |

![Excel cash flow statement for 2026E to 2028E with operating, investing and financing sections and ending cash](published/assets/images/three-statement-model-modeling-test/11-cash-flow-statement.png "The cash flow statement with beginning and ending cash rows added, so the 2026 ending cash of 86.9 is visibly 80.0 plus the 6.9 net change.")

2026: net income 83.7, plus D&A 44.0, minus the 10.6 increase in receivables (135.6 minus 125.0), minus the 8.5 increase in inventory, plus the 4.2 increase in payables, gives 112.8 from operations. Capex takes 55.0. Amortization takes 30.0 and dividends 20.9. Net change plus 6.9, so ending cash is 80 plus 6.9, or 86.9. That's above the 50 minimum, so the revolver stays at zero.

![Waterfall chart of 2026 cash flow from net income of 83.7 through each flow to ending cash of 86.9](published/assets/images/three-statement-model-modeling-test/12-cash-waterfall-2026.png "Walk the 2026 column as a bridge: operations bring in 112.8, capex, amortization and dividends take 105.9 of it back out, and cash ends the year 6.9 higher at 86.9.")

2027, the expansion year: operations bring in 125.3, but capex is 142.6 (12 percent of 1,188), amortization is 30.0 and dividends are 23.2. Cash before the revolver is 86.9 plus 125.3 minus 142.6 minus 30.0 minus 23.2, which is 16.4. That's 33.6 below the minimum, so the revolver draws 33.6 and ending cash lands at exactly 50.0.

2028: operations 136.6, capex 63.0, amortization 30.0, dividends 24.6. Cash before the revolver is 50.0 plus 136.6 minus 63.0 minus 30.0 minus 24.6, which is 69.0. That's 19.0 above the minimum, so the revolver repays 19.0 of its 33.6 balance, leaving 14.6, and cash sits at 50.0 again.

Now go back to the balance sheet and read the check row: 0.0, 0.0, 0.0. **When every link is in place, the balance sheet balances on its own, and that is the entire test of whether the model works.**

**What the toggle changes**

Same model, toggle set to 1, interest on the average of beginning and ending debt.

| Line | 2026E (toggle 0) | 2026E (toggle 1) | 2027E (toggle 0) | 2027E (toggle 1) | 2028E (toggle 0) | 2028E (toggle 1) |
|---|---|---|---|---|---|---|
| Interest expense | 18.0 | 17.1 | 16.2 | 16.3 | 16.4 | 14.9 |
| Net income | 83.7 | 84.4 | 93.0 | 92.9 | 98.5 | 99.7 |
| Revolver (ending) | 0.0 | 0.0 | 33.6 | 33.1 | 14.6 | 13.2 |
| Cash (ending) | 86.9 | 87.4 | 50.0 | 50.0 | 50.0 | 50.0 |
| Balance check | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

Interest on the average balance is lower in 2026 (debt falls during the year) and a touch higher in 2027 (the revolver draw lifts average debt). Net income moves by less than one in every year, the revolver draw changes by half a million, and the check row is zero either way. **The circularity changes the answer by tenths and changes the model's failure risk by a lot, which is why beginning balance interest is the right default in a timed test.**

## 10. What to add and what to skip in a two to three hour modeling test

The prompt decides, but when it leaves room, here's the order of priority.

**Add, in this order:**

1. The check row. First, not last.
2. A revolver plug with a minimum cash assumption.
3. A simple debt schedule: one term loan with amortization, one revolver, interest on the beginning balance (or on the average, with the toggle).
4. A PP&E schedule and a working capital schedule, since those are the two places models go wrong.
5. Memo lines: cash before revolver, free cash flow.
6. A basic sensitivity table if time allows: a small grid showing how 2028 ending cash or net income moves across two revenue growth cases and two margin cases.
7. A short outputs block at the top: 2028 revenue, EBITDA, net income, ending cash, ending debt.

**Skip unless the prompt asks:**

- Segment builds (revenue by product line or region). One revenue line.
- Detailed tax schedules (deferred taxes, net operating losses). One effective rate.
- Stock based compensation detail. Treat it as a cost inside SG&A and add it back on the cash flow statement only if the historicals do.
- Multiple debt tranches with different rates and a payment order. One term loan plus a revolver.
- Share count roll-forwards and EPS.
- Quarterly periods.
- Scenario switches (base, upside, downside). A sensitivity table answers the same question in a fraction of the time.
- Leases, pensions and equity method investments. Hold them flat.

**A correct simple model beats an incorrect ambitious one, because the grader is deciding whether to trust you with a live model on Monday, not whether you can build every schedule in the textbook.**

## 11. A time budget for a two hour three statement modeling test

**Students who run out of time are almost never slow at Excel: they spend thirty minutes on a segment schedule nobody asked for, then rush the links.** Here's the split I give students for a two hour build.

| Clock | Task |
|---|---|
| 0:00 to 0:10 | Read the prompt twice. Write every requested output on paper. Sketch the layout: assumptions on top, statements below, schedules at the bottom. |
| 0:10 to 0:30 | Input the historicals in blue. Compute historical ratios. Type the projection assumptions in blue. Add the historical balance check. |
| 0:30 to 0:50 | Income statement down to net income and dividends. PP&E schedule. Working capital schedule. |
| 0:50 to 1:10 | Balance sheet except cash and revolver. Cash flow statement with revolver lines at zero. |
| 1:10 to 1:25 | Link ending cash to the balance sheet. Add the check row. Fix until it reads zero in every year. |
| 1:25 to 1:40 | Debt schedule and revolver. Link draws and repayments into financing. Check row again. |
| 1:40 to 1:50 | Sanity pass: margins trend sensibly, cash never drops below the minimum, debt never goes negative, capex and D&A make sense together. Set revenue growth to zero in every year and confirm the model still balances, then set it back. |
| 1:50 to 2:00 | Formatting pass (colors, number formats, one formula per row). Outputs block. Save with the filename the prompt asked for. Sensitivity table only if there's time left. |

Save every fifteen minutes regardless. A model that balanced at 1:38 and crashed at 1:52 is worth nothing if the last save was at 0:40.

For a 90 minute test, compress the middle: ten minutes less on inputs, ten less on statements, and skip the sensitivity entirely. For a three hour test, the extra hour goes to a DCF or an LBO on top of the operating model, not to a fancier operating model. Our [LBO walkthrough](https://www.wallstreetguide.net/post/walk-me-through-an-lbo-the-6-step-answer-interviewers-want-to-hear) covers what sits on top when the test is for a private equity seat.

## 12. The errors that fail modeling tests

**Most failed modeling tests fail on one of a short list of mechanical errors, and each one has a mechanism you can learn to see coming.** Here's the list, with the mechanism, because knowing why something breaks is how you stop doing it.

- **The balance sheet doesn't balance, and the candidate types a number to make it balance.** Graders click the check row's inputs and find the typed plug immediately. An honest model with a 12.0 imbalance and a note saying "check off by 12.0, likely dividends, out of time" scores better than a forced zero, because the first shows judgment and the second shows a willingness to hide.
- **Sign errors on the cash flow statement.** An increase in receivables added instead of subtracted. An increase in payables subtracted instead of added. The tell is a check row that's off by exactly double a working capital change.
- **Hardcodes inside formulas.** =E12*1.08 and its cousins. The JPMorgan model from the opening ran on numbers pasted by hand from one sheet to the next, and the bank's own report calls that out as an operational flaw before it even gets to the formula error. A number that lives inside a formula can't be seen, changed or audited.
- **Capex that never reaches PP&E, or D&A that gets counted twice.** Capex on the cash flow statement but PP&E held flat is a growing imbalance equal to each year's capex. D&A subtracted from PP&E and also subtracted from the cash flow statement (instead of added back) is an imbalance of twice D&A.
- **Interest on the wrong balance, or a circularity that explodes with no toggle.** A model full of #REF! in the last twenty minutes, with no way to break the loop, is the single most common way strong candidates run out the clock.
- **Cash that goes negative with no revolver.** The balance sheet still balances, which is why candidates miss it. A grader reads negative cash as a sign you never looked at your own output.
- **A SUM range that stops one row short.** You insert a line and the total above it doesn't pick it up. This exact error made the news in 2013. In 2010, Carmen Reinhart and Kenneth Rogoff published "Growth in a Time of Debt," which argued that growth drops sharply once government debt passes 90 percent of GDP. In 2013, Thomas Herndon, Michael Ash and Robert Pollin at the University of Massachusetts Amherst got the working spreadsheet and found, among other problems, an averaging formula whose range stopped short and left five countries (Australia, Austria, Belgium, Canada and Denmark) out of the result. With that and the other issues corrected, the average growth figure for high-debt countries moved from slightly negative to about 2.2 percent. Check every SUM range after you insert a row.
- **One year's formula that differs from the rest of its row.** Usually from fixing one cell by hand and forgetting to fill right. Highlight the row and press Ctrl+\ (Excel's row differences shortcut) to find the odd cell.
- **Mixed units or periods.** Revenue in thousands next to debt in millions. A trailing twelve month figure (the last four reported quarters added up) sitting in a fiscal year column.
- **Building the wrong thing.** The prompt asked for five years and you built three, or asked for free cash flow and you never computed it. Section 2's "read it twice, write the outputs" habit exists for this.
- **No saved file.** It happens every cycle.

## 13. What the grader opens first

Here's the first five minutes from the grader's side, because it tells you where to spend your last ten.

They open the file and look for the check row. If it reads zero across, they relax a little. If it doesn't, they look at the pattern the same way section 6 does, and they decide in about a minute whether the error is a missing link (forgivable, especially with a note) or a typed plug (not).

Then they read the cash line and the debt lines across the years. Negative cash, negative debt, or a revolver that grows forever all get noticed here.

Then they press F2 on three or four cells in the cash flow statement and the balance sheet to see whether the links are real. They're checking that net income is a reference to the income statement, that D&A is a reference and not a typed 44, that ending cash is beginning cash plus the net change.

![Close-up of cash flow statement rows in Excel with the formulas that link net income, D&A and ending cash](published/assets/images/three-statement-model-modeling-test/13-formula-closeup.png "What F2 shows the grader: net income is a reference to the income statement, D&A is a reference and not a typed 44, and ending cash is beginning cash plus the net change.")

Then they read the assumptions block and ask whether the story holds: margins that don't move for no reason, capex that matches the growth, a tax rate that looks like the company's.

Last, they change something. Usually revenue growth to zero, or the minimum cash to a higher number, to see whether the model still balances and the revolver responds. **A grader spends the first five minutes trying to break the model, and a model that survives those five minutes has passed, even if the formatting is plain.**

If you have ten minutes left and a choice between a sensitivity table and re-checking the links, re-check the links. The sensitivity table is a bonus. The links are what's being graded.

## 14. Templates worth downloading

My rule for linking a template is that it has to be free, from a source bankers recognize, and built the way this guide teaches. One clears the bar. [Mergers & Inquisitions](https://mergersandinquisitions.com/3-statement-model/) posts the completed Excel file from its 90 minute three statement case study on Otis Worldwide, downloadable from the article with no signup [VERIFY: file still downloadable without signup at publish]. I opened it: one tab, a drivers block at the top, three historical years and five projected, income statement to balance sheet to cash flow statement, interest on the beginning debt balance, a minimum cash assumption, and a balance check row. The structure matches sections 4 through 8 almost line for line, which makes it a good file to reverse-engineer once and then rebuild from a blank sheet without looking.

The other usual sources (Macabacus, Wall Street Prep, Corporate Finance Institute, A Simple Model) all gate their three statement templates behind an email signup or a trial account [VERIFY: whether any of the four has since posted an ungated template], so I'm not linking them here. If you're weighing a paid course for the modeling test, our [review of Wall Street Prep](https://www.wallstreetguide.net/post/is-wall-street-prep-worth-it-4-pros-and-cons-you-need-to-know) covers what it does and doesn't teach.

One more thing about templates. **Download a template to learn the layout, then build from a blank sheet three times before the test, because the test is a blank sheet.** If you'd rather see how the same build shows up on the corporate side, our [FP&A interview questions](https://www.wallstreetguide.net/post/20-fp-a-interview-questions-and-answers) post covers the budgeting version.

## Say this, don't say that

The modeling test usually comes with a conversation, either a walkthrough of your file or a few technical questions in the next round. These are the ones that come up most.

**How do the three statements link?**

Don't say: "Net income flows into cash flow and everything ties to the balance sheet."

Say: "Net income goes to the top of the cash flow statement and into retained earnings. Non-cash items like D&A get added back, and D&A also reduces PP&E. Working capital changes convert balance sheet movements into cash. Capex and debt flow through investing and financing onto PP&E and the debt lines. The net change in cash becomes the balance sheet cash. If all of that is right, the balance sheet balances."

**Your balance sheet is off. What do you check first?**

Don't say: "I'd rebuild the cash flow statement."

Say: "I'd read the pattern. A constant difference is a one-time break, usually a historical input or a first-year link. A growing difference is a recurring item missing or with the wrong sign, and the first year's difference tells me which line. If it's exactly double a line item, I've got the sign wrong on that line."

**Why does interest create a circular reference?**

Don't say: "Because Excel can't handle average balances."

Say: "Interest on the average debt balance depends on ending debt, which includes the revolver. The revolver depends on cash, cash depends on net income, and net income depends on interest. I handle it with a toggle that switches interest to the beginning balance so I can break the loop if the model errors out."

**Why is cash the last thing you calculate?**

Don't say: "Because it's the plug."

Say: "Because cash is the result of everything else. Every operating, investing and financing decision changes cash, so the cash flow statement has to be complete before I know the ending balance. Projecting cash directly would mean guessing the answer instead of deriving it."

**Capex goes up by $100 this year. Walk me through it.**

Don't say: "Cash goes down 100 and that's it."

Say: "This year, nothing on the income statement. Investing cash flow is down 100, so ending cash is down 100, and PP&E is up 100. Assets are unchanged in total, so the balance sheet balances. Starting next year, depreciation on the new asset lowers EBIT, which lowers net income and retained earnings, gets added back on the cash flow statement, and reduces PP&E."

## Build it from a blank sheet three times

Everything above fits in about 100 rows. The reason students fail the modeling test isn't that the three statement model is hard to understand. It's that they understand it from reading and have never built one against a clock, so under time pressure they can't yet build the links they could describe.

Pick a company you like, pull its 10-K, and build the model from a blank sheet this week. Time it. Build it again next week without looking at the first one. The third time through, you'll see the six links before you type them, the check row will read zero on the first try more often than not, and two hours will feel like enough time.
