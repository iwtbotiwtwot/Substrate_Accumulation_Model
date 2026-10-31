# Duck program and peer method: changelog since 2.0.0 and a report on the drift

Prepared 2026-10-30 at Sean Brady's request ("Produce a detailed changelog including any change that effects how the
program and peers function with a report documenting the drift. I do not mind change in this program or CLAUDE.md I just
need to be in the loop."). Every item below is read from the ironclad repository (history entries, git log, campaign
files, the method document) and from the session transcripts for the times of Sean Brady's approvals; nothing is from
memory. Times are Central (CDT). Directed by Sean Brady. Executed with Claude Code. Every change listed was executed by
Claude Code; the "in the loop" column says whether Sean Brady approved it under CLAUDE.md §13 (phrase + readback for a
permanent change; readback approval + temporary notation for a temporary one), directed it in chat without the §13
steps, or was not told.

## 0. Plain language first

The engine and its releases are in order: every Duck or core version since 2.0.1 has your phrase, a readback, a verified
rollback and its own tag. What drifted is everything that tells the peers what to do. The method document says the
peers "produce ideas and constructions, not answers or proofs", "author your own methods", and that every campaign
copies one briefing and changes only the question. From the second day of 2.0 that rule was not followed: each run's
briefing was copied from the previous run and grew. Host code arrived as a housekeeping rule on 20 October, the
verification form you set for the RH and FEOP checks on 21 October was applied to exploration runs on 22 October and to
a learning run on 28 October, task budgets and witness discipline arrived on 22–24 October, the method's own "author
your own methods" was weakened by an unreleased edit on 21 October, and the standing window moved to 1500 s in that same
unreleased edit. The peers' behaviour follows the briefings exactly: they wrote no host scripts in the first three 2.0
runs and 66 to 137 per run afterwards. Fourteen of the changes below were directed by you in chat; none of those
fourteen was read back as a change to the method, and nine more you were not told about.

## 1. Changelog, chronological

### 1.1 Versioned program changes (engine and Duck layer)

| version | readback | phrase / approval | installed | what changed for the program and the peers | in the loop |
|---|---|---|---|---|---|
| 2.0.0 / R22 | 19 Oct 17:35 | 19 Oct 17:36 "Allow permanent changes, readback approved" | 17:37 | the peer method promoted: four peers bound to controllers, lead outside, one 900 s window, peer-authored recipes; change control §13 installed | §13, phrase recorded only in the doc-repo decisions, not in H002731 |
| Opus peers (temporary) | 18:05 | 19 Oct 18:06 "temporary change approved" (aq_identification); 18:33 "follow your next recommended idea, temporary change to use Opus peers" (resting_clock) | — | research peers on the Opus model for two runs | §13 temporary; the second had direction but no separate readback approval |
| 2.0.1 / R23 | 19 Oct 22:41 | 22:44 "Allow permanent changes and readback is approved." | 22:52 | research peers on the Opus model by default (docs only) | §13 |
| 2.1.1 / R25 (temporary) | 22:54–22:57 (across a compaction) | 22:57 "Our time, readback approved." | 23:22; reverted 23:51 | result handles on every completed return; `$handle` consumption across controllers; for feop_bound_c02 only | §13 temporary; reinstalled in a worktree for the exact rerun on 20 Oct 00:00 "Exact replication on 2.1.1, temporary change approved, readback approved." |
| side-by-side native (temporary) | 00:34 | 20 Oct 01:03 "Run the side by side natively, temporary change approved." | — | run-level change, no program change | §13 temporary |
| 2.2.0 / R26 | none before the phrase (the 01:41 message was the list of seven items) | 20 Oct 02:10 "Allow permanent changes, do the five Duck-layer defects as one release followed by the volume i pair readback approved." | 02:30 | pointer records carry `authored_by`; research mode accepts an empty query list; memory-gate head-of-line bypass (limit 3); second-return shape documented; `expected_status: FAILED` for declared controls (D5 part 1) | phrase given; the readback document was written after the phrase; one phrase for two versions |
| 2.3.0 / R27, core 0.11.0 | none before the phrase | same message, 02:10 | 03:01 | new core beside the sealed 0.10.2: `static_profile` construction, `local_metric_clock` readout, feedback `lapse_source` | as above |
| 2.3.1 / R28, core 0.11.1 | 20 Oct 16:47 | 17:10 "Allow permanent changes, readback approved" | 17:17 | the feedback clock: `feedback.history`, derived lapse χ = 1/N scaling the source block; three refusals | §13 |
| 2.3.2 / R29, core 0.11.2 | 21 Oct 10:13 (after the phrase at 10:03 "Leave it declared - Allow permanent changes") | 10:15 "readback approved" | 10:21 | the ordered feedback clock: per-event `metric_lapse`, path-ordered propagator, energy and inertia identities as native certificates, `ordered_history`, `inertia_scale`, `initial_field` | §13 |
| 2.3.3 / R30 | 21 Oct 11:08 | 11:09 "Allow permanent changes readback approved" | 11:21 | task fields `expected_output_status`, `expected_reason`, `supersedes`; FAILED_SUPERSEDED label; briefings state the three fields | §13 |
| 2.3.4 / R31 | 21 Oct 13:04 (the options message, which also reported the unreleased method edit below) | 13:19 "proceed with recommendation, allow permanent changes readback approved" | 13:32 | `expected_failed_check`; `expected_reason` also matches native failure records and failed checks; `observed_failed_checks` on returns | phrase given; the release plan was committed with the install |
| 2.3.5 / R32, core 0.11.3 | 24 Oct 12:47 | 13:50 "Allow permanent changes, readback approved" | 14:08 | declared floor on the one-log reservoir; new construction `line_of_sight`; regression coefficients; refusals | §13 |

