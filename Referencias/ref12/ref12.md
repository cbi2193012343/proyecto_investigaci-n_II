## Lipschitz continuous dynamic programming 

## with discount 

Jose M. Maroto[a] and Manuel Moran[b,*] 

> aDepartment of Estadística e Investigación Operativa II. 

Universidad Complutense, 28223 (Madrid), Spain. 

b Department of Fundamentos del Análisis Económico I. Universidad Complutense, 28223 (Madrid), Spain. 

*Corresponding author. PHONE: +34913942407, FAX: +34913942561. 

E-mail addresses: mmoranca@ccee.ucm.es (M. Moran[�] ), maroto@ccee.ucm.es. 

## April 13, 2005 

## Abstract 

We show that if the return function, the technological constraints and the transition function of a standard problem of stochastic dynamic programming with discount satisfy Lipschitz regularity assumptions, then the value function is Lipschitz regular. 

Keywords: Dynamic programming, optimization, optimal growth, renewable resources, non-smoothness. 

1 

## 1 Introduction 

The results of this paper stand for a class of dynamic optimization problems with in…nite horizon and discount, in a stochastic setting, as described by Stokey, Lucas and Prescott [29], chaps. 4, 9. 

It is well known that, under topological assumptions (compactness and continuity) on the data of the problem (i.e., state space, return function and technological constraint correspondence), the existence, uniqueness and continuity of the value function is guaranteed. 

The theory of dynamic programming with discount proceeds by completing the topological assumptions with a rather extensive block of assumptions, which we call standard assumptions, including concavity, smoothness and monotonicity of the data. Such assumptions guarantee the concavity, smoothness and numerical computability of the value function and optimal policy correspondence. In the non-random case they also guarantee the convergence of the optimal paths to an equilibrium state, and if noninterior optimal paths are ruled out, then a recursive computation of the optimal paths through Euler equations is possible. 

The examples in Section 4 show that all these nice properties, with exception of the existence and continuity of the value function, fail to hold under small departures from the standard assumptions. A variety of phenomena emerge there related with nonconcavity of the objective function, as countably many points of discontinuity and non-uniqueness, following a systematic pattern, in the optimal policy correspondence; discontinuities in the form of jumps upwards in the 

2 

marginal value function, synchronized with the discontinuities of the optimal policy correspondence (Example 18); asymptotic cyclic behavior of the optimal paths (Example 18). In these cases, not only do the properties derived from the standard assumptions are hopelessly lost, but also the numerical computation of the value function through Bellman operator iterates is not possible for states out of the grid used for the discretization of the phase space, since no rate of convergence can be derived from the standard theory for such states. 

Is it possible to construct an alternative theoretical framework which does not require the extensive list of standard assumptions? Can such theory give useful information on some relevant problems that are intractable in the standard framework? 

The aim of this paper is to give some partial answers to these questions. In particular we show that if the data of the problem satisfy Lipschitz continuous assumptions, then the value function is Lipschitz continuous (see Theorem 14). A …rst consequence of our result is that in that setting the value function and optimal policy correspondence are numerically computable (see Morán and Maroto [26]), thus giving a theoretical basis to our examples above, and to some numerical experiments that have recently raised interest in the literature (Dawid and Kopel [11, 12]). 

The most direct antecedent of this paper is the result of Bertsekas [3]. There, in a setting of optimal stochastic control with a discrete state space for the random shocks and admissible controls, it is proved that under Lipschitz assumptions on the data of the problem, the value function can be computed. If we 

3 

ignore the di¤erent settings of the problems, the main contribution of our results is that Bertsekas’method does not permit us to prove that the value function is Lipschitz regular, which is the key step to the obtention of the rate of convergence of the numerical algorithm for the computation of the value function (Morán and Maroto [26]). 

The Lipschitz continuity of the value function has been analyzed by Yue [30, 31] in optimal control and optimal time control problems respectively. Montrucchio [25] proves that the policy function is Lipschitz continuous under assumptions of strong concavity. 

Bardi and Capuzzo-Dolceta [2] proved that the value function is Lipschitz continuous in in…nite horizon problems of optimal control with discount. This result does not allow dependence of the admissible controls on the state of the system, i.e., the existence of a technological constraint correspondence is ruled out. Such correspondence plays a central role in the problem. 

Relevant research regarding applications of the results in this paper is focused on nonconcavity of the growth function of the resource in problems of optimal exploitation of renewable resources (Clark [8]). Notice that these problems are equivalent to optimal growth models with linear or strictly concave objective functions and convex-concave production functions (Majumdar and Mitra [22, 23], Dechert and Nishimura [13], Le Van and Dana [21]). In this sense, the results in this paper can also be applied to these economic problems. 

A second …eld where the results of this paper …nd natural application is that of dynamic optimization problems with convex objective functions. This case 

4 

has been shown to be relevant in the exploitation of renewable resources. In particular, there is empirical evidence in the literature about convex objective functions in …sheries management (Bj;rndal [5], Bj;rndal and Conrad [6]). See also Dasgupta and Mäler [10] for a recent overview on nonconvex ecosystems, and Dawid and Kopel [11, 12] for a numerical analysis of a renewable resource subject to a convex objective function. The case of a convex objective function is also relevant in capital accumulation models of the …rm where the revenue is a convex function of the capital stock (Hartl and Kort [15]). See also Hartl and Kort [16] for capital accumulation models where the revenue is a convex-concave function of the capital stock. 

Lastly, there are relevant economic problems that may be treated in the Lipschitz setting. See Arrow et al. [1], Brian [7], and Heal [17] for recent overviews on economic problems related to nonconcavities. See also references in Example (18). 

## 2 Preliminaries 

## 2.1 The optimization problem 

We describe the stochastic dynamic optimization problem we deal with. Let (X; X ) be a measurable space with X � R[n] and let X be the ��algebra of Borel subsets of X. The space X is assumed to be the domain of an endogenous state variable x, and Z � R[m] endowed with the ��algebra Bm of Borel subsets of Z is the domain of a sequence z0; z1; z2; ::: of exogenous random shocks. 

