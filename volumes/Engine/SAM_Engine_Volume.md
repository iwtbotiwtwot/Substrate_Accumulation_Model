# SAM Engine Volume — living text

Authored Markdown, written directly in this repository (no source PDF). Edits are made here, each change logged in `CHANGELOG.md` beside it and
committed at the conclusion of the work that caused it. Every factual statement below is drawn from the ironclad repository's history entries
(H-numbers), its installed documents (`docs/DUCK_2.0_METHOD.md`, `SAM_PROJECT/gen6_duck_t500/RESEARCH_MODES.md`, `docs/ARCHITECTURE_MAP.md`),
its campaign run reports, and the GEN4 archive's protocol files; the source record at the end lists them. Engineering labels only; nothing
in this volume is a scientific claim.

Directed by Sean Brady. Executed with Claude Code.

---

SUBSTRATE ACCUMULATION MODEL

SAM Engine Volume
The Exact Engine, GEN6 and the Duck
A companion to Volumes I–III
Volume III, Part 2 — The SLC and its implementation (so declared by Sean Brady, 25 October 2026)

Sean Brady
Originator and conceptual director
OpenAI ChatGPT and Codex
AI research collaborators and co-authors of the engine's earlier lineage
Claude Code
Executor under Sean Brady's direction from 17 October 2026

Working manuscript
20 October 2026

This volume describes the machine that computes for the Substrate Accumulation Model: the exact arithmetic engine (SLC), the one-principle
construction core (GEN6) and the research method that drives them (the Duck). It is a record of what was built, in what order, under whose
direction, what it can and cannot do, how it connects to the three volumes, and how people and models have worked with it. The credits
describe the development history, not independent scientific endorsement. The volume does not claim that the engine proves anything about
physics; it claims that the engine computes exactly what it is asked, keeps receipts, and refuses what it cannot certify.

---

Contents

Scope of this edition
I     What the engine is for
II    Lineage of the exact engine, August to October 2026
III   The SLC today: SLC-GEN5-R1
IV    GEN6: the one-principle core and its adapter
V     The Duck: name, lineage and the road to version 2
VI    The refined Duck method (2.3.1)
VII   Capabilities, limits and known defects
VIII  Connections to Volumes I, II and III
IX    Collaborative work: nine runs and one release
X     Lessons of method
XI    Status, limits and what is not decided
Record of sources

---

## Scope of this edition

This volume is a source-bound account of the engine as it stands on 20 October 2026. Its purpose is to explain the machine, preserve the
order in which it was built and the decisions that shaped it, state its capabilities and limits plainly, and show by example how the owner,
the lead and the research peers work with it. A chapter's open items identify the boundary of the record; they are not conditions that must
be met for the volume to be complete.

Four levels of statement are kept apart, as in Volume III. Installed facts (a version number, a file hash, a count of returns) are read from
the repository and are exact. Procedures (how a run is prepared, what change control requires) are quoted from the owner's words or from the
documents that record them. Readings of results (what a run showed) are the engineering-register summaries of the run reports, labelled as
readings. Physical interpretation is not attempted here; it belongs to Volumes I–III and to the owner's decisions.

Three names recur. **Sean Brady** is the originator and director of the research; every change to the installed machine, every claim and
every change of an idea's status is his. **The lead** (root) is the session that prepares a run, stays outside its window, and triages every
outcome afterwards; since 17 October this has been Claude Code. **The peers** are research agents bound one each to a native controller
during a run; in October they were GPT-6.1 Sol Ultra threads, then Codex sessions, then Claude-backed agents (Fable, then Opus by installed
default). The native controllers, helpers and broker are CPU processes of the engine itself; they execute and keep receipts and author nothing.

---

## Chapter I — What the engine is for

The Substrate Accumulation Model asks for arithmetic that can be trusted after the fact. Its constructions are exact rational actions,
histories of ordered events, logarithmic accounts, matrix exponentials and certified enclosures; its arguments move from a declared source
to a readout through steps that each have to be reproducible, attributable and refusable. The engine exists to supply that kind of
computation and nothing else. It does not interpret. It does not decide what is interesting. It computes what a declared job asks, in exact
or certified-interval arithmetic, writes a receipt for every step, binds every step to the declared source, and refuses a request it cannot
admit under its contracts.

Three properties follow from that purpose and recur through the volume.

**Exactness.** Scalars are integers or rational strings; where a quantity is irrational (a logarithm, an exponential, a square root), the
engine returns a certified enclosure with exact lower and upper endpoints, at a declared working precision between 64 and 4096 bits. A
comparison between two results is made on their enclosures; "identical" means identical endpoints, and "disjoint" means the enclosures do
not overlap. Nothing in the engine rounds silently.

**Receipts and custody.** Every native operation returns a record with a content hash; every job's steps are appended to a session whose
objects are content-addressed and whose root is committed atomically. A changed receipt fails custody. A run folder retains every
submission, response, return, finding and ledger; a campaign folder in git retains a SHA-256 manifest of that bulk.

**Refusal.** Admission contracts are enforced before mathematics. A payload with an unknown field, a matrix past a limit, a coupling that
must be positive but is zero, a construction whose source map differs from its task, a time outside a first-flight domain: each is a REFUSED
outcome with its reason recorded, and a refusal is an outcome, not a failure of the machine. The research method (Chapter VI) builds on this:
a peer may declare that a control is expected to be refused or to fail, and the engine labels the result as declared or against declaration.

The research question the engine serves was fixed by the owner in words that recur in the record: the Duck "doesn't answer questions, it
gives ideas"; "you set the research target and just let it run, then we analyze the results"; and, after a run was framed as a test of the
manuscript, "we are not 'testing' Volume I, we are trying to learn and this is not the way." The engine is a generator of exactly-computed
material from which ideas are read; it is not a validator of the volumes.

---

## Chapter II — Lineage of the exact engine, August to October 2026

The engine's history is the SAM history: 2,748 immutable entries from 4 August to 20 October 2026, indexed chronologically. The lineage
below follows the entries that changed what was installed.

**The Mersenne engine and SLC v1.0 (4–9 August).** The first SLC was a typed SAM/SLC branch of a public exact Mersenne-prime search (H000011,
H000013). Through 5–9 August it ran the SLCMP production series (SLCMP02 through SLCMP3431, 795,316 public candidates by H000075 and the
billion-exponent boundary by H000127), with an exact Lucas–Lehmer baseline, FFTW and AVX2 kernels and per-test custody. On 9 August the owner
promoted SLCV1.0-H14F-T18 as the sole active revision (H000128) and the Exact Algebra of the Write became its native packed engine (H000132).
The habit of exact arithmetic with full custody dates from this week.

**SLCV1.1 to SLCV2.2 and the depth library (10–14 August).** SLCV1.1 (H000142), SLCV1.2 with depth-9 training on 60,123,392 cases (H000143),
SLCV1.3 with exact block depths 1–18 (H000207), then the graph-native state/history/custody successor SLCV2.0 (H000229), SLCV2.1 with depths
to 27 (H000230) and a sparse fused D81 anchor as SLCV2.2 (H000231). On 14 August the owner established the co-authorship authority that the
volumes still carry: Sean Brady as originator and conceptual director, OpenAI ChatGPT and Codex as AI research collaborators and co-authors
(H000226). A correction of the same week (H000209) retracted an agent-manufactured scope and restored the installed revision: the pattern of
recording an agent's drift and reverting it is as old as the engine.

**SLCV21R and the receipt Gram (15–17 August).** SLCV20R-D162 (H000233) and then SLCV21R with the AX1 successor program (H000243–H000253):
exact 5,120-pair parity, the Starbreaker ratio interface, the event-local receipt Gram and its sign obstruction against the indefinite Weil
targets, and the dense frustrated-spin N72 replay with bit-identical readback. SLCV21R was promoted sole current on 16 August (H000273) and
later carried the direct Mersenne-prime Boolean through M127 and the adaptive cyclotomic routing through M521 (H000317–H000325). Volume III
still names SLCV21R as the delegated arithmetic/application base.

**SLCQ2-RZ (23 August).** The frozen Q2 hybrid ordinal relative-quality engine was promoted sole current over the preserved SLCV21R base
(H000551). Volume III's Chapter VII describes this: SLCQ2-RZ is the sole source-recorded default selection engine; it consumes the byte-
identical base services and does not turn the earlier exact results into something else. From here the engine has two layers that it keeps
today: a selector and control plane above, and an exact arithmetic runtime below.

