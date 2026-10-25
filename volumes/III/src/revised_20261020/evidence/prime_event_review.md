# Prime event review and chapter draft

## Review findings for integration

The full ten-page attached paper was read from Library extraction, including all tables, equations, numerical traceability, and qualifications. Its title is **Reliability and resource tradeoffs in hidden-spin feedback for prime-sequence computation**, Sean Brady, dated 27 September 2026. It is not a primality proof and does not establish a relation to FEOP. The older local `prime_event_report2/REPORT.md` has an H001812 cutoff at which the balanced long run was still active. That pending status is superseded by `prime_balance1/REPORT.md`, `ANALYSIS.json`, `COMPARISON.json`, `HOLDOUT_ANALYSIS.json`, and the attached paper. Do not retain the older pending status as the current outcome.

The major result deserves its own chapter: an explicit microscopic failure mechanism led to an algebraically chosen successor, followed by a complete matched billion-index experiment and an unscreened fresh-seed continuation. Preserve the event scheduler, carried hidden state, three-reading dynamics, frozen source, paired profiles, actual resource change, and independent scoring. The source-strength controls and Poisson analysis explain this success quantitatively; they do not erase it.

Bounded transcription checks performed for this review, without executing a scientific campaign: evaluated the displayed elementary coefficient/root formulas; summed the census opportunities; recomputed 569-to-40 reduction and the two fitted Poisson zero-error probabilities. They agree with the attachment. The fresh/source JSON summaries were read directly. No original sources were changed.

One important attachment-extraction issue is resolved: the balance formula requires both nested square roots. The correct expression is `t* = (1/2) arcosh sqrt(C + sqrt(C^2-C))`, C=cosh8. The flat PDF extraction can obscure that nesting.

### Evidence keys

- **PE1** Attached `Prime_Event_PRE_Expanded_Rev3(1).pdf`, Library `libfile_fedd048f461881919e053e75267bcecd`, actual title above; ten pages. Sections II and III give the source and observed experiments; IV gives reanalysis/census; V gives controls; VI and Table VI give traceability.
- **PE2** `/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/GEN4/prime_balance1/REPORT.md`, final matched/fresh report; machine-readable companions `ANALYSIS.json`, `COMPARISON.json`, `HOLDOUT_ANALYSIS.json`, `FINAL_VERIFIED.json`, `SOURCE_CHECK.json`, `QUALIFICATION_CHECK.json`, `HOLDOUT_VERIFIED.json`. `ANALYSIS.json` records 20 errors per matched profile, 47 exact seeds and worst two errors. `COMPARISON.json` has `all_billion_complete: true`. `HOLDOUT_ANALYSIS.json` records 13 exact, two false positives and one false negative per fresh profile.
- **PE3** Same campaign `DERIVATION.md`, `DESIGN.md`, `POD_PLAN.md`, `HOLDOUT_PLAN.md`; source target fixed before successor generation. `SOURCE_CHECK.json` records 1,080 checks over 280 propagators and maximum normalized discrepancy 1.582067810090848e-14 against separately implemented Padé propagation.
- **PE4** `GEN4/prime_event_report2/REPORT.md`, older synthesis with explicit recurrence, hidden-spin elimination, heat-bath dynamics, local cohorts, baseline billion run, local replay and balance derivation. Sources retained under its `sources/` directory include `04_interaction_compiler1_DERIVATION.md`, `06_prime_seed_mechanism1_REPORT.md`, `09_prime_pod1_REPORT.md`, `10_prime_balance1_DERIVATION.md`. Use this for derivations and predecessor results, not as final successor status.
- **PE5** `GEN4/spin_prime_connection1/REPORT.md`, also retained at `GEN4/prime_event_friend_guide1/sources/06_spin_prime_connection1_REPORT.md`. Pinning a retained spin turns four-port even interactions into the odd gate coefficient; six compiled microscopic gates measured, no new closed-loop prime trajectories.
- **PE6** `GEN4/prime_sam_dynamics1/REPORT.md`, also retained at `GEN4/prime_event_friend_guide1/sources/04_prime_sam_dynamics1_REPORT.md`. Exact projection and memory-kernel analysis on the actual balanced 128-state gate, separate from frozen production runs.

