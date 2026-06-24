## On the Local Lipschitz Stability of Bayesian Inverse Problems 

Bj¨orn Sprungk[†] 

> † Institute for Mathematical Stochastics, University of G¨ottingen, Goldschmidtstraße 7, 37077 G¨ottingen, Germany 

January 23, 2020 

## Abstract 

In this note we consider the stability of posterior measures occuring in Bayesian inference w.r.t. perturbations of the prior measure and the log-likelihood function. This extends the well-posedness analysis of Bayesian inverse problems. In particular, we prove a general local Lipschitz continuous dependence of the posterior on the prior and the log-likelihood w.r.t. various common distances of probability measures. These include the total variation, Hellinger, and Wasserstein distance and the Kullback–Leibler divergence. We only assume the boundedness of the likelihoods and measure their perturbations in an L[p] - norm w.r.t. the prior. The obtained stability yields under mild assumptions the well-posedness of Bayesian inverse problems, in particular, a well-posedness w.r.t. the Wasserstein distance. Moreover, our results indicate an increasing sensitivity of Bayesian inference as the posterior becomes more concentrated, e.g., due to more or more accurate data. This confirms and extends previous observations made in the sensitivity analysis of Bayesian inference. 

Keywords: Bayesian inference, robust statistics, inverse problems, well-posedness, Hellinger distance, Wasserstein distance, Kullback–Leibler divergence 

Mathematics Subject Classification: 60B10, 62C10, 62F15, 62G35, 65N21 

## 1 Introduction 

In recent years, Bayesian inference has become a popular approach to model and solve inverse problems in various fields of applications, see, e.g., [1, 2] for a comprehensive introduction. Here, noisy observations are used to update the knowledge of unknown parameters from a given prior distribution to a resulting posterior distribution. The relation between the parameters and the observable quantities are given by a measurable forwad map which, in combination with an assumed error distribution, determines the likelihood function for the data given the parameter. The Bayesian approach is quite appealing and, in particular, yields a wellposed inverse problem [1, 3, 4, 5, 6, 7], i.e., its unique solution—the posterior distribution—depends (locally Lipschitz) continuously on the observational data and behaves also stable w.r.t. (numerical) approximations of the forward map. However, besides the observed data and the employed likelihood model, the subjective choice of the prior distribution significantly affects the outcome of the Bayesian inference, too. In order to account for that a robust Bayesian analysis has emerged, where a class of suitable priors or likelihoods is considered and the range of all resulting posterior quantities or statistics is computed or estimated, see, e.g., [8, 9] for an introduction. Moreover, the well-known Bernstein–von Mises theorem [10] establishes a kind of “asymptotic stability” at least in finite-dimensional spaces. This theorem tells us that, under suitable assumptions, the posterior measure concentrates around the true parameter, which generates the observations, as more and more data is observed. This convergence to the truth is called consistency and it is independent of the chosen prior measure as long as the true parameter belongs to its support. However, for posterior measures 

1 

on infinite-dimensional spaces the situation is far more delicate, and positive as well as negative results for consistency exist, see, e.g., [11, 12, 13, 14]. Furthermore, in [15, 16, 17] the authors show an extreme instability of Bayesian inference—called Bayesian brittleness—w.r.t. small perturbations of the likelihood model as well as w.r.t. classes of priors based on only finitely many pieces of information. In particular, the range of attainable posterior quantities (e.g., expectations or probabilities) over a class of allowed priors and likelihoods covers the essential (prior) range of the quantity of interest. This brittleness occurs for arbitrarily many data and arbitrarily small perturbations of the likelihood model. However, the distance used to measure the size of the perturbations plays a crucial role here as we will discuss later on. 

In this paper we take a slightly different approach than the classical robust Bayesian analysis: Instead of bounding the resulting posterior range of certain quantities or statistics of interest for a given class of admissible priors or likelihood models, we rather study whether the distance between the posterior measures themselves can be bounded uniformly by a constant multiplied with the distance of the corresponding prior measures or log-likelihood functions. Thus, the goal is to establish a (local) Lipschitz continuity of the posterior w.r.t. the prior or the log-likelihood with explicit bounds on the local Lipschitz constant. To this end, we employ the following common distances and divergences for (prior and posterior) probability measures: the total variation, Hellinger, and Wasserstein distance as well as the Kullback–Leibler divergence. Perturbations of the log-likelihood function are measured by suitable L[p] -norms w.r.t. the prior measure. Indeed, under rather mild assumptions we can state the local Lipschitz continuity of posteriors on general Polish spaces w.r.t. the prior and the log-likehood for all distances and divergences listed above. On the other hand, our estimates show that the sensitivity of the posterior to perturbations of prior or log-likelihood increases as the posterior concentrates—an observation also made in [18, 19]. We discuss this issue and its relation to the Bernstein–von Mises theorem in Section 3 and 5 in detail. 

As mentioned at the beginning, a local Lipschitz dependence of the posterior measure w.r.t. the observational data and approximations of the forward map has been proven in [1, 6] for Gaussian and Besov priors and the Hellinger distance. These results have been generalized to heavy-tailed prior measures in [3, 4, 7] and a continuous dependence in Hellinger distance was recently shown under substantially relaxed conditions in [5]. In the latter work a continuous dependence on the data was also established concerning the Kullback– Leibler divergence and Wasserstein distance between the resulting posteriors. Moreover, in [20] it is shown that converging approximations of the forward map yield the convergence of the perturbed posteriors to the true posterior in terms of their Kullback–Leibler divergence. These previous results relate, of course, to our stability statements for perturbed log-likelihoods. 

However, the focus of this note is rather on the general structure of the local Lipschitz dependence on the log-likelihood and the prior measure. In fact, stability w.r.t. the data or approximations of the forward map follows—under suitable assumptions—from our general results. Besides that, the local Lipschitz dependence of the posterior on the prior has not been established in the literature to the best of our knowledge. Furthermore, a stability or well-posedness analysis of Bayesian inverse problems in Wasserstein distance (i.e., perturbations of posterior and prior are measured in Wasserstein distance) has also been missing—the recent results on continuity w.r.t. the observed data [5] have been established in parallel to our work. This distance is of particular interest for studying the stability w.r.t. perturbations of the prior measure on infinite-dimensional spaces such as function spaces. The reason behind is that the total variation and Hellinger distance as well as the Kullback–Leibler divergence obtain their maximum value for mutually singular measures and probability measures on infinite-dimensional spaces tend to be singular—cf., the necessary conditions for Gaussian measures on Hilbert spaces to be equivalent [21, 22]. Thus, these distances and divergences may be of little practical use for prior stability whereas the Wasserstein distance of perturbed priors does not rely on their equivalence. Besides that, the Wasserstein distance has been proven quite flexible and useful for various topics in probability theory such as convergence of Markov processes [23] and perturbation theory for Markov chains [24, 25]. We establish a first stability analysis of Bayesian inverse problems w.r.t. the Wasserstein distance and show how the general stability result yields a well-posedness of Bayesian inverse problems 

2 

in Wasserstein distance. For the latter we use the same basic assumptions stated in [1, 5, 6] for the wellposedness in Hellinger distance. 

In summary, this paper contributes to the stability analysis of Bayesian inference and provides positive statements in a quite general setting. Our results, although quantitative, are rather of qualitative nature establishing a local Lipschitz stability and, on the other hand, illustrating the increasing sensitivity of the posterior to perturbations in prior or log-likelihood for an increasingly informative likelihood. Our setting considers bounded likelihoods which excludes, e.g., the case of infinite-dimensional observations (cf. [1, Section 3.3]). 

The outline of the paper is as follows: In the next section we introduce the general setting and the common form of our main results. We also discuss their relation to classical robust Bayesian analysis and Bayesian brittleness. In Section 3 to 5 we provide the exact statements and proofs for stability in the Hellinger and total variation distance, Kullback–Leibler divergence, and Wasserstein distance. In particular, we establish in Section 5 the well-posedness of Bayesian inverse problems in Wasserstein distance. Furthermore, the relation of the obtained stability statements to the existing literature and results on robust Bayesian analysis is discussed in Section 6. The Appendix includes some more detailed explanations and calculations on the relation between Bayesian brittleness and stability as well as an explicit computation for the Hellinger distance of Gaussian measures on separable Hilbert spaces. 

## 2 Setting and Main Results 

Throughout this paper let (E, dE ) be a complete and separable metric space with Borel σ-algebra E and let P(E) denote the set of all probability measures µ on (E, E). We also consider the special case of a separable Hilbert space H with norm ∥· ∥H. 

In this paper we focus on posterior probability measures µΦ ∈P(E) of the form 

**==> picture [315 x 23] intentionally omitted <==**

resulting from a prior measure µ ∈P(E) and a measurable negative log-likelihood Φ: E → R+, R+ := [0, ∞). The constant Z := �E[e][−][Φ(][x][)][µ][(d][x][)][ ∈][(0][,][ ∞][)][ denotes the normalization constant, sometimes called] evidence. The assumption that Φ(x) ≥ 0 is convenient and not very restrictive, since any µΦ of the form (1) with Φ: E → R being bounded from below, i.e., inf x∈E Φ(x) > −∞, can be rewritten as µΦ(dx) = exp(−(Φ(x) − inf Φ))/(Z exp(− inf Φ)) µ(dx). 

Posterior measures as in (1) occur, for example, when we consider the Bayesian approach to inverse problems such as reconstructing an unknown x[†] ∈ E based on noisy data 

**==> picture [69 x 14] intentionally omitted <==**

of a measurable forward map G : E → R[n] with additive noise ǫ ∈ R[n] . Inverse problems are typically ill-posed and require some kind of regularization. In the Bayesian approach we employ a probabilistic regularization, i.e., we incorporate a-priori knowledge about x[†] by a prior probability measure µ ∈P(E), and assume a random noise ε ∼ νε ∈P(R[n] ), i.e., ǫ in the equation above is viewed as a realization of the random variable ε. The Bayesian approach then consists of conditioning the prior measure µ on observing the data y ∈ R[n] as a realization of the random variable 

**==> picture [307 x 12] intentionally omitted <==**

This results in a conditional or posterior probability measure on E. If the noise distribution allows for a bounded Lebesgue density νε(dǫ) ∝ exp(−ℓ(ǫ))dǫ, with ℓ : R[n] → R being bounded from below, inf ǫ∈Rn ℓ(ǫ) > −∞, then the posterior measure of X ∼ µ given that Y = y is of the form (1) with Φ(x) = Φ(x, y) := ℓ(y − G(x)), see, e.g., [1, 5, 6]. A common noise model is a mean-zero Gaussian noise, i.e., νε = N (0, Σ), 

3 

