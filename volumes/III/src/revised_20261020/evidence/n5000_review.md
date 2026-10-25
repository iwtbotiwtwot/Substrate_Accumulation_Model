# N5000 evidence review and proposed manuscript chapter

Directed by Sean Brady. Manuscript source review and editorial aggregation by Codex. This review reads retained results and performs count transcription arithmetic only. It launches no scientific campaign and changes no research source.

## Immediate findings for the editor

The N5000 result is a complete exact joint-density calculation for six specified 5,000-spin complete Ising graphs. Each graph has 12,497,500 nonzero signed pair interactions and four ordered retained spins. The primary data contain **1,530,259,992 nonzero energy-magnetization-boundary records** across 96 boundary tables. A second injective exponent encoding gives 96 matching tables: **192 logical rows and 96 matched pairs**. The campaign completed in **2,824.215 seconds** on its recorded PRO6000 source. This deserves a full chapter led by what was computed, how exactness was obtained, and what the resulting object makes reusable.

The primary record total is an editorial sum of the 96 K_MAJOR logical-row counts in `GEN4/spin_n5000_archive1/ARCHIVE_MANIFEST.json`. It was not stated as one headline total in the archived README. The matching T_MAJOR total is the same. `evidence/n5000_manifest_aggregation.json` preserves the precise aggregation and source hash. Counting both encodings as additional physical results would double-count the same joint measures.

The 89 unique compressed contents represent all 192 logical rows because some boundary output bytes are exact duplicates. The archive contains **609,671,270,157 compressed bytes** from **1,045,145,366,546 distinct raw bytes**. Every compressed shard was decompressed and checked against its original production raw SHA256 during archive creation. Later completed custody records cover all 89 shards. The early README's download hold is historical; `spin_n5000_final_download1/COMPLETE.md` is the later completed authority.

The attached N2000 paper concerns a different size and its own physical readouts. Its 244,104,392 primary records, ground-state degeneracies, excitation gaps, entropy limits and low-temperature heat-capacity results must not be relabeled as N5000 results. N5000 extends the exact joint construction to the specified larger finite graphs. The N5000 chapter can explain the shared method and then cite the N2000 chapter for its separately calculated physics.

## Proposed chapter text

# Exact joint densities at N5000

## The completed object

We computed the complete joint density of energy, magnetization and four retained spins for six specified complete Ising graphs with 5,000 spins. Every unordered pair interacts, so each graph contains 12,497,500 nonzero pair couplings. The six sources combine three packet constructions with positive or negative uniform fill. All energies, all magnetizations and all sixteen assignments of the retained spins are included.

The primary result contains 1,530,259,992 nonzero records. Each record gives an energy, a magnetization, a retained-spin assignment and an exact integer count of configurations realizing those coordinates. A record is a counted bin, not one individually visited configuration. The counts together account for all 2^5000 spin assignments for each source. Holding the four retained spins fixed leaves 2^4996 assignments in each boundary sector.

The computation also retained a second encoding of the same joint measure. Six sources times sixteen boundary assignments give 96 primary tables; two exponent encodings give 192 logical output rows and 96 matched encoding pairs. All pairs agree on the canonical joint digest, record count and source-derived moments. This is a completed finite enumeration represented by exact generating functions. Its scientific value lies in retaining the full correlation among energy, magnetization and the boundary, so later questions can be answered from the computed object.

| Source family | Uniform fill | Primary nonzero records | Correction bound B | Lattice step d |
|---|---:|---:|---:|---:|
| Packet | +1 | 79,952 | 0 | 1 |
| Packet | -1 | 461,138,212 | 26,660 | 2 |
| Signed packet | +1 | 63,968,000 | 2,000 | 2 |
| Signed packet | -1 | 461,223,474 | 24,660 | 2 |
| Signed packet chain | +1 | 76,796,480 | 2,332 | 2 |
| Signed packet chain | -1 | 467,053,874 | 24,994 | 2 |
| Total | | **1,530,259,992** | | |

Each row includes all sixteen boundary assignments in one encoding. The second encoding reproduces the same row totals. The correction bound measures the total absolute departure from the uniform fill after that fill has been removed; it does not count the complete graph's physical interactions. The small packet/+1 table is the exact uniform ferromagnetic control. Its counts depend only on magnetization and the fixed boundary.