All abbreviated `GEN4/` paths above are relative to `/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/`. No new stochastic trajectories, deterministic censuses, source-control campaigns or matrix-exponential experiments were run during this review. PE1 reports the new analysis package's existence and internal filenames, but those files were not obtained in this review. Consequently the post hoc control and census values below are attributed to the attached manuscript rather than described as independently regenerated here.

---

# Prime event computation and microscopic reliability

The prime-event program constructed a seven-spin stochastic decision gate inside an event-created sieve and improved its reliability by changing specified microscopic interactions. The original gate produced an exact prime/composite decision sequence through one billion for one of 64 seeds per accumulation profile. A successor selected from the source algebra before its trajectories were generated produced exact sequences for 47 of the same 64 seeds per profile. With that source then frozen, 13 of 16 fresh seeds also produced exact sequences through one billion. The matched total fell from 569 to 40 errors across the two paired profiles, a 92.9701 percent reduction. These are completed experiments with retained source, trajectory, scoring and archive records. [PE1, Sections II–III; PE2]

The chapter follows the construction that made this improvement intelligible. An accepted event writes future return channels. Two banks turn the channel history into gate inputs. Six hidden spins provide controllable pair and triple terms for an output spin. Full finite-state dynamics carries the hidden configuration from one reading to the next. Local replay identified the input sector responsible for the baseline's first composite errors; elimination of the hidden spins explained that sector; a balance equation selected the revised couplings. The resulting observations can then be compared with numerical survival calculations and stated resource budgets.

## The event created sieve

A candidate is an integer n, processed sequentially from 2 to a declared horizon N. A return channel is a stored period established by an earlier accepted candidate. If p is accepted, its channel returns at 2p, 3p and subsequent positive multiples within the horizon. Channels enter two banks alternately in creation order, beginning with bank 0. A bank reports whether at least one of its channels returns at the current candidate. A logical input r_i equals +1 when bank i returns and -1 otherwise.

The ideal decision accepts exactly when neither bank returns. This recurrence generates the primes by induction. Initially 2 is accepted. If all accepted candidates below n are precisely the earlier primes, then a prime n has no earlier prime divisor and receives no return. A composite n has an earlier prime divisor, whose installed channel returns at n. Thus the ideal rule accepts every prime and rejects every composite. The arithmetic resides in integer periods and their future multiples; the seven-spin system implements the decision from the two bank inputs. An independent sieve supplies reference labels for scoring the generated sequence. [PE1, Section IIA; PE4, Section 3]

A stochastic decision changes the history. A falsely accepted composite installs its own channel, and an omitted prime fails to install one. Either changes the parity of the number of accepted events and can therefore alter the bank assignment of later channels. Hidden microscopic state also carries between candidates. An exact trajectory means no incorrect acceptance or rejection anywhere through N, not merely a final event count that happens to match. At N=10^9, an exact trajectory emits all 50,847,534 primes and no composites.

## The microscopic gate and its effective margins

The gate has an output spin e and six hidden spins h_j, each taking values -1 or +1. The two bank inputs are clamped during a candidate. An accepting reading has e=-1. The source is specified at dimensionless inverse temperature beta=1 by pair couplings to the hidden spins and explicit hidden fields. Let x=(e,r_1,r_2). Its energy is

$$E(e,h\mid r_1,r_2)=-\sum_{j=1}^{6}h_j[(Wx)_j+\eta_j].$$

Two hidden spins form pair modules of strength u, with rows (u,u,0) and (u,0,u). Four more form a triple module of strength t, with rows (-t,-t,t), (-t,t,-t), (t,-t,-t), (t,t,t). The hidden fields are eta=(0,0,t,t,t,t). Every microscopic interaction is a pair interaction or a declared one-spin field. The effective three-spin term appears after the hidden variables are summed. [PE1, Section IIB; PE4, Sections 4–5]

Because the hidden spins are conditionally independent at fixed e and inputs, their partition factors multiply. The conditional free energy is therefore

$$F(e\mid r_1,r_2)=-\sum_j\log\{2\cosh[(Wx)_j+\eta_j]\}=C(r_1,r_2)+eH(r_1,r_2),$$

where C contains terms independent of the output. The output field and its two coefficients are

$$H=-a(r_1+r_2)+br_1r_2,\qquad a(u)=\tfrac12\log\cosh(2u),$$

