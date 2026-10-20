# Release record: Duck 2.2.0 / IRONCLAD-R26, the five Duck-layer defects (PERMANENT), 2026-10-20

**Kind:** program release (engineering; no scientific content).
**Where:** ironclad `docs/DUCK_2.2_RELEASE_PLAN.md` (readback), `docs/DUCK_2.2_ROLLBACK_CHECK.json`, history entry H002743, tag `duck-2.2.0`,
tests `SAM_PROJECT/gen6_duck_t500/tests/test_release_2_2.py`, fixtures `qualification/fixtures/declared_control` and `gen6_history`.

**Direction (Sean Brady):** "Allow permanent changes, do the five Duck-layer defects as one release followed by the volume i pair readback
approved."

**Changes, Duck layer only (sealed core 0.10.2 and SLC engines untouched):**
1. Pointer records for oversized results now carry `authored_by`, `construction`, `cites`, `prior_task_key` (119 of 298 returns in the
   fibering run had lacked the author label).
2. Research mode accepts an empty initial query list; search workers stand ready for live submissions.
3. Memory gate: a head task blocked only by memory no longer blocks its lane; a younger task that fits may pass it, at most three times per
   head, logged; causal-ACK-blocked heads still block.
4. The second-return route (history import, then resume) is documented as a task shape in the peer template, from its fixture.
5. Declared controls: a task may state `expected_status: "FAILED"`; a failing return is counted `FAILED_AS_DECLARED` and no longer relabels
   the run; a declared control that completes is counted against the run. Closes design point D5 raised in runs 3 and the side-by-side.

**Checks:** suite OK (5 new tests); verify PASS on IRONCLAD-R26 / Duck 2.2.0; rollback to Duck 2.0.1 (tag `duck-2.0.1`) verified before install;
declared-control fixture (pre-registered) finalized COMPLETE with counts {COMPLETED 1, FAILED_AS_DECLARED 1}, exactly as written; gen6_history
imports COMPLETED on 2.2.0 (the resume step was not exercised in the short window: the lead's decision submission preceded the imports and was
rightly rejected). Not yet exercised by a run: the pointer label and the memory bypass; both rest on code and tests until the next large run.

**Still open from the 2.0 defects list, outside the Duck layer:** a `common_clock` block dropped on a feedback construction and no per-stroke
trace time (sealed core); recipe scalar inputs reject intervals (SLC method engine).

Directed by Sean Brady. Executed with Claude Code.
