# Exact joint densities at N5000

## The completed object

We computed the complete joint density of energy, magnetization and four retained spins for six specified complete Ising graphs with 5,000 spins. Every unordered pair interacts, so each graph contains 12,497,500 nonzero pair couplings. The six sources combine three packet constructions with positive or negative uniform fill. All energies, all magnetizations and all sixteen assignments of the retained spins are included.

The primary result contains 1,530,259,992 nonzero records. Each record gives an energy, a magnetization, a retained-spin assignment and an exact integer count of configurations realizing those coordinates. A record is a counted bin, not one individually visited configuration. The counts together account for all $2^{5000}$ spin assignments for each source. Holding the four retained spins fixed leaves $2^{4996}$ assignments in each boundary sector.

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

Each row includes all sixteen boundary assignments in one encoding. The second encoding reproduces the same row totals. The correction bound measures the total absolute departure from the uniform fill after that fill has been removed; it does not count the complete graph's physical interactions. The small packet/+1 table is the exact uniform ferromagnetic control. Its counts depend only on magnetization and the fixed boundary. [N5-6, N5-7]

## What the six sources contain

A packet is a finite graph with fifteen spins arranged in three complete five-spin layers. Perfect matchings connect consecutive layers. One full packet has forty parent edges: thirty within its layers and ten in the two matchings. At N=5000, 333 full packets and one terminal five-spin packet give 13,330 unbridged parent edges. The terminal packet preserves the actual remainder of the construction.

The packet family assigns positive couplings to these parent edges. The signed-packet family changes one edge in every five-spin layer to negative, giving 1,000 negative parent edges and 12,330 positive edges. The signed-packet chain adds 333 gateway bridges with alternating signs: 167 positive and 166 negative. For each family, all pairs absent from the parent receive a uniform fill $J_0=+1$ or $J_0=-1$; parent edges retain their signs. Thus the graph is physically complete even though its departure from the uniform fill has a small-component structure.

The retained spins have the ordered labels $\mathcal P=(0,1,60,61)$. A boundary mask $b$ from 0 to 15 records their signs: bit $a$ is one when spin $\mathcal P_a$ is positive. Retaining the ordered mask makes the output conditional on an explicit physical boundary rather than only on its number of positive spins. Exact duplicate output files can share storage where the source proves equality; their boundary identities remain separately recorded. [N5-2, N5-7]

## Separating the collective interaction

A spin takes a value $s_i\in\{-1,+1\}$. Energy is the negative signed sum of pair products, and magnetization is the sum of the spins. With no local fields in these sources,

$$\displaystyle E(s)=-\sum_{i<j}J_{ij}s_i s_j,\qquad M(s)=\sum_i s_i.$$ 

The joint density $g(E,M,b)$ counts the assignments having those three coordinates. The uniform fill can be handled without materializing every pair during counting. Squaring the total magnetization gives

$$M^2=N+2\sum_{i<j}s_i s_j.$$ 

Writing each pair coupling as $J_{ij}=J_0+\Delta J_{ij}$ therefore gives the exact identity

$$E=E_c-\frac{J_0}{2}(M^2-N),\qquad E_c=-\sum_{i<j}\Delta J_{ij}s_i s_j.$$ 

The dense term is a function of one collective coordinate, $M$. All remaining configuration dependence is in the correction graph. A source edge equal to the fill has zero correction. A source edge opposite to it has correction +2 or -2. This identity changes the representation of the exact Hamiltonian; it does not discard any pair coupling or approximate its contribution.

For counting, let $k=(M+N)/2$ be the number of positive spins and $B=\sum_{i<j}|\Delta J_{ij}|$ the total absolute correction. The shifted correction index $t=(E_c+B)/2$ is an integer. The original coordinates are recovered by

$$M=2k-N,\qquad E=2t-B-\frac{J_0}{2}\bigl[(2k-N)^2-N\bigr].$$ 

The method must retain $k$ jointly with $t$. Summing over magnetization too early would destroy the association needed to restore the dense $M^2$ term. This is why the result is a joint density rather than merely a correction-energy histogram. [N5-2, N5-5]

## Local tables and exact composition