5 

The state of the system at time t is therefore described by a vector (xt; zt) ranging in the set S := X � Z: As a topological space, S is endowed with the product topology, and as a measure space it is endowed with the product ��algebra. The technological constraints of the problem are represented by a correspondence �: S ! X which speci…es the set �(xt; zt) of feasible states xt+1: We shall write � for the graph of �; and consider in � the topology and ��algebra inherited from the product space X � X � Z. 

Let the value z0 of the …rst random shock be known, and for t � 1 assume that the sequence of random variables zt are a Markov stochastic process with stationary transition function Q; which for z 2 Z ; A in the ��algebra Bm of Borel subsets of R[m] and t � 1, speci…es the probability Q(z; A) that zt 2 A conditional to zt�1 = z: This de…nes in a standard way, for z0 2 Z and t � 1, the probability measure �[t] (z0; �) on the t�fold product space Z[t] = Z � Z � ::: � Z which speci…es the (conditional to z0) probabilities �[t] (z0; A) that the sequence z[t] := (z1; z2; :::; zt) of …rst t random shocks belongs to the sets A in the t-fold product ��algebra Bm[t][:] 

Given z0 2 Z and x0 2 X; a planner faces the problem of …nding an optimal plan, that is, a constant �0 and a sequence �1; �2; �3; ::::of measurable functions �t := Z[t] ! X which solves the problem 

**==> picture [318 x 28] intentionally omitted <==**

where the supremum is taken over all plans satisfying the technological constraints; � 2 (0; 1) is a discount factor; and R is the return function, de…ned on 

6 

the graph � of the correspondence �; so R (xt; xt+1; zt) is the return at time t if the state variable is set to be xt+1 at time t + 1 and the current state of the system is (xt; zt): 

## 2.2 Notation and de…nitions 

We now discuss the required conditions on the data in the above problem, explore the scope of application of such conditions, and state several properties derived from such conditions, that are to be used later on. 

## 2.2.1 Lipschitz functions 

Given a metric space (Y; d) and a point x 2 Y; we shall denote by U (x; r) and B(x; r) respectively, the open and the closed ball centered at x with radius r: 

Recall that a mapping between two metric spaces f : (Y; d) ! (Y[0] ; d[0] ) is said to be a Lipschitz mapping if it satis…es d[0] (f (a); f (b)) � Kd(a; b) for all a; b 2 Y and some constant K. We shall write f 2 L(K) for such mapping (or LA(K) if we want to make explicit some subset A � Y where the Lipschitz condition holds for f restricted to A). The function f is said to be locally Lipschitz on Y if for every x 2 Y there exists a constant K and an open ball U (x; "); " > 0; such that f 2 L(K) on U (x; "); and we write f 2 L[loc] (K) ( L[loc] A[(][K][))][if][such] condition holds on Y (for f restricted to A � Y ). A function v will be said to belong to BLY (�; K) (BL[loc] Y[(][�; K][))][if][v][2][ L][Y][ (][K][)][(][L][loc] Y[(][K][))][and][it][is][bounded] by � (in the supremum norm) on Y . 

De…nition 1 : We call L�convex a subset C � R[p] if it is a bilipschitz image 

7 

of a convex set. 

The key property of L�convex sets is that functions which are locally Lipschitz on them, are also globally Lipschitz. The following lemma can be easily proved 

Lemma 2 : Let C � S � R[p] be a L�convex set with f (C) convex and f bilipschitz, and let v:S ! R with v 2 L[loc] C[(][K][)][.][Then][v][2][ L][C][(�][C][K][)][with] 

**==> picture [206 x 12] intentionally omitted <==**

where Kf and Kf �1 denote respectively the Lipschitz constants of f and f[�][1] : 

Remark 3 : If C is convex then we can set f = id; which shows �C = 1: It is easy to see that in any case �C � 1 (see note 1). The case p = 1 does not have interest, since a L�convex subset of R is an interval. 

## 2.2.2 Correspondences and Hausdor¤ metric 

Given a metric space (Y; d) and a subset A � Y , we denote by [A]� the �- parallel body of A, that is, [A]� = [x2AB(x; �): For compact non-empty subsets A; B � Y we de…ne dH (A; B) = minf" : B � [A]"g; and DH (A; B) = maxfdH (A; B); dH (B; A)g: With this de…nition DH is a metric on the set HY of compact non-empty subsets of Y . DH is known in the literature as the Hausdor¤ metric. 

The results in this paper depend on the following quali…cation of continuity of a correspondence. 

8 

De…nition 4 : Let �: X ! Y be a correspondence between metric spaces (X; d) and (Y; d[0] ). We say that � is topologically continuous at x if it is a compact non-empty valued correspondence, continuous at x and DH (@�(x); @�(y)) ! 0 as y ! x, where @� denotes the boundary of �. � is said to be topologically continuous if it is topologically continuous at all x 2 X: 

The topologically continuous correspondences most frequently used in the literature are compact, convex valued continuous correspondences. Indeed, it can be shown that compact and convex valued correspondences are topologically continuous. 

The following lemma states the property of the type of correspondences used in the proof of the main result. 

Lemma 5 : Let (X; d) and (Y; d[0] ) be metric spaces and let �: X ! Y be a correspondence topologically continuous at x 2 X. Then 

i) For any y 2 int(�(x)); there exists an open neighbourhood U of x and an open neighbourhood U[0] of y such that U[0] � int(�(z)) for all z 2 U . 

ii) (Mutual factibility condition) If G : X ! Y is a compact valued u.h.c correspondence such that G(x) � int(�(x)); then there exists an open neighbourhood U of x such that G(z) � int(�(x)) and G(x) � int(�(z)) hold for any z 2 U: 

Proof. i) Let � = d[0] (y; @�(x)): We know that �> 0 because y 2= @(�(x)): By lower hemi-continuity of �, for a su¢ ciently small " and for any z with d(z; x) < "; there exists z[0] 2 �(z) with d[0] (z[0] ; y) < �=2: By topological continuity 