$$b(t)=\tfrac12\log\!\left[\frac{\cosh(2t)^4}{\cosh(4t)}\right].$$

The equilibrium probability of an accepting output is 1/(1+exp(-2H)). With no returns, H=2a+b and the gate favors acceptance. With one returning bank, the two pair contributions cancel and H=-b. With both banks returning, H=b-2a. The positive magnitudes b and 2a-b are the two composite-blocking margins. They identify how strongly the source favors rejection in the two composite input sectors.

For the baseline u=4 and t=2, the coefficients are a=3.653426466 and b=2.960949986. The one-bank margin is 2.960949986; the two-bank margin is 4.345902946. The baseline consequently gives substantially weaker static protection to the one-bank sector. This is a source calculation, not an explanation inferred only from aggregate error counts.

## Carrying microscopic state through the decision

The experiment retains all 2^7=128 free-spin configurations. A heat-bath generator Q_0 assigns a transition rate 1/(1+exp[E(z)-E(s)]) when z differs from s by one spin flip, with diagonal entries chosen so each generator column sums to zero. The attempt-rate multiplier is Gamma=512. A candidate's total exposure tau_k is split among r confirming readings, giving the transition matrix T=exp(Q_0 Gamma tau_k/r). Original production uses r=3.

Every reading samples the complete microscopic state. Its output must equal -1, and all three readings must accept before the candidate is emitted. If D projects onto states with e=-1 and v_s is the incoming state vector, the acceptance probability is

$$p_{\rm accept}(s)=\mathbf1^{T}(DT)^r v_s.$$

The final sampled state initializes the next candidate whether the candidate was accepted or rejected. All prescribed random readings are consumed even after an earlier reading rejects. This preserves both state history and random-stream alignment. Cubing the equilibrium acceptance probability would discard finite relaxation and correlations between readings; it is not the production calculation. [PE1, Section IIC]

Two accumulation profiles use a common 35-phase duration sequence. The uniform profile has accumulation 1/4, and the rough profile varies its accumulation over the phases. Exposure is proportional to duration times the square root of one minus accumulation, with normalization matching total exposure per cycle. These are supplied dimensionless cadence profiles. Each seed uses shared random streams across profiles, so the profiles are paired observations of that seed.

## Replay located a correctable microscopic weakness

Baseline seed 1000063 was exact through one billion under both profiles. The mechanism study compared each other seed's first incorrect decision with that seed at the same candidate. Because neither path had yet erred, the return histories and bank inputs were identical. Across 126 local comparisons, replacing the failing seed's three draws with the successful seed's draws corrected all 126 decisions while retaining the failing incoming state. Replacing the incoming state while keeping the failing draws left all 126 decisions incorrect. In 32 comparisons the incoming states already matched. The realized random triple was the local discriminator in these comparisons. [PE1, Section IIIA; PE4, Section 9]

Of those first errors, 120 were composite emissions and six were missed primes. Every first composite emission had exactly one bank returning. This links the replay directly to the source field: the pair terms cancel in precisely that sector, leaving b as the blocking margin. The replay covered 230 saved chunks, 1.15 billion decisions and 264 local windows, checking replayed event bits and checksums. It resolved the local first-error mechanisms; it did not generate entire altered futures after each hypothetical intervention.

One missed-prime example makes the meaning of microscopic replay explicit. At prime 3,510,937, the failing seed and successful seed both enter state 103. The failing readings are 56,56,101; the successful readings are 56,56,56. The third failing draw lies in state 101's narrow rejecting interval, about 3.77×10^-11 wide. This is an identified numerical event in a retained dynamics, rather than an unexplained exception assigned to a special seed property.

## The algebraically chosen successor

At fixed a>0, the smaller of the two blocking margins obeys min(b,2a-b)<=a, with equality precisely when b=a. The successor therefore kept the pair-module strength u=4 and raised the four triple rows and their hidden fields together until b(t)=a. This choice was fixed before successor trajectories were examined.

Let C=cosh8 and z=cosh(2t)^2. The balance equation becomes z^2=C(2z-1). Its physical positive-strength root gives

$$t_* =\tfrac12\operatorname{arcosh}\sqrt{C+\sqrt{C^2-C}}=2.3464897298984759\ldots.$$