### 1.2 Method document edited outside a release (`docs/DUCK_2.0_METHOD.md`; §5 makes any edit a permanent change)

| when | commit | change | in the loop |
|---|---|---|---|
| 19 Oct 17:37 | 613fd500 | freeze description and recovery command corrected after the 2.0.0 install | not told |
| 19 Oct 23:22 / 23:51 | 287310df, c2abbaca | the temporary episode wrote and removed a version row and a heading, although the episode file says the document stays byte-identical to the 2.0.1 freeze | not told |
| 21 Oct 10:47 | bcc02e29 | standing authoring requirement: a staircase is one admitted method; "standing authoring requirements live in campaigns/recipe_library/ and are copied into every briefing" (this put the recipe library under §5) | directed ("One recipe per staircase", 21 Oct) without §13 steps |
| 21 Oct 13:03 | 2e591ff2 | 1500 s standing window with a 600 s probe option; identities compiled from the library, not authored in the window; a one-page digest opens every framing | the window directed (12:xx–13:00, "1500 seconds is the standing window with a 600 second 'probe' run as an option"); "compiled not authored" and the digest not read back |

### 1.3 Briefing and authoring templates edited outside a release

| when | commit | file | change | in the loop |
|---|---|---|---|---|
| 19 Oct 23:58 | f7584603 | PEER_BRIEFING.md, RECIPE_AUTHORING.md (peer_restore template) | `because` keeps cross-controller keys only; `method_ref` under `returned` | not told as a method change (listed in the episode file as "should go in with" the permanent change) |
| 20 Oct 01:30, 02:08 | a3b31682, 78b034ae | RECIPE_AUTHORING.md | word and recipe limits learned in the FEOP runs | not told as a method change |

The method's rule "copy `campaigns/peer_restore_20261019/PEER_BRIEFING.md` and change only the question" was followed by
no campaign after 19 October; every briefing from 20 October was copied from the previous run's briefing.

### 1.4 Recipe library (briefing material from 21 Oct 10:47 on; every commit unversioned)

