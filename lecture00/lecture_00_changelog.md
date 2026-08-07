# Changelog — lecture_00.qmd

记录对 `lecture_00.qmd` 的每次修改:改动位置、修改前 → 修改后、修改原因。

---

## 1. Section 4.1 (`#sec-capm`) — beta interpretation

**Before:**
> β = 1.3 means the stock tends to move 1.3% when the market moves 1%.

**After:**
> β = 1.3 means that when the market's return is 1% higher, the stock's return is, on average, 1.3% higher (or lower, if β is negative).

**Reason:** To make the direction of the relationship explicit. The original phrasing ("tends to move X% when the market moves Y%") is ambiguous about direction — it doesn't clarify that beta describes the sign of the co-movement, not just its magnitude. The revised wording states explicitly that a higher market return is associated with a higher (or lower, for negative beta) stock return, and adds "on average" to flag that this is an expected relationship, not a deterministic one.

---

## 2. Section 5.2 (`#sec-controls`) — multiple regression coefficient interpretation

**Added (after "...after removing what the other variables already explain."):**
> This is the single most important difference from simple regression: a coefficient in a multiple regression is never just "the relationship between xₖ and y," it is that relationship net of everything else in the model. Add or drop a variable and the remaining coefficients generally change.

**Reason:** To make explicit and stress a point that was previously only implicit in "holding the other variables fixed" — that a multiple-regression coefficient's meaning is conditional on which other variables are in the model, and that this is the key conceptual departure from simple regression. Stating it directly, rather than leaving it to be inferred, reduces the risk that students read $\beta_k$ as a fixed, model-independent quantity.

**Transition sentence revised for flow:**

**Before:**
> This is exactly what the Γ′Controls term did in the Lecture 3 StockTwits regression:

**After:**
> The Lecture 3 StockTwits regression is this idea in practice. Without the Γ′Controls term, β would pick up not just retail attention but everything that moves with it:

**Reason:** To make explicit and stress a point that was previously only implicit in "holding the other variables fixed" — that a multiple-regression coefficient's meaning is conditional on which other variables are in the model, and that this is the key conceptual departure from simple regression. Stating it directly, rather than leaving it to be inferred, reduces the risk that students read $\beta_k$ as a fixed, model-independent quantity.

**Transition sentence revised for flow:**

**Before:**
> This is exactly what the Γ′Controls term did in the Lecture 3 StockTwits regression:

**After:**
> The Lecture 3 StockTwits regression is this idea in practice. Without the Γ′Controls term, β would pick up not just retail attention but everything that moves with it:

**Reason:** After inserting the new sentence above, the paragraph had two sentences in a row both opening with "This is...", which read as repetitive. The transition sentence was rewritten to connect the new content to the StockTwits example while removing the repeated construction, and to more directly set up *why* the controls matter (β would otherwise absorb confounding effects) before the reader sees the equation.

---

## 3. Section 8 (`#sec-testing`) — H₀/H₁ bullet list: test statistic and decision rule

**Before:**
> We compute a statistic (a t-stat), ask how likely it is under H₀ (the p-value), and reject H₀ if that's small enough.

**After (split into two bullets):**
> The test statistic. t = (β̂ − β₀) / SE(β̂). It measures how many standard errors the estimate sits away from the null value.
>
> The decision. The p-value is the probability, if H₀ were true, of drawing a sample whose t-statistic is at least this far from zero. Reject H₀ when that probability falls below the significance level α you fixed in advance.

**Reason:** To make the previously compressed one-line summary clearer. The original bullet packed the definition of the t-statistic, the definition of the p-value, and the decision rule into a single sentence, which left the mechanics vague (what exactly is being measured, what "small enough" means). Splitting it into two parallel bullets — one defining the test statistic explicitly with its formula, one defining the p-value and stating the decision rule in terms of α — matches the structure of the $H_0$/$H_1$ bullets above and gives each concept room to be stated precisely.

---

## 4. Section 8 (`#sec-testing`) — two-sided vs. one-sided example

**Before:**
> "Is β ≠ 0?" is two-sided (the usual default). "Is β > 0?" is one-sided — appropriate only when theory rules out the other direction beforehand.

**After:**
> "Is β ≠ 0?" is two-sided (the usual default). "Is β > 0 (or β < 0)?" is one-sided — appropriate only when theory rules out the other direction beforehand.