Within a component, each permitted spin assignment contributes a monomial $x^k y^t$. Its coefficient counts how often those local coordinates occur. Local tables retain gateway spins until their incident bridges are accounted for. Multiplying compatible component polynomials adds positive-spin counts and correction indices, while multiplying their exact integer multiplicities. Summing the gateway assignment joins the compatible cases.

The alternating bridge construction is particularly useful. A bridge whose sign equals the fill has zero correction, so it disappears from the correction graph. The remaining correction components contain at most two complete packets. They are assembled from gateway tables rather than by enumerating all $2^{30}$ assignments of a two-packet component. Repeated components share the same source-bound polynomial, and repeated powers and grouped boundary roots remove repeated arithmetic.

This produces one polynomial $G_b(x,y)$ for each retained boundary. Its coefficient at $(k,t)$ is the desired configuration count after the coordinate decoding above. The correctness argument is constructive: each local assignment appears once in its local table, disjoint component products form every compatible global assignment, and gateway summation closes each interface once. No global configuration is sampled probabilistically. [N5-2, N5-3]

## Two encodings and exact GPU arithmetic

The two-variable polynomial is packed into a one-variable exponent using its known coordinate bounds. A common lattice step $d$ divides the correction indices. Put $u=t/d$ and $T=B/d$. The two maps are

$$\phi_K(k,u)=k(T+1)+u,\qquad \phi_T(k,u)=u(N+1)+k.$$ 

Both are injective on the admitted coordinate rectangle. Division with remainder restores the original coordinates, and output decoding rejects coordinates outside the declared bounds. The two layouts make the same joint counts take different coefficient positions and multiplication layouts. Their agreement tests packing, reconstruction and decoding at the scale of the completed object.

The GPU route multiplies integer polynomials using number-theoretic transforms modulo suitable primes. It then reconstructs the nonnegative integer coefficients by the Chinese remainder theorem. The product of the selected moduli is strictly greater than the full coefficient bound. Each reconstructed coefficient therefore has a unique value in the admitted interval. The stored counts are exact integers; floating-point transforms are not used for them.

N5000 required an enlarged reconstruction buffer. The successor backend admits eighty 64-bit limbs, or 5,120 bits; the N5000 route uses seventy-nine limbs. The serialized count field has 626 bytes, followed with its exact energy and magnetization coordinates to give a 634-byte raw record. The resource planner admits the transform arrays, host output arrays, writer concurrency and disk reserve before the full run. This mattered because exact coefficient growth and output volume remain real costs even when the source factorization is compact. [N5-1, N5-2, N5-4, N5-5]

## Validation of the completed density

Each boundary table satisfies conditional magnetization closure. If $r(b)$ is the number of positive retained spins, the count at fixed total positive-spin number $k$ must be

$$\sum_E g(E,2k-N,b)=\binom{N-4}{k-r(b)}.$$ 

The writer checks this identity for every admitted $k$. It is stronger than checking only the total $2^{4996}$ because it constrains every magnetization marginal. The energy moments are derived directly from the source couplings and fixed boundary, independently of the polynomial products. To see their content, write the fixed-boundary energy as a constant $c_b$, linear terms $a_v s_v$ on free spins, and pair terms $-J_{uv}s_us_v$. Under the uniform distribution of the free spins, these distinct spin monomials are orthogonal. With $A=2^{N-4}$, the exact checks are

$$\sum_{E,M}g=A,\qquad \sum_{E,M}Eg=A c_b,$$

$$\sum_{E,M}E^2g=A\left(c_b^2+\sum_{v\notin\mathcal P}a_v^2+\sum_{\substack{u<v\\u,v\notin\mathcal P}}J_{uv}^2\right).$$

Here $c_b=-\sum_{u<v\in\mathcal P}J_{uv}s_us_v$ and $a_v=-\sum_{p\in\mathcal P}J_{vp}s_p$. These source identities constrain the total mass, first energy moment and second energy moment without using the product coefficients as their answer key.

The host output stage writes the exact coordinates and integer multiplicities, checks their widths and support, computes canonical bucket digests, flushes the files, and rereads each complete durable raw file to confirm its hash. Production compares all 96 pairs of independently packed encodings on canonical digest, record count and moments. The preparatory qualification records 75 checks including CPU-equal coefficients at 3,000-, 4,000- and 5,000-bit widths and small source/encoding cases. The largest packet/-1 boundary pilot passed in both encodings before admission of full production.