## What the six sources contain

A packet is a finite graph with fifteen spins arranged in three complete five-spin layers. Perfect matchings connect consecutive layers. One full packet has forty parent edges: thirty within its layers and ten in the two matchings. At N=5000, 333 full packets and one terminal five-spin packet give 13,330 unbridged parent edges. The terminal packet preserves the actual remainder of the construction.

The packet family assigns positive couplings to these parent edges. The signed-packet family changes one edge in every five-spin layer to negative, giving 1,000 negative parent edges and 12,330 positive edges. The signed-packet chain adds 333 gateway bridges with alternating signs: 167 positive and 166 negative. For each family, all pairs absent from the parent receive a uniform fill J0 of +1 or -1; parent edges retain their signs. Thus the graph is physically complete even though its departure from the uniform fill has a small-component structure.

The retained spins have the ordered labels P=(0,1,60,61). A boundary mask b from 0 to 15 records their signs: bit a is one when spin P_a is positive. Retaining the ordered mask makes the output conditional on an explicit physical boundary rather than only on its number of positive spins. Exact duplicate output files can share storage where the source proves equality; their boundary identities remain separately recorded.

## Separating the collective interaction

A spin takes a value s_i in {-1,+1}. Energy is the negative signed sum of pair products, and magnetization is the sum of the spins. With no local fields in these sources,

E(s) = -sum_(i<j) J_ij s_i s_j,       M(s) = sum_i s_i.

The joint density g(E,M,b) counts the assignments having those three coordinates. The uniform fill can be handled without materializing every pair during counting. Squaring the total magnetization gives

M^2 = N + 2 sum_(i<j) s_i s_j.

Writing each pair coupling as J_ij=J0+Delta J_ij therefore gives the exact identity

E = E_c - J0(M^2-N)/2,       E_c = -sum_(i<j) Delta J_ij s_i s_j.

The dense term is a function of one collective coordinate, M. All remaining configuration dependence is in the correction graph. A source edge equal to the fill has zero correction. A source edge opposite to it has correction +2 or -2. This identity changes the representation of the exact Hamiltonian; it does not discard any pair coupling or approximate its contribution.

For counting, let k=(M+N)/2 be the number of positive spins and B=sum|Delta J_ij| the total absolute correction. The shifted correction index t=(E_c+B)/2 is an integer. The original coordinates are recovered by

M = 2k-N,

E = 2t-B-J0[(2k-N)^2-N]/2.

The method must retain k jointly with t. Summing over magnetization too early would destroy the association needed to restore the dense M^2 term. This is why the result is a joint density rather than merely a correction-energy histogram.

## Local tables and exact composition

Within a component, each permitted spin assignment contributes a monomial x^k y^t. Its coefficient counts how often those local coordinates occur. Local tables retain gateway spins until their incident bridges are accounted for. Multiplying compatible component polynomials adds positive-spin counts and correction indices, while multiplying their exact integer multiplicities. Summing the gateway assignment joins the compatible cases.

The alternating bridge construction is particularly useful. A bridge whose sign equals the fill has zero correction, so it disappears from the correction graph. The remaining correction components contain at most two complete packets. They are assembled from gateway tables rather than by enumerating all 2^30 assignments of a two-packet component. Repeated components share the same source-bound polynomial, and repeated powers and grouped boundary roots remove repeated arithmetic.

This produces one polynomial G_b(x,y) for each retained boundary. Its coefficient at (k,t) is the desired configuration count after the coordinate decoding above. The correctness argument is constructive: each local assignment appears once in its local table, disjoint component products form every compatible global assignment, and gateway summation closes each interface once. No global configuration is sampled probabilistically.

## Two encodings and exact GPU arithmetic

The two-variable polynomial is packed into a one-variable exponent using its known coordinate bounds. A common lattice step d divides the correction indices. Put u=t/d and T=B/d. The two maps are

phi_K(k,u)=k(T+1)+u,

phi_T(k,u)=u(N+1)+k.

Both are injective on the admitted coordinate rectangle. Division with remainder restores the original coordinates, and output decoding rejects coordinates outside the declared bounds. The two layouts make the same joint counts take different coefficient positions and multiplication layouts. Their agreement tests packing, reconstruction and decoding at the scale of the completed object.

