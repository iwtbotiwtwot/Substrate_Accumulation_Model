# Execution Posture, Engine Policy & Output Contract (GEN7)

## 1. Operating Posture: Mode 2/3 Hybrid (Unverified-Lane CR2 + Locked-Baseline Continuation)
- **Verification Standard:** For every unverified Volume II claim in your assigned lane, reconstruct the proof and calculation independently from the raw source operands, pre-commit predictions before execution, and include at least one reachable hypothesis-breaking control (`expected_status`, `expected_reason`, or `expected_failed_check`).
- **Reachable Control Rule:** Verify that your breaking control is not a symmetry null before locking it (as occurred in `03_car_fock_loading/LI6` attempt 001 on `(0,1,2)/(0,2,1)` before switching to `(0,1,2)/(0,1,4)`).
- **Locked Baseline Reuse:** Cite `01_atoms` (`H003004`), `02_spin_memory` (`H003005`), and `03_car_fock_loading` / `03r` (`H003006` / `H003008`) as verified inputs without re-running their base scripts.

## 2. How Hard to Lean on the Native Engine vs. Host (`.venv`)
You are expected to use **both** the native engine (`./native`) and the pinned host Python environment (`.venv` with `python-flint` and `sympy`), dividing the work as follows:
- **Mandatory Native Engine (`./native`) Scope:** Every primary theorem, bound, and failing control in your lane MUST be anchored by completed native receipts. Use the native engine for:
  1. Source operator words (`GEN3_SOURCE_OPERATOR_WORD`) and exact Gram/contraction checks.
  2. Certified linear algebra (`GEN3_COMPLEX_PRODUCT`, `GEN3_COMPLEX_SOLVE`, `GEN3_COMPLEX_EXP`, `GEN3_COMPLEX_ADJOINT`, and small/bounded `GEN3_COMPLEX_RANK`).
  3. Certified logarithmic forms, traces, and entropies (`GEN5_LOG_QUADRATIC_FORM`, `GEN5_LOG_TRACE`, `GEN5_ENTROPY`).
  4. Finite-state generators, protocols, and continuum wave histories (`GEN3_MODULAR_*`, `QUANTUM_WAVE_HISTORY`).
  5. Reusable multi-step graphs (`GEN5_METHOD_ADMIT`, `GEN5_METHOD_COMPILE`, `GEN5_METHOD_EXECUTE`).
  *Target at least 4–8 completed native submissions per peer across your lane's core claims and controls.*
- **Host Python (`.venv`) Scope:** Use host scripts for fast combinatorial enumeration (e.g., the 30-path C-12 DP, 4,096-state star-layer enumeration, 51-q roster scans, or 176 reference stencils), symbolic algebra, and high-precision `Arb` quadratures—then pass the resulting exact rational/Gaussian-integer operands into native tasks to lock the certificate. Never label a host calculation as `NATIVE_CERTIFIED`.
- **Menu Visibility Note:** If a specialized menu is active, it only filters what is displayed; the engine still accepts any valid operation from the full capability catalogue.
- **Inspecting Results:** `./native show` now outputs a compact summary (omitting echoed inputs and code hashes so large payloads do not truncate before the mathematical value). Use `./native show` to read values quickly, and read the underlying receipt JSON file on disk when extracting SHA-256 hashes for your report.

## 3. Hardware, Memory & Schema Guardrails (12 GiB Cap / ~7.4 GiB Shared Working Room)
- **Protect the 7.4 GiB Working Pool:** Never submit `GEN3_COMPLEX_RANK` or `GEN3_COMPLEX_SOLVE` on dense rational matrices above `64x64` with large numerator/denominator bit-heights. Certify larger ranks via a pre-selected minor determinant, exact Gaussian-integer/modular reduction, or analytical block span. Keep host Python scripts single-threaded (`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`) and under `1.5 GiB` RSS.
- **Blacklisted Operation:** Do NOT call `GEN2_HD_PRIMITIVES` as a standalone task (the task admission check requires `source_binding`, which the operation handler then refuses).
- **180-Second Late-Window Cutoff:** Submit NO multi-step or large-matrix native tasks during the final 180 seconds of the window. Reserve the final 180 seconds strictly for readback checks, analytical proof completion, and report assembly.
- **Prechecked Payload Schemas:**
  * `GEN3_SOURCE_OPERATOR_WORD` requires exact top-level fields (`name`, `source_binding`, `context`, `data: {operators, program, output}`) with matching output basis row count (`Word output basis differs` otherwise).
  * Matrices inside a `GEN5_METHOD_ADMIT` recipe are limited to 512 entries; submit larger matrices as single operations.
  * Singular solves return `COMPLETED` with `INVERTIBILITY_UNRESOLVED` (and rank-deficient matrices may return `RANK_UNRESOLVED`); read controls by status rather than expecting `FAILED`.

## 4. Standardized Handback Format (`REPORT.md`)
Omit historical boilerplate and volume summaries. Structure your final report strictly in four sections:
1. **Executive Delta Table:**
   Columns: `ID | Vol II Ch/Sec | Exact Result or Interval | Native Key(s) & Status | Provenance (NATIVE_CERTIFIED / HOST_DIRECTED_ARB / HOST_EXACT_RAT / ANALYTICAL_PROOF) | Verdict`
2. **Self-Contained Derivations (Drop-In TeX Ready):**
   Full step-by-step proofs and equations ready for direct insertion into the Volume II TeX source, stating exact source hashes, norm conventions, and remaining physical/calibration gaps.
3. **Controls, Obstructions & Superseded Attempts:**
   Exact numerical witnesses for all failing controls, rejected shortcuts, and any caller-contract corrections.
4. **Exceptions-Only Custody Diff:**
   Concise tally of completed native tasks, superseded keys, and any `MISSING_RECEIPT` or unadmitted tasks.