**Reason:** To clarify that a one-sided test is not restricted to the ">0" direction. The original example only showed "β > 0," which could leave the impression that one-sided tests always test for a positive effect. Adding "(or β < 0)" makes clear that the direction is set by the researcher's theory beforehand and could equally be tested as β < 0.

---

## 5. Section 8 (`#sec-testing`) — significance level α, rewritten as three bold-lead-in bullets

**Before:**
> The 5% significance level *is* your tolerated Type I error rate: even when there is truly no effect, you'll wrongly "find" one 5% of the time. That fact is harmless for one test — and quietly catastrophic when a whole literature runs thousands of them (Section 10). A quick simulation makes the 5% concrete:

**After (three bullets):**
> **Why we need a threshold.** Even when β is truly zero, sampling noise means β̂ almost never comes out exactly zero. So the question is never "is the estimate nonzero" but "is it far enough from zero to count as evidence." The significance level α is where you draw that line.
>
> **What the level means.** α is a conditional probability: given that H₀ is true, it is the probability that the test rejects it. Setting α = 0.05 says that among many independent samples drawn under H₀, the rule would reject in 5% of them. The condition is what makes the number meaningful, and it is also what makes it easy to misread. α is not the probability that H₀ is true, and it is not the probability that this particular rejection is a mistake.
>
> **Seeing it happen.** The claim above is about repeated sampling, which you never observe in practice but can simulate. Below, H₀ is true by construction: x and y are generated independently, so β is zero. We draw 2,000 independent samples, run the regression on each, and count how often the test rejects at α = 0.05.

**Reason:** To build the significance-level concept in a coherent sequence — why a threshold is needed at all, what α precisely means as a conditional probability (and what it does *not* mean, addressing the P(reject | H₀ true) vs. P(H₀ true | rejected) confusion directly), and then bridge into the simulation that follows. The bold-lead-in, short-paragraph format matches the style already used elsewhere in this section (e.g. "Two ways to be wrong").

**Note:** the original sentence also carried a forward pointer to Section 10 ("quietly catastrophic when a whole literature runs thousands of them") — the multiple-testing motivation. The new version drops that pointer. Flagging in case you want it preserved somewhere (e.g. added to the end of the "Seeing it happen" bullet, or left for Section 10 to pick up on its own).

---

## 6. Structural move — "The logic of hypothesis testing" relocated

**Before:** `# The logic of hypothesis testing {#sec-testing}` sat after `# R² and why a small R² is normal {#sec-r2}` (i.e. after the Standard errors / t-stat / p-value / CI section and the R² section).

**After:** The entire section (unchanged content) now sits immediately after `# Interpreting coefficients {#sec-coefficients}` and before `# Standard errors, t-values, p-values, confidence intervals {#sec-inference}`.

New top-level order: 1 Motivation → 2 Data → 3 Moments → 4 OLS → 5 Interpreting coefficients → **6 The logic of hypothesis testing** → 7 Standard errors/t-values/p-values/CI → 8 R² → 9 Real regression table → 10 Pitfalls → 11 End-to-end example → 12 Cheat sheet.

**Reason:** It is more natural to introduce the hypothesis-testing framework (H₀, H₁, test statistic, decision rule) before the mechanics of the t-statistic and p-value, rather than after. All cross-references in the document use Quarto's `@sec-xxx` label syntax, which renumbers automatically, so no other section numbers needed manual edits.

---

## 7. Coherence fixes after the move (Section 5 → 6 transition, Section 6 opening line)

**Before (end of Section 5, "Interpreting coefficients"):**
> Whether that January coefficient is *real* or just noise is the job of the t-stat and p-value — which is the next section.

**After:**
> Whether that January coefficient is *real* or just noise is a question of hypothesis testing — the framework covered next, which the t-stat and p-value (the following section) make precise.

**Before (opening line of Section 6, "The logic of hypothesis testing"):**
> Everything above is really one framework: hypothesis testing.

**After:**
> This section sets up the framework that the t-statistic, p-value, and R² sections ahead will make precise: hypothesis testing.

**Reason:** Both sentences were written when hypothesis testing came *after* the t-stat/p-value/R² material and referred back to it ("the next section" pointing to t-stat/p-value; "everything above" summarizing t-stat/p-value/R²). After the move, hypothesis testing now comes *before* that material, so both sentences pointed the wrong direction. Rewritten to point forward instead: Section 5's closing line now names hypothesis testing (not t-stat/p-value) as what comes next, and Section 6's opening line frames itself as the setup that later sections will make precise, rather than a recap of content not yet introduced.