A cheap portable replay supplies an additional concrete comparison. Recomputing the packet/+1 control on the CPU reproduced all 32 encoding/boundary rows in 37.768777 seconds, matching the canonical and raw record hashes, moments and counts. That replay verifies the analytically simple control through the public route. It does not replace the full six-source production, whose other cases retain their own exact checks and paired-encoding records. [N5-1, N5-3, N5-5, N5-8]

## The computation and its preserved data

Full production completed 192 logical rows and all 96 encoding pairs in 2,824.215 seconds, about 47 minutes. The recorded machine was an RTX PRO6000 Blackwell system with 97,887 MiB of device memory, about 27.2 CPU equivalents, 187,999,997,952 bytes of host RAM and a 4 TB container disk. The largest pilot recorded a process allocation of 83,785 MiB of GPU memory. These are the conditions of one completed execution, not a fitted general runtime law.

Before production, the source-bound compiler encountered the generic 4,096-variable admission ceiling. The completed successor normalized and authenticated the explicit frozen N5000 parent graphs while retaining the generic solver's existing admission policy. The failed preparation remains in provenance. Its relevance is the exact source-binding correction that enabled the finished run; it is not the result of the N5000 campaign.

Lossless zstd compression and byte deduplication reduced the completed files to 89 unique compressed contents. The archive is 609,671,270,157 bytes, compared with 1,045,145,366,546 distinct raw bytes. Compression took 1,260.611 seconds. Each compressed shard was decompressed and checked against its production raw hash. The manifest preserves every logical boundary alias, source, plan, record count, canonical digest and raw hash.

The frozen source-input restoration is a separate completed achievement in the chain. When an earlier backup path was absent, all sixteen original input files were reconstructed byte-identically from the retained source grammar and original construction receipts. The restored parent JSON, coupling bitstreams and manifests match their original SHA256 identities, including their original serialization details. No N5000 bulk output was lost. The final restoration uses the native GEN3 checkpoint route, and earlier restoration attempts remain preserved.

Later custody records complete the data chain. Batches 001 and 002 have Drive size and SHA256 verification. The T500 download records verify batches 003 through 006, with batches 005 and 006 adding 32 shards and 203,896,054,295 bytes in the final stage. All 89 shards and 609,671,270,157 compressed bytes have recorded external custody. The completed final-download record supersedes the early all-batches download hold in the original archive README. These statements cite the retained verification receipts; they do not claim a fresh reread of the full archive during this manuscript revision. [N5-1, N5-6, N5-7, N5-9, N5-10, N5-11, N5-12, N5-13, N5-15]

## What the result makes available

Once $g(E,M,b)$ is available, a uniform field can be applied by replacing $E$ with $E-hM$. The partition function for a fixed retained boundary is then the exact finite sum

$$Z_b(\beta,h)=\sum_{E,M}g(E,M,b)\exp\!\bigl[-\beta(E-hM)\bigr].$$ 

Boundary fields, partial boundary closure, fixed-magnetization questions and added uniform pair couplings likewise operate on retained coordinates. These operations reuse a completed count rather than enumerate the spins again. The multiplicities remain exact even when an exponential or thermodynamic readout is evaluated numerically with its own precision contract.

The scale increase from N2000 to N5000 is substantive because the larger output retains the same detailed finite observables across 12,497,500 physical pair interactions. The reason it is tractable is also explicit: the collective magnetization removes the uniform complete interaction from the hard local bookkeeping, while repeated bounded correction components control the remaining factorization. The result establishes this exact computation for the six specified sources. It is not a universal exact solver for arbitrary dense frustrated graphs, and the single production timing does not establish an asymptotic runtime exponent. [N5-2, N5-7, N5-16]

## N5000 thermal ordering and retained boundary memory

### A separately defined thermal family

Later N5000 calculations reuse the exact correction polynomials to determine ordering, fluctuations and boundary response. The thermal question requires an explicit normalization. In the archived unit-fill Hamiltonian, the collective term and sparse correction both have their original integer strengths. Dividing that whole Hamiltonian by $N$ scales both terms. The later fixed-sparse-strength family instead uses

