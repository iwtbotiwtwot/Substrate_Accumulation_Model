# Release record: Duck 2.3.3 / IRONCLAD-R30, D5 completed, 2026-10-21

**Kind:** permanent installed-version change, Duck layer only (CLAUDE.md §13). Sean Brady: "proceed as recommended", then "Allow permanent changes readback approved".
**Where:** ironclad main 4566c04 (merge commit; release commit e3dc873, tag duck-2.3.3), history entry H002754, plan docs/DUCK_2.3_3_RELEASE_PLAN.md, fixture qualification/fixtures/declared_control_2
(PREREGISTRATION.json with two open amendments, RUN_CHECK.json), runs runs/duck/ironclad-r30-declared-control-2, -2b, -2c.

**What changed.** A control task may now declare the engine status it must complete with (expected_output_status, for controls the engine completes as
unresolved), or the reason it must fail with (expected_reason; a control failing for another reason counts against its declaration). A resubmission may
declare the undeclared failed first attempt it supersedes; when it completes, the first attempt is labelled FAILED_SUPERSEDED in the accounting and the run
can finalize COMPLETE, while the first attempt's receipt is never rewritten. An undeclared failure nobody supersedes still labels the run as before.

**Evidence.** Tests 162 before, 170 after; verify PASS at IRONCLAD-R30 / 2.3.3 / 0.11.2. The fixture needed three runs: the first used a first attempt the
engine completed (the registered expectation was wrong; the superseding submission was correctly rejected); the second used a payload that failed natively
but the superseding submission was rejected by the same-author rule because the first attempt was a plan opening; the third submitted both in the window
and every registered relation held. Known limit logged: a plan opening cannot be superseded. Rollback to duck-2.3.2 verified before install. Independence: none.

Directed by Sean Brady. Executed with Claude Code.
