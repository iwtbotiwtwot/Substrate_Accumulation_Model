# Decisions (Sean Brady, in his words)

- 2026-10-19 — "I think this is when we start to build https://github.com/iwtbotiwtwot/Substrate_Accumulation_Model (repo
  exists) as the courtroom successor. I only want to apply courtroom discipline to documentation and provenance I don't want to
  make everything a test. I want to carefully document on all 3 volumes, I am terrible at remembering to commit and sync that
  should be procedure at the conclusion of any run or 'test'. I'll defer to you for the layout, would need a living .md of
  [the three volume PDFs] that we can update as we go."
- 2026-10-19 — Duck 2.0.0 installed in ironclad ("Allow permanent changes, readback approved"); change control in ironclad
  CLAUDE.md §13 governs any change to the research program.
- 2026-10-19 — Model choice: "Repeated runs with Fable will get expensive in the long run … we should designate a 'recommended
  model' for each run if some are less complex than others." Lead's readback: peers on Opus for the a(q) run as a temporary
  change, reverting after. Sean Brady: "temporary change approved".
- 2026-10-19 — Follow up on the lead's recommended idea: the a(q) identification (ironclad campaign `aq_identification_20261019`).
- 2026-10-19 — "follow your next recommended idea, temporary change to use Opus peers." → ironclad campaign `resting_clock_20261019` (the resting-clock comparison that decides γ); peers on Opus as a temporary change for this run, reverting after.
- 2026-10-20 — "I gave Codex a shot a Duck, big mistake same problem- unauthorized changes. Can you look into this and make sure we are running exactly the last version you ran." Then: "I was suspicious and did not allow any merges, mark abandoned - the runs contain useful information can we retain the data?" → Codex branches abandoned in both repositories (ours-merge), data retained outside git (ironclad H002734).

## 2026-10-20 — Result handles as a TEMPORARY program change
Sean Brady approved the readback ("Our time, readback approved") for Duck 2.1.x result handles, installed for the FEOP run only; main returns to Duck 2.0.1 at the run's conclusion unless he types the permanent-change phrase. Record: runs/20261020_result_handle_test/RECORD.md.

## 2026-10-20 — Temporary change ended; ironclad main back on Duck 2.0.1
Per Sean Brady's change-control rule, the result-handle change (Duck 2.1.1 / IRONCLAD-R25) was reverted after feop_bound_c02 concluded (ironclad H002738): program files restored from tag duck-2.0.1, suite OK, verify PASS, 2.0.1 freeze matches; records of the episode kept; recovery from tag duck-2.1.1-temp if Sean Brady makes it permanent. Run record: runs/20261020_feop_bound_c02/RECORD.md.

## 2026-10-20 — Blind replication of the FEOP run
Sean Brady asked for the same FEOP run without the data it had gained, to compare. Done as a worktree at the pre-run commit with Duck 2.1.1 reinstalled there temporarily (approved readback); main stayed on 2.0.1; worktree removed after. Procedure adopted for future replications: pre-run commit worktree, fresh peers, lead's capture outside what peers read. Record: runs/20261020_feop_bound_c02_rerun/RECORD.md.

## 2026-10-20 — Third FEOP replicate on the installed version
Sean Brady asked for the same run on the reverted Duck 2.0.1 to check it does not underperform the temporary build; agreed framing: regression check plus third replicate, not a performance comparison. Result: the installed version ran the full recipe; the temporary handle change was not needed by this campaign. Open design point D5: a run with one declared failing control is labelled FAILED_WITH_RETAINED_OUTCOMES because a task cannot declare an expected FAILED. Record: runs/20261020_feop_bound_c02_run3/RECORD.md.

## 2026-10-20 — Matrix limit: recipe route tried first, engine release not needed for reach
Sean Brady chose to try the fibering/recipe route before any engine release. Result (ironclad H002742): fibering reaches far past the 64-row word limit with no program change, and the real obstruction is the residue count p^(2k), which no matrix limit changes. The engine-release candidate for the matrix limit is therefore downgraded to a convenience; the route to the bracket rows at large k is a per-level receipt, logged as an open idea. Record: runs/20261020_feop_bracket_fiber/RECORD.md.

