# On convergence rates of Bayesian predictive densities and posterior distributions 

Ryan Martin 

Department of Mathematics, Statistics, and Computer Science University of Illinois at Chicago rgmartin@math.uic.edu 

Liang Hong Department of Mathematics Bradley University lhong@bradley.edu 

November 6, 2018 

## Abstract 

Frequentist-style large-sample properties of Bayesian posterior distributions, such as consistency and convergence rates, are important considerations in nonparametric problems. In this paper we give an analysis of Bayesian asymptotics based primarily on predictive densities. Our analysis is unified in the sense that essentially the same approach can be taken to develop convergence rate results in iid, mis-specified iid, independent non-iid, and dependent data cases. 

Keywords and phrases: Density estimation; Hellinger distance; Kullback–Leibler divergence; Markov process; nonparametric; separation. 

## 1 Introduction 

In Bayesian nonparametric problems, asymptotic concentration properties of the posterior distribution are often key to motivating a particular choice of prior. Indeed, for infinite-dimensional problems, elicitation of subjective priors is difficult and a theory of objective priors for remains elusive, so large-sample properties of the posterior are often what drives the choice of prior. A desirable (frequentist) property can be summarized roughly as follows: for a given “true model” and prior, as more and more data becomes available, the posterior distribution becomes more and more concentrated around this true model with large probability. Early efforts along these lines are given in Doob (1949) and Schwartz (1965). Stronger results, some including rates of convergence, are presented in Barron et al. (1999), Ghosal et al. (1999), Ghosal et al. (2000), Shen and Wasserman (2001), Ghosal and van der Vaart (2001, 2007b), Tokdar (2006), 

1 

and Walker et al. (2007). Modern efforts include extensions to non-Euclidean sample spaces (Bhattacharya and Dunson 2010), more complex models (Pati et al. 2011), and misspecified models (Kleijn and van der Vaart 2006; Lian 2009; Shalizi 2009). 

This paper presents a sort of unified analysis of Bayesian posterior convergence rates based on predictive densities. These predictive densities are fundamental quantities in Bayesian statistical inference—they are the Bayes estimates of the density under a variety of loss functions. This connection with predictive densities is not new, but the extent to which we depend on these quantities gives our analysis a strong Bayesian flavor. Moreover, we show how essentially the same techniques can be used to develop convergence rate theorems for a variety of models, including iid, mis-specified iid, independent non-iid, and dependent data. In particular, we prove (apparently) new Cesaro-style convergence rate results for predictive densities, in each of the four contexts above, under weaker conditions than usual for posterior convergence rate theorems. We also develop a fundamental lemma, also based on predictive densities, which helps bound the numerator of the posterior probability for sets not-too-close to the true data-generating density. This result is similar to Proposition 1 in Walker et al. (2007), but the proof is different and applies almost word-for-word in a variety of contexts. It also relies an interesting notion of separation of points and sets, apparently due to Choi and Ramamoorthi (2008). This lemma is then used to prove posterior convergence rate theorems. 

The remainder of the paper is organized as follows. Section 2 develops the notation and terminology used throughout the paper, in particular, the notion of prior thickness at the true data-generating density, and separation of sets from this same density. Sections 3 and 4 cover predictive density and posterior convergence rates, respectively, both in the simplest iid context. In Section 4, we prove an auxiliary result that demonstrates the sieve+covering style conditions in Ghosal et al. (2000) are weaker than the prior summability conditions in Walker et al. (2007). The results on predictive density and posterior convergence rate theorems are extended to the mis-specified iid, independent non-iid, and dependent cases in Sections 5–7, respectively. Finally, some concluding remarks are given in Section 8. 

## 2 Bayesian nonparametrics 

## 2.1 Notation and 

Let Y be a Polish space equipped with its Borel σ-algebra Y . Suppose Y1:n = (Y1, . . . , Yn), n ≥ 1, are independent Y-valued observations with common distribution F , and that F has a density f = dF/dµ with respect to some σ-finite measure µ on (Y, Y ). Let F be the set of all such densities f and F its Borel σ-algebra. Then a prior distribution Π for f is a probability measure on the measurable space (F, F ). Following Bayes’ theorem, the posterior distribution of f , given Y1:n, can be written as 

**==> picture [365 x 32] intentionally omitted <==**

We require a topology on F, and here we focus on the Hellinger topology. The Hellinger distance H is given by H(f, f[′] ) = {� (f[1][/][2] − f[′][1][/][2] )[2] dµ}[1][/][2] , for f, f[′] ∈ F. 

2 

For describing large-sample properties of the posterior, it is standard to assume that there is a “true density” f[⋆] from which the data Y1, . . . , Yn are observed. It shall be required that the prior Π puts a sufficient amount of mass around this f[⋆] ; the precise conditions on Π are stated in Section 2.2. With “true density” f[⋆] , it is typical to rewrite the posterior (1) as 

**==> picture [318 x 32] intentionally omitted <==**

where R0(f ) ≡ 1 and 

**==> picture [315 x 33] intentionally omitted <==**

In what follows, we will occasionally refer to the posterior Πn, restricted to a given set A. By that we mean the measure Π[A] n[defined][as][Π][A] n[(][·][) = Π][n][(][A][ ∩·][)][/][Π][n][(][A][).][Also,][≲][and] ≳ will denote inequality up to a universal constant. 

Convergence rates of the posterior Πn concerns the amount of probability assigned to (expanding) sets that do not contain the true density f[⋆] when n is large. Let (εn) be a positive vanishing sequence. Then the posterior Πn has a Hellinger convergence rate εn if Πn({f : H(f[⋆] , f ) ≳ εn}) → 0 in probability. Here, and in what follows, the “in probability” qualification is with respect to P = P[∞] f[⋆][,][the][product][distribution,][under][f][ ⋆][,] of the infinite data sequence Y1:∞ = (Y1, Y2, . . .). 

## 2.2 Prior support conditions 

In order for the posterior distribution to concentrate around f[⋆] , some support conditions on the prior Π are needed. For example, if there exists a set A ∋ f[⋆] such that Π(A) = 0, then, trivially, the posterior cannot concentrate around f[⋆] . To avoid these kinds of degeneracies, it is typical to assume that Π satisfies the Kullback–Leibler property, i.e., that Π({f : K(f[⋆] , f ) < ε}) > 0 for all ε > 0, where K(f[⋆] , f ) = � log(f[⋆] /f )f[⋆] dµ is the Kullback–Leibler divergence of f from f[⋆] . See Wu and Ghosal (2008, 2010) for sufficient conditions and a host of examples. While the Kullback–Leibler property itself is not a necessary condition for posterior convergence, it does make up part of an important and useful set of sufficient conditions, developed by Schwartz (1965). Indeed, the Kullback– Leibler property alone is enough to imply that the posterior is weakly consistent. But extra conditions, beyond the Kullback–Leibler property, are generally needed to establish strong consistency; see Choi and Ramamoorthi (2008). 

