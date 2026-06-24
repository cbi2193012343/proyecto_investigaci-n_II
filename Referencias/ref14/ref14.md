SNN/2004-1 

# A linear theory for control of non-linear stochastic systems 

Hilbert J. Kappen[∗] 

Department of Medical Physics & Biophysics Radboud University, Geert Grooteplein 21 6525 EZ Nijmegen, The Netherlands † 

(Dated: February 2, 2008) 

We address the role of noise and the issue of efficient computation in stochastic optimal control problems. We consider a class of non-linear control problems that can be formulated as a path integral and where the noise plays the role of temperature. The path integral displays symmetry breaking and there exist a critical noise value that separates regimes where optimal control yields qualitatively different solutions. The path integral can be computed efficiently by Monte Carlo integration or by Laplace approximation, and can therefore be used to solve high dimensional stochastic control problems. 

PACS numbers: 02.30 Yy, 02.50 Ey, 05.45. -a, 07.05.Dz, 45.80.+r 

Optimal control of non-linear systems in the presence of noise is a very general problem that occurs in many areas of science and engineering. It underlies autonomous system behavior, such as the control of movement and planning of actions of animals and robots, but also for instance the optimization of financial investment policies and control of chemical plants. The problem is simply stated: given that the system is in this configuration at this time, what is the optimal course of action to reach a goal state at some future time. The cost of each time course of actions consists typically of a path contribution, that specifies the amount of work or other cost of the trajectory, and an end cost, that specifies to what extend the trajectory reaches the goal state. 

In the absence of noise, the optimal control problem can be solved in two ways: using the Pontryagin Minimum Principle (PMP) [1] which is a pair of ordinary differential equations that are similar to the Hamilton equations of motion or using the Hamilton-Jacobi-Bellman (HJB) equation, which is a partial differential equation [2]. 

In the presence of (Wiener) noise, the PMP formalism is replaced by a set of stochastic differential equations which become difficult to solve (see however [3]). The inclusion of noise in the HJB framework is mathematically quite straight-forward, yielding the so-called stochastic HJB equation [4]. Its solution , however, requires a discretization of space and time and the computation becomes intractable in both memory requirement and CPU time in high dimensions. As a result, deterministic control can be computed efficiently using the PMP approach, but stochastic control is intractable due to the curse of dimensionality. 

For small noise, one expects that optimal stochastic control resembles optimal deterministic control, but for larger noise, the optimal stochastic control can be en- 

tirely different from the deterministic control [5], but there is currently no good understanding how noise affects optimal control. 

In this paper, we address both the issue of efficient computation and the role of noise in stochastic optimal control. We consider a class of non-linear stochastic control problems, that can be formulated as a statistical mechanics problem. This class of control problems includes arbitrary dynamical systems, but with a limited control mechanism. It contains linear-quadratic [4] control as a special case. We show that under certain conditions on the noise, the HJB equation can be written as a linear partial differential equation 

**==> picture [150 x 10] intentionally omitted <==**

with H a (non-Hermitian) operator. Eq. 1 must be solved subject to a boundary condition at the end time. As a result of the linearity of Eq. 1, the solution can be obtained in terms of a diffusion process evolving forward in time, and can be written as a path integral. The path integral has a direct interpretation as a free energy, where noise plays the role of temperature. 

This link between stochastic optimal control and a free energy has two immediate consequences. 1) Phenomena that allow for a free energy description, typically display phase transitions. We argue that for stochastic optimal control one can identify a critical noise value that separates regimes where the optimal control is qualitatively different and illustrate this with a simple example. 2) Since the path integral appears in other branches of physics, such as statistical mechanics and quantum mechanics, we can borrow approximation methods from those fields to compute the optimal control approximately. We show how the Laplace approximation can be combined with Monte Carlo sampling to efficiently compute the optimal control. 

Let ⃗x be an n-dimensional stochastic variable that is subject to the stochastic differential equation 

> ∗Electronic address: B.Kappen@science.ru.nl 

> †URL: http://www.snn.kun.nl/~bert 

