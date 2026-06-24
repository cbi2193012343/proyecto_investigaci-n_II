*Manuscript Click here to download Manuscript: RACSAM_EPTOB_R2.tex Click here to view linked References 

```
 1
```

```
 2
```

```
 3
```

```
 4
```

Noname manuscript No. (will be inserted by the editor) 

```
 5
```

```
 6
```

```
 7
```

```
 8
```

`9` Bayes spaces: use of improper distributions and `10` exponential families 

- `11` 

- `12` 

```
13
```

- J. J. Egozcue · V. Pawlowsky-Glahn · 

`14` R. Tolosana-Delgado · M. I. Ortego · 

`15` G. van den Boogaart 

- `16` 

- `17` 

```
18
```

```
19
```

```
20
```

Received: date / Accepted: date 

```
21
```

```
22
```

Abstract Bayes spaces are vector spaces of sigma-additive positive measures. `23` Proportional measures are considered equivalent and can be represented by `24` densities with respect to a fixed dominating measure. The addition in these `25` spaces is perturbation. It corresponds to Bayes theorem, which appears as a `26` linear operation. Bayes spaces, with continuous dominating measures, contain `27` finite and infinite measures. Finite measures are equivalent to probability mea- `28 29` sures. Infinite measures include what in Bayesian statistics are called improper `30` priors and non-integrable likelihood functions, justifying the use of such im- `31` proper densities in Bayes theorem. Many concepts of probability theory can `32` be handled in a natural way in the context of Bayes spaces. Particularly, an `33` exponential family of probability densities appears as a cone contained in an `34` affine subspace of the Bayes space. The framework of Bayes spaces allows an `35` easy handling of exponential families and their extensions to improper distri- `36` butions. Furthermore, the vector space structure of Bayes spaces allows the `37` definition of derivatives of densities. In Bayesian statistics, these derivatives `38` are a new tool to examine sensitivity of posterior distributions with respect to `39` both observed data and prior changes. 

- `40` 

- `41` 

Keywords Simplex · Aitchison geometry · derivative · sensitivity 

- `42` 

- `43` 

- `44` 1 Introduction 

- `45` 

- `46` 

- `47` 

In the 1980’s, J. Aitchison [1,3], proposed the log-ratio approach to deal with compositional data. He proposed perturbation as a natural and interpretable 

- `48` 

- `49` 

- `50` 

- `51` 

- `52` 

- `53` 

J. J. Egozcue 

Dept. Matem´atica Aplicada III, Universidad Polit´ecnica de Catalunya Tel.: +34-93-4016908 

Fax: 

E-mail: juan.jose.egozcue@upc.edu Present address: Mod. C2 Campus Nord UPC, Jordi Girona 1–3, E-08034-Barcelona 

- `54` 

- `55` 

```
56
```

- `57` 

- `58` 

- `59` 

- `60` 

- `61` 

```
62
63
64
65
```

```
 1
```

```
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
```

2 

operation between elements of the simplex. When motivating the interpretation of perturbation, Aitchison noted that, identifying probability vectors with elements of the simplex, perturbation is the discrete probability Bayes formula. If p = (p1, p2, . . . , pk) and q = (q1, q2, . . . , qk) denote probability vectors, i.e. � pi = � qi = 1 and all components are positive, they are elements of the unit k-part simplex, S[k] . Their perturbation is 

**==> picture [292 x 25] intentionally omitted <==**

where C is the closure operator, which assigns a vector of positive components adding to one to a vector whose components are positive. If p is identified with a prior set of probabilities and q is proportional to a discrete likelihood, then p ⊕ q is the posterior probability following Bayes formula. Equation (1), can be used when p and q are simply vectors of positive components, i.e. non necessarily normalized to unit, and the result p ⊕ q remains in S[k] . Therefore, there is no need of using a normalized likelihood. 

Although incidentally, J. Aitchison [3] also introduced powering of a vector of the simplex. For α a real constant, powering of p ∈S[k] by α is 

**==> picture [227 x 11] intentionally omitted <==**

At the beginning of the XXI century, the equivalence of vectors of proportional positive components, based on the principle of scale invariance for compositional data [3], became evident [4,8]. From this perspective, the elements of the simplex are thought of as representatives of the equivalence class of vectors with proportional components. At the same time, the simplex S[k] , with perturbation and powering as operations, is a (k − 1)–dimensional vector space [6,5]. Adding the distance defined in [2] and the associated inner product and norm, S[k] becomes a Euclidean space [21,13]. As a consequence, the Bayes formula can be viewed as the group operation (addition) in the so-called Aitchison geometry of the simplex (see [17] for a formal review). After closure, both prior, likelihood and posterior are represented within the Aitchison geometry of the simplex. Figure 1 shows the simple but appealing vector representation of Bayes formula using coordinates in S[3] . The (orthonormal) basis used in Figure 1 consists of the two S[3] compositions C exp(1/√2, −1/√2, 0), C exp(1/√6, 1/√6, −�2/3), where exp operates componentwise. This basis generates the balance-coordinates b1 = (1/√2) log(p1/p2) and b2 = �2/3 log[(p1p2)[1][/][2] /p3], where the pi are proportional to probabilities in the Bayes formula. 