The GPU route multiplies integer polynomials using number-theoretic transforms modulo suitable primes. It then reconstructs the nonnegative integer coefficients by the Chinese remainder theorem. The product of the selected moduli is strictly greater than the full coefficient bound. Each reconstructed coefficient therefore has a unique value in the admitted interval. The stored counts are exact integers; floating-point transforms are not used for them.

N5000 required an enlarged reconstruction buffer. The successor backend admits eighty 64-bit limbs, or 5,120 bits; the N5000 route uses seventy-nine limbs. The serialized count field has 626 bytes, followed with its exact energy and magnetization coordinates to give a 634-byte raw record. The resource planner admits the transform arrays, host output arrays, writer concurrency and disk reserve before the full run. This mattered because exact coefficient growth and output volume remain real costs even when the source factorization is compact.

## Validation of the completed density

Each boundary table satisfies conditional magnetization closure. If r(b) is the number of positive retained spins, the count at fixed total positive-spin number k must be

sum_E g(E,2k-N,b) = binomial(N-4,k-r(b)).

The writer checks this identity for every admitted k. It is stronger than checking only the total 2^4996 because it constrains every magnetization marginal. The energy moments are derived directly from the source couplings and fixed boundary, independently of the polynomial products. These constrain the sum of counts, the energy-weighted sum, and the squared-energy-weighted sum.

The host output stage writes the exact coordinates and integer multiplicities, checks their widths and support, computes canonical bucket digests, flushes the files, and rereads each complete durable raw file to confirm its hash. Production compares all 96 pairs of independently packed encodings on canonical digest, record count and moments. The preparatory qualification records 75 checks including CPU-equal coefficients at 3,000-, 4,000- and 5,000-bit widths and small source/encoding cases. The largest packet/-1 boundary pilot passed in both encodings before admission of full production.

A cheap portable replay supplies an additional concrete comparison. Recomputing the packet/+1 control on the CPU reproduced all 32 encoding/boundary rows in 37.768777 seconds, matching the canonical and raw record hashes, moments and counts. That replay verifies the analytically simple control through the public route. It does not replace the full six-source production, whose other cases retain their own exact checks and paired-encoding records.

## The computation and its preserved data

Full production completed 192 logical rows and all 96 encoding pairs in 2,824.215 seconds, about 47 minutes. The recorded machine was an RTX PRO6000 Blackwell system with 97,887 MiB of device memory, about 27.2 CPU equivalents, 187,999,997,952 bytes of host RAM and a 4 TB container disk. The largest pilot recorded a process allocation of 83,785 MiB of GPU memory. These are the conditions of one completed execution, not a fitted general runtime law.

Before production, the source-bound compiler encountered the generic 4,096-variable admission ceiling. The completed successor normalized and authenticated the explicit frozen N5000 parent graphs while retaining the generic solver's existing admission policy. The failed preparation remains in provenance. Its relevance is the exact source-binding correction that enabled the finished run; it is not the result of the N5000 campaign.

Lossless zstd compression and byte deduplication reduced the completed files to 89 unique compressed contents. The archive is 609,671,270,157 bytes, compared with 1,045,145,366,546 distinct raw bytes. Compression took 1,260.611 seconds. Each compressed shard was decompressed and checked against its production raw hash. The manifest preserves every logical boundary alias, source, plan, record count, canonical digest and raw hash.

The frozen source-input restoration is a separate completed achievement in the chain. When an earlier backup path was absent, all sixteen original input files were reconstructed byte-identically from the retained source grammar and original construction receipts. The restored parent JSON, coupling bitstreams and manifests match their original SHA256 identities, including their original serialization details. No N5000 bulk output was lost. The final restoration uses the native GEN3 checkpoint route, and earlier restoration attempts remain preserved.

Later custody records complete the data chain. Batches 001 and 002 have Drive size and SHA256 verification. The T500 download records verify batches 003 through 006, with batches 005 and 006 adding 32 shards and 203,896,054,295 bytes in the final stage. All 89 shards and 609,671,270,157 compressed bytes have recorded external custody. The completed final-download record supersedes the early all-batches download hold in the original archive README. These statements cite the retained verification receipts; they do not claim a fresh reread of the full archive during this manuscript revision.

## What the result makes available