Σ ∈ R[n][×][n] symmetric and positive definite, which yields Φ(x) = Φ(x, y) =[1] 2[|][Σ][−][1][/][2][(][y][ −][G][(][x][))][|][2][where][ | · |] denotes the Euclidean norm on R[n] . For clarity, we omit the dependence of the observational data y in Φ most of the time. The main focus of this paper is to study the stability of the posterior µΦ w.r.t. perturbations of the log-likelihood model Φ as well as the chosen prior measure µ. 

An interesting and important special case in practice are Bayesian inverse problems in function spaces, i.e., where E is a separable Hilbert space such as H = L[2] (D) with D ⊂ R[n] denoting a spatial domain, cf. Example 1. In such situations Gaussian measures µ = N (m, C) on H are a convenient class of prior measures, see, e.g., [6, 1, 26, 27]. Often the mean m ∈H and the trace-class covariance operator C : H →H are chosen themselves from parametric classes. For instance, we may suppose a linear model for the mean m =[�][J] j=1[θ][j][φ][j][,][φ][j][∈H][,][with][parameter][θ][=][(][θ][1][, . . . , θ][J][)][∈][R][J][.][Or,][furthermore,][we][may][consider] Gaussian prior measures on suitable function spaces H ⊆ L[2] (D) with covariance operators belonging to the Mat´ern class, i.e., C = Cα,β,γ = β(I + γ[2] ∆)[−][α] with parameters α, β, γ > 0 and ∆ denoting the Laplace operator, see, e.g., [26, 27]. Since in practice the so-called hyperparameters θ, α, β, and γ are often estimated by statistical procedures, a stability of the resulting posterior measure w.r.t. slightly different means, covariances, or hyperparameters of the corresponding Gaussian prior measures seems highly desirable. Therefore, we remark in each of the following sections on particular bounds for posteriors resulting from perturbed Gaussian priors. 

Example 1. A model problem in Bayesian inverse problems is to infer a log conductivity coefficient u ∈ C(D), D ⊂ R[k] , of, e.g., a subsurface layer by noisy measurements of the corresponding potential p ∈ H[1] (D) which is typically described by an elliptic partial differential equation on D of the form 

**==> picture [173 x 15] intentionally omitted <==**

with suitable source term f ∈ L[2] (D) and boundary data g ∈ H[1][/][2] (∂D). In practice there are often (only) finitely many local observations of p as well as of u available, e.g., by measurements at borehole locations. The observations of u can then be used to derive a Gaussian prior measure µ = N (m, C) on H := L[2] (D) ⊃ C(D) for the (regularizing) Bayesian approach to the underdetermined inverse problem. However, as explained above the construction of the prior µ usually involves statistical estimation of hyperparameters for the mean m and the covriance C employing the noisy observations of u. For instance, for Mat´ern covariances the hyperparameters can be estimated by maximizing the corresponding Gaussian likelihood of the observed values of u. Therefore, also the solution of the Bayesian inverse problem, the posterior measure µΦ for u resulting from conditioning on the noisy data of p, will depend on the accuracy of this statistical estimation. Our results establish a local Lipschitz dependence of the resulting posterior on the chosen prior, thus, controlling the effect of (inaccurately estimated) priors on posterior decisions. 

Remark 2 (Unbounded likelihoods). Our setting excludes Bayesian inverse problems with unbounded likelihood functions e[−][Φ] : E → (0, ∞). Such likelihoods can appear in the additive noise model described above if the probability density function of the noise distribution νε is not bounded—for instance, if one component of ε follows a chi-squared distribution with degree of freedom one or a beta distribution with both shape parameters equal to one half. Moreover, also the setting of infinite-dimensional data is excluded: Consider an observable Y := G(X) + ε where G : E →H is a measurable mapping into an infinite-dimensional separable Hilbert space H and ε ∼ N (0, Q) is a mean-zero Gaussian random variable in H with covariance operator Q : H →H. If the range of G is a subset of the range of Q, i.e., rg G ⊂ rg Q, then the resulting posterior for X ∼ µ given a realization Y = y, y ∈H, can be shown to be of the form (1), cf. [1, Section 3.3]. In this case Φ is given by 

**==> picture [259 x 23] intentionally omitted <==**

4 

where ⟨·, ·⟩H denotes the inner product in H and where we assume that exp(−Φ) ∈ L[1] µ[(][R][)][ for the moment.] However, if y ∈/ rg Q[1][/][2] , then Φ(x) can, in general, not be bounded from below—since the lower bound is, formally, − 2[1][∥][Q][−][1][/][2][y][∥][H][.] On the other hand, more general noise models than additive noise are covered. For instance, if G : E → R is measurable and we can observe Y := εG(X) with ε ∼ N (0, σ[2] ) being stochastically independent of X ∼ µ, then the resulting posterior given Y = y is again of the form (1) with Φ(x) = 2[1][y][2][/][(][σ][2][G][2][(][x][))][ ≥][0][.] 

Main Results. We are interested in the stability of the posterior measure µΦ ∈P(E) w.r.t. perturbations of the negative log-likelihood function Φ: E → [0, ∞) and the prior measure µ ∈P(E). The former includes for Φ(x) = ℓ(y − G(x)) perturbations of the observed data y ∈ R[n] or the forward map G, e.g., due to numerical approximations of G, cf. Remark 4 below. We then bound the difference between the original posterior µΦ and two kinds of perturbed posteriors: 

1. perturbed posteriors µΦ� ∈P(E) resulting from perturbed log-likelihood functions Φ:[�] E → R, i.e., 

**==> picture [353 x 25] intentionally omitted <==**

2. perturbed posteriors µ�Φ ∈P(E) resulting from perturbed prior measures µ� ∈P(E), i.e., 

**==> picture [353 x 26] intentionally omitted <==**

In particular, we prove the local Lipschitz continuity of µΦ ∈P(E) w.r.t. the log-likelihood Φ ∈ L[p] µ[(][R] +[)] and the prior µ ∈P(E) in several common distances and divergences for probability measures d : P(E) × P(E) → [0, ∞]. Here, L[p] µ[(][R] +[)][denotes][the][set][of][non-negative][functions][which][are][p][-integrable][w.r.t.][the] prior measure µ. For d we consider the total variation distance, the Hellinger distance, the Kullback–Leibler divergence, and the Wasserstein distance. Given suitable assumptions our results are then of the following form: 

1. For a given prior µ ∈P(E) and log-likelihoods Φ, Φ[�] ∈ L[p] µ[(][R] +[)][with][suitable][p][∈][N][, there][exists][a] constant Cµ,Φ < ∞ and a q ∈ N such that 

**==> picture [172 x 29] intentionally omitted <==**

This yields a local Lipschitz continuity as follows: For any Φ ∈ L[p] µ[(][R] +[)][ and][any][radius][r][>][0][ there] exists again a constant Cµ,Φ(r) < ∞ such that 

**==> picture [382 x 17] intentionally omitted <==**

The particular values for Cµ,Φ(r) and p for each of the studied distances and divergences are given in Table 1 where for the Wasserstein distance we require |µ|[2] P[2][:= inf][x][0][∈][E] �E[d] E[2][(][x, x][0][)][ µ][(d][x][)][ <][ ∞][.] 

2. Similarly, for a given measurable Φ: E → [0, ∞) and suitable priors µ, �µ ∈P(E) there exists a constant Cµ,Φ < ∞ and a q ∈ N such that 

**==> picture [200 x 29] intentionally omitted <==**

5 

|d|Total Variation|Hellinger|Kullback–Leibler|1-Wasserstein|
|---|---|---|---|---|
|Cµ,Φ(r)|Z−1|exp(∥Φ∥L1µ +r)|2 exp(∥Φ∥L1µ +r)|2|µ|P2exp(2∥Φ∥L1µ + 2r)|
|p|1|2|1|2|



Table 1: Local Lipschitz constant Cµ,Φ(r) of the mapping L[p] µ[(][R] +[)][ ∋][Φ][ �→][µ] Φ[∈][(][P][(][E][)][, d][)][ in (][4][) w.r.t. vari-] ous distances and divergences d; here r > 0 denotes the radius of the local neighborhood of Φ in L[p] µ[(][R] +[)][.] 

|d|Total Variation|Hellinger|Kullback–Leibler|1-Wasserstein.|
|---|---|---|---|---|
|Cµ,Φ(r)|2/Z|2/(Z −2r)|2/(Z −<br>√<br>2r)|(1 +DLip(e−Φ))2/(Z −Lip(e−Φ)r)|
|Rµ,Φ|+∞|Z/2|Z2/2|Z/Lip(e−Φ)|
|Conditions|—|—|µ,�µequivalent|dE bounded byD,e−Φ Lipschitz|



Table 2: Local Lipschitz constant Cµ,Φ(r) of the mapping µ �→ µΦ in (5) w.r.t. various distances and divergences d and necessary conditions for (5) to hold; here Rµ,Φ denotes the upper limit for the radius r of the local neighborhood of µ w.r.t. d. 

where[d][(][µ,][µ][�][)+] 2[d][(][µ,µ][�][)] = d(µ, �µ) in case of the Kullback–Leibler divergence. Again, this yields a local Lipschitz continuity: For any µ ∈P(E) there exists for each radius 0 < r < Rµ,Φ a constant Cµ,Φ(r) < ∞ such that 

**==> picture [382 x 24] intentionally omitted <==**

The particular values for Cµ,Φ(r) and the radius bound Rµ,Φ as well as corresponding conditions for each of the studied distances and divergences are given in Table 2—here, Lip(e[−][Φ] ) denotes the global Lipschitz constant of e[−][Φ] : E → (0, 1] w.r.t. dE. 

3. In both cases (i) and (ii) the estimated local Lipschitz constant Cµ,Φ(r) grows as the normalization constant Z of µΦ decays or ∥Φ∥L1µ increases, respectively. For the local Lipschitz dependence on the prior we even have that the maximal local neighborhood of µ, for which our Lipschitz bound holds, shrinks as Z → 0. Thus, the sensitivity w.r.t. perturbtations of prior or log-likelihood increases, in general, if the normalization constant Z of µΦ decreases due to, for instance, a higher concentration or localization of the posterior measure. 

Thus, besides positive stability results our bounds suggest an increasing sensitivity of the posterior w.r.t. perturbations of the prior or log-likelihood for increasingly informative Φ, e.g., due to more or more precise observations employed in the Bayesian inference. 

Remark 3. The considered total variation distance dTV, Hellinger distance dH, and Kullback–Leibler divergence dKL are related in the following way: 

**==> picture [396 x 23] intentionally omitted <==**

