# **DOBRUSHIN’S ERGODICITY COEFFICIENT FOR MARKOV OPERATORS ON CONES** 

STEPHANE GAUBERT AND ZHENG QU[´] 

ABSTRACT. Doeblin and Dobrushin characterized the contraction rate of Markov operators with respect the total variation norm. We generalize their results by giving an explicit formula for the contraction rate of a Markov operator over a cone in terms of pairs of extreme points with disjoint support in a set of abstract probability measures. By duality, we derive a characterization of the contraction rate of consensus dynamics over a cone with respect to Hopf’s oscillation seminorm (the infinitesimal seminorm associated with Hilbert’s projective metric). We apply these results to Kraus maps (noncommutative Markov chains, representing quantum channels), and characterize the ultimate contraction of the map in terms of the existence of a rank one matrix in a certain subspace. 

## 1. INTRODUCTION 

A basic result in the theory of Markov chains, due to Doeblin and Dobrushin, is the characterization of the contraction rate of a Markov operator acting on a space of measures equipped with the total variation norm. Consider in particular a finite Markov chain with transition (row stochastic) matrix _A_ ∈ R _[n]_[×] _[n]_ . The associated Markov operator is the map ν �→ ν _A_ from R _[n]_ to R _[n]_ , where the elements of R _[n]_ are thought of as row vectors. The set of probability measures can be identified to the standard simplex P := { ν ∈ R _[n]_ | ν _i_ ⩾ 0 for 1 ⩽ _i_ ⩽ _n_ , ∑ 1⩽ _i_ ⩽ _n_ ν _i_ = 1}, and the total variation norm is nothing but one half of the ℓ1 norm ∥·∥1 on R _[n]_ . We are interested in the Lipschitz constant of the map ν �→ ν _A_ , P → P with respect to the total variation norm, or equivalently, in the operator norm of the map ν �→ ν _A_ on the subspace of vectors of R _[n]_ with zero sum, equipped with the same norm, 

**==> picture [228 x 32] intentionally omitted <==**

The Doeblin-Dobrushin characterization reads 

**==> picture [303 x 56] intentionally omitted <==**

**==> picture [13 x 9] intentionally omitted <==**

The expression of δ ( _A_ ) given by (1) is known as _Doeblin contraction coefficient_ , see [LPW09], whereas the second expression, in (2), is known as _Dobrushin ergodicity coefficient_ [Dob56]. The latter is often used to show that δ ( _A_ ) < 1. This holds in particular if there is a _Doeblin state_ , i.e., a distinguished state _t_ such that _Ait_ ⩾ ε > 0 for all 1 ⩽ _i_ ⩽ _n_ . Then, δ ( _A_ ) ⩽ 1 − ε . 

A dual characterization of δ ( _A_ ) has been used in linear consensus theory. The latter is motivated by communication networks, control theory and parallel computation [Hir89, BT89, BGPS06, Mor05, BHOT05, OT09, AB09]. It studies dynamics of the form 

**==> picture [313 x 10] intentionally omitted <==**

where _Ak_ are row stochastic matrices, acting on column vectors. One looks for conditions which guarantee the convergence of _xk_ to a _consensus state_ , i.e., to a scalar multiple of the unit vector _e_ of R _[n]_ . To this end, one considers the 

_Date_ : October 4, 2014. 

> _Key words and phrases._ Markov operator, Dobrushin’s ergodicity ordered linear space, invariant measure, contraction ratio, consensus, noncommutative Markov chain, quantum channel, zero error capacity, rank one matrix. 

> The authors were partially supported by the PGMO Programme of FMJH and EDF, and by the programme “Ing´enierie Num´erique & S´ecurit´e” of the French National Agency of Research, project “MALTHY”, number ANR-13-INSE-0003. 

> An announcement of some of the present results has appeared in the Proceedings of the ECC’13 (European Control Conference), July 17-18 2013, Zurich. 

1 

following seminorm, sometimes called _diameter_ or _Tsitsiklis’ Lyapunov function_ [TBA86] 

**==> picture [98 x 17] intentionally omitted <==**

for all _x_ , _y_ ∈ R _[n]_ . It is known [CSM05] that 

**==> picture [273 x 25] intentionally omitted <==**

so that the Doeblin-Dobrushin ergodicity coincides with the one-step contraction rate of the consensus dynamics with respect to the diameter seminorm. We note that the same seminorm ∆ is a fundamental tool in PerronFrobenius theory, where it is called _Hopf’s oscillation_ [Hop63, Bus73] or _Hilbert’s seminorm_ [GG04]. 

In this paper, we extend the Doeblin-Dobrushin theorem, as well as the dual characterization (4), to Markov operators over cones. We consider a bounded linear self-map _T_ of a Banach space X , equipped with a normal cone C ⊂ X , and a _unit_ element **e** belonging to the interior of C . We say that _T_ is an _abstract Markov operator_ if _T_ (C ) ⊂ C and _T_ ( **e** ) = **e** . The _Hopf oscillation_ in the space X is the seminorm defined by 

**==> picture [176 x 11] intentionally omitted <==**

where ≼ denotes the partial order induced by C . Our main result reads: 

**Theorem 1.1** (Contraction rate in Hopf’s oscillation seminorm) **.** _Let T_ : X → X _be an abstract Markov operator. Then_ 

**==> picture [280 x 97] intentionally omitted <==**

This theorem follows from Theorems 5.1 and 6.2 below. The notations and notions used here are detailed in Section 5. In particular, _T_[⋆] denotes the adjoint of _T_ and we make use of the following norm, which we call _Thompson’s norm_ , 

**==> picture [146 x 11] intentionally omitted <==**

on the space X , and denote by ∥·∥[⋆] _T_[the dual norm. The notation][ P][(] **[e]**[) =][ {][µ][ ∈][C][ ⋆][:][⟨][µ][,] **[e]**[⟩][=][ 1][}][ refers to the abstract] _simplex_ of the dual Banach space X[⋆] of X , where C[⋆] is the dual cone of C ; extr denotes the extreme points of a set; ⊥ denotes a certain _disjointness_ relation, which will be seen to generalize the condition that two measures have disjoint supports. 

Taking X = R _[n]_ , C the standard positive cone R _[n]_ +[,][and] **[e]**[the][standard][unit][vector][(][1][,...,][1][)][⊤][,][we][recover][from] Theorem 1.1 the Doeblin-Dobrushin characterization (1),(2), as well as its dual form in linear consensus theory (4). Results related to Theorem 1.1 have previously appeared. In a finite dimensional setting, Reeb, Kastoryano, and Wolf [RKW11] gave a characterization analogous to the second equality of the above theorem without the disjointness condition. We refer to Remark 5.3 for a comparison. Also, Mukhamedov gave in [Muk13], in the setting of von Neumann algebras, a characterization similar to the same equality, still without the disjointness condition. He established some other properties of the ergodicity coefficient, and derived ergodic type theorems for nonhomogeneous Markov chains. 

Several motivations lead to consider Markov operators over cones which differ from the standard positive cone of R _[n]_ . 

First, Sepulchre, Sarlette, and Rouchon [SSR10] and independently, Reeb, Kastoryano and Wolf [RKW11] , have shown that tools from Perron-Frobenius theory (specially contraction results in different metrics over cones) provide a unifying general approach to address issues from quantum information and control. Here, quantum channels are represented by self-maps _T_ of the cone of positive semidefinite matrices, preserving the Loewner order, and the identity matrix. Relations with classical “consensus” theory were also addressed in [SSR10]. We derive further results, showing 

2 

**==> picture [232 x 31] intentionally omitted <==**

Then, we use the above formula to show that the convergence of a noncommutative consensus system or equivalently the ergodicity of a noncommutative Markov chain can be characterized by the existence of a rank one matrix in certain subspace of matrices (Theorem 7.7 and 7.8). Also, it follows from these results that an operator _T_ representing a quantum channel has a contraction rate of 1 (absence of contraction) with respect to Hopf’s oscillation if and only if there exists two distinguishable pure states, i.e., a quantum clique of cardinality 2 [BS08], or equivalently if the quantum channel has a positive zero-error capacity [MA05]. 