Once g(E,M,b) is available, a uniform field can be applied by replacing E with E-hM. The partition function for a fixed retained boundary is then the exact finite sum

Z_b(beta,h)=sum_(E,M) g(E,M,b) exp[-beta(E-hM)].

Boundary fields, partial boundary closure, fixed-magnetization questions and added uniform pair couplings likewise operate on retained coordinates. These operations reuse a completed count rather than enumerate the spins again. The multiplicities remain exact even when an exponential or thermodynamic readout is evaluated numerically with its own precision contract.

The scale increase from N2000 to N5000 is substantive because the larger output retains the same detailed finite observables across 12,497,500 physical pair interactions. The reason it is tractable is also explicit: the collective magnetization removes the uniform complete interaction from the hard local bookkeeping, while repeated bounded correction components control the remaining factorization. The result establishes this exact computation for the six specified sources. It is not a universal exact solver for arbitrary dense frustrated graphs, and the single production timing does not establish an asymptotic runtime exponent.

## Subsequent N5000 physical readouts

N5000 also appears in later fixed-sparse-strength thermal and selected-coefficient calculations. They answer a different question from producing the full archived joint table. In the transition campaign the Hamiltonian is H_N=-(M^2-N)/(2N)+kappa C_N: the dense interaction is divided by N while the sparse correction has fixed strength kappa. This differs from dividing the entire archived Hamiltonian by N. The normalization must be stated before comparing thermal conclusions.

For the specified repeated-component families, an exact 71-coefficient nonnegative Bernstein certificate establishes m_0(y)<chi y for y>0, excluding an earlier distant ordered maximum. Together with the threshold beta_c chi=1, uniqueness at the threshold and the negative quartic stabilizer, this establishes the first global continuous ordering onset at every fixed finite kappa>=0. At kappa=1 the chain threshold is beta_c=1.663815941534 to the reported digits. At the finite map's twelve-decimal temperature center, the N5000 mean squared magnetization per spin is 0.0077033393. The exact-critical limit sqrt(N)<(M/N)^2> has the separately derived chain amplitude 0.546951358570.

The selected N5000 window contains 69,904 final records, including 2,056 exact zeros, for k=2372 through 2628 and aligned-negative-edge index 0 through 16 across all sixteen boundaries. At offsets -0.03, 0 and +0.03 from the transition center, those counts capture 53.607483%, 37.267444% and 17.264479% of the complete Gibbs probability. The complete partition function supplies each denominator. The exact window is therefore a reusable finite result with measured probability coverage; it is not represented as the entire equilibrium distribution.

These later readouts connect an exact source construction to ordering, fluctuations and boundary memory. They should be developed alongside the volume's thermal-history discussion, with this chapter providing the full N5000 computational foundation and a clear cross-reference to the different normalization. Their derivations and counts retain the `spin_transition1` campaign identity rather than being added retrospectively to the original production.

## Source and evidence register

Use prefix A=`/home/lilhelper/SAM_Research_Overflow/SAM_Research_Project/` for the following paths. All were read during this source review; the original files remain unchanged.

