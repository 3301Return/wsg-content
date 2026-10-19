---
headline: "Financial Modeling Test: What to Expect and How to Practice"
byline: stephen-turban
target_keyword: financial modeling test
secondary_keywords: [modeling test, excel modeling test, private equity modeling test, investment banking modeling test, financial modeling test practice]
format: ultimate-guide
hook_type: real-public-story
word_count_target: ~2000-2500, guideline only, no cap
status: draft-v1
---

# Financial Modeling Test: What to Expect and How to Practice

**Meta description:** WSG founder Stephen Turban breaks down the financial modeling test: who gives it, the five formats, how graders score, a worked two-hour DCF, and how to prep.

Thomas Herndon, a 28-year-old economics PhD student at UMass Amherst, was stuck on a class assignment [VERIFY: semester of the assignment; the critique he co-wrote was published April 15, 2013]. His econometrics professor had asked everyone to replicate a published paper. Herndon picked "Growth in a Time of Debt," the 2010 Reinhart and Rogoff paper claiming economies slow once government debt passes 90 percent of GDP. His numbers wouldn't match. After repeated requests, the authors sent him their Excel file. Inside, an averaging formula stopped short and left five countries out. With that error and two other problems in the data [corrected](https://peri.umass.edu/publication/does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff/), average growth for high-debt countries went from negative 0.1 percent to positive 2.2 percent.

A financial modeling test is that story in miniature. You get a case pack and a clock, you build a spreadsheet, and then someone whose job is to find the bad cell opens your file and starts clicking. I'm Stephen Turban, founder of WallStreetGuide. I went to Harvard and through McKinsey's recruiting before I started WSG, and the modeling test is the round where I watch strong students lose offers they'd already half earned, usually to a flipped sign or a terminal value that never got discounted.

This guide covers who gives modeling tests and when, the five formats, what's in the case pack, how graders actually score, a full two-hour DCF test worked line by line on a fictional industrial company, a minute-by-minute time budget, the mistakes that fail, and a four-week practice plan with the Excel shortcuts that matter.

## What is a financial modeling test?

A financial modeling test is a timed exercise where a firm hands you a prompt and some financial data and asks you to build a working model in Excel: usually an LBO, a DCF, or a three statement model with one of those on top. **A financial modeling test checks three things in order: whether the model works, whether it's right, and whether you built it fast and cleanly enough to be trusted with a live deal model on Monday.** Private equity firms use it as the main technical filter in associate recruiting and, increasingly, in internship recruiting. Banks use it for lateral hires, off-cycle analysts and some Summer Analyst finals. The file you hand in is graded by someone who builds these for a living, and the questions they ask you afterward are part of the test.

## How long is a financial modeling test?

Anywhere from 20 minutes to five days, depending on the format. **The most common financial modeling test runs 60 to 120 minutes and asks for a simple LBO or DCF from a one-page prompt; the two to four hour version adds a three statement build from historicals; the take-home runs one to five days and adds a short memo.** A paper LBO on a whiteboard takes 20 to 30 minutes and uses no Excel at all. The prompt always states the limit, and sizing your build to the clock is the first skill the test measures.

## 1. Who gives financial modeling tests, and when

Start with the firm's reason for running one. An interview can tell a firm whether you understand how a DCF works. It can't tell them whether you can build one without breaking it, at speed, in a file someone else can read. **A modeling test exists because the firm is about to hand a new hire a model that real money depends on, and talking about models doesn't predict whether you can build them.**

So the firms that test hardest are the ones where a junior person's model goes straight into a decision.