We also derive as a direct illustration a convergence result (geometric convergence of the iterates of the operator to a rank one operator, or geometric convergence to a “consensus state”) in Theorem 6.1. Actually, the present contraction results are useful more generally when considering iterates of random contractions. Then, almost sure convergence to a consensus state can be obtained by adapting ideas of Bougerol [Bou93], see the discussion in §6 below. We limited our convergence treatment here to simple illustrations of our results: we note that the question of proving “weak ergodicity results” in their best generality has been thoroughly studied, we refer the reader to the work of Mukhamedov [Muk13], and to the references therein. 

Our second and original motivation arises from _non-linear_ , rather than linear, Perron-Frobenius theory, i.e., from the study of non-linear maps over cones. In this setting, the interior of a cone C is equipped with _Hilbert’s projective metric_ , defined by: 

**==> picture [196 x 22] intentionally omitted <==**

Birkhoff [Bir57] characterized the contraction ratio with respect to _dH_ of a linear map _T_ preserving the interior C[0] of the cone C , 

**==> picture [162 x 54] intentionally omitted <==**

This fundamental result, which implies that a linear map sending the cone C into its interior is a strict contraction in Hilbert’s metric, can be used to derive the Perron-Frobenius theorem from the Banach contraction mapping theorem, see [Bus73, KP82, EN95] for more information. 

The generalization of Birkhoff’s theorem to non-linear maps, and in particular, the computation of the Lipschitz constant of nonlinear maps with respect to Hilbert’s projective metric, has important applications (including population dynamics), and it has motivated several works, specially the one of Nussbaum [Nus94], who observed that _dH_ is the weak Finsler metric obtained when taking ω (·/ **e** ) to be the infinitesimal distance at point **e** . In other words, 

**==> picture [134 x 23] intentionally omitted <==**

where the infimum is taken over piecewise _C_[1] paths γ : [0, 1] → C[0] such that γ (0) = _x_ and γ (1) = _y_ . He deduced that the contraction ratio, with respect to Hilbert’s projective metric, of a nonlinear map _f_ : C[0] → C[0] that is positively homogeneous of degree 1 (i.e. _f_ ( λ _x_ ) = λ _f_ ( _x_ ) for all λ > 0), restricted to a geodesically convex subset _U_ ⊂ C[0] , can be expressed in terms of the Lipschitz constants of the linear maps _Df_ ( _x_ ) with respect to a family of Hopf’s oscillation seminorms: 

**==> picture [307 x 77] intentionally omitted <==**

We recognize in κ ( _x_ ) a variant of the δ ( _A_ ), in which the domain and range of _A_ are equipped with different unit elements, namely _x_ and _f_ ( _x_ ). Our characterization carries over to this case. In particular, 

3 

Theorem 5.1 below gives an explicit formula for κ ( _x_ ), which, in combination with Nussbaum’s characterization (5) allows one to compute the contraction rate of a non-linear map with respect to Hilbert’s projective metric. 

## 2. THOMPSON’S NORM AND HILBERT’S SEMINORM 

We start by some preliminary results. Throughout the paper, (X , ∥·∥) is a real Banach space. Denote by X[⋆] the dual space of X . For any _x_ ∈ X and _q_ ∈ X[⋆] , denote by ⟨ _q_ , _x_ ⟩ the value of _q_ ( _x_ ). Let C ⊂ X be a closed pointed convex cone with nonempty interior C0 , in particular, α C ⊂ C for α ∈ R[+] , C + C ⊂ C and C ∩ (−C ) = 0. The partial order ≼ induced by C on X is defined as follows: 

**==> picture [82 x 10] intentionally omitted <==**

For _x_ ≼ _y_ 

**==> picture [114 x 11] intentionally omitted <==**

For _x_ ∈ X and _y_ ∈ C0 

(7) 

**==> picture [122 x 23] intentionally omitted <==**

Observe that since _y_ ∈ C0, and since C is closed and pointed, the two sets in (7) are non-empty, closed, and bounded from below and from above, respectively. In particular, _m_ and _M_ take finite values. 

For _x_ ∈ X and _y_ ∈ C0, we call _oscillation_ [Bus73] the difference between _M_ ( _x_ / _y_ ) and _m_ ( _x_ / _y_ ): 

**==> picture [118 x 11] intentionally omitted <==**

Let **e** denote a distinguished element in C0, which we shall call a _unit_ . For _x_ ∈ X 

∥ _x_ ∥ _T_ := max( _M_ ( _x_ / **e** ), − _m_ ( _x_ / **e** )) 

which we call _Thompson’s norm_ , with respect to the element **e** , and 

∥ _x_ ∥ _H_ := ω ( _x_ / **e** ) 

which we call _Hilbert’s seminorm_ with respect to the element **e** . 

_Remark_ 2.1 _._ These terminologies are motivated by the fact that Thompson’s part metric and Hilbert’s projective metric are Finsler metrics for which the infinitesimal distances at the point **e** ∈ C[0] are respectively given by ∥·∥ _T_ and ∥·∥ _H_ , see [Nus94]. The seminorm ∥·∥ _H_ is also called Hopf’s oscillation seminorm [Bus73]. Besides, it is clear that the unit **e** is an _order unit_ and Thompson’s norm ∥·∥ _T_ is the corresponding _order unit norm_ , see [Ell64, Alf71, Nag74]. 

We assume that the cone X is normal, that is, there is a constant _K_ > 0 such that 

**==> picture [104 x 11] intentionally omitted <==**

It is known that under this assumption the two norms ∥·∥ and ∥·∥ _T_ are equivalent, see [Nus94]. Therefore the space X equipped with the norm ∥·∥ _T_ is an order unit Banach space. Since Thompson’s norm ∥·∥ _T_ is defined with respect to a particular element **e** , we write (X , **e** , ∥·∥ _T_ ) instead of (X , ∥·∥ _T_ ). 

_Example_ 2.2 _._ We X = R _[n]_ , the standard positive cone C = R _[n]_ +[and the] unit vector **e** = **1** := (1,..., 1) _[T]_ . It can be checked that Thompson’s norm with respect to **1** is nothing but the sup norm 

**==> picture [98 x 15] intentionally omitted <==**

whereas Hilbert’s seminorm with respect to **1** is the so called _diameter_ : 

**==> picture [126 x 17] intentionally omitted <==**

_Example_ 2.3 _._ Let X = S _n_ , the space of Hermitian matrices of dimension _n_ and C = S[+] _n_[, the cone of positive semi-] definite matrices. Let the identity matrix _In_ be the unit element: **e** = _In_ . Then Thompson’s norm with respect to _In_ is nothing but the sup norm of the spectrum of _X_ , i.e., 

**==> picture [132 x 17] intentionally omitted <==**

4 

where λ ( _X_ ) := ( λ 1( _X_ ),..., λ _n_ ( _X_ )), is the vector of ordered eigenvalues of _X_ , counted with multiplicities, whereas Hilbert’s seminorm with respect to _In_ is the diameter of the spectrum: 

**==> picture [178 x 17] intentionally omitted <==**

3. ABSTRACT SIMPLEX IN THE DUAL SPACE AND DUAL UNIT BALL 

We denote by (X[⋆] , **e** , ∥· ∥[⋆] _T_[)][the][dual][space][of][(][X][ ,] **[e]**[,][∥· ∥] _[T]_[)][where][the][dual][norm][∥· ∥][⋆] _T_[of][a][continuous][linear] functional _z_ ∈ X[⋆] is defined by: 

∥ _z_ ∥ _T_[⋆][:][=][sup] ⟨ _z_ , _x_ ⟩ . ∥ _x_ ∥ _T_ =1 

The _abstract simplex_ 