To establish rates of convergence, something even stronger than the usual Kullback– Leibler property is needed. Set V (f[⋆] , f ) = � {log(f[⋆] /f )}[2] f[⋆] dµ. 

Definition 1. Let (εn) be a positive sequence such that εn → 0 and nε[2] n[→∞][.][The] prior Π is said to be εn-thick at f[⋆] if, for some constant C > 0, 

**==> picture [350 x 16] intentionally omitted <==**

This is exactly condition (2.4) in Ghosal et al. (2000), which they motivate with entropy considerations. Since (4) is stronger than the Kullback–Leibler property, prior thickness can be seen as a support condition on the prior, guaranteeing that the prior 

3 

assigns a sufficient amount of mass near f[⋆] . Beyond this intuition, the following technical lemma, giving a lower bound on the denominator in (2), is a consequence of prior thickness. See Ghosal et al. (2000, Lemma 8.1 and the proof of Theorem 2.1). 

Lemma 1. Let In = � Rn(f ) Π(df ) be the denominator in (2). If Π is εn-thick at f[⋆] , then P(In ≤ e[−][cnε] n[2] ) → 0 for any c > C + 1 with C as in (4). 

Next is a simple application of Lemma 1, similar to Proposition 4.4.2 in Ghosh and Ramamoorthi (2003), that will be used in the proof of the main results. 

Lemma 2. Assume Π is εn-thick at f[⋆] . For a sequence (Un) ⊂ F , suppose that Π(Un) ≲ e[−][rnε] n[2] , where r > C + 1, with C as in (4). Then Πn(Un) → 0 in probability. 

Proof. Write Πn(Un) = Ln/In. Using Markov’s inequality and the assumption on Π(Un), it is easy to check that P(Ln > e[−][cnε] n[2] ) ≲ e[−][(][r][−][c][)][nε] n[2] . Therefore, if c ∈ (C + 1, r), then P(e[cnε] n[2] Ln > η) → 0 for any η > 0. Similarly, from Lemma 1, for the same c, P(In ≤ e[−][cnε] n[2] ) → 0. Then by the law of total probability, 

**==> picture [412 x 73] intentionally omitted <==**

Both quantities on the right-hand side vanish with n, so Πn(Un) → 0 in probability. 

## 2.3 Convexity and separation 

Choi and Ramamoorthi (2008) make use of two important properties for subsets A of F. Here we define and discuss these properties. 

Definition 2. A set A ⊆ F is convex if, for any probability measure Φ supported on A, the expectation, fΦ = � f Φ(df ), also belongs to A. 

Examples of convex subsets of F include balls, i.e., all those f within a specified distance from a center f0. For an important example, let h = H[2] /2, a slight modification of the squared Hellinger distance. Choose a point f0 ∈ F and let A = {f : h(f0, f ) ≤ r}. Now, take any probability measure Φ supported on A. Then by convexity of h and definition of A, we have 

**==> picture [170 x 28] intentionally omitted <==**

Therefore, fΦ is in A and, hence, A is convex. In the applications that follow, the probability measure Φ will often be a truncated version of the posterior distribution. 

Definition 3. A density f[⋆] ∈ F and a set A ⊆ F are δ-separated (with respect to h) if h(f[⋆] , f ) > δ for all f in A. 

4 

For an important example, choose r > 0 and f0 such that H(f[⋆] , f0) > r. Then f[⋆] and A = {f : H(f0, f ) < r/2} are δ-separated, with δ = r[2] /8. To see this, note that the triangle inequality implies 

**==> picture [221 x 13] intentionally omitted <==**

From the definitions of f0 and A, the right-hand side is strictly greater than r/2. Therefore, h(f[⋆] , f ) > r[2] /8, so f[⋆] and A are (r[2] /8)-separated (with respect to h). 

In the applications that follow, we shall extend this idea in two directions. First, in some cases, we need separation with respect to distances other than Hellinger distance H (or h). Second, we shall consider sequences of sets (An) and sequences of numbers (δn). Then the notion of δn-separation of a density f[⋆] and sets An is straightforward. 

## 3 Convergence rates for predictive densities 

Predictive densities are fundamental quantities in Bayesian analysis. Indeed, they are the Bayes density estimators under a variety of different loss functions. In particular, the predictive density of Yi, given Y1, . . . , Yi−1, is 

**==> picture [135 x 27] intentionally omitted <==**

the posterior expectation of f (y). For example, in a density estimation problem with Hellinger distance as the loss function, the predictive density f[ˆ] n is the Bayes estimator of f in the sense that it minimizes Bayes risk. 

Our first result develops a Kullback–Leibler convergence rate for predictive densities in a Cesaro sense. The proof is based on calculations in Barron (1987). 

Proposition 1. For a given vanishing sequence (εn), let Kn = {f : K(f[⋆] , f ) ≤ ε[2] n[}][.][If] log Π(Kn) ≳ −nε[2] n[,][then][n][−][1][ �][n] i=1[E][{][K][(][f][ ⋆][,][f][ˆ][i][−][1][)][}][ ≲][ε][2] n[.] 

Proof. Let f[⋆n] denote the joint density for an iid sample (Y1, . . . , Yn), i.e., the n-fold product of the f[⋆] . Likewise, let f[ˆ][n] denote the joint density of (Y1, . . . , Yn) under the Bayesian model with prior Π, i.e., f[ˆ][n] = � f[n] Π(df ). Since densities are non-negative, 

**==> picture [262 x 29] intentionally omitted <==**

where Π[K][n] is the prior Π restricted and normalized to Kn. Therefore, if we define Π(Kn) f[ˆ][n,][K][n] as the lower bound above, then 

**==> picture [317 x 49] intentionally omitted <==**

where the last inequality is by convexity of K. Recall the chain rule for the Kullback– Leibler number between product densities: K(f[⋆n] , f[n] ) = nK(f[⋆] , f ). Therefore, 

**==> picture [286 x 29] intentionally omitted <==**

5 

By definition of Kn, the first term in the upper bound above is ≤ ε[2] n[,][and,][by][the] assumption on Π(Kn), the second term is ≲ ε[2] n[.] 

To complete the proof, we must connect n[−][1] K(f[⋆n] , f[ˆ][n] ) and the average in the statement of the proposition. For this we show that f[ˆ][n] (Y1, . . . , Yn) factors as a product �ni=1[f][ˆ][i][−][1][(][Y][i][)][of][predictive][densities.][The][key][is] 

**==> picture [280 x 114] intentionally omitted <==**