see [28]. Moreover, on bounded metric spaces (E, dE ) with dE ≤ D, D ∈ R, we have for the 1-Wasserstein distance W1(µ, �µ) ≤ D dTV(µ, �µ), see [28]. However, the established local Lipschitz bounds in Table 1 and 2 are derived by studying each distance individually, since this allowed for sharper estimates. For example, a Lipschitz continuity of Φ �→ µΦ in dKL would only imply a H¨older continuity in dTV or dH by (6). 

6 

Remark 4. The bound d(µΦ, µΦ� ) ≤ Cµ,Φ(r)∥Φ − Φ[�] ∥L[p] µ[can usually][be used][to prove local][Lipschitz][con-] tinuous dependence of the posterior on the data or show stability w.r.t. numerical approximations, say Gh, ofΦ(� xthe) :=forward2[1][|][y][ −][G] map[h][(][x] G[)][|][2] :[and obtain] E → R[n] . For example, for an additive Gaussian noise ε ∼ N (0, Σ) we can set 

**==> picture [325 x 15] intentionally omitted <==**

If G, Gh ∈ L[2] µ[p][(][R][n][)][, then the Cauchy–Schwarz inequality yields] 

**==> picture [313 x 21] intentionally omitted <==**

Analogous expressions can be obtained for the case of perturbed data �y ∈ R[n] , i.e., for Φ([�] x) :=[1] 2[|][y][�][ −][G][(][x][)][|][2][.] 

## 3 Stability in Hellinger and Total Variation Distance 

First, we study the continuity of the posterior measure µΦ ∈P(E) w.r.t. the log-likelihood function Φ: E → [0, ∞) and the prior measure µ ∈P(E) in the Hellinger distance 

**==> picture [303 x 36] intentionally omitted <==**

� Here, ν denotes an arbitrary measure on E dominating µ and µ, e.g., ν = 2[1][µ][ +] 2[1][µ][�][. The Hellinger][distance] is topologically equivalent to the total variation distance 

**==> picture [299 x 27] intentionally omitted <==**

see (6), but it yields also continuity of the moments of square-integrable functions, see [1, Theorem 21]. We investigate now the stability of the posterior µΦ w.r.t. Φ in Hellinger distance. The related issue of stability w.r.t. the data y and numerical approximations Φh of Φ, cf. Remark 4, was already established for Bayesian inverse problems with additive Gaussian noise and a Gaussian prior µ by Stuart [6] and recently extended by Dashti and Stuart [1] and Latz [5] to a more general setting. Moreover, in [29, Section 4] we already find a similar result under slightly different assumptions. Nonetheless, we state the theorem and proof for completeness. 

Theorem 5. Let µ ∈P(E) and Φ, Φ:[�] E → R belong to L[2] µ[(][R][)][ with][ ess inf][µ][Φ =][0][. Then, we have for the] two probability measures µΦ, µΦ� ∈P(E) given by (1) and (2), respectively, 

**==> picture [346 x 31] intentionally omitted <==**

where [t]− := min(0, t) for t ∈ R. 

Proof. Analogously to the proof of [6, Theorem 4.6] or [29, Theorem 4.2] we start with 

**==> picture [435 x 75] intentionally omitted <==**

7 

where 

**==> picture [425 x 36] intentionally omitted <==**

Since | e[−][t] − e[−][s] | = e[−][min(][t,s][)] |1 − e[−|][t][−][s][|] | ≤ e[−][min(][t,s][)] |t − s| for any t, s ∈ R, we obtain 

**==> picture [404 x 37] intentionally omitted <==**

and since |t[1][/][2] − s[1][/][2] | ≤ 2[1][min(][t, s][)][−][1][/][2][ |][t][ −][s][|][ for][ t, s >][ 0][ we have] 

**==> picture [137 x 28] intentionally omitted <==**

Now, as for I1 we obtain 

**==> picture [326 x 85] intentionally omitted <==**

and due to Z ≤ 1 we have 

which concludes the proof. 

For the term min(Z, Z[�] ) appearing in the estimate (11) we provide the following lower bound. Proposition 6. Let µ ∈P(E) and Φ, Φ:[�] E → R belong to L[1] µ[(][R][)][.][Considering][the][probability][measures] µΦ, µΦ� ∈P(E) given by (1) and (2) we have 

**==> picture [338 x 20] intentionally omitted <==**

Proof. By Jensen’s inequality and the convexity of t �→ exp(−t) we have 

**==> picture [341 x 27] intentionally omitted <==**

Analogously, Z[�] ≥ exp �−∥Φ[�] ∥L1µ�. The statment follows by the triangle inequality. 

Combining Proposition 6 and Theorem 5 we obtain for a given prior µ ∈P(E) the local Lipschitz continuity of the mapping L[2] µ[(][R][+][)][ ∋][Φ][ �→][µ][Φ][∈P][(][E][)][ w.r.t. the Hellinger distance. In particular, for a given] Φ ∈ L[2] µ[(][R][+][)][ and any][ r][>][ 0][ there exists a constant][ C][Φ][,µ][(][r][) := exp(][∥][Φ][∥] L[1] µ[+][ r][)][ <][ ∞][such that] 

**==> picture [323 x 17] intentionally omitted <==**

All results in the remainder of the paper will be of the form as in Theorem 5: We bound the distance of the posteriors by a constant times the distance of the log-likelihoods or priors where the constant depends on min(Z, Z[�] ) which can be bounded uniformly for all sufficiently small perturbations. For stability w.r.t. different priors we get the following result. 

8 

Theorem 7. Let µ, �µ ∈P(E) and Φ: E → [0, ∞) be measurable. Then, for µΦ, �µΦ ∈P(E) as in (1) and (3), respectively, we have 

**==> picture [283 x 28] intentionally omitted <==**

Proof. Let ρ(x) :=[d] d[µ] ν[(][x][)][ and][ρ][�][(][x][) :=][d] d[µ] ν[�][(][x][)][ denote the densities of][ µ][ and][µ][�][ w.r.t. a dominating][ ν][∈P][(][E][)][.] Then, we have 

**==> picture [415 x 198] intentionally omitted <==**

where Z = �E[e][−][Φ(][x][)][ρ][(][x][)][ ν][(d][x][)][ and][Z][�][=] �E[e][−][Φ(][x][)][ρ][�][(][x][)][ ν][(d][x][)][. We obtain analogously][to Theorem][ 5] 

where 

Due to Φ(x) ≥ 0 we get 

**==> picture [243 x 25] intentionally omitted <==**

Moreover, as in the proof of Theorem 5, we have I2 ≤ 1 2Z min(Z,Z[�] )[|][Z][ −][Z][�][|][2][ and due to (][6][)] 

**==> picture [315 x 26] intentionally omitted <==**

Hence, since Z ≤ 1 we obtain 

**==> picture [329 x 33] intentionally omitted <==**

Concerning the local Lipschitz continuity of the mapping P(E) ∋ µ �→ µΦ ∈P(E), Φ: E → [0, ∞), w.r.t. the Hellinger distance, we obtain the following due to Theorem 7: Given a µ ∈P(E) and a radius 0 ≤ r < 2[1][Z][=] 2[1] �E[e][−][Φ][d][µ][ there exists a constant][ C][Φ][,µ][(][r][) :=] Z−22r[such that] 

**==> picture [287 x 12] intentionally omitted <==**

due to min(Z, Z[�] ) ≥ Z −|Z − Z[�] | ≥ Z − 2dH(µ, �µ). Hence, in comparison to the local Lipschitz continuity of Φ �→ µΦ discussed above the radius of the local neighborhood of µ also depends on µ. 

For stability in total variation distance we could simply use the relation (6) between dTV and dH combined with Theorem 5 and Theorem 7. However, sharper bounds are obtained by adopting the proofs of Theorem 5 and Theorem 7, accordingly. 

9 

Theorem 8. Let µ ∈P(E) and Φ, Φ[�] ∈ L[1] µ[(][R][)][ with][ ess inf][µ][Φ = 0][. Then, we have for][ µ][Φ][, µ] Φ�[∈P][(][E][)][ as in] (1) and (2), respectively, 

**==> picture [223 x 27] intentionally omitted <==**

Moreover, for µ, �µ ∈P(E) and measurable Φ: E → [0, ∞) we have for µΦ, �µΦ ∈P(E) as in (1) and (3), respectively, 

**==> picture [135 x 23] intentionally omitted <==**

Remark 9 (Increasing sensitivity). The bounds established in Theorem 5, 7, and 8 involve the inverse of the normalization constant Z of µΦ. This suggests that Bayesian inference becomes increasingly sensitive to pertubations of the log-likelihood or prior as the posterior µΦ concentrates due to more or more accurate data. This may seem counterintuitive given the well-known Bernstein–von Mises theorem [10, 30] in asymptotic Bayesian statistics: Under suitable conditions the posterior measure concentrates around the true, data-generating x[†] ∈ E in the large data limit. This statement holds independently of the particular prior µ as long as x[†] belongs to the support of the measure µ ∈P(E), i.e., as long as x[†] ∈ supp µ. However, the latter resolves the alleged contradiction: Given a suitable infinite space E and a non-atomic prior µ ∈P(E)—i.e., for each x ∈ E we have for balls Br(x) := {y ∈ E : dE(x, y) ≤ r} that limr→0 µ(Br(x)) = 0[1] —we can � � construct for any ǫ > 0 a perturbed prior µ with dTV(µ, �µ) ≤ ǫ but µ(Br(x[†] )) = 0 for a sufficiently small � radius r = r(ǫ) > 0. Thus, µΦ concentrates around x[†] and µΦ around another x[⋆] ∈ supp �µ, see [30], and their total variation distance will tend to 1 since dE(x[†] , x[⋆] ) ≥ r > 0. Similar arguments also apply to perturbations of the likelihood function, since x[†] is typically the minimizer of the log-likelihood Φ on supp µ, and, therefore, we can construct perturbed Φ[�] with a different minimizer x[⋆] = x[†] but with arbitrarily small L[1] µ[-distance][∥][Φ][ −][Φ][�][∥] L[1] µ[. Thus, it is indeed][the case that Bayesian][inference][becomes][more sensitive][to per-] turbations of the log-likelihood or the prior as the amount of data or its accuracy increases. This also holds for other divergences and distances, cf. Remark 18. 

� Remark 10 (Stability w.r.t. Gaussian priors). Concerning Gaussian priors µ = N (m, C) and µ = N (m, � C[�] ) on a separable Hilbert space H with norm ∥·∥H we can bound the Hellinger distance of the resulting posteriors by Theorem 7. In order to obtain a non-trivial bound, we require that µ and µ� are absolutely continuous � w.r.t. each other, i.e., that m − m ∈ rg C[1][/][2] = rg C[�][1][/][2] and C[−][1][/][2][ �] CC[−][1][/][2] − I is a Hilbert–Schmidt operator on H, see, e.g., [21, Corollary 6.4.11] or [22, Section II.3]. Assuming furthermore that T := C[−][1][/][2][ �] CC[−][1][/][2] is a positive definite operator on H, we can then use the exact expressions for the Hellinger distance of equivalent Gaussian measures: 

