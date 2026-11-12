# Independent derivation of C7–C9

C7, C8 and C9 hold in the submitted conditional scalar model. The C9 comparison with proper matter-particle breakup remains conditional on C3; this verifier does not import a verdict from the active CHANNEL track. All numerical values below are derived in `attempts/003/stdout.json`, repeated from a relocated capsule in `attempts/004/stdout.json`. The exact code is `replay.py`. The first attempt's erroneous verifier Green-function lookup is retained in `attempts/001`; it changed no submitted claim.

## 1. Actual source, coordinates and CAR convention

Let the cube vertices and Walsh indices both be the integers 0,…,7, with character χ_k(x)=(-1)^{popcount(k & x)} and normalized orbital χ_k/√8. The four flavor labels are p-up, p-down, n-up, n-down, with population μ=(2,1,2,1). The full one-cell μ space has dimension C(8,2)·8·C(8,2)·8=50176. This is the relevant fixed-weight subspace of the ambient exterior power Λ⁶(C⁸⊗C⁴), rather than a replacement of that parent by the source image.

The original source data are retained locally in `inputs/LI6_PRINCIPAL_LEDGER.json`, `LI6_EXACT_OPERANDS.json` and the additionally recovered window1 operand `FREE_PAIR_PARENT.json`. The latter contains the actual 64×24 adjacent-pair injection. Its columns are read, rather than reconstructed from an assumed column order. Each column is one ordered pair (x,x⊕d), d∈{1,2,4}; all 24 occur once. The physical replacement receiver is identified by `inputs/REGISTER_FREE_RECEIVER.json` and the frozen source scripts listed by hash in `SOURCE_INVENTORY.json`. Those scripts were read for definitions only.

Let J be that adjacent injection and Q=I-|χ₀/√8⟩⟨χ₀/√8|. The Pauli-allowed residual map is A=(Q⊗Q)J. In the normalized nonzero Walsh-pair basis its exact entries are

    A[(k,l),(x,d)] = χ_k(x)χ_l(x⊕d)/8,   k,l=1,…,7.

The replay derives G₀₀=A* A and its rank24 directly from J. The fixed p-up and n-up zero modes and the independently variable down Walsh modes a,b∈{0,…,4} give the raw physical map R with

    R*R = I₂₅ ⊗ G₀₀.

Different down-core pairs are orthogonal and residual up flavors do not conflict with down cores. The rank is therefore 25·24=600. Its polar form F₀=R(I₂₅⊗G₀₀^(-1/2)) is one isometry on all 600 polar source coordinates. The positive square root exists because the exact Gram is positive definite; positivity follows from A* A and full rank. No column is normalized separately.

For u₀=1₂₄/√24 and the actual offset contrast u₁(x,d)=(1_{d=1}-1_{d=2})/4, exact multiplication gives

    G₀₀u₀=(5/8)u₀,  G₀₀u₁=u₁,  ||u₀||=||u₁||=1,  ⟨u₀,u₁⟩=0.

Consequently the polar residual images are diagonal Walsh geminals

    u = Σ(k=1,…,7) (3-2|k|)/√15 · |k,k⟩,
    v = Σ(k=1,…,7) (χ_k(1)-χ_k(2))/4 · |k,k⟩.

These coefficients are derived from A, not accepted from the supplied phase Gram. The physical source columns use u with down-core assignments

| Walsh excitation a | Proton phase edge | Neutron phase edge |
|---|---:|---:|
| 1 | 0 | 5 |
| 2 | 2 | 6 |
| 3 | 3 | 8 |
| 4 | 1 | 4 |

Edge7 uses v and both down cores at zero. This is the physical-join replacement: the two join edges use down Walsh mode4 and carry its physical kinetic cost. It is not the older blocked up-orbital/register receiver.

All CAR actions use orbital-major mode number 4x+α. A flavor-major source creation word is converted to that exterior basis by its permutation sign. For a proton excitation a, one geminal term is the word

    p_up(0), p_up(k), p_down(a), n_up(0), n_up(k), n_down(0),

and analogously for the neutron column. The replay retains the signed words and coefficients for every phase column and proves their full Gram is I₉.

