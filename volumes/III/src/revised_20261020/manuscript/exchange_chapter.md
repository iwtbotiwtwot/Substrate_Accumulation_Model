# Exact Exchange and Symbolic Matter

## A local source becomes an interacting exact object

The exchange program constructed a continuous route from retained Li7 source operators to finite interacting chains and then returned their spectra to symbolic matter calculations. Its completed outputs include nineteen arrangement classes, a fully matched finite polynomial Bethe benchmark, a complete length-thirteen exchange spectrum accounting for 67,108,864 states, and composition with thirty-two local-matter families in 2.011662 seconds of recorded assembly. The assembly reused completed exchange factors and local quartics. [EX, pp2–10]

The local exchange space $V$ has four states. Chain length $L$ counts copies of this four-state factor; it is distinct from isotope mass number, Ising spin count and Starbreaker layer count. $T$ is the retained local return operator, $K$ the signed source-role interaction, and $Q(g)=T+gK$ their symbolic local family. On the chain, $P$ exchanges two factors, and the periodic exchange Hamiltonian is $H_{\mathrm{ex}}=\sum_{j=1}^L P_{j,j+1}$. Independent parameters $J$, $\mu$, $g$ and later $\nu$ remain symbolic.

The signed interaction uses inherited source incidence vectors $d$ and their diagonal component matrices $D^a$:

$$
K=\sum_{a=1}^{3}D^aTD^a.
$$

All thirty-five assignments of three proton roles and four neutron roles produce nineteen exact $K$ spectra and nineteen exact $T+K$ spectra. The classes are the sixteen reversal pairs and three palindromic singletons. Equal species counts or equal counts of unlike neighbors do not determine the result. The source-role operator reads additional arrangement information. Species erasure sends $K$ to zero, and sign erasure changes its spectrum. [EX, p2]

The full coupling calculation constructs $35\times48=1{,}680$ four-state component polynomials $\det(qI-T-gK)$. Five exact coupling evaluations determine each degree-at-most-four coupling dependence, and every coefficient array agrees with an independent determinant expansion over all twenty-four permutations. Comparing complete 192-state characteristic polynomials gives equality only at $g=0$ between distinct arrangement classes. The nineteen whole-spectrum classes therefore remain distinct for every nonzero coupling. This concerns equality of entire spectra; it does not exclude individual level crossings. [EX, p3]

## The canonical quartic retains the actual source matrix

In the canonical component, $T$ has diagonal entries 84 and off-diagonal entries 8 on the path 2–1–3–4. $K$ has diagonal $(672,2016,672,672)$, with path entries 96,32,32. After ordering along that path and subtracting $(84+672g)I$, define

$$
a=8+96g,\qquad b=8+32g,\qquad h=1344g,\qquad x=q-(84+672g).
$$

The centered matrix is tridiagonal with diagonal $(h,0,0,0)$ and off-diagonal $(a,b,b)$. Its characteristic polynomial is

$$
p(x;g)=x^4-hx^3-(a^2+2b^2)x^2+2hb^2x+a^2b^2.
$$

This follows from successive tridiagonal minors: $p_0=1$, $p_1=x-h$, $p_2=xp_1-a^2$, $p_3=xp_2-b^2p_1$, $p_4=xp_3-b^2p_2$. At $g=0$, the uncentered eigenvalues are $80\pm4\sqrt5$ and $88\pm4\sqrt5$. In the original 192-state generated Li7 instance, each has total multiplicity forty-eight. The quartic is derived from the retained matrix rather than fitted to sampled eigenvalues. [EX, pp2–3,12]

The 1,680 component occurrences yield 165 distinct ordered operator pairs, thirty-two symbolic quartics and 162 uniform-field compatibility classes. These count different properties. An ordered pair keeps the actual matrices in an aligned basis; a quartic keeps their eigenvalue multiset; a compatibility class determines which placed operators preserve the fixed transfer family. Equal local spectra do not by themselves establish that differently placed operators are compatible. [EX, pp5–6]

## The source extension supplies the exchange law

Sean Brady's explicit extension lifts the completed receiver-current swap to two separately owned four-state factors:

$$
P\lvert i,j\rangle=\lvert j,i\rangle.
$$

The local return operator is not silently replaced by a permutation. $T$ and $K$ retain their source roles; $P$ is the newly specified joint action. It preserves the sum of one-hot contents, reverses their directed difference, and squares to the identity. The rational exchange family is

$$
R(u,v)=(u-v)I+\eta P,\qquad\eta\ne0.
$$

The Yang–Baxter consistency condition reduces to a scalar coefficient identity. For this family the residual coefficient is $\eta^2[(u-w)-(u-v)-(v-w)]$, which vanishes identically. Native exact word coefficients on the sixty-four-state three-factor space and an independent permutation replay check the construction. The $R$-matrix belongs to established integrable-system mathematics; the project result is the specified source extension, its exact execution, and the resulting reusable source-to-matter chain. [EX, pp3–4]