**==> picture [308 x 60] intentionally omitted <==**

We provide a detailed derivation of these formulas in Appendix B and only make the following remarks here: (a) the inverse T[−][1] exists and is bounded on H, since T is positive definite and T − I is Hilbert–Schmidt, i.e., the smallest eigenvalue of T is bounded away from zero; (b) the determinant det 21 √T + 2[1] √T[−][1] is � � well-defined as a Fredholm determinant, since I − ([1] 2 √T +[1] 2 √T[−][1] ) is trace-class, see Appendix B; and (c) 1 √t 1 we have det � 2 √T +[1] 2 √T[−][1] � ≥ 1 due to 2[+] 2√t[≥][1][ for][ t >][ 0][. If, moreover,][ C][−][1][/][2][ �][CC][−][1][/][2][ −][I][is trace] class we can bound 

**==> picture [247 x 23] intentionally omitted <==**

> 1Similar requirements were essential for the brittleness results in [16, 17]. 

10 

where ∥A∥HS := �tr (A[∗] A) denotes the Hilbert–Schmidt norm of a Hilbert–Schmidt operator A : H →H. This bound is derived by Pinsker’s inequality and means of [31]. Thus, using Theorem 8 we can bound the total variation distance of posteriors resulting from Gaussian priors with different mean or covariance. However, we remark that Gaussian priors on function spaces are often singular w.r.t. each other. For example, Gaussian priors with Mat´ern covariance operator C = Cα,β,γ = β(I + γ[2] ∆)[−][α] [26, 27] are singular for different values of α > 0 or β > 0. We refer to [27] for a further discussion and for a particular subclass of equivalent Gaussian priors with Mat´ern covariance. 

## 4 Stability in Kullback–Leibler Divergence 

A common way to compare the relative information between two probability measures µ, �µ ∈P(E) is to compute the Kullback–Leibler divergence (KLD) between them, which in case of existence of[d] d[µ] µ�[is] 

**==> picture [173 x 27] intentionally omitted <==**

If µ is not absolutely continuous w.r.t. µ�, then dKL(µ∥µ�) := +∞. The KLD is not a metric for probability measures due to the lack of symmetry and triangle inequality[2] but nonetheless an important quantity in information theory and optimal experimental design. Moreover, the total variation and Hellinger distance can be bounded by the KLD, see (6). In particular, the well-known Pinkser’s inequality states that 2d[2] TV[(][µ,][ �][µ][)][ ≤] dKL(µ∥µ�), see [28]. 

In the following, we study the stability of µΦ in terms of the KLD w.r.t. perturbations of the log-likelihood and the prior. Previous results in this direction were obtained by [5, 20] stating a continuous dependence of µΦ on the data y ∈ R[n] [5] and a stability of µΦ w.r.t. numerical approximations of the forward map G : E → R[n] [20] under suitable assumptions. 

Theorem 11. Let µ ∈P(E) and Φ, Φ:[�] E → R belong to L[1] µ[(][R][)][with][ess inf][µ][Φ][=][0][.][Then,][for][the][two] probability measures µΦ, µΦ� ∈P(E) given in (1) and (2), respectively, 

**==> picture [353 x 31] intentionally omitted <==**

Proof. We have d[d] µ[µ] Φ[Φ] �[(][x][) =][d] d[µ] µ[Φ][(][x][)] ddµµΦ�[(][x][) =][Z] Z[�][e][Φ(][�][x][)][−][Φ(][x][)][and, thus,] 

**==> picture [315 x 28] intentionally omitted <==**

We further obtain 

**==> picture [346 x 31] intentionally omitted <==**

1 as well as due to | log t − log s| ≤ min(t,s)[|][t][ −][s][|][ for][ t, s >][ 0][ and][ |][ e][−][t][ −][e][−][s][ | ≤][e][−][min(][t,s][)][ |][t][ −][s][|][ for][ t, s][ ∈][R] that 

**==> picture [347 x 31] intentionally omitted <==**

> 2There exists a metric for probability measures based on the KLD called the Jensen–Shannon distance [32]. 

11 

cf. the proof of Theorem 5 for |Z − Z[�] | ≤ e[−][[ess][inf][µ][Φ]][�][−] ∥Φ − Φ[�] ∥L1µ, Hence, we end up with 

**==> picture [457 x 34] intentionally omitted <==**

An analogous proof to Theorem 11 also yields 

**==> picture [353 x 32] intentionally omitted <==**

Concerning the following stability statement w.r.t. perturbed priors µ� ∈P(E) we restrict ourselves to µ� which are equivalent to µ. Note that this assumption is sensible, since otherwise dKL(µ∥µ�) or dKL(µΦ∥µ�Φ) 

Theorem 12. Let µ, �µ ∈P(E) be equivalent and Φ: E → [0, ∞) be measurable. Then, for µΦ, �µΦ ∈P(E) given in (1) and (3), respectively, we have 

**==> picture [383 x 27] intentionally omitted <==**

Proof. Let ρ(x) := d[d] µ[µ] �[(][x][)][, then we have] d[d] µ[µ] �Φ[Φ][(][x][) =] Z[Z][�][ρ][(][x][)][ and obtain] 

**==> picture [361 x 87] intentionally omitted <==**

Concerning the second term we first note that 

**==> picture [327 x 26] intentionally omitted <==**

and then apply Jensen’s inequality for the convex function t �→− log(t), t > 0, to obtain 

**==> picture [463 x 28] intentionally omitted <==**

where we used that[d][µ][�] 1 dµ[(][x][) =] ρ(x)[. Hence, we end up with] 

**==> picture [199 x 26] intentionally omitted <==**

which yields the first statement. The second statement is a direct implication of Pinsker’s inequality and |Z − Z[�] | ≤ 2dTV(µ, �µ). 

Again, Theorem 12 also implies a bound for the alternative KLD 

**==> picture [360 x 28] intentionally omitted <==**

12 

� Remark 13 (Kullback–Leibler divergence of Gaussian priors). For Gaussian measures µ = N (m, C), µ = N (m, � C[�] ) on separable Hilbert spaces H there exists an exact formula for their KLD [33]: Given µ and µ� are equivalent, and C[−][1][/][2][ �] CC[−][1][/][2] − I is trace-class on H we have 

**==> picture [337 x 23] intentionally omitted <==**

Again, this can be used combined with Theorem 12 to bound the KLD of posterior measures resulting from (equivalent) Gaussian priors in terms of the pertubations in mean and covariance. 

## 5 Stability in Wasserstein Distance 

In this section we focus on measuring perturbations of posterior and prior distributions in the Wasserstein distance. The main advantage of this metric is that it does not rely on the absolute continuity of distributions. � Therefore, also for singular measures such as Dirac measures δx, δx� ∈P(E) at x = x in E the Wasserstein distance yields a sensible value which decays to 0 as dE(x, �x) → 0. Besides that, the Wasserstein distance is based on the metric of the underlying space E which allows some flexibility in the application by employing a suitable metric. We introduce the following spaces of probability measures on a complete and separable metric space (E, dE ) given a q ≥ 1: 

**==> picture [377 x 30] intentionally omitted <==**

For measures µ, �µ ∈P[q] (E) we can now define the q-Wasserstein distance by 

**==> picture [241 x 30] intentionally omitted <==**

� where Π(µ, �µ) denotes the set of all couplings π ∈P(E × E) of µ and µ, i.e., π(A × E) = µ(A) and � π(E × A) = µ(A) for each A ∈E. We note that (P[q] , Wp) is again a complete and separable metric space, see, e.g., [34]. 

We focus on the 1-Wasserstein distance W1 subsequently. The advantage of this particular distance is its dual representation also known as Kantorovich–Rubinstein duality [34]: 

**==> picture [289 x 29] intentionally omitted <==**

|f (x)−f (y)| where Lip(f ) := supx=y∈E dE (x,y) denotes the global Lipschitz constant of f w.r.t. the metric dE on E. Our first result considers stability in Wasserstein distance w.r.t. perturbations of the log-likelihood function. 

Theorem 14. Let µ ∈P[2] (E) and assume Φ, Φ:[�] E → R belong to L[2] µ[(][R][)][ with][ess inf][µ][Φ][=][0][. Then,][for] the two probability measures µΦ, µΦ� ∈P(E) given in (1) and (2), respectively, we have 

**==> picture [415 x 29] intentionally omitted <==**

Proof. Let x0 ∈ E be arbitrary. We start with the dual representation 

**==> picture [280 x 29] intentionally omitted <==**

13 

where we can take the supremum also w.l.o.g. w.r.t. all Lipschitz continuous functions f : E → R with Lip(f ) = supx=y∈E |f (dxE)(−x,yf ()y)| ≤ 1 and f (x0) = 0. The latter two conditions imply |f (x)| ≤ dE(x, x0). Furthermore, we have that 

**==> picture [441 x 92] intentionally omitted <==**

where 

We can bound I2 as follows using | e[−][t] − e[−][s] | ≤ e[−][min(][t,s][)] |t − s| for t, s ∈ R and the Cauchy–Schwarz inequality: 

**==> picture [397 x 65] intentionally omitted <==**

Moreover, due to | Z[1][−] Z[1] �[|][ =][|][ �][Z] Z[−] Z[�][Z][|] and |Z − Z[�] | ≤ e[−][[ess][inf][µ][Φ]][�][−] ∥Φ − Φ[�] ∥L1µ, see Theorem 5, we have 

**==> picture [429 x 64] intentionally omitted <==**

Since x0 ∈ E was chosen arbitrarily we obtain the statement. 

If one prefers an estimate without |µΦ|P 1, then we can bound W1(µΦ, µΦ� ) also by 

**==> picture [374 x 67] intentionally omitted <==**

where we used |µΦ|P 1 ≤ Z1[|][µ][|][P][1][in][the][first][line][and][in][the][second][line][|][µ][|][P][1][≤|][µ][|][P][2][and][∥][Φ][ −][Φ][�][∥][L][1] µ[≤] ∥Φ − Φ[�] ∥L2µ due to Jensen’s inequality as well as min(Z, Z[�] ) ≤ Z ≤ 1. 

As outlined in Remark 4, we can use Theorem 14 to show a (local Lipschitz) continuous dependence of the posterior measure w.r.t. the observed data y ∈ R[n] in Wasserstein distance. This is done in detail at the end of this section under similar conditions as for Hellinger well-posedness, cf. [1, 5]. 