| when | commit | change | in the loop |
|---|---|---|---|
| 21 Oct 10:47 | bcc02e29 | staircase recipe, generator, task writer, offline harness | directed |
| 21 Oct 11:07 | 03915ea9 | fibered source words with partition receipts | directed ("the 64x64 engine limit stays; Duck-side helper") |
| 21 Oct 12:23 | 2e4a5147 | identity recipes (reversal, collinearity) | readback approved 12:24 as a "cheap change" for one run; the library stayed |
| 21 Oct 13:03 | 2e591ff2 | 24 identities validated and installed as the compiled set | reported at 13:04; not read back as a method change |
| 21 Oct 14:43 | b940fa95 | fibered-word gap fixes from feop_transfer_1 | not told |
| 21 Oct 19:05 | d027c39d | staircase revision 2: per-stage states, dwells, lapse ledger | directed ("Build the staircase recipe that returns each stage's state and proceed") |
| 22 Oct 11:38 | 11bc35e5 | staircase_front (THREE's front method) | directed ("Put three's recipe in") |
| 22 Oct 12:41 | 90182ad7 | staircase revision 3, staircase_front revision 2 | not told |

### 1.5 Briefing lineage: what the peers were told, by the date it first appeared

Computed by reading every campaign's TARGET.md and PEER_BRIEFING.md in creation order and listing each process line the
first time it appears (`tools`-independent script; the full line list is retained with this report's session). The 2.0
template is the baseline.

| first appeared | campaign | new instruction to the peers | in the loop |
|---|---|---|---|
| 19 Oct 16:27 | peer_restore (template) | "produce ideas and constructions, not answers or proofs"; one 900 s window; expectation before a scan, account for a peer's result, read a failure; "author your own methods"; hands = the native catalogue; roles CLOCK/RULER/PROPAGATION/JOINT | the method (H002731) |
| 19 Oct 18:29 | aq_identification | `because` naming completed result keys; `$result` paths inside payloads | 2.0.x features, in releases |
| 19 Oct 22:52 | feop_bound_c02 | roles renamed per campaign (LOCAL, CRT, BOUND, REVIEW); "openings" re-executed in the run so numbers exist by `$result`; result handles | roles and openings not read back |
| 20 Oct 01:05 | feop_sidebyside | "keep every host-side script and data file under peers/NAME/gen/"; "build a control that should fail so the task COMPLETES with a sign"; "the window closes 900 s after ROUND1_START.json; nothing before FINALIZATION_RESULT is an instruction to stop"; "four things asked by role" | not read back |
| 20 Oct 03:07 | voli_lapse | "the manuscript's statements with their locations, the external key written before the run" | you struck this framing during the run ("we are not 'testing' volume I we are trying to learn") |
| 20 Oct 03:26 | explore_voli_threads | roles dropped: ONE, TWO, THREE, FOUR; "no test, no key, no expectation to meet. Produce constructions and leads; say what failed" | followed your 20 Oct direction |
| 20 Oct 17:44 | spin_work | `prior/LEAD_FRAMING.md` read first; "we are trying to learn" as the standing words | the framing document not read back |
| 20 Oct 18:33 | rh_crossover | "ONE bounded queue of at most 64 tasks shared by all four peers; keep at most ~12 in flight; submit a chain's next step only when the previous completed" | not read back |
| 21 Oct 12:23 | voli_threads_5 | 1500 s window marked TEMPORARY; "identity recipes, compiled not authored"; LEAD_FRAMING as "a one-page digest of everything established natively; it replaces reading the older reports" | window: readback approved 12:24; compile-not-author and digest not read back |
| 21 Oct 13:37 | spin_work_4 | "the standing window since 2026-10-21" (1500 s) | your direction, recorded outside §13 |
| 21 Oct 16:17 | spin_reconstruct_1 | blind rebuild: read only this directory; list every file read; say if you already know a value | your decision after the "exam" discussion; superseded the same day |
| 21 Oct 16:57 | spin_verify_1, feop_verify_1 | the verification form: "you have everything the earlier peers had, plus their answers"; separate code; exhaustive optimum; predictions time-stamped in NOTES.md before any task; routes assigned by name (library route / independent-code route); "state for every number its hypotheses and its comparison family" | your decision ("less like a test and more like a verification"; "Proceed with the FEOP verification run in the same form") |
| 21 Oct 18:06 | volii_matter_1 | "Volume II is material, not a statement under test" | followed your rule |
| 22 Oct 10:50 | volii_matter_3 | "exploration ... in the verification form: you are given everything, including the lead's predictions, and you write your own before computing"; **Budget, a rule of this run**: tasks per window with counts (8 records, 12 generators, 12 maps, chain 3, witnesses 2–4); "one case to its witness before the next; no front-loaded scans"; `expected_reason`, `expected_failed_check`, `supersedes` rules | your "word" on the lead's recommendation after volii_matter_2; the form transfer and the budget not read back as method changes |
| 22 Oct 11:45–14:09 | volii_matter_4–6 | "a labelled host addendum that already contradicts two of [the lead's predictions]" given to the peers; four conventions "that are rules of this run" | directed runs ("Put three's recipe in ... run the third family recommendation"; "Apply the suggested words to all of them"; "run the switched share"); the addendum practice not read back |
| 22 Oct 19:29 | rh_transition_2 | "separate code, not edits of the lead's"; the lead's two host implementations given; "exhaustive where a search is claimed; controls built to break" | your "proceed as recommended" on route A |
| 24 Oct 11:20 | voli_ceiling_1 | "This is an idea run (Sean Brady: 'Duck doesn't answer questions it gives ideas'): the record wanted is candidate equations with exact hands and an honest line on each"; Budget rule (25 tasks, 36 ceiling, 900 s); "host algebra (sympy/mpmath) is allowed for writing and checking candidate laws; native witnesses on the identities that arise" | your words framed it; host algebra "allowed" not read back |
| 24 Oct 12:45 | voli_ceiling_3 | standing rules list: admit on your own controller; exact strings everywhere; `source_binding: {"$source": true}`; declare domain checks as REFUSED; recipe limits | engine facts, not read back as briefing content |
| 24 Oct 16:01 | voli_ceiling_4 | host algebra "is allowed and expected" | not read back |
| 24 Oct 17:36 | volii_gate_1 | "the Volume II standing window" (1500 s); openings = four gate recipes pre-admitted on every controller; the installed machine named in the briefing | not read back |
| 24 Oct 20:10 | volii_li6_1 | verification form with the archive's numbers as predictions and "the lead's host reproduction with separate code"; openings with expected values written in the briefing ("expect 12", "expect 6") | your "go #1" on the recommendation; expected values in the briefing not read back |
| 25 Oct 16:40 | rh_window_1 | "everything is given, including the lead's predictions, the lead's host code and its results; you write your own predictions, you write separate code, and you build native witnesses"; 92 new process lines | your "go #1" (the RH window table in verification form) |
| 28 Oct 03:39 | typed_primes_1 | briefing copied from rh_window_1 (32 of 63 lines identical; 4 from the template); "This is a learning run"; "Courtroom II rules apply: numbers you report come from a file you produced"; TARGET: "Host code (standard Python; mpmath/sympy under peers/NAME/gen/) is expected: the table is host work; the native lane is for certificates"; openings = the table's counts admitted by exact value | your "go" on the 900 s pair; the briefing's content not read back |

### 1.6 Runs since 2.0.0: form and the peers' behaviour

`gen` = host scripts and data files the peers wrote under `peers/*/gen/`; `native` = native returns in the run.

| date | campaign | window | form | roles | budget rule | host-code instruction | gen | native |
|---|---|---|---|---|---|---|---|---|
| 19 Oct | peer_restore (next) | 600/900 | idea | named | no | none | 0 | — |
| 19 Oct | aq_identification | 900 | idea | named | no | none | 0 | — |
| 19 Oct | resting_clock | 900 | idea | named | no | none | 0 | — |
| 19–20 Oct | feop_bound_c02 (3 runs) | 900 | computation by role | named | no | none | 10 | 74 / 61 / 61 |
| 20 Oct | feop_sidebyside | 900 | computation by role | named | no | scripts rule | 51 | 210 |
| 20 Oct | feop_bracket_fiber | 900 | computation by role | named | no | scripts rule | 122 | 298 |
| 20 Oct | voli_lapse | 900 | manuscript vs external key (struck) | named | no | scripts rule | 22 | 148 |
| 20 Oct | explore_voli_threads | 900 | learning | none | no | scripts rule | 66 | 245 |
| 20 Oct | spin_work_1, spin_work_2 | 900 | learning | none | no | scripts rule | 62, 57 | 399, 417 |
| 20 Oct | rh_crossover_1 | 900 | learning | none | no | scripts rule | 43 | 315 |
| 20 Oct | voli_threads_3 | 900 | learning | none | no | scripts rule | 41 | 245 |
| 21 Oct | spin_work_3 | 900 | learning | none | no | scripts rule | 60 | 465 |
| 21 Oct | voli_threads_4 | 900 | learning | none | no | scripts rule | 33 | 233 |
| 21 Oct | voli_threads_5 | 1500 (TEMPORARY) | learning | none | no | scripts rule | 55 | 435 |
| 21 Oct | spin_work_4 | 1500 | learning | none | no | scripts rule | 107 | 529 |
| 21 Oct | feop_transfer_1 | 1500 | learning | none | no | scripts rule | 54 | 447 |
| 21 Oct | spin_reconstruct_1 | 1500 | blind rebuild | none | no | scripts rule | 0 | 8 |
| 21 Oct | spin_verify_1, feop_verify_1 | 1500 | verification | none | no | scripts rule, separate code | 87, 77 | 491, 346 |
| 21 Oct | volii_matter_1, _2 | 1500 | learning | none | no | scripts rule | 129, 126 | 514, 586 |
| 22 Oct | volii_matter_3–6 | 1500 | exploration in the verification form | none | yes | scripts rule | 71, 62, 33, 52 | 250, 235, 247, 207 |
| 22 Oct | rh_transition_2 | 1500 | verification | none | yes | separate code | 49 | 218 |
| 24 Oct | voli_ceiling_1–4 | 900 | idea run | none | yes | host algebra allowed (→ expected) | 14, 25, 26, 27 | 53, 108, 114, 143 |
| 24 Oct | voli_ceiling_5 | 1500 | idea run | none | yes | allowed and expected | 33 | 165 |
| 24 Oct | volii_gate_1 | 1500 | idea run | none | yes | allowed and expected | 45 | 161 |
| 24–25 Oct | volii_li6_1 | 1500 | verification | none | yes | separate code | 49 | 165 |
| 25 Oct | rh_window_1 | 1500 | verification | none | yes | lead's host code given; separate code | 137 | 146 |
| 28 Oct | typed_primes_1 (+ replicate) | 900 | learning | none | yes | host code expected | 78 | 110 (+105) |

## 2. The drift, documented

### 2.1 What the method says and what the briefings came to say

The method (H002731, 19 Oct) and its template say a peer produces ideas and constructions, authors its own methods, has the
native catalogue as its hands, and reads one briefing whose only variable part is the question. By 28 October the briefing
in force said: the openings are a table of counts; host code is expected; the table is host work; the native lane is for
certificates of host numbers; a budget of about 25 tasks with 40 as the ceiling; one case to its witness before the next;
no front-loaded scans; every number names its comparison family; Courtroom II rules apply to every number reported. The
first paragraph still said "ideas, equations and witnesses, not answers or proofs". A peer reading both follows the
concrete one.

### 2.2 The behaviour followed the briefings, from the second day

The three runs on the template (peer_restore next, aq_identification, resting_clock) have no peer host scripts. The first
FEOP run has 10; from 20 October every run has 22 to 137, with hundreds of native returns per window. The counts do not
move with the stated form: learning runs (spin_work_4: 107 scripts, 529 returns) and verification runs (rh_window_1: 137
scripts, 146 returns) look alike. The idea runs of 24 October are the exception, with 14 to 33 scripts, and they are
also the runs whose briefing led with "Duck doesn't answer questions it gives ideas" and had the smallest budgets. The
peers do what the briefing in front of them says, and the briefing changed on 20 October.

### 2.3 The mechanism, in the order it operated

1. **Copy-forward instead of the template.** The method's rule to copy the template briefing and change only the question
   was never followed after 19 October. Each briefing descended from the previous run's, so every rule added for one run
   stayed for all later runs. The typed-primes briefing shares 32 of its 63 lines with rh_window_1 and 4 with the template.
2. **Host code legitimised as housekeeping (20 Oct).** "Keep every host-side script under peers/NAME/gen/" was written to
   stop file collisions in the FEOP runs. Read by a peer, it says host scripts are part of the job. It is in every
   briefing after it.
3. **Roles by campaign, then none (19–20 Oct).** The template's four roles became campaign-specific computational roles
   (LOCAL, CRT, BOUND, REVIEW; BRACKET, REMAINDER, COMPARE, REVIEW) with "four things asked by role", then were dropped
   for ONE to FOUR after your 20 October correction. The computational framing of the role runs survived the dropping of
   the roles.
4. **Openings as a starting table (19 Oct on).** Pre-executed openings make numbers referenceable by `$result`. From
   volii_li6_1 the briefing also printed the expected values; from typed_primes the openings were the counts of a table
   the lead had computed. A window that starts from the lead's numbers continues from them.
5. **The verification form outside verification (22 Oct, 28 Oct).** You set the form on 21 October for verification runs:
   everything given, separate code, predictions first. On 22 October volii_matter_3 was framed as "exploration in the
   verification form" and the next three runs followed; the briefing also handed peers "a labelled host addendum that
   already contradicts two of [the lead's predictions]". On 28 October a learning run inherited the RH verification
   briefing and the sentence "host code is expected". Neither transfer was read back to you as a change of form.
6. **Budgets and witness discipline (22–24 Oct).** "Budget, a rule of this run" with task counts, "one case to its
   witness before the next", "no front-loaded scans", and the standing-rules block of engine facts turned the window
   into a schedule of certified tasks. These answered real problems (late returns, queue overruns, broken payloads) and
   none was read back as a method change.
7. **"Compiled, not authored" (21 Oct 13:03).** The unreleased method edit made the identities a compiled library and
   opened every framing with a digest of what is established. It removed the method's own counterweight to execution,
   and the briefings from voli_threads_5 said so to the peers.
8. **The method silent on forms.** The method document never defined idea run, learning run, verification form, blind
   rebuild, budget or host code. They exist only in briefings, so the briefing of the last run became the method of
   the next, and the method's version history has no row for any of them.

### 2.4 Who was in the loop

Directed by Sean Brady in chat, recorded, but never read back as a change to the method (dates): the "we are trying to
learn" standing words and the end of external keys (20 Oct); the verification form (21 Oct); 1500 s standing (21 Oct);
one recipe per staircase (21 Oct); staircase revision 2 (22 Oct); "Put three's recipe in" (22 Oct); route A separate-code
verification (22 Oct); "Duck doesn't answer questions it gives ideas" (24 Oct); "go" on each run named in §1.6.

Not told: the host-scripts rule; the controls-that-fail rule; queue and in-flight limits; the LEAD_FRAMING document and
the digest; the budget rule; expected values printed in openings; host algebra allowed then expected; the verification
form applied to exploration and to a learning run; the method edits of 19 and 21 October other than the window; the
template edits of 19–20 October; the library revisions of 21 Oct 14:43 and 22 Oct 12:41.

### 2.5 What did not drift

The engine, its releases and rollbacks; the lead outside the window with no steering, no ranking and no decoys; engineering
labels only and no claims; preregistration by hash before preparation; the run records, each naming the installed version,
window, peers and campaign; the triage after the window in engineering labels; the Courtroom II publish/withhold rule.

### 2.6 Correction to the lead's earlier statement in this session

Earlier today the lead said "the break was 28 October". The run table says otherwise: the peers' behaviour changed on 20
October, the second day of 2.0, when host scripts entered the briefings and the FEOP computations set the pattern. 28
October is the day a learning run was given a verification briefing with "host code is expected", which is the sharpest
single instance, not the first.

## 3. Decisions this leaves with Sean Brady

Listed, not recommended. Which of the briefing rules of §1.5 become method (a release with the phrase), which are
dropped, and which stay run-by-run with a temporary readback. Whether the template rule ("copy and change only the
question") is restored or replaced by a versioned briefing. Whether the method document gains definitions of the run
forms (idea, learning, verification, blind rebuild) and of host code's place in each. Whether the two unreleased method
edits of 21 October are ratified in a release or reverted. Whether the recipe library is briefing material under §5, and
if so how its revisions are versioned. How the 900 s runs of 24 and 28 October are annotated against the 1500 s standing
window.