The first term in the last line is the expectation of f (Yn) with respect to the posterior distribution Πn−1, which is exactly f[ˆ] n−1(Yn); the second term is the normalizing constant for Πn−1. The next step is to apply the same trick to the normalizing constant. That is, write it as an expectation of f (Yn−1) with respect to the posterior distribution Πn−2 times a new normalizing constant. This gives 

**==> picture [282 x 35] intentionally omitted <==**

Continuing like this, we find that f[ˆ][n] (Y1, . . . , Yn) factors as[�][n] i=1[f][ˆ][i][−][1][(][Y][i][).][Now,] 

**==> picture [267 x 93] intentionally omitted <==**

The conditional expectation is K(f[⋆] , f[ˆ] i−1), so K(f[⋆n] , f[ˆ][n] ) equals[�][n] i=1[E][{][K][(][f][ ⋆][,][f][ˆ][i][−][1][)][}][.] This, together with the ≲ ε[2] n[bound][on][n][−][1][K][(][f][ ⋆n][,][f][ˆ][ n][)][completes][the][proof.] 

Observe that the assumption of Proposition 1 is implied by εn-thickness of Π at f[⋆] . Also, the Kullback–Leibler divergence can be replaced by the Hellinger distance via the well-known inequality h ≲ K. That is, n[−][1][ �][n] i=1[E][{][h][(][f][ ⋆][,][f][ˆ][i][−][1][)][}][ ≲][ε][2] n[.] For another perspective, let f[¯] n = n[−][1][ �][n] i=1[f][ˆ][i][−][1][,][an][average][of][predictive][densities.] By convexity of h, h(f[⋆] , f[¯] n) ≤ n[−][1][ �][n] i=1[h][(][f][ ⋆][,][f][ˆ][i][−][1][).][Therefore, Proposition 1 says that, if] the prior is suitably concentrated around f[⋆] , then H(f[⋆] , f[¯] n) = OP (εn). As Walker (2003) explains, the prior Π would have to be rather strange for this not to imply convergence of the predictive density f[ˆ] n itself at the same εn rate. 

It is interesting that the predictive densities, and averages thereof, are asymptotically well-behaved with only local properties of the prior (Barron 1999). This is particularly 

6 

important because posterior convergence rates involve a compromise between local and global global properties. For example, overall posterior convergence rates are determined by max{εn, ε[′] n[}][,][where][ε][′] n[gives][a][global][characterization][of][the][complexity][of][the][model.] In many cases, ε[′] n[is][bigger][than][ε][n][,][slowing][down][the][overall][posterior][convergence][rate;] see Ghosal and van der Vaart (2001). Proposition 1 requires no global conditions, so there is nothing slowing down convergence. So, although Proposition 1 is a weaker result than full posterior convergence, it does provide some nice intuition. 

## 4 Convergence rates for the posterior 

## 4.1 Review of existing results 

There are essentially two kinds of theorems: the first kind makes assumptions on the “size” of the model F, and the second kind makes assumptions on how the prior probabilities are spread across F. Before proving the convergence rate theorem, we discuss these conditions in more detail. In particular, we show in Proposition 2 that the latter assumption is stronger than the former. Throughout this discussion, we silently assume that the prior Π is εn-thick at f[⋆] , with constant C given in (4). 

The first set of sufficient conditions are like those in Ghosal et al. (2000). Their concern is the existence of a suitable high mass, low entropy sieve. Let (Fn) be an increasing sequence of measurable subsets of F. The idea is that the sieve Fn will be large enough to contain all the reasonable f ’s, but also small enough to be covered by a relatively small number of Hellinger balls that are each easier to work with. Let N(εn, Fn, H) denote the Hellinger εn-covering number of Fn, that is, the minimum number of Hellinger balls of radius εn needed to cover Fn. Theorem 2.1 of Ghosal et al. (2000) assumes that the following condition (“S” for sieve) holds: 

Condition S. There exists a sieve Fn ⊂ F such that, for sufficiently large n, 

**==> picture [218 x 33] intentionally omitted <==**

Part (a) ensures that Π assigns most of its probability to a large subset of F, and Part (b) guarantees that this “large” subset of F is not too large. As opposed to prior thickness, which is a local property, S(a) and S(b) are global properties. These conditions have, along with prior thickness, been verified for a variety of important priors, including Dirichlet process mixtures. 

Despite the nice geometric intuition of Condition S, identifying a suitable sieve is sometimes difficult in practice. Fortunately, there is an alternative sufficient condition (“P” for prior), due to Walker et al. (2007), which can be easier to work with. 

Condition P. Let Bn = {f : H(f[⋆] , f ) > εn}. For (An,j)j≥1 a covering of Bn by Hellinger balls of radius δn < εn, and some constants c > 0 and β > 1, the following holds: 

**==> picture [133 x 28] intentionally omitted <==**

7 

The case β = 2 was considered in Walker et al. (2007). This condition ensures that the prior is sufficiently concentrated near f[⋆] . That is, if the prior is too spread out, then those covering sets could get large enough posterior probability that the summation above is of exponential order. An advantage of Condition P is that it is directly related to the Bayesian problem, through the prior probabilities, and often these prior probabilities have a nice form. And by allowing β ≈ 1, the Condition P here is weaker than that in Walker et al. (2007) with β = 2. However, in applications, the sets An,j are typically assigned exponentially small prior probability so it is not clear if β ∈ (1, 2) is easier to verify or leads to any improvement in the rate of convergence. 

We claim that Condition S is, in a certain sense, more fundamental than Condition P, despite the fact that the latter is often easier in practice. To justify this claim, we prove that Condition S is actually weaker than Condition P. This connection between the two sets of conditions is implicit in Theorem 5 of Ghosal and van der Vaart (2007b). An analogous result is given in Choi and Ramamoorthi (2008, Theorem 4.4) in the context of posterior consistency. 

Proposition 2. Condition P implies Condition S. 

Proof. Without loss of generality, suppose that, for each n, the sets An,j are ordered such that Π(An,1) ≥ Π(An,2) ≥· · · . Also, let Sn =[�] j[Π(][A][n,j][)][1][/β][,][which][can][be][expressed][as] Sn = e[cnε] n[2][−][v][(][n][)] for some v(n) > 0 such that v(n) →∞. Take r > C + 1, and set 

**==> picture [303 x 37] intentionally omitted <==**

Clearly, log N(εn, Fn, H) = log Jn ≤ ([r] β[+] −[βc] 1[)][nε] n[2][≲][nε][2] n[,][so][F][n][satisfies][Condition][S(b).] Next, the special ordering of Π(An,j) implies that JΠ(An,J)[1][/β] ≤[�][J] j=1[Π(][A][n,j][)][1][/β][≤][S][n] for any J, which in turn implies that Π(An,J ) ≤ Sn[β][/J][β][.][Therefore,] 

