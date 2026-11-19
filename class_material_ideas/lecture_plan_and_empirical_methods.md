# MGFD40: Proposed Lectures 2–6 and the Empirical Toolkit

The proposal follows the structure in `lecture_introduction.tex`: one foundations block, then the three big themes (Overreaction, Underreaction, Mispricing). It reuses content from the current lectures 1–5 and maps each lecture onto sections of *The Madness of Markets* (see `Madness_of_Markets_research_papers.md`).

The guiding idea: **every lecture teaches one behavioural phenomenon and one empirical method**, and the method is taught through a paper from the book. By the midterm, students should be able to read a finance paper's tables and design a basic test themselves.

Lecture 1 is the introduction, which is already done.

---

## Overview

| Lecture | Theme | Book chapters | Core method taught |
|---|---|---|---|
| 2 | Foundations: how investors decide | Ch 2, 9, 10 | Reading a regression table; exogenous shocks as "clean tests"; spurious correlation |
| 3 | Market efficiency: is it risk or is it mispricing? | Ch 1 (limits to arbitrage), Ch 3 (Carhart, Berk–Green), Ch 6 (carbon) | Event studies; portfolio sorts; factor alphas; risk-vs-mispricing tests |
| 4 | Overreaction | Ch 1, 3, 4 | Long-horizon returns; double sorts; using exogenous price pressure; identification (homophily) |
| 5 | Underreaction | Ch 5, 6, 7 | Testing the mechanism through cross-sectional heterogeneity; Fama–MacBeth; text and alternative data |
| 6 | Mispricing ("misreaction") and limits to arbitrage | Ch 8, 9 | Law-of-one-price tests; horse-race regressions; bunching/threshold tests; backtest hygiene |

*(If the midterm comes after Lecture 6, everything below is examinable.)*

---

## Lecture 2: Foundations: How Investors Actually Decide

*(Merges current Lectures 2 and 3)*

### What to cover

- Expected utility vs. prospect theory (Kahneman & Tversky 1979): loss aversion, reference points, probability weighting.
- The disposition effect: Shefrin & Statman (1985), Odean (1998); realisation utility (Barberis & Xiong 2012); the rolled-disposition fix (Frydman, Hartzmark & Solomon 2018).
- Heuristics: anchoring, representativeness and the law of small numbers, gambler's fallacy (Chen, Moskowitz & Shue 2016).
- Overconfidence: Barber & Odean (2000, 2001, 2002), Robinhood attention trading (Barber et al. 2022).
- Mood: sunshine (Hirshleifer & Shumway 2003), football (Edmans, García & Norli 2007), music sentiment (Edmans et al. 2022).

### Methods to teach

1. **How to read a regression table** (do this first and repeat it every lecture). Cover:
   - coefficient sign and size;
   - standard error and t-stat (|t| > 1.96, plus the modern t > 3 hurdle);
   - economic vs. statistical significance (the effect of a one-standard-deviation change);
   - R² (why it's tiny in return regressions and why that's fine);
   - fixed effects ("within-country", "within-month");
   - clustered standard errors (why errors in the same month or firm are correlated).

   Vehicle: the football paper's main table. Loss dummy coefficient ≈ −0.4% for World Cup elimination games.
2. **Exogenous shocks as natural experiments.** Why weather, sports and clock changes are "clean". They shift mood without changing cash flows, so a risk story can't explain the result. This is the students' first exposure to the logic of identification.
3. **Spurious correlation and data mining.** Tyler Vigen's correlations, Paul the Octopus, and out-of-sample replication (Saunders → Hirshleifer & Shumway). This sets up multiple testing in Lecture 3.
4. **Building a behavioural measure from trading data.** Odean's PGR vs. PLR (proportion of gains realised vs. proportion of losses realised). It's simple enough to compute by hand on an exam.

---

## Lecture 3: Market Efficiency: Is It Risk or Is It Mispricing?

*(Merges current Lectures 4 and 5. This is the methods core of the course.)*