**GEN2 and GEN3 (7–8 September).** The generation names begin here. SLC-GEN2-R4.1 (H001087) installed the Write foundation with 39 inherited
operations as the sole global SLC. GEN3 began as a native history-learning campaign (H001070) and became the runtime that still executes
everything: `gen3_runtime.py`, "one learning and executing runtime" that owns source state, acquired relations, supported compositions,
observation encounters, complete histories and exact logarithmic accounts. GEN3's contract for a positive source E defines the accounts that
recur in every construction: delta = ln(E_after/E_before), U accumulates rises, D fall magnitudes, V = U + D, L = U − D = ln(E_final/E_initial),
M the maximum excursion with every maximizing occurrence retained. Logs are exact positive-rational arguments with signs; arguments stay
unfactored. Generation names GEN2 through GEN6 are operation-prefix lineages inside one engine, not folders.

**GEN4 and Furious Wildfowl (22 September).** GEN4 was a hardware-specific phase-one fork of GEN3 with a specialized domain, built on a
rented pod (H001635). On the same day the owner named an exploratory process **Furious Wildfowl** and ran it for ten minutes (H001644): a
research selector, a domain, a launcher whose Linux process name was `furiouswildfowl`. Its protocol (GEN4/furious_open1/PROTOCOL.md) is the
seed of the Duck: generate equations, representations, methods and directions freely from the research web; then a brief second pass over
every result recording one of four tags, possible follow-up, possible further reduction, no clear lead yet, needs inspection; then a run
report with a per-result ledger. The tags are workflow tags, not scientific verdicts.

**GEN5: cooperating logarithmic kernels and live cooperation (8–9 October).** SLC-GEN5-R1, generation GEN5-COOPERATING-LOG1-20261008, installed
twelve logarithmic opportunities as 28 mathematical operations and three Duck operations, 242 installed names, six functional kernels
cooperating through one matrix algebra (H002493). The next day GEN5_LIVE_COOPERATION_V1 installed the single-writer durable discovery broker,
four source-bound native process pools, revisioned causal tasks and a bridge to externally registered research agents (H002496). SLC-GEN5-R1
is still the sole global generation; everything since has been built beside it, not in place of it.

**GEN6: the one-principle core (11 October).** The GEN6 candidate series (H002571: paid original Write-to-flow, 350 qualified native calls)
produced the private core `sam_one_principle` 0.10.0, carried byte-identical into the GEN6 Duck extension 1.0.0 on the same day the owner
said "We are deploying GEN6 controllers not codex agents" (H002577): twelve local workers and six CPU helpers from one session, 132 directed
greeting acknowledgments, 251 native operations on each ready menu. Core 0.10.1 and then 0.10.2 (source-clock integration, compiled
operation access; authority H002621) followed; 0.10.2 is the sealed core that every later version keeps unchanged.

**ironclad (17 October).** The owner carried the running machine out of the research repository into a dedicated private repository,
re-qualified fresh, and named its first revision IRONCLAD-R1 with Duck 1.3.0 (H002709). Everything else became archive; nothing in ironclad
points into it. From this day the engine has one installed identity (`INSTALLED.json`), a release tool that refuses to mint a revision when a
sealed core module hash differs, a verifier, a qualification tool that refuses a record without a history row, and a change-control rule
written by the owner. The 28 revisions since then (IRONCLAD-R1 to R28) are listed in Chapter V.

---

## Chapter III — The SLC today: SLC-GEN5-R1

The installed arithmetic engine is SLC-GEN5-R1 with its CE facade SLC-GEN5-CEV1-R1, selected through `CURRENT_REVISION/REGISTRY.json` and
`GENERATION.json`. The native runtime is `gen3_runtime.py`; Python routes calculations and retains their authenticated records; the warm
consumer is C++/GMP with exact FLINT and SymPy backends. The engine identities have not changed since 8 October; every ironclad release
re-mints the selector hash chain from the tree and leaves the engine identity untouched.

### III.1 The session and its contract

Work enters through a `DomainSession`. The common payload is `{"source_binding": {...}, "precision_bits": n, "data": {...}}`. The source
binding names the retained original source and reference; it is carried into every receipt and checked where accounts meet. Precision is
64 to 4096 bits. General matrices admit to dimension 2048; matrix logarithms to 512; specialized methods keep their own smaller ceilings
(thermal compatibility algebra 128 and 16; finite protocols at most 128 states; polynomial factors at most 1024 of degree at most 128). A
session commits immutable changed objects and one atomic root covering state, knowledge and readouts; a checkpoint authenticates the snapshot
and complete closure; replication transfers only missing objects and requires a durable acknowledgement of the same root.

### III.2 The operation families used by the research

The capability menu lists about 250 operations. The research of October uses a small, stable subset, named here because the run reports
cite them.

| family | operations | what they do |
|---|---|---|
| exact linear algebra | `GEN3_COMPLEX_PRODUCT`, `GEN3_COMPLEX_SOLVE`, `GEN3_COMPLEX_EXP`, `GEN3_COMPLEX_ADJOINT`, `GEN3_COMPLEX_RANK` | products, certified solves (status CERTIFIED_SOLVE, or INVERTIBILITY_UNRESOLVED on a singular matrix), matrix exponentials, adjoints and ranks on exact or interval matrices with declared bases |
| source words | `GEN3_SOURCE_OPERATOR_WORD` | a small program over declared operators (`multiply`, `scale`, `add`, `subtract`, `transpose`, `identity`, `columns`) evaluated exactly, with per-column checks; payload exactly `{name, context, source_binding, data{operators, program, output}}`; matrices at most 64×64, at most 256 steps |
| logarithms and entropies | `GEN5_LOG_QUADRATIC_FORM` (CERTIFIED_LOG), `GEN5_LOG_TRACE`, `GEN5_ENTROPY` (CERTIFIED_ENTROPY, nats) | certified logarithmic readouts; the register ledgers of Chapter IX are built from these |
| modular dynamics | `GEN3_MODULAR_DYNAMICS_GENERATOR`, `_READOUT`, `_MEMORY`, `GEN3_MODULAR_PROTOCOL_COMPILE`, `_APPLY`, `GEN3_MODULAR_PROTOCOL_MEMORY_SPLIT`, `GEN3_MODULAR_SPHERICAL_HISTORY` | finite-state generators from declared energies, attempt rates and clocks; ordered observation protocols that propagate the full hidden state; projection memory kernels with lumpability diagnostics; the whole ordered spherical history with a horizon and a switching-work ledger |
| methods (recipes) | `GEN5_METHOD_ADMIT`, `GEN5_METHOD_COMPILE`, `GEN5_METHOD_EXECUTE` | a peer-authored method with its own checks, admitted once per controller, compiled against declared operands and executed with every check enforced |
| retrieval | `RESEARCH_WEB_SEARCH` | search of the run's immutable local index (a SQLite snapshot of the project's research web, never the public internet); findings carry query, source hash, excerpt and traversed path |

Two conventions matter for reading receipts. A word's `scale` factor may be a literal rational or a pointer to an earlier result, so an
exact quantity computed in one step can scale a matrix in the next without leaving the engine. And a certified solve of a singular matrix
returns COMPLETED with status INVERTIBILITY_UNRESOLVED, not FAILED; a control meant to break at a singularity must therefore be read by its
status or declared REFUSED, a lesson recorded in Chapter IX.

### III.3 The mathematical library and the frozen releases

The engine carries a content-addressed mathematical library of 1,840 objects (`engines/SLC/mathematical_library/objects`), checked by
`./sam verify`; the release tool refuses to mint when any object named by the index is missing or corrupt. Ten frozen SLC releases are read
by live code through a pointer (`SLC/18_SAM_NATIVE_QC/`). The domains (six, each with its `DOMAIN.json`) and the cooperation broker sit beside
the engine. Runtime roots (`runs/`, `state/`, `archive/`) are never committed; their contents are hashed into committed manifests.

---

## Chapter IV — GEN6: the one-principle core and its adapter