**==> picture [177 x 13] intentionally omitted <==**

2 

with dξ[⃗] a Wiener process with ⟨dξidξj⟩ = νij dt, and νij independent of ⃗x, ⃗u, t. ⃗b(⃗x, t) is an arbitrary n- dimensional function of ⃗x and t, and ⃗u an n-dimensional vector of control variables. Given ⃗x at an initial time t, the stochastic optimal control problem is to find the control path ⃗u(·) that minimizes 

and assume there exists a scalar λ such that 

**==> picture [154 x 11] intentionally omitted <==**

with δij the Kronecker delta. In the one dimensional case, such a λ can always be found. In the higher dimensional case, this restricts the matrices R ∝ ν[−][1] [11]. Eq. 8 reduces the dependence of optimal control on the n-dimensional noise matrix to a scalar value λ that will play the role of temperature. Eq. 5 reduces to the linear equation 1 with 

**==> picture [234 x 54] intentionally omitted <==**

**==> picture [192 x 22] intentionally omitted <==**

with R a matrix, V (⃗x, t) a time-dependent potential, and φ(⃗x) the end cost. The brackets ⟨⟩⃗x denote expectation value with respect to the stochastic trajectories (2) that start at ⃗x. 

Let ρ(⃗y, τ |⃗x, t) with ρ(⃗y, t|⃗x, t) = δ(⃗y − ⃗x) describe a diffusion process for τ > t defined by the Fokker-Planck equation 

One defines the optimal cost-to-go function from any time t and state ⃗x as 

**==> picture [507 x 122] intentionally omitted <==**

J satisfies the stochastic HJB equation which takes the form 

We arrive at the important conclusion that ψ(⃗x, t) can be computed either by backward integration using Eq. 1 or by forward integration of a diffusion process given by (5) Eq. 10. 

We can write the integral in Eq. 11 as a path integral. We use the standard argument [6] and divide the time interval t → tf in n1 intervals and write ρ(⃗y, tf |⃗x, t) = �ni=11[ρ][(][⃗x][i][, t][i][|][⃗x][i][−][1][, t][i][−][1][)][and][let][n][1][→∞][.][The][result][is] 

with Tr(ν∇[2] J) =[�] ij[ν][ij][∂][2][J/∂x][i][∂x][j][and] 

**==> picture [165 x 13] intentionally omitted <==**

the optimal control at ⃗x, t. The HJB equation is nonlinear in J and must be solved with end boundary condition J(⃗x, tf ) = φ(⃗x). Define ψ(⃗x, t) through [10] 

**==> picture [216 x 25] intentionally omitted <==**

with � [d⃗x]⃗x an integral over all paths ⃗x(t → tf ) that start at ⃗x and with 

**==> picture [174 x 11] intentionally omitted <==**

**==> picture [475 x 31] intentionally omitted <==**

the Action associated with a path. From Eqs. 7 and 12, the cost-to-go J(x, t) becomes a log partition sum (ie. a free energy) with temperature λ. 

in which particles get annihilated at a rate V (⃗x, t)/λ: 

**==> picture [240 x 27] intentionally omitted <==**

The path integral Eq. 12 can be estimated by stochastic integration from t to tf of the diffusion process Eq. 10 

where † denotes that the particle is taken out of the simulation. Denote the trajectories by ⃗xα(t → tf ), α = 

3 

1, . . . , N . Then, ψ(⃗x, t) and ⃗u are estimated as 

**==> picture [198 x 84] intentionally omitted <==**

where ’alive’ denotes the subset of trajectories that do not get killed along the way by the † operation. The normalization 1/N ensures that the annihilation process is properly taken into account. Eq. 16 states that optimal control at time t is obtained by averaging the initial directions of the noise component of the trajectories dξ[⃗] α(t), weighted by their success at tf . 

The above sampling procedure can be quite inefficient, when many trajectories get annihilated. One of the simplest procedures to improve it is by importance sampling. We replace the diffusion process that yields ρ(⃗y, tf |⃗x, t) by another diffusion process, that will yield ρ[′] (⃗y, tf |⃗x, t) = exp(−S[′] /λ). Then Eq. 12 becomes, 