The resulting a=b=3.6534264659876117 in the archived binary64 source output. Pair strength, temperature, cadence, three-reading rule, scheduler and matched random streams remain fixed. The triple strength and associated hidden fields increase by 17.32 percent. This establishes a maximum of the weaker static margin at fixed pair coefficient. The subsequent experiment determines the effect on full trajectories. [PE3]

The finite-state calculation shows both sides of the change. The one-bank three-reading false-emission probability falls from about 1.91×10^-8 to about 3.0×10^-10, approximately a factor of 63. The two-bank probability rises from 4.74×10^-12 to about 3.01×10^-10, approximately a factor of 64. The no-return sector also becomes more reliable. Equalizing the blocking margins transfers protection from the stronger composite sector to the weaker one; the frequency of those sectors matters to sequence survival. [PE1, Table I]

## Completed billion index results

All 64 seeds 1000000–1000063 were evaluated under both accumulation profiles using frozen baseline records for the matched comparison. Every successor trajectory completed through one billion. The final observed results are:

| Source and profile | Seeds | Composite emissions | Missed primes | Exact trajectories |
|---|---:|---:|---:|---:|
| Baseline uniform | 64 | 271 | 13 | 1 |
| Baseline rough | 64 | 272 | 13 | 1 |
| Balanced uniform | 64 | 17 | 3 | 47 |
| Balanced rough | 64 | 17 | 3 | 47 |
| Fresh balanced uniform | 16 | 2 | 1 | 13 |
| Fresh balanced rough | 16 | 2 | 1 | 13 |

Per matched profile, 62 seeds improved, one was unchanged, and one worsened. All balanced matched seeds were exact through 10^8; the worst had two errors at 10^9. The complete matched error count fell from 569 to 40 across profiles. Balanced uniform and rough event sequences agreed for every matched seed pair. The profiles remain paired because they share streams; they do not turn 64 seeds into 128 independent seeds. [PE2]

The fresh continuation fixed the successor source and used all 16 seeds 10000000–10000015 with disjoint base and auxiliary random-seed ranges. There was no source retuning or seed screening. Thirteen of 16 were exact through one billion per profile; each of the other three had one error. The errors were composite emissions at 82,866,449 and 203,033,716 and a missed prime at 997,044,317. Fifteen of 16 were exact through 10^8. These fresh streams test the frozen source beyond the matched roster; there is no corresponding fresh baseline ensemble. [PE1, Section IIIC; PE2]

The significance is a completed progression from mechanism to source design to observed improvement. It does not rest on a selected exceptionally long successful seed: the matched roster and fresh roster are reported in full, with per-seed outcomes retained. The experiment measures stochastic sequence reliability in a constructed sieve. Its exact finite realizations do not issue arbitrary-input primality certificates or establish an unbounded guarantee; the prime-event sources do not establish a relation to FEOP.

## How retained history changes a later input

A baseline profile pair exposes a concrete feedback path. Rough seed 1000053 accepts an extra composite at 312,596,611. That changes event-count parity. When prime 483,920,363 is later accepted, its channel enters a different bank than in the uniform partner. At 967,840,726=2×483,920,363, its return meets the period-2 return. The partners now present one-bank and two-bank inputs and make different decisions. The earlier erroneous period does not divide the later candidate; its influence passes through channel creation order and bank assignment. [PE1, Section IIID; PE4, Section 10]

This example establishes a history-mediated change in a later gate input and decision. The average effect of post-error feedback on the ensemble error count is a separate quantity. Zero-error survival ends at the first error, before post-error amplification can occur. That distinction permits a clean survival calculation along the ideal input history without pretending that all later erroneous histories are identical.

## Statistical and state aware explanations of the reliability scale

For a Poisson reference with mean error count lambda, the zero-error probability is exp(-lambda). The baseline uniform mean is 284/64=4.4375, giving 0.011825, compared with observed 1/64=0.015625. The matched balanced mean is 20/64=0.3125, giving 0.731616, compared with 47/64=0.734375. The balanced histogram has 47 zero-error, 14 one-error and three two-error trajectories. Fitted Poisson expectations for these counts are approximately 46.82,14.63 and 2.29. The sample Fano factors, variance divided by mean, are 0.9721 for uniform baseline, 0.9619 for rough baseline and 1.0032 for matched balanced. [PE1, Section IVA and Table III]