9 

of �; we also may assume that DH (@�(x); @�(z)) < �=2 holds if d(z; x) < ". In this situation B(y; �=2) � int(�(z)) must hold. To check this, assume …rst that B(y; �=2) \ �(z)[c] = ;: Then B(y; �=2) \ @�(z) = ; since we know that z[0] 2 B(y; �=2) \ �(z) 6= ; (see note 2). Let z[00] 2 @�(z) with d[0] (y; z[00] ) � �=2 and let z[000] 2 @�(x) with d[0] (z[00] ; z[000] ) < �=2: We get the contradiction d[0] (y; z[000] ) < �: This proves that B(y; �=2) � �(z) hold. Since we have already proved that B(y; �=2) \ @�(z) = ; cannot hold, this shows that if d(z; x) < ", then U (y; �=2) � B(y; �=2) � int(�(z)): 

ii) By upper hemicontinuity of G there exists an open neighbourhood U[0] of x such that, for z 2 U[0] ; G(z) � [G(x)]"; with " < dH (G(x); @�(x)): By the condition imposed on "; [G(x)]" \ @�(x) = ; holds, so G(z) � int(�(x)): 

By part i), for any y 2 G(x) there exists an open neighbourhood Uy of x such that if z 2 Uy then U (y; "(y)) � int(�(z)) holds for a su¢ ciently small positive "(y): By compactness we may …nd a cover fU (y[0] ; "(y[0] ))gy02Y 0 of G(x); where Y[0] � Y is a …nite set. Let U = U[0] \y02Y 0 Uy0 , let z 2 U and let y 2 G(x). Since z 2 U[0] ; G(z) � int(�(x)) holds, and as y 2 U (y[0] ; "(y[0] )) for some y[0] 2 Y and z 2 Uy0 we get y 2 U (y[0] ; "(y[0] )) � int(�(z)); so G(x) � int(�(z)). 

The Hausdor¤metric gives also sense to the following de…nition, which allows us to introduce a second (metric) quali…cation of continuous correspondences 

De…nition 6 : Let � be a compact non-empty valued correspondence from the metric space (Y; d) to the metric space (Y[0] ; d[0] ): Then we write � 2 L(K) if �H 2 L(K); so DH (�(x); �(y)) � Kd(x; y); x; y 2 Y: 

Lipschitz correspondences arise in problems of optimal economic growth 

10 

and exploitation of renewable resources, with technological constraints given by �(x) = fy : 0 � y � f (x)g where f (x) is a Lipschitz production function (law of growth of the resource, in problems of exploitation of renewable resources). It is easy to see that the Lipschitz constant of � coincides with that of f (see note 3). 

## 2.2.3 Lipschitz transition functions 

We shall use a metric on the set MZ of Borel probability measures on the domain Z of the random shocks. Notice that the measures Q(z; �) de…ned by the transition function described above belong to MZ: We shall consider in MZ the metric given by d�(�; �) = supfj R fd� � R fd� j: f 2 BLZ(�; 1)g; where BLZ(�; 1) is the set of functions f : Z ! R such that f 2 LZ(1) and k f k� � (with k �k the supremum norm). The metrics d� are equivalent metrics for any (positive) value of �: The metric d1 is called Fortet-Mourier distance (see Dudley [14]). If Z is a compact subset of R[m] ; it su¢ ces to take the supremum, in the de…nition of the metric, over functions f 2 LZ(1): We shall denote this metric by d(�; �): 

These distances allows us to introduce the following Lipschitz condition in the transition function Q of the Markov process which governs the random shocks 

De…nition 7 : We say that the transition function satis…es the Lipschitz condition for the constant KQ; and write Q 2 LZ(KQ) if the mapping Q(z) := Q(z; �) from the metric space (Z; d), with d the Euclidean distance, to the metric space 

11 

(MZ; d�); with the constant � speci…ed later on (see (4)), satis…es Q 2 LZ(KQ): 

The transition functions of many standard Markov processes satisfy the condition Q 2 LZ(KQ): As an example, consider the class of Markov processes de…ned by an initial random variable z0 in R[m] and the stochastic di¤erence equation zt+1 = g(zt; �t); with g : Z � R[p] ! Z � R[m] ; f�tg an i.i.d. process with �t 2 R[p] ; all t; and g Borel-measurable (see Stokey, Lucas and Prescott [29], chap. 8). The transition function is here de…ned on the Borel subsets A � Z by Q(z; A) = P f� 2 R[p] : g(z; �) 2 Ag: Among the Markov processes in this class are AR and VAR models. The following proposition gives a simple su¢ cient condition for these processes to satisfy Assumption IV below, which in turn implies the convergence of the process to a unique invariant measure if the state space Z is compact. 

Proposition 8 : If the function g(�; �) : Z ! Z satis…es g(�; �) 2 LZ(K) then Q 2 LZ(K): Furthermore, if K < 1 and Z is compact, given an arbitrary probability distribution (in MZ) for the random variable z0; the probability distributions of the random variable fztg converge (at a exponential rate, in the weak topology) to a unique invariant measure independent from z0: 

Proof. Let z 2 Z: For a Borel sets A � Z we have Q(z; A) = P f� : g(z; �) 2 Ag;where P is the invariant probability distribution of the process f�tg: This means that, if gz : Z ! Z is the z�section of g de…ned by gz(�) = g(z; �); then Q(z; �) is the image probability distribution of P under the mapping gz: For �> 0, f 2 BLZ(�; 1) and z; z[0] 2 Z the change of variable formula (see 

12 

Billingsley [4]) gives 

**==> picture [237 x 77] intentionally omitted <==**

where it has been used that f 2 LZ(1) and g(�; �) 2 LZ(K): This shows that d�(Q(z; �); Q(z[0] ; �)) � K k z � z[0] k; and the …rst assertion is proven. 

Assume now that Z is a compact set. Recall that, in this case, MZ endowed with the metrics d(�; �) = supfj R fd� � R fd� j: f 2 LZ(1)g is a complete metric space, and the convergence de…ned by the metrics d is equivalent to the weak convergence. Let T[�] : MZ ! MZ be the adjoint operator associated to the transition function Q(z; �), de…ned by T[�] (�)(A) = R Q(z; A)d�(�) for � 2 MZ (see Stokey, Lucas and Prescott [29], chap. 8): We want to prove that, for any � 2 MZ; T[�][k] (�) ! � 2 MZ; where the limiting measure � is independent from �: We only need to prove that T[�] is a contracting mapping. Given f 2 LZ(1) and �; �[0] 2 MZ we have 

**==> picture [300 x 131] intentionally omitted <==**

where it has been used that K[�][1] f (g(�; �)) 2 LZ(1) if g(�; �) 2 LZ(K):This gives 

13 

d(T[�] �; T[�] �[0] ) � Kd(�; �[0] ); as it was to be shown. 

The following lemma, whose proof is elementary, shows the role played by 

the requirement Q 2 LZ(KQ): 

Lemma 9 : If the transition function satis…es Q 2 LZ(KQ); then, for z; z[0] 2 Z, 

y 2 X; and v 2 BLy�Z(�; K), the following inequality holds 

**==> picture [285 x 12] intentionally omitted <==**

## 2.3 Assumptions 

We are now ready to formulate our assumptions on the data X; Z; R; �; and Q: Some straightforward consequences of these assumptions used later on are also analyzed in the remainder of this section. 

Assumption I: X is a closed subset of R[n] and Z is a closed subset of R[m] : Assumption II: R is a real bounded function and R 2 L�(KR): Assumption III: � is a topologically continuous correspondence and � 2 

## LS(K�). 

Assumption IV : Q 2 LZ(KQ) with KQ�< 1: 

In this paper we shall consider only the case of interior optimal paths (see (10), in Theorem 14). We do not add this assumption to the list above because from that list and the results in Theorem 14, it can be obtained the Lipschitz continuity of the value function in the general case of eventually interior optimal plans (See Morán and Maroto [27]). Thus the list above may be considered the basic assumptions for the Lipschitz continuous dynamic programming setting. 

14 

Remark 10 : Assumption IV embodies the case of i.i.d. random shocks if we take Q(�; A) to be constant for each A 2 Bm: In this case KQ = 0; and �KQ < 1 always holds. The deterministic version of the optimization problem (1) is also embodied in our analysis if we think of Z as a singleton fz0g with Q(z0; fz0g) = 1 and Q(z0; ;) = 0: In this case we also have KQ = 0: VAR models zt = Azt + #t with �t i.i.d. also satisfy Assumption IV if the eigenvalues of A are inside the unit ball, including VAR models with roots of the unity. 

Remark 11 : In the most classical models of economic growth the marginal utility of capital tends to in…nity when the capital tend to zero so the return function fails to be a Lipschitz function on a neighbourhood of the origin. These case can be treated in the above setting by considering compact subsets Y = X�U which do not contain a small neighbourhood U of the origin. The high marginal value on U imposes a fast optimal growth. Then the space Y � Z, where the assumptions above hold, may be taken as the phase space of the problem. See Examples 18 and 19 for cases in such situation. 

A consequence of Assumption IV is that Q(z) = Q(z; �) is a continuous mapping; so the transition function Q enjoys the Feller property (See Stokey, Lucas and Prescott [29], chap.11). 

Since X and Z are closed sets by Assumption I, so it is S; which, therefore, is also a complete metric space. Let BCS(�) denote the set of real continuous functions on S bounded in supremum norm by the constant �: Bellman operator 

15 

T; de…ned by 

**==> picture [310 x 23] intentionally omitted <==**

preserves the set BCS of real continuous bounded functions on S; i.e. T : BCS ! BCS; and it is a contractive operator with respect to the supremum norm in BCS (see Stokey, Lucas and Prescott [29], chap. 9). It is easy to check that if v 2 BCS(�) then Tv 2 BCS(k R k +��): Thus, under Assumptions I � IV , setting 

**==> picture [215 x 12] intentionally omitted <==**

we have T : BCS(�) ! BCS(�): 

We shall keep from now onwards the value of � given by (4). It follows from the completeness of BCS(�) the existence of a unique V 2 BCS(�) such that T (V ) = V: Moreover, if T[k] denotes the k�th iterate of T; then k T[k] (v)�V k! 0 for any v 2 BCS and V is the unique value function of the optimization problem (1). 

It is well known that the optimal policy correspondence G : S ! X; given by 

**==> picture [291 x 12] intentionally omitted <==**

is a compact valued and u.h.c correspondence. For each v 2 BCS a maximizing correspondence Gv may be de…ned by 

**==> picture [297 x 12] intentionally omitted <==**

16 

Observe that, as a consequence of Theorem of Maximum (see Stokey, Lucas and Prescott [29], Theorem 3.6), Gv is a u.h.c. and compact valued correspondence. 

## 3 Lipschitz regularity of the value function 

We …rst obtain an upper bound for the rate of growth of Lipschitz constants under Bellman operator T (see de…nition in expression (3)). 

The following simple Lemma states a property of Lipschitz correspondences used in Lemma 13. 

Lemma 12 : Let �: (Y; d) ! (Y[0] ; d[0] ) be a Lipschitz correspondence with � 2 LY (K): If x1; x2 2 Y and y 2 �(x1) then there exists y[0] 2 �(x2) with d[0] (y; y[0] ) � Kd(x1; x2): 

Proof. Assume on the contrary that for all y[0] 2 �(x2); d[0] (y; y[0] ) > Kd(x1; x2) holds: Then y 2= [�(x2)]"; for " = Kd(x1; x2); giving the contradiction DH (�(x1); �(x2)) > Kd(x1; x2): 

Lemma 13 : Let v 2 BCS and v 2 L(M0); M0 � 0: Then, under Assumptions I� IV; Tv 2 L(M1) holds, with M1 = KR(1+K�)+maxf1; M0g�KQ +M0�K�: 

Proof. Let (x; z); (x[0] ; z[0] ) 2 S: We may assume Tv(x; z) � Tv(x[0] ; z[0] ). Let y 2 Gv(x; z), so that it holds 

**==> picture [266 x 23] intentionally omitted <==**

17 

Since y 2 �(x; z) and, by assumption III; 

**==> picture [205 x 11] intentionally omitted <==**

we may …nd (see Lemma 12) some y[0] 2 �(x[0] ; z[0] ) with 

**==> picture [249 x 12] intentionally omitted <==**

Using Assumption II and (6) we get for the …rst summand in (5) 

**==> picture [322 x 65] intentionally omitted <==**

For the second summand in (5) using that: v 2 LS(M0); (6); and Lemma 9 we get 

**==> picture [341 x 98] intentionally omitted <==**

� � v(y[0] ; �)Q(z[0] ; d�) + �(maxf1; M0gKQ + M0K�) k (x; z) � (x[0] ; z[0] ) k : (8) Z 

Using that Tv(x; z) � Tv(x[0] ; z[0] ), (7) and (8) 

**==> picture [335 x 44] intentionally omitted <==**

Lastly, Using that y[0] 2 �(x[0] ; z[0] ) we obtain 

18 

**==> picture [213 x 11] intentionally omitted <==**

This lemma shows that the Lipschitz constants Mk of the iterates T[k] v follow the di¤erence equation 

**==> picture [292 x 12] intentionally omitted <==**

The result to be proved in this section is the following 

Theorem 14 : Let C � S be a compact set and assume that 

**==> picture [259 x 11] intentionally omitted <==**

Let Assumptions I � IV hold. Then V 2 L[loc] C[(][�; K][)][;][with][K][= max][f][1][; K][R][(1][�] �KQ)[�][1] g: Let w 2 BLS(�; M0); for some given constant M0; and let �> 0. Then there exists a j0(�) such that T[j] w 2 BL[loc] C[(][�; K][ +][ �][)][;][all][j][> j][0][(][�][)][:][If][C] is an L�convex set, then V 2 BLC(�; �CK) and T[j] w 2 BLC(�; �C(K + �)); all j > j0(�); with �C given by (2). 

If we interpret the variable x as the stock level of some economic resource, the assumption (10) means that neither the exhaustion of the resource nor a null consumption will be optimal at any period. This is the relevant situation in problems of economic growth, if the extinction of the economy is ruled out, and in problems of exploitation of renewable resources, if the extinction of the resource and the paralysis of the exploitation for a period is too costly. 

In order to prove Theorem 14, we …rst ensure that the correspondence Gv (see de…nition in Section 2.3) satis…es on C the condition required to G in the statement of the above theorem if v is a small perturbation of V . 

19 

Lemma 15 : i) If BCS is endowed with the supremum norm topology and BCS � S is endowed with the product topology, then the correspondence G[�] : BCS � S ! X de…ned by G[�] (v; c) = Gv(c) is upper hemi-continuous. 

ii) There exists an open ball U (V ); centered at V; of the normed space BCS; such that Gv(x; z) � int(�(x; z)) holds if (x; z) 2 C and v 2 U (V ). 