## A complete finite polynomial Bethe benchmark

A transfer matrix is obtained by letting an auxiliary four-state factor interact successively with the chain and tracing out that auxiliary factor. With auxiliary label $a$, the local operators and ordered product are

$$
L_{aj}(u)=uI+\eta P_{aj},\qquad M_a(u)=L_{aL}(u)\cdots L_{a1}(u),
$$

$$
\tau_L(u)=\operatorname{tr}_a M_a(u),\qquad[\tau_L(u),\tau_L(v)]=0.
$$

At the regular point its logarithmic derivative gives

$$
H_{\mathrm{ex}}=\eta\tau_L(0)^{-1}\tau_L^{\prime}(0)=\sum_{j=1}^{L}P_{j,j+1},\qquad L+1\equiv1,
$$

with no identity offset in the retained gauge. At $L=2$ the two periodic bonds give $H_2=2P_{12}$. This convention fixes the spectral numbers used in every subsequent matter calculation. [EX, p4]

The finite benchmark constructs sixteen exact nested polynomial tuples: two at $L=2$, four at $L=3$ and ten at $L=4$. Each is checked against the simultaneous eigenspaces of every transfer coefficient, including the full GL4 multiplet multiplicities. All 336 states are accounted for, and five hundred exact transfer-coefficient commutators vanish.

| Chain length | Exchange eigenvalue and multiplicity | Total states |
|---|---|---:|
| 2 | −2:6; 2:10 | 16 |
| 3 | −3:4; 0:40; 3:20 | 64 |
| 4 | −4:1; −2:50; 0:60; 2:110; 4:35 | 256 |

Polynomial divisibility also handles singular Bethe-root presentations. At $L=4$, the tuple $Q_1=z(z+1)$, $Q_2=Q_3=1$ gives the regular collected eigenvalue $\Lambda(z)=4z^4+4z^3-2z-1$ and energy $\Lambda^\prime(0)/\Lambda(0)=2$. Dividing individual terms at the singular roots would obscure that exact result. The benchmark instead collects the numerator, checks exact divisibility, and compares the resulting polynomial with the actual joint eigenspaces. The complete finite result is $L=2,3,4$; the large-chain spectrum below uses a separately established representation route. [EX, pp4,11]

## Exact representation structure closes length thirteen

The full tensor space has dimension $4^L$, but the exchange operator lies in the permutation algebra. Schur–Weyl decomposition separates a local-matter representation $U_\lambda$ from a permutation representation $S_\lambda$ for each partition $\lambda$ of $L$ with at most four rows. Exchange acts on $S_\lambda$, and multiplying its eigenvalue multiplicity by dim $U_\lambda$ recovers the full tensor account. The exact dimension closure is

$$
\sum_{\substack{\lambda\vdash L\\\ell(\lambda)\le4}}\dim U_\lambda\,\dim S_\lambda=4^L.
$$

Momentum splits the permutation blocks further. Exact modular characteristic polynomials and bounded Chinese remainder reconstruction avoid uncontrolled rational coefficient growth. At $L=10$, momentum reduces the largest block from 768 to 77. A separately recorded fifty-four-sector comparison takes 117.611 seconds for the rational characteristic-polynomial stage and 0.962 seconds for its modular counterpart. These are times for that stage and comparison. [EX, pp4–5]

The raw-coordinate route retains an invertible basis matrix $B$ and the retained action $H_B$ without first normalizing the basis. The pencil $H_B-xB$ has determinant $(-1)^n\det(B)\det(xI-B^{-1}H_B)$, so its exact normalization and coordinate maps recover the same spectrum. At $L=13$, opposite momenta are paired over the real cyclotomic field $\mathbb Q(\zeta_{13}+\zeta_{13}^{-1})$, of degree six. A 7,920-dimensional rational primitive-parity problem becomes a largest 1,320-dimensional matrix over that field. Supported GPU work constructs exact projector/action residues and columns; CPU arithmetic performs certified lifting and spectral computation. [EX, pp5,13]

The completed L13 record closes all thirty-nine partitions and accounts for $4^{13}=67{,}108{,}864$ states. Its 713.1002004-second clock is the resumed hybrid completion, importing thirty-two finished partitions and completing the remainder. It is not a fresh whole-L13 timing. The completed factors and multiplicities are the result used by the subsequent matter calculation. The attached article's L14 run was only launched at its cutoff and is not included in that completed count. [EX, pp5,10; H001563]

## One retained exchange solution supports thirty two matter families

A uniform sum of local operators commutes with every site permutation. For a local $Q$, the identity $P(Q\otimes I)=(I\otimes Q)P$ gives $[P,Q\otimes I+I\otimes Q]=0$. Consequently the homogeneous Hamiltonian