The phase address rule is read from the original operand. Address14336 gives exponents (0,0,2,2,2,0,0,0,0), hence the unchanged normalized vector

    z=(1,1,-1,-1,-1,1,1,1,1)/3.

The decoded vector is also compared to all eighteen retained real/imaginary coordinates. This normalization is the source norm9, followed by division by3.

## 2. Flavor representation and source projectors

For one-body orbital E_xy=Σ_α c†_(xα)c_(yα) and flavor Q_ab=Σ_x c†_(xa)c_(xb), the CAR relation for bilinears immediately gives [E_xy,Q_ab]=0. The orbital and flavor actions commute on the full exterior power. Classical skew Howe duality gives

    Λ⁶(C⁸⊗C⁴) = ⊕_{λ ⊢ 6, λ₁≤4, length(λ)≤8} O_λ ⊗ F_{λᵗ}.

This decomposition is multiplicity free as a product representation. Its μ restriction is ⊕ O_λ⊗F_{λᵗ}[μ]. The representation dependency was checked against the classical statements in [Aboumrad, arXiv:2208.08979v1, Theorems3.10 and3.12](https://arxiv.org/html/2208.08979v1#S3.SS3). The primary readback is hash-retained under `inputs/`. Only this structural dependency is taken from that source; every source coefficient and energy calculation here is separate.

The fresh replay uses flavor, rather than the prior orbital, Casimirs:

    C₂=Σ_ab Q_ab Q_ba,   C₃=Σ_abc Q_ab Q_bc Q_ca.

Both products are applied with full CAR signs, retaining intermediate flavor weights before returning to μ. It would be wrong to truncate each Q_ab to the μ sector first. Each density occupation profile is invariant under flavor operations, so the computation can use its entire finite flavor fiber without deleting any relevant intermediate state.

For each allowed partition λ, fill the first λ_i flavors in orbital i. This Ferrers determinant is a joint highest-weight vector. Applying the CAR Casimirs to it derives their scalar labels. The required labels and independently enumerated semistandard-tableau weight multiplicities are

| Orbital λ | Flavor λᵗ | C₂ | C₃ | dim F_{λᵗ}[μ] |
|---|---|---:|---:|---:|
| 42 | 2211 | 14 | 46 | 1 |
| 33 | 222 | 18 | 54 | 1 |
| 411 | 3111 | 18 | 90 | 1 |
| 321 | 321 | 24 | 111 | 4 |

All nine allowed λ labels, their U8 dimensions and μ multiplicities are retained; their dimension sum is exactly50176. In particular, the Casimir degeneracy between33 and411 is real. The replay chooses an integer linear combination of C₂ and C₃ with distinct labels on all allowed irreps, forms its rational Lagrange projectors, and checks every projector's adjoint, idempotence, pairwise orthogonality, completeness and both Casimir eigen-equations. This proves that the source contractions are contractions with the actual flavor-isotypic projectors.

The source P_a/N_a pair has one k=a term of occupation33 and squared amplitude1/15. All k≠a terms have occupation321 and total squared amplitude14/15, since a∈{1,2,3,4} has |3-2|a||=1. The direct CAR contractions on the complete μ fibers give

| Occupation fiber | 42 source pair Gram | 33 source pair Gram | 411 | 321 source pair Gram |
|---|---|---|---|---|
| 33 | J₂/2 | anti-J₂/2 | 0 | 0 |
| 321 | 3J₂/10 | anti-J₂/6 | 0 | [[8,-2],[-2,8]]/15 |

Here J₂ has all entries1 and anti-J₂=[[1,-1],[-1,1]]. Combining with the actual geminal coefficients therefore gives

    G₄₂ = 47J₂/150,
    G₃₃ = 17 anti-J₂/90,
    G₃₂₁ = [[112,-28],[-28,112]]/225.

The replay does not assume that this reduction is enough: it assembles all nine signed source vectors and contracts them on every actual occupation profile. Cross-a terms vanish, edge7 is pure42, and every phase Gram for411 or any other unused irrep is zero. The resulting projected-source Gram ranks are5,4,8. These Gram matrices are compressed projectors, not generally idempotent matrices on the phase9 coordinates.

Their contractions with the decoded z are

    w₄₂=169/675,  w₃₃=34/135,  w₃₂₁=112/225,

with sum1. This proves C7 from the original source and CAR representation.

## 3. Full flavor information and target capacities

Write Φ_λ=Π_λF₀P₉, where P₉ is the actual polar phase injection. Let r_λ=rank(Φ_λ)=rank(Φ_λ*Φ_λ) and m_λ=dimF_{λᵗ}[μ]. Choose any basis of the r_λ-dimensional image and expand each basis vector in a fixed orthonormal flavor-weight basis. The span S_λ of all orbital coefficients has dimension at most r_λm_λ. The computed bounds are therefore

    dimS₄₂≤5,  dimS₃₃≤4,  dimS₃₂₁≤32.

Using rank8 instead of32 for the last capacity would discard flavor information. One vector Σ(i=1,…,4) o_i⊗f_i/2 already needs four independent orbital coefficients; the exact reduced orbital Gram I₄/4 in the control exhibits this failure.

Let G=(I+L_Q3)^(-1). Exact inversion, independently checked by the Walsh spectral formula, gives distance entries (36,13,8,6)/105 for distances0,1,2,3. The scalar density energy is V(ρ)=ρ*Gρ, including all self terms and both orders of every mixed term.

The following target orbital weight profiles are used:

| Type | Profiles | Orbital count | V |
|---|---|---:|---:|
| 42 | 4 at x,2 at neighboring y; ordered x,y | 24 | 928/105 |
| 33 | 3 at x,3 at neighboring y; unordered pair | 12 | 882/105 |
| 321 | 3 at x,2 at y,1 at z; y,z distinct neighbors of x | 48 | 770/105 |

Each profile is a permutation of its highest orbital weight. Its weight multiplicity in O_λ is one, so its complete flavor fiber is one orbital direction tensor F_{λᵗ}. In the μ restriction the replay derives ranks1,1,4 per profile, respectively, and enumerates every profile. Distinct profiles are orthogonal. Thus the available orbital dimensions are24,12,48, sufficient for the entire S_λ in all three cases.

The listed potentials are also maxima on the respective irreps, though only their attained values are needed for C8. The weights of a Schur module are majorized by λ: column-strict tableaux imply that the total count of any k symbols is at most λ₁+…+λ_k. Thus they lie in the convex hull of the permutations of λ. The positive quadratic V is convex, so its maximum occurs at a highest-weight permutation. For42 and33, decreasing Green entries favor nearest neighbors. For321, the numerator is504+12Gdist(x,y)·105+6Gdist(x,z)·105+4Gdist(y,z)·105. Three distinct cube vertices cannot be pairwise adjacent. The smallest loss from replacing a distance1 entry13 by distance≥2 entry≤8 occurs on the coefficient4 pair; the result is770, attained by the specified wedge of two cube edges.

## 4. A finite algebraic whole-parent unitary

Here is an explicit finite procedure, not merely a dimension assertion or a separate mapping of columns.

1. Use the canonical exterior basis and CAR flavor matrices. For each flavor highest weight λᵗ, solve the rational linear equations imposing that weight and annihilation by all raising Q_(a,a+1). The resulting highest-weight space is the orbital multiplicity factor O_λ. Apply lexicographic exact Gram–Schmidt to choose its orthonormal basis.
2. Apply ordered flavor-lowering words to those highest-weight vectors. Choose a common independent list of lowering words and orthonormalize their flavor Gram once. The same Gram is used for every orbital copy. This constructs a common identification O_λ⊗F_{λᵗ}; it does not make independent choices that could rotate different flavor fibers differently.
3. Expand all Π_λF₀P₉ columns in this basis. Concatenate their orbital coefficients for every basis vector of F_{λᵗ}[μ]. Lexicographic exact Gram–Schmidt gives an orthonormal basis s₁,…,s_d of S_λ, where d≤r_λm_λ.
4. For target profiles, start from one reference highest orbital weight line and apply orbital permutation operators to identify the flavor factors across profiles. These operators commute with flavor. Order the profiles lexicographically to obtain an orthonormal target orbital list t₁,…,t_D. Map s_i to t_i for i≤d.
5. Complete both lists to orthonormal bases of all O_λ by lexicographic Gram–Schmidt against the fixed orbital basis. Define U_λ=Σ_i |t_i⟩⟨s_i|. For all phase-absent λ take U_λ=I. Then

       U = ⊕_λ (U_λ ⊗ I_{F_{λᵗ}}).

Every step uses finite exact linear algebra, positive algebraic square roots and a prescribed ordering. G₀₀^(-1/2) is algebraic and finite, so the source coefficients needed here are algebraic as well. No numerical tolerance or limiting filter is involved. A dense50176×50176 matrix need not be formed to specify or prove this finite algorithm.

U is a unitary on the whole ambient six-particle one-cell parent and commutes with full U4. In particular it preserves μ, every flavor multiplicity Gram and all cross-source flavor correlations, not merely the three scalar sector probabilities. Its restriction to the original600 image is one source-wide map UF₀. In raw coordinates its Gram remains I₂₅⊗G₀₀.

For every original source Write w that is unitary in the original source metric, use polar source coordinates and extend it physically as

    J_g w J_g* + (I-J_gJ_g*).

This is a unitary on the receiving Hilbert space and has exactly the original action on all source coordinates. It may be physically nonlocal. Preserving these Writes is not a claim that they remain diagonal local phase gates.

The full-cell matter extension is also explicit. Let H_z be the all-six-in-cell-z subspace in Λ⁶(ℓ²(Z³)⊗C⁸⊗C⁴). These subspaces are mutually orthogonal and U4 invariant. Define the translated copy of U on each H_z and identity on the orthogonal complement of their direct sum. The resulting bounded direct-sum unitary is translation covariant and flavor preserving. It retains all separated-cell configurations in the parent. It does not claim to be generated by the kinetic Hamiltonian.

## 5. Kinetic energy, parity and full Fock dressing

The fixed Hamiltonian is

    H=T+dΓ(ω)+gΣ_(z,x) ρ_(z,x)(b_(z,x)+b†_(z,x)),
    T=Σ_particles(2τL_Q3+t_cell L_Z3),  ω=⊕_z(I+L_Q3).

The count parity Σ_xρ_x|x| mod2 is even on every42 target profile and odd on every33 and321 profile. Any single internal hop flips this parity. Thus same-type target hopping compressions vanish. Hopping commutes with full flavor, so cross-type compressions vanish too, including opposite-parity42/33 or42/321 pairs. The replay checks this directly using the complete μ fibers: there are480 raw CAR hopping edges and144 nonzero raw profile blocks among the target states, but every projected block is exactly zero. This is a compression statement; hopping and current images in the parent are not set to zero.

For a matter determinant D, set f_D=-gω^(-1)ρ_D. On the full scalar Fock space define the decomposable Weyl unitary

    W_g=Σ_D |D⟩⟨D|⊗W(f_D).

The countable sum is a unitary direct sum. Since N=6, ||ρ_D||≤6, and 1≤ω≤7, the displacement and its field-energy norm are uniformly bounded. Weyl translation consequently preserves the field quadratic-form domain with a uniform bound. The finite-particle lattice T is bounded; the linear field interaction is relatively form bounded with arbitrarily small coefficient against dΓ(ω). Thus H has a semibounded closed form on the usual field form domain. Completing the square there yields

    H = T + Σ |ω^(1/2)b + gω^(-1/2)ρ|² - g²V

as a form identity, with the appropriate summed one-particle mode notation. The term in squares is nonnegative. These assertions extend from finite matter/finite-boson vectors by form closure. No field-number truncation or finite-cell approximation is used.

On W_g(ψ⊗vac), the square term has zero expectation. For every density branch, the field energy is +g²V and the interaction is -2g²V. The effective -g²V is their sum, not an omitted field cost or a density counterterm.

The matter hopping expectation contains coherent overlaps. For an internal neighbor hop x→y,

    ⟨f_D'|f_D⟩ = exp[-g²||G(e_x-e_y)||²/2]
                  = exp[-583g²/11025] = r.

The replay derives this common coefficient from the exact G. Therefore every internal hopping matrix element is multiplied by the same r, and the exact zero target compression survives dressing. Cell hopping leaves the all-six-in-one-cell trial space; its off-diagonal compression is zero. Each of six particles still pays the internal diagonal6τ and cell diagonal6t_cell. Hence the full kinetic compression is exactly36(τ+t_cell)I₉.

For J_g=W_g(UF₀⊗vac), J_g*J_g=I₆₀₀ and full flavor commutation survives because every density operator is flavor invariant. Only its phase9 energy compression is asserted:

    P₉*J_g*HJ_gP₉ = 36(τ+t_cell)I₉ - g²M,
    M = (928G₄₂+882G₃₃+770G₃₂₁)/105,

where the G's now denote the rebuilt nine-dimensional compressed flavor projectors, including edge7. This is an exact expectation pullback, not an operator equality on the parent that removes full Fock or hopping complements. This proves the energy part of C8.

## 6. Unchanged preparation and the conditional margin

Each paired block of M is

    [[189149,6379],[6379,189149]]/23625,

and edge7 is928/105. The exact phase9 spectrum is5222/675 with multiplicity4,65176/7875 with multiplicity4, and928/105 with multiplicity1. Thus5222/675 is the uniform phase9 density minimum. The unchanged z gives

    ⟨z,Mz⟩ = 565492/70875,
    E_z = 36(τ+t_cell) - (565492/70875)g².

At τ=1, t_cell=1/1000, g²=35 the separate physical terms are

| Term | Exact value |
|---|---:|
| Kinetic | 9009/250 |
| Field | 565492/2025 |
| Interaction | -1130984/2025 |
| Complete upper | -4925191/20250 |

Conditional on C3, its hypothesis g²≥735τ/44 holds, and the common proper-channel lower is-752g²/105+8τ=-728/3. The difference lower minus upper is exactly11191/20250>0. This proves the submitted C9 conditional conclusion, with the original input, Hamiltonian and energy zero. It is not a full essential-spectrum, fiber-HVZ or empirical isotope statement.

## 7. Controls and precise scope

All six assigned controls have retained arithmetic evidence in `controls` in the replay output.

* C₂ alone has a rank-two eigenvalue18 block containing both33 and411. A nonzero411 vector has C₃=90, whereas33 has C₃=54. C7 therefore needs the higher invariant (or an equivalent representation argument).
* A rank-one phase vector with four independent flavor coefficients has orbital reduced rank4. The actual321 rank8 phase image requires the safe capacity bound32.
* Sending all unchanged input weight into42 would lose probability506/675. It also changes ⟨C₂⟩ from2698/135 to14, a nonzero invariant defect808/135; that is incompatible with full U4 preservation.
* Omitting kinetic or field energy removes9009/250 or565492/2025, respectively, at the submitted point. Both are explicitly included in the complete energy above.
* The phase9-to600 promotion fails for an actual raw600 source input, not only by a dimensional warning. Use ground down cores a=b=0 and the antisymmetric pair-coordinate difference (0,1)-(1,0) from the original24 dictionary. Its raw metric norm is3/2, and exact CAR projection places it entirely in411. Our finite extension is identity on this phase-absent irrep. An independently expanded position state has6144 nonzero determinants, V=1783/315 and ⟨A_internal⟩=34/3. Its full dressed energy is36(τ+t_cell)-(68τ/3)r-(1783/315)g². At the submitted point, using only0<r≤1, this exceeds the uniform phase9 upper by at least6749/135>0. Thus the stated map genuinely has no uniform phase9-quality energy bound on all600 inputs.
* A phase flip on one orbital, tensored with flavor identity, is U4 preserving but has a nonzero commutator with fixed hopping. The exact one-particle commutator has squared Frobenius norm96; a retained legal six-particle CAR edge also witnesses noncommutation. Any exp(-itH) commutes with H. Symmetry compatibility therefore does not implement autonomous evolution under fixed H, and no paid preparation or control-work claim follows.

The receiving map is a constructive variational isometry preserving the full source metric, Writes and flavor data. C7–C9 require no scientific correction. The verifier's failed lookup, successful correction and added physical scope counterexample remain in the sealed record. The appropriate next step is lead integration with CHANNEL's independently reached C3 verdict and the other completed track, without adding the two distinct receiving maps' energy gains.