(8) P( **e** ) := { µ ∈ C[⋆] | ⟨ µ , **e** ⟩ = 1} , 

where C[⋆] is the _dual cone_ of C : 

**==> picture [154 x 11] intentionally omitted <==**

_Remark_ 3.1 _._ For the standard positive cone (Example 2.2, X = R _[n]_ , C = R _[n]_ +[and] **[ e]**[ =] **[ 1]**[), the dual space][ X][⋆][is][ X][=][ R] _[n]_ itself and the dual norm ∥·∥[⋆] _T_[is the][ ℓ][1][ norm:] 

**==> picture [90 x 19] intentionally omitted <==**

The abstract simplex P( **1** ) is the standard simplex in R _[n]_ : 

**==> picture [124 x 20] intentionally omitted <==**

i.e., the set of probability measures on the discrete space {1,..., _n_ }. 

_Remark_ 3.2 _._ For the cone of semidefinite matrices (Example 2.3, X = S _n_ , C = S[+] _n_[and] **[ e]**[ =] _[ I][n]_[), the dual space][ X][⋆][is] X = S _n_ itself and the dual norm ∥·∥[⋆] _T_[is the trace norm:] 

**==> picture [160 x 21] intentionally omitted <==**

The simplex P( _In_ ) 

P( _In_ ) = { ρ ∈ S _[n]_ +[: trace][(][ρ][) =][ 1][}][.] 

The elements of this set are called _density matrices_ in quantum physics. They are thought of as noncommutative analogues of probability measures. 

By the duality between order unit and base normed spaces [Ell64], the space (X[⋆] , **e** , ∥·∥[⋆] _T_[)][ is a base normed space.] The abstract simplex P( **e** ) coincides with the _base_ and the dual norm ∥·∥[⋆] _T_[with the] _[ base norm]_[. We denote by] _[ B]_[⋆] _T_[(] **[e]**[)] the dual unit ball: 

_B_[⋆] _T_[(] **[e]**[) =][ {] _[x]_[ ∈][X][⋆][| ∥] _[x]_[∥][⋆] _T_[⩽][1][}][.] 

We denote by conv( _S_ ) the convex hull of a set _S_ . The next lemma relates the abstract simplex P( **e** ) to the dual unit ball _B_[⋆] _T_[(] **[e]**[)][. The proof can be found in [Ell64, Alf71].] 

**Lemma 3.3** ([Ell64]) **.** _The dual unit ball B_[⋆] _T_[(] **[e]**[)] _[ of the space]_[ (][X][⋆][,] **[e]**[,][∥·∥][⋆] _T_[)] _[, satisfies]_ 

(9) _B_[⋆] _T_[(] **[e]**[) =][ conv][(][P][(] **[e]**[)][∪−][P][(] **[e]**[))][.] 

_Remark_ 3.4 _._ Reeb, Kastoryano, and Wolf [RKW11] a _base_ B of a proper cone K in a dimensional vector space V , which coincides with the definition of our “abstract simplex”. They defined the _base norm_ of µ ∈ V with respect to B by: 

∥ µ ∥B = inf{ λ ⩾ 0 : µ ∈ λ conv(B ∪−B)}. 

_distinguishability norm_ of µ ∈ V by: 

**==> picture [286 x 18] intentionally omitted <==**

And Theorem 14 in their paper [RKW11] states that the distinguishability norm is equal to the base norm: 

(11) ∥ µ ∥ _M_ ˜ = ∥ µ ∥B . 

5 

be seen as a dual one to ours. 

## 4. CHARACTERIZATION OF EXTREME POINTS OF THE DUAL UNIT BALL 

A standard result of functional analysis shows that if W is a closed subspace of a Banach space (X , ∥·∥), then the quotient space X /W is a Banach space, canonically equipped with the _quotient norm_ 

**==> picture [78 x 15] intentionally omitted <==**

see [Con90, Chap. III, § 4]. The next lemma shows that when X is equipped with Thomspon’s norm, Hilbert’s seminorm coincides with the quotient norm of X /R **e** , up to a factor 2. 

**Lemma 4.1.** _For all x_ ∈ X _, we have:_ 

**==> picture [97 x 16] intentionally omitted <==**

_Proof._ The expression 

**==> picture [185 x 11] intentionally omitted <==**

is minimal when _M_ ( _x_ / **e** )+ λ = − _m_ ( _x_ / **e** ) − λ . Substituting the value of λ obtained in this way in ∥ _x_ + λ **e** ∥ _T_ , we arrive at the announced formula. □ 

**Lemma 4.2.** _The quotient normed space_ (X /R **e** , ∥·∥ _H_ ) _is a Banach space. Its dual is_ (M ( **e** ), ∥·∥[⋆] _H_[)] _[ where]_ M ( **e** ) := { µ ∈ X[⋆] |⟨ µ , **e** ⟩ = 0}, 

_and_ 

**==> picture [299 x 22] intentionally omitted <==**

_Proof._ It is shown in [Con90, Chap. III, Theorem 10.2] that if W is a closed subspace of a Banach space (X , ∥· ∥), the dual of the quotient space X /W can be identified isometrically to the space of continuous linear forms on X that vanish on W , equipped with the dual norm ∥·∥[⋆] of X[⋆] . Specializing this result to the case in which X is equipped with twice the Thompson norm and W = R **e** , and noting that multiplying the norm on the space X by a given positive factor divites the corresponding dual norm by the same factor, we obtain (12). □ 

The above lemma implies that the unit ball of the space (M ( **e** ), ∥·∥[⋆] _H_[)][, denoted by] _[ B]_[⋆] _H_[(] **[e]**[)] 

**==> picture [287 x 12] intentionally omitted <==**

_Remark_ 4.3 _._ In the case of the standard positive cone (X = R _[n]_ , C = R _[n]_ +[and] **[ e]**[ =] **[ 1]**[), Lemma 4.2 implies that for any] two probability measures µ , ν ∈ P( **1** ), the dual norm ∥ µ − ν ∥[⋆] _H_[is the total variation distance between][ µ][and][ ν][:] 

**==> picture [152 x 21] intentionally omitted <==**

Before giving a representation of the extreme points of _B_[⋆] _H_[(] **[e]**[)] _[ disjointness]_[ relation][ ⊥][on][ P][(] **[e]**[)][.] 

For all ν , π ∈ P( **e** ), we say that ν and π are _disjoint_ , denoted by ν ⊥ π , if 

**==> picture [45 x 21] intentionally omitted <==**

for all µ ∈ P( **e** ) such that µ ≽[ν] 2[and][ µ][≽][π] 2[.] 

_Example_ 4.5 _._ In the case of the standard positive cone (X = R _[n]_ , C = R _[n]_ +[and] **[ e]**[ =] **[ 1]**[), two][points][ ν][,][π][in][ P][(] **[1]**[)][ are] disjoint if and only if for all 1 ⩽ _i_ ⩽ _n_ , ν _i_ = 0 or π _i_ = 0 holds, meaning that ν and π , thought of as discrete probability measures, have disjoint supports. 

We have the following characterization of the disjointness property. 

**Lemma 4.6.** _Let_ ν , π ∈ P( **e** ) _. The following assertions are equivalent:_ 

- (a) ν ⊥ π _._ 

6 

(b) _The only elements_ ρ , σ ∈ P( **e** ) _satisfying_ 

**==> picture [60 x 8] intentionally omitted <==**

_are_ ρ = ν _and_ σ = π _._ 

_Proof._ (a)⇒ (b): Let any ρ , σ ∈ P( **e** ) such that 

**==> picture [62 x 8] intentionally omitted <==**

Then it is immediate that 

ν + σ = π + ρ . 

Let µ =[ν][+] 2[σ] =[π][+] 2[ρ][. Then][ µ][∈][P][(] **[e]**[)][,][ µ][≽][ν] 2[and][ µ][≽][π] 2[. Since][ ν][⊥][π][, we obtain that][ µ][=][ν][+] 2[π][. It follows that][ ρ][=][ ν] and σ = π . (b)⇒ (a): Let any µ ∈ P( **e** ) such that µ ≽[ν] 2[and][ µ][≽][π] 2[. Then] 