$$H_{N,\kappa}=-\frac{M^2-N}{2N}+\kappa C_N,\qquad \kappa\ge0,\qquad N=20+30m.$$

Here $C_N=2\sum_{\text{negative edges}}s_i s_j$ for the signed positive-fill sources; the packet control has $C_N=0$. The dense pair coefficient is $1/N$, while the sparse correction has fixed strength $\kappa$. The choice $\kappa=1/N$ recovers whole scaling of the original positive-fill source. Holding $\kappa$ fixed defines the thermal extension used in the transition theorem. This source distinction makes the later physical results interpretable without changing the original integer counts. [N5-14]

Let $F(y)$ be the partition function of one repeated correction component in dimensionless auxiliary field $y$, including its actual sparse Boltzmann factor. The signed-packet motif has $n=15$ spins and the chain motif has $n=30$; a fixed boundary root and a five-spin tail complete each finite source. Gaussian decoupling of the collective term gives the bulk variational pressure

$$\sup_{y\in\mathbb R}\Phi_{\beta,\kappa}(y),\qquad
\Phi_{\beta,\kappa}(y)=-\frac{y^2}{2\beta}+\frac1n\log\frac{F(y)}{F(0)}.$$

The inverse temperature $\beta$ is in the declared model units. Define the repeated-component magnetization per spin and zero-field susceptibility by

$$m_0(y)=\frac1n\partial_y\log F(y),\qquad \chi=m_0'(0).$$

A stationary point satisfies $y=\beta m_0(y)$, and an extremal macroscopic state has magnetization $m_*=y_*/\beta$. The finite root and tail contribute only $O(1)$ to $\log Z$ on each compact field interval. They therefore leave the limiting bulk maximization unchanged while remaining present in the finite conditional weights and boundary-memory observables. The bound $F(y)/F(0)\le e^{n|y|}$ controls the distant Gaussian tails. [N5-14]

### The first global ordering transition

The exact source factors reduce the ordering question to rational functions of two bounded variables. Put $a=\tanh(2\beta\kappa)$ and $v=\tanh y$, and define

$$P(a,v)=1+(-a^3+2a^2-3a)v^2+a^2v^4.$$

Up to positive field-independent constants, the repeated factors are

$$F_{\mathrm{packet}}(y)\propto\cosh^{15}y,$$

$$F_{\mathrm{signed}}(y)\propto\cosh^{15}y(1-av^2)^3,$$

$$F_{\mathrm{chain}}(y)\propto\cosh^{30}y(1-av^2)^4P(a,v).$$

The chain factor has a four-spin path and four negative pairs in its correction core, together with free correction spins. It is not a thirty-spin path. The source-factorization identities were checked against the frozen generating polynomials. The resulting susceptibilities are

$$\chi_{\mathrm{packet}}=1,\qquad
\chi_{\mathrm{signed}}=1-\frac{2a}{5},\qquad
\chi_{\mathrm{chain}}=\frac{30-14a+4a^2-2a^3}{30}.$$

A local threshold alone would leave open a first-order transition caused by a distant maximum before that threshold. The completed derivation closes that gap by proving the global response inequality $m_0(y)<\chi y$ for every $y>0$. Its algebraic certificate uses the polynomial

$$S_4(x)=1+\frac{x}{3}+\frac{x^2}{5}+\frac{x^3}{7}+\frac{x^4}{9}.$$

For each signed family, the exact rational response satisfies

$$\chi S_4(v^2)-\frac{m_0(y)}{v}
=\frac{v^2Q_f(a,v^2)}{D_f(a,v)},$$

where the denominators are

$$D_{\mathrm{signed}}=1575(1-av^2),\qquad
D_{\mathrm{chain}}=4725(1-av^2)P(a,v).$$

Both are positive on $0\le a\le1$ and $0\le v<1$. The numerators have bidegrees $(2,4)$ and $(7,6)$ in $(a,x)$, where $x=v^2$. Expanding them in the Bernstein basis on the unit square gives 15 and 56 nonnegative rational coefficients, respectively. All 71 coefficients and the exact reconstruction of the power-basis polynomials are retained. Because each Bernstein basis function is nonnegative on that square, this proves $Q_f\ge0$ throughout the parameter domain. It is an exact finite certificate of a continuum statement. [N5-14]

