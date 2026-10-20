# Run record: result-handle test (Duck 2.1.1 / IRONCLAD-R25), 2026-10-20

**Kind:** engineering test of a TEMPORARY program change (no scientific claim).
**Where:** ironclad `qualification/fixtures/result_handle`, runs `ironclad-r24-handle-smoke`, `ironclad-r24-handle-smoke2`,
`ironclad-r25-handle-smoke`; history entry H002736; ironclad main `287310d`, tag `duck-2.1.1-temp`.

**Direction (Sean Brady):** "Make every checked result usable in another calculation. … Add a common result handle carrying the
inputs, dependencies, basis, source and execution identity. Let another controller consume it directly." Readback approved
("Our time, readback approved") as a temporary change for the FEOP run `feop_bound_c02_20261020`; reverts to Duck 2.0.1
(tag `duck-2.0.1`, rollback verified in a worktree before install) when that run concludes, unless made permanent.

**What changed (Duck layer only; sealed core 0.10.2 untouched):** every completed native return carries a `handle`
(inputs, dependencies, basis labels of matrix outputs with deterministic labels where none are declared, source binding and
native source manifest, execution identity, outputs). A `{"$handle": key, "output": name}` reference resolves to a typed
certified-matrix operand with those bases, authenticated like `$result`; the referenced result's event joins the consumer's
`because` (2.1.1). A `$handle` to an output the result lacks is refused at admission.

**Result:** fixture hashed 03:59:31Z before implementation; five expectations written in advance. The 2.1.0 smoke met four
(the `because` link was missing); 2.1.1 fixed it and met all five: a cross-controller adjoint of a source-word residual
(−24/169) completed with the generated labels swapped, `because [18]` acknowledged by the consumer's controller, control
refused with "has no output 'no_such_output'; its handle offers ['matrix']". Suite OK; verify PASS; qualification PASS on
the 2.1.1 smoke.

**Status:** TEMPORARY, installed for one run. Independent verification: none (Claude-written code and tests; fixture
inputs copied from the abandoned Codex run).

Directed by Sean Brady. Executed with Claude Code.