**==> picture [122 x 11] intentionally omitted <==**

From (b) we know that 2 µ − π = ν . 

**==> picture [8 x 8] intentionally omitted <==**

· We denote by extr( ) the set of extreme points of a convex set. 

**Proposition 4.7.** _The set of extreme points of B_[⋆] _H_[(] **[e]**[)] _[, denoted by]_[ extr] _[B]_[⋆] _H_[(] **[e]**[)] _[, is characterized by:]_ extr _B_[⋆] _H_[(] **[e]**[) =][ {][ν][ −][π][ |][ ν][,][π][∈][extr][P][(] **[e]**[)][,][ν][⊥][π][}][.] 

_Proof._ It follows from (9) that every point µ ∈ _B_[⋆] _T_[(] **[e]**[)][ can be written as] 

**==> picture [50 x 8] intentionally omitted <==**

with _s_ + _t_ = 1, _s_ , _t_ ⩾ 0, ν , π ∈ P( **e** ). Moreover, if µ ∈ M ( **e** ), then 

**==> picture [148 x 11] intentionally omitted <==**

thus _s_ = _t_ = 2[1][. Therefore every][ µ][∈] _[B]_[⋆] _T_[(] **[e]**[)][∩][M][ (] **[e]**[)][ can be written as] 

**==> picture [108 x 20] intentionally omitted <==**

Therefore by (13) we proved that 

(14) _B_[⋆] _H_[(] **[e]**[) =][ {][ν][ −][π][ :][ ν][,][π][∈][P][(] **[e]**[)][}][.] 

Now let ν , π ∈ extr P( **e** ) and ν ⊥ π . We are going to prove that ν − π ∈ extr _B_[⋆] _H_[(] **[e]**[)][.][Let][ν][1][,][π][1][,][ν][2][,][π][2][ ∈][P][(] **[e]**[)][ such] that 

Then 

**==> picture [114 x 50] intentionally omitted <==**

By Lemma 4.6, the only possibility is 2 ν = ν 1 + ν 2 and 2 π = π 1 + π 2. Since ν , π ∈ extr P( **e** ) we obtain that ν 1 = ν 2 = ν and π 1 = π 2 = π . Therefore ν − π ∈ extr _B_[⋆] _H_[(] **[e]**[)][.] Now let ν , π ∈ P( **e** ) such that ν − π ∈ extr _B_[⋆] _H_[(] **[e]**[)][. Assume by contradiction that][ ν][is not extreme in][ P][(] **[e]**[)][ (the case] in which π is not extreme can be dealt with similarly). Then, we can find ν 1, ν 2 ∈ P( **e** ), ν 1 ̸= ν 2, such that ν =[ν][1][+] 2[ν][2] . It follows that 

**==> picture [90 x 19] intentionally omitted <==**

where ν 1 − π , ν 2 − π are distinct elements of _B_[⋆] _H_[(] **[e]**[)][, which is a contradiction. Next we show that][ ν][⊥][π][. To this end,] let any ρ , σ ∈ P( **e** ) such that 

**==> picture [62 x 8] intentionally omitted <==**

Then 

**==> picture [172 x 20] intentionally omitted <==**

If σ = π , then ν − σ = ν − π and this contradicts the fact that ν − π is extremal. Therefore σ = π and ρ = ν . From Lemma 4.6, we deduce that ν ⊥ π . 

□ 

7 

_Remark_ 4.8 _._ In the case of standard positive cone (X = R _[n]_ , C = R _[n]_ +[and] **[ e]**[ =] **[ 1]**[), the set of extreme points of][ P][(] **[1]**[)][ is] the set of standard basis vectors { _ei_ } _i_ =1,..., _n_ . The extreme points are pairwise disjoint. 

_Remark_ 4.9 _._ In the case of cone of semidefinite matrices (X = S _n_ , C = S[+] _n_[and] **[ e]**[ =] _[ I][n]_[), the set of extreme points of] P( _In_ ) is 

**==> picture [154 x 11] intentionally omitted <==**

which are called _pure states_ in quantum information terminology. Two extreme points _xx_[∗] and _yy_[∗] are disjoint if and only if _x_[∗] _y_ = 0. To see this, note that if _x_[∗] _y_ = 0 then any Hermitian matrix _X_ such that _X_ ≽ _xx_[∗] and _X_ ≽ _yy_[∗] should satisfy _X_ ≽ _xx_[∗] + _yy_[∗] . Hence by definition _xx_[∗] and _yy_[∗] are disjoint. Inversely, suppose that _xx_[∗] and _yy_[∗] are disjoint and consider the spectral decomposition of the matrix _xx_[∗] − _yy_[∗] , i.e., there is λ ⩽ 1 and two orthonormal vectors _u_ , _v_ such that _xx_[∗] − _yy_[∗] = λ ( _uu_[∗] − _vv_[∗] ). It follows that _xx_[∗] − _yy_[∗] = _uu_[∗] − ((1 − λ ) _uu_[∗] + λ _vv_[∗] ). By Lemma 4.6, the only possibility is _yy_[∗] = (1 − λ ) _uu_[∗] + λ _vv_[∗] and _xx_[∗] = _uu_[∗] thus λ = 1, _u_ = _x_ and _v_ = _y_ . Therefore _x_[∗] _y_ = 0. 

## 5. THE OPERATOR NORM INDUCED BY HOPF’S OSCILLATION SEMINORM 

Consider two real Banach spaces X1 and X2. Let C1 ⊂ X1 and C2 ⊂ X2 be respectively two closed pointed convex normal cones with non empty interiors C1[0][and][ C] 2[ 0][. Let] **[ e]**[1][ ∈][C] 1[ 0][and] **[ e]**[2][ ∈][C] 2[ 0][. Then, we know from Section 4 that the] two quotient spaces (X1/R **e** 1, ∥· ∥ _H_ ) and (X2/R **e** 2, ∥· ∥ _H_ ) are Banach spaces. The dual spaces of (X1/R **e** 1, ∥· ∥ _H_ ) and (X2/R **e** 2, ∥·∥ _H_ ) are respectively (M ( **e** 1), ∥·∥[⋆] _H_[)][ and][ (][M][ (] **[e]**[2][)][,][∥·∥][⋆] _H_[)][ (see Lemma 4.2).] Let _T_ be a continuous linear map from the space (X1/R **e** 1, ∥· ∥ _H_ ) to (X2/R **e** 2, ∥· ∥ _H_ ). The operator norm of _T_ , denoted by ∥ _T_ ∥ _H_ , is given by: 

**==> picture [17 x 9] intentionally omitted <==**

**==> picture [186 x 27] intentionally omitted <==**

_adjoint operator T_[⋆] : (M ( **e** 2), ∥·∥[⋆] _H_[)][ →][(][M][ (] **[e]**[1][)][,][∥·∥][⋆] _H_[)][ of] _[ T]_[is:] 

**==> picture [210 x 11] intentionally omitted <==**

The operator norm of _T_[⋆] , denoted by ∥ _T_[⋆] ∥[⋆] _H_[, is then:] 

**==> picture [121 x 21] intentionally omitted <==**

A classical duality result (see [AB99, § 6.8]) shows that an operator and its adjoint have the same operator norm. In particular, 

**==> picture [66 x 11] intentionally omitted <==**

**Theorem 5.1.** _Let T_ : X1 → X2 _be a bounded linear map such that T_ ( **e** 1) ∈ R **e** 2 _. Then,_ 

**==> picture [196 x 49] intentionally omitted <==**

_Moreover, the supremum can be restricted to the set of mutually disjoint extreme points:_ 

(16) 

**==> picture [209 x 62] intentionally omitted <==**