Studying the stability w.r.t. the prior in Wasserstein distance is unfortunately more delicate than in the previous sections and the following result requires some restrictive assumptions which we discuss afterwards. 

Theorem 15. Let E be bounded w.r.t. the metric dE, i.e., 

**==> picture [117 x 21] intentionally omitted <==**

14 

and let e[−][Φ] : E → [0, 1] be Lipschitz w.r.t. dE, i.e., Lip(e[−][Φ] ) < ∞. Then, for the two probability measures µΦ, �µΦ ∈P(E) given in (1) and (3), respectively, we have 

**==> picture [297 x 28] intentionally omitted <==**

and 

**==> picture [141 x 14] intentionally omitted <==**

Proof. Again, let x0 ∈ E be arbitrary. By the duality of W1 we have 

**==> picture [319 x 29] intentionally omitted <==**

For any f : E → R with Lip(f ) ≤ 1 and f (x0) = 0 we get that g(x) := f (x) e[−][Φ(][x][)] satisfies g(x0) = 0 as well as 

**==> picture [315 x 48] intentionally omitted <==**

since |f (x)| ≤|f (x0)| + |f (x) − f (x0)| ≤ dE(x, x0) ≤ D. Hence, we obtain 

**==> picture [361 x 29] intentionally omitted <==**

and by the triangle inequality 

**==> picture [459 x 62] intentionally omitted <==**

Since x0 ∈ E was chosen arbitrarily and 

**==> picture [283 x 28] intentionally omitted <==**

we obtain the statement. 

A slightly worse but maybe more convenient bound than the one given in Theorem 15 is 

**==> picture [205 x 32] intentionally omitted <==**

which is derived by using Z ≤ 1 and |µ|P 1 ≤ D due to the boundedness of E. 

The assumption on the boundedness of dE on E is not that restrictive, since we can always consider a bounded version d[�] E(x, y) := min(D, dE (x, y)), D > 0, of a metric dE on E and, thereby, obtain a bounded metric space (E, d[�] E ). However, a crucial restriction in Theorem 15 is the Lipschitz condition Lip(e[−][Φ] ) < ∞ w.r.t. a bounded metric on E. For example, for Euclidean spaces E = R[n] equipped with the bounded 

15 

metric dE(x, y) := min(D, |x − y|), D > 0, and a sufficiently smooth Φ ∈ C[1] (R[n] ; [0, ∞)) the condition Lip(e[−][Φ] ) < ∞ would require that 

**==> picture [179 x 27] intentionally omitted <==**

where ∇ denotes the gradient w.r.t. the usual Euclidean norm | · | on E = R[n] . This condition fails to hold, for instance, for functions Φ: R[n] → [0, ∞) which are bounded but have growing derivatives such as Φ(x) = 1 + sin(exp(x)), x ∈ R. 

However, we present the following result stating the continuous dependence of the posterior on the prior in Wasserstein distance. Here, we consider the general q-Wasserstein distance, since the proof does not rely on the particular Kantorovich–Rubinstein duality of the 1-Wasserstein distance. 

Lemma 16. Let q > 0 and consider a µ ∈P[q] (E) and a sequence of �µ[(][k][)] ∈P[q] (E), k ∈ N, with corresponding µΦ as in (1) and 

**==> picture [277 x 30] intentionally omitted <==**

given a measurable Φ: E → [0, ∞). If Φ is continous, then 

**==> picture [219 x 16] intentionally omitted <==**

Proof. We exploit the equivalence of convergence in q-Wasserstein distance and weak convergence, see [34]: For ν, ν[(][k][)] ∈P[q] (E), k ∈ N, the statement limk→∞ Wq(ν, ν[(][k][)] ) → 0 is equivalent to 

**==> picture [307 x 26] intentionally omitted <==**

where x0 ∈ E is arbitrary and ⇀ denotes weak convergence of measures, i.e., ν[(][k][)] ⇀ν means � f (x) ν[(][k][)] (dx) → � f (x) ν(dx) for any bounded, continuous f : E → R. Since Wq(µ, �µ[(][k][)] ) → 0, we know that for any such f we have 

**==> picture [402 x 114] intentionally omitted <==**

which implies that 

since e[−][Φ] is continuous and bounded by assumption. Thus, we have µ�[(] Φ[k][)][⇀µ][Φ][. Moreover, we use that] 

is equivalent to 

**==> picture [225 x 73] intentionally omitted <==**

16 

for any continuous f : E → R with |f (x)| ≤ C(1 + d(x, x0)[q] ), C ∈ R, see [34, Definition 6.8]. Since e[−][Φ] is continuous and bounded by one, we therefore obtain 

**==> picture [294 x 81] intentionally omitted <==**

which yields by the same arguments as above that 

Hence, the statement is proven. 

We close the discussion on Wasserstein stability with a few remarks on the results we have obtained. 

Remark 17 (Wasserstein distance of Gaussian priors). The 2-Wasserstein distance of Gaussian measures µ = N (m, C), �µ = N (m, � C[�] ) on a separable Hilbert space H is given by 

**==> picture [311 x 27] intentionally omitted <==**

see [35, Theorem 3.5]. This provides a bound for the 1-Wasserstein distance of Gaussian priors, since W1(µ, �µ) ≤ W2(µ, �µ) due to Jensen’s inequality. Besides that we have for µ = N (m, C) that µ ∈P[2] (H) with |µ|P 2 = �tr (C). We highlight, that W1(µ, �µ) or W2(µ, �µ) does not depend on the equivalence of Gaussian priors µ, �µ. 

Remark 18 (Increasing sensitivity). The bounds established in Theorem 14 and 15 suggest also for the Wasserstein distance an increasing sensitivity of the posterior to perturbations of the log-likelihood or prior as the posterior becomes increasingly concentrated. In Remark 9 we have outlined why such an increasing sensitivity is quite natural in the topology induced by the total variation or Hellinger distance. The same reasoning applies when pertubations are measured by the Kullback–Leibler divergence, since the KLD also relies on the equivalence of (perturbed posterior and prior) measures. We now argue that this increasing sensitivity is also natural for the Wasserstein distance. To this end, we consider a sequence of increasingly concentrated posterior measures µ[(] Φ[k][)][(d][x][)][:=][Z] k[−][1] e[−][k][Φ(][x][)] µ(dx) for k ∈ N with Zk := �E[e][−][k][Φ(][x][)][µ][(d][x][)][.][Let] S := supp(µ) and assume that x⋆ := argminx∈S Φ(x) exists and is unique. Then, under mild assumptions, µΦ[(][k][)] converges weakly to δx⋆, see [36]. Given a perturbed prior µ� we set µ�[(] Φ[k][)][(d][x][)][:=][Z][�] k[−][1] e[−][k][Φ(][x][)] µ�(dx) with Z[�] k := �E[e][−][k][Φ(][x][)][µ][�][(d][x][)][.][If][x][�][⋆][:=][argmin] x∈S[�][Φ(][x][)][exists][and][is][unique,][where][S][�][:=][supp(][µ][�][)][,][then] µ�Φ[(][k][)][converges][weakly to][ δ][x][�] ⋆[under][mild assumptions][[][36][]. Thus, in order][to have non-exploding][local Lip-] schitz constants w.r.t. the Wasserstein distance of the mappings µ �→ µ[(] Φ[k][)] as k →∞, we require that there exists a radius r > 0 and a constant C < ∞ such that 

**==> picture [267 x 30] intentionally omitted <==**

In the following, we assume that the metric dE of the complete and separable space (E, dE ) is bounded. This yields, given the weak convergence of µ[(] Φ[k][)][to][ δ][x][⋆][and of][µ][�][(] Φ[k][)][to][ δ][x][�] ⋆[, that] 

**==> picture [235 x 30] intentionally omitted <==**

see [34]. Next, we construct a sequence of perturbed priors µ�[(][ǫ][)] ∈P[1] (E) with W1(µ, �µ[(][ǫ][)] ) < ǫ, ǫ > 0, for which the ratio dE(x⋆, �x[(] ⋆[ǫ][)][)][/][W] 1[(][µ,][ �][µ][(][ǫ][)][)][deteriorates][to][infinity][as][ǫ][→][0][.][To][this][end,][we][consider][a] 

17 

ball of radius ǫ > 0 around x⋆, i.e., Bǫ(x⋆) := {x ∈ E : dE(x, x⋆) ≤ ǫ}, and set for an arbitrarily chosen xǫ ∈ ∂Bǫ(x⋆) 

**==> picture [307 x 14] intentionally omitted <==**

i.e., outside the ball Bǫ(x⋆) the measure µ�[(][ǫ][)] coincides with µ but all the probability mass µ(Bǫ(x⋆)) inside the ball Bǫ(x⋆) is now concentrated at the single point xǫ. Assuming that Φ is continuous and ǫ sufficiently small we have x�[(] ⋆[ǫ][)] := argminx∈supp �µ(ǫ) Φ(x) ∈ ∂Bǫ(x⋆). Thus, dE(x⋆, �x[(] ⋆[ǫ][)][) =][ ǫ][. On the other hand,] 

**==> picture [249 x 28] intentionally omitted <==**

Hence, for suitable non-finite spaces E and non-atomic priors µ such that limǫ→0 µ(Bǫ(x)) = 0 for any x ∈ E we have 

**==> picture [191 x 31] intentionally omitted <==**

This shows that also in the Wasserstein topology, the posterior depends increasingly sensitively on perturbations of the prior as the likelihood becomes more informative. A similar reasoning can be employed to show also the increasing sensitivity w.r.t. perturbations of the log-likelihood measured in L[p] µ[-norms.] 

Wasserstein Well-posedness. In the following we show how the stability result in Theorem 14 can be used to establish well-posedness of Bayesian inverse problems (BIP) in Wasserstein distance. The well-posedness of BIP w.r.t. Hellinger distance, including a local Lipschitz-continuous dependence on the data, has been studied in a number of works [1, 3, 4, 5, 6, 7]. Recently, well-posedness has been extended to the Kullback– Leibler divergence and Wasserstein distance in [5], but stating only a continuous dependence on the data. We prove a local Lipschitz dependence on the observed data in Wasserstein distance based on Theorem 14. 

We briefly recall the Bayesian setting from Section 2: Given a prior µ ∈P(E) for the unknown and an observed realization y ∈ R[n] of Y := G(X) + ε, X ∼ µ and ε ∼ νε, the resulting posterior µΦ is of the form (1) with Φ(x) := ℓ(y − G(x)). Here, ℓ denotes the negative log-density of the νε(dǫ) ∝ exp(−ℓ(ǫ))dǫ. We now show a local Lipschitz continuous dependence of the posterior µΦ on the data y ∈ R[n] in Wasserstein distance—given the same basic assumption on Φ or ℓ, respectively, required in [1, 6] and slightly modified in [3, 4, 7] for the Hellinger distance. 

