# N2000 Exact Joint Densities and Low Energy Physics

Six specified complete Ising graphs with 2,000 spins were solved exactly while retaining energy, magnetization, and four ordered boundary spins. The primary output contains **244,104,392 nonzero integer records**. The retained joint measure accounts for all $2^{2000}$ labelled spin configurations of each graph and supports later field and boundary-response questions without repeating the microscopic enumeration. The subsequent physical readouts determine exact ground energies and degeneracies, analytic residual-entropy limits along a declared size sequence, excitation gaps, field thresholds, and controlled low-temperature heat capacities. These are substantive results about how the specified interactions organize the states. [A1, pp 1-10]

The clearest physical comparison is between negative-fill signed packets and the same packets joined by alternating bridges. The bridges reduce the N2000 ground-state multiplicity by a factor of approximately $2.07536\times10^{20}$, lower the ground energy from $-10,840$ to $-10,974$, and reduce the first excitation gap from 10 to 4. On the commensurate sequence $N=60r$, their pairing of correction components halves the limiting ground-state entropy per spin from $\ln 2/15$ to $\ln 2/30$. The lower ground multiplicity and softer first excitation coexist: they describe different aspects of the exact spectrum. [A1, pp 5-8]

## The computed object and the six sources

An Ising spin is a binary variable taking the values $-1$ and $+1$. A spin configuration specifies the value at every labelled vertex. The Hamiltonian assigns an energy to each configuration using the pair couplings $J_{ij}$ and site fields $h_i$. In this chapter the sign convention is

$$E(s)=-\sum_{i<j}J_{ij}s_i s_j-\sum_i h_i s_i,\qquad M(s)=\sum_i s_i.$$

All six archived N2000 systems have zero fields and pair couplings $J_{ij}\in\{-1,+1\}$. Every physical pair is coupled, giving $\binom{2000}{2}=1,999,000$ nonzero interactions. Energies are dimensionless, and the complete interaction has not been divided by $N$. The sources therefore describe finite, unnormalized complete graphs. [A1, p 2, Eqs 1-2]

The retained boundary is the ordered vertex list $P=(0,1,60,61)$. A boundary mask $b\in\{0,\ldots,15\}$ records those four spin signs, with a set bit denoting $+1$. The joint density is the integer count

$$g(E,M,b)=\#\{s:E(s)=E,\ M(s)=M,\ s|_P=b\}.$$

Each nonzero record is one supported energy-magnetization-boundary bin and its multiplicity. It is not one separately visited global configuration. Each fixed boundary has total count $2^{1996}$; the 16 boundary sectors sum to $2^{2000}$. Keeping the boundary ordered preserves which retained vertex receives a later perturbation. [A1, p 2, Eqs 3-4]

The construction starts with packets. A full packet contains 15 vertices arranged in three complete five-vertex layers. Perfect matchings join successive layers, giving $3\binom{5}{2}+2(5)=40$ parent edges. At N2000 there are 133 full packets and one terminal five-vertex packet, with 5,330 unbridged parent edges in total. The inherited vertex labels are retained explicitly. In the signed family, one edge in every complete layer is negative: there are 400 negative and 4,930 positive parent edges. The chain adds 133 gateway bridges, alternating in sign from $+1$, so 67 bridges are positive and 66 negative. [A1, p 2]

For each of these three parents, all absent pairs receive a uniform fill $J_0=+1$ or $J_0=-1$, while existing parent edges retain their signs. This gives six sources. Packet with positive fill is the uniform ferromagnetic complete graph and supplies an analytic control. The other five sources contain frustrated cycles. They share the same spin count and complete physical connectivity, but their correction structures and spectra differ. [A1, pp 2, 4]

| Source | Negative physical pairs | Nonzero corrections | Correction bound $B$ | Largest implemented correction component |
|---|---:|---:|---:|---:|
| Packet positive fill | 0 | 0 | 0 | 15 |
| Packet negative fill | 1,993,670 | 5,330 | 10,660 | 15 |
| Signed packet positive fill | 400 | 400 | 800 | 15 |
| Signed packet negative fill | 1,994,070 | 4,930 | 9,860 | 15 |
| Signed packet chain positive fill | 466 | 466 | 932 | 30 |
| Signed packet chain negative fill | 1,994,003 | 4,997 | 9,994 | 30 |

The component sizes in the final column describe the implemented packet grouping. The original source retains all 1,999,000 interactions in every case. [A1, p 4, Table I]