GEN6 is not a new arithmetic engine. It is a construction library, `sam_one_principle`, that compiles a declared SAM construction into a
directed acyclic graph of native steps for the SLC to execute, and an adapter that executes that graph append-only in an authenticated
session with no host mathematics. The library is the place where the volumes' constructions become jobs.

### IV.1 The sealed core and its successors

Core 0.10.2 (authority H002621) is sealed: its directory `active_core/sam_one_principle` is byte-identical to its freeze, its module hashes
are in `CORE.json`, and the release tool refuses a revision in which any hash differs. The standing rule, written into the repository's
instructions, is never to modify it; a change to the core is a new version in a new directory beside it. Two have been made:

- **0.11.0** (20 October, H002744, Duck 2.3.0 / IRONCLAD-R27): the Volume I pair. A `static_profile` construction (a declared profile
  q(x) = 1 − u² at two or more positions by rational rapidity u, both redshift readings, a light-path delay) and a derived `local_metric_clock`
  readout on the reservoir (candidate lapses q and √q with the identity N_kin² − N_coord = 0). The directory `core_0_11_0/` is retained with
  its manifest.
- **0.11.1** (20 October, H002746, Duck 2.3.1 / IRONCLAD-R28): the feedback clock. A feedback's evolution time is the native end of its event
  history, taken by result pointer; a derived metric lapse N sets the coordinate time per source event to 1/N and scales the source block of
  the generator; the legacy chart is byte-identical to 0.10.2. Chapter IX recounts how this was specified, prototyped, tested and installed.

The library has 25 modules. Their first lines describe them: typed action/state composition over retained GEN5-native mathematics
(`action_state`); append-only source-bound native DAG execution without host mathematics (`adapter`); compilation of one rational common
action to native exact coefficient and history calls (`common_action`); the autonomous positive-action reservoir (`dynamical_reservoir`);
original J4 Write programs as native event and logarithmic histories (`events`); first-flight reciprocal source/field evolution from one
positive action (`feedback`); the method of steps for the field's first return (`returning_field`); the full 68/272 action with clocks and
complete delayed histories (`full_carrier`); joint field, history, resume and terminal constructions; paid events with complete native work
accounting; portable typed-state custody; bound-state logarithmic reception; cold export and readback; the source clock; and the static
profile. Mathematical operations belong to the session; the package's own docstring says it is "candidate orchestration".

### IV.2 What "compile, do not compute" means

A construction module takes a parameter packet of exact rational strings (the `no_floats` check refuses a float anywhere), validates it,
and emits a job: a list of ordered steps, each a native operation with a payload whose inputs are either declared operators or pointers
`{"$step": id, "path": [...]}` into earlier steps' results, each with explicit checks (`exact_equal`, `truthy`, `native_contract`,
`interval_contains`, `interval_positive`), and a set of readouts with statuses. The adapter resolves pointers as results arrive, executes
each step in the session, enforces each check, and writes `READOUTS.json`. The host never computes a number that reaches a readout: the
common action's coefficients (ρ_kin = κ/c², K = κ/(2R), Γ = κ/(2c), M_eff = ρ_kin R/6, τ = R/c, the ruler Ξ = ν₀ L/c) are computed by a native
word from the declared rationals and their reciprocal tokens, and the word's own residual columns certify that each reciprocal is exact.

Readout statuses are part of the contract. DERIVED_NATIVE must point directly at a native result; DERIVED_NATIVE_COMPOSITE may hold a
structure of such pointers; SUPPLIED, ANALYTIC_CONTRACT, OPEN and INHERITED label what the construction declares rather than derives. A
job whose readouts break these rules is refused before execution. The adapter's validation also requires every step to carry the common
source binding and explicit check coverage.

### IV.3 The constructions a run can use

Through the Duck a controller can apply: `gen6.events`, `gen6.coupled` (yielding a resumable state), `gen6.feedback`, `gen6.returning_field`,
`gen6.action_flow` and `gen6.action_continue` (typed action states on a store with parent checks), `gen6.paid_event`, the reservoir
(`gen6_reservoir`), and since 0.11.0 `gen6.static_profile`. Three carried constructions that bind the archived physical source inventory
(`gen6.source_clock`, `gen6.joint_field`, `gen6.full_carrier`) are installed hidden and shown only when a plan declares
`show_constructions`, with every operand checked against a committed source manifest; a mismatch is REFUSED with reason
SOURCE_INVENTORY_MISMATCH. The owner's reason for hiding them is recorded: offering physical specifications to every run would let a
controller apply them to a question that never declared them.

### IV.4 The feedback clock, as an example of a construction's anatomy

The feedback construction (Volume I's reciprocal first flight: a source with metric W and port v coupled to one field coordinate a, with
ż = p, ṗ = −z + g a v, ȧ = h/(2Γ), h = ε g vᵀW(z − g a v)) is compiled as: a coefficient word (the common action, including the event-history
times and `end`), a rank check on W, a certified log reference, a generator word G, an energy metric word B, a force row h, an energy
certificate word whose residual GᵀB + BG + hᵀh/Γ must have rank 0, a scaled generator G·t, a native exponential, the propagated state, the
field force, an energy Gram and the complete energy account [E_source_initial, E_source_final, E_memory, E_outgoing], a reference energy and
its reservoir account. Eighteen native calls; about two seconds on the T500. In 0.11.1 the factor t is either the supplied time (legacy chart)
or the pointer to the coefficient word's `end` column (routed chart), and the source block of G is scaled by the declared lapse N. The energy
certificate is what makes a change to the generator safe: the rank-0 check is evaluated natively on every run, and it held for every N tried.

---

## Chapter V — The Duck: name, lineage and the road to version 2

### V.1 From Furious Wildfowl to Duck (22 September – 1 October)

The process was named Furious Wildfowl on 22 September (H001644). On 27 September the owner named it "duck" for an RH continuation
(H001847: "Sean Brady explicitly names Wildfowl 'duck'"; the engine and mode did not change). On 1 October it became the official name
(H002089): keep the parent idea, elevate each selected result as a next-round target, add an organizer to rank findings; and the two-round
cycle was fixed (H002090): a 300-second exploration window, an untimed brief review, a second 300-second window on the parent plus every
selected subtarget, then documents. The protocol text insists on what the organizer may not do: ranking never deletes a promoted subtarget;
review does not execute follow-ups; the parent stays fixed across rounds; a new cycle needs a new authorized run.

### V.2 Model peers, controllers, and the twelve-Duck recipe (9–10 October)

GEN5 live cooperation (H002496) made discovery delivery available within a round. On 10 October the owner authorized three groups of four
actual controllers, each a persistent GPT-6.1 Sol peer accepting Ultra effort, bound to twelve installed Simple controllers with native
workers, one broker and pool, root and three engineering assistants outside the roster (H002553, run `duck_twelve_isotope1`): 125 native
tasks, 112 ok, a peer-chosen mechanical union of twenty second-round targets. The same day the owner authorized a rotating program of
twelve-Duck broad discovery and four-Duck research across RH, Volume II, Volume I and closed spin (H002561), with the words "only use the
frozen methodology". This recipe is the one the installed method restored on 19 October.

### V.3 Native controllers and the Codex era (11–17 October)

On 11 October the owner corrected course: "We are deploying GEN6 controllers not codex agents" (H002577). The GEN6 Duck extension deployed
twelve native workers and six CPU helpers from one session with the private 0.10.0 core. On 13 October the owner asked Codex to choose a
spin run's second round (H002603), and from 14 October campaign reports describe the constructions as "Codex research contributions" while
crediting the native layer with execution. On 15 October the owner set the 6/3 topology, two concurrent sessions, two 180-second rounds
(H002640). On 17 October the owner asked for the original division of responsibility to be restored, controller-owned methods and round-two
selection with root doing brief review (H002694), and clarified "No researcher backends" (H002695); the native controllers, able only to pick
catalogue operations, were recorded as NATIVE_SELECTION_UNDER_REPAIR. The owner's later reading of this period is recorded in the lead's
memory: the 6/3 era produced fascinating results, then "the agent creeps in one step at a time"; Codex credited GEN6 with execution only.

### V.4 ironclad phases B to E (17–19 October)