**Private equity is where the modeling test is close to universal.** On-cycle associate recruiting (the process that pulls first-year bankers into PE seats that start after their analyst program ends) puts a timed LBO in front of nearly every candidate who reaches a second round, and off-cycle recruiting at middle-market funds does the same with more variety in format. The undergrad PE internship process has been catching up: more of the funds that hire sophomores and juniors directly now add a modeling exercise or a paper LBO to their final rounds, though the format varies fund to fund [VERIFY: which undergrad PE internship programs include a timed modeling exercise in their current cycle; confirm against each fund's posting or recent candidate reports]. If that's your target, our guide to [landing a private equity internship as an undergrad](https://www.wallstreetguide.net/post/the-ultimate-guide-to-landing-a-private-equity-internship-as-an-undergrad) covers the full process, and the [25 private equity interview questions for undergrad candidates](https://www.wallstreetguide.net/post/private-equity-interview-questions-25-for-undergrad-candidates) covers what gets asked around the test.

**Growth equity tests you too, but on a different model.** A growth equity case is more likely to be a revenue or cohort build (a revenue projection that tracks each year's new customers as its own group) with a simple cap table (who owns what share of the company, and at what price) than a full LBO, because the firms buy minority stakes with little or no debt. The time limit is similar (one to three hours) and the grading is heavier on the assumptions than on the debt schedule.

**Banks test selectively, and mostly for hires who start on a live deal.** Elite boutiques and middle-market banks almost always give a modeling test to lateral candidates and off-cycle analysts, because those hires go onto a live deal in week one. For Summer Analyst recruiting it's occasional rather than standard: a few boutiques and middle-market banks run a 60 to 90 minute DCF or three statement exercise at the final round, and bulge brackets mostly don't, relying on the technical questions in the superday instead [VERIFY: which banks currently use a modeling exercise in Summer Analyst finals; treat as a pattern, not a list]. Restructuring groups are the exception on the bank side, and their cases lean toward a capital structure table and a recovery analysis (how much each class of lender gets back if the company is sold or reorganized) rather than a DCF.

**Corporate development and some hedge funds test on their own terms.** Corporate development teams (the in-house M&A groups at large companies) tend to send a take-home: a model plus a few slides on whether to do the deal. Fundamental hedge funds, when they recruit undergrads at all, usually ask for a stock pitch with a model behind it, and a few run a timed three statement build. Most undergrads will see a bank or PE version first.

Here's how common each one is, and where in the process it sits.

| Who tests | How common | Usual format | Where it sits in the process |
|---|---|---|---|
| Private equity, associate recruiting (on-cycle and off-cycle) | Nearly universal | Timed Excel LBO, 60 to 180 minutes; sometimes a take-home case | Second round or final, often the same day as the interviews |
| Private equity, undergrad internships | Increasingly common, varies by fund | Paper LBO, or a short timed LBO | Final round [VERIFY: fund by fund] |
| Growth equity | Common | Revenue or cohort model, cap table, 60 to 180 minutes | Second round or final |
| Elite boutiques and middle-market banks, laterals and off-cycle analysts | Nearly universal | Three statement plus DCF or LBO, 2 to 4 hours | Before or at the final round |
| Elite boutiques and middle-market banks, Summer Analyst recruiting | Occasional | 60 to 90 minute DCF or three statement build | Final round, at a minority of firms [VERIFY: pattern] |
| Bulge bracket banks, Summer Analyst recruiting | Rare | Technical questions instead of a build | Superday |
| Restructuring groups | Common for laterals, occasional for interns | Capital structure and recovery case, sometimes a short model | Final round |
| Corporate development | Common | Take-home model plus slides | After a first-round call |
| Hedge funds (fundamental) | Varies widely | Stock pitch with a model, or a timed three statement build | Second round onward |

## 2. The five financial modeling test formats

Each format tests something different, hands you something different, and wants something different back. Know which one you're walking into before you open Excel. **Every modeling test is one of five formats, and the format tells you what to build, how long you have, and what the grader will open first.**

**The paper LBO.** Twenty to thirty minutes, a whiteboard or a sheet of paper, no Excel. You get five or six round numbers (purchase multiple, EBITDA, leverage, growth, exit multiple, years) and talk your way to a multiple of money and a rough IRR. It tests whether you understand the LBO machine, not whether you can type. Our [walk me through an LBO](https://www.wallstreetguide.net/post/walk-me-through-an-lbo-the-6-step-answer-interviewers-want-to-hear) post covers the arithmetic step by step, so I won't repeat it here.

**The timed Excel LBO.** Sixty to 120 minutes. You get a one-page prompt: purchase price or multiple, a financing structure, a few operating assumptions, an exit year and multiple. You build from a blank sheet: sources and uses, a simple operating model, a debt schedule, returns, and if there's time a sensitivity table. The grader opens the returns first and the debt schedule second. This is the format in most on-cycle PE processes.

**The timed three statement plus DCF or LBO.** Two to four hours. You get a case pack with three years of historicals, sometimes a CIM excerpt, and a prompt asking for projections, an integrated three statement model, and a valuation on top. It tests whether you can go from a filing to a value without a template. The worked example in section 5 is the DCF version of this format.

**The take-home case.** One to five days. You get a CIM or a public company name, a data room or a 10-K, and a prompt like "should we invest at $X a share?" You hand in a model and a five to ten slide memo with a recommendation. The model matters less than the thinking: the grader reads the memo first, flips to the model to check whether the numbers support it, then grills you on both. Smaller funds and off-cycle processes use this most.

**The live build on a shared screen.** Thirty to ninety minutes over a video call, screen shared, an associate watching. Sometimes they talk; sometimes they don't. It tests speed, shortcuts, and whether you can keep building while someone asks you why you used 25 percent for tax. Less common than the other four, more common since 2020, and the one students fear most.

| Format | Time | What you get | What you hand in | What it tests |
|---|---|---|---|---|
| Paper LBO | 20 to 30 minutes | Five or six round inputs, spoken or on a card | A multiple of money and an IRR, out loud, with the steps | Whether you understand the LBO machine |
| Timed Excel LBO | 60 to 120 minutes | A one-page prompt | A working LBO from a blank sheet: sources and uses, operating model, debt schedule, returns | Speed, structure, a debt schedule that works |
| Timed three statement plus DCF or LBO | 2 to 4 hours | A case pack with historicals, an assumptions page, sometimes a template | An integrated model that balances, with a valuation on top | Going from a filing to a value without a template |
| Take-home case | 1 to 5 days | A CIM or 10-K, maybe a data room, a prompt | A model plus a 5 to 10 slide memo and a recommendation | Judgment, assumptions, writing |
| Live build on a shared screen | 30 to 90 minutes | A short prompt, read to you or sent as you start | A model built in front of the grader, explained as you go | Composure, shortcuts, defending assumptions in real time |

![Horizontal range chart of the five modeling test formats by time, from paper LBO to take-home case](published/assets/images/financial-modeling-test-what-to-expect/01-five-formats-by-length.png "Four of the five formats fit inside an afternoon, and the one to plan your prep around is the two to four hour three statement build with a valuation on top.")

**The format you're least likely to get is the one you've practiced most, so practice the one the firm actually gives.** Ask whoever scheduled the round. HR will usually tell you the length and whether it's Excel or paper, and that one answer shapes your whole prep.

## 3. What's in the case pack, and where each input lives

A case pack has four or five pieces. Knowing what each is for saves you the ten minutes most candidates lose reading everything twice.

**The prompt** is one page. It says what to build, how long you have, the valuation date, what to hand in, and the outputs the grader wants (an implied share price, an IRR, a balance check). Read it twice and write every requested output on paper before you type anything. **The most common way to fail a modeling test is to build something the prompt didn't ask for and run out of time on what it did.**

**The historical financials** are two or three years of income statement, balance sheet and cash flow statement, usually simplified to the lines the model needs. In a private company case they come as a table in the pack. In a public company case you get the 10-K and the lines are yours to find.

**The assumptions page** gives you the numbers the firm doesn't want you to guess: tax rate, risk-free rate, equity risk premium, exit multiple or terminal growth, debt terms, share count. If the pack gives an assumption, use it. If it doesn't, make one, write it in blue, and label it.

**The CIM excerpt**, when there is one, is a few pages of the confidential information memorandum (the sales document a bank writes about a company that's for sale). It tells you what the segments are, what drives them, and what management thinks growth looks like. Pull the segment names and the management growth story from it; treat the management projections as the Bull case, not the Base.

**The blank template**, when there is one, has the layout and formatting locked and the formulas missing. It's a gift: the structure decision is made for you. It's also a trap, because a locked template usually has rows you don't need and the grader can tell at a glance which ones you left empty.

For a public company test, you only need about fifteen lines from the 10-K, and knowing where they sit saves half an hour.

| What you need | Where it lives in the 10-K | What you pull |
|---|---|---|
| Revenue, cost of sales, SG&A, operating income, interest, pretax income, taxes, net income | Item 8, consolidated statements of operations | Three years, as reported, in the filing's units |
| Segment revenue and segment operating profit | Item 7 (Management's Discussion and Analysis, the MD&A) and the segment note in Item 8 | Revenue by segment for the build; management's commentary on what moved |
| D&A, capex, stock-based compensation | Item 8, consolidated statement of cash flows | D&A from operating activities, capex from investing activities |
| Receivables, inventory, payables, accrued liabilities, deferred revenue | Item 8, consolidated balance sheet | Year-end balances for the working capital days |
| Net PP&E | Balance sheet, and the PP&E note | Ending balance to start the roll-forward |
| Debt tranches, rates, maturities | The debt note in Item 8 | Principal and rate per tranche for the cost of debt |
| Cash and equivalents | Balance sheet | For net debt |
| Noncontrolling interest, preferred stock | Balance sheet and equity note | For the enterprise value to equity value bridge |
| Basic and diluted share count | The cover page (shares outstanding at the latest date) and the EPS note | Diluted count for the implied share price; options and RSUs if you're asked for a treasury stock method |
| Effective tax rate | The income tax note | The rate to put on EBIT |
| Operating leases | The lease note | Usually left alone in a two-hour test; the prompt will say |

**Everything on the right of that table is a blue hardcode on your Inputs tab, and everything else in the model is a formula that traces back to one of those cells.**

## 4. How graders grade a financial modeling test

Firms don't publish rubrics, and I've never been a grader. What follows is the pattern from the debriefs students bring me every cycle: what students who passed were asked about, what students who failed were told, and what the associates and VPs I've talked to say they open first. **A grader spends the first five minutes trying to break your model, and the order they try things in is the order you should build in.**

**First, does it work.** They open the file and go straight to the output the prompt asked for. In a DCF test that's the implied share price and the enterprise value bridge. In an LBO test it's the returns and the sources and uses table (where the deal's money comes from and where it goes: do sources equal uses, does the debt pay down, does cash ever go negative). In a three statement test it's the balance check row. If the output is a number and not an error, and the check reads zero, they keep going. If the check is off and there's a typed number making it balance, most graders stop caring about the rest.

**Second, is it right.** Now they click. The working capital line: is an increase in receivables a use of cash (negative) and an increase in payables a source (positive)? Taxes: on EBIT, not on pretax income, because an unlevered cash flow has to be before interest. Terminal value: discounted from the end of the last projected year, not left in future dollars. The share count: diluted, not basic. Net debt: debt minus cash, not plus. The discount factor: the exponent matches the convention you said you used. **Six cells decide most modeling tests: the working capital sign, the tax line, the terminal value discount, the share count, net debt and the discount exponent.**

**Third, speed and scope.** Did you finish what was asked, and did you spend the time on the right things? A model with the DCF done and a plain sensitivity grid beats a model with a beautiful segment schedule and no terminal value. A grader can see from your sheet where your two hours went.

**Fourth, is it clean.** Blue hardcodes, black formulas, green links to other sheets. One formula per row, filled across. No typed numbers inside formulas (=C12*1.04 is a hardcode hiding in a formula; =C12*(1+C5) with C5 holding 4 percent in blue is the right form). Units stated once at the top of each block. Labels a stranger could read. No hidden rows. In September 2008, a first-year associate at Cleary Gottlieb converted a Lehman Brothers contract spreadsheet of nearly 1,000 rows to a PDF for a court filing around 11:30 at night, and the conversion un-hid rows that were supposed to stay hidden; 179 contracts that Barclays had not agreed to buy ended up in the purchase agreement, and the bank had to [ask the court](https://www.abajournal.com/news/article/excel_error_by_a_cleary_gottlieb_associate_alters_lehman_asset_deal1) to take them back out. Graders know that story. Hidden rows read as something to be suspicious of, not as tidiness.

**Fifth, the debrief.** Can you defend every assumption in two sentences? Why 9.5x? Why 60 days of receivables? What would change your number the most? The debrief is where a correct model with lazy assumptions loses to a slightly rougher model whose builder clearly understood the company. Section 10 covers the questions and the answers.

| Rubric part | What the grader checks | What fails it | Rough weight |
|---|---|---|---|
| 1. Does it work | The requested output exists; the balance check or sources and uses ties; no errors | #REF!, a typed plug, cash going negative with no note | Pass or fail gate |
| 2. Is it right | Working capital sign, tax on EBIT, terminal value discounted, diluted shares, net debt, discount exponents | Any one of those wrong by itself can fail the test | About 40 percent |
| 3. Speed and scope | The prompt's outputs are all there; time went to the DCF, not to decoration | A finished schedule nobody asked for and an unfinished valuation | About 20 percent |
| 4. Cleanliness | Color code, one formula per row, no hardcodes in formulas, units labeled, no hidden rows | Mixed colors, typed numbers inside formulas, unlabeled blocks | About 15 percent |
| 5. The debrief | Two-sentence defense of each assumption; knows what moves the answer | "That's what the template had"; can't name the biggest driver | About 25 percent |

The weights are my read from student debriefs, not a published scale, and they move by firm [VERIFY: founder read; no firm publishes a rubric]. **The grading order never changes: works, then right, then fast, then clean, then defended.**

## 5. A full worked example: a two-hour DCF financial modeling test

Here's the whole thing on a company I made up for this article: Torvik Flow Systems, a mid-cap industrial that makes pumps, valves and controls, and sells aftermarket parts and service for both. Three segments, one tax rate, two debt tranches, a current share price of $38.00 and 60.0 million diluted shares. Fiscal year ends December 31. Every number below came out of a script I ran before pasting the tables in, so the tables tie, and the model carries full precision underneath; if you re-add a displayed column by hand you'll sometimes land 0.1 off, which is rounding, not an error. Figures are in $ millions except per-share data.

The prompt, as a test would give it: "Using the attached historicals and assumptions, build a five-year DCF for Torvik Flow Systems as of December 31, 2025. Include a scenario switch, a working capital schedule driven by days, a PP&E roll-forward, a WACC built from the peer set provided, a terminal value by exit multiple with a perpetuity growth cross-check, an implied share price, and a sensitivity table of share price to WACC and exit multiple. You have two hours."

If the conceptual DCF is new to you, read our [walk me through a DCF](https://www.wallstreetguide.net/post/walk-me-through-a-dcf-the-7-step-answer-that-works) post first; this section assumes you know the shape and shows you the build.

The layout, before any numbers: a Cover tab with the scenario switch cell, an Inputs tab (historicals, segment build, assumptions block), a Schedules tab (working capital and PP&E), a Cost of debt tab, a Beta tab, a WACC tab, a DCF tab and a Sensitivity tab. Column A is a narrow margin, labels sit in column B, years run across from column C, and each block carries its own year header so it reads on its own. Blue for hardcodes, black for formulas, green for links to other tabs. In a two-hour test you can collapse all of that onto one sheet with the same blocks in the same order; the tabs are what the take-home version grows into.

### Step 1. Input the historicals and compute the ratios

Type the three years of income statement in blue, costs as negatives so every subtotal is a SUM. Then compute the ratios under them in black: growth, margins, the effective tax rate. The ratios are what you'll project, so they go here, not on a separate page.

| $ millions | 2023A | 2024A | 2025A |
|---|---|---|---|
| Revenue | 1,210.0 | 1,276.0 | 1,350.0 |
| Cost of sales | (810.0) | (845.0) | (884.0) |
| Gross profit | 400.0 | 431.0 | 466.0 |
| SG&A | (250.0) | (260.0) | (270.0) |
| EBIT | 150.0 | 171.0 | 196.0 |
| Interest expense | (24.0) | (24.0) | (24.0) |
| Pretax income | 126.0 | 147.0 | 172.0 |
| Taxes | (31.5) | (36.8) | (43.0) |
| Net income | 94.5 | 110.3 | 129.0 |
| Diluted shares (millions) | 60.0 | 60.0 | 60.0 |
| Diluted EPS ($) | $1.58 | $1.84 | $2.15 |
| Revenue growth |  | 5.5% | 5.8% |
| Gross margin | 33.1% | 33.8% | 34.5% |
| SG&A as a percent of revenue | 20.7% | 20.4% | 20.0% |
| EBIT margin | 12.4% | 13.4% | 14.5% |
| Effective tax rate | 25.0% | 25.0% | 25.0% |
| D&A (from the cash flow statement) | 40.0 | 42.0 | 44.0 |
| EBITDA | 190.0 | 213.0 | 240.0 |
| EBITDA margin | 15.7% | 16.7% | 17.8% |
| Capex (from the cash flow statement) | 48.0 | 50.0 | 54.0 |

![Excel Inputs tab with Torvik's 2023 to 2025 income statement, margins, tax rate, D&A, EBITDA and capex](published/assets/images/financial-modeling-test-what-to-expect/02-historicals-and-ratios.png "Only the blue cells are typed. Every subtotal is a SUM and every ratio underneath is a formula, which is what lets you project the ratios instead of the dollars.")

In words: gross profit is revenue plus cost of sales (cost of sales is negative, so the SUM works). EBIT is gross profit plus SG&A. Pretax income is EBIT plus interest. Taxes are pretax income times the 25 percent rate, shown negative. EBITDA is EBIT plus D&A, and D&A comes from the cash flow statement, not the income statement, because the income statement buries it inside cost of sales and SG&A. Revenue growth is this year divided by last year minus one. Every margin is the line divided by revenue.

Two things a grader notices here. Margins are expanding (gross margin from 33.1 to 34.5 percent, EBIT margin from 12.4 to 14.5 percent) and the mix is shifting toward aftermarket, the fastest-growing segment and, in most industrial businesses, the one that earns the most per dollar of sales. Your projections should continue that story or say why they don't.

### Step 2. Build revenue by segment

Torvik reports three segments, so revenue gets built bottom-up: each segment's revenue, its growth rate, and its share of the total.

| $ millions | 2023A | 2024A | 2025A |
|---|---|---|---|
| Pumps | 530.0 | 548.0 | 570.0 |
| Valves and Controls | 385.0 | 406.0 | 430.0 |
| Aftermarket Parts and Service | 295.0 | 322.0 | 350.0 |
| Total revenue | 1,210.0 | 1,276.0 | 1,350.0 |
| Pumps growth |  | 3.4% | 4.0% |
| Valves and Controls growth |  | 5.5% | 5.9% |
| Aftermarket Parts and Service growth |  | 9.2% | 8.7% |
| Pumps mix | 43.8% | 42.9% | 42.2% |
| Valves and Controls mix | 31.8% | 31.8% | 31.9% |
| Aftermarket Parts and Service mix | 24.4% | 25.2% | 25.9% |

![Excel segment build with revenue, growth and mix for pumps, valves and controls, and aftermarket](published/assets/images/financial-modeling-test-what-to-expect/03-segment-build.png "The check row under total revenue reads 0.0 in every year, and the growth rows show the story: aftermarket grows about 9 percent while pumps grow about 4.")

Total revenue here is a SUM of the three segments, and that SUM has to equal the revenue line in Step 1. Put a check cell next to it (segment total minus reported revenue, which should read 0.0). Mix is each segment divided by the total. **The segment build is where the grader learns whether you read the pack: aftermarket growing at 9 percent while pumps grow at 4 is the whole investment story, and your assumptions have to show you saw it.**

### Step 3. Write the assumptions block with the Bear, Base and Bull rows

This is the block the scenario switch reads. For every driver that changes with the scenario, you write three rows across the five projected years, one per case, and a fourth "live" row that picks one of the three using the switch cell on the Cover tab. In Excel that's a CHOOSE or an INDEX: if the switch cell holds 1, 2 or 3, the live row returns the Bear, Base or Bull row. Every projection formula points at the live row, never at a case row directly, so flipping one cell flips the whole model.

![Close-up of the scenario switch cell on the Cover tab and the pumps growth row that reads it](published/assets/images/financial-modeling-test-what-to-expect/04-scenario-switch.png "One cell on the Cover tab holds a 2 for Base. The live pumps row runs a CHOOSE on that cell, so it shows the Base numbers, and every projection points at the live row.")

| Driver | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| Pumps growth, Bear | 1.0% | 0.0% | 1.0% | 2.0% | 2.0% |
| Pumps growth, Base | 4.0% | 4.0% | 3.5% | 3.5% | 3.0% |
| Pumps growth, Bull | 6.0% | 6.0% | 5.0% | 5.0% | 4.0% |
| Valves and Controls growth, Bear | 2.0% | 1.0% | 2.0% | 3.0% | 3.0% |
| Valves and Controls growth, Base | 6.0% | 5.5% | 5.0% | 4.5% | 4.0% |
| Valves and Controls growth, Bull | 8.0% | 8.0% | 7.0% | 6.0% | 5.0% |
| Aftermarket Parts and Service growth, Bear | 5.0% | 4.0% | 4.0% | 4.0% | 4.0% |
| Aftermarket Parts and Service growth, Base | 8.0% | 7.5% | 7.0% | 6.0% | 5.0% |
| Aftermarket Parts and Service growth, Bull | 10.0% | 10.0% | 9.0% | 8.0% | 7.0% |
| Gross margin, Bear | 34.0% | 34.0% | 34.0% | 34.0% | 34.0% |
| Gross margin, Base | 34.8% | 35.0% | 35.2% | 35.4% | 35.5% |
| Gross margin, Bull | 35.0% | 35.5% | 36.0% | 36.5% | 36.5% |
| SG&A as a percent of revenue, Bear | 20.5% | 20.5% | 20.5% | 20.5% | 20.5% |
| SG&A as a percent of revenue, Base | 20.0% | 19.9% | 19.8% | 19.8% | 19.8% |
| SG&A as a percent of revenue, Bull | 19.5% | 19.4% | 19.3% | 19.2% | 19.2% |
| D&A as a percent of revenue (all cases) | 3.3% | 3.3% | 3.3% | 3.3% | 3.3% |
| Capex as a percent of revenue (all cases) | 4.0% | 4.0% | 4.0% | 4.0% | 4.0% |
| Receivable days, DSO (all cases) | 60 | 60 | 60 | 60 | 60 |
| Inventory days, DIO (all cases) | 90 | 90 | 90 | 90 | 90 |
| Payable days, DPO (all cases) | 45 | 45 | 45 | 45 | 45 |
| Accrued liabilities as a percent of revenue | 4.0% | 4.0% | 4.0% | 4.0% | 4.0% |
| Deferred revenue as a percent of revenue | 2.0% | 2.0% | 2.0% | 2.0% | 2.0% |
| Tax rate on EBIT (all cases) | 25.0% | 25.0% | 25.0% | 25.0% | 25.0% |

![Excel assumptions block with Bear, Base and Bull rows and a shaded live row for each driver](published/assets/images/financial-modeling-test-what-to-expect/05-assumptions-block.png "Three typed rows per driver and a fourth shaded row that picks one. The fixed drivers at the bottom, days, D&A, capex and tax, don't change with the scenario.")

The Base case continues the historical pattern and fades it: pumps slow from 4 percent to 3, aftermarket from 8 to 5, gross margin climbs a point over five years, SG&A leaks down 20 basis points as revenue grows faster than overhead. The Bear case is a flat industrial cycle: pumps go nowhere for two years, margins stop expanding, SG&A doesn't scale. The Bull case is management's deck: faster everything and two points of gross margin. The drivers below the margin rows don't change with the scenario, because in a two-hour test the pack gives them and nobody expects you to flex payable days.

Every one of these is a blue cell. The days assumptions come straight from the 2025A balances in Step 5 (60.0, 90.0 and 45.0 days, rounded), the D&A and capex percentages from 2025A (44 over 1,350 is 3.3 percent; 54 over 1,350 is 4.0 percent), and the tax rate from the historical effective rate.

### Step 4. Project the operating build

Now the projections are formulas only. Each segment's revenue is last year times one plus its live growth rate. Total revenue is the SUM. Cost of sales is revenue times one minus the live gross margin, shown negative. SG&A is revenue times the live SG&A percentage, negative. EBIT is the SUM. D&A is revenue times 3.3 percent; EBITDA is EBIT plus D&A; capex is revenue times 4.0 percent.

| $ millions | 2023A | 2024A | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|---|---|
| Pumps | 530.0 | 548.0 | 570.0 | 592.8 | 616.5 | 638.1 | 660.4 | 680.2 |
| Valves and Controls | 385.0 | 406.0 | 430.0 | 455.8 | 480.9 | 504.9 | 527.6 | 548.7 |
| Aftermarket Parts and Service | 295.0 | 322.0 | 350.0 | 378.0 | 406.4 | 434.8 | 460.9 | 483.9 |
| Total revenue | 1,210.0 | 1,276.0 | 1,350.0 | 1,426.6 | 1,503.7 | 1,577.8 | 1,648.9 | 1,712.9 |
| Revenue growth |  | 5.5% | 5.8% | 5.7% | 5.4% | 4.9% | 4.5% | 3.9% |
| Cost of sales | (810.0) | (845.0) | (884.0) | (930.1) | (977.4) | (1,022.4) | (1,065.2) | (1,104.8) |
| Gross profit | 400.0 | 431.0 | 466.0 | 496.5 | 526.3 | 555.4 | 583.7 | 608.1 |
| Gross margin | 33.1% | 33.8% | 34.5% | 34.8% | 35.0% | 35.2% | 35.4% | 35.5% |
| SG&A | (250.0) | (260.0) | (270.0) | (285.3) | (299.2) | (312.4) | (326.5) | (339.2) |
| EBIT | 150.0 | 171.0 | 196.0 | 211.1 | 227.1 | 243.0 | 257.2 | 268.9 |
| EBIT margin | 12.4% | 13.4% | 14.5% | 14.8% | 15.1% | 15.4% | 15.6% | 15.7% |
| D&A | 40.0 | 42.0 | 44.0 | 47.1 | 49.6 | 52.1 | 54.4 | 56.5 |
| EBITDA | 190.0 | 213.0 | 240.0 | 258.2 | 276.7 | 295.0 | 311.6 | 325.5 |
| EBITDA margin | 15.7% | 16.7% | 17.8% | 18.1% | 18.4% | 18.7% | 18.9% | 19.0% |
| Capex | 48.0 | 50.0 | 54.0 | 57.1 | 60.1 | 63.1 | 66.0 | 68.5 |

![Excel operating build for 2023 to 2030 from segment revenue down to EBITDA and capex](published/assets/images/financial-modeling-test-what-to-expect/06-operating-build.png "Historical columns are green links back to the Inputs tab and projected columns are black formulas. Revenue growth fades from 5.7 to 3.9 percent while EBITDA margin climbs to 19.0.")

Check it against the story before you move on. Revenue growth fades from 5.7 percent to 3.9 as the segments slow. EBIT margin goes from 14.5 to 15.7 percent, a point of expansion over five years, which is what a point of gross margin and a little SG&A leverage should produce. Capex runs above D&A every year (57.1 against 47.1 in 2026E), so net PP&E grows, which fits a company growing at 4 to 6 percent. If any of those three sentences had come out wrong, the assumptions block is where I'd look first, not the formulas.

### Step 5. Working capital by days

Working capital is the cash the business has tied up in running itself: money customers owe it (receivables), stock on the shelf (inventory), minus money it owes suppliers (payables) and other short-term obligations it hasn't paid yet (accrued liabilities) or cash it collected before doing the work (deferred revenue). The DCF needs the change in that number each year, because when working capital grows, cash that the income statement counted as profit is still sitting in receivables and inventory, and hasn't actually arrived.

Days are how you project it. Receivable days (DSO) is receivables divided by revenue times 365: how many days of sales are sitting unpaid. Inventory days (DIO) is inventory divided by cost of sales times 365. Payable days (DPO) is payables divided by cost of sales times 365. You compute the historical days, pick a projected number (usually the latest year, rounded), and reverse the formula: projected receivables equal projected revenue times DSO divided by 365.

| $ millions | 2022A | 2023A | 2024A | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|---|---|---|
| Accounts receivable | 190.0 | 199.0 | 210.0 | 222.0 | 234.5 | 247.2 | 259.4 | 271.1 | 281.6 |
| Inventory | 195.0 | 200.0 | 208.0 | 218.0 | 229.4 | 241.0 | 252.1 | 262.7 | 272.4 |
| Accounts payable | 97.0 | 100.0 | 104.0 | 109.0 | 114.7 | 120.5 | 126.1 | 131.3 | 136.2 |
| Accrued liabilities | 46.0 | 48.0 | 51.0 | 54.0 | 57.1 | 60.1 | 63.1 | 66.0 | 68.5 |
| Deferred revenue | 23.0 | 24.0 | 26.0 | 27.0 | 28.5 | 30.1 | 31.6 | 33.0 | 34.3 |
| Net working capital | 219.0 | 227.0 | 237.0 | 250.0 | 263.6 | 277.5 | 290.7 | 303.4 | 315.0 |
| (Increase) / decrease in NWC |  | (8.0) | (10.0) | (13.0) | (13.6) | (13.9) | (13.3) | (12.7) | (11.6) |
| DSO (days) |  | 60.0 | 60.1 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 | 60.0 |
| DIO (days) |  | 90.1 | 89.8 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 |
| DPO (days) |  | 45.1 | 44.9 | 45.0 | 45.0 | 45.0 | 45.0 | 45.0 | 45.0 |
| NWC as a percent of revenue |  | 18.8% | 18.6% | 18.5% | 18.5% | 18.5% | 18.4% | 18.4% | 18.4% |

![Excel working capital schedule with receivables, inventory, payables, net working capital and days from 2022 to 2030](published/assets/images/financial-modeling-test-what-to-expect/07-working-capital.png "The bold (increase) / decrease row is the one that feeds free cash flow, and it's negative every year because a growing balance ties up cash.")

Net working capital is receivables plus inventory minus payables minus accrued liabilities minus deferred revenue. The (increase) / decrease line is last year's NWC minus this year's, so a growing balance shows as a negative number, which is the use of cash that goes into free cash flow. In 2026E, NWC grows from 250.0 to 263.6, so 13.6 of cash goes out. The 2022A column is there only so the 2023A change can be computed; a test pack will give you that opening balance or tell you to start the change in the second historical year.

**Working capital in a DCF is a sign test disguised as a schedule: a growing balance is a cash outflow, and a candidate who adds it instead of subtracting it has just made the company worth more for tying up cash.** Section 8 shows what that mistake does to the share price.

### Step 6. The PP&E roll-forward

Net PP&E (the plant and equipment on the balance sheet, net of the depreciation already charged) rolls forward with one formula: beginning balance, plus capex, minus depreciation and amortization, equals ending balance. The ending balance of one year is the beginning balance of the next.

| $ millions | 2023A | 2024A | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|---|---|
| Beginning net PP&E | 384.0 | 392.0 | 400.0 | 410.0 | 420.0 | 430.5 | 441.6 | 453.1 |
| Plus: capex | 48.0 | 50.0 | 54.0 | 57.1 | 60.1 | 63.1 | 66.0 | 68.5 |
| Less: depreciation and amortization | (40.0) | (42.0) | (44.0) | (47.1) | (49.6) | (52.1) | (54.4) | (56.5) |
| Ending net PP&E | 392.0 | 400.0 | 410.0 | 420.0 | 430.5 | 441.6 | 453.1 | 465.1 |
| Capex as a percent of revenue | 4.0% | 3.9% | 4.0% | 4.0% | 4.0% | 4.0% | 4.0% | 4.0% |
| D&A as a percent of revenue | 3.3% | 3.3% | 3.3% | 3.3% | 3.3% | 3.3% | 3.3% | 3.3% |

![Excel PP&E roll-forward: beginning balance plus capex less depreciation equals ending balance, 2023 to 2030](published/assets/images/financial-modeling-test-what-to-expect/08-ppe-roll-forward.png "Four rows and one formula: 384.0 plus 48.0 minus 40.0 lands on 392.0 in 2023, and each ending balance becomes the next year's beginning.")

In a DCF the roll-forward isn't strictly needed to get to a share price, since capex and D&A are already in the cash flow. Build it anyway. It takes four rows, it proves to the grader that the historical capex and D&A tie to the balance sheet (384.0 plus 48.0 minus 40.0 is 392.0, which matches the 2023A filing), and it's where you'd see a projection error like D&A outrunning capex until PP&E goes negative. Some packs give D&A as a percent of beginning PP&E or of capex instead of revenue; either way the roll works the same.

### Step 7. Cost of debt

Torvik has two tranches of debt. Each has a principal and a rate; the pre-tax cost of debt is the weighted average, with weights by principal. The after-tax cost is the pre-tax cost times one minus the tax rate, because interest is deductible and the government pays a quarter of it.

| Tranche | Principal | Weight | Rate |
|---|---|---|---|
| Term loan B | 250.0 | 62.5% | 5.75% |
| Senior notes | 150.0 | 37.5% | 6.50% |
| Total debt and weighted pre-tax cost | 400.0 | 100.0% | 6.03% |
| After-tax cost of debt at a 25% tax rate |  |  | 4.52% |

![Excel cost of debt tab with two tranches, weights by principal, 6.03 percent pre-tax and 4.52 percent after tax](published/assets/images/financial-modeling-test-what-to-expect/09-cost-of-debt.png "Weight each tranche by principal, add up principal times rate, divide by total debt: 6.03 percent before tax and 4.52 after.")

The arithmetic: 250.0 times 5.75 percent is 14.4; 150.0 times 6.50 percent is 9.8; the sum, 24.1, divided by 400.0 is 6.03 percent. (In the historicals, interest expense was 24.0 a year, which matches within rounding: a quick tie the grader may check.) Times 0.75 gives 4.52 percent. In a real test, the tranches and rates come from the debt note in the 10-K; if the company's bonds trade, the yield to maturity on them is a better cost of debt than the coupon, and the pack will say if it wants that.

### Step 8. Beta, unlevered from the peers and relevered for Torvik

Beta measures how much a stock moves with the market. A beta of 1.1 means the stock tends to move 1.1 percent for every 1 percent the market moves. The problem is that a company's own beta is noisy, and it reflects that company's debt load, which isn't the business risk you want. So you take a set of peers, strip the debt effect out of each one's beta (unlever it), take the median, and put Torvik's own debt back in (relever it).

Unlevered beta equals levered beta divided by one plus (one minus the tax rate) times debt over equity. Relevered beta equals the median unlevered beta times one plus (one minus the tax rate) times Torvik's debt over equity. The peers here are fictional, labeled by what they'd be; in a real pack you'd get five to eight named companies with their betas, debt and market caps.

| Company | Levered beta | Debt | Equity value | D / E | Tax rate | Unlevered beta |
|---|---|---|---|---|---|---|
| Peer A (large-cap pumps) | 1.20 | 600.0 | 3,000.0 | 0.20 | 25% | 1.043 |
| Peer B (valves) | 1.05 | 300.0 | 2,500.0 | 0.12 | 25% | 0.963 |
| Peer C (industrial controls) | 1.35 | 1,200.0 | 4,000.0 | 0.30 | 25% | 1.102 |
| Peer D (flow equipment, small cap) | 0.95 | 200.0 | 1,800.0 | 0.11 | 25% | 0.877 |
| Peer E (fluid handling) | 1.15 | 900.0 | 3,600.0 | 0.25 | 25% | 0.968 |
| Median unlevered beta |  |  |  |  |  | 0.968 |
| Mean unlevered beta (for reference) |  |  |  |  |  | 0.991 |
| Torvik debt to equity (400.0 / market cap) |  | 400.0 | 2,280.0 | 0.175 | 25% |  |
| Torvik relevered beta |  |  |  |  |  | 1.096 |

![Excel beta tab with five peer betas unlevered, the 0.968 median and Torvik relevered at 1.096](published/assets/images/financial-modeling-test-what-to-expect/10-beta.png "Unlever each peer, take the median of the five, then put Torvik's own 0.175 debt to equity back in to get a 1.096 beta.")

Walk one row. Peer A: debt over equity is 600 over 3,000, which is 0.20. One minus the tax rate is 0.75. 0.75 times 0.20 is 0.15. One plus 0.15 is 1.15. 1.20 divided by 1.15 is 1.043. Do that for all five, sort them, and the middle one (0.968) is the median. Use the median, not the mean, because one odd peer (a company whose stock had a wild year and carries a 1.35 beta because of it) shouldn't drag the answer.

Then Torvik's own debt to equity: 400.0 of debt over a market cap of 2,280.0 (the $38.00 share price times 60.0 million diluted shares) is 0.175. 0.75 times 0.175 is 0.132. One plus that is 1.132. 0.968 times 1.132 is 1.096. That's the beta that goes into the cost of equity.

### Step 9. WACC

The weighted average cost of capital is the blended return the company's investors require, which is the rate you discount unlevered cash flows at. Cost of equity comes from the capital asset pricing model: the risk-free rate plus beta times the equity risk premium (the extra return stocks earn over government bonds). The pack gives a 4.50 percent risk-free rate and a 5.00 percent equity risk premium. In a real test with no pack number, the risk-free rate is the 10-year Treasury yield on the valuation date from the [Treasury's daily yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026) (5.28 percent on October 2, 2026 [VERIFY: current 10-year yield at publish]), and the equity risk premium is whatever the firm uses; Aswath Damodaran's [published estimate](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) for the US was 4.46 percent in his January 2026 update [VERIFY: Damodaran's latest US ERP], and banks' internal numbers tend to sit between 5 and 6 percent. When the pack gives a number, use the pack's number even if today's yield is different; the grader wants to see that you read the pack.

| Line | Value |
|---|---|
| Risk-free rate (from the pack) | 4.50% |
| Equity risk premium (from the pack) | 5.00% |
| Relevered beta | 1.096 |
| Cost of equity = risk-free + beta times ERP | 9.98% |
| Pre-tax cost of debt | 6.03% |
| After-tax cost of debt | 4.52% |
| Share price on the valuation date ($) | $38.00 |
| Diluted shares (millions) | 60.0 |
| Equity value (market cap) | 2,280.0 |
| Total debt | 400.0 |
| Equity weight | 85.1% |
| Debt weight | 14.9% |
| WACC | 9.16% |

![Excel WACC tab building a 9.98 percent cost of equity and a 9.16 percent WACC](published/assets/images/financial-modeling-test-what-to-expect/11-wacc.png "Five inputs and one weighted average. The green cells are links to the Beta, Cost of debt and Cover tabs, so each one traces back to where it came from.")

Cost of equity: 4.50 plus 1.096 times 5.00 is 9.98 percent. Weights use market values: equity is 2,280.0 out of 2,680.0 total capital, so 85.1 percent; debt is the other 14.9 percent. WACC is 0.851 times 9.98 plus 0.149 times 4.52, which is 8.49 plus 0.67, or 9.16 percent. **WACC is five inputs and one weighted average, and the grader cares less about the 9.16 than about whether you can say where each of the five came from.**

### Step 10. Unlevered free cash flow and present value

Unlevered free cash flow is the cash the business generates before anyone gets paid for financing it: EBIT, minus the tax the company would pay on EBIT if it had no debt, plus D&A (a non-cash charge that reduced EBIT but didn't cost cash), minus capex (cash spent that EBIT didn't count), minus the increase in working capital (cash tied up that EBIT counted as profit). NOPAT, net operating profit after tax, is EBIT times one minus the tax rate.

Then discount. The valuation date is December 31, 2025, the last fiscal year end, so each projected year ends a whole number of years out: the year fraction is 1.00 for every year. With end-of-year discounting you'd divide 2026E's cash flow by one plus WACC to the power of 1, 2027E's by the power of 2, and so on. The mid-year convention says that's too harsh: a year's cash arrives across the year, not on December 31, so treat it as arriving at the midpoint and use exponents of 0.5, 1.5, 2.5, 3.5 and 4.5. I use mid-year for an industrial like Torvik, whose sales come in evenly. For a retailer that sells half its year in December, end-of-year is closer to the truth.

If the valuation date had been, say, March 31, 2026, the year fraction for 2026E would be 0.75 (nine months of the year left), you'd count only 75 percent of 2026E's cash flow, and the mid-year exponent for that stub would be half of 0.75, or 0.375, with the later years at 0.75 plus 0.5, 0.75 plus 1.5, and so on. Most two-hour packs set the valuation date at a fiscal year end so you don't have to.

| $ millions | 2023A | 2024A | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|---|---|
| EBIT | 150.0 | 171.0 | 196.0 | 211.1 | 227.1 | 243.0 | 257.2 | 268.9 |
| Less: taxes on EBIT at 25% | (37.5) | (42.8) | (49.0) | (52.8) | (56.8) | (60.7) | (64.3) | (67.2) |
| NOPAT | 112.5 | 128.3 | 147.0 | 158.4 | 170.3 | 182.2 | 192.9 | 201.7 |
| Plus: D&A | 40.0 | 42.0 | 44.0 | 47.1 | 49.6 | 52.1 | 54.4 | 56.5 |
| Less: capex | (48.0) | (50.0) | (54.0) | (57.1) | (60.1) | (63.1) | (66.0) | (68.5) |
| Less: increase in NWC | (8.0) | (10.0) | (13.0) | (13.6) | (13.9) | (13.3) | (12.7) | (11.6) |
| Unlevered free cash flow | 96.5 | 110.3 | 124.0 | 134.8 | 145.9 | 157.9 | 168.7 | 178.1 |
| Year fraction from the valuation date |  |  |  | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Discount period (mid-year) |  |  |  | 0.50 | 1.50 | 2.50 | 3.50 | 4.50 |
| Discount factor at 9.16% WACC |  |  |  | 0.9571 | 0.8767 | 0.8031 | 0.7357 | 0.6739 |
| Present value of UFCF |  |  |  | 129.0 | 127.9 | 126.8 | 124.1 | 120.1 |

![Excel block from EBIT to unlevered free cash flow, mid-year discount periods, discount factors and present values](published/assets/images/financial-modeling-test-what-to-expect/12-ufcf-and-present-value.png "Tax is on EBIT, the working capital line comes in negative from the Schedules tab, and the mid-year periods run 0.50 to 4.50, so the five present values sum to 627.9.")

Walk 2026E. EBIT is 211.1. Tax at 25 percent is 52.8, leaving NOPAT of 158.4. Add back D&A of 47.1, subtract capex of 57.1, subtract the 13.6 increase in working capital: 134.8 of unlevered free cash flow. The discount factor is one divided by 1.0916 to the power of 0.5, which is 0.9571. 134.8 times 0.9571 is 129.0. Do the same for each year and the five present values sum to 627.9.

![Close-up of the 2026 unlevered free cash flow column in Excel with each row's formula written beside it](published/assets/images/financial-modeling-test-what-to-expect/13-formula-closeup.png "What F2 would show in the 2026E column: tax is minus EBIT times the tax rate cell, working capital is a link, and the discount factor reads the WACC tab, with no typed number inside any formula.")

Notice the taxes row in the historical columns: 2025A tax on EBIT is 49.0, but the income statement showed 43.0 of actual taxes, because the company deducted 24.0 of interest first. The DCF uses the 49.0 on purpose. The cash flow is unlevered, so the tax has to be unlevered too. The interest tax shield (the tax the company saves by deducting interest) shows up in the WACC through the after-tax cost of debt, and counting it twice is one of the classic errors in section 8.

### Step 11. Terminal value, enterprise value, equity value, share price

The five projected years are worth 627.9 today. Everything after 2030 is the terminal value, and there are two ways to size it. The exit multiple method says: at the end of 2030, sell the company at a multiple of its EBITDA that a buyer would pay for a business like this. The perpetuity growth (Gordon growth) method says: the 2030 cash flow grows at a steady rate forever, and a growing perpetuity is worth next year's cash flow divided by the discount rate minus the growth rate. The pack asks for the exit multiple as the method and the growth rate as the cross-check, which is how most banks run it.

| Line | Value |
|---|---|
| Sum of present values, FY2026E to FY2030E | 627.9 |
| FY2030E EBITDA | 325.5 |
| Exit multiple | 9.5x |
| Terminal value at the end of FY2030 | 3,091.8 |
| Discount factor, 5.0 years | 0.6450 |
| Present value of terminal value | 1,994.3 |
| Enterprise value | 2,622.2 |
| Terminal value as a share of enterprise value | 76.1% |
| Less: total debt | (400.0) |
| Plus: cash | 95.0 |
| Less: noncontrolling interest | (10.0) |
| Equity value | 2,307.2 |
| Diluted shares (millions) | 60.0 |
| Implied share price ($) | $38.45 |
| Current share price ($) | $38.00 |
| Implied upside / (downside) | 1.2% |
| Implied share price with end-of-year discounting ($) | $38.00 |
| Gordon growth cross-check: implied perpetual growth in the 9.5x multiple | 3.22% |
| Gordon growth cross-check: terminal value at 2.5% growth | 2,739.7 |
| Gordon growth cross-check: implied exit multiple | 8.4x |
| Gordon growth cross-check: implied share price at 2.5% growth ($) | $34.67 |
| Current EV / LTM EBITDA (market, for reference) | 10.8x |

![Excel terminal value and bridge from enterprise value to equity value to a 38.45 dollar share price](published/assets/images/financial-modeling-test-what-to-expect/14-terminal-value-and-bridge.png "The terminal value is discounted five full years at 0.6450 even though the cash flows use mid-year, and the Gordon growth rows underneath bracket the answer at $34.67.")

Terminal value is 2030E EBITDA of 325.5 times 9.5, which is 3,091.8. That's a 2030 number, so it gets discounted five full years, not 4.5: the sale happens at the end of the year, even when the cash flows use mid-year. One divided by 1.0916 to the fifth is 0.6450, and 3,091.8 times 0.6450 is 1,994.3. Enterprise value is 627.9 plus 1,994.3, or 2,622.2.

Then the bridge from the whole company to the shareholders. Enterprise value belongs to everyone who financed the business. Subtract the 400.0 of debt (lenders get paid first), add back the 95.0 of cash (the company holds it and it isn't needed to run the business), subtract the 10.0 of noncontrolling interest (the slice of a subsidiary owned by someone else). Equity value is 2,307.2. Divide by 60.0 million diluted shares: $38.45 a share, against a $38.00 market price. The DCF says the stock is about fairly valued, 1.2 percent of upside.

![Waterfall chart from present values and terminal value to enterprise value of 2,622.2 and equity value of 2,307.2](published/assets/images/financial-modeling-test-what-to-expect/15-value-bridge.png "The five years of cash flow are worth 627.9 and the terminal value 1,994.3, which is why the exit multiple is the assumption a grader argues with first.")

Three cross-checks a grader will ask about:

- **The terminal value is 76 percent of enterprise value.** Normal for a five-year DCF on a steady company; most land between 60 and 80 percent. Above 85 means the projection period is too short or the multiple is doing all the work.
- **The 9.5x exit multiple implies 3.22 percent perpetual growth.** Implied growth equals terminal value times WACC minus the final-year cash flow, divided by terminal value plus the final-year cash flow. 3.22 percent is a touch above the 2 to 3 percent you'd defend for an industrial, so the multiple is slightly generous. Run it the other way: at 2.5 percent growth the terminal value is 2,739.7, which implies 8.4x EBITDA and a $34.67 share price. The two methods bracket the answer, and the honest read is "somewhere between $35 and $38."
- **The market pays 10.8x trailing EBITDA for Torvik today, so a 9.5x exit assumes the multiple compresses as growth slows.** Trailing, or LTM, means the last twelve months of reported results. That's 2,595.0 of enterprise value (2,280.0 of market cap plus 400.0 of debt minus 95.0 of cash plus 10.0 of noncontrolling interest) over 240.0 of 2025A EBITDA. Assuming a turn of compression is the conservative and defensible choice.

The end-of-year line is there for the debrief: the mid-year convention adds about 45 cents to the share price, and you should be able to say so.

### Step 12. The sensitivity grid

A sensitivity table shows what the share price does when the two assumptions you're least sure of move. In Excel it's a two-way data table (Data, What-If Analysis, Data Table): WACC down the side, exit multiple across the top, the implied share price in the body, with a row and column input cell pointing at the WACC and multiple cells in the DCF. Build the axes off step-size cells (0.50 percent and 0.5x here) so the grid re-centers if the base case changes.

| WACC (down) / exit multiple (across) | 8.5x | 9.0x | 9.5x | 10.0x | 10.5x |
|---|---|---|---|---|---|
| 8.16% | $36.60 | $38.43 | $40.26 | $42.09 | $43.92 |
| 8.66% | $35.76 | $37.55 | $39.34 | $41.13 | $42.92 |
| 9.16% | $34.95 | $36.70 | $38.45 | $40.20 | $41.95 |
| 9.66% | $34.17 | $35.88 | $37.59 | $39.30 | $41.01 |
| 10.16% | $33.40 | $35.07 | $36.74 | $38.41 | $40.08 |

![Excel sensitivity grid of implied share price by WACC down the side and exit multiple across](published/assets/images/financial-modeling-test-what-to-expect/16-sensitivity-grid.png "The shaded center cell matches the DCF at $38.45, and a half turn of multiple moves the price about twice as far as a half point of WACC.")

The center cell is the base case, $38.45, and that's the first thing to confirm when the table fills: if the center doesn't match the DCF, the input cells are pointed at the wrong place. Read across: each half-turn of multiple is worth about $1.75 a share. Read down: each half point of WACC is worth about 85 cents. **The sensitivity grid tells the grader which assumption to argue with you about, and here the answer is the exit multiple, which moves the share price twice as fast as the discount rate.**

### Step 13. Flip the switch

Last, go to the Cover tab and change the one cell. Nothing else is touched.

| Scenario | FY2030E revenue | FY2030E EBITDA margin | FY2030E EBITDA | FY2030E UFCF | Enterprise value | Implied share price | vs $38.00 |
|---|---|---|---|---|---|---|---|
| Bear | 1,514.2 | 16.8% | 254.4 | 134.8 | 2,081.0 | $29.43 | (22.5%) |
| Base | 1,712.9 | 19.0% | 325.5 | 178.1 | 2,622.2 | $38.45 | 1.2% |
| Bull | 1,865.1 | 20.6% | 384.2 | 212.2 | 3,061.9 | $45.78 | 20.5% |

A flat industrial cycle with no margin expansion is worth $29 a share. Management's deck is worth $46. The market is sitting at the Base case. In a take-home, that's your football field; in a two-hour test, it's the last table you build and the one that proves the switch works.

### What a take-home version adds

With three days instead of two hours, the same workbook grows three tabs. A comps tab: five to eight real peers with price, shares, market cap, debt, cash, enterprise value, LTM and forward (next twelve months) EBITDA and EPS, with low, high, mean and median rows, so you can value Torvik at the peer median EV/EBITDA and P/E alongside the DCF. A football field: the low and high implied share price from each method (comps on EV/EBITDA, comps on P/E, the DCF's Bear, Base and Bull, the 52-week trading range) on one floating bar chart, so the reader sees where $38.00 sits. And the memo: five to ten slides with the recommendation on the first one, the thesis in three bullets, the DCF and comps summary, the sensitivity, the risks, and what you'd want to diligence. The model gets built the same way; the memo is where the take-home is actually graded.

## 6. A minute-by-minute time budget for a two-hour modeling test

Sam, a junior, came to WSG last fall a week after failing a growth equity modeling test. He'd built a three-way segment schedule with a cohort build nobody asked for, and when time was called he had no terminal value and no share price. The model was beautiful and it had no answer in it. The second time around, with the budget below taped to his desk, he finished with twelve minutes to spare and got the offer.

**Students who run out of time on a modeling test are almost never slow at Excel; they build in the wrong order and discover the model has no output at minute 105.** Build so that a half-finished model still scores: inputs, operating build, DCF, checks, sensitivities, formatting, in that order. **A grader can give partial credit to a DCF with no sensitivity grid and no credit to a sensitivity grid with no DCF, so build in the order that leaves an answer on the page at every minute.**

| Clock | Build | Why here |
|---|---|---|
| 0:00 to 0:08 | Read the prompt twice. Write every requested output on paper. Sketch the block order on the same page. | Building the wrong thing is the most expensive mistake and the cheapest to prevent. |
| 0:08 to 0:25 | Inputs tab: historicals in blue, ratios in black, segment build, assumptions block with the three scenario rows and the live row. Scenario switch cell on top. | Everything downstream points here. Typing it fast and clean now saves hunting later. |
| 0:25 to 0:45 | Operating build: segment revenue, income statement to EBIT, D&A, EBITDA, capex, all five projected years, one formula per row filled right. | The longest block. If you're past 0:50 here, drop the segment detail to one revenue line and keep moving. |
| 0:45 to 0:58 | Working capital by days and the PP&E roll-forward. Check row: segment total equals revenue; 2025A ending PP&E equals the filing. | Two short schedules that feed the cash flow. |
| 0:58 to 1:10 | Cost of debt, beta (unlever, median, relever), WACC. | Three small tables, mechanical once the pack's numbers are in. |
| 1:10 to 1:30 | DCF: EBIT to unlevered free cash flow, discount periods and factors, present values, terminal value by exit multiple, enterprise value to equity value to share price. | The answer. Nothing after this matters if this isn't done. |
| 1:30 to 1:38 | Checks: terminal value share of EV, implied growth, implied multiple at 2.5 percent, end-of-year versus mid-year, net debt sign. Set growth to zero in every segment and confirm nothing breaks; set it back. | This is the grader's first five minutes, run by you first. |
| 1:38 to 1:48 | Sensitivity grid with step cells. Confirm the center cell equals the DCF price. Flip the switch to Bear and Bull and note the three prices. | The two outputs that make the debrief easy. |
| 1:48 to 1:57 | Formatting pass: colors, number formats, units in the block headers, labels, freeze panes, no hidden rows. Delete scratch cells. | Cleanliness is 15 percent and takes nine minutes. |
| 1:57 to 2:00 | Save with the filename the prompt asked for. Open it again to confirm it saved. | Every cycle, someone hands in an empty file. |

![Timeline bar chart of the two-hour modeling test budget, block by block, with the DCF from 1:10 to 1:30](published/assets/images/financial-modeling-test-what-to-expect/17-time-budget.png "Lay the budget on one clock and the order is the point: the DCF is finished at 1:30, and everything after it is checking, sensitivities and cleanup.")

Save every fifteen minutes regardless, and once more at 1:30 before you touch the sensitivity table, because a data table on a slow laptop is the one thing in this build that can freeze Excel.

For a 90-minute version, compress the middle: ten minutes less on the operating build (one revenue line, no segments), no PP&E roll-forward, and the sensitivity only if you're at 1:20 with the DCF done. For a three-hour version, the extra hour goes to an integrated balance sheet and cash flow statement under the DCF, not to a fancier DCF.

## 7. What to add and what not to add under time pressure

The prompt decides. When it leaves room, here's the order. **Under time pressure, add the things a grader checks and skip the things a grader merely admires.**

**Add, in this order:**

1. A check row for every tie the grader would test: segment total to revenue, PP&E to the filing, sources equal uses if there's a transaction, the sensitivity center equals the DCF.
2. The scenario switch, if the assumptions block already has three rows. It's one cell and one CHOOSE per driver, ten minutes at most, and it turns one answer into three.
3. A one-line sensitivity: even a single row of share price across five exit multiples, if the two-way table won't fit.
4. The Gordon growth cross-check: two cells (implied growth, implied multiple) that answer the first debrief question before it's asked.
5. The end-of-year share price next to the mid-year one, so you can quantify the convention.
6. A short outputs block at the top: 2030E revenue, EBITDA, WACC, enterprise value, share price, upside. A grader who sees the answer in the first screen relaxes.

**Skip unless the prompt asks:**

- Segment detail beyond what the pack gives. If the pack has three segments, build three; don't split pumps into product lines because the CIM mentions them.
- A tax schedule (deferred taxes, net operating losses). One rate on EBIT.
- Stock-based compensation detail. In a two-hour DCF, leave it in SG&A as a cost and don't add it back; say so in the debrief if asked.
- A full comps tab. Name the market multiple in a cell for the cross-check and move on.
- A treasury stock method share count (the calculation that adds the shares in-the-money options would create), unless the pack gives you options and strike prices. Use the diluted count from the filing.
- Leases, pensions, equity method investments. Hold them where the balance sheet has them.
- Quarterly periods. Annual.
- Chart formatting. A football field chart is a take-home deliverable. In a timed test, the sensitivity table is the chart.
- Custom number formats, conditional formatting, named ranges. The color code is enough.

**A correct simple DCF beats an incorrect ambitious one every time, because the grader is deciding whether to trust you with a live model, not whether you can build every schedule in the textbook.**

## 8. The mistakes that fail financial modeling tests

**Most failed modeling tests fail on one of ten mechanical errors, and each one has a mechanism you can learn to see coming.** I've used the Torvik model to show what the common ones do to the answer, so you can see why a grader treats them as failures rather than slips.

**The working capital sign is flipped.** Increase in receivables added to cash flow instead of subtracted. In Torvik's model, adding the five years of working capital growth instead of subtracting it moves the share price from $38.45 to $40.22: the company got more valuable for tying up more cash, which is backwards. In December 1994, a Fidelity tax accountant transcribing numbers for the Magellan fund's year-end estimate [omitted the minus sign](https://catless.ncl.ac.uk/Risks/16.72.html) on a $1.3 billion net capital loss, which turned it into a $1.3 billion gain, a $2.6 billion swing; the fund had told shareholders to expect a $4.32 a share distribution and then had to cancel it. All of that came from one missing minus sign.

**The terminal value isn't discounted.** The 3,091.8 of 2030 terminal value gets added to today's present values at face. Torvik's share price jumps from $38.45 to $56.74. A grader who sees an implied upside of 49 percent on a steady industrial clicks the terminal value cell first and finds this within thirty seconds.

**Tax on pretax income instead of EBIT.** The candidate pulls the income statement's taxes (43.0 in 2025A) into the cash flow instead of computing tax on EBIT (49.0). Every projected year's cash flow is 6.0 too high (the 24.0 of interest times 25 percent), and the interest tax shield is counted twice, once here and once in the after-tax cost of debt in WACC. Torvik goes to $38.86. Smaller than the other two, which is exactly why it gets through: the number looks fine and the method is wrong.

**Fiscal and calendar years are mixed.** A company with a September fiscal year end gets a December 31 valuation date and whole-year discount periods, so every cash flow is discounted a quarter too long or too short. Or a trailing twelve month EBITDA (the last four reported quarters) sits in a fiscal year column next to annual numbers. Check the fiscal year end in the first five minutes and write it on the Cover tab.

**A hardcoded plug.** The balance check is off by 12.0, so the candidate types 12.0 into a cell to make it zero. Graders find typed plugs by clicking the check row's inputs, and it ends the conversation. **An honest check that's off by 12.0 with a note beside it scores better than a forced zero, because the first shows judgment and the second hides a problem.** The note can be one line: "check off by 12.0, likely deferred revenue, out of time."

**A circular reference with no toggle.** A DCF doesn't usually need one, but a three statement build with interest on average debt does: interest depends on debt, debt depends on cash, cash depends on interest. Without a switch cell that sets interest to the beginning balance, one wrong keystroke fills the model with errors at minute 100. Build the toggle before you build the circularity.

**An unlabeled unit.** Revenue in thousands next to debt in millions, or a share count in millions divided into an equity value in thousands, so the implied price is off by a thousand. Units go in the block header once ("$ millions, except per share") and every number in the block obeys them.

**A model that only works for the Base case.** The switch is there, but flipping it to Bear produces an error, because one formula points at the Base row instead of the live row. Flip the switch before you hand in. It takes four seconds.

**A formula range that stops short.** The SUM for total revenue catches two segments of three because a row was inserted after the formula was written. This is the Reinhart and Rogoff error from the top of this article: an average whose range left five countries out, in a paper that [policymakers quoted](https://en.wikipedia.org/wiki/Growth_in_a_Time_of_Debt) to justify austerity, found by a graduate student who tried to rebuild it. After you insert any row, press Ctrl plus backslash on the total's row to find the cell whose formula differs from its neighbors, and press F2 on every subtotal once before you save.

**No saved file.** It happens every cycle.

## 9. How to practice for a financial modeling test, four weeks out and one week out

The test rewards one thing above all: having built this exact model, from a blank sheet, enough times that your hands know the order. **Reading about a DCF prepares you for the interview question; building one from a blank sheet three times prepares you for the test, and those are different skills.** Here's the plan I give students.

### Four weeks out: get the layout into your hands

Week one is learning the layout from a finished file, then rebuilding it. My rule for linking a template is that it has to be free, from a source bankers recognize, and built the way this article teaches. Two clear the bar. [Mergers & Inquisitions](https://mergersandinquisitions.com/3-statement-model/) posts the completed Excel file from its 90-minute three statement case on Otis Worldwide, downloadable from the article [VERIFY: file still downloadable without signup at publish]: three historical years, five projected, a drivers block on top, a balance check row. [A Simple Model](https://www.asimplemodel.com/resources/quick-references/free-downloads) lists a free LBO model download on its quick references page [VERIFY: download still free and ungated at publish], which is the right file to reverse-engineer for the timed LBO format. Macabacus, Wall Street Prep and the Corporate Finance Institute all have good DCF templates, but each one sits behind a trial, an email signup or an account [VERIFY: gating at publish], so I'm not linking them; if you're deciding whether to pay for a course, our [review of Wall Street Prep](https://www.wallstreetguide.net/post/is-wall-street-prep-worth-it-4-pros-and-cons-you-need-to-know) is the honest read.

For a public company to practice on, go to [EDGAR](https://www.sec.gov/search-filings), the SEC's filing database, type a ticker, open the latest 10-K, and pull the fifteen lines from the table in section 3. Pick a company with two or three segments and a boring capital structure: an industrial, a packaging company, a food company. Avoid banks (no EBITDA, no working capital in the normal sense), insurers, and anything with a fiscal year that doesn't end in December, at least for the first few builds.

Week one: open the M&I file, trace every formula with Ctrl plus left bracket until you can say what each block does. Then close it and rebuild the three statement model from a blank sheet with the same inputs. Untimed. It'll take four hours. That's fine.

Week two: the DCF. Build Torvik from this article's tables, from blank, every step in section 5. Then build it again on a real 10-K. Untimed, but write down how long each took.

### The rebuild-from-memory drill

Weeks three and four are the same drill, three times each week: the same model, from a blank workbook, timed, no notes, no template open. **Build the same model three times from a blank sheet, timed, because the first build teaches you the model and the third build teaches you where your own fingers slow down.**

Build one, start the clock, stop when the share price appears, write the time down. Build two, same model, same day or the next: you'll be a third faster and you'll notice the two blocks you fumbled. Build three: those two blocks are what you drill in between. By the sixth build, a Torvik-sized DCF from blank takes most students 70 to 80 minutes, which leaves 40 minutes of a two-hour test for checks, sensitivities and formatting.

Then change the format. One build as a 60-minute timed LBO from a one-page prompt (use the A Simple Model file's inputs). One as a 30-minute paper LBO, out loud, with a friend reading the inputs. One as a 90-minute three statement build. The format you'll be tested on gets the most reps, but one of each keeps you from freezing when the prompt isn't what you expected.

### The 20 Excel shortcuts that matter

Twenty shortcuts cover almost everything a modeling test asks your hands to do. These are the Windows keys. Mac Excel maps some of them differently, and a test on a firm laptop will be Windows, so practice on Windows.

1. **Ctrl plus arrow key.** Jump to the edge of a data block. Ctrl plus right from the label lands on the last year.
2. **Ctrl plus Shift plus arrow key.** Select from here to the edge. The way you grab a row of formulas before filling.
3. **F2.** Edit the cell in place and see its formula with each reference colored. The single most used auditing key.
4. **F4.** While editing a formula, cycle the selected reference through $C$5, C$5, $C5 and C5. Outside editing, it repeats your last action.
5. **Ctrl plus R, Ctrl plus D.** Fill right, fill down. Write a year's formula once, select across, Ctrl plus R.
6. **Alt plus equals.** AutoSum. Puts a SUM over the block above or to the left.
7. **Ctrl plus 1.** Format Cells. Number formats, font color, borders, all from one dialog.
8. **Ctrl plus Shift plus 1, Ctrl plus Shift plus 5.** Number format with two decimals and commas; percent format.
9. **Alt, then H, then F, then C.** Opens the font color menu from the Home tab, for turning a hardcode blue. (Pressing Alt alone shows the ribbon's key letters, so any ribbon command is reachable without a mouse.)
10. **Ctrl plus Page Up, Ctrl plus Page Down.** Previous and next sheet.
11. **Ctrl plus left bracket.** Select the cells this formula refers to, the precedents. The fastest way to check where a number came from. F5 then Enter takes you back.
12. **Ctrl plus right bracket.** Select the cells that depend on this one. Press before deleting anything.
13. **Ctrl plus grave accent (the key under Escape).** Show every formula on the sheet at once instead of the values. Press again to go back. Ten seconds of this before you hand in finds typed numbers hiding in formula rows.
14. **Ctrl plus backslash.** Row differences: select a row of formulas and this highlights any cell whose formula doesn't match the one in the active cell. Run it on every row after you insert a column.
15. **Alt, then M, then P; Alt, then M, then D.** Trace precedents and trace dependents arrows from the Formulas tab; Alt, then M, then A, then A removes the arrows.
16. **Alt, then W, then F, then F.** Freeze panes at the active cell, so labels and years stay on screen.
17. **Shift plus Space, then Ctrl plus Shift plus plus; Ctrl plus minus.** Select the row, insert a row above it; delete the selected row. Then press Ctrl plus backslash on the totals.
18. **Alt, then A, then W, then T.** Data, What-If Analysis, Data Table: the two-way sensitivity grid.
19. **F9.** Recalculate everything. If the sheet is on manual calculation (some firms set it that way for big models), nothing updates until you press it.
20. **Ctrl plus S.** Save. Every fifteen minutes.

A footnote on where these come from. The first spreadsheet to own the business desktop was Lotus 1-2-3, released on January 26, 1983: the IBM PC's first killer app, 175,000 copies sold in its first year, and so dominant through the decade that every command lived behind the slash key. Excel replaced it in the early 1990s, but open Excel's Advanced options today and scroll to the bottom: there's still a section called [Lotus compatibility](https://support.microsoft.com/en-us/office/advanced-options-33244b32-fe79-4579-91a6-48b3be0377c4), with a "Microsoft Excel menu key" box that holds a slash, and a "Transition navigation keys" setting that turns on Lotus's keystrokes. Forty years on, the program still remembers the one it beat.

### The no-mouse rule

For the last two weeks before the test, unplug the mouse when you practice. Every navigation, selection, format and fill becomes a keystroke. The first hour is miserable. By the third build, you'll be faster than you were with the mouse, because your hands never leave the keyboard and your eyes never leave the cell. **In a live build on a shared screen, the grader can see your mouse, and a candidate who reaches for it to click into a cell looks like someone who hasn't built many models.**

### Auditing your own model before you hand it in

The grader's first five minutes are an audit. Run the same audit in your last ten.

- F2 on every subtotal, reading the colored references. A SUM that doesn't cover the whole block shows up here.
- Ctrl plus left bracket on the share price, then on each number that feeds it, back through the chain to the inputs. Every step should land on a formula or a blue cell. If it lands on a black cell holding a typed number, that's a hardcode in disguise.
- Ctrl plus grave accent to show formulas, scroll the projected columns once, and look for any cell that shows a number instead of a formula.
- Ctrl plus backslash on each row of the DCF to catch the one year that differs.
- Trace precedents arrows (Alt, then M, then P) on the terminal value cell: the arrows should point at 2030E EBITDA and the multiple cell, and nothing else.
- Flip the scenario switch to Bear and Bull. No errors, prices in the right order.
- Set WACC to 20 percent and confirm the share price falls. Set the exit multiple to zero and confirm the terminal value goes to zero. Set them back.
- Check the fiscal year end, the units line, the valuation date and the filename against the prompt.

If you've done the [50 accounting questions](https://www.wallstreetguide.net/post/50-accounting-interview-questions-that-you-should-practice-before-your-interview) that come up in the interview around the test, this list will feel familiar: it's the same links, checked in a spreadsheet instead of out loud.

### One week out

Stop learning and start rehearsing. Three timed builds of the test's format, one a day, in the morning when the real one is likely to be. One build on an unfamiliar 10-K to make sure you can find the inputs cold. One session with a friend playing grader, opening your file and asking the section 10 questions. Then two days off Excel before the test; the model is in your hands by now, and the thing that fails tired candidates is reading the prompt wrong, not the formulas.

## 10. The debrief: say this, don't say that

The questions after a modeling test are short and specific, and the grader already knows the answer because they just read your file. They want to hear that you do too. **Every debrief answer has the same shape: name the assumption, give the reason, and say what happens to the price if it's wrong.**

**Why 2.5 percent terminal growth?**
Don't say: "It's the standard assumption."
Say: "A company can't outgrow the economy forever, so long-run GDP growth is the ceiling. Most analysts use 2 to 3 percent for a mature industrial, around inflation plus a little, and I picked the middle. I also ran the exit multiple the other way: 9.5x implies 3.2 percent perpetual growth, so the multiple is a touch generous and the perpetuity method lands lower, at about $35."

**Why a 9.5x exit multiple?**
Don't say: "That's what the pack gave me." (Even if it did. They know. They want the reason it's reasonable.)
Say: "The market pays 10.8x trailing EBITDA today. By 2030 revenue growth has slowed from almost 6 percent to 4, so a buyer should pay a bit less. 9.5x assumes a turn of compression, which is the conservative side, and the sensitivity shows every half turn is worth about $1.75 a share."

**What would change your number the most?**
Don't say: "Revenue growth." (It's the answer everyone gives and it's rarely the right one in a DCF.)
Say: "The exit multiple, then the WACC. Seventy-six percent of enterprise value is terminal value, so a half turn of multiple moves the price about $1.75 and a half point of WACC moves it about 85 cents. The operating assumptions matter mostly through 2030 EBITDA, and the Bear case shows what a flat cycle does: $29 instead of $38."

**Walk me through the working capital line.**
Don't say: "I grew it with revenue."
Say: "Receivables are 60 days of revenue, inventory 90 days of cost of sales, payables 45 days of cost of sales, straight from the 2025 balances. Net working capital runs about 18.5 percent of revenue and grows about $13 million a year, which is a use of cash, so it's subtracted. If the company could pull receivables to 50 days, that's about $39 million of cash released in year one, which is why working capital is the first thing a buyer looks at."

**Why mid-year discounting?**
Don't say: "It gives a higher value."
Say: "Torvik's cash comes in across the year, so discounting as if it arrived at the midpoint is closer to the truth than assuming December 31. It adds about 45 cents a share here. For a seasonal retailer I'd use end-of-year. The terminal value is still discounted five full years because the sale happens at year end."

**Why tax on EBIT and not on pretax income?**
Don't say: "Because that's how the formula goes."
Say: "The cash flow is unlevered, before any financing, so the tax has to be what the company would pay with no debt. The benefit of deducting interest is already in the WACC through the after-tax cost of debt, 4.52 percent instead of 6.03. Using the income statement's taxes would count that benefit twice."

**Your balance doesn't check. What happened?** (If it doesn't.)
Don't say: "It's basically right, it's just a small difference."
Say: "It's off by 12.0 in every year. A constant gap is a missing link rather than a sign error, because a sign error would grow. My guess is deferred revenue isn't flowing to the balance sheet. I'd fix it with another ten minutes; I left the check visible rather than plugging it."

## Build Torvik three times before you need to

The modeling test is the one round in finance recruiting where the result is in your hands, in the plain sense. Nobody's judging your story or your fit. There's a prompt, a clock, and a file, and the file either works or it doesn't.

So treat it the way Herndon treated the Reinhart and Rogoff spreadsheet: assume someone will open every cell. Build this article's DCF from a blank sheet this weekend, untimed, every table. Build it again next week with the clock running. Build it a third time with the mouse unplugged. By the third build you'll know exactly which block slows you down, and that's the one to drill. **The students who pass aren't the ones who know the most about valuation; they're the ones who've built the model enough times that the test feels like the fourth build instead of the first.**