**==> picture [215 x 23] intentionally omitted <==**

The idea is to chose ρ[′] such as to make the sampling of the path integral as efficient as possible. Here, we use the Laplace approximation, which is given by the k deterministic trajectories xβ(t → tf ) that minimize the Action 

**==> picture [220 x 31] intentionally omitted <==**

The Laplace approximation ignores all fluctuations around the modes and becomes exact in the limit λ → 0. The Laplace approximation can be computed efficiently, requiring O(n[2] m[2] ) operations, where m is the number of time discretization. 

For each Laplace trajectory, we define a diffusion processes ρ[′] β[according][to][Eq.][14][with][ ⃗b][(][⃗x, t][)][=][⃗x][˙][β][(][t][).][The] estimators for ψ and ⃗u are given again by Eqs. 15 and 16, but with weights 

**==> picture [248 x 35] intentionally omitted <==**

S is the original Action Eq. 13 and Sβ[′][is][the][new][Action] for the Laplace guided diffusion. When there are multiple Laplace trajectories one should include all of these in the sample. 

We give a simple one-dimensional example of a double slit to illustrate the effectiveness of the Laplace guided MC method and to show how the optimal cost-to-go undergoes symmetry breaking as a function of the noise. 

**==> picture [132 x 103] intentionally omitted <==**

**----- Start of picture text -----**<br>
8<br>6<br>4<br>2<br>0<br>−2<br>−4<br>−6<br>0 0.5 1 1.5 2<br>t<br>x<br>**----- End of picture text -----**<br>


FIG. 1: A double slit is placed at t = 1 with openings at −6 < x < −4 and 6 < x < 8. V = ∞ for t = 1 outside the openings, and zero otherwise. Also shown are two example trajectories under optimal control. 