**==> picture [337 x 35] intentionally omitted <==**

so Condition S(a) holds as well. 

Theorem 1. Suppose Π is εn-thick at f[⋆] . If either Condition S or Condition P holds, then Πn({f : H(f[⋆] , f ) ≳ εn}) → 0 in probability. 

Proof. The part involving Condition P follows from Proposition 2 and the part involving Condition S. The part involving Condition S is proved in Section 4.3. 

Although the result in Theorem 1 is known, the proof that follows will highlight the importance of predictive densities in the study of posterior convergence rates. The basic idea is that sets An in F such that the predictive densities, restricted to An, are not too close to f[⋆] will have vanishing posterior probability. These predictive densities are fundamental quantities in the Bayesian context, so the proof presented herein perhaps has a better Bayesian interpretation compared to those arguments based on, say, existence of a consistent sequence of tests. 

8 

## 4.2 A preliminary result 

Recall that Πk denotes the posterior distribution of f , given Y1, . . . , Yk. For a set An, we write Π[A] k[n] for that same posterior distribution, but restricted and normalized to An. Then we can define a corresponding predictive density: 

**==> picture [227 x 29] intentionally omitted <==**

For a sequence of sets (An), let Ln,i = �An[R][i][(][f][) Π(][df][) be the numerator of Π][i][(][A][n][) in (2),] i = 1, . . . , n. Note that Ln,0 = Π(An). It is easy to check that 

**==> picture [226 x 16] intentionally omitted <==**

For Yi−1 the σ-algebra generated by Y1, . . . , Yi−1, it follows that 

**==> picture [337 x 16] intentionally omitted <==**

The next result, akin to Proposition 1 in Walker et al. (2007), provides a convenient fixed-n bound the expected value of L[1] n,n[/][2][for][suitable][sets][A] n[.] 

Lemma 3. Let Π be εn-thick at f[⋆] , with C as in (4). If An is convex and dε[2] n[-separated] from f[⋆] , with d > C + 1, then E(L[1] n,n[/][2][)][ ≤][Π(][A] n[)][1][/][2][e][−][dnε] n[2] . Proof. Start with the “telescoping product” 

**==> picture [223 x 34] intentionally omitted <==**

Taking expectation of both sides, conditioning on Yi−1 and using (6), gives 

**==> picture [353 x 35] intentionally omitted <==**

The assumed convexity of An and its separation from f[⋆] together imply that 

**==> picture [166 x 33] intentionally omitted <==**

Multiplying both sides by Π(An)[1][/][2] completes the proof. 

The thickness assumption in Lemma 3 is not necessary, but it helps to set the notation for its primary application. This use of ratios of predictive densities is not new; see Walker (2004) and Walker et al. (2007). In fact, Lemma 3 is similar to the main conclusion in Proposition 1 of Walker et al. (2007), although the proof is a bit different. 

9 

## 4.3 Proof of Theorem 1 

For M a sufficiently large constant to be determined, define Bn = {f : H(f[⋆] , f ) > Mεn}. For the given Fn, it is clear that Πn(Bn) ≤ Πn(F[c] n[) + Π][n][(][B][n][∩][F][n][).][From][Condition][S(a)] and Lemma 2, we conclude that Πn(F[c] n[)][→][0][in][probability.][We][now][turn][attention][to] the second term, Πn(Bn ∩ Fn). 

Choose a covering Bn ∩ Fn ⊆[�][J] j=1[n][A][nj][,][where][each][A][nj][is][a][Hellinger][ball][of][radius] Mεn/2 with center in Bn. By Condition S(b), Jn = e[Rnε] n[2] for some R > 0. Now, since probabilities are ≤ 1, we have 

**==> picture [319 x 37] intentionally omitted <==**

where In = � Rn(f ) Π(df ) is the denominator of Πn(Anj), which is independent of j, and L =[the][numerator.][From the][triangle][inequality][argument][in][the] n,nj �Anj[R][n][(][f][) Π(][df][) is] example following Definition 3, we know that f[⋆] and Anj are (M[2] ε[2] n[/][8)-separated][for][all] j = 1, . . . , Jn. So, provided that M is sufficiently large, we may apply Lemma 3 to bound the expectation of the sum of L[1] n,nj[/][2][.][Indeed,] 

**==> picture [383 x 37] intentionally omitted <==**

If we choose M such that M[2] > 4[(C + 1) + 2R], then (application of Lemma 3 is valid and) the upper bound above vanishes as n →∞. Now let Sn =[�][J] j=1[n][L][1] n,nj[/][2][,][and][pick] c ∈ (C + 1, M[2] /4 − 2R). By Markov’s inequality we have 

**==> picture [271 x 16] intentionally omitted <==**

Also, by Lemma 1, we have P(In ≤ e[−][cnε] n[2] ) → 0. A total-probability argument like in the proof of Lemma 2 gives 

**==> picture [414 x 75] intentionally omitted <==**

Since both of these terms vanish, we conclude that Πn(Bn) ≤ Πn(F[c] n[) + Π][n][(][B][n][∩][F][n][)][ →][0] in probability, i.e., Πn({f : H(f[⋆] , f ) > Mεn}) → 0 in probability. 

## 5 Extension to mis-specified iid models 

## 5.1 Notation and setup 

It can happen that the true density f[⋆] lies outside the support of prior. In such cases, the posterior cannot concentrate around f[⋆] . However, the posterior can exhibit concentration 

10 

properties around a different point in F. Specifically, take f[◦] to be the f ∈ F that minimizes the Kullback–Leibler divergence, i.e., 

**==> picture [355 x 13] intentionally omitted <==**

An analysis of posterior concentration is presented in Kleijn and van der Vaart (2006). They show that, under certain conditions, the posterior distribution concentrates around the point f[◦] . Indeed, if 

**==> picture [131 x 34] intentionally omitted <==**

then the posterior is given by 

**==> picture [343 x 32] intentionally omitted <==**

Then the goal is to show that Πn(Bn[c][)][ →][0,][where][B][n][is][a][shrinking][neighborhood][of][f][ ◦][.] Here we give an analysis based primarily on predictive densities. First, we recall/revise some of our previous notions. 

Prior thickness. Let V[⋆] (f[◦] , f ) = � {log(f[◦] /f )}[2] f[⋆] dµ. Then we have the following analogue of Definition 1, i.e., the prior Π is εn-thick at f[◦] if, for some constant C > 0, 

**==> picture [341 x 16] intentionally omitted <==**

It follows from Lemma 7.1 of Kleijn and van der Vaart (2006) that the result of Lemma 1 above holds in the mis-specified case, i.e., 