## 2026-10-20 — Permanent release Duck 2.2.0 (five Duck-layer defects) and the Volume I pair
Sean Brady typed the permanent-change phrase and approved the readback for two items in order: the five Duck-layer defects as one release (done: Duck 2.2.0 / IRONCLAD-R26, ironclad H002743, tag duck-2.2.0) and then the Volume I pair (a static Λ(x) profile with two positions; a derived local metric clock), which live in the sealed core and therefore proceed as a new core version with its own written plan, fixtures and rollback check before install. Record: runs/20261020_duck_2_2_0_release/RECORD.md.

## 2026-10-20 — Core 0.11.0 installed as a new version beside the sealed 0.10.2
Sean Brady's permanent-change phrase and readback approval covered the Volume I pair; because both live in the sealed core, they were built as core 0.11.0 (a copy with additions; 0.10.2 untouched), installed as Duck 2.3.0 / IRONCLAD-R27 (ironclad H002744, tag duck-2.3.0). Procedure adopted for future core changes: new version directory, manifest repointed with the history entry as authority, predecessor manifest retained, rollback verified, fixtures pre-registered. Record: runs/20261020_core_0_11_0_release/RECORD.md.

## 2026-10-20 — Runs are for learning, not for testing the volumes
Sean Brady, during the voli_lapse run: "We are done binding these runs to manuscript/volume, again we are not 'testing' volume I we are trying to learn and this is not the way." and "That is the material we should be following up on, not 'finding manuscript material to test'." From here, run targets are open questions on the material the runs themselves produce (his pasted summary of a(q), resting_clock and spin_memory is the next material); no exam framing, no external keys, no pass/fail rows, no verdicts on volumes; run findings are recorded here as leads. The next campaign is staged and prepared, not deployed (stopped for the night). Record: runs/20261020_voli_lapse/RECORD.md.

## 2026-10-20 — Rollback of the Volume I pair withdrawn; feedback clock defined and installed as core 0.11.1
Sean Brady asked for a rollback of the Volume I pair, then withdrew it: "Disregard the rollback, I need a precise definition connecting lapse, event count, elapsed time and the feedback evolution time..." He adopted the recommended conventions ("proceed with your recommendations": coordinate time per source tick = 1/N; N scales the source block of the feedback generator) and approved the permanent change ("Allow permanent changes, readback approved"). Installed as core 0.11.1 / Duck 2.3.1 / IRONCLAD-R28 (ironclad H002746, tag duck-2.3.1). Record: runs/20261020_core_0_11_1_release/RECORD.md.

## 2026-10-21 — Γ stays declared; ordered feedback clock installed as core 0.11.2
Sean Brady, on the lead's readback of the ordered feedback clock (one metric lapse per event, field carried between events, inertia-identity certificate, N·Γ readout): "Leave it declared - Allow permanent changes", then "readback approved". Γ = κ/(2c) remains an input of the action; no construction derives it. Installed as core 0.11.2 / Duck 2.3.2 / IRONCLAD-R29 (ironclad H002753, tag duck-2.3.2). Record: runs/20261021_core_0_11_2_release/RECORD.md.

## 2026-10-21 — D5 and the 64×64 word limit: "proceed as recommended"
Sean Brady, on the lead's options: for D5, richer control declarations (an expected engine output status, an expected failure reason) plus declared superseding of undeclared failed first attempts, as one Duck release (2.3.3), prepared on ironclad branch `duck-2.3.3` and awaiting his "Allow permanent changes" and readback approval (docs/DUCK_2.3_3_RELEASE_PLAN.md). For the 64×64 source-word limit: the engine limit stays (option A); a Duck-side fibering helper with partition receipts is adopted (option C), ironclad `campaigns/recipe_library/fibered_word/` (commit 03915ea). An engine revision to 128 remains the step to ask for if the FEOP work needs p = 11 at k ≥ 3 by enumeration.