### What to cover

- EMH (weak, semi-strong, strong), the joint-hypothesis problem, and the three pillars (rational investors, uncorrelated errors, unlimited arbitrage).
- Limits to arbitrage: Shleifer & Vishny (1997), Tiger vs. Soros (Brunnermeier & Nagel 2004).
- Anomaly survival after publication: McLean & Pontiff (2016), Jacobs & Müller (2020).
- Fund performance as a test of efficiency: Carhart (1997), Berk & Green (2004).

### Methods to teach

1. **Event studies, step by step.**
   - Choose the estimation window and the event window.
   - Choose the expected-return model: market-adjusted, market model, or a factor model.
   - Compute AR, CAR and the cross-sectional t-test.
   - Watch for pitfalls: event clustering and confounding events.

   Vehicles: Huberman & Regev (EntreMed, stale news) and Bernard & Thomas (PEAD plot).
2. **Portfolio sorts.** Quintiles/deciles, long-short returns, equal- vs. value-weighting, NYSE breakpoints, and why microcaps can drive results.
3. **Factor regressions and alpha.** CAPM → FF3 → Carhart → FF5. Cover what the loadings say about a strategy (e.g., a value strategy loads on HML) and how alpha shrinks as factors are added.
4. **Risk vs. mispricing: the test toolkit.** This is the most important block of the course. Teach it as a checklist of tests, each tied to a paper:

   | Test | Logic | Paper from the book |
   |---|---|---|
   | **Earnings-announcement returns** | If returns are risk compensation, they shouldn't bunch on the 4 days when news arrives. If they're mispricing, a large share comes from positive surprises. | Edmans (2011): 40% of the Best Companies' alpha comes on announcement days. Atilgan, Demirtas, Edmans & Gunaydin: carbon premium. Bernard & Thomas (1990). |
   | **Analyst forecast errors** | Mispricing implies predictable errors in forecasts. | Edmans (2011); La Porta-style tests; Hartzmark & Solomon (2019, dividends) |
   | **Bad-state performance** | Risky strategies should do badly in recessions and crashes. | Lakonishok, Shleifer & Vishny (1994): value didn't underperform in bad states |
   | **Reversal** | Mispricing driven by non-fundamental demand should reverse; information shouldn't. | Edmans et al. (2022, music); Cookson et al. (attention spikes reverse the next day); Coval & Stafford (2007) |
   | **Mechanism heterogeneity** | The effect should be stronger where the bias or limits to arbitrage are stronger. | Hong, Lim & Stein (2000); Chopra et al. (1992); McLean (2010) |
   | **Exogenous mood shocks** | The shock has no cash-flow content, so there's no risk story. | Football, sunshine, SAD |
   | **Post-publication decay** | Risk premia shouldn't disappear when published; mispricing should shrink. | McLean & Pontiff (2016) |

5. **Multiple testing.** At 5%, 100 useless signals give about 5 "discoveries". Cover the Harvey, Liu & Zhu t > 3 hurdle and the factor zoo (already in L5).

---

## Lecture 4: Overreaction

### What to cover

- Extrapolation: Greenwood & Shleifer (2014); Shiller (1981) excess volatility.
- Long-run reversal (De Bondt & Thaler 1985; Zaremba et al. across 7 centuries) and value (Lakonishok, Shleifer & Vishny 1994; Asness, Moskowitz & Pedersen 2013).
- Size, and "size matters if you control your junk" (Asness et al. 2018).
- Overreaction to non-news: stale news (Huberman & Regev), LEI (Gilbert et al.), seasonality (Chang et al.), ticker confusion (Rashes), name changes (Cooper, Dimitrov & Rau).
- Fire sales: Coval & Stafford (2007); Edmans, Goldstein & Jiang (2012).
- Herding and social networks: Bailey et al. (2018), Pool, Stoffman & Yonker (2015), Cookson, Engelberg & Mullins (echo chambers), WallStreetBets.
- Real effects: catering (Polk & Sapienza 2009); M&A cancellations (Luo 2005).