Corollary 19. Let µΦ ∈P(E) be given as in (1) with Φ(x) = ℓ(y − G(x)) and assume that G : E → R[n] and ℓ : R[n] → [0, ∞) are measurable. Furthermore, we assume there exists a monotonic and non-decreasing function M : [0, ∞) × R → [0, ∞) such that for any y, �y ∈ R[n] with |y|, |y�| ≤ r < ∞, r > 0, we have 

**==> picture [285 x 12] intentionally omitted <==**

ras well as> 0 a constant M (r, ∥· ∥ Cr )< ∈ ∞L[2] µsuch that for each[(][R][)][. If there exists a bounded set] |y|, |y�| ≤ r we have[ A][ ⊂][E][ with][ µ][(][A][)][ >][ 0][, then there exists for any] 

**==> picture [115 x 14] intentionally omitted <==**

� where µΦ� is as in (2) with Φ([�] x) = ℓ(y − G(x)). 

Proof. By construction, we have ess infµ Φ[�] ≥ 0 and obtain by means of Theorem 14 

**==> picture [353 x 29] intentionally omitted <==**

18 

where the last inequality followed by our assumption. It remains to bound min(Z, Z[�] ) uniformly (w.r.t. |y|, |y�|) from below. By using the assumption again we obtain 

� max (ℓ(y − G(x)), ℓ(y − G(x))) ≤ ℓ(0 − G(x)) + rM (r, ∥x∥). 

For the bounded set A we define RA := supx∈A M (r, ∥x∥) < ∞ which then yields 

**==> picture [285 x 83] intentionally omitted <==**

due to µ(A) > 0. This concludes the proof. 

By similar arguments and appropriate assumptions, cf. [1, Section 4.2], local Lipschitz continuity in Wasserstein distance for converging approximation Gh of G, i.e., limh→0 Gh(x) = G(x) for all x ∈ E, can be shown. 

## 6 Discussion of Related Literature 

Besides the rather recent well-posedness studies of Bayesian inverse problems, the idea of a robust Bayesian analysis and the question about the sensitivity of the posterior w.r.t. the prior measure (or the likelihood function) have a long history in Bayesian statistics. Some of the early references are [37, 38, 39] and convenient overviews of many existing approaches and (positive) results are given in [40, 8, 9]. 

A common approach in robust Bayesian analysis is to consider a class of possible and sensible priors Γ ⊂P(E), or likelihood functions, and to study and bound the range of a functional of interest f : P(E) → R over the set of resulting posterior measures, i.e., to estimate inf µ∈Γ f (µΦ) and supµ∈Γ f (µΦ). These bounds can then be used for robust decision making accounting for a variation of the prior, or likelihood. Typical functionals of interest are, for instance, probabilities of certain events, e.g., f (µ) = µ(A), A ∈E, the (Fr´echet) mean of µ or the covariance of µ if E is a linear space. There exist several common types of classes of priors with corresponding bounds on the range of various functionals f . We refer to the literature above and focus only on a particular, appealing type of class—the ǫ-contamination class—later on. 

Moreover, in the described setting of robust Bayesian analysis also a notion of non-robustness or instability of Bayesian inference has been established, called the dilation phenomenon [41]. This occurs if 

**==> picture [217 x 20] intentionally omitted <==**

with one of the outer inequalities being strict. Thus, dilation means that the posterior range of f is larger than the prior range of f over the class Γ. Recently, an extreme kind of dilation, called Bayesian brittleness, was established in [15, 16, 17] w.r.t. (a) arbitrarily small perturbations of the likelihood and (b) classes of priors Γk ⊂P(E) specified only by k ∈ N moments or other functionals. 

Another approach to robust Bayesian analysis, starting with [18], considers the Fr´echet and Gˆateaux derivative of the posterior measure µΦ w.r.t. perturbations of the prior measure µ+ρ where ρ denotes a suitable signed measure of mass zero. This leads to a derivative-based sensitivity analysis of Bayesian inference, see, e.g., [42, 43, 19]. Already in these works, particularly [18, 19], the increasing sensitivity of the posterior measure in case of an increasing amount of observational data was noticed. 

In the following we discuss in more detail the relation of our stability results to the classical robust Bayesian analysis for ǫ-contamination classes of prior measures as well as to the derivative-based sensitivity analysis of posterior measures, and, moreover, explain why our results do not contradict Bayesian brittleness. 

19 

Robustness for ǫ-contamination classes. A commonly used class of admissible priors in robust Bayesian analysis are ǫ-contamination classes: Given a reference prior µ ∈P(E) and a set of suitable perturbing probability measures Q ⊂P(E), we consider the class 

**==> picture [257 x 13] intentionally omitted <==**

Common choices for Q are simply Q = P(E), all symmetric and unimodal distributions on E, or all distributions such that (1 − ǫ)µ + ǫν is unimodal if µ is. The choice Q = P(E) is, of course, the most conservative and comes closest to our setting. For brevity we denote Γǫ(µ) := Γǫ,P(E)(µ) in the following. If we consider now balls Bǫ[TV] of radius ǫ > 0 in P(E) w.r.t. total variation distance dTV we have 

**==> picture [227 x 13] intentionally omitted <==**

since dTV ((1 − ǫ)µ + ǫν, µ) ≤ ǫ. However, the ǫ-contamination class Γǫ(µ) is in general a strict subset of the ball Bǫ[TV] (µ), because supp µ ⊆ supp [(1 − ǫ)µ + ǫν] whereas there exist probability measures µ� with dTV(µ, �µ) ≤ ǫ but supp µ ⊈ supp �µ. Thus, our prior stability results are, in general, w.r.t. a larger class of perturbed prior measures than ǫ-contamination classes. 

Furthermore, we establish a local Lipschitz continuous dependence of the posterior measure on the prior w.r.t. particular probability distances such as the total variation distance. This is, in general, a different concept than bounding the posterior range of functionals of interest. Of course, for certain cases we can find relations. For example, concerning probabilities, i.e., functionals fA(µ) := µ(A) where A ∈E, a local Lipschitz continuity in terms of the total variation distance as in Theorem 8 implies also bounds on the posterior range of fA over Γǫ(µ). In particular, we obtain with the results of Section 3 that for all A ∈E 

**==> picture [297 x 28] intentionally omitted <==**

However, in [39] we find explicit expressions for the range of posterior probabilities for an A ∈E over the class Γǫ(µ): 

**==> picture [279 x 61] intentionally omitted <==**

On the other hand, these exact bounds do not allow the derivation of local Lipschitz continuity w.r.t. the total variation distance on Γǫ(µ), because they do not imply a bound for |µ�Φ(A) − µΦ(A)| by a constant times dTV(µ, �µ). Nonetheless, these exact ranges can be used to study lower bounds for the total variation distance of perturbed posteriors: 

**==> picture [413 x 59] intentionally omitted <==**

Bayesian brittleness. In [15, 16, 17] the authors establish several results concerning an extreme instability of Bayesian inference w.r.t. (a) small perturbations of the likelihood function and (b) w.r.t. a class of priors specified only by finitely many “generalized” moments. They call this instability brittleness and state it w.r.t. the posterior range of functionals[3] f : E → R. 

> 3Actually, in [15, 16, 17] the functionals f are functionals of the data distribution, i.e., f : P(Rn) → R. However, in the parametric setting considered here, e.g., the distribution of the data or observable Y given x ∈ E is N (G(x), Σ) for the Gaussian noise model, these functionals can be understood as functionals acting on x ∈ E, i.e., f : E → R. 

20 

Their brittleness result concerning perturbed likelihood models is that for arbitrary small perturbations the resulting range of posterior expectations of f is the same as the (essential) range of f over the support of the prior µ. This result is no contradiction to the local Lipschitz stability shown in this paper. The crucial difference between both results, brittleness and stability, is the way how perturbations of the likelihood are measured: In [16, 17] the likelihood function L is considered as a function of the parameter� x ∈ E and the� data y ∈ R[n] —i.e,. L(x, y) ∝ exp(−Φ(x, y))—and a perturbed likelihood L[�] —i.e., L(x, y) ∝ exp(−Φ(x, y))—is considered close to L if for all x ∈ E the resulting data distribution on R[n] with Lebesgue density L[�] (x, ·) is close to the distribution with Lebesgue density L(x, ·). For instance, employing the total variation distance for the induced data distributions on R[n] we would consider L[�] close to L if dL(L, L[�] ) := supx∈E ∥L(x, ·) − L[�] (x, ·)∥L1 is small—here, the L[1] -norm is taken w.r.t. the Lebesgue measure on R[n] . Thus, closeness of likelihood functions is considered in an average sense w.r.t. the data y but then uniformly w.r.t. x ∈ E. In this paper, on the other hand, we assume fixed data y ∈ R[n] and consider the negative log-likelihoods Φ(·) := − log L(·, y) and Φ([�] ·) := − log L[�] (·, y) close to each other if ∥Φ − Φ[�] ∥L1µ is small. Thus, in our case closeness of log-likelihoods is considered in an average sense w.r.t. the parameter x ∈ E and for the fixed observed data y ∈ R[n] . In Appendix A we discuss in greater detail (i) why brittleness w.r.t. the likelihood is natural if perturbations are measured by the distance dL as above, and (ii) how stability can again be obtained if we employ the alternative distance d[�] L(L, L[�] ) := supy∈Rn ∥L(·, y) − L[�] (·, y)∥L1µ . Note that the latter distance implies bounds on the perturbed marginal likelihood or evidence Z[�] = �E[L][�][(][x, y][)][µ][(d][x][)] whereas the first distance dL does not. This fact yields the difference between stability and brittleness, see Appendix A. 

The second brittleness result in [16, 17] is stated for classes of priors on E defined only by a set of finitely many functionals[4] Ψk : E → R, k = 1, . . . , K. In particular, given a measure ν0 ∈P(R[K] ) we consider the class Γ := {µ ∈P(E): Ψ∗µ = ν0} of priors where Ψ(x) := (Ψ1(x), . . . , ΨK (x)) and Ψ∗µ denotes the pushforward measure. This construction accounts for the fact that in practice only finitely many information are available in order to derive or choose a prior measure. In [16, 17] it is then shown under mild assumptions � that the range of posterior expectations of an f : E → R resulting from priors µ ∈ Γ coincides with the range of f on E. Again, this is not a contradiction to the local Lipschitz stability w.r.t. the prior established in this paper, since the class Γ is, in general, quite different from balls Br(µ) ⊂P(E) with radius r > 0 around a reference prior µ in Hellinger or Wasserstein distance. 