_Proof._ We already noted that ∥ _T_ ∥ _H_ = ∥ _T_[⋆] ∥[⋆] _H_[. Moreover,] 

**==> picture [118 x 30] intentionally omitted <==**

By the characterization of _B_[⋆] _H_[(] **[e]**[2][)][ in (14) and the characterization of the norm][ ∥·∥][⋆] _H_[in Lemma 4.2, we get] 

**==> picture [218 x 50] intentionally omitted <==**

For the second equality, note that 

**==> picture [214 x 44] intentionally omitted <==**

We next show that the supremum can be restricted to the set of extreme points. By the Banach-Alaoglu theorem, _B_[⋆] _H_[(] **[e]**[2][)][ is weak-star compact, and it is obviously convex. The dual space][ M][ (] **[e]**[2][)][ endowed with the weak-star topology] is a locally convex topological space. Thus by the Krein-Milman theorem, the unit ball _B_[⋆] _H_[(] **[e]**[2][)][,][which is][a][compact] convex set in M ( **e** 2) with respect to the weak-star topology, is the closed convex hull of its extreme points. So every element ρ of _B_[⋆] _H_[(] **[e]**[2][)][ is the limit of a net][ (][ρ][α][)][α][of elements in conv] � extr _B_[⋆] _H_[(] **[e]**[2][)] �. Observe now that the function 

**==> picture [242 x 20] intentionally omitted <==**

which is a sup of weak-star continuous maps is convex and weak-star lower semi-continuous. This implies that 

**==> picture [180 x 46] intentionally omitted <==**

Using the characterization of the extreme points in Proposition 4.7, we get: 

**==> picture [343 x 51] intentionally omitted <==**

_Remark_ 5.2 _._ When X1 [0, **e** 1] is the convex hull of the set of its extreme points, hence, the supremum over the variable _x_ ∈ [0, **e** 1] in (16) is attained at an extreme point. Similarly, if X2 is of finite dimension, the suprema over ( ν , π ) in the same equation are also attained, because the map ϕ in the proof of the previous theorem, which is a supremum of an equi-Lipschitz family of maps, is continuous (in fact, Lipschitz). 

_Remark_ 5.3 _._ Theorem 5.1 should be compared with a result of [RKW11] which can be stated as follows. 

_Proposition_ 5.4 (Proposition 12 in [RKW11]) _. Let_ V , V[′] _be two finite dimensional vector spaces and L_ : V → V[′] _be a linear map and let_ B ⊂ V _and_ B[′] ⊂ V[′] _be bases. Then_ 

**==> picture [355 x 26] intentionally omitted <==**

**==> picture [469 x 88] intentionally omitted <==**

Hence, by comparison with [RKW11], the additional information here is the equality between the contraction ratio in Hilbert’s seminorm of a unit preserving linear map ∥ _T_ ∥ _H_ , and the contraction ratio with respect to the base norms of the dual base preserving map ∥ _T_[⋆] ∥[⋆] _H_[. The latter is the primary object of interest in quantum information theory whereas] the former is of interest in the control/consensus literature [TBA86, Mor05]. We also proved that the supremum 

9 

in (18) can be restricted to pairs of _disjoint_ extreme points ν , π . Finally, the expression of the contraction rate as the last supremum in Theorem 5.1 leads here to an abstract version of Dobrushin’s ergodic coefficient, see Eqn (2) and Corollary 7.1 below. 

([Bir57]) **.** _Hilbert’s projective metric_ between two elements _x_ and _y_ of C0 is 

(19) _dH_ ( _x_ , _y_ ) = log( _M_ ( _x_ / _y_ )/ _m_ ( _x_ / _y_ )) . 