---

## 8. Section (`#sec-t-p`) — t-statistic half rewritten

**Before:**
> The **t-statistic** rescales the estimate by its own precision:
>
> t = β̂ / SE(β̂)
>
> It answers: *how many standard errors is the estimate away from zero?* The rule of thumb everyone uses:
>
> |t| > 1.96 ⇒ significant at the **5%** level. |t| > 1.65 ⇒ 10%, |t| > 2.58 ⇒ 1%. (These come from the normal distribution; for the small samples finance rarely has, they're slightly larger.)

**After:**
> A t-statistic is always a test of a specific null. Write H₀ as β = β₀. The statistic is
>
> t = (β̂ − β₀) / SE(β̂)
>
> which asks: how many standard errors does the estimate sit away from the value H₀ claims? If H₀ is true, β̂ should land near β₀, and t should be near zero. A large |t| is exactly what "the data look unlikely under H₀" means in numbers.
>
> Software defaults to β₀ = 0, so the reported t collapses to β̂ / SE(β̂). That is a choice of null, not a definition of t. In the Section 4.3 CAPM regression the interesting question is whether β = 1, and answering it means computing (β̂ − 1) / SE(β̂) yourself.
>
> In practice people read t against fixed cutoffs:
>
> |t| > 1.96 ⇒ significant at the **5%** level. |t| > 1.65 ⇒ 10%, |t| > 2.58 ⇒ 1%. These are two-sided critical values: 1.96 cuts off 5% of the normal distribution, split between the two tails. They are accurate once df exceeds about 100. Below that, use the t-distribution, where the cutoffs are somewhat larger.

**Reason (per user):** Rewrite the t-statistic half of the section to make clear that a t-statistic is always defined relative to a specific null ($\beta_0$), not just $\beta = 0$ by default — using the general form $t = (\hat\beta - \beta_0)/SE(\hat\beta)$ and pointing to the CAPM $\beta = 1$ case as a concrete example where $\beta_0 \ne 0$. Also folds in the previously agreed "two-sided critical values" clarification directly into the cutoffs callout, replacing the vaguer "(these come from the normal distribution...)" parenthetical.

**Implementation note:** the CAPM example is referenced via `@sec-read-summary` (Quarto crossref) rather than a hardcoded "Section 4.3," consistent with how every other section reference in the document is written.

---

## 9. Section (`#sec-ci`) — Confidence intervals rewritten

**Before:**
> A **95% confidence interval** is the range of plausible values for the true coefficient: roughly β̂ ± 1.96 × SE. If it excludes zero, the coefficient is significant at 5% — the same verdict as the t-stat, but it also shows you the *magnitude* uncertainty. Here it is for our CAPM:
>
> [code block for ci table]

**After:**
> A **95% confidence interval** is β̂ ± 1.96 × SE(β̂), where 1.96 is the two-sided critical value from Section 6.2 (1.65 for a 90% interval, 2.58 for a 99% one). The 95% describes the *procedure*, not this particular interval: if you repeated the study on many independent samples and built an interval each time, 95% of those intervals would contain the true β. The one in front of you either contains it or does not, and you cannot tell which.
>
> Here it is for our CAPM:
>
> [code block for ci table, unchanged]
>
> Read the MKT row two ways. The interval excludes zero, which is the same verdict as t = 11.48 and p ≈ 0. But it also excludes 1, which the reported t and p cannot tell you: they are computed against β₀ = 0. Apple moved more than one-for-one with the market over this sample, and the interval rules out one-for-one at the 5% level.

**Reason (per user):** Gives the CI section a distinct purpose rather than restating the t-stat's zero-vs-nonzero verdict. The rewrite (1) gives the correct repeated-sampling interpretation of "95%" instead of the loose "range of plausible values," (2) explicitly ties the 1.96 critical value back to the two-sided cutoffs established when the t-statistic was introduced, and (3) adds a worked reading of the MKT row showing that the CI can answer a question — is β = 1? — that the default-null t and p (computed against β₀ = 0) cannot, directly following up on the β₀ generalization made in the t-statistic rewrite above.

**Implementation note:** "Section 6.2" is written via `@sec-t-p` (Quarto crossref), consistent with the rest of the document.

---

## 10. Section (`#sec-robust`) — Robust/clustered/Newey-West SE rewritten; figure code externalized

**Before:** Short paragraph + 3-bullet list (em-dash style) + code comparing plain OLS vs. Newey-West t-stats.

**After:** Rewritten with:
- Two intro paragraphs explaining which assumptions in the @sec-se formula fail, and that the correction changes the SE/t-stat but never β̂ (unbiasedness preserved).
- A new figure (residual covariance-matrix panels for Plain OLS / White-HC / Newey-West / Clustered), inserted via an external script (see below).
- The three-bullet list rewritten without em dashes ("frees the diagonal...", "adds a band around the diagonal...", "frees whole blocks...") to match the covariance-matrix figure's language.
- A new **"Why the correction can be large"** paragraph with a worked panel-data example (500 firms × 120 months) and an overlapping-window example, explaining *why* corrected t-stats can differ substantially from plain OLS.
- The closing code comparison and last line are unchanged.

**Reason (per user):** Ties the three correction names to a visual (which covariance-matrix cells each one frees up), replaces the vague "you don't need the theory yet" framing with a concrete account of *why* the plain SE formula breaks (clustering / overlapping windows shrink effective sample size), and grounds "the correction can be large" with actual numbers instead of leaving it asserted.

**Figure code externalized:** Per the user's request, the plotting code for the new figure is **not** inlined in `lecture_00.qmd`. It now lives in `scripts/se_correction_panels.py`, and the qmd chunk pulls it in via Quarto's `file` chunk option:

```{{python}}
#| echo: false
#| fig-cap: "What each correction allows the residuals to do."
#| file: scripts/se_correction_panels.py
```

This is the Quarto-native way to source an external code file into a chunk (the file's contents execute exactly as if written inline). `scripts/se_correction_panels.py` was created alongside `lecture_00.qmd` — it will need to sit at that relative path (`scripts/` next to the `.qmd`) for the render to find it; update the `file:` path if you place it elsewhere.

---

## 3. Section 8 (`#sec-testing`) — H₀/H₁ bullet list: test statistic and decision rule

**Before:**
> We compute a statistic (a t-stat), ask how likely it is under H₀ (the p-value), and reject H₀ if that's small enough.

**After (split into two bullets):**
> The test statistic. t = (β̂ − β₀) / SE(β̂). It measures how many standard errors the estimate sits away from the null value.
>
> The decision. The p-value is the probability, if H₀ were true, of drawing a sample whose t-statistic is at least this far from zero. Reject H₀ when that probability falls below the significance level α you fixed in advance.

**Reason:** To make the previously compressed one-line summary clearer. The original bullet packed the definition of the t-statistic, the definition of the p-value, and the decision rule into a single sentence, which left the mechanics vague (what exactly is being measured, what "small enough" means). Splitting it into two parallel bullets — one defining the test statistic explicitly with its formula, one defining the p-value and stating the decision rule in terms of α — matches the structure of the $H_0$/$H_1$ bullets above and gives each concept room to be stated precisely.

---

## 4. Section 8 (`#sec-testing`) — two-sided vs one-sided example

**Before:**
> "Is β ≠ 0?" is two-sided (the usual default). "Is β > 0?" is one-sided — appropriate only when theory rules out the other direction beforehand.

**After:**
> "Is β ≠ 0?" is two-sided (the usual default). "Is β > 0 (or β < 0)?" is one-sided — appropriate only when theory rules out the other direction beforehand.

**Reason:** The original example only illustrated one-sided testing with $\beta > 0$, which could leave the impression that one-sided tests always point in the positive direction. Adding "(or $\beta < 0$)" makes clear that a one-sided test can be framed in either direction, depending on what theory predicts.

---

## What's working well

A few things worth calling out about the document as it stands, separate from the individual edits above:

- **Structure.** The overall organization — motivation, data, moments, OLS mechanics, coefficient interpretation, hypothesis testing, inference, R², reading a real table, pitfalls, end-to-end example, cheat sheet — builds in a logical order, and each section sets up what the next one needs.
- **One example carried throughout.** The CAPM regression on Apple returns runs from the OLS mechanics section all the way through coefficient interpretation, the t-stat/p-value walkthrough, and confidence intervals. Coming back to the same numbers ($\hat\beta$, $t = 11.48$, etc.) at each stage makes the notes feel complete rather than a series of disconnected examples.
- **Finance grounding, not just statistics.** Beyond the statistical mechanics, the notes consistently tie each concept back to a finance application — CAPM beta, the Fama-French three-factor model, the StockTwits/BHAR study, panel clustering by firm — so the statistical ideas land as tools for reading finance research rather than abstract math.