## Why a complete graph admits an exact construction

The dense fill can be carried by a collective observable rather than represented as a large local factor. Magnetization is sufficient for that part because binary spins obey

$$M^2=N+2\sum_{i<j}s_i s_j.$$

Write the source as its uniform fill plus the exact correction $\Delta J_{ij}=J_{ij}-J_0$. The complete energy then becomes

$$E=E_c-\frac{J_0}{2}(M^2-N),\qquad E_c=-\sum_{i<j}\Delta J_{ij}s_i s_j.$$

This is an identity of the full source. Retaining $M$ preserves the association needed to restore the dense contribution after contracting the corrections. A correction-energy marginal alone would lose that association. [A1, p 2, Eqs 5-7]

The correction graph has bounded packet and gateway interfaces. Local integer generating functions count packet assignments according to positive-spin count, correction energy, and the signs still needed by a boundary or a gateway. A full packet has at most $2^{15}=32,768$ local assignments. The original preparation produced 22 local tables on two A100 devices and compared them with independently arranged CPU Gray-code enumeration. The public preparation route uses the CPU enumeration. [A1, pp 2-3]

For a bridge correction $\delta$ joining gateway spins $a$ and $c$, define its nonnegative shifted contribution

$$\tau_\delta(a,c)=\frac{|\delta|-\delta ac}{2}.$$

If $L_{r+1,c}(x,y)$ is the next packet table with gateway sign $c$, a forward contraction has the form

$$F_{r+1}(b,c)=\sum_{a=\pm1}F_r(b,a)L_{r+1,c}(x,y)y^{\tau_{\delta_r}(a,c)}.$$

The gateway sign is summed only after its interactions have been included. The four externally retained spins remain fixed throughout. When a bridge sign equals the fill, its correction vanishes; in the alternating chain this separates the correction graph into components of at most two full packets. These components are joined from gateway tables, without enumerating all $2^{30}$ assignments of a paired component. Repeated scalar components become polynomial powers, and a length-balanced product tree combines them with the retained component. [A1, p 3, Eqs 10-12]

For storage and polynomial composition, let $B=\sum_{i<j}|\Delta J_{ij}|$, let $k=(M+N)/2$, and shift correction energy to the integer coordinate $t=(E_c+B)/2$. A common lattice step $d$ permits $u=t/d$ and $T=B/d$. The two packed exponents are

$$\phi_K(k,u)=k(T+1)+u,\qquad \phi_T(k,u)=u(N+1)+k.$$

The global coordinate bounds make both maps injective. Quotient and remainder recover the coordinates, with out-of-range values rejected. FLINT polynomial arithmetic, accessed through python-flint, preserves arbitrary-precision integer coefficients throughout. [A1, pp 2-3, Eqs 8-14]

The counting argument follows the construction. A local table counts every permitted local assignment once. Multiplication combines disjoint assignments and adds their observables. Summing gateway signs includes every compatible bridge state once. Restoring the collective term gives the complete physical energy. The resulting coefficient is therefore the multiplicity of one unique $(E,M,b)$. The two exponent orders provide a strong implementation cross-check; they share local source tables and an arithmetic library, so their agreement is not described as agreement between two unrelated mathematical solvers. [A1, p 3]

## The completed joint output and its validation

The six primary outputs have sharply different support sizes even though they describe the same number of spins and physical pairs. [A1, p 5, Table II]

| Source | Primary nonzero records | Raw GB | Losslessly compressed GB |
|---|---:|---:|---:|
| Packet positive fill | 31,952 | 0.0083 | 0.0042 |
| Packet negative fill | 73,522,212 | 19.0423 | 11.1916 |
| Signed packet positive fill | 10,227,200 | 2.6489 | 1.7201 |
| Signed packet negative fill | 73,556,274 | 19.0511 | 11.1050 |
| Signed packet chain positive fill | 12,265,280 | 3.1767 | 2.1078 |
| Signed packet chain negative fill | 74,501,474 | 19.2959 | 11.2691 |
| Total | 244,104,392 | 63.2231 | 37.3979 |

Here GB means $10^9$ bytes. The exact primary byte totals are 63,223,097,516 raw and 37,397,887,721 compressed. Six cases, 16 boundaries, and two encodings give 192 emitted boundary rows representing 96 distinct case-boundary measures. A boundary row is a whole conditional measure; a record is one supported bin within it. Only one encoding is needed to distribute the measure, while both encodings' scientific receipts are retained. [A1, pp 4-5]