**==> picture [310 x 16] intentionally omitted <==**

where In = � Rn(f ) Π(df ) is the denominator in (8). 

Separation. For a distance on F, consider a weighted Hellinger distance H[⋆] , whose square is given by H[⋆] (f, f[′] )[2] = � (f[1][/][2] − f[′][1][/][2] )[2] (f[⋆] /f[◦] ) dµ. In the well-specified case, i.e., f[◦] = f[⋆] , this is the usual Hellinger distance. Since � (f/f[◦] )f[⋆] dµ ≤ 1 for all f ∈ F (Kleijn and van der Vaart 2006, Lemma 2.3), we have 

**==> picture [248 x 90] intentionally omitted <==**

Write h[⋆] (f[◦] , f ) = 1 − � (f/f[◦] )[1][/][2] f[⋆] dµ, so that H[⋆][2] /2 ≤ h[⋆] . Now we say that f[◦] and a set A are δ-separated (with respect to h[⋆] ) if h[⋆] (f[◦] , f ) > δ for all f ∈ A. 

11 

## 5.2 Convergence rate results 

First, we extend Proposition 1 to the mis-specified case. The only noticeable change is the use of the Kullback–Leibler contrast K[⋆] (f[◦] , f ) in (7) instead of K(f[⋆] , f ). 

Proposition 3. For a sequence (εn), with εn → 0, let Kn = {f : K[⋆] (f[◦] , f ) ≤ ε[2] n[}][.][If] log Π(Kn) ≳ −nε[2] n[,][then][n][−][1][ �][n] i=1[E][{][K][⋆][(][f][ ◦][,][f][ˆ][i][−][1][)][}][ ≲][ε][2] n[.] 

Proof. Similar to that of Proposition 1; use convexity of K[⋆] . 

As before, if f[¯] n is the average predictive density, f[¯] n = n[−][1][ �][n] i=1[f][ˆ][i][−][1][,][then][Proposi-] tion 3 and convexity of the Kullback–Leibler contrast implies K[⋆] (f[◦] , f[¯] n) = OP (ε[2] n[).][Also,] the condition on Π(Kn) is implied by prior thickness (9). Therefore, just like in the wellspecified case, with only a local thickness condition on the prior, the predictive densities, or averages thereof, converge to the “best” density f[◦] in the model F. 

Towards a posterior concentration result, given sets (An) in F, let Ln,i be the numerator of Πi(An) in (8); note, Ln,0 = Π(An). Then, as before, it is easy to check that Ln,i/Ln,i−1 = f[ˆ] i[A] −[n] 1[(][Y][i][)][/f][ ◦][(][Y][i][),][i][ = 1][, . . . , n][.][Also] 

**==> picture [302 x 16] intentionally omitted <==**

We can now anticipate a version of Lemma 3 for the mis-specified case. 

Lemma 4. Let Π be εn-thick at f[◦] , with C as in (9). If An is convex and dε[2] n[-separated] from f[◦] , with d > C + 1, then E(L[1] n,n[/][2][)][ ≤][Π(][A] n[)][1][/][2][e][−][dnε] n[2] . 

Proof. Same as that of Lemma 3. 

To get a posterior convergence rate result, we must choose sets to be convex and suitably separated, with respect to h[⋆] , from f[◦] . For this, a natural choice would be H[⋆] -balls. Indeed, the triangle inequality argument before, and the fact that H[⋆][2] ≤ h[⋆] /2 shows that H[⋆] -balls centered away from f[◦] with sufficiently small radius are separated from f[◦] . Technically, a more complicated notion of “covering numbers for testing under mis-specficiation” are needed in these cases. However, if we assume F is convex, for simplicity, then these special covering numbers are bounded by ordinary H[⋆] -covering numbers. See Kleijn and van der Vaart (2006), Lemmas 2.1, 2.3, and the mixture model example in their Section 3. 

Theorem 2. Let F be convex and Π be εn-thick at f[◦] with constant C as in (9). Suppose there exists a sequence (Fn) such that Π(F[c] n[)][≲][e][−][rnε] n[2] , where r > C + 1, and log N(εn, Fn, H[⋆] ) ≲ nε[2] n[.][Then][Π][n][(][{][f][:][ H][⋆][(][f][ ◦][, f][)][ ≳][ε][n][}][)][ →][0][in][probability.] Proof. Similar to that of Theorem 1. 

## 6 Extension to independent non-iid models 

## 6.1 Setup and notation 

Let Y1, . . . , Yn be independent but not necessarily iid. To formulate this, we shall use some slightly different notation compared to the previous sections. Suppose that Yi ∼ fθi, 

12 

where, for each θ ∈ Θ, fθi is a density with respect to a measure µi on Yi, i = 1, . . . , n. An important example is the fixed-design Gaussian regression, i.e., Yi ∼ N(θ(xi), 1), where xi is a fixed covariate and θ(·) is an unknown regression function. The new θ notation is simply to indicate that there is a single unknown characteristic θ, common to all i = 1, . . . , n; the manner in which θ is used can differ across i, however. 

Let θ[⋆] denote the “true” value of θ. As before, define the likelihood ratio as 

**==> picture [142 x 34] intentionally omitted <==**

If Π is a prior distribution on Θ, then the posterior distribution for θ, given observations Y1, . . . , Yn, is given by 

**==> picture [369 x 32] intentionally omitted <==**

The goal is to show that Πn(Bn[c][)][→][0][for][B][n][a][shrinking][neighborhood][of][θ][⋆][.][Next][we] restate our main 

Prior thickness. Let 

**==> picture [339 x 34] intentionally omitted <==**

where K and V are defined in Section 2.2. Then we say the prior Π is εn-thick at θ[⋆] if for some constant C > 0, 

**==> picture [337 x 16] intentionally omitted <==**

It follows from Lemma 10 of Ghosal and van der Vaart (2007a) that the conclusion of Lemma 1 above holds in the independent non-iid case. That is, 

**==> picture [310 x 15] intentionally omitted <==**

where In = � Rn(θ) Π(dθ) is the denominator in (11). 

Separation. For a distance on Θ, we shall employ a type of mean-Hellinger distance Hn, whose square is given by 

**==> picture [162 x 33] intentionally omitted <==**

As usual, set hn = Hn[2][/][2.][Then][we][say][that][θ][⋆][and][a][set][A][⊆][Θ][are][δ][-separated] (with respect to hn) if hn(θ[⋆] , θ) > δ for all θ ∈ A. 

13 

## 6.2 Convergence rate results 

Before stating the independent non-iid version of Proposition 1, we need to set some more notation. Let f[ˆ] (i−1)i denote the predictive density of Yi given Y1, . . . , Yi−1, i.e., 