Derivative of the posterior and local sensitivity diagnostics. Besides the rather global pertubation estimates derived in the robust Bayesian analysis for, e.g., contamination classes of prior measures, several authors studied the local sensitivity of the posterior measure w.r.t. the prior. As a first result we mention the derivative of the posterior µΦ w.r.t. the prior µ in the total variation topology introduced by [18] as follows. Let TΦ : P(E) →P(E) denote the map from prior µ to posterior TΦ(µ) := µΦ(dx) = Z[1][exp(][−][Φ(][x][))][ µ][(d][x][)][. In] order to define the derivative of TΦ we consider the set S0(E) of signed measures ρ : E → R on E with zero � mass ρ(E) = 0 for modelling perturbations of probability measures, i.e., perturbed priors µ = µ + ρ. We introduce the set of all admissible perturbations[5] Pµ := {ρ ∈S0(E): µ + ρ ∈P(E)} of a prior µ ∈P(E) and notice that Pµ is star-shaped with center ρ0 = 0. Then the derivative ∂TΦ(µ) of TΦ at a prior µ ∈P(E) is defined as the linear map from Pµ to S0(E) satisfying 

**==> picture [231 x 26] intentionally omitted <==**

> 4Again, in [16, 17] the functionals Ψk are actually functionals of the data distribution associated with x ∈ E, i.e., Ψk : P(Rn) → 

R. 

> 5In [18] the authors allow for any perturbation ρ ∈S0(E) extending the application of TΦ also to signed measures. 

21 

where ∥ρ∥TV := �E ddνρ dν denotes the total variation norm of a (signed) measure ρ with ρ ≪ ν for a ��� ��� σ-finite measure ν. In [18, Theorem 4] it is then shown that 

**==> picture [223 x 33] intentionally omitted <==**

Moreover, [18, Theorem 4] states the following bounds for the norm of the derivative ∥∂TΦ(µ)∥ := sup∥ρ∥TV=1 ∥∂TΦ(µ)ρ∥TV: 

**==> picture [252 x 28] intentionally omitted <==**

i.e., for non-atomic priors µ we have ∥∂TΦ(µ)∥ = Z1[given][our][standing][assumption][inf][x][ Φ(][x][)][=][0][.][This] already implies an increasing sensitivity of the posterior w.r.t. perturbations of the prior for increasingly informative likelihoods, i.e., a decreasing normalization constant Z. 

Based on the Fr´echet derivative ∂TΦ(µ) at µ other authors studied the sensitivies of TΦ w.r.t. a given class of possible perturbations, see, e.g., [42, 43, 19]. For instance, given an ǫ-contamination class Γǫ,Q(µ) as above the authors of [19] study the sensitivity s(µ, Q; Φ) := supν∈Q s(µ, ν; Φ) with local sensitivies 

**==> picture [229 x 27] intentionally omitted <==**

Since (1 − ǫ)µ + ǫν = µ + ǫ(ν − µ) and dTV(µ, (1 − ǫ)µ + ǫν) = ǫ∥ν − µ∥TV, this local sensitivity coincides with the norm of the Gˆateaux derivative of TΦ at µ in the direction ρ = ν − µ ∈S0(E), i.e., s(µ, ν; Φ) = ∥TΦ(µ)(ν − µ)∥TV. In [19] the authors consider furthermore geometric perturbations of the prior such as µ�(dx) ∝ � ddµν �ǫ µ(dx), ǫ > 0, and local sensitivities based on divergences rather than total variation distance, see also [42, 43] employing the Kullback–Leibler divergence. Again, they derive an increasing sensitivity s(µ, Q; Φ) →∞ for various classes Q as the likelihood e[−][Φ] becomes more informative due to more observations in their case. In particular, they derive explicit growth rates of s(µ, Q; ΦN ) w.r.t. N ∈ N where N denotes the number of i.i.d. observations employed for Bayesian inference and ΦN the corresponding log-likelihood. 

These results on Fr´echet or Gˆateaux derivatives w.r.t. the prior measure are quite close to our approach establishing explicit bounds on the local Lipschitz constant. In particular, the constant Cµ,Φ(r) in the corresponding result (5) can be seen as an upper bound on the norm of the derivative ∥∂TΦ(µ�)∥ for all perturbed priors µ� ∈ Br(µ) belonging to the r-ball around µ in P(E)—cf. Theorem 8 stating that dTV(µΦ, �µΦ) ≤ 2[Compared][to][the][studies][in][[][42][,][43][,][19][]][we][allow][for][arbitrary][perturbed][priors][not][restricted] Z[d][TV][(][µ,][ �][µ][)][.] to (geometric) ǫ-contamination classes and, moreover, we consider different topologies on P(E) induced by Hellinger distance, Kullback–Leibler divergence and Wasserstein distance. 

Acknowledgments. The author would like to thank Jonas Latz, Han Cheng Lie and Daniel Rudolf for valuable comments, as well as Claudia Schillings and Tim Sullivan for helpful discussions and for the encouragement to write this note. Moreover, the author acknowledges the financial support by the DFG within the project 389483880. 

## A On Brittleness and Stability w.r.t. Perturbed Likelihoods 

In this appendix we discuss in more detail the phenomenon of Bayesian brittleness for perturbed likelihoods as stated in [16, Theorem 6.4]. Moreover, we reveal the mathematical reason behind the brittleness and show how one can obtain stability by modifying the distance for the likelihood functions. 

22 

Setting. We first recall the setting in [16, 17]. We assume a fixed prior measure µ ∈P(E) and for simplicity only consider the parametric case where the distribution of the observable data on R[n] depends only on x ∈ E. I.e., consider a prior distributed random variable X ∼ µ on E and an observable random variable Y on R[n] such that the conditional distribution of Y given X = x is given by νx ∈P(R[n] ) with νx(dy) = L(x, y)dy for a positive Lebesgue density L(x, ·): R[n] → (0, ∞). Thus, L(x, ·) ∈ L[1] (R[n] ) for all x ∈ E and we suppose that L : E ×R[n] → (0, ∞) is jointly measurable. Moreover, rather than observing a precise realization y ∈ R[n] of Y we suppose that we observe the event Y ∈ Bδ(y) ⊂ R[n] , i.e., we account for a finite resolution of the data described by the radius δ > 0 of the ball Bδ(y) = {y[′] ∈ R[n] : |y − y[′] | ≤ δ}. Conditioning X ∼ µ on the observation Y ∈ Bδ(y) yields a posterior probability measure on E depending on L which we denote by 

**==> picture [367 x 29] intentionally omitted <==**

where ZL := �E[exp(][−][Φ][L][(][x][))][ µ][(d][x][)][.] 

Bayesian brittleness. Let us now consider a perturbed likelihood model, namely, another jointly measurable L[�] : E × R[n] → (0, ∞) such that �R[n][L][�][(][x, y][)][d][y][=][1][for][all][x][∈][E][.][This][model][yields][a][perturbed] posterior measure which we denote by 

**==> picture [367 x 30] intentionally omitted <==**

and ZL� := �E[exp(][−][Φ] L[�][(][x][))][ µ][(d][x][)][. We can then ask for stability][of the mapping][L][�→][µ][L][. To this end, we] measure the distance between the two likelihood models L, L[�] by the following distance: 

**==> picture [265 x 21] intentionally omitted <==**

where �νx ∈P(R[n] ) denotes the probability measure on R[n] induced by L[�] (x, ·). Although, this distance seems natural for comparing parametrized models for data distributions it leads to instability, or brittleness, as stated in [16, Theorem 6.4]: Let f : E → R be a measurable quantity of interest and consider the posterior expectation of f which we simply denote by 

**==> picture [193 x 26] intentionally omitted <==**

then for each ǫ > 0 there exists a δ(ǫ) > 0 such that 

**==> picture [309 x 23] intentionally omitted <==**

with an analogous statement for the infimum. Thus, in other words, the range of all (perturbed) posterior expectations of f resulting from all perturbed likelihood models L[�] within an ǫ-ball around L w.r.t. dL covers the range of all (essential) prior values of f —as long as the observation is sufficiently accurate, i.e., δ < δ(ǫ). 

An explanation for brittleness. We explain the Bayesian brittleness and the mathematical reason behind in terms of the total variation distance of the posterior measures: 

**==> picture [405 x 28] intentionally omitted <==**

23 

Similarly to Theorem 8 we have 

**==> picture [379 x 25] intentionally omitted <==**

Thus, using the definition of ΦL and ΦL�, we can further bound 

**==> picture [425 x 27] intentionally omitted <==**

Hence, for stability we need to control the L[1] -difference of |L(x, ·) − L[�] (x, ·)| over the observed event, the ball Bδ(y). However, the bound dL(L, L[�] ) < ǫ only implies that 

**==> picture [251 x 28] intentionally omitted <==**

where |Bδ(y)| denotes the Lebesgue measure of Bδ(y0) ⊂ R[n] . Thus, for any ǫ we can take a sufficiently small δ and then ǫ/|Bδ(y0)| becomes arbitrarily large. Now, of course, these are just discussions about controlling upper bounds for the total variation distance between the posteriors, but it should be clear that we can easily construct sufficiently “bad” perturbed likelihoods L[�] with dL(L, L[�] ) < ǫ but dTV(µL(· | Bδ(y)), µL�(· | Bδ(y))) ≈ 1, see, for instance, the illustrative example in [17, pp. 574–575]. 

Obtaining stability. The above estimate (13) suggests that stability w.r.t. perturbed likelihoods can only be obtained in a distance for likelihoods L and L[�] which allows to control |L(x, y) − L[�] (x, y)| uniformly w.r.t. y. Thus, if we employ the following alternative distance given the fixed prior µ 

**==> picture [177 x 23] intentionally omitted <==**

then we get by Fubini’s theorem that 

**==> picture [385 x 55] intentionally omitted <==**

i.e., a local Lipschitz stability. We remark that using the distance d[�] L implies that we bound the range of the possible likelihoods for the observed event. As discussed before such a control is crucial for a stability w.r.t. perturbed likelihood models. 

## B Hellinger Distance of Gaussian Measures on Separable Hilbert Spaces 

We provide a proof of the explicit expressions for the Hellinger distance of Gaussian measures on a separable Hilbert space H stated in Remark 10, since this is missing so far in the literature to the best of our knowledge. 

� Different means, same covariance. We start with proving that if m − m ∈ rg C[1][/][2] , then 

**==> picture [295 x 27] intentionally omitted <==**

24 

To this end, we require the well-known Cameron–Martin formula for the density of �µ := N (m, C � ) w.r.t. µ := N (m, C). This density is, given that h := m� − m ∈ rg C[1][/][2] , 

**==> picture [290 x 28] intentionally omitted <==**