The production took 816.624947 seconds, including row emission and verified durable output. This timing excludes earlier preparation and pilot work and later compression and transfer. Fourteen workers used two FLINT threads each. The recorded CPU time was 16,159.967 seconds, equivalent to 19.79 average CPU cores during the measured interval, under a quota of 27.2. The configured memory limit was 465.66 GiB, and the largest recorded individual worker RSS was 18.69 GiB. Neither is a measured simultaneous fleet peak. RAM-staged rows were copied, fsynced, checksum-read back, and renamed before staging buffers were removed. [A1, pp 4-5]

Correctness was checked at several levels. For a boundary containing $r(b)$ positive spins, counting free-spin assignments gives the exact conditional magnetization identity

$$\sum_E g(E,2k-N,b)=\binom{N-4}{k-r(b)}.$$

This was checked at every allowed magnetization in every emitted boundary row. The first two energy moments were obtained separately from the couplings and fixed boundary signs. Summing all boundaries yields total count $2^{2000}$, first moment zero, and second moment $1,999,000\,2^{2000}$. Complete canonical row digests compare the full measures under the two encodings. N12 qualification uses independent joint variable elimination, N30 compares an uncompressed component route, CPU and GPU local tables agree, and a deliberately truncated binary is rejected. Source hashes, binary hashes, moment identities, and coordinate comparisons answer different questions and are retained together. [A1, pp 3-4, Eqs 16-19]

The positive-fill packet control is also available analytically. Its only supported energy at a given $M$ is $-(M^2-N)/2$, and its conditional multiplicity is the corresponding binomial coefficient. Each boundary has 1,997 records, giving 31,952 across all boundaries. A fresh public-runtime computation reproduced all 32 binary hashes for this control, including both encodings, in approximately 3.07 seconds after preparation. This demonstrates recovery of the control's algebra and serialization; the five nonuniform outputs have much larger support. [A1, p 4, Eqs 20-21]

## Exact ground states from the same source definitions

The paper's physical expansion reconstructed the published source motifs and computed their minimum energy and degeneracy at every magnetization. It used a smaller output than the original full joint measure and summed the retained boundaries. The two outputs have separate computational purposes and separate provenance. [A1, pp 5, 10]

A minimum/count state contains an energy $e$ and an exact multiplicity $c$. Combining alternatives keeps the lower energy and adds multiplicities only when the energies tie. Combining independent assignments adds energies and multiplies counts. Magnetization convolution combines packet states while retaining gateway signs until the bridges are processed. At fixed $M$, the collective fill energy is constant, so minimizing the correction energy and restoring the fill is exact. A final minimum over $M$ returns the global ground energy and sums all tied ground counts. [A1, p 5, Eqs 22-23]

Forward and reversed composition agreed at all 2,001 magnetization sectors for all six N2000 cases. Separate direct complete-pair sums verified every sector minimum and count at N5, N12, and N18. The N2000 ground levels also agree with the separately implemented truncated-spectrum calculation below. These readouts were computed from the source definitions; the revision did not claim that the 63 GB historical joint shards were reread for them. [A1, pp 5, 7-8]

| Source | Ground energy $E_0$ | Ground magnetization | Exact ground multiplicity $\Omega_0$ | $\ln\Omega_0/N$ |
|---|---:|---:|---:|---:|
| Packet positive fill | -1,999,000 | $\pm2000$ | 2 | 0.000346574 |
| Signed packet positive fill | -1,998,200 | $\pm2000$ | 2 | 0.000346574 |
| Signed packet chain positive fill | -1,998,068 | $\pm2000$ | 2 | 0.000346574 |
| Packet negative fill | -11,640 | 0 | 200771302400067787126123131419286927944400 | 0.047551493 |
| Signed packet negative fill | -10,840 | 0 | 200771302400067787126123131419286927944400 | 0.047551493 |
| Signed packet chain negative fill | -10,974 | 0 | 967403410158179609160 | 0.024160574 |

The counts are exact integers. The entropy densities are numerical evaluations of their logarithms. [A1, p 6, Table III]

For positive fill, the complete ferromagnetic background determines the ground ordering. Flipping a nonempty proper subset $S$ from an aligned state changes its energy by

$$\Delta E=2\sum_{i\in S,j\notin S}J_{ij}\geq 2\{|S|(N-|S|)-2n_-\},$$