**==> picture [229 x 28] intentionally omitted <==**

Proposition 4. For a sequence (εn), with εn → 0, let Kn = {θ : K[¯] n(θ[⋆] , θ) ≤ ε[2] n[}][.][If] log Π(Kn) ≳ −nε[2] n[,][then][n][−][1][ �][n] i=1[E][{][K][(][f][θ][⋆][i][,][f][ˆ][(][i][−][1)][i][)][}][ ≲][ε][2] n[.] 

Proof. The proof is similar to that of Proposition 1 once we set the appropriate notation, etc. Let f[ˆ][n] denote the joint density for (Y1, . . . , Yn) under the Bayes model. Then, just like in the proof of Proposition 1, 

**==> picture [269 x 33] intentionally omitted <==**

It follows that K(fθ[n][⋆][,][f][ˆ][ n][) =][ �][n] i=1[E][{][K][(][f][θ][⋆][i][,][f][ˆ][(][i][−][1)][i][)][}][.][Therefore,][we][can][safely][work][with] the notationally simpler n[−][1] K(fθ[n][⋆][,][f][ˆ][ n][).][From this point, follow the proof of Proposition 1,] i.e., restrict Θ to Kn and use convexity of the Kullback–Leibler number. 

For posterior convergence rates, take a sequence of subsets (An) in Θ and let Ln,i be the numerator of Πi(An) in (11), where Ln,0 = Π(An). As before, we have 

**==> picture [287 x 19] intentionally omitted <==**

where f([A] i−[n] 1)i[is][the][predictive][density][from][before,][but][with][the][posterior][Π][i][−][1][restricted] to the set An ⊂ Θ. Also, 

**==> picture [237 x 18] intentionally omitted <==**

where h = H[2] /2 and H is the usual Hellinger distance between densities. With this, we are ready for an analogue of Lemma 3 for the independent non-iid case. 

Lemma 5. Let Π be εn-thick at θ[⋆] , with C as in (12). If An is convex and dε[2] n[-separated] from θ[⋆] , with d > C + 1, then E(L[1] n,n[/][2][)][ ≤][Π(][A] n[)][1][/][2][e][−][dnε] n[2] . 

Proof. Just like the proof of Lemma 3. 

In the following theorem, we shall also need a type of max-Hellinger distance, 

**==> picture [160 x 18] intentionally omitted <==**

Also let hn,∞ = Hn,[2] ∞[/][2.][This][additional][sort][of][distance][will][be][needed][for][the][general] construction of sets which are both convex and sufficiently separated from θ[⋆] . Some remarks on removing the need for Hn,∞ are given following the proof. 

Theorem 3. Let Π be εn-thick at θ[⋆] with constant C as in (12). Suppose there exists a sequence (Θn) such that Π(Θ[c] n[)][ ≲][e][−][rnε] n[2] , where r > C+1, and log N(εn, Θn, Hn,∞) ≲ nε[2] n[.] Then Πn({θ : Hn(θ[⋆] , θ) ≳ εn}) → 0 in probability. 

14 

Proof. For a constant M > 0 to be determined, let Bn = {θ : Hn(θ[⋆] , θ) > Mεn}. It suffices to show that Πn(Bn ∩ Θn) → 0 in probability. We cover Bn ∩ Θ by Hn,∞-balls Anj of radius Mεn/2 with centers in Bn, where j = 1, . . . , Jn and Jn ≤ e[Rnε] n[2] , R > 0. That is, for suitable θj satisfying Hn(θ[⋆] , θj) > Mεn, take 

**==> picture [255 x 13] intentionally omitted <==**

Note the use of Hn,∞ in the definition of Anj as opposed to Hn. Everything will carry through as before as soon as we show that the Anj are convex and (M[2] ε[2] n[/][8)-separated] from θ[⋆] , with respect to hn. For convexity, let Φi, i = 1, . . . , n, be any probability measure on Anj. By convexity of h we get 

**==> picture [263 x 31] intentionally omitted <==**

By definition of Anj, the right-hand side is bounded by M[2] ε[2] n[/][8.][From][here][it][follows] that Anj is convex and, in particular, predictive densities f[ˆ] (Ai−nj1)i[,][restricted][to][A][nj][,][have] properties like those densities fθi with θ ∈ Anj. Our use of the max-Hellinger metric is necessary here because the measures Φi can vary with i, just like the posteriors ΠAi nj vary with i. Now, for separation, given θ ∈ Anj, the triangle inequality for Hn gives 

**==> picture [176 x 13] intentionally omitted <==**

The first term is greater than Mεn by the choice of θj. The second term is less than Hn,∞(θj, θ) which is less than Mεn/2 by the definition of Anj. Therefore, θ[⋆] and Anj are (M[2] ε[2] n[/][8)-separated][with][respect][to][h][n][.][Now][we][may][apply][Lemma][5][to][each][A][nj] just like in the proof of Theorem 1, to show that if M is large enough, then Πn({θ : Hn(θ[⋆] , θ) > Mεn}) → 0 in probability. 

The use of a max-Hellinger metric in Theorem 3 can be avoided in some cases, e.g., if Hn is equivalent to some fixed metric on θ-space. One specific example is nonparametric regression using splines; see Ghosal and van der Vaart (2007a, Sec. 7.7). 

## 7 Extension to Markov models process 

## 7.1 Setup and notation 

Let (Yn : n ≥ 0) be an ergodic Markov process on Y with transition density fθ(y[′] | y) and stationary density uθ(y), both with respect to a σ-finite measure µ on Y, and both indexed by θ ∈ Θ. That is, the transition density fθ characterizes the one-step moves Yn → Yn+1 of the process, and uθ the limiting marginal distribution of Yn. Here, like in Ghosal and van der Vaart (2007a), we assume the process is at stationarity, i.e., that Y0 ∼ uθ⋆, so that all the marginal distributions are the same and equal to uθ⋆. The goal here is estimation of the unknown index θ. Methods developed in the previous sections, particularly in Section 6, shall be used to prove posterior convergence rate theorems. 

Following the previous setup, let θ[⋆] denote the “true” θ value. Now define 

**==> picture [177 x 34] intentionally omitted <==**

15 

as the likelihood ratio for (Y0, Y1, . . . , Yn). For a prior distribution Π on Θ and a measurable set A ⊂ Θ, Bayes theorem gives the posterior distribution for f as follows: 

**==> picture [343 x 32] intentionally omitted <==**

The primary goal of this section is to investigate the convergence of Πn(An), where An is the complement of a shrinking neighborhood of θ[⋆] . The notion of “neighborhood” is more difficult here than in the previous cases; see Section 7.2 below. 

Prior thickness. For concentration properties of the prior Π, consider 