Proof. i) By Theorem of Maximum, it is enough to check that h(v; x; y; z) := R(x; y; z)+� R v(y; �)Q(z; d�) is a continuous function which, in view of the continuity of R, reduces to check the continuity of the integral term. Let (vk; yk; zk) 2 BCS � S , all k; with (vk; yk; zk) ! (v; y; z) 2 BCS � S: We may write 

**==> picture [231 x 104] intentionally omitted <==**

The third summand in the string tends to zero as k tends to in…nity because vk ! v in the supremum norm; the second summand tends to zero because Q enjoys Feller’s property; and the …rst summand tends to zero by Lebesgue theorem of dominated convergence, since the sequence of functions v(yk; �) converges to v(y; �) and k v(yk; �) k �k v k< 1: 

ii) Assume, by contradiction, that for all U (V ), all (x; z) 2 C and all v 2 U (V ), @�(x; z) \ Gv(x; z) = ?. Then, there exists a sequence vk ! V and sequences f(xk; zk)g in C and fykg in X with yk 2 @�(xk; zk) \ Gvk (xk; zk) 6= ?. By compactness we may assume (xk; zk) ! (x; z) 2 C. Using that � is topo- 

20 

logically continuous, so DH (@�(xk; zk); @�(x; z)) ! 0; and yk 2 @�((xk; zk)); we see that d(yk; @�(x; z)) ! 0: This means that for all k there exists an yk[�][2][@][�(][x; z][)][such][d][(][y][k][; y] k[�][)][!][0][.][By][compactness][we][may][assume][y] k[�][!][y] 2 @�(x; z); so we may assume yk ! y 2 @�(x; z). But this is a contradiction, since from the upper hemi-continuity of G[�] and from (vk; xk; zk) ! (V; x; z) it follows y 2 G(x; z) � int(�(x; z)): 