**==> picture [127 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>2.5<br>2<br>1.5<br>1<br>0.5<br>−10 −5 0 5 10<br>x<br>J<br>**----- End of picture text -----**<br>


FIG. 2: Comparison of Laplace approximation (dotted line) and Monte Carlo importance sampling (solid jagged line) of J(x, t = 0) with exact result (solid smooth line) for the double slit problem. The importance sampler used N = 100 trajectories for each x. R = 0.1, ν = 1, dt = 0.02. 

Consider a stochastic particle that moves with constant velocity from t = 0 to tf = 2 in the horizontal direction and where there is deflecting noise in the x direction: 

**==> picture [68 x 10] intentionally omitted <==**

The cost is given by Eq. 3 with φ(x) =[1] 2[x][2][and][V][ (][x, t][1][)] implements a slit at an intermediate time t1 = 1 (Fig. 1). Solving the cost-to-go by means of the forward computation using Eq. 11 can be done in closed form. The exact result, the Laplace approximation Eq. 17 and the Laplace guided importance sampling result using Eq. 18 are plotted for t = 0 as a function of x in Fig. 2. For each x, the Laplace approximation consists of the two deterministic trajectories, each being piecewise linear, starting at t = 0 in x and ending at t = 2 in x = 0. We see that the Laplace approximation is quite good for this example, in particular when one takes into account that a constant shift in J does not affect the optimal control. The MC importance sampler has maximal error of order 0.1 and is significantly better than the Laplace approximation. Naive MC sampling using Eq. 14 (not shown) fails for this problem, because most trajectories get killed by the infinite potential. Numerical simulations using N = 100000 trajectories yield estimation errors in J up to approximately 6 for certain values of x. 

4 

**==> picture [186 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
stochastic deterministic<br>2 2<br>0 0<br>−2 −2<br>0 1 2 0 1 2<br>t t<br>2 2<br>0 0<br>−2 −2<br>0 1 2 0 1 2<br>t t<br>x x<br>u u<br>**----- End of picture text -----**<br>


FIG. 3: Symmetry breaking in J as a function of T implies a ’delayed choice’ mechanism for optimal stochastic control. When the target is far in the future, the optimal policy is to steer between the targets. Only when T < 1/ν should one aim for one of the targets. Sample trajectories (top row) and controls (bottom row) under stochastic control (left column) and deterministic control (right column). ν = R = 1, t1 = 2. 

We show an example how optimal stochastic control exhibits spontaneous symmetry breaking. For two slits of width ǫ at x = ±1, the cost-to-go becomes to lowest order in ǫ: 

**==> picture [252 x 25] intentionally omitted <==**

where the constant diverges as O(log ǫ) independent of x and T = t1 − t the time to reach the slits. The expression between brackets is a typical free energy with inverse temperature β = 1/νT . It displays a symmetry breaking at νT = 1. The optimal control is given by the gradient of J: 

**==> picture [178 x 21] intentionally omitted <==**

- [1] L. Pontryagin, V. Boltyanskii, R. Gamkrelidze, and E. Mishchenko, The mathematical theory of optimal processes (Interscience, 1962). 

- [2] R. Bellman and R. Kalaba, Selected papers on mathematical trends in control theory (Dover, 1964). 

- [3] J. Yong and X. Zhou, Stochastic controls. Hamiltonian Systems and HJB Equations (Springer, 1999). 

- [4] R. Stengel, Optimal control and estimation (Dover publications, New York, 1993). 

- [5] S. Russell and P. Norvig, Artificial Intelligence. A modern Approach (Prentice Hall, 2003). 

- [6] H. Kleinert, Path integrals in quantum mechanics, statistics and polymer physics (World Scientific, 1995), second edition. 

- [7] W. Miller, J.Chem. Phys. 63, 1166 (1975). 

- [8] D. Freeman and J. Doll, J.Chem. Phys. 80, 5709 (1984). 

- [9] W. Fleming, Applied Math. Optim. 4, 329 (1978). 

For T > 1/ν (far in the past) optimal control steers towards x = 0 (between the targets) and delays the choice which slit to aim for until later. The reason why this is optimal is that the expected diffusion alone of size √νT is likely to reach any of the slits without control (although it is not clear yet which slit). Only sufficiently late in time (T < 1/ν) should one make a choice. 

Figure 3 depicts two trajectories and their controls under stochastic optimal control (Eq. 19) and deterministic optimal control (Eq. 19 with ν = 0), using the same realization of the noise. Note, that at early times the deterministic control drives x away from zero whereas in the stochastic control drives x towards zero and is smaller in size. The stochastic control delays the choice for which slit to aim until T ≈ 1. 

In summary, we have shown that stochastic optimal control involves symmetry breaking with qualitatively different solutions for high and low noise levels. This property is expected to be true also for more general stochastic control problems. The path integral formulation allows for an efficient solution of the HJB equation because it replaces the intractable n-dimensional numerical integration by a Monte Carlo sampling, which is known to be often much more efficient. This approach will thus be of direct practical value for the control of high dimensional, strongly non-linear, systems, such as for instance robot arms, navigation of autonomous systems, and chemical reactions. For realistic applications, naive sampling should be replaced by more advanced sampling schemes, such as importance sampling or a Metropolis method, and should be combined with efficient discretization such as splines, wavelets or a Fourier basis [7, 8]. 

## Acknowledgments 

I would like to thank Hans Maassen for useful discussions. This work is supported in part by the Dutch Technology Foundation and the BSIK/ICIS project. 

- [10] The log transform goes back to Schr¨odinger and was first used in control theory by [9]. 

- [11] For example, if both R and ν are diagonal matrices, in a direction with low noise, control is expensive (Rii large) and only small control steps are permitted. In noisy directions the reverse is true: control is cheap and large control values are permitted. As another example, consider a one-dimensional second order system subject to additive control x¨ = b(x, t) + u. The stochastic formulation is of the form 

**==> picture [157 x 12] intentionally omitted <==**

Eq. 8 states that due to the absence of a control term in the equation for dx, the noise in this equation should be zero. 

