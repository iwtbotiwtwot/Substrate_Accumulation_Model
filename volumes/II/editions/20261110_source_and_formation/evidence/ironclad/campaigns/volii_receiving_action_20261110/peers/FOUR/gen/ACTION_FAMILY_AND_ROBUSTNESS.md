# A canonical receiving family and a response-calibrated robustness bound

Working derivation, FOUR, 10 November 2026. These are added constitutive laws, with the original CAR/source definitions retained. They are not claimed to follow uniquely from the original incidence action.

Put K=I+L_Q3, with its actual cube edges, in every addressed cell. Let q,p be canonical oscillator coordinates, [q_x,p_y]=i delta_xy, and let a be a declared real parameter. Define

 H_a = T + (p^T K^a p + q^T K q - tr K^((a+1)/2))/2 + sqrt(2) g rho^T q.

The normal-ordering subtraction is the vacuum energy of this law; joined and proper branches use exactly the same vacuum reference. The field has all Fock occupations. Its real-time action is

 L_a = L_matter + dot(q)^T K^(-a) dot(q)/2 - q^T K q/2 - sqrt(2) g rho^T q.

At a=1 this is exactly the benchmark. At a=0 it is a strictly local ordinary spring network: canonical p²/2, onsite q²/2 and one (q_x-q_y)²/2 per cube edge. Both use the same physical flavor-blind density and unchanged matter kinetic T; neither includes a compensating density counterterm. Fractional intermediate powers are an expressly different, generally nonlocal inertia law.

For a Walsh mode with K eigenvalue k=1,3,5,7, the frequency is nu_k=k^((a+1)/2), the physical coordinate X=sqrt(2)q has vacuum variance k^((a-1)/2), its mode coupling in normalized b-coordinates is g k^((a-1)/4), and its equilibrium coherent displacement is -g k^(-(a+3)/4) rho_k. Thus

 chi_Xrho(z) = -2g K^a [K^(a+1)-z²]^-1,
 S_induced = -g² int rho(-z)^T [K+z² K^(-a)]^-1 rho(z),
 E_static = -g² rho^T K^-1 rho,
 N_b = g² <rho^T K^(-(a+3)/2) rho>,
 r_a = exp[-g²/4 (3^(-(a+3)/2)+2*5^(-(a+3)/2)+7^(-(a+3)/2))].

All static field shifts and static mixed energy probes therefore agree throughout this family; their equality does not identify the action. Dynamic poles, residues, calibrated vacuum noise, boson number and physical hopping suppression discriminate the family independently of Li6 binding. The normal-coordinate b in a changed law must not be silently identified with the benchmark's measured field X; physical X is sqrt(2)q throughout.

Completing the canonical field square gives H_a>=T-g²V, V=rho K^-1 rho, for every a. The held proper-channel proof is a proof of a lower for this same T-g²V, so its hypotheses and lower transfer without alteration. For the held U4 target, complete field energy is +g²V and vertex energy -2g²V. Same-irrep target configurations have fixed cube parity, while hopping and the full density-conditioned dressing commute U4; hence all compressed hopping blocks vanish for every a. Its exact kinetic cost is still36(tau+t_cell). The unchanged14336 upper, full source Gram and transported Writes survive, with the appropriate new full-Fock dressing. At (tau,t_cell,g²)=(1,1/1000,35), the allowance remains11191/20250. This is an analytical changed-law theorem, using the held source/capacity proof as input.

The selected hopping certificate is different. Native evaluation of the a=0 cloud gives kappa=.10633261316136558..., r(33/2)=.17299577319831216... . Its unchanged phi trial at the old selected point lies >.5852 above the held proper lower. The original finite filter error <=280/20833 still leaves it >.5718 above that lower. This particular certificate fails in the spring law; no absence-of-binding conclusion follows. The separate zero-hop U4 certificate remains valid.

For any finite list of independently measured positive field frequencies nu_j, exact monotone loading can be constructed. Take lambda_dot to be a normalized positive smooth bump convolved with the Bernoulli measures (delta_0+delta_(pi/nu_j))/2, one per distinct frequency. Its Fourier transform has a zero at every nu_j. The exact forced-oscillator solution therefore ends at the equilibrium cloud after time sum_j pi/nu_j+epsilon. For a=0 this is pi(1+1/sqrt3+1/sqrt5+1/sqrt7)+epsilon. Cubic symmetry makes the known density phase constant on each held target type. The prescribed kinetic-freezing control, physical clock and work store remain explicit resources, not consequences of the static law.

## General static-kernel uncertainty

Let a stable flavor-blind harmonic law, possibly with an explicit instantaneous term, complete to H_new>=T-rho^T B_new rho. Use the same cell geometry, matter T, zero and proper-channel definition. Suppose the self-adjoint static kernel satisfies ||B_new-35G0||<=delta on the addressed field one-particle space, where G0 is the benchmark direct-sum Green matrix. This includes a nonlocal kernel if the stated global operator norm is known. Field gaps and vertex form bounds must remain sufficient for the full-Fock realization.

For six particles and four CAR flavors, every occupation has sum rho_x²<=20: the maximal concentration is4+2. For all proper partitions, the sum of fragment density-square maxima is also<=20:5+1 gives18,4+2 gives20,3+3 gives18 and all finer partitions give less. Consequently the held lower transfers as
 L_new >= L_old-20 delta.

The held target profiles have density-square norms20,18,14 in42,33,321. Their unchanged14336 weighted average is
 Rbar=20(169/675)+18(34/135)+14(112/225)=11144/675.
Because scalar dressing retains the zero hopping compression, its changed-law upper satisfies
 U_new <= U_old+Rbar delta.

Thus the same source and all proper channels retain a sufficient allowance
 m_new >=11191/20250 -(24644/675)delta.
In particular delta<11191/739320=.01513688254... suffices before formation errors. This ties an independently measured kernel uncertainty to a mathematical endpoint certificate; delta is not selected to fit the desired binding.

An additional bounded two-body term of pair norm v, whose full flavor action is retained, costs at most15v in the six-particle upper and10v across any proper partition lower. A conservative combined condition is
 (24644/675)delta +25v + E_formation + C_irreversible <11191/20250.
E_formation must be a genuine energy-form error for full H. C_irreversible is an explicitly defined additional resource charge, if that score is requested; reversible work already transferred between system and battery cannot be added again as a second attraction or penalty. Initial reusable apparatus energy/coherence and its reset must also be reported rather than hidden in this score.