where $n_-$ is the total number of negative pairs. At N2000 the three positive-fill cases have $n_-\leq466$ and $|S|(N-|S|)\geq1999$, so this change is strictly positive. The two globally inverted aligned states are the complete ground family. [A1, p 5, Eq 24]

For negative fill, the nonzero corrections are positive parent edges with $\Delta J=2$. Let $m_+$ be their number and let $c(s)$ count correction edges whose endpoint spins differ. The energy becomes

$$E=-\frac{N}{2}-2m_++4c(s)+\frac{M^2}{2}.$$

Correction components favor internal alignment, while the antiferromagnetic collective term penalizes nonzero magnetization. At N2000 all negative-fill ground states have $M=0$ and lie 20 units above the reference $E_{\mathrm{ref}}=-N/2-2m_+$. The terminal packet prevents simultaneous zero cut cost and zero magnetization. Exact contraction resolves that finite-size constraint rather than assigning independent orientations to packets after imposing $M=0$. [A1, p 5, Eq 25]

Changing 400 signed-layer edges shifts the unbridged negative-fill ground energy by 800 while leaving the minimizing multiplicity unchanged at this size. Adding alternating bridges then locks portions of that orientational freedom together. The exact ratio of unbridged to chain ground multiplicity is approximately $2.075362773088\times10^{20}$. This reduction is a property of the ground states and is not inferred from the number of stored joint bins. [A1, pp 5-6]

## An analytic residual entropy limit

Residual entropy measures how many configurations remain at the minimum energy. Its density is the logarithm of the ground multiplicity divided by the spin count. A commensurate sequence removes the terminal-packet effect and makes the counting mechanism explicit. Take $N=60r$ with negative fill. Each unbridged family has $N/15$ ferromagnetic correction components of size 15. Aligning each component gives zero cut cost, and zero magnetization requires half of the components up and half down. Thus

$$\Omega_{0,\mathrm{unbridged}}(N)=\binom{N/15}{N/30}.$$

In the chain, the positive bridges pair adjacent packets, while negative bridges equal the fill and contribute no correction. There are $N/30$ internally aligned size-30 correction components, and half must point each way:

$$\Omega_{0,\mathrm{chain}}(N)=\binom{N/30}{N/60}.$$

These configurations minimize the nonnegative cut and magnetization terms separately, so an excited component cannot supply another state at the same minimum. The ground energies are $-35N/6$ for packet, $-163N/30$ for signed packet, and $-11N/2$ for the chain. [A1, p 6, Eqs 26-30]

The central-binomial asymptotic gives

$$\lim_{r\to\infty}\frac{\ln\Omega_{0,\mathrm{unbridged}}(60r)}{60r}=\frac{\ln2}{15},\qquad
\lim_{r\to\infty}\frac{\ln\Omega_{0,\mathrm{chain}}(60r)}{60r}=\frac{\ln2}{30}.$$

The bridges halve the residual-entropy density because they double the number of spins locked into one orientable component. Exact size calculations at N120, N300, N600, N900, N1200, N1800, and N1980 agree with the formulas. N2000 is separate: its terminal packet requires additional cut configurations to attain $M=0$, and its entropy lies above the nearby commensurate trend. The limit is established on the declared $N=60r$ family rather than estimated from that endpoint. [A1, pp 6-7, Eq 31]

## Field thresholds and soft excitations

A uniform field couples to the retained magnetization. Let $e_*(M)$ be the exact minimum full energy at fixed $M$. In a field $H$, the ground energy is the lower envelope

$$E_0(H)=\min_M\{e_*(M)-HM\}.$$

The lower convex hull of the integer points $(M,e_*(M))$ gives rational field crossings. The positive-fill cases select $M=+2000$ for every $H>0$. In negative fill, $M=0$ persists until the first positive crossing: $H=3$ for both unbridged families and $H=17/5$ for the chain. Each first crossing connects $M=0$ and $M=10$. Any additional collinear minimizing sectors must be included when computing the degeneracy at the crossing. [A1, p 7, Eq 32]

The first zero-field excitation is a different question. The gap $\Delta_1$ is the energy difference between the ground state and the next supported energy. The ratio $\Omega_1/\Omega_0$ compares the multiplicities at those two levels. [A1, pp 5, 8]

| Negative-fill source | First gap $\Delta_1$ | $\Omega_1/\Omega_0$ | First positive field crossing |
|---|---:|---:|---:|
| Packet | 14 | 5 | 3 |
| Signed packet | 10 | 2 | 3 |
| Signed packet chain | 4 | 67 | $17/5$ |