**==> picture [191 x 58] intentionally omitted <==**

where Ky(fθ⋆, fθ) = K(fθ⋆(· | y), fθ(· | y)) is the usual Kullback–Leibler divergence for densities; Vy is defined similarly, for V as in Section 2.2. Let Θ0 be the set of all θ’s such that both K(uθ⋆, uθ) and V (uθ⋆, uθ) are bounded by 1. With this notation, we say that the prior Π is εn-thick at θ[⋆] if, for some constant C > 0, 

**==> picture [347 x 15] intentionally omitted <==**

Lemma 10 of Ghosal and van der Vaart (2007a) gives an analogue of Lemma 1 above for the present dependent data case. That is, for C as in (15), 

**==> picture [314 x 16] intentionally omitted <==**

where In is the denominator in (14). 

Separation. Let Hy be the usual Hellinger distance on transition densities with fixed state y, i.e., Hy(fθ⋆, fθ) = H(fθ⋆(· | y), fθ(· | y)). Also let hy = Hy[2][/][2.][Now][define][the] max-Hellinger (semi)metric H∞(θ[⋆] , θ) = supy Hy(θ[⋆] , θ). We say that θ[⋆] and a set A ⊆ Θ are δ-separated (with respect to h∞) if h∞(θ[⋆] , θ) > δ for all θ ∈ A. 

## 7.2 Convergence rate results 

To start, consider the predictive density problem of Section 3. In this case, the predictive density is itself a transition density. In particular, we have 

**==> picture [279 x 28] intentionally omitted <==**

the expected transition density with respect to the posterior distribution Πi−1. This is a typical Bayes estimate of the transition density, and the claim is that it converges to the true transition density fθ⋆ as n →∞. In particular, we have the following convergence rate result for predictive densities. 

16 

Proposition 5. Given (εn) with εn → 0 and nε[2] n[→∞][,][let][K][n][=][{][θ][:][K][(][θ][⋆][, θ][)][≤] ε[2] n[,][K][(][u][θ][⋆][, u][θ][)][ <][ ∞}][.][If][log Π(][K][n][)][ ≳][−][nε][2] n[.][Then][n][−][1][ �][n] i=1[E][{][K][Y] i−1[(][f][θ][⋆][,][f][ˆ][i][−][1][)][}][ ≲][ε][2] n[.] Proof. Let f[ˆ][n] denote the joint density for (Y0, . . . , Yn) under the Bayes model. Then 

**==> picture [387 x 34] intentionally omitted <==**

ˆ just like in the proof of Proposition 4, where u0(Y0) = � uθ(Y0) Π(dθ). Another simple calculation shows that if fθ[n][⋆][is the joint distribution of (][Y][0][, Y][1][, . . . , Y][n][) under][θ][⋆][,][then the] joint Kullback–Leibler divergence K(fθ[n][⋆][,][f][ˆ][ n][)][equals] 

**==> picture [373 x 33] intentionally omitted <==**

Observe that n[−][1] K(uθ⋆, ˆu0) = O(ε[2] n[) and,][on][K][n][,][n][−][1][K][(][u][θ][⋆][, u][θ][) =][ O][(][ε][2] n[).][From here,][the] proof is just like that of Proposition 1. 

As before, the assumption of Proposition 5 is implied by prior thickness at θ[⋆] . The theorem also extends the result in Corollary 2.1 of Ghosal and Tang (2006). Indeed, our result is n[−][1][ �][n] i=1[K][Y] i−1[(][f][ ⋆][,][f][ˆ][i][−][1][) =][ O][P][(][ε][2] n[), which is stronger than the][ o][P][(1) obtained by] these authors. Our version of the Kullback–Leibler property is more strict than theirs, but this is typical when convergence rates are sought. 

Let (An) be a sequence of measurable subsets of Θ, and let Ln,i = �An[R][i][(][θ][) Π(][dθ][)][be] the numerator of the posterior probability Πi(An) in (14). Then 

**==> picture [337 x 16] intentionally omitted <==**

where f[ˆ] i[A] −[n] 1[is the predictive transition density when the posterior Π][i][−][1][is restricted to][ A][n][.] We also have 

**==> picture [386 x 16] intentionally omitted <==**

We can now present an extension of Lemma 3 for the case of Markov processes. 

Lemma 6. Let Π be εn-thick at θ[⋆] , with C as in (15). If An is convex and dε[2] n[-separated] from θ[⋆] , with d > C + 1, then E(L[1] n,n[/][2][)][ ≤][Π(][A] n[)][1][/][2][e][−][dnε] n[2] . Proof. Exactly the same as that of Lemma 3. 

The fact that data Yi−1 appears as part of the formula for the distance hYi−1 in (17) necessitates the use of the max-Hellinger metric, i.e., separation with respect to h∞ implies separation with respect to hy for any y, even if y is random. But we are free to formulate the convergence rate theorem with a different metric. Here we consider HQ(θ[⋆] , θ) = � Hy(fθ⋆, fθ) Q(dy), where Q is a probability measure on Y. In the nonlinear Gaussian autoregression example in Ghosal and van der Vaart (2007a, Sec.7.4), the measure Q is taken to be a two-point location mixture of Gaussians. 

17 

Theorem 4. Let Π be εn-thick at θ[⋆] with constant C as in (15). Suppose there exists a sequence (Θn) such that Π(Θ[c] n[)][ ≲][e][−][rnε] n[2] , where r > C +1, and log N(εn, Θn, H∞) ≲ nε[2] n[.] Then Πn({θ : HQ(θ[⋆] , θ) ≳ εn}) → 0 in probability. Proof. The proof is similar to that for the independent non-iid case. In particular, we cover the complement of a mean-Hellinger neighborhood of θ[⋆] by max-Hellinger-balls. The convexity and separation calculations are analogous to those in Theorem 3, and the rest of the argument goes just like in the proof of Theorem 1. 

## 8 Discussion 

Here we have presented an analysis of Bayesian asymptotics based primarily on predictive densities. These densities are fundamental quantities in Bayesian statistics, for they are Bayes density estimates under a variety of loss functions. So, in this sense, our analysis has a stronger Bayesian flavor than other existing approaches. We have also demonstrated how our basic approach can be tuned to handle a variety of models—iid, mis-specified iid, independent non-iid, and dependent Markov processes. For example, essentially the same predictive density convergence rate result holds in all these contexts. 