Next we state an elementary property that provides the basic tool for the proof of Theorem 14. 

Lemma 16 : Under Assumptions I � IV let v 2 BLS(�; M ); and assume that Tv(x; z) � Tv(x[0] ; z[0] ) holds, where (x[0] ; z[0] ); (x; z) 2 S are such that Gv(x; z) \ �(x[0] ; z[0] ) 6= ;: Then j Tv(x; z) � Tv(x[0] ; z[0] ) j� (KR + maxf1; M g�KQ) k (x; z) � (x[0] ; z[0] ) k : 

Proof. Let y 2 Gv(x; z) \ �(x[0] ; z[0] ): We have 

**==> picture [372 x 119] intentionally omitted <==**

where the …rst inequality holds because R 2 L�(KR) and using Lemma 9, and the second inequality holds because y 2 �(x[0] ; z[0] ). 

Using this lemma we …rst analyze the local action of T: This shall give a recursive law for the Lipschitz constants of iterates under Bellman operator of 

21 

functions in U (V ) which is as in (9) without the constant term K�KR and the (potentially) growing term Mk�1�K�: The mutual factibility condition (see Lemma 5 (ii)) guarantees that Lemma 16 can be applied to bounded Lipschitz functions in U (V ). 

Lemma 17 : Assume that v 2 U (V ) \ BLS(�; M ) for some constant M; where U (V ) is as in part ii) of Lemma 15 and let c 2 C: Then there exists an " > 0 such that Tv 2 BL(�; K) on U (c; "); with K = KR + maxf1; M g�KQ: 