The chain has a softer lowest excitation but a higher initial magnetization threshold. A low-energy excitation need not carry the magnetization required to become favorable in a uniform field. The exact data therefore resolve why the two response measures move in different directions. [A1, pp 5, 7-8]

## Exact low energy spectra and entropy resolution

The negative-fill energy decomposition also supports an exact bounded spectrum. Local polynomials track positive-spin count and the nonnegative cut count $c$. Their products retain all terms with $c\leq100$. Since cut contributions are nonnegative, a discarded term cannot later return to that range. At N2000 every state satisfying $E\leq E_{\mathrm{ref}}+400$ is represented. As $E_0=E_{\mathrm{ref}}+20$, the resulting complete energy window is $[E_0,E_0+380]$. It contains 184 supported levels for packet, 185 for signed packet, and 189 for the chain. [A1, p 7, Eq 33]

A separate C++ arbitrary-integer convolution produced these products. At N12 and N18, every supported level below the cutoff agrees with direct complete-graph enumeration for all three negative-fill sources. The N2000 ground levels agree exactly with the separate minimum/count calculation. The spectrum inside the retained window is exact; its construction does not approximate those coefficients. [A1, pp 7-8]

Microcanonical entropy is defined here as $S(E)=\ln g(E)$ with $k_B=1$. At increasing supported energies, successive entropy slopes are

$$\beta_i=\frac{S(E_{i+1})-S(E_i)}{E_{i+1}-E_i}.$$

Increasing slopes identify discrete nonconcavity. The analysis also constructs the smallest concave majorant within the window and measures its maximum vertical excess above the entropy points. Counts remain exact; the logarithms were evaluated with 70-digit precision. [A1, p 8, Eq 34]

The entropy curves have appreciable fine-level oscillation. To determine how much is tied to resolution, the analysis sums integer counts into fixed-width bins starting at $E_0$, then takes logarithms and places each value at its bin center. Only complete bins inside the known window are used. [A1, p 8]

| Negative-fill source | Exact levels | Width 4 | Width 8 | Width 16 |
|---|---:|---:|---:|---:|
| Packet | 7.26627 | 6.27352 | 3.21559 | 1.05748 |
| Signed packet | 3.19872 | 2.76719 | 1.64941 | 0.13406 |
| Signed packet chain | 9.25413 | 0.01281 | 0 | 0 |

The entries are maximum entropy deficits below the finite-window concave envelope. The chain has the largest deficit at individual levels, yet its nonconcavity vanishes at widths 8 and 16 in this window. Both unbridged families retain finite deficits under those coarse grainings. This establishes different shell sensitivity in the three exact spectra. A thermodynamic claim about ensemble inequivalence would additionally require a normalized size sequence and the relevant wider spectrum; the present calculation resolves the finite window and its stated resolutions. [A1, p 8, Table IV]

## Controlled low temperature heat capacity

The exact window is sufficient for a canonical calculation at low temperature because its omitted contribution can be bounded. Write the excitation energy as $\delta E=E-E_0$. The shifted window partition sum is

$$\widetilde Z_{\mathrm{win}}(\beta)=\sum_{E\leq E_0+380}g(E)e^{-\beta\delta E}.$$

Every N2000 energy is even, so the first omitted excitation is at least 382. The full configuration count is $2^{2000}$, while the retained ground contribution is $\Omega_0$. Therefore

$$\epsilon_Z=\frac{Z_{\mathrm{tail}}}{\widetilde Z_{\mathrm{win}}}\leq\frac{2^{2000}}{\Omega_0}e^{-382\beta}.$$

For $0<T\leq0.25$ in the archived energy units, this bound is below $e^{-190}$ even for the least-degenerate chain. A conservative bound using $\delta E_{\max}\leq1,999,000-E_0$ propagates the omitted mass into heat capacity at order $4\beta^2\delta E_{\max}^2\epsilon_Z$; at $T=0.25$ it is below $e^{-156}$ for every negative-fill case. These bounds control the omitted states. Numerical evaluation precision is handled separately. [A1, p 8, Eqs 35-36]

The expectation and heat capacity are evaluated from the retained counts with 70-digit exponentials and sums:

$$\langle\delta E\rangle=\frac{\sum\delta E\,g(E)e^{-\beta\delta E}}{\widetilde Z_{\mathrm{win}}},\qquad \frac{C}{k_B}=\beta^2\operatorname{Var}(\delta E).$$