## 2026-10-21 — Duck 2.3.3 installed
Sean Brady: "Allow permanent changes readback approved" on docs/DUCK_2.3_3_RELEASE_PLAN.md. Installed as Duck 2.3.3 / IRONCLAD-R30 (ironclad H002754, tag duck-2.3.3). Record: runs/20261021_duck_2_3_3_release/RECORD.md.

## 2026-10-21 — 1500 s window, one run (temporary)
Sean Brady: "Do both cheap changes and prepare the next run at 1500 seconds", then "readback approved". Temporary per CLAUDE.md §13: voli_threads_5 ran with a 1500 s window; the method's 900 s stands. Result of the trial: 67 identities certified natively against 12 at 900 s. The standing window is his next decision.

## 2026-10-21 — 1500 s is the standing window; 600 s probe runs as an option; recipes validated into the library
Sean Brady, after the voli_threads_5 trial (67 identities certified natively against 12 at 900 s): "1500 seconds is the standing window with a 600 second 'probe' run as an option. If recipes are validated pass, talk to me about the expected_reason fix." Recorded in ironclad docs/DUCK_2.0_METHOD.md (commit 2e591ff2). The 24 recipes the peers admitted in voli_threads_5 were replayed offline (admit, compile with the peers' inputs, execute): every passing execute PASSED and every declared control FAILED at its check; they are now in campaigns/recipe_library/identities/ with examples. The expected_reason fix is the next discussion.

## 2026-10-21 — Duck 2.3.4 installed
Sean Brady: "proceed with recommendation, allow permanent changes readback approved" (option B, a named check, plus option A, the widened reason). Installed as Duck 2.3.4 / IRONCLAD-R31 (ironclad H002757, tag duck-2.3.4). Record: runs/20261021_duck_2_3_4_release/RECORD.md.

## 2026-10-21 — Verification runs give the peers everything; no sealed answers
Sean Brady, on a staged blind rebuild of headline results (values sealed by hash, peers forbidden the earlier reports): "we are asking the peers to verify something and not giving it to them?" and "Is the a smarter way that is less like a test and more like a verification?" Decision: a verification run gives the peers every value, field file and report, and gets its strength from separate code, exhaustive optima, the explanation as a native ordering, predictions written before computing, and controls built to break the explanation. Hidden answer keys are for engineering fixtures of program changes, not for verifying what the runs learned. The earlier rule stands as clarified: runs are not pointed at the volumes as tests; verifying our own run results is in scope ("this is verifiying what we learned"). First run in this form: spin_verify_1 (ironclad H002760); FEOP next in the same form. Record: runs/20261021_spin_verify_1/RECORD.md.

## 2026-10-22 — Seven ideas closed on the lead's done-or-superseded list
Sean Brady: "Apply the suggested words to all seven and commit". Applied in `ideas/IDEAS.md`: adopted — voli_lapse "Fix the feedback lapse" (core 0.11.1); spin_work_2 queue-bound briefing note; spin_work_3 D5 note's remaining authoring-guide line; Duck 2.3.3 fixture authoring-guide line; the control-declaration note in spin_work_4 and volii_matter_1; the (field, dwell) keying part of spin_work_4's "Staircase library variants" (library revision 2; its other two parts stay open). Dropped as superseded — spin_work_4 "Execute TWO's compiled continuous-family recipes" (spin_verify_1's exhaustive optima). The thread index at the top of IDEAS.md was written the same day at his direction ("Write the thread index please").

## 2026-10-22 — volii_matter_3 items closed after volii_matter_4
Sean Brady: "Apply the suggested words to all of them and commit, proceed with the next recommended run please." Applied in `ideas/IDEAS.md` (volii_matter_3 section): adopted — the front recipe as a library candidate (built, ironclad 11bc35e5); a third family for the total-optimal pair (done: G160, G320, offset); per-chain and per-policy split of the interior switch (done); cross-family bands with a failing control, rM1/rM2 as full staircases, the split at the switched lapse list (done); switched-lapse shares: the lapse-1/4 case, the 1/2-against-1/4 ordering on one family, the exit-switch identity (done). Dropped — local continuous refinement (superseded by the grid-free optimum item); the stage-lapse ceiling as the switched share's denominator (not a bound). Next run directed: the grid-free optimum per chain with a native local-maximum certificate (the lead's recommendation after volii_matter_4).

## 2026-10-22 — the grid-free optimum item closed; the switched share directed with four constraints
Sean Brady: "Apply the suggested words and run the switched share please. For the proposed check, keep the record preparation, switching account and information denominator consistent, optimize both policies for total work, and test the switched N=1/2 versus N=1/4 ordering on the second field family." Applied: volii_matter_4's "grid-free optimum per chain with a native gradient certificate" — adopted (done in volii_matter_5, H002766). Run volii_matter_6 staged under the four constraints: records prepared on the unlapsed source (N_0 = 1, separation 1) for every case; the switching account is the native lapse ledger (gain_total = gain + gain_lapse) with the same lapse list form (1, N, N, 1) for every N; the information denominator is I(1), the unlapsed record's ceiling, for every N (THREE's stage-lapse denominator is not a bound and is not used); every chain at its field-plus-lapse (total) optimum on the family; the N = 1/2 against 1/4 ordering of gain_total tested on the second family (G160) with its negation declared.

## 2026-10-22 — RH exterior ledger: route A (domain experiment plus a standard verification window); no window change; no pod now
Sean Brady, after the lead compared a long Duck window carrying the arithmetic (B) against native sessions for the arithmetic and a standard 1500 s Duck window for
separate-code verification (A), and asked about a pod: "proceed as recommended". Route A: the native exterior ledger comes from the RH DomainSession runs on T500
(single process with fail-fast checks, and a six-shard replicate), followed by a 1500 s Duck verification window in which the peers reconstruct the ledger with separate
code, re-derive the mask topology, spot-check native forms and witness the headline differences and the published target. The standing window stays 1500 s (his
earlier "remove the time limit" was offered, not needed). A pod is deferred to a many-transition campaign (the sign of the exterior move across many accounts), staged
under the pod protocol with his cost and deadline bounds when he directs it.

## 2026-10-22 — Volumes track the record: every run's conclusion adds its entry to the living text
Sean Brady: "lets update before we remove or rearrange" and "I think that is a good idea lets update the data as we go and see what we end up with." Procedure from here: the
conclusion of every run or test adds its entry to the relevant volume's appended "Run results received into Volume N" section (result / reading / idea labels, campaign and
history entry cited) with a change-log line, as part of CLAUDE.md §2 of this repository. The three sections were created 2026-10-22 (doc repo 9bcf242). No removal or
rearrangement of manuscript text until Sean Brady decides the placement of Volume I's Chapters VII–XII (ideas/IDEAS.md).

- 2026-10-23 — Sean Brady, on the pods live page reaching its 32 KiB allowance (the predecessor-era sections were moved verbatim to ironclad docs/live_archive instead): "if we need to expand the live page to make sure we have everything we need that is approved." Standing approval to raise the live-page allowance in the validator (precedent H002719, 16 → 32 KiB) when a move would lose anything; not exercised yet, nothing was lost.

- 2026-10-23 — Sean Brady, on the original primitives and the fate/Home chapters: "they are not wrong and opened the door to what we are doing now - the basis for the original SLC ... I do not want to abandon those ideas but maybe set them as targets to receive their own more mature foundations if the roadmap allows it." Then "word" on a targets register: volumes/I/TARGETS_REGISTER_20261023.md (fourteen entries, each with where it entered, what it opened, what it awaits, the construction that would move it, the check). A target is not a premise.