Proof. By Lemma 15 we know that Gv(c) � int(�(c)) holds for c 2 C: By Lemma 5 applied to the correspondences � and Gv; we know that there exists an open ball U (c; ") such that if c[0] 2 U (c; "); then Gv(c[0] ) � �(c) and Gv(c) � �(c[0] ) hold. If Tv(c) � Tv(c[0] ); then Gv(c) � �(c[0] ) and Lemma 16 give j Tv(c) � Tv(c[0] ) j� K k c � c[0] k; and we arrive at the same conclusion if Tv(c) � Tv(c[0] ) using then that Gv(c[0] ) � �(c). 

We have now all the ingredients needed in the proof of Theorem 14. 

Proof. Let U (V ) be as in Lemma 15 and let w 2 BLS(�; M0) where M0 is some constant: Then, as T[k] w ! V; T[k][0][�][1] w 2 U (V ) holds if k0 is large enough. Hence T[k][0] w 2 U (V ) \ BLS(�; Mk0); with Mk0 as given by Lemma 13. Notice that, since T is a contractive operator, U (V ) is invariant under T: Reset M0 equal to the constant Mk0, let c 2 C; and let U (c; "(c)) be an open ball as that given by Lemma 17. We see that T[k][0][+][k] w 2 BL(�; Mk) on U (c; "(c)); k = 1; 2; ::;with Mk following now the di¤erence equation 

**==> picture [244 x 11] intentionally omitted <==**

22 

If K := KR(1 � �KQ)[�][1] > 1 and M0 � 1; then M1 = KR + �KQ; and since KR > 1 � �KQ; we get that M1 > 1: Therefore any solution of equation (11) follows in turn, for k � 2; the di¤erence equation 

**==> picture [225 x 12] intentionally omitted <==**

which converges to its unique equilibrium point K so, there is an integer k1(�) such that 

**==> picture [268 x 12] intentionally omitted <==**

