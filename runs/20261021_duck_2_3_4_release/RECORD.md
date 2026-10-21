# Release record: Duck 2.3.4 / IRONCLAD-R31, a control names its check, 2026-10-21

**Kind:** permanent installed-version change, Duck layer only (CLAUDE.md §13). Sean Brady: "proceed with recommendation, allow permanent changes readback approved".
**Where:** ironclad main 1ac3e47a (tag duck-2.3.4), history entry H002757, plan docs/DUCK_2.3_4_RELEASE_PLAN.md, fixture qualification/fixtures/declared_control_3
(PREREGISTRATION.json, RUN_CHECK.json), run runs/duck/ironclad-r31-declared-control-3.

**What changed.** A recipe control may now name the step whose check must fail. It counts as declared only when that check failed and the recipe raised no
engine error; a control that breaks for another reason counts against the run. The expected-reason text also matches the engine's own failure record and
the failed checks, so "bases differ" or a step name can be declared. The identity library's controls now name their residual check.

**Evidence.** Tests 170 before, 176 after; verify PASS at IRONCLAD-R31 / 2.3.4 / 0.11.2; pre-registered fixture: honest execute completed, the check control
as declared with the residual check observed, the basis-error control declared by reason as declared, and the basis-error control declared on the check
counted against the run, giving the registered label of one failure. Rollback to duck-2.3.3 verified before install. Independence: none.

Directed by Sean Brady. Executed with Claude Code.