The strictly positive remainder in the series for the inverse hyperbolic tangent gives

$$\frac{\operatorname{atanh}v}{v}>S_4(v^2),\qquad 0<v<1.$$

Together with $\chi\ge3/5$, the certificate therefore proves $m_0(y)<\chi y$. Consequently, when $\beta\chi\le1$, the derivative $\Phi'(y)=m_0(y)-y/\beta$ is strictly negative for $y>0$. Evenness makes zero the unique global maximizer, including at equality. When $\beta\chi>1$, the origin has positive curvature, so a nonzero maximizing pair has larger pressure. Thus the unique solution of

$$\beta_c\chi(\beta_c,\kappa)=1$$

is the **first global ordering transition** for every fixed finite $\kappa\ge0$ in these specified families. Maximizers satisfy $|y_*|\le\beta$; as $\beta$ decreases to $\beta_c$, compactness and uniqueness of the critical maximizer force $y_*\to0$. The negative fourth cumulant supplies a nondegenerate square-root onset. The stronger route through global concavity of $m_0$ is false at exact retained counterexamples; it is not needed for this successful first-onset proof. The conclusion concerns the first transition, with no claim to classify every remote stationary point at larger inverse temperature. [N5-14]

| Fixed correction strength $\kappa$ | Signed-packet $\beta_c$ | Chain $\beta_c$ |
|---:|---:|---:|
| $0$ | 1.000000000000 | 1.000000000000 |
| $1/8$ | 1.122873781777 | 1.136842176652 |
| $1/4$ | 1.295422047875 | 1.310642690959 |
| $1/2$ | 1.581042157548 | 1.582234699504 |
| $1$ | 1.663814710634 | 1.663815941534 |
| $2$ | 1.666663067473 | 1.666663067475 |

The exact susceptibility difference is $\chi_{\mathrm{chain}}-\chi_{\mathrm{signed}}=-a(1-a)^2/15$. Hence the chain threshold is strictly higher for finite positive $\kappa$, and both approach $5/3$ as $\kappa\to\infty$. The table reports rounded values from separately retained directed critical brackets. [N5-14]

### Critical fluctuations and a nonzero boundary response

At the exact critical temperature, let $c_4<0$ be the fourth cumulant per spin of the repeated component. The pressure near zero has a stabilizing quartic term $\Phi(y)=-by^4+O(y^6)$ with $b=-c_4/24>0$. The previously established global uniqueness controls the complement of a neighborhood of zero, and the Gaussian bound controls the distant tail. Rescaling $u=N^{1/4}y$ then gives

$$\sqrt N\,\left\langle\left(\frac MN\right)^2\right\rangle
\longrightarrow
\frac{\sqrt{24/(-c_4)}}{\beta_c^2}
\frac{\Gamma(3/4)}{\Gamma(1/4)}.$$

For the chain at $\kappa=1$, the amplitude is 0.546951358570. At the finite map's twelve-decimal rational critical centers, the computed N5000 value of $\langle(M/N)^2\rangle$ is 0.0077033393, compared with 0.0038595576 at N20000. The exact-critical asymptotic amplitude and the rounded finite input temperatures have distinct definitions and retained numerical receipts. Finite systems remain smooth; their curves are compared with the limiting transition rather than described as finite singularities. [N5-14]

The fixed retained root supplies a second physical consequence. Let $R_b(y)$ be its exact boundary factor including its correction Boltzmann weights. Below and at onset, concentration of the common integral at zero gives

$$\frac{Z_b}{Z_0}\longrightarrow\frac{R_b(0)}{R_0(0)}.$$

The common finite tail and normalization cancel. Applying the declared boundary protocol to these strictly positive limiting weights gives the memory limit directly, without extrapolating numerical data to enormous $N$. At exact chain criticality with $\kappa=1$, the preparation, between-reading and within-interval differences are respectively

$$-0.430454602216,\qquad
0.000189921648477,\qquad
0.000344266087525.$$