on U (c; "(c)): If K = 1 (so KR(1 � �KQ)[�][1] � 1) then, whenever a solution of (11) remains larger than 1; it follows the di¤erence equation (12); which converges to its unique equilibrium point KR(1 � �KQ)[�][1] � 1: If, for some k; we have Mk � 1 (which necessarily occurs in a …nite number of steps if KR(1 � �KQ)[�][1] < 1, see note 4 ), then Mk+1 = KR + �KQ � 1; because now KR � 1 � �KQ: Thus (13) always holds. 

Set j0(�) = k0 + k1(�): Then T[j] w 2 BLU (c;"(c))(�; K + �) for j � j0(�); which shows T[j] w 2 BL[loc] C[(][�; K][ +][�][)][; j][�][j][0][(][�][)][;][ and if][C][is a][L][�][convex,][T][ j][w][2] BLC(�; �C(K + �)); j � j0(�) by Lemma 2: 

Since the set of functions BLU (c;"(c))(�; K + �) is a closed set of functions and T[j] w 2 BLU (c;"(c))(�; K +�); j � j0(�); we see that V 2 BLU (c;"(c))(�; K + �) (see note 5). This shows that V 2 L[loc] C[(][�; K][+][�][)][;][and][as][�][was][ar-] bitrarily small, we get V 2 L[loc] C[(][�; K][)][:][If][C][is][L][�][convex,][Lemma][2][gives] V 2 LC(�; �CK): 

23 

## 4 Examples 

All data in the examples below were generated using a AXP-2100/AMP500 DIGITAL Computer, coded in standard FORTRAN 77. 

## 4.1 Deterministic example 

Example 18 An application of Theorem 14: Non-Concavity in Growth Models 

The optimization problem is 

**==> picture [331 x 31] intentionally omitted <==**

where � 2 (0; 1) is a discount factor; xt is the capital stock at period t; U (ct) is the utility function of a private owner of a …rm or household, where ct = f (xt) � xt+1 is the consumption at period t; and f (xt) is a production function. Note that (14) is the classical problem of optimal growth in a onesector model. 

The Bellman equation associated to (14) is in this case 

**==> picture [261 x 17] intentionally omitted <==**

We have analyzed the case of the utility function U (x) = x[0][:][7] + x[3] � x which is increasing, concave for low consumption levels, and it possesses an interval of convexity for high consumption levels. The numerical experiment shows that the optimal behaviour implied by such utility is rather common at a microeconomic level (see Rothenberg [28], and Arrow et al. [1], for theoretical justi…cation 

24 

of nonconcave utility functions in microeconomic problems). It is cyclical: It maintains low consumptions levels for some periods of time, and then makes a large consumption. The production function considered is f (x) = 0:95x exp(1 � x): It is concave and with strictly positive marginal productivity in the interval [0; xe] ; with f (xe) = xe = 1 + ln 0:95 < 1, which is the relevant domain of f (see …g. 1-b). 

In …gs. 1-a and 1-b we can see the value function solution of (15) and the associated optimal policy correspondence respectively. There are countably many discontinuities in the optimal policy following a visible pattern synchronized with jumps upwards in the marginal value of capital stock. In …g. 1-b the production function is also plotted. There is not extinction of the economy, since all solutions are interior. In particular, the optimal capital stock satis…es xt+1 � x[0] ' 0; 03 if xt � x[0] . Since xt+1 > xt if xt � x[0] ; Theorem 14 applies to this example taking Y = [x; 1]; with 0 < x � x[0] ; as state space of the problem (see Remark 11). Fig. 1-b reveals that one strongly attractive period-six cycle, supports the long run behavior of the optimal paths. Research in progress is addressed to the analytical characterization of the threshold point, beyond which the main part of the savings are expended in a large consumption. 

## 4.2 An stochastic example 

## Example 19 : Stochastic Optimal Growth 

We analyze here the Example (18) in a stochastic setting. Randomness enters in the problem through a multiplicative random shock which modi…es the 

25 

production function f , re‡ecting, for instance, the action of a exogenous shock which a¤ects negatively to the production function. The intensity zt of the multiplicative shock at period t is described by a stochastic i.i.d. process fzng where zn = 0; 5+0; 5zn[0][with][ z] n[0][distributed as a][ �][(0][:][5][;][ 0][:][5)][.][The output at period] t corresponding to a resource level x is given by ztf (x). The Bellman equation is written now V (x; z) = max0�y�zf (x)fU (zf (x) � y) + � RZ[V][ (][y; �][)][d�][(][�][)][g][;][where] Z = [0:5; 1] is the support of the probability distribution � of zn. Fig. 2 shows the value function of the problem. Notice that the value function is not a Lipschitz function on X � Z since the marginal return of capital stock tends to in…nity when the stock tends to zero. The numerical analysis reveals that there exists a minimal capital stock x = 0:003 such that G(x) � x if x � x; so we may use Y � Z; with Y := [x; 1]; as state space, as indicated in Remark 11. There is no extinction in this economy, as it can be checked that all optimal paths from a endogenous state x0 � x are always interior, so Theorem 14 applies to the set Y � Z: 

If we compare the value function in this stochastic example with that in the deterministic case, Example 18, we can see that the uncertainty derived from the random shock produces an smoothing e¤ect on the value function. Further numerical analysis reveals discontinuities in the z�sections of the optimal policy correspondence, which should cause non-smoothness of the value function. 

26 

## 5 Concluding remarks 

There are three directions for the future extension of this research: 

1) In Morán and Maroto [26], we analyze the convergence of the algorithm for the numerical computation of the value function. The Lipschitz continuity of the value function is the only assumption that we need in order to obtain a rate O(�) of convergence of the numerical algorithm, where � is the diameter of the discrete grid of points used for the computation. 

2) The results in this paper for the case of interior optimal plans allow us to prove the Lipschitz continuity of the value function for the case of eventually interior optimal plans. This case is relevant to the area of optimal exploitation of renewable resources where the existence of nonconcavities has been largely admitted. 

3) As a future perspective, the results in this paper allow us the use of powerful tools of non-smooth analysis (Clarke [9]). In the same spirit, an incipient development of a theory of dynamical systems with evolution law governed by correspondences (Lasota and Myjak [19, 20]), closely related to fractal geometry (Hutchinson [18]), open the perspective of the analysis of the long run behaviour of optimal policies and asymptotic stability of dynamical equilibria if nonuniqueness in the policy correspondence is allowed, so in the deterministic as in the stochastic settings. For recent research on chaotic behaviour of optimal paths, see also Majumdar et al. [24]. 

27 

## References 

- [1] K.J. Arrow, N. Yew-Kwang, X. Yang, Increasing returns and economic analysis, Macmillan Press, London, 1998. 

- [2] M. Bardi, I. Capuzzo-Dolcetta, Optimal Control and Viscosity Solutions of Hamilton-Jacobi-Bellman Equations, Birkhäuser, Boston, 1997. 

- [3] D. P. Bertsekas, Convergence of Discretization Procedures in Dynamic Programming, IEEE Transactions on Automatic Control. AC-20 (1975) 415419. 

- [4] P. Billingsley, Probability and Measure, John Wiley & Sons, New York, 1995. 

- [5] T. Bj;rndal, Production in a Schooling Fishery: The case of the North Sea Herring Fishery, Land Economics. 65 (1988) 49-56. 

- [6] T. Bj;rndal, J.M. Conrad, The dynamics of an open access …shery, Canadian journal of Economics. 20 (1987) 74-85. 

- [7] W. Brian, Increasing returns and path dependence in the economy, University of Michigan Press, 1994. 

- [8] C.W. Clark, Economically optimal policies for the utilization of biologically renewable resources, Mathematical Biosciences. 12 (1971) 245-260. 

- [9] F.H. Clarke, Optimization and Nonsmooth Analysis, Vol. 5 of Classics in 

   - Applied Mathematics, SIAM, Philadelphia, 1990. 

28 

- [10] P. Dasgupta, K.-G. Mäler, Special issue: The economics of non-convex ecosystems, Environmental & Resource Economics. 26 (2003). 

- [11] H. Dawid, M. Kopel, On the economically optimal exploitation of a renewable resource: the case of a convex environment and a convex return function, Journal of Economic Theory. 76 (1997) 272-297. 

- [12] H. Dawid, M. Kopel, On optimal cycles in dynamic programming models with convex return function, Economic Theory. 13 (1999) 309-327. 

- [13] W.D. Dechert, K. Nishimura, A complete characterization of optimal growth paths in an aggregated model with a non-concave production function, Journal of Economic Theory. 31 (1983) 332-354. 

- [14] R.M. Dudley, Probabilities and metrics, Lecture Notes Series 45, Aarhus Universitet, 1976. 

- [15] R.F. Hartl, P.M. Kort, Optimal investments with increasing returns to scale: a further analysis, in: E.J. Dockner, R.F. Hartl, M. Luptacik, G. Sorger (Eds.), Optimization, dynamics, and economic analysis: essays in honor of Gustav Feichtinger, Physica-Verlag, New York, 2000, pp. 226-238. 

