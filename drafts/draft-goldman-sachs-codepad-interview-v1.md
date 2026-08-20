---
headline: "Goldman Sachs CodePad Interview: 8 Questions to Expect"
byline: stephen-turban
target_keyword: goldman sachs codepad interview
secondary_keywords: [goldman sachs coderpad, goldman sachs coding interview, goldman sachs hackerrank, gs engineering interview]
format: listicle
word_count_target: 1800-2200
status: draft-v1
---

# Goldman Sachs CodePad Interview: 8 Questions to Expect

**Meta description:** WSG founder Stephen Turban breaks down the Goldman Sachs CodePad interview: where it sits in the funnel, 8 reported questions, and how engineers actually grade it.

**The CodePad round is a live, 45-to-60-minute coding interview where a Goldman Sachs engineer watches you solve one to two problems in a shared editor, and your code has to actually run.** It sits in the middle of the engineering funnel, after the HackerRank assessment and before Superday, and it cuts more candidates than either neighbor. Recent candidates describe the difficulty as one LeetCode easy to warm up, then one medium that decides the round.

Goldman opens 2027 Summer Analyst applications on August 15, 2026 [VERIFY: GS program page], so the students WSG coaches toward engineering seats are staring this round down right now. Here's the funnel, the eight most-reported questions, and what the interviewer's rubric rewards.

## What is the Goldman Sachs CodePad interview?

CodePad is the name candidates and recruiters use for Goldman's live technical screen, run on a collaborative editor in the CoderPad style with an engineer present. It is a conversation, never an async test: you talk through your approach, code it, run it, and debug it while they watch. US campus candidates often meet it as two back-to-back 45-minute technical interviews.

## Is CodePad the same as the HackerRank test?

No. Goldman's [official prep page](https://www.goldmansachs.com/careers/students/prepare) says engineering applicants take a HackerRank assessment, and that's the earlier, automated stage: timed problems, no human watching, formats ranging from two to four coding questions to mixed sets with logic and even machine-learning multiple choice [VERIFY: current OA format]. CodePad comes after, sometimes alongside a roughly 30-minute HireVue video interview. Different stage, different skills, different prep.

## The funnel, end to end

The 2025-26 reported sequence for engineering campus hires: apply through Goldman's [students hub](https://www.goldmansachs.com/careers/students), complete the HackerRank assessment, record the HireVue (five to seven questions, mostly behavioral with one technical and one markets-flavored), then the CodePad round or rounds, then a Superday of two to five interviews mixing coding, light system design, object-oriented concepts, and behaviorals. Average reported timeline runs about eight weeks application to offer. Formats drift by region and cohort, so treat recruiter emails as the authority on your version.

## Two tracks, one funnel

Goldman splits campus engineering into Summer Analyst roles, the nine-to-ten-week internship for penultimate-year students, and New Analyst roles for final-year students and recent grads going straight to full time. Both tracks report the same stage sequence, and both route through the same application portal. Regional cohorts differ more than tracks do: India cycles opened in early July 2026 with the Americas following August 15, and reported assessment formats vary most across regions [VERIFY: regional opening dates].

Note which division you're applying to as well. Engineering sits alongside Goldman's banking and markets tracks, with its own recruiters and its own interview content. Nothing in this article covers the IB technical interview; a DCF will not save you in a CodePad round.

## The 8 questions to expect

All eight below come from candidate interview reports on Glassdoor, LeetCode discussions, and engineering forums from 2021 through 2026. Goldman rotates specifics, so drill these as patterns rather than answers.

### 1. Trapping rain water

**The single most-reported Goldman question, appearing in both CodePad and Superday reports.** Given elevation heights, compute trapped water. Brute force is quadratic; the expected answer uses prefix maxima or two pointers for linear time. Interviewers reportedly push for the space-optimized version once your first pass works.

### 2. Compress a string with run-length encoding

**String manipulation opens many Goldman loops because it exposes off-by-one discipline fast.** Turn "aaabbccaaaa" into "a3b2c2a4". The trap is the final group falling out of the loop unprinted. Reported in both the online assessment and live rounds. The follow-up usually asks what happens when the compressed string runs longer than the original, and whether you'd return it anyway.

### 3. Longest substring without repeating characters

**Sliding window plus a hashmap is the pattern Goldman tests most across its stages.** Track last-seen indices, move the left edge on repeats, record the max. If you can't write this in ten minutes cold, you're not ready for the round.

### 4. Minimum meeting rooms for overlapping intervals

**Interval problems show up in finance interviews because scheduling and booking conflicts mirror real desk systems.** Sort start times, use a min-heap of end times, and the heap's peak size is the answer. Say that sentence out loud before coding and the interview tilts your way.

### 5. Design an LRU cache

**The LRU cache question grades design instinct, and it recurs in Goldman Superday reports.** Hashmap for lookups plus a doubly linked list for recency gives constant-time operations. Interviewers reportedly care less about finishing every method than hearing why the two structures pair.