These numbers refer to an explicit observation protocol. A heat-bath generator changes one retained bit at a time with rate $Q_{j,b}=w_j/(w_b+w_j)$ for weights $w_b=Z_b/Z_0$, and its columns sum to zero. Readings retain the least-significant bit, postselect even boundary states, and use intervals $\delta=1/3$. The preparation difference compares the state-zero start with conditional equilibration inside its initial coarse class. The between-reading difference measures the effect of conditional resets at intermediate readings. The within-interval difference compares those resets with evolution under the coarse generator. Conditional equilibration inside one class is not a globally stationary mixture. The nonzero limiting differences quantify retained boundary response under this declared clock; physical seconds and physical transition rates are separate source assignments. [N5-14]

The finite map evaluates 158 complete directed cases, including N5000 and N20000, correction strengths and temperature offsets, packet controls and four N200 cases. Complete 128-bit Arb integrals retain explicit infinite tails; 84 direct comparisons expand the N200 exact spectrum and sum Gibbs weights at 192 bits. The method therefore checks the new thermal normalization and finite readouts independently of the Gaussian integration. [N5-14]

### Exact occupied windows and measured probability

A later counting calculation retained a selected thermally occupied N5000 window: 69,904 final records, including 2,056 exact zeros. The window covers positive-spin numbers $2372\le k\le2628$, aligned-negative-edge indices $0\le t_{\mathrm{a}}\le16$, and all sixteen boundary assignments. Here $t_{\mathrm{a}}=L-d_{\mathrm{neg}}$ counts aligned negative edges, with $L$ their total number and $d_{\mathrm{neg}}$ the disagreeing-edge count. This $t_{\mathrm{a}}$ is defined for the later window calculation and is not the general shifted correction coordinate used earlier in the chapter. Its original unit-fill labels satisfy

$$M=2k-N,\qquad
E=4t_{\mathrm{a}}-2L-\frac{M^2-N}{2}.$$

The shortcut is mathematical. Reversing the chain's defect variable produces a repeated factor with monomial constant coefficient $\widehat f_0=32X^6$. If $q_n$ is the coefficient of the reversed defect variable at degree $n$ in its $m$th power, logarithmic differentiation gives

$$q_0=(32X^6)^m,\qquad
n\widehat f_0q_n=\sum_{i=1}^{7}\bigl((m+1)i-n\bigr)\widehat f_iq_{n-i}.$$

Every polynomial division is exact and checked for zero remainder. Only sixteen recurrence steps are needed for the N5000 window. The remaining pair, free spins and boundary root are then contracted exactly. A separate GPU calculation uses the original defect encoding and modular transforms; all 17,800 intermediate coefficients agree across the N5000 and N20000 windows before final root contraction. Global reversal agrees on all 275,104 final records. Exact zeros are preserved as source-imposed forbidden coordinates. [N5-14]

The N5000 CPU coefficient stage took 0.268194 seconds; the corresponding GPU route took 0.651927 seconds, with another 4.259603 seconds for common root contraction, output and mass evaluation. This short aligned-index regime favors the direct CPU recurrence. It complements the GPU's usefulness for the original much larger full-joint coefficient problem; the measured requests and timing boundaries are explicit. [N5-14]

For a window $W$, probability is evaluated against the **complete** partition function of the thermal family:

$$\Pr(W)=\frac1Z\sum_{(k,t_{\mathrm a},b)\in W}g(k,t_{\mathrm a},b)
\exp\!\left[\frac{\beta((2k-N)^2-N)}{2N}
-\beta\kappa(4t_{\mathrm a}-2L)\right].$$

| N5000 temperature offset $\beta-\beta_c$ | Captured Gibbs probability | Omitted Gibbs probability |
|---:|---:|---:|
| $-0.03$ | 53.607483% | 46.392517% |
| $0$ | 37.267444% | 62.732556% |
| $+0.03$ | 17.264479% | 82.735521% |

The exact counts capture substantial probability at and below the transition. Above onset, the ordered magnetization peaks move away from the window centered at zero, reducing its coverage. Both captured and omitted probabilities are retained as directed intervals. No uncomputed count is silently replaced by zero, and the selected window is not treated as the whole density. The complete N5000 joint construction, the global first-onset proof and the exact occupied window are three substantive completed results with separate output definitions and derivation chains. [N5-14, N5-16]
