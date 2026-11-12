# TWO-F03: complete signed-chain microscopic moments

Original source: signed_packet_chain_N005000 parent, positive complete fill1,
zero fields, ports[0,1,60,61], beta1/5000 and one attempt per physical site.
The original negative graph has668 isolated pairs,166 P4 paths and3000 free
vertices. Source0 lies in the untouched pair(0,1). The chain adds166 negative
bridges to the matching source, without changing that observed pair.

The FULL Hamiltonian is H=-(M²-N)/2+2sum_negative_edges s_i s_j. Retain observed
pair(s,t) explicitly. The bulk hasK2=667,K4=166,F=3000,n4998. Withq=exp(2/N),
r=q², a component configuration has relative weightr^(number of domain walls).
Thus its literal positive polynomials are

 p2=(1+x)²+2(r-1)x,
 p4=(1+x)^4+2(r-1)(r+2)x(1+x)²+2(r-1)²(r+1)x².

Every local configuration is retained (4pair,16path), including orientation
multiplicities. Deleting i pairs andj paths gives
P_ij(x)=p2^(K2-i) p4^(K4-j)(1+x)^F. Six arrays i+j<=2 suffice.

The actual self-excluded physical rate is
R(M,u,h)=1/[1+q^(u(M-u-2h))], whereh is the sum of that site's actual
negative-neighbor spins. Af=2sR(M,s,t) forA=-L andf=s0. Observed-site and
partner flips contribute

 S=R(M,s,t)[Af(M,s,t)-Af(M-2s,-s,t)]
  +R(M,t,s)[Af(M,s,t)-Af(M-2t,s,-t)].

Letd_+=Af(M,s,t)-Af(M-2,s,t), d_- analogously atM+2, and
g_+=R(M,1,0)d_+,g_-=R(M,-1,0)d_-,delta=g_+-g_-.
For literal bulk configurationc withl(c) plus spins, define

 B_c=sum_(verticesv in c)R(M,s_v,h_v)d_(s_v)-l(c)delta,
 C=S+F g_-+k delta.

At bulk plus countk, EXACTLY A²f=C+sum_c n_c B_c. This includes every
one of the5000 physical flips, its local field and its post-flip M. It is a
polynomial only for Gibbs contraction, not a dynamical magnetization quotient.

Define family insertion polynomials b_a(x)=sum_c w_c B_c x^l(c) and
c_a(x)=sum_c w_c B_c² x^l(c). The first moment ofsum nB is
sum_a K_a[x^k](b_a P_removed_a). Its square has the single-component term
sum_a K_a[x^k](c_a P_removed_a), SAME-family term
K_a(K_a-1)[x^k](b_a² P_removed_2a), and CROSS-family term
2K2K4[x^k](b2 b4 P_11). Together withC²+2C first moment this gives the exact
full Gibbs expectation of(A²f)². No mixed term is dropped.

For each observed pair andk, multiply by its weightr^(s!=t) exp(M²/(2N)),
whereM=2[k+(s+t+2)/2]-N, and normalize by the COMPLETE same partition.
The common absolute prefactor is exp[-1/2-2(668+3*166)/N], retained separately.
Thenmu0..mu4 are expectations of1,sAf,Af²,Af A²f,(A²f)².

Complete coefficient tail. Put y=x/(1+x)². Every removed-array polynomial is
(1+x)^n F(y), F(y)=(1+cy)^K2(1+ay+by²)^K4 with nonnegative coefficients.
For everyk, [x^k]x^d(1+x)^(n-2d)/binom(n,k)<=2^-d. Hence truncating atJ48
has a COMPLETE relative coefficient tail <=F(16)/32^49. The arrays retain
this outward, before signed observable contractions. The actual source tail
is below9.009e-62. The implementation uses directed Arb384, all literal local
rates and all six deletions. No full density archive or state array is built.

Independent qualifications. Native128-state N7 contains the observed pair,
one P4 andone free site. Its generator is built from literal full energies;
native full operator moments agree with all five adapter moments. Separately,
directed HOST full32768-state N15 has3pairs,2P4s,1free site, activating both
same-family and cross-family second inserts. Literal exp(dE/N) rates and full
A,A² actions agree with all five adapter intervals. These are qualification
models explicitly mapped to the original component laws, not relabeled N5000.

Actual N5000 host moments are approximately
(1,.9840415602952908,.9840415602952908,.9842322707000299,.9844261222147369).
The new native Gauss/Radau method consumes those complete moments; positive-cell
KL with its full tail gives microscopic stationary CMI atlag1/3 in
[3.41219962633e-6,3.41223131098e-6]nats. This is STRICTLY BELOW the retained
matching-source lower, by .251059%–.252913%. More negative bridges do not
monotonically increase this source/readout's finite-lag information.

Additional source diagnostic. Each unit heatbath complementA_j is an orthogonal
projection andAf=A0f. Thereforemu1=mu2 and
mu3-mu1=sum_(j!=0)||A_j A0f||². Directed actual partner contractions show the
other4998 sites carry99.97999635%of this hidden Dirichlet flow. This fraction
is NOT a decomposition ofCMI. The total hidden flow slightly increases in the
chain even while its finite CMI decreases, another nonmonotonic distinction.

All source files/hashes, literal negative edges, qualifications, tails and
native receipts remain in CHAIN_* artifacts, chain_moments.py and hidden_flow.py.
This establishes the finite original positive-fill chain result only; negative
fill, all-N CMI amplitudes and a physical-seconds assignment remain open.