These fitted comparisons describe the archived counts. A separate calculation in the attached expanded analysis predicts survival without fitting those counts. Along an error-free history, the ideal sieve determines each input. The microscopic correct-decision operator is A_n=(DT_n)^r for primes and T_n^r-A_n for composites. Starting from the no-return Gibbs vector, the product of these substochastic operators gives the model's zero-error probability: incorrect paths are removed at their first wrong decision.

The analysis does not multiply one billion matrices directly. It calculates the minimum and maximum wrong-decision probabilities over all 128 incoming states for each input and cadence phase, then counts how often each phase/input combination occurs on the ideal history. Every conditional distribution given survival lies within those extrema. Products of their complementary probabilities bound survival without assuming independent successive decisions. Numerical implementation uses logarithms of 1-epsilon, with binary64 propagators.

The ideal-history census contains 50,847,534 no-return candidates, 129,835,417 bank-0-only candidates, 77,222,775 bank-1-only candidates and 742,094,273 both-bank candidates, totaling 999,999,999 decisions. The resulting uniform-profile numerical survival envelopes are [0.0158014,0.0158362] for baseline and [0.717107,0.717210] for balanced. The latter predicts about 45.90 exact cases out of 64 and 11.47 out of 16, compatible with the observed 47 and 13. This is a model-based explanation of the recorded reliability scale. The quoted envelopes cover incoming-state variation in the numerical model; they are not directed-interval certificates of exact real matrix exponentials. [PE1, Section IVB–C and Table IV]

The census also explains the cost of weakening the two-bank margin: both-bank candidates are the largest sector. Their balanced contribution is about 0.224 of total hazard 0.332. A useful trajectory objective therefore weights local error risks by their actual opportunities, rather than maximizing the weakest static margin alone.

## Resource comparisons make the design conclusion precise

Source strength must be defined before alternatives are compared. Summing absolute couplings gives B_J=4u+12t. Including the four hidden fields gives B_Jeta=4u+16t. Baseline budgets are (40,48); balanced budgets are (44.157877,53.543836), increases of 10.39 and 11.55 percent. The 17.32 percent figure refers specifically to t. These are dimensionless source-strength conventions; no device energy consumption was measured.

The attached analysis compares uniform strengthening of the original u:t=2:1 ratio with balancing under these stated budgets. It also tests four or five confirming readings while dividing the same candidate exposure among them. The following are numerical predictions for the uniform profile, separate from the observed matched and fresh ensembles. [PE1, Section V and Table V]

| Control | Confirming readings | Predicted zero error probability through 10^9 |
|---|---:|---:|
| Original baseline | 3 | 0.015801–0.015836 |
| Original balanced | 3 | 0.717107–0.717210 |
| Uniformly scaled baseline matched in coupling budget | 3 | 0.708104–0.708408 |
| Uniformly scaled baseline matched in coupling plus hidden field budget | 3 | 0.769661–0.769936 |
| Uniformly scaled baseline matched in a+b | 3 | 0.592883–0.593218 |
| Balanced source at original coupling plus hidden field budget | 3 | 0.005023–0.005027 |
| Baseline with unchanged total exposure | 4 | 0.773634–0.773842 |
| Baseline with unchanged total exposure | 5 | 0.720757–0.735827 |

Balancing retains a small advantage over uniform strengthening at matched coupling-only budget. Uniform strengthening performs better when hidden fields are counted in the strength budget. Four-reading confirmation is competitive at the original source strengths and unchanged exposure, but changes sampling and measurement costs. Five readings suppress false emissions further while increasing missed-prime opportunities; more confirmation does not monotonically improve the combined fidelity objective.

These comparisons place the observed intervention among explicit design alternatives. The original intervention achieved a large measured improvement with pair strength and cadence fixed. It does not establish balancing as a universal optimum at every resource convention. The controls identify which resources and error opportunities a subsequent optimization must price.

## Connecting exact spin responses to prime gate design