(The notation _M_ (·/·) 

Consider a linear operator _T_ : X1 → X2 such that _T_ (C1[0][)][ ⊂][C] 2[ 0][. Following [Bir57, Bus73], the] _[ projective diameter]_ of _T_ 

diam _T_ = sup{ _dH_ ( _T_ ( _x_ ), _T_ ( _y_ )) : _x_ , _y_ ∈ C1[0][}][.] 

Birkhoff’s contraction formula [Bir57, Bus73] states that the oscillation ratio equals to the contraction ratio of _T_ and they are related to its projective diameter. 

**Theorem 5.6** ([Bir57, Bus73]) **.** 

**==> picture [256 x 28] intentionally omitted <==**

_T_[⋆] : 

diam _T_[⋆] = sup{ _dH_ ( _T_[⋆] ( _u_ ), _T_[⋆] ( _v_ )) : _u_ , _v_ ∈ C2[⋆][\][0][}][.] 

Note that diam _T_ = diam _T_[⋆] . This is because 

**==> picture [235 x 56] intentionally omitted <==**

**Corollary 5.7** (Compare with [RKW11]) **.** _Let T_ : X1 → X2 _be a bounded linear map such that T_ ( **e** 1) ∈ R **e** 2 _and T_ (C1[0][)][ ⊂][C] 2[ 0] _[, then:]_ 

**==> picture [202 x 22] intentionally omitted <==**

_Proof._ 

**==> picture [296 x 30] intentionally omitted <==**

Then we apply Birkhoff’s contraction formula. 

**==> picture [8 x 8] intentionally omitted <==**

_Remark_ 5.8 _._ Reeb et al. [RKW11] showed in a different way that 

**==> picture [108 x 22] intentionally omitted <==**

∥ _T_[⋆] ∥[⋆] _H_[=][ ∥] _[T]_[∥] _[H]_[is established,] the latter inequality follows from Birkhoff’s contraction formula. 

6. APPLICATION TO MARKOV OPERATORS ON CONES AND DISCRETE TIME CONSENSUS DYNAMICS 

A bounded linear map _T_ : X → X is a _Markov operator_ with respect to a unit vector **e** in the interior C[0] of a closed convex pointed cone C ⊂ X if it satisfies the two following properties: 

(i) _T_ is positive, i.e., _T_ (C ) ⊂ C . 

(ii) _T_ preserves the unit element **e** , i.e., _T_ ( **e** ) = **e** . 

The case when ∥ _T_ ∥ _H_ < 1 or equivalently ∥ _T_[⋆] ∥[⋆] _H_[<][ 1][is][of][special][interest;][the][following theorem shows that][the] iterates of _T_ converge to a rank one projector with a rate bounded by ∥ _T_ ∥ _H_ . 

10 

**Theorem 6.1** (Geometric convergence to consensus/invariant measure) **.** _Let T_ : X → X _be a Markov operator with respect to the unit element_ **e** _. If_ ∥ _T_ ∥ _H_ < 1 _or equivalently_ ∥ _T_[⋆] ∥[⋆] _H_[<][ 1] _[, then there is]_[ π][∈][P][(] **[e]**[)] _[ such that for all x]_[ ∈][X] ∥ _T[n]_ ( _x_ ) −⟨ π , _x_ ⟩ **e** ∥ _T_ ⩽ (∥ _T_ ∥ _H_ ) _[n]_ ∥ _x_ ∥ _H_ , 

_and for all_ µ ∈ P( **e** ) 

**==> picture [122 x 11] intentionally omitted <==**

_Proof._ The intersection 

**==> picture [138 x 11] intentionally omitted <==**

is nonempty (as a non-increasing intersection of nonempty compact sets), and since ∥ _T_ ∥ _H_ < 1 and 

**==> picture [128 x 11] intentionally omitted <==**

this intersection must be reduced to a real number { _c_ ( _x_ )} ⊂ R depending on _x_ , i.e., 

**==> picture [150 x 14] intentionally omitted <==**

Thus for all _n_ ∈ N, 

**==> picture [196 x 11] intentionally omitted <==**

**==> picture [204 x 11] intentionally omitted <==**

It is immediate that: 

_c_ ( _x_ ) **e** = _n_ lim→ ∞ _[T][ n]_[(] _[x]_[)] 

from which we deduce that _c_ : X → R is a continuous linear functional. Thus there is π ∈ X[⋆] such that _c_ ( _x_ ) = ⟨ π , _x_ ⟩. Besides it is immediate that ⟨ π , **e** ⟩ = 1 and π ∈ C[⋆] because 

_x_ ∈ C ⇒ _c_ ( _x_ ) **e** ∈ C ⇒ _c_ ( _x_ ) ⩾ 0 ⇒⟨ π , _x_ ⟩ ⩾ 0. 

Therefore π ∈ P( **e** ). Finally for all µ ∈ P( **e** ) and all _x_ ∈ X we have 

**==> picture [189 x 35] intentionally omitted <==**

Hence 

∥( _T_[⋆] ) _[n]_ ( µ ) − π ∥ _H_[⋆][⩽][(][∥] _[T]_[∥] _[H]_[)] _[n]_[.] 

□ 

A time invariant discrete time consensus system can be described by 

(20) 

**==> picture [122 x 11] intentionally omitted <==**

The main concern of consensus theory is the convergence of the orbit _xk_ to a _consensus state_ , which is represented by a scalar multiple of the unit element **e** . The dual system of (20) represents a homogeneous discrete time Markov system: 

(21) 

π _k_ +1 = _T_[⋆] ( π _k_ ), _k_ = 1, 2,... . 

One of the central issues in Markov chain study is the ergodic property, i.e., the convergence of the distribution π _k_ to an _invariant measure_ , given by a fixed point of _T_[⋆] . Theorem 6.1 shows that if ∥ _T_ ∥ _H_ < 1 or equivalently ∥ _T_[⋆] ∥[⋆] _H_[<][ 1,] then the consensus system (20) is globally convergent and the homogeneous Markov chain (21) is ergodic. A time-dependent consensus system is described by 

**==> picture [296 x 11] intentionally omitted <==**

where { _Tk_ : _k_ ⩾ 1} is a sequence of Markov operators sharing a common unit element **e** ∈ C[0] . Then if there is an integer _p_ > 0 and a constant α < 1 such that for all _i_ ∈ N 

**==> picture [86 x 11] intentionally omitted <==**

then the same lines of proof of Theorem 6.1 imply the existence of π ∈ P( **e** ) such that for all { _xk_ } satisfying (22), 

**==> picture [164 x 15] intentionally omitted <==**

11 

Moreover, if { _Tk_ : _k_ ⩾ 1} is a stationary ergodic random process, then the almost sure convergence of the orbits of (22) to a consensus state can be deduced by showing that 

**==> picture [101 x 11] intentionally omitted <==**

for some _p_ > 0, see Bougerol [Bou93]. The ergodicity of a inhomogeneous Markov chain can be studied in a dual approach. Hence, in Markov chain and consensus applications, a central issue is to compute the operator norm ∥ _T_ ∥ _H_ of a Markov operator _T_ . 

A direct application of Theorem 5.1 leads to following characterization of the operator norm. 

**Theorem 6.2 .** _Let T_ : X → X _be a Markov operator with respect to_ **e** _. Then,_ 

**==> picture [260 x 24] intentionally omitted <==**

_Proof._ Since _T_ ( **e** ) = **e** , we have: 

**==> picture [342 x 70] intentionally omitted <==**

_Example_ 6.3 _._ Let us specialize Theorem 6.2 to the case of the standard positive cone of R _[n]_ (Example 2.2). Then, a Markov operator R _[n]_ → R _[n]_ is of the form _T_ ( _x_ ) = _Ax_ , where _A_ is a row-stochastic matrix. We get 

**==> picture [174 x 23] intentionally omitted <==**

**==> picture [132 x 26] intentionally omitted <==**

_Remark_ 6.4 _._ Consider the time-variant linear consensus system: 

(23) _xk_ +1 = _Akxk_ , _k_ = 1, 2,... , 

where { _Ak_ } is a sequence of stochastic matrices. Moreau [Mor05] showed that if all the non-zero entries of the matrices { _Ak_ } are bounded from below by a positive constant α > 0 and if there is _p_ ∈ N such that for all _i_ ∈ N there is a node connected to all other nodes in the graph associated to the matrix _Ai_ + _p_ ... _Ai_ +1, then the system (23) is globally uniformly convergent. These two conditions imply exactly that there is a Doeblin state associated to the matrix _Ai_ + _p_ ... _Ai_ +1. The uniform bound α is to have an upper bound on the contraction rate, more precisely, 

**==> picture [157 x 11] intentionally omitted <==**

## 7. APPLICATIONS TO NONCOMMUTATIVE MARKOV OPERATORS 

X = S _n_ , C = S[+] _n_[and] **[ e]**[ =] _[ I][n]_[, Example 2.3).] A completely positive unital linear map Φ : S _n_ → S _n_ is characterized by a set of matrices { _V_ 1,..., _Vm_ } satisfying 

(24) 

**==> picture [51 x 25] intentionally omitted <==**

such that the map Φ is given by: 

**==> picture [300 x 26] intentionally omitted <==**

12 

The matrices { _V_ 1,..., _Vm_ } are called _Kraus operators_ . It is clear that Φ : S _n_ → S _n_ operator of Φ is given by: 

**==> picture [120 x 26] intentionally omitted <==**

It is a completely positive and trace-preserving map, called Kraus map. The map Φ and Ψ represent a purely quantum channel [SSR10, RKW11]. In particular, the adjoint map Ψ is trace-preserving and acts on density matrices. The operator norm of Φ : S _n_ /R _In_ → S _n_ /R _In_ is the contraction ratio with respect to the diameter of the spectrum: 

**==> picture [168 x 25] intentionally omitted <==**

The operator norm of the adjoint map Ψ : P( _In_ ) → P( _In_ ) is the contraction ratio with respect to the trace norm (the total variation distance): 

**==> picture [160 x 26] intentionally omitted <==**

The valuesSpecializing Theorem 6.2 to Kraus maps, we obtain the noncommutative version of Dobrushin’s ergodicity coeffi- ∥ Φ ∥ _H_ and ∥ Ψ ∥[⋆] _H_[are the noncommutative counterparts of][ δ][(][·][)][.] cient. 

**Corollary 7.1 .** _Let_ Φ _be a completely positive unital linear map defined in_ (25) _. Then,_ 

**==> picture [383 x 31] intentionally omitted <==**

_Proof._ It can be easily checked that 

**==> picture [126 x 13] intentionally omitted <==**

Hence, Theorem 6.2 and Remark 4.9 yield: 

**==> picture [379 x 82] intentionally omitted <==**

from which (26) follows. 

_Remark_ 7.2 _._ For the noncommutative case, it is not evident whether more effective characterization of the contraction rate exists. Note that the dual operator norm was studied in quantum information theory, see [RKW11] and references therein. They provided a Birkhoff type upper bound (Corollary 9 in [RKW11]): 

**==> picture [108 x 11] intentionally omitted <==**

The value diam Ψ is not directly computable. This upper bound is equal to 1 if and only if diam Ψ = ∞ , which is satisfied if and only if there exist a pair of nonzero vectors _u_ , _v_ ∈ C _[n]_ such that: 

span{ _Viu_ : 1 ⩽ _i_ ⩽ _m_ } ̸= span{ _Viv_ : 1 ⩽ _i_ ⩽ _m_ }. 

**Corollary 7.3.** _The following conditions are equivalent:_ 

1. ∥ Φ ∥ _H_ = ∥ Ψ ∥[⋆] _H_[=][ 1][.] 

2. _There are nonzero vectors u_ , _v_ ∈ C _[n] such that_ 

**==> picture [136 x 12] intentionally omitted <==**

3. _There is a rank one matrix Y_ ⊂ C _[n]_[×] _[n] such that_ 

**==> picture [154 x 11] intentionally omitted <==**

13 

_Proof._ From Corollary 7.1 we know that ∥ Φ ∥ _H_ = 1 if and only if there exist an orthonormal basis { _x_ 1,..., _xn_ } and two vectors _u_ , _v_ ∈ C _[n]_ of norm 1 such that 