$$
H=JH_{\mathrm{ex}}+\mu\sum_{j=1}^{L}Q(g)^{(j)}
$$

uses the same exchange decomposition. If $q_i(g)$ are the four local roots and $n=(n_0,n_1,n_2,n_3)$ is a Schur occupation with $\sum_i n_i=L$, then its combined energy is

$$
E_{\lambda,e,n}=Je+\mu\sum_{i=0}^{3}n_iq_i(g).
$$

The multiplicity is the exchange multiplicity $m_\lambda(e)$ times the exact Schur-weight multiplicity $K_{\lambda,n}$. Coincident energies add their multiplicities. This formula explains the reuse: a new local family needs the retained exchange factors, local roots, occupations, source maps and multiplicities; it does not require the exchange operator to be solved again. [EX, p6]

| Retained exchange input | Partitions | Local families | States per family | Factor and weight pairs | Assembly seconds |
|---|---:|---:|---:|---:|---:|
| L12 | 34 | 32 | 16,777,216 | 54,633 | 0.842111 |
| L13 | 39 | 32 | 67,108,864 | 35,184 | 2.011662 |

Both rows perform zero new exchange solves and zero new local-quartic solves. The L13 shared template retains 133 distinct exchange factors. Its assembly clock measures the composition stage, separately from obtaining those factors. This is the main computational significance: a completed many-body spectrum remains an exact operand for an entire family of further matter calculations. [EX, pp6–7; H001565]

The all-length one-site criterion also identifies when nonidentical local sources may be mixed. For $L\ge2$ in the homogeneous untwisted family, a sum $\sum_j A_j^{(j)}$ commutes with every transfer matrix exactly when $A_j-\operatorname{tr}(A_j)I/4$ is independent of site. Uniform traceless content is sufficient; scalar offsets may differ and remain in the final energy. The retained example $K_{036}-K_{012}=336I$ has that property. The necessity follows from commutation with the cyclic shift at $\tau_L(0)$, then partial tracing its shift defect. This is an all-length algebraic statement with its declared transfer-family assumptions. [EX, p6]

## Fusion and a conserved current connect composite channels

The pair projectors $E_\pm=(I\pm P_{12})/2$ select ten symmetric and six antisymmetric local states. The exact fused/fundamental $R$-polynomials act on forty- and twenty-four-dimensional spaces. All fifteen bivariate coefficient matrices in the mixed Yang–Baxter comparison vanish in each channel, checked in the faithful regular representation of $S_4$. Uniform matter actions lift into the same fused bases and have eigenvalues $q_i+q_j$, with $i\le j$ in the symmetric channel and $i<j$ in the antisymmetric channel. [EX, pp6–7]

On three factors the oriented exchange current is $C=\sum_j[P_{j,j+1},P_{j+1,j+2}]$. It commutes with $H_{\mathrm{ex}}$ and obeys

$$
C^2=3H_{\mathrm{ex}}^2-27I,\qquad\det(xI-C)=x^{24}(x^2+27)^{20}.
$$

The current's diagonal pair-parity blocks vanish; both cross maps have rank twenty. It therefore transports the two twenty-dimensional mixed-symmetry sectors between the symmetric-pair and antisymmetric-pair carriers while preserving their exchange energy. The fully symmetric twenty-dimensional sector and fully antisymmetric four-dimensional sector form its kernel. These are exact operator identities and ranks, with no physical time assigned to $C$. [EX, pp7–8,13; H001565]

## The collective interaction preserves the exact family

The completed compatibility analysis also supplies a genuine two-object interaction. Equal coupling of every unordered pair gives

$$
Y_Q=\sum_{i<j}Q^{(i)}Q^{(j)}=\frac12\left[Q_{\mathrm{tot}}^2-(Q^2)_{\mathrm{tot}}\right].
$$

Expanding the square proves the identity, and both uniform sums commute with every site permutation. Thus $JH_{\mathrm{ex}}+\mu Q_{\mathrm{tot}}+\nu Y_Q$ preserves the entire transfer family at every length. On a Schur occupation, define $s=\sum_i n_iq_i$ and $r=\sum_i n_iq_i^2$. Its energy is

$$
E_{\lambda,e,n}=Je+\mu s+\frac\nu2(s^2-r),
$$

with the inherited multiplicities. Existing exchange and weight records therefore already support this collective two-object term. [EX, p8]

The nearest-neighbor density family spanned by $T\otimes T$, $T\otimes K+K\otimes T$ and $K\otimes K$ has a different completed answer. For all 165 retained pairs, its strict three-site commutator outputs have rank three. For $L\ge5$ no nonzero combination in that specified span commutes with the retained $H_{\mathrm{ex}}$. This delimits that proposed geometry; the collective construction is an explicit compatible successor. Spatial coefficients, nuclear calibration and all-length polynomial Bethe completeness remain separate questions. None is required to state the completed finite spectra or the all-length compatibility identities already derived.