1. A`GEN4/spin_gpu_n5000_1/README.md`: construction admission, Q01 75 checks, Q02 pilot, hardware, 79-limb N5000 support, 626-byte count, 634-byte record, launch and production target.
2. A`GEN4/spin_gpu_n5000_1/prepare.py`: exact frozen source normalization, source moments, local-table and component planning, two exponent encodings and source-file identities.
3. A`GEN4/spin_gpu_n5000_1/production.py`: grouped identical roots, pair validation, output reuse with hash checks, exact production status and stage boundaries.
4. A`GEN4/spin_gpu_n5000_1/gpu.py` and `gpu_baseline.py`: integer NTT, modulus-product coefficient bound, exact CRT/Garner reconstruction and resource admission. No code was executed or modified.
5. A`GEN4/spin_gpu_n5000_1/output.cpp` and `output.py`: support decoding, full conditional binomial marginals, canonical bucket digests, exact GMP moments, durable full raw-file hash readback.
6. A`GEN4/spin_n5000_archive1/README.md`: full production completion in 2,824.215 s, 192 rows/96 pairs, 89 unique compressed contents, byte counts, 1,260.611 s compression, all-shard decompression checks and CPU replay summary.
7. A`GEN4/spin_n5000_archive1/ARCHIVE_MANIFEST.json`: authoritative exact logical-row counts, B bounds, steps, ports, raw/canonical hashes and aliases. Production result hash is `071e4dc5bca4805e1c6cffc5cd1c24bcaad0057adfae235d89ba641d668d513d`.
8. A`GEN4/spin_n5000_archive1/CHEAP_REPLAY_RESULT.json`: native CPU packet/+1 replay PASS, 32 rows, 37.768777473014779 s, canonical/raw hashes and counts, public runtime SLC-GEN4-P1 / SLC-GEN4-CE-P1 / domain GEN3-R4.
9. A`GEN4/spin_n5000_archive1/PUBLICATION_READY.json`, `PUBLICATION.json` and `CI_RESULT.json`: package file hashes, retained historical public commit `286dfeabb67d680926561f777fc58416dbcc1447`, and successful CI record. Public source: `https://github.com/iwtbotiwtwot/frustrated-spin/tree/286dfeabb67d680926561f777fc58416dbcc1447/reproduce/n5000`. This manuscript revision performs no publication.
10. A`GEN4/spin_n5000_source_recovery1/README.md`, `RESULT.json`, `CHECKPOINT.json`: all sixteen original frozen inputs restored byte-identically, preserved serialization and corrected native checkpoint. No bulk output loss.
11. A`GEN4/spin_n5000_drive12_1/RESULT.json`: completed paginated Drive metadata verification for batches 1/2, 24 shards, 202,360,997,829 bytes. Payload was not redownloaded at that stage.
12. A`GEN4/spin_n5000_t500_download1/RESULT.json`: batches 1-4 downloaded with 57 verified shards and 405,775,215,862 bytes; this is a historical intermediate receipt, not the final retained-location summary.
13. A`GEN4/spin_n5000_final_download1/RESULT.json` and `COMPLETE.md`: batches 5/6 complete, 32 shards, 203,896,054,295 bytes, final all-89-shard custody summary, transfers inactive and restricted key revoked.
14. A`GEN4/spin_transition1/REPORT.md`: later fixed-sparse-strength global first-onset theorem, N5000 and N20000 finite thermal map, exact occupied-window counts, probabilities and method comparison. Its directly linked `PROOF.md`, `THEOREM.json` and `METHODOLOGY.md` are the mathematical and reproduction chain for a full thermal chapter.
15. A`SAM_LIVE/10_PODS_CURRENT.md`: latest bounded live routing, N5000 complete H002035, joint completion H002058 and prior N120 general-graph exact results. Relevant cross-domain contribution: distinguish the structured complete-graph N5000 milestone from the separately solved connected five-regular frustrated N120 graph, whose correction/elimination structure and workload differ.
16. A`manuscripts/drafts/frustrated-spin-work-to-date-20261006/paper.md`: retained synthesis, useful for cross-referencing the two Hamiltonian normalizations, thermal consumers, occupied-window work and later history/control program. This review uses original campaign records for headline N5000 totals.

## Editorial cautions and remaining scope

- Do not call 192 output rows 192 distinct Hamiltonians: there are six sources, sixteen retained boundaries and two encodings.
- Do not call the output 2^5000 enumerated records: it counts 2^5000 configurations in a much smaller exact bin representation.
- Do not add N2000 ground-state numbers to N5000. The shared method is not an identity of finite spectra.
- Do not treat the 32-row analytic-control CPU replay as CPU reproduction of every nonuniform source.
- Do not confuse 89 deduplicated archive contents with 89 logical scientific boundary results.
- Do not repeat the historical download hold as current incompleteness. The later final-download record covers all 89 shards.
- Do not imply a new fresh full-data readback or fresh CI test during the manuscript revision. This is a source review of completed evidence.
- The earlier failed generic admission and restoration checkpoint attempts belong in compact provenance. They explain the implemented corrections without displacing the completed result.

NEGATIVE DRIFT CHECK - COMPLETION: CLEAR. The completed exact joint density leads; limitations identify the actual source family, output semantics and validation scope. Helpful additional evidence uncovered: the primary N5000 total of 1,530,259,992 records can be reported directly from the manifest, and the later N5000 thermal/occupied-window results offer substantive follow-on sections.