**==> picture [194 x 27] intentionally omitted <==**

This is equivalent to that for each _i_ ∈{1,..., _n_ }, either 

is true, or 

**==> picture [104 x 40] intentionally omitted <==**

is true. This is equivalent to 

**==> picture [142 x 11] intentionally omitted <==**

The equivalence between the second and the third condition is trivial by taking _Y_ = _vu_[∗] . □ 

_Remark_ 7.4 _._ The condition appearing in item 2 of Corollary 7.3 is equivalent to the positivity of the zero-error capacity [MA05], or to the existence of a quantum clique of cardinality 2 [BS08]. The latter problem is known to be QMA1 complete (proof of Theorem 3.2 in [BS08]). Thus, Corollary 7.3 relates the absence of contraction to a known hard problem in quantum computing. 

We consider a time-invariant noncommutative consensus system: 

(27) 

**==> picture [112 x 11] intentionally omitted <==**

where Φ is a completely positive unital map. To study the convergence of such system, Sepulchre, Sarlette and Rouchon [SSR10] proposed to study the contraction ratio 

**==> picture [142 x 18] intentionally omitted <==**

They applied Birkhoff’s contraction formula (Theorem 5.6) to give an upper bound on the contraction ratio α : 

**==> picture [92 x 11] intentionally omitted <==**

The following theorem is a direct corollary of Nussbaum [Nus94]. 

**Theorem 7.5.** _(Corollary of_ [Nus94, Thm2.3] _)_ 

**==> picture [228 x 25] intentionally omitted <==**

By this theorem, it is clear that the contraction ratio used in [SSR10] is an upper bound of the operator norm ∥ Φ ∥ _H_ : 

**==> picture [52 x 11] intentionally omitted <==**

We next provide an algebraic characterization of the global convergence of system (27), based on the result established in Corollary 7.3. Let us consider a sequence of matrix subspaces defined as follows: 

**==> picture [70 x 11] intentionally omitted <==**

**==> picture [251 x 11] intentionally omitted <==**

**Lemma 7.6.** _There is k_ 0 ⩽ _n_[2] − 1 _such that_ 

**==> picture [94 x 11] intentionally omitted <==**

_Proof._ It follows from (24) that H _k_ +1 ⊇ H _k_ for all _k_ ∈ N. Besides, if for some _k_ 0 ∈ N such that 

**==> picture [64 x 11] intentionally omitted <==**

then 

**==> picture [94 x 11] intentionally omitted <==**

This property also implies that if for some _k_ 0 ∈ N 

**==> picture [64 x 12] intentionally omitted <==**

then 

**==> picture [138 x 21] intentionally omitted <==**

□ 

Since the dimension of H _k_ can not exceed _n_[2] , the case 

H _k_ 0+1 ̸= H _k_ 0 , 

can not happen more than _n_[2] times. 

For all _k_ ∈ N, let G _k_ be the orthogonal complement of H _k_ . Then there is _k_ 0 ⩽ _n_[2] − 1 such that 

(28) G _k_ ⊇ G _k_ +1, ∀ _k_ ∈ N; G _k_ 0 = G _k_ 0+ _s_ , ∀ _s_ ∈ N 

**Theorem 7.7.** _The following conditions are equivalent:_ 

(1) _There exists k such that_ ∥ Φ _[k]_ ∥ _H_ < 1 _._ 

(2) _Every orbit of the system_ (27) _converges to an equilibrium co-linear to In._ 

(3) _The subspace_ ∩ _k_ G _k does not contain a rank one matrix._ 

(4) _There exists k_ 0 ⩽ _n_[2] − 1 _such that_ ∥ Φ _[k]_[0] ∥ _H_ < 1 _._ 

_Proof._ (1) ⇒ (2): We apply Theorem 6.1 to the application Φ _[k]_ . 

(2) ⇒ (1): Consider the quotient real linear space W := S _n_ /R _In_ . Since Φ ( _In_ ) = _In_ , Φ yields a quotient linear map W �→ W . We already observed in (15) that ∥ Φ ∥ _H_ is the operator norm induced by the norm ∥· ∥ _H_ on W . It follows that ∥ Φ 1 Φ 2∥ _H_ ⩽ ∥ Φ 1∥ _H_ ∥ Φ 2∥ _H_ holds for all linear maps Φ 1, Φ 2 : W → W , and so, by Fekete’s subadditive lemma, 

**==> picture [115 x 20] intentionally omitted <==**

Observe also that ∥ Φ ∥ _H_ ⩽ 1, so that ∥ Φ _[k]_ ∥ _H_ ⩽ 1 holds for all _k_ ⩾ 1. Then, if (1) is not true, we deduce that 

(29) 

**==> picture [82 x 19] intentionally omitted <==**

Now, for any real normed vector space (V , ∥· ∥V ), let VC = V + _i_ V V , and for any R-linear self-map _T_ of V , let _T_ C denote the complexification of _T_ , so that _T_ C( _x_ + _iy_ ) = _T_ ( _x_ )+ _iT_ ( _y_ ) for all _x_ , _y_ ∈ V . Recall that VC can be equipped with the norm 

∥ _x_ + _iy_ ∥VC = sup ∥ _x_ cos θ − _y_ sin θ ∥V 0⩽ θ ⩽2 π 

and that the operator norm of _T_ induced by the norm ∥·∥V on V , denoted by ∥ _T_ ∥V , as well as the operator norm of _T_ C induced by ∥·∥VC on VC, denoted by ∥ _T_ C∥VC, coincide, 

(30) 

**==> picture [76 x 11] intentionally omitted <==**

Consider in particular ( _Sn_ )C = _Sn_ + _iSn_ ≃ C _[n]_[×] _[n]_ , observe that ( _Sn_ /R _In_ )C ≃ C _[n]_[×] _[n]_ /C _In_ . It follows from (30) that 

**==> picture [117 x 14] intentionally omitted <==**

holds for all _k_ , and so, by (29), 

(31) 

**==> picture [78 x 18] intentionally omitted <==**

By Gelfand’s formula, the left-hand side of (31) is the spectral radius of the C-linear map Φ C : WC → WC. Hence, Φ C has an eigenvalue on the unit circle, meaning that there exists θ ∈ [0, 2 π ), _X_ , _Y_ ∈ _Sn_ , with _X_ + _iY_ ̸∈ C _In_ , such that 

**==> picture [132 x 13] intentionally omitted <==**

and so 

**==> picture [140 x 12] intentionally omitted <==**

for all _k_ ⩾ 1. Identifying the real and imaginary parts, we get Φ _[k]_ ( _X_ ) = cos( _k_ θ ) _X_ − sin( _k_ θ ) _Y_ + α _kIn_ and Φ _[k]_ ( _Y_ ) = sin( _k_ θ ) _X_ + cos( _k_ θ ) _Y_ + β _kIn_ , for some α _k_ , β _k_ ∈ R. Observe that since _X_ + _iY_ ̸∈ C _In_ , we have _X_ , _Y_ ̸∈ R _In_ . It follows that the orbit ( Φ _[k]_ ( _X_ )) _k_ ⩾1 does not converge to a scalar multiple of _In_ , contradicting (2). (3) ⇔ (1): Note that for all _k_ ∈ N, 

**==> picture [140 x 22] intentionally omitted <==**

By Corollary 7.3, we know that ∥ Φ _[k]_ ∥ _H_ = 1 if and only if the subspace G _k_ contains a a rank one matrix. Therefore , ∥ Φ _[k]_ ∥ _H_ = 1 for all _k_ ∈ N if and only if the subspace ∩ _k_ G _k_ contains a rank one matrix. 

15 

(3) ⇒ (4): By (28), there is _k_ 0 ⩽ _n_[2] − 1 such that G _k_ 0 = ∩ _k_ G _k_ . It follows that if (3) is true then there is _k_ 0 ⩽ _n_[2] − 1 such that G _k_ 0 does not contain a rank one matrix. Then by Corollary 7.3 we deduce that ∥ Φ _[k]_[0] ∥ < 1 if (3) is true. □ 