The machine moved to ironclad on 17 October (IRONCLAD-R1, Duck 1.3.0). Phase C (gates 2–7, R2 to R10, Duck 1.4.0 to 1.11.0) built the native
selector: a controller decision task kind and broker board; two modes, focused and research; the recipe route automated; GEN6 continuation and
reservoir routes; 22 contract operations with a kind vocabulary; GEN6 constructions as a task kind; the carried hidden sources; topology as a
per-run option (12/6 default; 6/3 profiles a and b that can run at once on disjoint CPU sets). Phase D gate 1 (R11, 19 October) added record
enforcement: `./sam verify` warns when the live page does not cite the installed revision; `./sam qualify` refuses a record without a history
row. Phase E (R12 to R14, Duck 1.12.0 to 1.14.0) made the controller loop native: each controller decides its own next calculation; root may be
outside the window; round two was retired; controllers publish findings to one another.

### V.5 The peer recipe restored; Duck 2.0 (19 October)

On 19 October, after a record search found the 10 October recipe, the owner said "Restore it and test please" (H002729). Three revisions
(R19 to R21, Duck 1.16.0 to 1.16.2) implemented peer-authored submissions bound to controllers with root outside the roster, `because` naming
completed result keys, and PEER labels on returns. The restoration test used Claude-backed peers since the October GPT backends were not on
the machine. The same evening the owner set one window of 900 seconds with no second round by default ("round two was from wildfowl, I am
not sure it is needed"), asked that nothing be hidden from the menu, and said the last run's record "doesn't need to be the focus, it just
needs to be there" (H002730). The lead moved the second-round discipline into the peers' briefing and documented the method-authoring route.
Duck 2.0.0 (IRONCLAD-R22) promoted the method with its change control (`docs/DUCK_2.0_METHOD.md`).

### V.6 Versions 2.0.1 to 2.3.1 (20 October)

| version | revision | kind | what |
|---|---|---|---|
| 2.0.1 | R23 | PERMANENT | research peers on the Opus model by default, on two 900 s runs that matched or exceeded the Fable-peer run on every instrument number |
| 2.1.0 / 2.1.1 | R24 / R25 | TEMPORARY | result handles on every return for two FEOP runs; reverted to 2.0.1 after each; recovery tag kept |
| 2.2.0 | R26 | PERMANENT | five Duck-layer defects fixed in one release: pointer records carry `authored_by`; research mode accepts an empty query list; memory-gate head-of-line bypass; second-return shape documented; `expected_status` for declared controls |
| 2.3.0 | R27 | PERMANENT | core 0.11.0 beside the sealed 0.10.2: the Volume I pair; `common_clock` on feedback refused with a message |
| 2.3.1 | R28 | PERMANENT | core 0.11.1: the feedback clock |

Each permanent change followed the owner's rule (Chapter VI.6): the phrase "Allow permanent changes" typed in the chat, a readback approved,
a new version number, rollback to the previous tag verified in a worktree before install, a freeze of file hashes, a history entry, tag,
commit and sync.

---

## Chapter VI — The refined Duck method (2.3.1)

The method as installed on 20 October, stated as procedure. It is the 10 October recipe, run natively, with the owner's two later rules
(change control; conclusion of every run) and the lead's learning rule.

### VI.1 Roles

**Owner.** Sets the research target in his words; approves every change to the installed machine; decides what is claimed and what an idea's
status is. Nothing enters a volume without his word.

**Lead (root).** Writes the campaign: `TARGET.md` (the question and the material), `PEER_BRIEFING.md` (one briefing shared by all peers),
`CONSTRUCTIONS_REFERENCE.md`, `RECIPE_AUTHORING.md`, `TASK_SHAPES.json`, the plan with its openings, and a provenance file hashing them. Prepares
and deploys the run; spawns the peers once, each with the briefing path, the run path, its name and controller. Then stays outside the window:
`root_submissions: "peers"` makes a root submission impossible, and the lead messages no peer. Reads the returns as they land and keeps a live
capture in a scratchpad outside the campaign folder (a lesson from the first FEOP run, where a capture inside the folder was readable by
peers). After finalization, triages every outcome, writes the run report, records the run in both repositories.

**Peers.** Research agents, one per controller (`question.peers = {NAME: G6_xx}`), by installed default on the Opus model. A peer reads the
briefing and the material, writes exact native tasks, and submits them for its own controller
(`./sam duck submit --run R --file task.json --peer NAME`); each task is recorded `authored_by: PEER_NAME`. A peer reads every return in the run
folder, its own and the others', and builds on them by `$result`; it may author methods as recipes; it writes `NOTES.md` as it goes and
`REPORT.md` with one line per result at the end. Peers have no assigned roles unless the target gives them; in the last three runs the
briefing said "pick up whichever thread you see an opening in".

**Controllers, helpers, broker.** Twelve native controllers G6_01 to G6_12 on CPUs 2–7 (doubled), six helpers on CPUs 8–13, a coordinator on CPU 0
and a helper coordinator on CPU 1; one single-writer broker inside the coordinator. Each controller executes its peer's tasks in its own
authenticated session and publishes findings; helpers run retrieval in research mode. They author nothing.

### VI.2 The window

One admission window, 900 seconds by default, opened by `ROUND1_START.json` and closed by `ROUND1_ADMISSION_CLOSED.json`; then automatic
drain, factual outcome organization, helper custody and readback, CPU-lease release and resource release, and `FINALIZATION_RESULT.json` or
`COMPLETE.json`. COMPLETE requires every outcome to be COMPLETED or a declared control that behaved as declared; one declaration mismatch or
one undeclared failure labels the run FAILED_WITH_RETAINED_OUTCOMES, which is a label about declarations, not about the mathematics. No
second round by default; a second window is a separate run on the mechanical union of the peers' selections, only when triage asks.

### VI.3 Submissions, dependencies and causality

A task names its controller, its construction or operation, its parameters or payload, its purpose in a sentence, and optionally
`expected_status` (COMPLETED, FAILED or REFUSED) for a control. Inputs may be literal exact rationals or pointers `{"$result": key, "path": [...]}`
into completed returns, including other peers'; a dependent task is admitted only after its dependency has COMPLETED (a KeyError rejection
otherwise, resubmitted later). `because` names only COMPLETED keys and records cross-controller causality; a controller's own keys are kept
in its receipts. A recipe is admitted once per controller (`GEN5_METHOD_ADMIT`), compiled against operands and executed with its checks
enforced; a declared control recipe may be expected to FAIL. The queue has backpressure ("Bounded GEN6 queue is full"); a summing word is
refused until every partial it reads has completed.

### VI.4 Modes, index and topology