### 6. Group anagrams

**Hashing with a canonical key is the concept under this reported Superday question.** Sort each word as its key, or count characters for the faster variant, and bucket the results. The follow-up usually probes the complexity difference between the two key strategies.

### 7. Shortest time to reach every node in a network

**Graph questions at Goldman stay practical: machines, connections, propagation time.** With unit edge weights this is breadth-first search from the source, tracking depth. Candidates report pairing questions like this with a quick linked-list warm-up, finding the middle of a list, in the same session. Expect the follow-up to add weighted edges and ask what changes, which is your cue to say Dijkstra and explain why the plain queue stops working.

### 8. Valid parentheses

**Stack questions are Goldman's favorite warm-up, and fumbling one ends rounds early.** Push openers, match closers, and an empty stack at the end means valid. Reported in recent online assessments alongside a buy-sell stock array question of similar weight.

## The three mistakes that end rounds early

Debriefs from students we've coached through this loop repeat three failure patterns, and none of them is "couldn't solve it."

Coding before agreeing on the problem. Strong candidates restate the input, the output, and one edge case, then ask "is that the right read?" before writing a line. Weak candidates burn fifteen minutes building the wrong function beautifully.

Ignoring the run button. The editor executes code, and interviewers report that candidates who never run anything until the end signal that they don't work the way engineers work. Run early, run often, and narrate what each failure tells you.

Freezing on the optimization ask. "Can you do better than O(n squared)?" is an invitation, never an ambush. The expected response is thinking out loud about which data structure buys down the inner loop. Silence is the only wrong answer.

## The HireVue and Superday bookends

The HireVue deserves an evening of its own prep. Recent engineering candidates report seven questions in about 30 minutes, five behavioral, one technical, one finance-adjacent, each with 30 seconds of prep and two minutes of answer. Record yourself once against a timer; the format punishes ramblers more than it punishes nerves.

Superday runs two to five interviews in a day, and reports from early 2026 describe one round of pure problem solving and one mixing system design at survey depth, object-oriented questions like singleton and factory patterns, and behaviorals with your resume open. Teams vary: a strat-leaning desk asks probability, a platform team asks about services and caching. **Superday interviewers assume you can code by that stage, so the differentiator becomes whether they'd want to sit next to you during an outage.**

## What the interviewer is actually grading

Engineers who run these rounds describe the rubric consistently: state an approach before coding, write code that compiles and runs, name the time and space complexity unprompted, and test your own edge cases before declaring victory. One Superday report put it plainly, that they want quality code rather than a math wizard. Communication is scored the whole way through, which is why silent perfect solutions underperform talkative imperfect ones.

Behavioral threads run through technical rounds too. The HireVue mixes in questions like how you'd debug a production issue and one finance-adjacent prompt such as how you'd value a company, at survey depth only.

## How to prepare in four weeks

Week one: 20 easy problems on arrays, strings, and hashmaps, all typed into a bare editor without autocomplete, since the CodePad environment strips your IDE comforts. Weeks two and three: 25 mediums weighted toward the patterns above, plus [HackerRank's interview kit](https://www.hackerrank.com/interview/interview-preparation-kit) to match the OA's house style. Week four: mock interviews out loud, ideally with a CS friend playing a probing interviewer, because narrating while coding is a separate skill from coding.

Pick one language and stay in it; candidates report Python, Java, and C++ all land fine, and interviewers occasionally quiz fundamentals in your chosen one, like Python's Timsort behind the sort call or how Java hashmaps resolve collisions. Fluency in one beats tourism across three.

Comp for context: entry-level Goldman engineers report roughly $111,000 in total first-year pay on self-reported trackers, with wide variance by team and city [VERIFY: Levels.fyi self-reported, small sample].

## Say this, don't say that

**When you're stuck mid-problem:**
Don't say: nothing, while typing and deleting the same line for three minutes.
Say: "My hashmap approach breaks on duplicates. Give me a second to check whether sorting first fixes the key collision."

**When asked why Goldman engineering:**
Don't say: "Goldman is a prestigious firm with great technology."
Say: "I read about the risk platform work in the engineering blog, and a second-year analyst I spoke with in June described rebuilding a pricing service used by three trading desks. Shipping code that moves real money is the draw."

## What about the questions not on this list?

Rotation is constant, so cover the categories these eight represent rather than memorizing them: arrays and two pointers, strings, hashmaps, stacks and queues, light trees and graphs, and one design question like LRU. Recent online assessments have added machine-learning and prompt-engineering multiple choice for some cohorts, worth a skim if your OA invite mentions it. Dynamic programming appears rarely and stays light when it does.

Applications for the 2027 Summer Analyst class open August 15, 2026, and Goldman screens on a rolling basis [VERIFY: rolling review policy]. Submit inside the first two weeks, book your OA while the material is fresh, and treat every CodePad mock as a conversation rehearsal. The code gets you considered. The narration gets you hired.