In a dual way, the above analysis also applies to the ergodicity study of noncommutative Markov chain given by: (32) Π _k_ +1 = Ψ ( Π _k_ ), _k_ = 1, 2,... 

Below is a dual version of Theorem 7.7. 

**Theorem 7.8.** _The following conditions are equivalent:_ 

- (1) _There exists k such that_ ∥ Ψ _[k]_ ∥[⋆] _H_[<][ 1] _[.]_ 

(2) _The Markov chain_ (32) _converges to a unique invariant measure regardless of initial distribution._ 

(3) _The subspace_ ∩ _k_ G _k does not contain a rank one matrix._ 

- (4) _There exists k_ 0 ⩽ _n_[2] − 1 _such that_ ∥ Ψ _[k]_[0] ∥[⋆] _H_[<][ 1] _[.]_ 

_Remark_ 7.9 _._ alently, the ergodicity of the noncommutative Markov chain (32) would be that there is _k_ 0 ⩽ _n_[2] − 1 such that 

## H _k_ 0 = C _[n]_[×] _[n]_ . 

Thus, checking the global convergence appears to be more tractable than checking the one step contraction (compare this characterization with the one of Corollary 7.3). 

||REFERENCES|
|---|---|
|[AB99]|C. D. Aliprantis and K. C. Border._Infnite Dimensional Analysis. A Hitchiker’s Guide_. Springer, 1999.|
|[AB09]|D. Angeli and P.-A. Bliman. Convergence speed of unsteady distributed consensus: decay estimate along the settling spanning-trees.|
||_SIAM J. Control Optim._, 48(1):1–32, 2009.|
|[Alf71]|E. M. Alfsen. _Compact convex sets and boundary integrals_. Springer-Verlag, New York, 1971. Ergebnisse der Mathematik und ihrer|
||Grenzgebiete, Band 57.|
|[BGPS06] <br>[BHOT05]|S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah. Randomized gossip algorithms._IEEE Trans. Inform. Theory_, 52(6):2508–2530, 2006.<br> V. D. Blondel, J. M. Hendrickx, A. Olshevsky, and J. N. Tsitsiklis. Convergence in multiagent coordination, consensus, and focking. In|
||_Proceedings of the joint 44th IEEE Conference on Decision and Control and European Control Conference_, pages 2996–3000. IEEE,|
||2005.|
|[Bir57]|G. Birkhoff. Extensions of Jentzsch’s theorem._Trans. Amer. Math. Soc._, 85:219–227, 1957.|
|[Bou93]|Ph. Bougerol. Kalman fltering with random coeffcients and contractions. _SIAM J. Control Optim._, 31(4):942–959, 1993.|
|[BS08]|S. Beigi and P. W. Shor. On the complexity of computing zero-error and holevo capacity of quantum channels. arxiv:0709.2090v3,|
||2008.|
|[BT89]|D. P. Bertsekas and J. N. Tsitsiklis._Parallel and distributed computation: numerical methods_. Prentice-Hall, Inc., Upper Saddle River,|
||NJ, USA, 1989.|
|[Bus73]|P. J. Bushell. Hilbert’s metric and positive contraction mappings in a Banach space._Arch. Rational Mech. Anal._, 52:330–338, 1973.|
|[Con90]|J. B. Conway._A course in functional analysis_, volume 96 of_Graduate Texts in Mathematics_. Springer-Verlag, New York, second edition,|
||1990.|
|[CSM05]|M. Cao, D. A. Spielman, and A. S. Morse. A lower bound on convergence of a distributed network consensus algorithm. In_Proc. of the_|
||_joint 44th IEEE Conference on Decision and Control and European Control Conference_, pages 2356–2361. IEEE, 2005.|
|[Dob56]|R. Dobrushin. Central limit theorem for non-stationary Markov chains. I._Teor. Veroyatnost. i Primenen._, 1:72–89, 1956.|
|[Ell64]|A. J. Ellis. The duality of partially ordered normed linear spaces._J. London Math. Soc._, 39:730–744, 1964.|
|[EN95]|S. P. Eveson and R. D. Nussbaum. An elementary proof of the Birkhoff-Hopf theorem._Math. Proc. Cambridge Philos. Soc._, 117(1):31–|
||55, 1995.|
|[GG04]|S. Gaubert and J. Gunawardena. The Perron-Frobenius theorem for homogeneous, monotone functions._Trans. of AMS_, 356(12):4931–|
||4950, 2004.|
|[Hir89]|M. W. Hirsch. Convergent activation dynamics in continuous time networks._Neural Networks_, 2(5):331–349, 1989.|
|[Hop63]|E. Hopf. An inequality for positive linear integral operators._Journal of Mathematics and Mechanics_, 12(5):683–692, 1963.|
|[KP82]|E. Kohlberg and J. W. Pratt. The contraction mapping approach to the Perron-Frobenius theory: why Hilbert’s metric?_Math. Oper. Res._,|
||7(2):198–210, 1982.|
|[LPW09]|D. A. Levin, Y. Peres, and E. L. Wilmer._Markov chains and mixing times_. American Mathematical Society, Providence, RI, 2009. With|
||a chapter by James G. Propp and David B. Wilson.|
|[MA05]|R. A. C. Medeiros and F. M. De Assis. Quantum zero-error capacity._Int. J. Quanum Inform._, 03:135, 2005.|
|[Mor05]|L. Moreau. Stability of multiagent systems with time-dependent communication links._IEEE Trans. Automat. Control_, 50(2):169–182,|
||2005.|
|[Muk13]|F. Mukhamedov. The Dobrushin ergodicity coeffcient and the ergodicity of noncommutative Markov chains. _J. Math. Anal. Appl._,|
||408(1):364–373, 2013.|
|[Nag74]|R. J. Nagel. Order unit and base norm spaces. In_Foundations of quantum mechanics and ordered linear spaces (Advanced Study Inst.,_|
||_Marburg, 1973)_, pages 23–29. Lecture Notes in Phys., Vol. 29. Springer, Berlin, 1974.|



16 

|[Nus88]|R. D. Nussbaum. Hilbert’s projective metric and iterated nonlinear maps._Mem. Amer. Math. Soc._, 75(391):iv+137, 1988.|
|---|---|
|[Nus94]|Roger D. Nussbaum. Finsler structures for the part metric and Hilbert’s projective metric and applications to ordinary differential|
||equations._Differential Integral Equations_, 7(5-6):1649–1707, 1994.|
|[OT09]|A. Olshevsky and J. N. Tsitsiklis. Convergence speed in distributed consensus and averaging. _SIAM J. Control Optim._, 48(1):33–55,|
||2009.|
|[RKW11]|D. Reeb, M. J. Kastoryano, and M. M. Wolf. Hilbert’s projective metric in quantum information theory._J. Math. Phys._, 52(8):082201,|
||33, 2011.|
|[SSR10]|R. Sepulchre, A. Sarlette, and P. Rouchon. Consensus in noncommutative spaces. In _Proceedings of the 49th IEEE Conference on_|
||_Decision and Control_, pages 6596–6601, Atlanta, USA, Dec 2010.|
|[TBA86]|J. N. Tsitsiklis, D. P. Bertsekas, and M. Athans. Distributed asynchronous deterministic and stochastic gradient optimization algorithms.|
||_IEEE Trans. Automat. Control_, 31(9):803–812, 1986.|



INRIA AND CMAP UMR 7641 CNRS, E[´] COLE POLYTECHNIQUE, 91128 PALAISEAU C´EDEX, FRANCE _E-mail address_ : Stephane.Gaubert@inria.fr 

SCHOOL OF MATHEMATICS, UNIVERSITY OF EDINBURGH, EDINBURGH, EH9 3FD, UK _E-mail address_ : zheng.qu@ed.ac.uk 

17 