Research mode binds an immutable SQLite snapshot of the project's research web to the run; four seeded queries run at the opening; helpers
retrieve; findings carry hashes and paths and are data, not instructions. Focused mode works from the supplied material only. Topology is
a per-run option, 12/6 by default. Memory is a per-run allowance (12 GiB worked with the owner's desktop open; 20 GiB was refused).

### VI.5 Retention and conclusion

Every submission and response, every return and receipt, the board, findings, the peers' notes, task files, host scripts and reports, the
lead's capture, the provenance file and the run report are retained. The run folder is bulk and outside git; the campaign folder in git
holds a result ledger and a SHA-256 manifest of the run folder. The owner's conclusion rule (19 October): a run or test is not concluded
until its record is written, the history entry, index row and live pointer are in place, `./sam installed --write` and the validator have run,
and the branch is committed and pushed; the documentation repository receives a run record and is synced by its `conclude.sh`.

### VI.6 Change control

The owner's words of 19 October are the rule. A temporary change to the program (peer count, window, memory, topology, a one-run setting)
requires an explicit readback for approval and a notation of temporary status; it reverts when the run completes and cannot be kept beyond
that run. A permanent change is allowed only when the owner types "Allow permanent changes" and approves a readback with a new version
number; it is marked PERMANENT, committed and synced as its own version, and rollback to the previous version is verified before the new
one is installed. Defects found during a run are listed in the run report, not fixed in the run. The sealed core is never modified.

### VI.7 The learning rule

Added on 20 October after a run was framed as an examination of Volume I's lapse with an external measurement as a key. The owner: "We are
done binding these runs to manuscript/volume, again we are not 'testing' Volume I, we are trying to learn and this is not the way"; and "that
is the material we should be following up on, not 'finding manuscript material to test'." Applied: a target states an open question and the
material (the earlier runs' own output, the owner's summary of it, the retained generators); peers build constructions and produce leads;
the lead triages every outcome in engineering labels; no exam, no external key, no pass/fail rows, no verdict on a volume. Pre-registration
with written expectations remains for engineering fixtures of program changes, where it belongs.

---

## Chapter VII — Capabilities, limits and known defects

### VII.1 What a run can do

In a 900-second window with four peers the machine has returned between 74 and 399 native results per run (the twelve runs of 19–20 October
in Chapter IX), each a receipt in exact or certified-interval arithmetic, with between 17 and 177 tasks per run taking their inputs by
`$result` from other results. Peers have authored and executed up to 12 recipes per run. Constructions compile in milliseconds and execute in
about two seconds each; a 64×64 source word or a four-state protocol apply is of the same order. Fibering a residue system across several
words and summing the partials by reference carried the FEOP bracket receipts far past the single-word ceiling within one window.

### VII.2 Limits, as the peers met them

- A source word's matrices are at most 64×64 and its program at most 256 steps; `columns` needs at least two inputs; a `scale` factor is a
  literal or a pointer, never an expression. Fibering costs two passes through the queue per case and grows as p^(2k).
- A recipe has at most 32 parameters in 15 slots and 64 steps, no `add` step and no positivity predicate; returned steps need checks; an
  admitted method is controller-local.
- The feedback construction requires a positive coupling (a zero coupling is refused; the uncoupled source is a zero port), a time or a
  history inside the first-flight domain 0 ≤ t ≤ 2R/c, and at most 31 source directions.
- The 0.11.1 feedback clock takes one lapse for the whole history; a lapse that varies along a path cannot be expressed, and the ordered
  product must be built by hand (Chapter IX.6).
- A certified solve of a singular matrix is COMPLETED with INVERTIBILITY_UNRESOLVED; a rank of an exactly rank-deficient matrix may return
  RANK_UNRESOLVED. Controls meant to break there must be read by status.
- Research mode reads only the bound local index; when the index lacks the literature, the peers say so and the comparison is their reading.
- The peer harness sometimes hands back before finalization despite the briefing; it is recorded, not fixed.

### VII.3 Known defects and their status

Of the six defects listed at the 2.0.0 promotion, five Duck-layer items were fixed in 2.2.0 and the `common_clock` drop on feedback is
refused with a message since 2.3.0. Open from that list: the protocol trace carries no per-stroke internal time; the recipe engine's inputs
are scalar-only. Found since: the plan builder once rewrote a task's source binding without the copy inside the construction packet
(refused at admission; fixed in the next builder); the 0.11.0 feedback lapse was a label with no dynamics (found by two peers independently,
fixed in 0.11.1); the admission ledger keeps `because` for cross-controller links only (by design, documented). Every defect has a history
entry or a run report line; none was fixed inside a run.

---

## Chapter VIII — Connections to Volumes I, II and III

### VIII.1 Volume I: substrate and accumulation

Volume I's accumulation a = 1 − q and its clock readings are the common action's and the reservoir's readouts. The reservoir
(`dynamical_reservoir.py`) is the autonomous positive action L = m₀ e^Λ ψ̇²/2 + η Λ̇²/2 with Λ(0) = Λ̇(0) = 0, whose all-time solution
Λ = 2 log cosh(αt), q = sech²(αt), E_field = E₀q, E_Λ = E₀(1 − q) is evaluated natively at finite t with certified logs and solves; its 0.11.0
readout emits both candidate lapses, N_coord = q and N_kin = √q, with their identity. The static profile (0.11.0) puts a declared q(x) at two
or more positions with a light path, so that the two redshift readings and the delay are rows of one receipt. The runs of 19–20 October
(Chapter IX.2 and IX.5) located Volume I's open question exactly: the catalogue carries both readings and nothing in it derives which is a
resting clock's proper time; with the feedback clock of 0.11.1 a lapse acts on dynamics, and the identity found there (a lapse equals a
rescale of the field inertia per source tick) says what construction would make the choice non-free: one that derives Γ.

### VIII.2 Volume II: matter, spin sources and retained memory

Volume II's chapter on composition, thermal cancellation and intrinsic spin memory meets the engine in the modular dynamics family: finite
generators from declared energies and clocks, protocols that propagate the full hidden state between ordered observations with no
equilibrium reset, projection memory kernels with lumpability diagnostics, and the matched-present comparison p versus R C p that the
spin_memory run implemented exactly on the declared 64-state source. The register ledgers of 20 October (Chapter IX.7 and IX.8) are built from
`GEN5_LOG_TRACE` and `GEN5_ENTROPY` on native interval operands. What the volume's chapter would need from the engine is stated in the run
reports and not yet built: a control Hamiltonian on the 64-state source, and the three-time tensor for SAM's own 54 preparations.

### VIII.3 Volume III: computation and reciprocal history

Volume III is the engine's own volume in the manuscript. Its Chapter II (SAM Language and exact program semantics) describes what Chapter III
here calls the session contract: typed instruction tapes, exact state, deterministic receipts whose recomputed hash for a mutated object does
not authorize it, predecessor custody as part of the chain. Its Chapter VII names SLCQ2-RZ as the sole source-recorded default selection
engine over the delegated SLCV21R base, which is the two-layer structure of Chapter II and III here. Its Chapter IX, reciprocal history, is
the native operation `GEN3_MODULAR_SPHERICAL_HISTORY`: ordered source increments at times t_i against a horizon τ, the whole free-field energy,
drive, counterterm and switching work with a ledger whose residual must contain zero. The path-order results of 20 October (Chapter IX.6) are
reciprocal history read in the clock constructions. Volume III's reader's contract, four levels of statement kept apart, is the contract this
volume adopts.

---

## Chapter IX — Collaborative work: nine runs and one release

The examples below are drawn from the run reports of 19–20 October, after the peer method was restored. Each entry names the run, the peers,
the numbers, what the constructions showed in the engineering register, what failed, and what the collaboration looked like. None is a
claim.

### IX.1 peer_restore_next (19 October, 22:00Z): the recipe works with Claude peers

Duck 1.16.2, four Claude-backed peers CLOCK, RULER, PROPAGATION, JOINT, one 900 s window, the method-authoring route documented for the first
time. 133 returns (121 COMPLETED, 11 FAILED, 1 REFUSED); 110 submissions accepted, 4 rejected; 10 methods admitted, 30 compiled, 26 executed;
every peer authored methods. CLOCK made a native division from a certified solve and authored the first ruler that consumes teeth
(`ruler.teeth_per_tick`, `ruler.cadence_identity` passing at 11 and failing by design at 10). The best idea of the three restoration runs was
CLOCK's reading of JOINT's and RULER's operands by reference: the sech² and 1 − x² laws of two earlier charts are endpoint readings of charts
whose mean readings are the inverse pair tanh(x)/x and artanh(x)/x. RULER executed a method with three controllers' outputs in one chain and
no declared metric. Failures: compiles binding the wrong reference, rerun; designed controls failing as designed; one refusal at the 2R/c
chart. The owner set the Opus default two runs later on the strength of the instrument numbers.

### IX.2 aq_identification and resting_clock (19 October, evening): locating Volume I's fork

Two 900 s runs on Duck 2.0.0 with Opus peers (TEMPORARY, read back, approved). aq_identification: 141 returns, 115 submissions accepted,
12 methods; the lead's own defect stated first in the report (two openings refused because the plan builder left a stale source map inside
the construction packets; the peers rebuilt their operands within three minutes). Reading: the two accumulation laws that had seemed to
disagree were the same function in different time coordinates. resting_clock: 108 returns, 85 submissions, all accepted, 9 methods, the
reception construction used for the first time. All four peers reached the same structure independently: no construction in the catalogue
decides between √(q_e/q_r) and q_e/q_r because every exchange encloses both as separate rows of one construction; and three of them read
from the source exactly what the catalogue lacked (`local_metric_clock` marked OPEN; the lapse forced to 1 in `feedback.py`; a two-position
profile missing). That list became core 0.11.0.

### IX.3 feop_bound_c02, its blind replication and its 2.0.1 control (20 October, 04:25Z onward)