We have opted here for simplicity of presentation rather than strength of results. For example, one can easily tailor the analysis, taking more efficient choice of coverings, etc, to achieve sharper rates. In particular, to achieve n[−][1][/][2] rates in finite-dimensional parametric models, a special type of covering is required (e.g., Ghosal et al. 2000, Theorem 2.4), and this can be incorporated into the present analysis. On the other hand, if convergence of predictive densities is the only concern, then these special coverings are not necessary—only local thickness of the prior is needed. Indeed, it is straightforward to follow the argument in Ghosal and van der Vaart (2007a, Sec. 7.7) to show that, in a nonparametric regression context, where the true regression function θ[⋆] lies in an α- smooth function class, and a spline-based prior is used, the predictive densities converge, in the sense of Proposition 4, at the minimax rate n[−][α/][(2][α][+1)] . In this example, however, Ghosal and van der Vaart’s analysis gives full convergence of the posterior at the same rate under basically the same assumptions. But there may be some cases where the weaker conditions of the predictive density convergence theorems may be more useful. 

- Consider a basic iid Bayesian density estimation problem. For Dirichlet process location-mixtures of Gaussians, care must be taken in choosing a prior for the common component scale σ. This is like the choice of bandwidth in classical density estimation. Typical conditions restrict the amount of mass the prior for σ can place near zero. However, these conditions are primarily needed for the control of model entropy—when σ is near zero, the class of possible models is enormous, making the entropy large. But if convergence of predictive densities is the question of interest, so that only local thickness is required, as in Proposition 1, then entropy is not a concern. Therefore, one can expect practically weaker assumptions on the prior if the focus is on convergence of predictive densities. 

- For dependent data models, there may be some advantage to the predictive densitybased approach. Indeed, in Section 7, convergence of the predictive densities in Proposition 5 follows without any assumptions on the mixing of the process. This 

18 

is due to the fact that only “first moment” conditions—bounds on the Kullback– Leibler number—are needed. Compare this to the posterior convergence analysis in Ghosal and van der Vaart (2007a, Sec. 4) which requires assumptions on the mixing of the process and some “higher-than-second moment” conditions. 

Finally, we mention that this investigation began by looking at a predictive density analysis of the posterior by using a law of large numbers for martingale difference arrays. Unfortunately, that approach seemed to be somewhat limited; specifically, a non-trivial extension to a uniform martingale law of large numbers is needed. That idea is still interesting, see Martin and Hong (2012), although the results here are stronger. 

## References 

- Barron, A. (1987), “Are Bayes rules consistent in information?” in Open Problems in Communications and Computation, eds. Cover, T. M. and Gopinath, B., Springer– Verlag, New York, pp. 85–91. 

- Barron, A., Schervish, M. J., and Wasserman, L. (1999), “The consistency of posterior distributions in nonparametric problems,” Ann. Statist., 27, 536–561. 

- Barron, A. R. (1999), “Information-theoretic characterization of Bayes performance and the choice of priors in parametric and nonparametric problems,” in Bayesian statistics, 6 (Alcoceber, 1998), New York: Oxford Univ. Press, pp. 27–52. 

- Bhattacharya, A. and Dunson, D. B. (2010), “Nonparametric Bayesian density estimation on manifolds with applications to planar shapes,” Biometrika, 97, 851–865. 

- Choi, T. and Ramamoorthi, R. V. (2008), “Remarks on consistency of posterior distributions,” in Pushing the Limits of Contemporary Statistics: Contributions in Honor of Jayanta K. Ghosh, Beachwood, OH: Inst. Math. Statist., vol. 3 of Inst. Math. Stat. Collect., pp. 170–186. 

- Doob, J. L. (1949), “Application of the theory of martingales,” in Le Calcul des Probabilit´es et ses Applications, Paris: Centre National de la Recherche Scientifique, Colloques Internationaux du Centre National de la Recherche Scientifique, no. 13, pp. 23–27. 

- Ghosal, S., Ghosh, J. K., and Ramamoorthi, R. V. (1999), “Posterior consistency of Dirichlet mixtures in density estimation,” Ann. Statist., 27, 143–158. 

- Ghosal, S., Ghosh, J. K., and van der Vaart, A. W. (2000), “Convergence rates of posterior distributions,” Ann. Statist., 28, 500–531. 

- Ghosal, S. and Tang, Y. (2006), “Bayesian consistency for Markov processes,” Sankhy¯a, 68, 227–239. 

- Ghosal, S. and van der Vaart, A. (2007a), “Convergence rates of posterior distributions for non-i.i.d. observations,” Ann. Statist., 35, 192–223. 

19 

- Ghosal, S. and van der Vaart, A. W. (2001), “Entropies and rates of convergence for maximum likelihood and Bayes estimation for mixtures of normal densities,” Ann. Statist., 29, 1233–1263. 

- (2007b), “Posterior convergence rates of Dirichlet mixtures at smooth densities,” Ann. Statist., 35, 697–723. 

- Ghosh, J. K. and Ramamoorthi, R. V. (2003), Bayesian Nonparametrics, New York: Springer-Verlag. 

- Kleijn, B. J. K. and van der Vaart, A. W. (2006), “Misspecification in infinite-dimensional Bayesian statistics,” Ann. Statist., 34, 837–877. 

- Lian, H. (2009), “On rates of convergence for posterior distributions under misspecification,” Comm. Statist. Theory Methods, 38, 1893–1900. 

- Martin, R. and Hong, L. (2012), “A law of large numbers for martingale arrays with applications in nonparametric estimation,” Unpublished manuscript, arXiv.1201.3102. 

- Pati, D., Dunson, D. B., and Tokdar, S. T. (2011), “Posterior consistency in conditional distribution estimation,” Unpublished manuscript. 

- Schwartz, L. (1965), “On Bayes procedures,” Z. Wahrs. verw. Geb., 4, 10–26. 

- Shalizi, C. R. (2009), “Dynamics of Bayesian updating with dependent data and misspecified models,” Electron. J. Stat., 3, 1039–1074. 

- Shen, X. and Wasserman, L. (2001), “Rates of convergence of posterior distributions,” Ann. Statist., 29, 687–714. 

- Tokdar, S. T. (2006), “Posterior consistency of Dirichlet location-scale mixture of normals in density estimation and regression,” Sankhy¯a, 68, 90–110. 

- Walker, S. (2003), “On sufficient conditions for Bayesian consistency,” Biometrika, 90, 482–488. 

- (2004), “New approaches to Bayesian consistency,” Ann. Statist., 32, 2028–2043. 

- Walker, S. G., Lijoi, A., and Pr¨unster, I. (2007), “On rates of convergence for posterior distributions in infinite-dimensional models,” Ann. Statist., 35, 738–746. 

- Wu, Y. and Ghosal, S. (2008), “Kullback Leibler property of kernel mixture priors in Bayesian density estimation,” Electron. J. Stat., 2, 298–331. 

- (2010), “The L1-consistency of Dirichlet mixtures in multivariate Bayesian density 

- estimation,” J. Multivariate Anal., 101, 2411–2419. 

20 