The retained Ising boundary-response work supplies a separate, completed connection. A zero-field four-port free energy contains even pair and four-spin terms. Fixing one port converts the four-spin coefficient into the output/input triple coefficient, while an output-to-pinned-port pair produces an output bias. A declared output field can cancel that bias at a selected temperature. The resulting conditional form is the same pair/triple form used by the prime gate. [PE5]

For the N=1000 positive-fill packet source at beta=4/1000, the retained pinned response gives b/a=0.9070698726632545 after output-bias cancellation. Compiling that ratio into the six-hidden-spin gate at beta=1, with mean pair coefficient fixed to the historical value, gives a worst uniform one-bank three-reading false-emission probability 2.31833×10^-9. The original gate's value is 1.91437×10^-8, an improvement of approximately 8.26 times. The balanced gate remains lower at 3.04423×10^-10. The calculation built six new microscopic designs and evaluated their finite-rate behavior; it did not propagate new closed-loop prime trajectories or simulate the kinetics of the original thousand-spin graph.

The source of the response remains explicit. For the pinned N1000 no-return field, the recorded energy-entropy decomposition is 3.6386520569=4.0074318192-0.3687797623. Degeneracy and thermal entropy therefore contribute to the field transferred into gate design. The connection is available even from the unfrustrated positive-fill packet source; this experiment identifies retained boundary response, rather than frustration alone, as the useful design input. It provides a direct reason to retain the full boundary-resolved spin calculations discussed elsewhere in this volume.

## Hidden memory is a calculable part of the gate

A separate projection analysis applies the retained-history method to the actual balanced 128-state gate. It projects onto the output probability and lifts through conditional hidden-spin Gibbs states. Eliminating the remaining hidden-state component gives a memory convolution plus an initial-memory term. All four input sectors have nonzero sampled kernels, and output-flip rates vary substantially among microscopic states sharing the same output. The output bit alone consequently does not form a closed Markov state. [PE6]

For a switch from both-return equilibrium to no-return input, duration one and uniform accumulation 1/4, the full three-reading acceptance at Gamma=8 is 0.306867084; a two-state Markov projection gives 0.581372959. At Gamma=64 the corresponding values are 0.984884914 and 0.999052329. At the production rate Gamma=512, the largest tested switching discrepancy is 1.82×10^-12. These calculations identify when hidden preparation and memory materially affect reduced predictions, while explaining why a reduced picture can be accurate at the production cadence. They are separate domain probes, not changes installed retrospectively in the archived billion-index ensembles.

## Validation and what the retained records support

The balanced source passed 1,080 source checks including all 280 profile/phase/input transition matrices against a separately implemented direct Padé exponential. After column normalization, the maximum entry discrepancy was 1.5821×10^-14; the initial unnormalized comparison and its column-mass drift are retained. Short-run qualification contributed 64,574 checks, including scalar CDF sampling, independent modulo-based return reconstruction and final-state/count/checksum agreement. [PE2–PE3]

The matched campaign checked all 25,600 chunk hashes and chains and scored all 127,999,999,872 candidate decisions against the independent sieve. It checked 1,572,864 retained microscopic prefix samples against their output decisions. The fresh continuation checked 6,400 chunks, scored 31,999,999,968 decisions and checked 393,216 prefix samples. Together these phases contain 159,999,999,840 scored decisions across paired profiles, a work count rather than a count of distinct integers or independent statistical replications. Whole-sequence scoring is extensive; complete independent replay of every microscopic transition is not claimed.

Native source construction, qualification, matched execution and fresh continuation retain their result, export and checkpoint receipts. The archived source and matched data comprise 26,220 files and 25,821,384,418 bytes; the fresh archive contains 6,535 files and 6,350,494,109 bytes. Final hash receipts record successful T500 custody. A standalone clean replay of baseline seed 1000063 through one billion matches its final microscopic state, event count and checksum while emitting exactly the reference prime sequence. [PE1, Section VI; PE2]

The achieved result is a source-linked reliability method: construct a finite microscopic gate, retain its dynamics and event history, localize a failure, choose a coupling change from the algebra, and measure the complete successor ensemble. The finite successes, local derivations and resource comparisons remain distinct and jointly usable. Their scope is the specified stochastic source, digital recurrence, cadence and observed or numerically analyzed ensembles. Physical gate calibration, an average causal measurement of post-error feedback, and new matched ensembles for the alternative resource designs remain separate tasks.