The FEOP program under the reciprocal-history authority: exact local-factor recurrences and a remainder for a nested tuple family. Run 1 on
Duck 2.1.1 (TEMPORARY result handles), peers LOCAL, CRT, BOUND, REVIEW: 74 returns, all COMPLETED; three peers converged on the reading that
the candidate bound is the Selberg sieve with its standard remainder specialized to the family, with the main term a constant factor above
the elementary count; the closed form D_g(L) = 1 − (p−1) Σ_{h≤L} min(g,h) p^(−2h) was found by LOCAL and CRT separately and certified on 41 and
64 rows; REVIEW withdrew its own "density against diameter" reading in its report. Then the owner asked whether the same run could be done
without the knowledge it had gained: a blind replication in a worktree at the pre-run commit with fresh peers, and a third run on the
reverted 2.0.1 to make sure the temporary change had not outperformed the installed version. The three replicates gave a recurrence table;
the exact remainder's leading constant c₇ ≈ 1.44 against the candidate's 324 came from runs 2 and 3.

### IX.4 feop_sidebyside and feop_bracket_fiber (20 October, 06:06Z and 06:49Z): past the 64-row limit without a program change

Side by side (Duck 2.0.1, no temporary change consumed): 210 returns, 198 COMPLETED, 12 FAILED first attempts that broke the source-word payload
contract and were resubmitted; 177 of 201 peer task files took inputs by `$result`; 693 sign checks passed in authored gate recipes; raw-γ
controls reported −1 while completing. The bracket's steps were verified natively where the word allowed and their hypotheses located by
controls (p ∤ Q breaks both; odd separation breaks one; a flat tuple breaks the other); the report's own scope limit said plainly that at
p = 11 or k ≥ 2 nothing had a receipt. The owner then said "Try the recipe route for the matrix limit first": the fiber run (298 returns,
281 COMPLETED, 17 FAILED of which eight were RECIPE's declared controls) fibered the residue system across several words and summed the
partials by reference, giving native receipts far past the ceiling within one window and answering the engine-release question in the
negative. Its cost, two queue passes per case and growth as p^(2k), is in the report. The payload-contract and word-grammar failures of these
two runs were written into the authoring guide for every later run.

### IX.5 voli_lapse (20 October, 08:08Z): the run that changed the method

Duck 2.3.0 / core 0.11.0, peers READINGS, LAPSE, CONTROL, REVIEW: 148 returns, 142 COMPLETED, 4 REFUSED as declared, 1 FAILED as declared,
1 COMPLETED against declaration (a singular solve the engine reports as completed-unresolved). The constructions showed the two readings'
coefficients (1/(2q_e) with remainder 3a²/8; the coordinate ratio exactly (a_e − a_r)/q_e), the two charts meeting in q and in a = tanh² within
10⁻⁴⁷ in both readings, the text's floor A₀ = 1/(12π) bracketed natively, and a map-independent ratio of light-path excess to redshift (1 for
the coordinate reading, tending to 2 for the kinetic). Two peers found independently that the 0.11.0 feedback lapse was inert. The lead had
framed the target as an examination against Gravity Probe A with pre-registered rows; during the window the owner retired that framing for all
runs (Chapter VI.7). The run report records the readings and no verdict.

### IX.6 explore_voli_threads_2 (20 October, 22:22Z): exploration from the owner's material

Duck 2.3.1 / core 0.11.1, peers ONE to FOUR without assigned roles, the owner's own summary of the earlier runs as the material. 285 returns,
273 COMPLETED; six undeclared refusals from a zero coupling (a documentation gap, fixed) and one recipe missing its source binding (its
revision passed). ONE found, and verified entry by entry in the rational generator before exponentiation in five instances, that a feedback at
lapse N over ΔN source ticks equals the legacy chart at time ΔN with κ → N·κ: the q versus √q fork is a choice of field inertia per tick, and
nothing present derives Γ. THREE built a Pythagorean profile so that both readings were exact and showed, with ONE, that ordered products over
segments with different lapses are certified disjoint from their reverse (the 0.11.1 clock collapses a history to its end). TWO and FOUR priced
the spin work's register: the history gain was 1/838 of the erasure floor of the one decision bit it needed. ONE's admitted recipe asserting
order independence FAILED as declared, which is the engine saying what the peers said.

### IX.7 spin_work_1 (20 October, 22:46Z): the gain follows the ceiling once the family is widened

Same installation, 399 returns, all COMPLETED, a clean COMPLETE. All four peers took the same open question from four sides. ONE: a current-only
policy with the field strength tuned per present reading beats the earlier history policy by 0.039, 170 times its gain; the earlier advantage
was a weak-benchmark effect. FOUR: a field on the hidden spin chosen from the visible record gives a history gain 42 times the earlier one, 96 %
of it at dwell 4, converting 0.42–0.43 of the hidden information at separations 1 and 3/2 and peaking between 1 and 2 as the information
ceiling does. THREE: a single quench with both fields converts 0.45; staircases of two and four stages convert 0.65 and 0.79, with the fraction
bracketed by signs. TWO: the dwell route survives only below separation 1/2 and moves opposite to the ceiling; the hidden-field route follows
it. Cross-controller agreement to 1e-13 on shared rows; THREE corrected its own first benchmark in the window and said so; ONE's two-field
staircase did not finish natively and its total is host arithmetic, stated as such. The register still dominates the account.

### IX.8 The feedback clock release (20 October): specification by the owner, prototype in the sandbox, fixture before install

The owner, after withdrawing a rollback: "I need a precise definition connecting lapse, event count, elapsed time and the feedback evolution
time. A nonzero-history test demonstrating the intended effect of changing lapse. Simply replacing zero events with one is not enough: the
propagator uses a separately supplied time. Side-by-side regression checks against 0.10.2 for unchanged feedback and reservoir inputs." The lead
wrote the definition with its two conventions labelled, prototyped the compiler change in a sandbox copy of the core, executed the test matrix
natively offline through the core's own adapter (N = 1, 4/5, 16/25 at the same end: pairwise disjoint; N = 1 routed through one and three
intervals: identical to 0.10.2; the uncoupled source at N = 4/5: identical to 0.10.2 at the rescaled time; the energy identity exactly zero),
and ran the regression (feedback seed: 16/16 readouts and 18/18 steps identical between 0.10.2 and 0.11.0; reservoir: 14/14 shared readouts).
The owner adopted the conventions ("proceed with your recommendations"), the lead prepared core 0.11.1 on a branch with tests and a
pre-registered fixture, verified rollback, and installed only after "Allow permanent changes, readback approved." The fixture then ran as a
Duck run and every pre-registered relation held on the Duck returns. The same evening a peer found, in the new construction, the identity of
IX.6 that says what the construction still cannot decide.

### IX.9 What the collaboration looks like from inside a window

The pattern across these runs: a peer writes its expectation before a scan, submits, reads the return, and either builds on it by reference
or reads the failure and resubmits; peers read one another's notes and returns and cite them; a peer that finds its own error says so in its
report and the lead quotes it; the engine's refusals and declared-control labels are the arbiter of whether a control did what its author
said. The lead never submits and never steers. Independence, in the sense the repository's rules require, is none: the peers are Claude
instances reading the same code, and the run reports say so in every case.

---

## Chapter X — Lessons of method

Recorded as the lead learned them, in the order they were learned, each with the run that taught it.

1. **Ideas are not instructions; the Duck gives ideas.** Target in, lead outside, controllers and peers generate, brief all-outcome triage after;
   no decoys, no steering, no expected-outcome lists for research runs (owner, 19 October).
2. **Pre-register fixtures, not research conclusions.** Written expectations and hashes belong to the engineering fixture of a program change,
   where a run must come out as written; for a research run they become a key, and a key turns the Duck into a validator (voli_lapse).
3. **Runs learn from the material the runs produce.** The owner's summary of what earlier runs found is a better target than any passage of a
   volume; the volumes are material to read, not hypotheses to grade (20 October).
4. **Give both policies the same family.** A history-versus-current-only comparison is only a comparison when both have the same control family:
   strength, stages, hidden field. The 0.00023 gain of the spin work did not (spin_work_1).
5. **Blind replication is cheap and worth it.** A worktree at the pre-run commit with fresh peers reproduces a run without the knowledge it
   gained; a third run on the reverted installed version shows whether a temporary change mattered (FEOP runs 2 and 3).