### Methods to teach

1. **Measuring long-horizon returns.** CAR vs. BHAR, why they diverge over 3–5 years, and the "bad model" problem. Introduce **calendar-time portfolios** as the fix.
2. **Double (conditional) sorts.** For example, reversal *within* size groups, or size *within* quality groups (the "control your junk" result). This is how you show an effect isn't just another known effect in disguise.
3. **Using non-fundamental price pressure as an instrument.** Mutual-fund-flow-driven sales (Coval & Stafford; Edmans, Goldstein & Jiang). Key idea: the client redeeming from a fund isn't trading on information about the stock, so the price drop is exogenous. This is students' first look at an instrumental-variable argument without the econometrics jargon.
4. **Identification in social-network studies.** The problem: homophily and shared information vs. genuine influence. Three solutions from the book:
   - **Distant friends** (Bailey et al.): the shock happens where your friends live, not where you live.
   - **Timing around moves** (Pool et al.): check that portfolio overlap appears only *after* the managers become neighbours. This is an event-time plot with **pre-trends**, a gentle intro to difference-in-differences.
   - **Random assignment of interaction** (Maturana & Nickerson): overlapping free periods.
5. **Placebo tests.** Huberman & Regev (the stock reacted to the same news twice). Name-change firms with no change in business are a placebo for "real" internet pivots.

---

## Lecture 5: Underreaction

### What to cover

- Momentum: Jegadeesh & Titman (1993, 2001), industry momentum, time-series momentum, crashes (Daniel & Moskowitz 2016), crowding (Lou & Polk "comomentum").
- PEAD: Bernard & Thomas; attention via busy days (Hirshleifer, Lim & Teoh 2009) and Fridays (DellaVigna & Pollet 2009).
- Economic links (Cohen & Frazzini 2008), contrast effects (Hartzmark & Shue 2018), lazy prices (Cohen, Malloy & Nguyen 2020), no news is news (Giglio & Shue 2014).
- Intangibles: employee satisfaction (Edmans 2011), customer satisfaction, brands, R&D efficiency (Cohen, Diether & Malloy; Hirshleifer, Hsu & Li).
- CEO signals: casting calls, opportunistic insider trades (Cohen, Malloy & Pomorski 2012), jets, mansions, narcissism.

### Methods to teach