- [16] R.F. Hartl, P.M. Kort, Optimal investments with convex-concave revenue: a focus-node distinction, Optimal Control Applications & Methods. 25 (2004) 147-163. 

- [17] G. Heal, The economics of increasing returns, Edward Elgar, United Kindong, 1999. 

29 

- [18] J.E. Hutchinson, Fractals and self-similarity, Indiana University Mathematical journal. 30 (1981) 713-747. 

- [19] A. Lasota, J. Myjak, Markov Operator and fractals, Bulletin of the polish Academy of Science. 45 (1997) 197-207. 

- [20] A. Lasota, J. Myjak, Attractors of Multifunctions, Bulletin of the polish Academy of Science. 48 (2000) 1-44. 

- [21] C. Le Van, R.-A. Dana, Dynamic Programming in Economics, Kluwer Academic Publishers, Netherlands, 2003. 

- [22] M. Majumdar, T. Mitra, On optimal exploitation of a renewable resource in a nonconvex environment and the minimum safe standard of conservation, Working paper No. 223, Cornell University, 1980. 

- [23] M. Majumdar, T. Mitra, Intertemporal allocation with a non-convex technology: the aggregative framework, Journal of Economic Theory. 27 (1982) 101-136. 

- [24] M. Majumdar, T. Mitra, K. Nishimura, Optimization and Chaos, Springer, Berlin, 2000. 

- [25] L. Montrucchio, Lipschitz Continuous Policy Functions for Strongly Concave Optimization Problems, Journal of Mathematical Economics. 16 (1987) 259-273. 

- [26] M. Morán, J.M. Maroto, Convergence in Dynamic Programming with Discount, Working paper, Universidad Complutense, 2003. 

30 

- [27] M. Morán, J.M. Maroto, Lipschitz continuous dynamic programming with discount: The case of eventually interior optimal plans. Manuscript in preparation. 

- [28] J. Rothenberg, Non-convexity, agregation, and Pareto optimality, The Journal of Political Economy. 68 (1960) 435-468. 

- [29] N.L. Stokey, R. Lucas, E. Prescott, Recursive methods in economic dynamics, Harvard University Press, Cambridge, 1989. 

- [30] R. Yue, Lipschitz Continuity of Value Functions in a Class of Optimal Controls Problems Governed by Ordinary di¤erential Equations, in: S. Chen, J. Yong (Eds.), Control Theory, Stochastic Analysis and Applications, World Scienti…c, Singapure, 1991, pp. 125-137. 

- [31] R. Yue, Properties of the Bellman Function in Time-Optimal Control Problems, Journal of Optimization Theory and Applications. 94 (1997) 155-168. 

31 

## Notes 

1.- d(f (x); f (y)) � Kd(x; y); which shows that any Lipschitz constant for f[�][1] must be larger than K[�][1] : This shows that Kf Kf �1 � KK[�][1] = 1: 

2.- The sets B(y;[�] 2[)][ \][ adh][(�(][c][))][and][B][(][y;][�] 2[)][ \][ �(][c][)][c][are][non-empty][closed] sets whose union completes the connected set B(y;[�] 2[)][.][We][may][write][B][(][y;][�] 2[)][ \] adh(�(c)) = (B(y;[�] 2[)][ \][ �(][c][))][ [][ (][B][(][y;][�] 2[)][ \][ @][(�(][c][)))][:][If][B][(][y;][�] 2[)][ \][ @][(�(][c][))][=][;] then (B(y;[�] 2[)][\][adh][(�(][c][))][\][(][B][(][y;][�] 2[)][\][�(][c][)][c][)][=][;][;][in][contradiction][with][the] connectedness of B(y;[�] 2[)][:] 

3.- Let I = [0; a] and J = [0; b]: Then DH (I; J) = d(a; b): For the correspondences described in the text we have �(x) = [0; f (x)]. Therefore, if f 2 L(K) we have DH (�(x); �(y)) = d(f (x); f (y)) � Kd(x; y). 

4.- If KR(1 � �KQ)[�][1] = 1 then Mk does not have to become smaller that 1 in a …nite number of steps but, for any �> 0; it becomes smaller than 1 + � in a …nite number of steps, as required. 

5.- Let vn ! v with vn 2 LU (K + �): Then, given x; y 2 U and " > 0 there exists an n such that d(vn(x); v(x)) � " and d(vn(y); v(y)) � ": Therefore, for x; y 2 U; 

d(v(x); v(y)) � 2" + d(vn(x); vn(y)) � 2" + (K + �)d(x; y); 

and, since " was arbitrary, we get v 2 LU (K + �): 

32 

**==> picture [557 x 413] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.1<br>1<br>0.9<br>0,8<br>OF<br>0.6<br>0,5<br>O.4<br>,<br>0,4 é<br>o,1<br>0<br>ti a,1 O,2 0,3 O,4 0,5 0,6 O,? 0,8 og 1<br>Figure ]-a. Value function.<br>**----- End of picture text -----**<br>


**==> picture [557 x 407] intentionally omitted <==**

**----- Start of picture text -----**<br>
ZO<br>0,8<br>a4 |<br>a<br>f<br>é<br>é<br>0.2 / Ba<br>ra ———<br>é<br>gi<br>x<br>Oo ol Oe O,3 O,4 0,5 0,6 OF o,8 0.9 1<br>Figure 1-b. Production function, optimal policy correspondence and optimal dynamics.<br>**----- End of picture text -----**<br>


**==> picture [476 x 250] intentionally omitted <==**

**----- Start of picture text -----**<br>
_———a ee<br>0.8 Prse<br>i)<br>1<br>0,95<br>o,9<br>0,85<br>0 0 5<br>1 95 ~~ < 67 °<br>0.4 0.5 96 o.6<br>* o,9 0,5<br>1<br>**----- End of picture text -----**<br>


Figure 2. Value function. 