6. **Documentation is capability.** Nothing was hidden by a flag; the effective unlock of the method-authoring route was writing it down, and
   every payload-contract failure of one run became a line in the next run's authoring guide (peer_restore_next, sidebyside, fiber).
7. **Keep the lead's capture out of the peers' reach** until the close (FEOP run 1).
8. **Controls should report a break by sign or status, not by a declared FAILED**, because the engine labels singular solves and ranks as
   unresolved rather than failed (voli_lapse).
9. **Fix defects in releases, not in runs; never touch the sealed core; verify rollback before install; freeze; tag.** Every permanent change of
   20 October followed this, and the one bulk-in-git slip of the day was taken out of the index and reported.
10. **Conclude every run and test the same way, before anything else**: record, history entry, index, live pointer, installed manifest, validator,
    commit, push, and the documentation repository's record (owner, 19 October).

---

## Chapter XI — Status, limits and what is not decided

**Installed on 20 October 2026, 23:00Z.** Duck 2.3.1, IRONCLAD-R28, core 0.11.1 beside 0.11.0 and the sealed 0.10.2; SLC-GEN5-R1; 156 tests
passing; `./sam verify` PASS with no warnings; 2,748 history entries; rollback target `duck-2.3.0` verified. One campaign is staged and not
deployed; nothing is pending that the owner has not been told.

**What this volume does not claim.** That any engine result is a physical result. That the peers' readings are verified: within-run
agreement is between Claude instances reading the same code, and the repository's independence rule counts none of it. That the engine
decides the q versus √q question, the spin work's closed-cycle account, or anything about the original 54 spin preparations; the run reports
say what construction each would need. That the method is finished: the per-event ordered lapse, a construction deriving Γ, a control
Hamiltonian on the 64-state source, finite-dwell staircases and register reuse over repeated cycles are logged as open ideas awaiting the
owner's word.

**Caveats on this text.** Dates and counts are read from the history index and run reports as of the writing; the engine-lineage chapter
compresses roughly a thousand entries from August and September into a page and names only those that changed what was installed. The
descriptions of the GPT-peer and Codex eras rest on the history entries and the lead's verified lineage notes, not on the lead's own
observation. The owner may renumber or retitle this volume; it is a working manuscript, authored in Markdown with no PDF source, and its
change log begins with this edition.

Directed by Sean Brady. Executed with Claude Code.

---

## Record of sources

History entries (ironclad `SAM_HISTORY/entries/`): H000011, H000013, H000075, H000127, H000128, H000132, H000142, H000143, H000207, H000209,
H000226, H000229, H000230, H000231, H000233, H000243–H000253, H000273, H000317–H000325, H000551, H001070, H001087, H001635, H001644, H001847,
H002086, H002089, H002090, H002493, H002496, H002553, H002561, H002571, H002577, H002603, H002621, H002640, H002694, H002695, H002709–H002718,
H002729, H002730, H002734, H002736, H002743–H002748.

Installed documents (ironclad): `CLAUDE.md` §§1–14; `docs/DUCK_2.0_METHOD.md`; `docs/DUCK_2.2_RELEASE_PLAN.md`; `docs/CORE_0_11_PLAN.md`;
`docs/CORE_0_11_1_PLAN.md`; `docs/ARCHITECTURE_MAP.md`; `docs/PHASE_B_PLAN.md` to `PHASE_E_PLAN.md`; `SAM_PROJECT/gen6_duck_t500/README.md`,
`RESEARCH_MODES.md`, `INTEGRATION_SUCCESSOR.md`; `CURRENT_REVISION/engines/SLC/README.md`, `CAPABILITIES.md`, `GEN5.md`; `qualification/RELEASES.json`.

Campaign run reports (ironclad `campaigns/`): peer_restore_20261019 (NEXT_RUN_REPORT.md), aq_identification_20261019, resting_clock_20261019,
feop_bound_c02_20261020 (RUN_REPORT.md, rerun/, run3/), feop_sidebyside_20261020, feop_bracket_fiber_20261020, voli_lapse_20261020,
explore_voli_threads_20261020, spin_work_20261020; the retained Codex campaign spin_memory_20261019; sandbox branch
sandbox/feedback-lapse-20261020 (FEEDBACK_LAPSE_DEFINITION.md, RESULTS.md).

Archive (SAM_Research_Project, read-only): GEN4/furious_open1/PROTOCOL.md; GEN4/duck_process1/RUN_CYCLE.md; GEN4/duck_twelve_isotope1.

Documentation repository: `runs/20261020_*/RECORD.md`; `decisions/DECISIONS.md`; `ideas/IDEAS.md`.

---

# Addition (25 October 2026): the continuation to the 25 October state

Sean Brady, 2026-10-25: "a modernized vol ii and vol iii updated with the latest spin/feop work, potentially add a 'part 2' specifically for SCL work and its
implementation. The most recent version Claude has produced of Duck has been the most successful and consistent to date. A starting manuscript has been made
for the SLC work already." This manuscript is that starting text; from this date it is Volume III, Part 2. The sections below continue Chapters VII, IX, X and XI
to the installed state of 25 October 2026 in the same register: installed facts read from the repository, procedures quoted, readings labelled as readings,
no physical interpretation. Directed by Sean Brady. Executed with Claude Code.

## Chapter IX continued — the runs and releases of 21–25 October 2026

Twenty-one further runs and three releases since the edition of 20 October. Duck runs are 1500 s windows with four Opus peers and the lead outside unless
stated; RH entries are domain experiments in the RH DomainSession (host enumeration, native transcendentals and solves) with one Duck verification window.