where ⟨C[−][1] h, · − m⟩ : H → R is well-defined as a random variable in L[2] µ[(][R][)][, see, e.g., [][44][, Chapter 1]. We] then use that 

**==> picture [371 x 33] intentionally omitted <==**

which can be verified easily, and that for any x[′] ∈H and µ = N (m, C) 

**==> picture [249 x 27] intentionally omitted <==**

� � see [44, Proposition 1.2.7], in order to derive that for µ = N (m, C), µ = N (m, C � ) with h = m − m ∈ rg C[1][/][2] 

**==> picture [359 x 87] intentionally omitted <==**

Same mean, different covariances. We now show that, for rg C[1][/][2] = rg C[�][1][/][2] , T := C[−][1][/][2][ �] CC[−][1][/][2] being positive definite and T − I being Hilbert–Schmidt on H, we have 

**==> picture [293 x 30] intentionally omitted <==**

W.l.o.g. we assume m = 0 in the following and use [22, Theorem 3.3] which states that for µ := N (0, C) and µ� := N (0, C[�] ) and given the assumptions above, we have 

**==> picture [338 x 32] intentionally omitted <==**

where the tk > 0, k ∈ N, denote the eigenvalues of T and the measurable mapping ψ : R[N] →H is specified in the proof of [22, Theorem 3.3]. We do not require the explicit definition of ψ, only the following relation which is also stated in the proof of [22, Theorem 3.3]: With ν :=[�][∞] k=1[N][(0][,][ 1)][we][have][µ][=][ψ][∗][ν][,][i.e,.] µ = N (0, C) is the pushforward of the product measure ν under the mapping ψ, see [22] for details. We use these facts in combination with (14) to obtain that for µ := N (0, C) and µ� := N (0, C[�] ) 

**==> picture [325 x 61] intentionally omitted <==**

25 

A straightforward calculation yields 

**==> picture [431 x 96] intentionally omitted <==**

and, thus, 

where we assumed for the moment that the infinite products converge. Note, that the infinite product on the right-hand side coincides with det 21 √T +[1] 2 √T[−][1] given that this (Fredholm) determinant is finite, i.e., � � given that I − 21 √T +[1] 2 √T[−][1] is a trace-class operator. Thus, if we can show that � � 

**==> picture [239 x 32] intentionally omitted <==**

then the above formula for d[2][C][�][))][ is verified. We define the function][ f][(][t][) :=][1+][t] H[(][N][(][m, C][)][, N][(][m,] 2√t[for][ t >][ 0] and compute its first and second derivative f[′] (t) =[t][1][/][2][−] 4[t] t[−][1][/][2] and f[′′] (t) =[3][t][−][1][/] 8[2] t[2][−][t][1][/][2] , respectively. We notice that f (1) = 1 and f[′] (1) = 0, hence, 

**==> picture [255 x 28] intentionally omitted <==**

Moreover, we have that tk − 1 → 0 as k →∞, since T − I is Hilbert–Schmidt on H. Thus, there exists a k0 ∈ N such that |1 − tk| ≤ 2[1][for][ k][≥][k][0][. We obtain by setting][ c][ := max] t∈[[1] 2[,][ 3] 2[]][ |][f][ ′′][(][t][)][|][ <][ ∞][that] 

**==> picture [179 x 28] intentionally omitted <==**

which yields, since T − I is Hilbert–Schmidt, that 

**==> picture [290 x 35] intentionally omitted <==**

## References 

- [1] M. Dashti and A. M. Stuart. The Bayesian approach to inverse problems. In R. Ghanem, D. Higdon, and H. Owhadi, editors, Handbook of Uncertainty Quantification, pages 311–428. Springer, 2017. 

- [2] J. Kaipio and E. Somersalo. Statistical and Computational Inverse Problems. Springer, New York, 2005. 

- [3] B. Hosseini. Well-posed Bayesian inverse problems with infinitely divisible and heavy-tailed prior measures. SIAM/ASA J. Uncertainty Quantification, 5(1):1024–1060, 2017. 

- [4] B. Hosseini and N. Nigam. Well-posed Bayesian inverse problems: priors with exponential tails. SIAM/ASA J. Uncertainty Quantification, 5(1):436–465, 2017. 

26 

- [5] J. Latz. On the well-posedness of Bayesian inverse problems. arXiv:1902.10257, 2019. 

- [6] A. M. Stuart. Inverse problems: a Bayesian perspective. Acta Numerica, 19:451–559, 2010. 

- [7] T. J. Sullivan. Well-posed Bayesian inverse problems and heavy-tailed stable quasi-Banach space priors. Inverse Probl. Imag., 11(5):857–874, 2017. 

- [8] J. O. Berger. An overview of robust Bayesian analysis. Test, 3(1):5–124, 1994. 

- [9] D. R. Insua and F. Ruggeri, editors. Robust Bayesian Analysis, volume 152 of Lecture Notes in Statistics. Springer, New York, 2000. 

- [10] A. W. van der Vaart. Asymptotic Statistics. Cambridge University Press, Cambridge, UK, 1998. 

- [11] I. Castillo and R. Nickl. Nonparametric Bernstein–von Mises theorems in Gaussian white noise. Ann. Stat., 41(4):1999–2028, 2013. 

- [12] I. Castillo and R. Nickl. On the Bernstein–von Mises phenomenon for nonparametric Bayes procedures. Ann. Stat., 42(5):1941–1969, 2014. 

- [13] D. Freedman. On the Bernstein–von Mises theorem with infinite-dimensional parameters. Ann. Stat,, 27(4):1119–1140, 1999. 

- [14] H Leahu. On the Bernstein-von Mises phenomenon in the Gaussian white noise model. Electronic Journal of Statistics, 5:373–404, 2011. 

- [15] H. Owhadi and C. Scovel. Brittleness of Bayesian inference and new Selberg formulas. Commun. Math. Sci., 14(1):83–145, 2016. 

- [16] H. Owhadi, C. Scovel, and T. Sullivan. Brittleness of Bayesian inference under finite information in a continuous world. Electronic Journal of Statistics, 9(1):1–79, 2015. 

- [17] H. Owhadi, C. Scovel, and T. Sullivan. On the brittleness of Bayesian inference. SIAM Review, 57(4):566–582, 2015. 

- [18] P. Diaconis and D. Freedman. On the consistency of Bayes estimates. Ann. Stat., 14(1):1–26, 1986. 

- [19] L. Gustafson, P. and Wasserman. Local sensitivity diagnostics for bayesian inference. Ann. Stat., 23(6):2153–2167, 1995. 

- [20] Y. Marzouk and D. Xiu. A stochastic collocation approach to Bayesian inference in inverse problems. Communications in Computational Physics, 6(4):826–847, 2009. 

- [21] V. Bogachev. Gaussian Measures. American Mathematical Society, 1998. 

- [22] H.-H. Kuo. Gaussian Measures in Banach Spaces. Lecture Notes in Mathematics. Springer, Berlin Heidelberg, 1975. 

- [23] M. Hairer, J. C. Mattingly, and M. Scheutzow. Asymptotic coupling and a general form of Harris’ theorem with applications to stochastic delay equations. Probability Theory and Related Fields, 149(1– 2):223–259, 2011. 

- [24] D. Rudolf and N. Schweizer. Perturbation theory for Markov chains via Wasserstein distance. Bernoulli, 24(4A):2610–2639, 2018. 

27 

- [25] F. Medina-Aguayo, D. Rudolf, and N. Schweizer. Perturbation bounds for Monte Carlo within metropolis via restricted approximations. Stoch. Proc. Appl., 2019. doi:10.1016/j.spa.2019.06.015. 

- [26] H. Roininen, J. M. J. Huttunen, and S. Lasanen. Whittle–Mat´ern priors for Bayesian statistical inversion with applications in electrical impedance tomography. Inverse Probl. Imag., 8(2):561–586, 2014. 

- [27] M. Dunlop, M. A. Iglesias, and A. M. Stuart. Hierarchical Bayesian level set inversion. Stat. Comput., 27:1555–1584, 2017. 

- [28] A. L. Gibbs and F. E. Su. On choosing and bounding probability metrics. International Statistical Review, 70(3):419–435, 2001. 

- [29] A. M. Stuart and A. L. Teckentrup. Posterior consistency for Gaussian process approximations of Bayesian posterior distributions. Math. Comp., 87:721–753, 2018. 

- [30] B. J. K. Kleijn and A. W. van der Vaart. The Bernstein-von-Mises theorem under misspecification. Electronic Journal of Statistics, 6:354–381, 2012. 

- [31] L. Devroye, A. Mehrabian, and T. Reddad. The total variation distance between high-dimensional Gaussians. arXiv:1810.08693v3, 2019. 

- [32] D. M. Endres and J. E. Schindelin. A new metric for probability distributions. IEEE Transactions on Information Theory, 49(7):1858–1860, 2003. 

- [33] L. Pardo. Statistical Inference Based on Divergence Measures. Number 185 in Statistics: Textbooks and Monographs. Chapman & Hall/CRC, Boca Raton, FL, 2006. 

- [34] C. Villani. Optimal Transport: Old and New. Number 338 in Grundlehren der Mathematischen Wissenschaften. Springer, Berlin Heidelberg, 2009. 

- [35] M. Gelbrich. On a formula for the L[2] Wasserstein metric between measures on Euclidean and Hilbert spaces. Mathematische Nachrichten, 147(1):185–203, 1990. 

- [36] C.-R. Hwang. Laplace’s method revisited: weak convergence of probability measures. Ann. Prob., 8(6):1177–1182, 1980. 

- [37] A. P. Dempster. A subjectivist look at robustness. Bull. Int. Statist. Inst., 46:349–374, 1975. 

- [38] I. J. Good. Probability and the Weighing of Evidence. Charles Griffin, London, 1950. 

- [39] P. J. Huber. The use of Choquet capacities in statistics. Bull. Internat. Statist. Inst., 45:181–191, 1973. 

- [40] J. O. Berger. Robust Bayesian analysis: sensitivity to the prior. J. Statist. Plann. Inference, 25(3):303– 328, 1990. 

- [41] L. Wasserman and T. Seidenfeld. The dilation phenomenon in robust Bayesian inference. J. Statist. Plann. Inferences, 40:345–356, 1994. 

- [42] D. K. Dey and L. R. Birmiwal. Robust Bayesian analysis using entropy and divergence measures. Statist. Probab. Lett., 20(1):287–294, 1994. 

- [43] A. E. Gelfand and D. K. Dey. On Bayesian robustness of contaminated classes of priors. Statist. Decisions, 9:63–80, 1991. 

- [44] G. Da Prato and J. Zabczyk. Second Order Partial Differential Equations in Hilbert Spaces. Cambridge University Press, Cambridge, 2004. 

28 