1. **Testing the mechanism through cross-sectional heterogeneity** (Edmans's "Level 2 thinking"). This is the single most transferable research skill. The template: *"If the anomaly comes from mechanism M, it should be stronger where M is stronger."* Implement it as a split-sample test or an **interaction term** (`signal × low_attention`). Examples:
   - inattention → Friday announcements, busy days, small firms, low analyst coverage;
   - slow diffusion → no common fund owner (Cohen & Frazzini);
   - bad news travels slowly → stronger among losers (Hong, Lim & Stein).
2. **Fama–MacBeth cross-sectional regressions.** These are the alternative to portfolio sorts when you want to control for many characteristics at once. Each month, regress returns on characteristics, then average the coefficients over time and compute a t-stat on the averages. Explain when to use sorts and when to use FM.
3. **Constructing a surprise measure.** SUE (standardized unexpected earnings), meaning actual minus consensus scaled by price or a standard deviation. Students should see that the definition of "news" is a research choice.
4. **Text and alternative data as signals.**
   - Lazy prices: cosine similarity between this year's 10-K and last year's.
   - Glassdoor and NLP culture scores (Sparkline).
   - Satellite car counts (Kang et al.).
   - LLM headline classification (Lopez-Lira & Tang).

   Teach the pipeline: raw text → a number per firm-period → sort or regress. Also teach the look-ahead traps, such as filing dates vs. fiscal year ends.
5. **Strategy evaluation beyond alpha.** Sharpe ratio, drawdowns, crash risk, and conditional/volatility-managed strategies (Daniel & Moskowitz raise the Sharpe ratio from 0.7 to 1.2). Teach turnover and transaction costs as the "is it implementable?" question.

---

## Lecture 6: Mispricing ("Misreaction") and Limits to Arbitrage

### What to cover

- Law-of-one-price violations: 3Com/Palm (Lamont & Thaler 2003), Royal Dutch/Shell (De Jong et al.), on- vs. off-the-run Treasuries, BB+ vs. BBB− bonds, the kimchi premium (Makarov & Schoar), closed-end fund discounts (Lee, Shleifer & Thaler; Bradley et al. activism).
- The big market delusion (Cornell & Damodaran); skewness and Bessembinder (2018).
- Wrong anchors: 52-week high (George & Hwang 2004), round numbers (Bhattacharya et al.), lottery stocks (Bali, Cakici & Whitelaw; Kumar), nominal prices (Shue & Townsend).
- Dividends: the free-dividends fallacy, the dividend month premium, predictable reinvestment flows (Hartzmark & Solomon).
- Why these persist: short-sale constraints, noise-trader risk, funding liquidity (LTCM).

### Methods to teach

1. **Computing an arbitrage spread.** The stub value (3Com = 1.525 × Palm + cash + core business), the twin-share price ratio, and the NAV discount. These are pure arithmetic, so they're great for exams. The research question is then *why doesn't the spread close?*, which points to short-sale constraints, borrowing costs and holding-period risk.
2. **Horse-race regressions.** George & Hwang put the 52-week-high signal and past returns in the same regression, and the 52-week high "wins". Teach how to decide which of two correlated explanations dominates, and the limits of that inference.
3. **Threshold and bunching tests.** Examples:
   - firms bunching just above 50% sales in the glamorous segment (Chen, Cohen & Lou);
   - order imbalances around round numbers;
   - the investment-grade cliff at BBB−.

   Students learn to plot a histogram around a cutoff and ask "is there too much mass just above?". This is the intuition behind regression discontinuity and density (McCrary) tests.
4. **Arithmetic vs. geometric returns, and mean vs. median.** Volatility drag and skewness. Have students **bootstrap random single-stock and 5-stock portfolios** to show that the median stock underperforms T-bills.
5. **Backtest hygiene** (summary of the whole course):
   - look-ahead bias (using information not yet public, such as `shift()` errors in pandas);
   - survivorship bias (delisted stocks dropped);
   - data snooping;
   - microcap dominance;
   - stale prices / non-synchronous trading;
   - ignoring transaction costs and short-sale costs.

---

## How to Think Like a Researcher: A Framework to Give Students

Teach this as a one-page recipe in Lecture 3, and reuse it for every paper in Lectures 4–6 and for the group project.

1. **Puzzle.** What pattern contradicts the efficient-markets benchmark? State it as a number (e.g., "losers beat winners by 25% over 3 years").
2. **Mechanism.** Which bias or friction could cause it? Overextrapolation, inattention, anchoring, limits to arbitrage, agency.
3. **Main prediction.** What return pattern should the mechanism produce?
4. **"Level 2" prediction.** Where should the effect be stronger or weaker if the mechanism is right? This is the test that convinces referees.
5. **Data and measurement.** What is the signal, when is it publicly known, and what is the return window?
6. **Baseline test.** Portfolio sort, event study, or regression.
7. **Kill the risk story.** Use the tests in the Lecture 3 checklist.
8. **Kill the other alternatives.** Reverse causality, omitted variables, homophily, data mining. Use placebos and pre-trends.
9. **Robustness and out of sample.** Other periods, other countries, other assets. The book's recurring "it works in 7 centuries / 40 countries / baseball cards" pattern.
10. **Economic significance and implementability.** Magnitude after costs and in large stocks, plus capacity.

**Habits to drill:**

- **"What would have to be true?"** Before running anything, write down what the data must show for each competing story.
- **Kill your own result.** Edmans's own story: referees made him run the earnings-surprise test on the Best Companies.
- **Ask the five referee questions of every result:** Is it risk? Is it data mining? Is it driven by microcaps? Does it survive transaction costs? Is there look-ahead bias?
- **Reading papers:** start from the abstract, then the main table, then the identification section. Teach a 5-line summary template: *question, data, method, main result (with magnitude), main threat.*

---

## Practical Skills to Test on the Midterm

These can all be done with a calculator and no computer. Each is linked to a paper students will have seen.

### A. Reading tables and output

1. **Interpret a regression table.** Give a real table (e.g., football, Hartzmark & Shue contrast effects, or Cohen–Lou–Malloy "casting"). Ask:
   - (a) the sign and meaning of the key coefficient;
   - (b) whether it is significant at 5% (compute t = coef / SE);
   - (c) the economic magnitude of a 1-SD change;
   - (d) what the fixed effects absorb;
   - (e) why the standard errors are clustered by date.
2. **Interpret factor regressions across models.** A strategy's alpha under CAPM, FF3 and FF5, with loadings. Ask: what kind of strategy is this, judging from the loadings? Does the anomaly survive? What does a falling alpha tell you?
3. **Interpret an event-time plot.** A PEAD-style CAR figure: where is the immediate reaction, where is the drift, and what would an efficient market look like?

### B. Calculations

4. **Event study by hand.** Give 5 days of stock and market returns, plus α and β from an estimation window. Compute daily ARs and the CAR, then test significance given a standard deviation.
5. **CAR vs. BHAR.** Compute both over 3 periods and explain the difference.
6. **Portfolio sort.** Give 10 stocks with a signal and next-month returns. Form quintiles, compute the long-short return, then redo it value-weighted and explain the difference.
7. **Odean's PGR and PLR.** Give counts of realised and paper gains and losses, compute both, and test the disposition effect.
8. **Law-of-one-price arithmetic.** Compute 3Com's implied stub value, or the return from buying a closed-end fund at a 15% discount if it open-ends.
9. **Volatility drag.** Compare the arithmetic and geometric average for two return streams (Edmans's Stock A vs. Stock B).
10. **Multiple testing.** "You test 200 signals at 5% and find 12 significant. How many would you expect by chance? What t-stat threshold would you use?"

### C. Research design (the questions that separate A students)

11. **Risk vs. mispricing.** "Strategy X earns 6% a year in alpha. Propose two tests that distinguish risk compensation from mispricing, and say what result supports each story." Expected answer: earnings-announcement returns, analyst forecast errors, bad-state performance, reversal, post-publication decay.
12. **Mechanism prediction.** "A paper argues anomaly Y is caused by investor inattention. Name two subsamples where Y should be stronger and explain why." (Fridays, busy days, small or low-coverage firms, no common owners.)
13. **Spot the identification problem.** "People whose neighbours hold tech stocks are more likely to buy tech stocks, so neighbours influence each other." Name the confound (homophily or shared local information) and propose a design that fixes it (movers with pre-trends, distant friends, random assignment).
14. **Critique a backtest.** Give a short description or a 10-line pandas snippet with a planted flaw. Students must find it: no `.shift(1)` on the signal (look-ahead), only currently listed stocks (survivorship), an equal-weighted microcap universe, or no transaction costs.
15. **Exogenous shock design.** "Propose a mood shock other than sports or weather that could test whether sentiment moves prices. Why is it plausibly unrelated to fundamentals? What is the main threat?"
16. **Mini research proposal (short answer).** Give a vignette from the book with no paper attached (e.g., the Turkish hazelnut frost, or AGM venue changes). Students write: question → mechanism → testable prediction → data → test → one alternative explanation and how to rule it out.

### D. Optional take-home or assignment version (Python)

- Replicate a small event study (earnings announcements of 20 firms) with the market model.
- Build a momentum or reversal sort on the Fama–French data already in `lecture05/data`, then regress the long-short returns on FF factors.
- Run a "Level 2" split: momentum in small vs. large stocks.
- Bootstrap the median single-stock vs. index return (Bessembinder).