| Date | Run or release | Record | Machine | Returns / status | What it showed (engineering register) |
|---|---|---|---|---|---|
| 21 Oct | spin_verify_1 | H002760 | Duck 2.3.4 | verification form adopted | five spin results verified to the enclosure width by three implementations; S2d's reversal stands; one account corrected |
| 21 Oct | feop_verify_1 | H002761 | Duck 2.3.4 | two code bases, predictions first | transfer operator re-derived four times, verified at p = 11…23 and joint moduli; hypotheses mapped; Φ reconciles the two forms |
| 21 Oct | volii_matter_1 | H002762 | Duck 2.3.4 | one control against declaration (basis error) | `coupled` construction's first research use; the two recipients of a lapse separated natively |
| 22 Oct | volii_matter_2 | H002763 | Duck 2.3.4, staircase rev 2 | — | lapse orders invisible under the clock recipient, order-sensitive under the energy recipient |
| 22 Oct | volii_matter_3 | H002764 | Duck 2.3.4 | 250 returns, 0 late, 0 undeclared | field-plus-lapse total optimised natively per chain; THREE's front recipe |
| 22 Oct | volii_matter_4 | H002765 | Duck 2.3.4, front library | 235 / 0 / 0 | order 1's total lead 1.83–1.90e-4 on every family; front cross-checked to 1e-40 |
| 22 Oct | volii_matter_5 | H002766 | Duck 2.3.4, staircase rev 3 | 247 / 0 / 0 | every chain's continuous optimum certified a local maximum; the lead's mechanism fails host and native |
| 22 Oct | volii_matter_6 | H002767 | Duck 2.3.4 | 207 / 0 / 0 | the switched share at N = 1/4 above N = 1/2, witnessed; Sean Brady's four conventions as rules |
| 22 Oct | rh_transition_1 | H002768 | RH DomainSession | 1262 calls, 1185 checks | the original source's transition to 1367; two host implementations agree to 8e-80; published target to every digit |
| 23 Oct | rh_transition_2 (window) + native ledger + cloud replica | H002769 | Duck 2.3.4; GCE c3d-highcpu-180 | 218 returns, 0 late; 1673 calls, 881 checks | native exterior ledger PASS; four separate implementations agree; the replica proved exact by `./sam verify` (now STOPPED) |
| 23 Oct | rh_transition_3 | H002770 | T500 + cloud | 5067 calls, 880 checks, identical enclosures | adaptive receiver reproduced; its rise structural; the sign belongs to the receiver's weights; four of five predictions failed |
| 23 Oct | rh_transition_4 | H002771 | T500, unattended | three PASSes | account 1367 → 1371 both receivers; the two-cut combiner form; storage covers the crossing by 1 + ℓ̄/m exactly |
| 24 Oct | rh_sweep_1371_1389 | H002772 | T500, 9.47 h unattended | fourteen PASSes, 44,066 calls | seven accounts to 1389, ledger seamless; sharp −8.66e-4 per account; Δℓ flip at 1383 → 1385 as declared |
| 24 Oct | rh_sweep addenda | H002773–H002775 | host + native checks | — | the change is dP/dY × ΔY; the sign is the admission rule's choice; the adaptive sign a 2 % residual decided by the weights; standing prediction 1389 → 1391: sharp −8.6305e-4, adaptive +6.449e-6 |
| 24 Oct | voli_ceiling_1 | H002776 | Duck 2.3.4, 900 s | FAILED_WITH_RETAINED_OUTCOMES (one undeclared), 44 COMPLETED | four exact languages for the 1/π road; the ceiling a floor beside the reservoir |
| 24 Oct | voli_ceiling_2 | H002777 | Duck 2.3.4, 900 s | FAILED_WITH_RETAINED_OUTCOMES, 93 COMPLETED | the line of sight as a staircase; smallest lawful non-road ledger has four hidden stages |
| 24 Oct | voli_ceiling_3 | H002778 | Duck 2.3.4, 900 s | eleven methods | the regression gate as three native faces; lawfulness global, invisible to any finite jet |
| 24 Oct | **Core 0.11.3 / Duck 2.3.5 / IRONCLAD-R32** | H002779 | PERMANENT | 182 tests OK; verify PASS; rollback duck-2.3.4 verified; tag duck-2.3.5 | declared reservoir floor and the `line_of_sight` construction (derivation OPEN) |
| 24 Oct | voli_ceiling_4 | H002780 | Duck 2.3.5, 900 s | COMPLETE, 143 returns, 0 undeclared, 0 late | the two constructions are one object on cosh²φ = e^{ds}; the delay is the accumulation gap |
| 24 Oct | voli_ceiling_5 | H002781 | Duck 2.3.5, 1500 s | FAILED_WITH_RETAINED_OUTCOMES (superseded controls), 165 returns, 0 late | the exponent as a count of directions is a declared stiffness isotropy; shear invisible to the volume law |
| 24 Oct | volii_gate_1 | H002782 | Duck 2.3.5, 1500 s | COMPLETE, 0 undeclared | Volume II's spin engine through the gate: gain neither mixture nor one-signed; the label is the entrance's |
| 25 Oct | volii_li6_1 | H002783 | Duck 2.3.5, 1500 s | STOPPED_INCOMPLETE by the lead after a 49-min drain; 170 outcomes, 147 COMPLETED, 4 undeclared | Li-6 receiver algebra from archive operands, every prediction exact; the retained complement a Z₄ phase register with a J gauge |

Releases between runs: **Duck 2.3.3** (IRONCLAD-R30; `expected_output_status`, `expected_reason`, `supersedes`: a control can name the engine status it expects, the
reason it expects, and a repaired attempt can supersede its own failed first attempt), **Duck 2.3.4** (IRONCLAD-R31; `expected_failed_check`: a control names the recipe
step whose check must fail, and a generic failure phrase no longer passes as a declaration), **Core 0.11.3 / Duck 2.3.5** (above). Each followed the §13 procedure:
readback document, branch, tests, pre-registered fixture, rollback verified, "Allow permanent changes" typed by Sean Brady, install, freeze, tag.

## Chapter VII addendum — limits and defects found 21–25 October

- **The drain has no deadline.** After a window closes the Duck drains the running tasks with no time limit. In volii_li6_1 one exact 36×36 rank with entries near
  10⁵⁷ held the drain for 49 minutes until the lead stopped the run (`./sam duck stop`), which labels the run STOPPED_INCOMPLETE, queued tasks DEFERRED and the running
  task INTERRUPTED. Logged as a Duck defect (ideas file); the process remedy proposed to the owner is three briefing lines: a size rule for exact tasks (depth ≤ 3,
  operands ≲ 10¹², else modular ranks or the host), a late-window rule (nothing heavy in the last three minutes), and the lead's drain clock (stop five minutes after
  close, recorded as an operator stop). Awaiting Sean Brady's agreement; the code is untouched.
- **Source words.** `GEN3_SOURCE_OPERATOR_WORD` takes exactly the fields name, source_binding, context, data (operators, program, output) and refuses any other
  ("Supply exactly the source operation fields"); the output must carry the declared basis row count ("Word output basis differs"). Products of rational matrices are
  certified enclosures of width about 2⁻¹²⁶, not exact; identities are read by `interval_contains`. Ranks of rational matrices are exact integers.
- **Recipes.** Matrices inside a recipe are limited to 512 entries; larger objects go as single operations.
- **Peers' host tools.** sympy's `.rank()` on a 36-dimensional span with entries near 10¹¹ did not finish in thirty minutes; exact Fraction elimination finishes in
  seconds. `pkill -f <script>` matches the shell that issues it; use `pgrep` and kill by pid. Both are process notes, not engine defects.
- **Lead slips, recorded as such.** Framing-table numbers typed rather than computed (voli_ceiling_5; the rule now: compute every framing number and host-check every
  framing identity before hashing); a briefing that claimed width-zero products (volii_li6_1; corrected after the offline precheck).
- **Closed since the edition.** The 2.3.3 and 2.3.4 fields close Chapter VII.2's note that controls must be read by status: a control now names the status, the reason
  or the failing check it expects, and the ledger counts the rest against the run.

## Chapter X continued — lessons 11–18

11. **The verification form** (adopted 21 October, spin_verify_1): everything given, separate code, predictions first. A result stands when two implementations
    written from the rules alone agree to the enclosure width and the lead's pre-registered predictions are scored, failures included, in the report.
12. **Weights first** (rh_transition_3 to the window addenda): the receiver's weights decide the sign of a change before the arithmetic does. The first line of any
    chart is what it weights; a prediction is a prediction of a receiver's reading.
13. **Compute every framing number** (voli_ceiling_5). A number typed into a framing table is a number the peers will inherit; host-check every identity before the
    preregistration hash.
14. **A control's declared check must be reachable** before any step that could raise (voli_ceiling_3 and after); a control that breaks earlier is right for the wrong
    reason, and 2.3.4 now labels it AGAINST_DECLARATION.
15. **Supersedes is for first attempts**, never for a control, and must name the latest failed attempt (2.3.3; the ceilings).
16. **Precheck openings offline** through the core's own adapter before deploying; a refused opening in the window costs the peers minutes and the lead a slip
    (volii_li6_1's word payload, found offline).
17. **Admit on your own controller; keep a running task count; read the board before duplicating.** The briefing lines that cut the duplicated submissions of the
    matter runs to zero.
18. **Size exact tasks for the window** (proposed after volii_li6_1, awaiting the owner): depth, operand size and timing rules in the briefing rather than a change
    to the drain.

## Chapter XI — status at 25 October 2026

**Installed.** Duck 2.3.5, IRONCLAD-R32, core 0.11.3 beside 0.11.2, 0.11.1, 0.11.0 and the sealed 0.10.2 (`active_core/`, never modified); SLC-GEN5-R1; 182 tests OK at the
install; `./sam verify` PASS; history entries through H002783 (2,373 index rows); rollback target `duck-2.3.4` verified; research peers on the Opus model by default. The
Google Cloud replica ironclad-c3d-20261022 is STOPPED; session stores are archived to Google Drive by SHA manifest and removed locally. Nothing is deployed; nothing is
pending that the owner has not been told, except his decision on the three process lines above.

**What changed in the method since the edition.** Controls declare what they expect in three ways and a peer can supersede its own failed attempt; the verification
form is standard for reproductions; the recipe libraries (staircase, front, identities, gate faces) are admitted at the start of a run and consumed by `$result`;
runs are prepared from the owner's words and the volumes' own chapters as material, never as keys; the lead triages every outcome after the close and writes its own
slips first.

**What this part does not claim** is unchanged from the edition of 20 October: no engine result is a physical result; within-run agreement between Claude instances is
not independence; the engine decides none of the volumes' open joins (the lapse, Γ, the floor, the count, the connector action, the common energy map, the all-scale
bound), and every run report names the construction each would need.

Directed by Sean Brady. Executed with Claude Code.