| Negative-fill source | Total $C(0.25)/k_B$ |
|---|---:|
| Packet | $7.49644\times10^{-21}$ |
| Signed packet | $1.35947\times10^{-14}$ |
| Signed packet chain | $1.93020\times10^{-3}$ |

These are total heat capacities; division by N gives the per-spin quantity. The lowest gaps explain their separation through the leading expression

$$\frac{C}{k_B}\sim\left(\frac{\Delta_1}{T}\right)^2\frac{\Omega_1}{\Omega_0}e^{-\Delta_1/T}.$$

The chain's gap-4 level with multiplicity ratio 67 creates a much larger response at this temperature than the gap-10 and gap-14 levels of the unbridged sources. The comparison comes from exact low-energy counts with a quantified tail, rather than from output cardinality or a fitted response curve. [A1, p 8, Table V and Eqs 37-38]

## Reusing the full joint measure

The full joint output preserves more response information than either the ground-state or low-energy reductions. For a uniform field, its fixed-boundary partition function is

$$Z_b(\beta,H)=\sum_{E,M}g(E,M,b)e^{-\beta(E-HM)},\qquad Z=\sum_bZ_b.$$

It gives magnetization susceptibility $\chi=\beta\operatorname{Var}(M)$ and field-dependent heat capacity $C_H/k_B=\beta^2\operatorname{Var}(E-HM)$. A specified additional boundary energy $V(b)$ multiplies each $Z_b$ by $e^{-\beta V(b)}$. Because the source already contains its original boundary interactions, $V$ describes a perturbation of those interactions rather than adding their original contribution again. [A1, p 9, Eq 40]

The joint coordinates can also define a deliberate Hamiltonian extension with independently chosen collective and correction strengths:

$$E_{\kappa,\lambda}=\lambda E_c-\frac{\kappa}{2N}(M^2-N).$$

The correction energy is recoverable as $E_c=E+J_0(M^2-N)/2$. This permits a normalized collective term while keeping the correction term separately controlled. Dividing the entire archived energy by N would scale both parts and would be a different choice. Any phase comparison must state the new couplings and size sequence. [A1, p 9, Eq 39]

The completed contribution is an exact joint construction for six declared dense systems and a detailed physical reading of their low-energy organization. The graph's dense fill is retained through magnetization; its finite correction interfaces make the counting tractable. The output supports future uniform-field and boundary queries at arbitrary temperature with adequate numerical precision. Arbitrary internal site fields or individual pair changes require further observables unless they are expressible through the retained coordinates. The residual-entropy limits apply to the specified commensurate families, while the N2000 spectra and response values are exact finite-source results. [A1, pp 3, 9-10]

## Evidence and editorial verification

**A1** is Sean Brady, *Exact joint densities and low-energy structure of complete Ising graphs with tractable corrections*, dated 27 September 2026, attachment `libfile_72e347f72e948191b8d066bde1da9383`, local file `attachments/N2000_PRE_Expanded_Rev3(1).pdf`, 11 pages. Source construction and counting: pp 2-4, Eqs 1-21, Tables I-II. Ground states and analytic entropy: pp 5-7, Eqs 22-32, Table III. Low-energy spectra and thermal readout: pp 7-9, Eqs 33-40, Tables IV-V. Provenance and data availability: p 10; references: p 11.

The attachment identifies the original joint-density archive as DOI `10.5281/zenodo.22989862` and its frozen reproduction repository as commit `9773a4e4757e7503bfe279c04459c1356681220d` of `iwtbotiwtwot/frustrated-spin`. These are source identifiers reported by the attachment. This editorial task did not retrieve or rerun that archive. The paper itself separates the original full joint campaign from its later minimum/count, truncated-spectrum, entropy, field, and canonical readouts. Those later readouts reconstruct the published source definitions and do not claim a fresh bulk-shard readback. [A1, pp 10-11]

Bounded editorial arithmetic checks confirmed the six record counts sum to 244,104,392, the complete-pair count is 1,999,000, the positive-fill ground-energy shifts equal twice their negative-pair counts, the stated entropy densities follow from the exact ground multiplicities, and their ratio is $2.0753627730880107\times10^{20}$. Substitution into the supplied tail bound gives a chain logarithmic omitted-weight bound of approximately $-190.026786$ at $T=0.25$ and a logarithmic conservative heat-capacity bound of approximately $-156.840638$. These checks verify transcription and arithmetic and are not new scientific campaigns.