The intuitive idea that elements of the simplex S[k] can approach probability densities by increasing k, the number of parts, and labelling them with real numbers, led to a first attempt to extend the Aitchison geometry of the simplex to probability densities supported on a finite interval [18]. The result was twofold: (a) the extended space contains both densities associated with finite and with infinite positive measures; (b) the set of square-log-integrable densities constitutes a Hilbert space where the addition is Bayes theorem for densi- 

```
 1
```

3 

```
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
```

**==> picture [336 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>-1 -0.8 -0.6 -0.4 -0.2 0 0.2<br>-0.2<br>-0.4<br>-0.6<br>-0.8<br>b1<br>1 2 3 1 2 3 1 2 3 PRIOR LIKELIHOOD POSTERIOR<br>b2<br>**----- End of picture text -----**<br>


Fig. 1 Left panel, from left to right: fictitious priori, likelihood and posterior represented as histograms. Right panel: vector representation of Bayes formula using balance-coordinates. 

ties on a continuos support. As in the case of discrete probability, perturbation admits non-normalized and non-integrable priors or likelihood functions. 

The next step in the generalization of the Aitchison geometry to density functions was the introduction of Bayes spaces (van den Boogart et al. 2010 [15]), linear spaces of densities/measures supported on an arbitrary measurable space. This approach reproduced the main facts described in [18] in a quite more general framework to the price of a more detailed theory, and added some results on exponential families. Section 2 presents a summary of the theory of Bayes spaces. Our present aim is to rethink the use of improper priors and non-integrable likelihood functions as used in Bayesian statistics (Section 3). The vector space structure of Bayes spaces allows the definition of derivatives of densities, and Section 4 illustrates some potential uses. 

## 2 Bayes spaces 

This section contains the elements of the theory of Bayes spaces developed in [15]. It is presented here for completeness of the following sections. The elements of a Bayes space are classes of sigma-additive, positive measures defined on a measurable space (Ω, A), where Ω is a set and A is a sigmaalgebra on it. These measures are called simply measures for short. In the examples presented in the following sections, Ω is alternatively identified with the real numbers, R, the non-negative real numbers, R+, or with the nonnegative integers, N0, equipped with the standard sigma-algebras (Borelian sets, etc.). Other choices, including multidimensional real spaces, are possible. Then, a reference measure λ, defined on Ω, is selected. Reference measures are called dominating measures to reserve the term reference for its usual use in Bayesian statistics (e.g. Bernardo, 1979 [9]). The dominating measure can be the Lebesgue measure on R, its restriction to R+, or the counting measure on N0. Probability measures can be used as well as dominating measures, e.g. 

```
 1
```

```
 2
```

4 

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
```

the standard normal on R. Given a dominating measure λ in Ω, the set of measures M(λ) is defined as follows: a measure µ is in M(λ) if for all A ∈A, λ(A) = 0 iff µ(A) = 0. In M(λ) all measures are absolutely continuous with respect to λ and, therefore, their Radon-Nikod´ym derivatives exist. In M(λ), all measures can be identified with their densities with respect to λ, e.g. µ is identified by fµ = dµ/dλ, where the subscript may be substituted by the name of a random variable which probability measure is µ. 

Inspired on the principle of scale invariance for compositional data and the likelihood principle (e.g. Robert, 1994 [22] or Birnbaum, 1962 [14]) that consider proportional positive functions equivalent, an equivalence relation, called B-equivalence and denoted (=B), is defined. If fµ and fν are the densities of µ, ν ∈M(λ) respectively, then fµ(x) =B fν(x) iff there exist a positive constant c > 0 such that, fµ(x) = c · fν(x), λ − a.e. (λ-almost everywhere), i.e. if their densities are proportional. B-equivalence allows to represent a class of proportional densities by any of its members, e.g. if µ is a finite measure it can be represented by its normalization to unit integral, which is a standard probability density function. The set of B-equivalence classes with dominating measure λ is denoted B(λ). 

A commutative group operation called perturbation (⊕) is defined in B(λ) 

as 

**==> picture [148 x 11] intentionally omitted <==**

Therefore, up to a multiplicative constant, perturbation is multiplication of densities. Also, a multiplication by real constants, called powering (⊙), is deas 

**==> picture [129 x 12] intentionally omitted <==**

The neutral element of perturbation in B(λ) is a constant density which corresponds to the dominating measure. Opposite-perturbation densities are obtained using (−1) powering, i.e. the opposite-perturbation of fµ is ⊖fµ =B (−1)⊙ fµ, λ− a.e. Perturbation-subtraction fµ ⊖ fν corresponds to the RadonNikod´ym derivative of the measure µ with respect to the measure ν. With ⊕ and ⊙, B(λ) is a vector space on R. Depending on the dominating measure it can be either finite or infinite dimensional. Standard definitions of linear dependence-independence, linear subspaces and affine geometry can be rephrased in B(λ) without any additional difficulty. 

Special attention deserve r-dimensional affine subspaces of B(λ). Let fi, i = 0, 1, 2, . . ., r be r linearly independent densities in B(λ); denoting by[�] i repeated perturbation on the subindex i, 

**==> picture [222 x 23] intentionally omitted <==**

is contained in an r-dimensional affine subspace with origin at f0 and basis fi, i = 1, 2, . . . , r. In Eq. (3) the specification λ − a.e. has been suppressed for short, and will be so from now on. Particularly, using the terminology of analytical geometry, f spans a straight-line if r = 1, a plane if r = 2, . . . 

```
61
```

```
62
63
64
65
```

```
 1
```

```
 2
```

`3` 5 `4 5 6` 3 Bayes theorem and improper distributions `7 8` Improper distributions have been used in Bayesian statistics for a long time `9` (e.g. [20], [16]). However, the reasons for their use are not clear, and the argu- `10` ments in favor or against depend on the author. For instance, Box and Tiao `11` (1973) [16] admit improper priors whenever the likelihood function is concen- `12` trated so that the posterior is proper. This is similar to claim for a proper `13` posterior distribution [10]. In other cases, improper priors are just not recom- `14` mended or are only considered admissible when obtained as objective reference `15` priors as a limiting form of proper ones (see an interesting discussion on ref- `16` erence priors in [11]). An interesting summary advocating the adequate use of `17` improper priors can be found in [22] (pp. 25–28). `18 19` Bayes spaces [15] provide a formal framework to deal with the controversial `20` use of improper distributions, both improper priors and non integrable like- `21` lihood functions, in the context of Bayesian statistics. Improper priors, non `22` integrable likelihood functions, or even improper posteriors, represent mea- `23` sures included in some B(λ).(λ).λ).). To make this evident, some generalization of `24` probability theory is needed, specifically in terms of its interpretation. First `25` of all it is worth pointing out that probability of an event is not an absolute `26` measure. It should be compared with the probability of another event. When `27` one asserts that event A11 has probability p1,1,, it is relative to the convention `28` that the probability of the whole probability space is 1, or better, that the `29` probability of the complementary, A1,1,, is 1 − p1.1.. Apparently this allows to `30` think about probabilities as absolute values, although it is, in fact, relative to `31` the complementary. If one is faced to compare evidence in favor of A11 relative `32` to another event A2,2,, which has probability p2,2,, the only relevant quantity is `33` the ratio, also called odds, p1/p2, or the typical log-odds-ratio, log(p1/p2). The p1/p2, or the typical log-odds-ratio, log(p1/p2). The1/p2, or the typical log-odds-ratio, log(p1/p2). The/p2, or the typical log-odds-ratio, log(p1/p2). The2, or the typical log-odds-ratio, log(p1/p2). The, or the typical log-odds-ratio, log(p1/p2). Thep1/p2). The1/p2). The/p2). The2). The). The `34` ratio p1/p2 p1/p21/p2/p22 is scale-invariant, it does not matter if the probability was set to 1, `35` to 100, or even if the whole space was assigned with an infinite, thus improper, `36 37` probability, as long as p11 and p22 are finite. This means that for comparison `38` of evidence of two events using ratios, the fact that the used measure is finite `39` or infinite, is irrelevant. For easy terminology, any density f in B(λ)(λ)λ)) can be `40` called evidence function.. Its integral on A ∈A, ∈A,, `41 42` evf (A) = IA(x)f (x)dλ(x) , `43` � `44 45` where IA(x) is the indicator function of A, is called evidence of A. Provided `46` that for two events A1, A2 ∈A, evf (A1), evf (A2) < +∞, they can be com- `47` pared using log(evf (A1)/evf (A2)): positive values of this log-ratio point out `48` evidence in favor of A1, negative values of the log-ratio indicate evidence in `49` favor of A2, and a null log-ratio means equal evidence of A1 and A2. As a `50` consequence, the fact of whether f is integrable or not over the whole space is `51` irrelevant for comparing finite evidences of events. `52` The use and interpretation of non-integrable likelihood functions in Bayesian `53` statistics seems to be less controversial than the case of improper priors. They `54 55 56 57 58 59 60 61 62 63 64 65` 

Bayes spaces [15] provide a formal framework to deal with the controversial use of improper distributions, both improper priors and non integrable likelihood functions, in the context of Bayesian statistics. Improper priors, non integrable likelihood functions, or even improper posteriors, represent measures included in some B(λ).(λ).λ).). To make this evident, some generalization of probability theory is needed, specifically in terms of its interpretation. First of all it is worth pointing out that probability of an event is not an absolute measure. It should be compared with the probability of another event. When one asserts that event A11 has probability p1,1,, it is relative to the convention that the probability of the whole probability space is 1, or better, that the probability of the complementary, A1,1,, is 1 − p1.1.. Apparently this allows to think about probabilities as absolute values, although it is, in fact, relative to the complementary. If one is faced to compare evidence in favor of A11 relative to another event A2,2,, which has probability p2,2,, the only relevant quantity is the ratio, also called odds, p1/p2, or the typical log-odds-ratio, log(p1/p2). The p1/p2, or the typical log-odds-ratio, log(p1/p2). The1/p2, or the typical log-odds-ratio, log(p1/p2). The/p2, or the typical log-odds-ratio, log(p1/p2). The2, or the typical log-odds-ratio, log(p1/p2). The, or the typical log-odds-ratio, log(p1/p2). Thep1/p2). The1/p2). The/p2). The2). The). The ratio p1/p2 p1/p21/p2/p22 is scale-invariant, it does not matter if the probability was set to 1, to 100, or even if the whole space was assigned with an infinite, thus improper, probability, as long as p11 and p22 are finite. This means that for comparison of evidence of two events using ratios, the fact that the used measure is finite or infinite, is irrelevant. For easy terminology, any density f in B(λ)(λ)λ)) can be called evidence function.. Its integral on A ∈A, ∈A,, 

The use and interpretation of non-integrable likelihood functions in Bayesian statistics seems to be less controversial than the case of improper priors. They 

```
 1
```

```
 2
```

```
 3
```

6 

```
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
```

```
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
```

```
42
43
44
45
46
47
48
49
50
51
52
53
```

```
54
55
56
57
58
59
60
61
62
63
64
65
```

appear as attached to the kind of experiment providing the data or, equivalently, the probability model of the observations. However, the problem is similar to the improper prior case because, ultimately, Bayes theorem is based on the existence of a (proper) joint probability distribution of observations and parameters. The density of parameters conditional to observed values (i.e. likelihood) should be a probability density or, if not normalized, a density of a measure. 

On the other hand, both prior densities and likelihood functions are evidence functions: both convey the same kind of information, the first conditional to the subjectiveness of the analyst and the second conditional to the observations and the assumed model. There is no obvious reason to treat them as different objects. Consequently, they are treated here as evidence functions or densities in B(λ). The fact that likelihood functions are obtained from the joint density of the sample, given the parameters, thus quantifying uncertainty of observations, does not contradict its character of evidence function on the parameters. In fact, in a likelihood function, sample values are considered fixed, whereas parameters appear as the arguments of the likelihood/evidence function. 

The critical point when removing the condition of integrability of priors and likelihood functions is the validity of Bayes theorem or, in terms of B(λ), of perturbation as the way of updating evidence on the parameters. This task is not difficult if one postulates perturbation in B(λ) as the operation that integrates evidence from two sources of information. The only requirement should be the coherence with the probabilistic Bayes theorem. 

To put the approach in the context of Bayes spaces, consider Ω = Ωx × Ωθ where Ωx is the space of observations and Ωθ the space of parameters. The sigma-algebra in Ω is obtained from the sigma-algebras Ax, Aθ, defined in Ωx, Ωθ, respectively. Similarly, λx, λθ, dominating measures in Ωx, Ωθ, respectively, provide a dominating measure λ in Ω. If Ax ∈Ax and Aθ ∈Aθ, then λ(Ax × Aθ) = λx(Ax) · λθ(Aθ). Measures in B(λ) are represented by densities with respect to λ and can be proper (finite) or improper (infinite). Assume that, using some model linking observations and parameters, a joint evidence function, f ∈ B(λ), is given such that 

f (x, θ) =B(λ) fx(x|θ) ⊕B(λθ) fθ(θ) =B(λ) fθ(θ|x) ⊕B(λx) fx(x) , (4) where equivalence and perturbation signs have been subscripted to indicate which space they are referred to. Condition (4) is formally equivalent to Bayes theorem except for the following points: (a) any of the densities can correspond to infinite (improper) measures; (b) the densities fθ(θ) and fx(x) are proportional to the standard marginals if f corresponds to a finite measure, but this is no longer true whenever f represents an infinite measure; (c) fx(x|θ), fθ(θ|x) are proportional to conditional densities for f integrable, i.e. corresponding to a finite measure, but again they have no interpretation in the strict probabilistic sense when f is non integrable. 

The last two terms in (4) lead to 

**==> picture [160 x 12] intentionally omitted <==**

**==> picture [14 x 11] intentionally omitted <==**

```
 1
```

```
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
```

7 

```
11
12
```

```
13
```

```
17
18
19
```

```
30
31
32
33
34
35
36
37
38
39
```

which, after removing constant terms in x, coincides with the probabilistic Bayes theorem when the three densities in Eq. (5) represent finite measures in B(λθ). 

Expressions (4) and (5) are said event-coherent when their restrictions to events with finite evidence correspond to the standard probabilistic Bayes theorem. Consider any event A = Ax × Aθ ∈A such that evf (Ax × Aθ) < +∞; then 

```
14
15
```

```
16
```

```
20
```

```
21
```

```
22
```

```
23
```

```
24
```

```
25
```

```
26
```

```
27
```

```
28
```

```
29
```

```
40
```

```
41
```

```
42
```

```
43
```

```
44
```

```
45
```

```
46
```

```
47
```

```
48
```

**==> picture [293 x 41] intentionally omitted <==**

where |A, |Ax and |Aθ denote restriction of the measure to the sets A, Ax, Aθ, respectively. For instance, B(λθ(θ|Aθ)) has dominating measure λθ restricted to the event Aθ. Similarly, Eq. (5) restricted to the event Aθ is 

**==> picture [285 x 12] intentionally omitted <==**

where all evidence functions correspond to finite measures. In the conditions of Eq. (5), comparison of evidence of two events in θ, D1, D2 ⊆ Aθ is equivalent to compare their respective probabilities. In fact, in Aθ, the posterior probability density p(θ|x) = c · (fθ(θ|x, Aθ) · f0(θ|Aθ)) where c is the normalizing constant and f0 denotes the density of the dominating measure with respect to the standard measure used in probability theory, i.e. Lebesgue for continuous variables, counting measure for discrete variables. The computation of the ratio of posterior probabilities of D1 and D2 is 

**==> picture [264 x 84] intentionally omitted <==**

A similar result can be obtained using the prior densities. Equation (8) implies that ratio comparisons of prior and posterior probabilities of two events obtained from restricted inferences, where all densities (prior, likelihood, posterior) are proper (Eq. 7), and from an extended Bayes formula, admitting improper priors, non integrable likelihoods and/or improper posteriors (Eq. 5), are equal. This constitutes the essence of the event-coherence of Bayes theorem extended to the framework of Bayes spaces. 

```
49
```

```
50
```

```
51
```

```
52
```

```
53
```

```
54
```

## 4 Derivative of a density with respect to external parameters 

In the framework of Bayes spaces, proper and improper densities (priors, likelihood functions and posteriors) are viewed as vectors. In some cases they can 

```
55
56
57
58
59
```

```
60
```

```
61
```

```
62
```

```
63
64
65
```

```
 1
```

```
 2
```

8 

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
```

depend on some external variables (time, space, temperature, . . . ), thus defining a function from these variables into the corresponding Bayes space. Particularly, likelihood functions of one parameter given some observation is an example of this kind of functions, where the observations play the role of external variables. Also prior densities are often selected from a given family of densities by fixing the value of some parameters, hereafter called hyper-parameters to distinguish them from parameters which are the target of Bayesian inference. 

An interesting idea is to define derivative of these functions with respect to external parameters. For simplicity, consider the case of a single real external variable, f : R → B(λ). The derivative is again a function D[⊕] f : R → B(λ), defined as the limit, if it exists, 

**==> picture [262 x 22] intentionally omitted <==**

where x spans the measurable space Ω and t is the real external variable considered. The limit in (9) can be defined on the topology of the vector space B(λ). If the limit exists, it can be obtained using x-point convergence (λ − a.e.). Stronger convergence criteria can be defined but, in general, they require some metrics on B(λ). The superscript in Dt[⊕][,][called][generically][B][-] derivative, recalls that increments of densities in B(λ) are computed using the perturbation-subtraction, and not the usual real difference. Definition (9) is an extension of the derivative of simplicial functions used in compositional data analysis [19]. 

Computation of B-derivatives is reduced to logarithmic derivatives. If Dt[⊕][f][(][x][|][t][)][exists,][then] 

**==> picture [143 x 12] intentionally omitted <==**

where Dt denotes the derivative of a real function with respect to t. 

Derivative of functions in B(λ) have potential applications in robust statistics, sensitivity analysis with respect to prior densities in Bayesian statistics, or in the framework of exponential families of distributions. For instance, the fact that exponential families lie in an affine subspace of B(λ) means that the B-derivative of the family with respect to each of its parameters gives a tangent direction included in the affine subspace. Constant direction derivatives in B(λ) with respect to all parameters imply that the family is exponential, a sufficient condition. The following examples illustrate these properties. 

Derivatives of the Gamma exponential family 

Consider the exponential Gamma family in R+ 

**==> picture [298 x 12] intentionally omitted <==**

which elements are probability densities provided that C(a, b) is the appropriate normalizing constant. The densities f (x|a, b) (10) are the densities of the 

```
59
```

```
60
```

```
61
```

```
62
```

```
63
64
65
```

```
 1
```

```
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
```

9 

Gamma family with respect to the Lebesgue measure restricted to R+, denoted λ+. These probability densities are in B(λ+) and they can be re-written as 

**==> picture [271 x 21] intentionally omitted <==**

Whenever the restrictions on a and b are removed from (10), the expression still corresponds to a density of an infinite measure with respect to λ+. Therefore, Eq. (11) spans a two-dimensional affine subspace of B(λ+), with origin at 1/x, and constitutes an extended exponential family [15]. Note that the obvious basis of this subspace is x[±][1] , exp(±x), which first element is not a proper probability density and the second one depends of the selected sign. The B- derivatives of f (x|a, b) (11) with respect to a and b are respectively 

**==> picture [290 x 14] intentionally omitted <==**

which is the expected result. In fact, x and exp(−x) are constant directions, as densities in B(λ+), and their logarithms coincide with the so-called sufficient statistics for a and b respectively in the Gamma exponential family. It is interesting to realise that the origin of the affine subspace is 1/x. The density 1/x could be taken as density of a dominating measure. In that case, f (x|a, b)/(1/x) is the extended Gamma family, and would appear as a subspace in B(1/x). The origin of the subspace would be at the dominating measure with density 1/x, which would be the neutral element. 

## Tangent exponential family 

The derivative in a Bayes space allows to go a little bit further, and get an expression of a tangent exponential family to a family which is not exponential. The univariate skew-normal family [7] is 

**==> picture [261 x 25] intentionally omitted <==**

```
43
```

```
44
45
46
47
48
49
```

```
50
```

```
51
52
53
```

```
54
55
56
57
58
```

where ϕ(x), Φ(x) are the probability density and cumulative distribution of a N (0, 1) distribution, respectively. Assuming µ = 0 and σ = 1, a single parameter family in α is considered for simplicity. To deal with this single parameter skew-normal family, it is convenient to take the N (0, 1) measure as dominating measure in the Bayes space, denoted B(ϕ). The density of f (x|µ, σ, α) with respect to the measure N (0, 1), denoted f0, is 

**==> picture [251 x 12] intentionally omitted <==**

where the parameters µ, σ have been dropped from the notation of f . From Eq. (13), it is clear that the family is not exponential. The B-derivative in B(ϕ) with respect to α confirms this aspect: 

**==> picture [251 x 25] intentionally omitted <==**

```
59
```

```
60
```

```
61
```

```
62
```

```
63
64
65
```

```
 1
```

```
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
```

10 

involves α, and therefore, it is neither a constant density included in the extended exponential family, nor a constant direction in B(ϕ). For any fixed value of α, the tangent family has the expression 

**==> picture [197 x 24] intentionally omitted <==**

where β is the real parameter which allows g0 to span the whole tangent exponential family. In terms of a density with respect to the Lebesgue measure in R, g0 corresponds to 

**==> picture [197 x 25] intentionally omitted <==**

where C(β) is the normalizing constant for β > 0. This example shows that Bayes spaces supply a useful geometric terminology to distribution theory. 

## Tangent sensitivity analysis 

```
33
34
```

```
35
```

```
36
```

```
37
```

```
38
```

```
39
```

```
40
```

A possible use of the B-derivative of measures in a Bayesian context is sensitivity analysis. Sensitivity analysis is normally understood as a description of changes of posterior characteristics due to changes in the prior distribution. Sensitivity of posterior characteristics can also be conceived with respect to changes in observed data. In general, derivatives describe these relative changes, and the B-derivative is appropriate in this case. The first relevant property is that the B-derivative of a posterior density with respect to one hyper-parameter of the prior is equal to the B-derivative of the prior density, regardless of the likelihood function, which does not depend on the prior hyper-parameters. From (4), Bayes theorem can be rewritten as 

**==> picture [259 x 12] intentionally omitted <==**

where the dependence of the prior on the hyper-parameters ψ has been made explicit. As the dominating measure in B(λθ) and the likelihood function do not depend on ψ, Equation (14) yields 

```
41
```

```
42
```

```
43
```

```
44
```

```
45
```

```
46
```

**==> picture [146 x 14] intentionally omitted <==**

A similar result is obtained if sensitivity with respect to one observed-datapoint is required: the B-derivative of the posterior with respect to one observeddata-point is equal to the B-derivative of the likelihood function. 

`47` To illustrate the possibilities in sensitivity analysis, consider, for instance, `48` that a number of events xo have been observed within a time to. Assume `49` these events occur as a Poisson process with parameter θ (events per unit of `50` time). The number of events within time to is denoted X and has a Poisson `51` distribution with parameter θ. The likelihood of θ, given the observation, is 

```
52
```

```
53
```

```
54
```

**==> picture [141 x 24] intentionally omitted <==**

```
55
```

```
56
57
```

```
58
```

```
59
```

```
60
```

```
61
```

```
62
```

```
63
```

```
64
65
```

```
 1
```

```
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

11 

The prior density for θ is chosen from the Bayesian conjugate Gamma family. The prior density of θ is then 

**==> picture [253 x 24] intentionally omitted <==**

where the positiveness of a and b guarantees that the prior is proper. Typically, a = 0 provides an improper prior. Suppose that the value of a and b have been elicited, and therefore, the prior mean and variance of θ are a/b and a/b[2] , respectively, provided a > 0 and b > 0. The change of the posteriori with respect to a or to b may be of interest in a sensitivity analysis. For instance, taking into account the B-derivatives of the Gamma family (12), 

**==> picture [187 x 12] intentionally omitted <==**

**==> picture [218 x 13] intentionally omitted <==**

The posterior changes due to small changes of the hyper-parameters a + δa, b + δb, are linearly approximated perturbing the posterior by 

**==> picture [121 x 11] intentionally omitted <==**

Making the changed posterior explicit, 

**==> picture [313 x 12] intentionally omitted <==**

where ≃B means tangent approximation. In this particular case, the equality =B holds in Eq. (15) due to the fact that the Gamma family is a plane in B(λ+) and coincides with its tangent plane. According to the expression of the perturbed posterior (15), prior hyper-parameter a + δa can be viewed as the number of events which occurred in a fictitious observation during a time b + δb, additional to the actually observed events xo in a time to [12]. A remarkable fact is that (15) is valid even if the prior was improper. For instance, with a = 0, the prior is improper, but a positive or negative δa still can be interpreted as an increment/decrement of the observed events. A similar interpretation is valid for b = 0, that generates an improper prior, as δb can be interpreted as a fictitious increment/decrement of the observation time t0. If a ≤ 0 or b ≤ 0 the prior is improper, but the posterior is a proper one if xo + a > 0 and t0 + b > 0. 

This example uses a Bayesian conjugate prior from the Gamma exponential family and the interpretation of the hyper-parameters and their increments from the known expression of the posterior. A less simple example consists of using another type of prior. For instance, assume that the prior for θ has a log-normal distribution which density is 

**==> picture [261 x 53] intentionally omitted <==**

```
62
63
64
65
```

```
 1
```

```
 2
```

12 

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
```

The B-derivatives of this prior with respect to the hyper-parameters are 

**==> picture [288 x 55] intentionally omitted <==**

The posterior density for θ, when the hyper-parameters m and s[2] are modified to m + δm and s[2] + δs[2] , respectively, is linearly approached by 

**==> picture [299 x 68] intentionally omitted <==**

From this expression, one realizes that changes on the ratio m/s[2] virtually modify the number of counted events xo, but time of observation to remains as actually observed. The density exp[− log[2] (θ)] has the characteristic shape of the log-normal density. Its main role is introducing a penalty on very small values of θ, i.e. positive values of δs[2] reduce the posterior probability of small number of events per time unit. 

Geometrically, this kind of sensitivity analysis consists of approaching the posterior, as a function of the prior hyper-parameters, by the tangent space at the values of the elicited hyper-parameters. However, to complete a sensitivity analysis, two additional geometric concepts are needed. One is the possibility of measuring the size of the derivatives, i.e. a norm on elements of the B- spaces. The other is orthogonality of directions, here represented by densities such as θ, exp(−θ), exp[− log[2] (θ)] in the example. These concepts, which are available in Hilbert spaces, have been developed on B-spaces with uniform dominating measure restricted to a finite real interval [18]. They hold also for discrete measures restricted to a finite number of points, thus reducing to the geometry of the simplex [21]. An extension to general dominating measures is underway. 

## 5 Conclusions 

The elements of Bayes spaces are classes of proportional sigma-additive measures which are represented by densities with respect to a fixed dominating measure. The group operation, called perturbation, is equivalent to Bayes theorem applied to a likelihood and a prior distribution. With this operation, Bayes spaces are vector spaces. The fact that Bayes spaces include both proper and improper probability measures raised a discussion on the use of improper priors and non-integrable likelihood functions in Bayesian statistics. Prior and posterior densities (proper or improper) and likelihood functions (integrable or 

```
 1
 2
```

```
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
```

13 

not) are elements of Bayes spaces, called herein evidence functions. It has been shown that evidence functions, disregarding their proper o improper character, can be used to carry out comparisons of probabilities of events satisfying the event-coherence condition. 

Bayes spaces also provide a framework where standard probability concepts can be thought of in geometric terms. For instance, exponential families of probability densities can be viewed as convex cones within a finite dimensional linear manifold, as previously proven in [15]. Here, a derivative in Bayes spaces has been defined, and its use to build the tangent linear manifold to a nonexponential family has been exemplified. Related to sensitivity of a posterior density with respect to prior parameters, the derivative of the posterior is shown to be equal to that of the prior. 

Acknowledgements This research has been supported by the Spanish Ministry of Education and Science under two projects: ’Ingenio Mathematica (i-MATH)’ Ref. No. CSD200600032 and ’CODA-RSS’ Ref. MTM2009-13272; and by the Ag`encia de Gesti´o d’Ajuts Universitaris i de Recerca of the Generalitat de Catalunya under the project Ref: 2009SGR424. 

## References 

1. Aitchison, J.: The statistical analysis of compositional data (with discussion). Journal of the Royal Statistical Society, Series B (Statistical Methodology) 44(2), 139–177 (1982) 

2. Aitchison, J.: Principal component analysis of compositional data. Biometrika 70(1), 57–65 (1983) 

3. Aitchison, J.: The Statistical Analysis of Compositional Data. Monographs on Statistics and Applied Probability. Chapman & Hall Ltd., London (UK). (Reprinted in 2003 with additional material by The Blackburn Press) (1986) 

4. Aitchison, J.: On criteria for measures of compositional difference. Mathematical Geology 24(4), 365–379 (1992) 

```
33
34
```

5. Aitchison, J., Barcel´o-Vidal, C., Egozcue, J.J., Pawlowsky-Glahn, V.: A concise guide 

`35` for the algebraic-geometric structure of the simplex, the sample space for compositional 

`36` data analysis. In: U. Bayer, H. Burger, W. Skala (eds.) Proceedings of IAMG’02 — The `37` eigth annual conference of the International Association for Mathematical Geology, vol. `38` I and II, pp. 387–392. Selbstverlag der Alfred-Wegener-Stiftung, Berlin, 1106 p (2002) 

   6. Aitchison, J., Barcel´o-Vidal, C., Mart´ın-Fern´andez, J., Pawlowsky-Glahn, V.: Reply to Letter to the Editor by S. Rehder and U. Zier. Mathematical Geology 33(7), 849–860 (2001) 

```
39
```

- `40` 

- `41` 7. Azzalini, A., Dalla Valle, A.: The multivariate skew-normal distribution. Biometrika `42` 83(4), 715–726 (1996) 

- `43` 8. Barcel´o-Vidal, C., Mart´ın-Fern´andez, J.A., Pawlowsky-Glahn, V.: Mathematical foun- `44` dations of compositional data analysis. In: G. Ross (ed.) Proceedings of IAMG’01 — The sixth annual conference of the International Association for Mathematical Geology, 

- `45` pp. 1–20 (2001). CD-ROM 

- `46` 

   9. Bernardo, J.M.: Reference posterior distributions for Bayesian statistics. J. Royal Statistical Society, B 41(2), 113–147 (1979) 

- `47` 

   10. Bernardo, J.M.: Bayesian statistics. Encyclopedia of Life Support Systems (EOLSS), A Integrated Virtual Library. www.eolss.net. Probability and Statistics (R. Viertl, ed). Oxford, UK: UNESCO, 2003. (2003) 

- `48` 

- `49` 

- `50` 

11. Bernardo, J.M., Ram´on, J.M.: An introduction to Bayesian reference anlysis: inference 

`51` on the ratio of multinomial parameters. The Statistician 47(Part 1), 101–145 (1998) 

   12. Bernardo, J. M. , Smith A. F. M.: Bayesian Theory. Wiley, Chichester, UK (1986) 

- `52` 

- `53` 13. Billheimer, D., Guttorp, P., Fagan, W.: Statistical interpretation of species composition. Journal of the American Statistical Association 96(456), 1205–1214 (2001) 

- `54` 

- `55` 

- `56` 

- `57` 

- `58` 

- `59` 

- `60` 

- `61` 

- `62` 

```
63
64
65
```

```
 1
```

```
 2
```

```
 3
 4
 5
```

14 

```
 6
 7
 8
 9
```

```
10
```

14. Birnbaum, A.: On the foundations of statistical inference (with discussion). J. Amer. Statist. Assoc. 57, 269–326 (1962) 

15. van den Boogaart, K.G., Egozcue, J.J., Pawlowsky-Glahn, V.: Bayes linear spaces. Statistics and Operations Research Transactions, SORT 34(2), 201–222 (2010) 

16. Box, G.E.P., Tiao, G.C.: Bayesian Inference in Statistical Analysis. Addison-Wesley, Reading Mass. USA (1973) 

17. Egozcue, J.J., Barcel´o-Vidal, C., Mart´ın-Fern´andez, J.A., Jarauta-Bragulat, E., D´ıazBarrero, J.L., Mateu-Figueras, G.: Elements of simplicial linear algebra and geometry. In: Pawlowsky-Glahn, V. and Buccianti A. (eds.), Compositional Data Analysis: Theory and Applications, Wiley, Chichester UK (2011) 

```
11
12
```

```
13
```

```
14
```

18. Egozcue, J.J., D´ıaz-Barrero, J.L., Pawlowsky-Glahn, V.: Hilbert space of probability 

`15` density functions based on Aitchison geometry. Acta Mathematica Sinica (English `16` Series) 22(4), 1175–1182 (2006) 

   19. Egozcue, J.J., Jarauta-Bragulat, E., D´ıaz-Barrero, J.L.: Calculus of simplex-valued functions. In: Pawlowsky-Glahn, V. and Buccianti A. (eds.), Compositional Data Analysis: Theory and Applications, Wiley, Chichester UK (2011) 

```
17
```

- `18` 

```
19
```

   20. Jeffreys, H.: Theory of probability. Oxford U. Press, London, third edition (first edition 1939) (1961) 

- `20` 

- `21` 21. Pawlowsky-Glahn, V., Egozcue, J.J.: Geometric approach to statistical analysis on the `22` simplex. Stochastic Environmental Research and Risk Assessment (SERRA) 15(5), 384–398 (2001) 

```
23
```

22. Robert, C.P.: The Bayesian choice. A decision-theoretic motivation. Springer-Verlag, 

`24` New York (1994) 

- `25` 

- `26` 

- `27` 

- `28` 

- `29` 

- `30` 

- `31` 

- `32` 

- `33` 

- `34` 

- `35` 

```
36
```

- `37` 

```
38
```

- `39 40` 

- `41` 

```
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
```

