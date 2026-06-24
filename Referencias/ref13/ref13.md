## **Efficient computation of optimal actions** 

## **Emanuel Todorov[1]** 

Departments of Applied Mathematics and Computer Science & Engineering, University of Washington, Box 352420, Seattle, WA 98195; 

Edited by James L. McClelland, Stanford University, Stanford, CA, and approved April 28, 2009 (received for review November 16, 2007) 

**Optimal choice of actions is a fundamental problem relevant to fields as diverse as neuroscience, psychology, economics, computer science, and control engineering. Despite this broad relevance the abstract setting is similar: we have an agent choosing actions over time, an uncertain dynamical system whose state is affected by those actions, and a performance criterion that the agent seeks to optimize. Solving problems of this kind remains hard, in part, because of overly generic formulations. Here, we propose a more structured formulation that greatly simplifies the construction of optimal control laws in both discrete and continuous domains. An exhaustive search over actions is avoided and the problem becomes linear. This yields algorithms that outperform Dynamic Programming and Reinforcement Learning, and thereby solve traditional problems more efficiently. Our framework also enables computations that were not possible before: composing optimal control laws by mixing primitives, applying deterministic methods to stochastic systems, quantifying the benefits of error tolerance, and inferring goals from behavioral data via convex optimization. Development of a general class of easily solvable problems tends to accelerate progress—as linear systems theory has done, for example. Our framework may have similar impact in fields where optimal choice of actions is relevant.** 

action selection | cost function | linear Bellman equation | stochastic optimal control 

**I** fpossible.you areButgoingwhichto act,wayyouis best?mightThisas wellis theactgeneralin the bestproblemway we consider here. Examples include a nervous system generating muscle activations to maximize movement performance (1), a foraging animal deciding which way to turn to maximize food (2), an internet router directing packets to minimize delays (3), an onboard computer controlling a jet engine to minimize fuel consumption (4), and an investor choosing transactions to maximize wealth (5). Such problems are often formalized as Markov decision processes (MDPs), with stochastic dynamics _p_ ( _x_[′] | _x_ , _u_ ) specifying the transition probability from state _x_ to state _x_[′] under action _u_ , and immediate cost _ℓ_ ( _x_ , _u_ ) for being in state _x_ and choosing action _u_ . The performance criterion that the agent seeks to optimize is some cumulative cost that can be formulated in multiple ways. Throughout the article we focus on one formulation (total cost with terminal/goal states) and summarize results for other formulations. 

Optimal actions cannot be found by greedy optimization of the immediate cost, but instead must take into account all future costs. This is a daunting task because the number of possible futures grows exponentially with time. What makes the task doable is the optimal cost-to-go function _v_ ( _x_ ) defined as the expected cumulative cost for starting at state _x_ and acting optimally thereafter. It compresses all relevant information about the future and thus enables greedy computation of optimal actions. _v_ ( _x_ ) equals the minimum (over actions _u_ ) of the immediate cost _ℓ_ ( _x_ , _u_ ) plus the expected cost-to-go E[ _v_ ( _x_[′] )] at the next state _x_[′] : 

**==> picture [196 x 13] intentionally omitted <==**

The subscript indicates that the expectation is taken with respect to the transition probability distribution _p_ (·| _x_ , _u_ ) induced by action _u_ . Eq. **1** is fundamental to optimal control theory and is called the Bellman equation. It gives rise to Dynamic Programming (3) and 

Reinforcement Learning (2) methods that are very general but can be inefficient. Indeed, Eq. **1** characterizes _v_ ( _x_ ) only implicitly, as the solution to an unsolved optimization problem, impeding both analytical and numerical approaches. 

Here, we show how the Bellman equation can be greatly simplified. We find an analytical solution for the optimal _u_ given _v_ , and then transform Eq. **1** into a linear equation. Short of solving the entire problem analytically, reducing optimal control to a linear equation is the best one can hope for. This simplification comes at a modest price: although we impose certain structure on the problem formulation, most control problems of practical interest can still be handled. In discrete domains our work has no precursors. In continuous domains there exists related prior work (6–8) that we build on here. Additional results can be found in our recent conference articles (9–11), online preprints (12–14), and supplementary notes [supporting information (SI) _Appendix_ ]. 

## **Results** 

**Reducing Optimal Control to a Linear Problem.** We aim to construct a general class of MDPs where the exhaustive search over actions is replaced with an analytical solution. Discrete optimization problems rarely have analytical solutions, thus our agenda calls for continuous actions. This may seem counterintuitive if one thinks of actions as symbols (“go left,” “go right”). However, what gives meaning to such symbols are the underlying transition probabilities—which are continuous. The latter observation is key to the framework developed here. Instead of asking the agent to specify symbolic actions, which are then replaced with transition probabilities, we allow the agent to specify transition probabilities _u_ ( _x_[′] | _x_ ) directly. Formally, we have _p_ ( _x_[′] | _x_ , _u_ ) = _u_ ( _x_[′] | _x_ ). 

Thus, our agent has the power to reshape the dynamics in any way it wishes. However, it pays a price for too much reshaping, as follows. Let _p_ ( _x_[′] | _x_ ) denote the passive dynamics characterizing the behavior of the system in the absence of controls. The latter will usually be defined as a random walk in discrete domains and as a diffusion process in continuous domains. Note that the notion of passive dynamics is common in continuous domains but is rarely used in discrete domains. We can now quantify how “large” an action is by measuring the difference between _u_ (·| _x_ ) and _p_ (·| _x_ ). Differences between probability distributions are usually measured via Kullback–Leibler (KL) divergence, suggesting an immediate cost of the form 

**==> picture [249 x 32] intentionally omitted <==**

The state cost _q_ ( _x_ ) can be an arbitrary function encoding how (un)desirable different states are. The passive dynamics _p_ ( _x_[′] | _x_ ) and controlled dynamics _u_ ( _x_[′] | _x_ ) can also be arbitrary, except that 

Author contributions: E.T. designed research, performed research, analyzed data, and wrote the paper. 

This article is a PNAS Direct Submission. 

Freely available online through the PNAS open access option. 

See Commentary on Page 11429. 

1E-mail: todorov@cs.washington.edu. 

This article contains supporting information online at www.pnas.org/cgi/content/full/ 0710743106/DCSupplemental. 

**11478–11483** PNAS **July 14, 2009** vol. 106 no. 28 

www.pnas.org / cgi / doi / 10.1073 / pnas.0710743106 

**==> picture [169 x 23] intentionally omitted <==**

This represents the first general class of MDPs where the optimal actions can be found analytically given the optimal costs-to-go. Previously, such results were available only in continuous domains. 

The Bellman equation can now be simplified ( _SI Appendix_ ) by substituting the optimal action, taking into account the normalization term and exponentiating. The result is 

**==> picture [173 x 10] intentionally omitted <==**

**Fig. 1.** New problem formulation. ( _A_ ) A coin-toss example where the action corresponds to biasing the coin. The optimal bias is obtained by minimizing the sum (black) of the KL divergence cost (red) and the expected state cost (blue). Note that the tosses are independent and thus the temporal dynamics are irrelevant in this example. ( _B_ ) A stochastic shortest-path problem illustrating how our framework can capture the benefits of error tolerance. See main text. 

we require _u_ ( _x_[′] | _x_ ) = 0 whenever _p_ ( _x_[′] | _x_ ) = 0. This constraint is needed to make KL divergence well-defined. It has the added benefit of preventing the agent from jumping directly to goal states, and more generally from making state transitions that are physically impossible. 

Fig. 1 illustrates the construction above with two simple examples.Fig.1 _A_ isacoin-tossproblemwhere _q_ (Tails) = 0, _q_ (Heads) = 1 and the passive dynamics correspond to an unbiased coin. The action _u_ has the effect of biasing the coin. The optimal bias, which turns out to be _u_[∗] (Heads) = 0.27, achieves a trade-off between keeping the action cost and the expected state cost small. Note that the controller could have made the coin deterministic by setting _u_ (Heads) = 0, but this is suboptimal because the associated action cost is too large. In general, the optimal actions resulting from our framework are stochastic. Fig. 1 _B_ is a shortest-path problem where _q_ = 0 for the goal state (gray) and _q_ = 1 for all other states. The passive dynamics correspond to the random walk on the graph. At the green state it does not matter which path is taken, so the optimal action equals the passive dynamics, the action cost is 0, and the cost-to-go (shown inside the circle) equals the length of the deterministic shortest path. At the red state, however, the optimal action deviates from the passive dynamics to cause a transition up, incurring an action cost of 0.6 and making the red state worse than the green state. In general, _v_ ( _x_ ) is smaller when the task can be accomplished in multiple ways starting from _x_ . This reflects a preference for error tolerance that is inherent in our framework. 

We now return to the theoretical development. The results take on a simpler form when expressed in terms of the _desirability_ function 

**==> picture [160 x 10] intentionally omitted <==**

This terminology reflects the fact that _z_ is large at states where the cost-to-go _v_ is small. Substituting Eq. **1** in Eq. **2** , the Bellman equation can be written in terms of _z_ as 

**==> picture [236 x 22] intentionally omitted <==**

The expression being minimized resembles KL divergence between _u_ and _pz_ , except that _pz_ is not normalized to sum to 1. Thus, to obtain proper KL divergence ( _SI Appendix_ ), we have to multiply and divide by the normalization term 

**==> picture [206 x 19] intentionally omitted <==**

Recall that KL divergence achieves its global minimum of zero when the 2 distributions are equal. Therefore, the optimal action _u_[∗] is proportional to _pz_ : 

The expectation _G_ [ _z_ ] is a linear operator; thus, Eq. **7** is linear in _z_ . It can be written more compactly in vector notation. Enumerate the states from 1 to _n_ , represent _z_ ( _x_ ) and _q_ ( _x_ ) with the _n_ -dimensional column vectors **z** and **q** , and _p_ ( _x_[′] | _x_ ) with the _n_ -by- _n_ matrix _P_ , where the row-index corresponds to _x_ and the column-index to _x_[′] . Then Eq. **7** becomes **z** = _M_ **z** ,where _M_ = diag(exp(− **q** )) _P_ ,expisapplied element-wise and diag transforms vectors into diagonal matrices. The latter equation looks like an eigenvector problem, and indeed it can be solved (9) by using the power iteration method **z** ← _M_ **z** (which we call Z iteration). However, the problem here is actually simpler because the eigenvalue is 1 and _v_ ( _x_ ) = _q_ ( _x_ ) at terminal states. If we define the index sets _T_ and _N_ of terminal and nonterminal states and partition **z** , **q** , and _P_ accordingly, Eq. **7** becomes 

**==> picture [214 x 9] intentionally omitted <==**

The unknown **z** _N_ is the vector of desirabilities at the nonterminal states. It can be computed via matrix factorization or by using an iterative linear solver. 

Let us now compare our result (Eq. **8** ) with policy iteration (3). We have to solve an equation of the form _A_ **z** = **b** just once. In policy iteration one has to solve an equation of the form _A_ (π) **v** = **b** (π) toevaluatethecurrentpolicy π;then,thepolicyhastobeimproved and the process repeated. Therefore, solving an optimal control problem in our formulation is computationally equivalent to half a step of policy iteration. 

Thus far, we have studied MDPs with discrete state spaces. There exists a family of continuous (in space and time) problems related to our MDPs. These problems have stochastic dynamics 

**==> picture [185 x 10] intentionally omitted <==**

**ω** ( _t_ ) is Brownian motion and σ is the noise amplitude. The cost rate is of the form 

**==> picture [174 x 20] intentionally omitted <==**

The functions _q_ ( **x** ), **a** ( **x** ), and _B_ ( **x** ) can be arbitrary. This problem formulation is fairly general and standard (but see _Discussion_ ). Consider, for example, a one-dimensional point with mass _m_ , position _xp_ , and velocity _xv_ . Then, **x** = [ _xp_ , _xv_ ][T] , **a** ( **x** ) = [ _xv_ , 0][T] , and _B_ = [0, _m_[−][1] ][T] . The noise and control signals correspond to external forces applied to the point mass. 

Unlike the discrete case where the agent could specify the transition probability distribution directly, here, **u** is a vector that can shift the distribution given by the passive dynamics but cannot reshape it. Specifically, if we discretize the time axis in Eq. **9** with step _h_ , the passive dynamics are Gaussian with mean **x** + _h_ **a** ( **x** ) and covariance _h_ σ[2] _B_ ( **x** ) _B_ ( **x** )[T] , whereas the controlled dynamics are Gaussian with mean **x** + _h_ **a** ( **x** ) + _hB_ ( **x** ) **u** and the same covariance. Thus, the agent in the continuous setting has less freedom comparedwiththediscretesetting.Yetthetwosettingssharemany similarities, as follows. First, the KL divergence between the above Gaussians can be shown to be 2σ _h_[2][∥] **[u]**[∥][2][, which is just the quadratic] energy cost accumulated over time interval _h_ . Second, given the 

Todorov 

PNAS **July 14, 2009** vol. 106 no. 28 **11479** 

**Table 1. Summary of results for all performance criteria** 

|**Table 1. Summary of results for all performance criteria**|**Table 1. Summary of results for all performance criteria**|**Table 1. Summary of results for all performance criteria**|
|---|---|---|
|Discrete<br>Continuous<br>Finite<br>exp(_q_)_zt_ =**_G_**[_zt_+1]<br>_qz_ =**_L_**[_z_] + _∂_<br>_∂t z_<br>~~oo~~<br>~~_~~|||
|Total|exp(_q_)_z_ =**_G_**[_z_]|_qz_ =**_L_**[_z_]|
|Average|exp(_q_−_c_)_z_ =**_G_** _z_|(_q_−_c_)_z_ =**_L_** _z_|
|Discounted|exp(_q_)_z_ =**_G_**[_zα_]|_qz_ =**_L_**[_z_] −_z_log(_zα_)|



optimal cost-to-go _v_ ( **x** ), the optimal control law can be computed analytically (4): 

**==> picture [169 x 11] intentionally omitted <==**

Here, subscripts denote partial derivatives. Third, the Hamilton– Jacobi–Bellman equation characterizing _v_ ( **x** ) becomes linear (6, 7) ( _SI Appendix_ ) when written in terms of the desirability function _z_ ( **x** ): 

**==> picture [160 x 10] intentionally omitted <==**

The second-order linear differential operator _L_ is defined as 

**==> picture [226 x 21] intentionally omitted <==**

Additional similarities between the discrete and continuous settings will be described below. They reflect the fact that the continuous problem is a special case of the discrete problem. Indeed, we can show ( _SI Appendix_ ) that, for certain MDPs in our class, Eq. **7** reduces to Eq. **12** in the limit _h_ → 0. 

The linear equations **7** and **12** were derived by minimizing total cost in the presence of terminal/goal states. Similar results can be obtained ( _SI Appendix_ ) for all other performance criteria used in practice, in both discrete and continuous settings. They are summarized in Table 1. The constant _c_ is the (unknown) average cost computed as the principal eigenvalue of the corresponding equation. is the exponent of the differential cost-to-go function (3) ( _SI Appendix_ ). The constant _α_ is the exponential discount factor. Note that all equations are linear except in the discounted case. The finite-horizon and total-cost results in continuous settings were previously known (6, 7); the remaining six equations were derived in our work. 

**Fig. 2.** Approximating shortest paths. The computation of shortest path lengths is illustrated here using the graph of internet routers and their connectivity as of 2003. This dataset is publicly available at www.caida.org. The graph has 190,914 nodes and 609,066 undirected edges. The shortest path length from each node to a specified destination node was computed exactly by using dynamic programming adapted to this problem, and also approximated by using our algorithm with ρ = 40. Our algorithm was ≈5 times faster, although both implementations were equally optimized. The exact shortest path lengths were integers between 1 and 15. ( _A_ ) The approximate values were binned in 15 bins according to the corresponding correct value. The range of approximate values in each bin is shown with the blue symbols. The diagonal red line is the exact solution. ( _Inset_ ) Histogram of all values in one bin, with the correct value subtracted. Note that all errors are between 0 and 1, thus rounding down to the nearest integer recovers the exact solution. This was the case for all bins. ( _B_ ) To assess the effects of the free parameter ρ, we solved the above problem 500 times for each of 10 values of ρ between 25 and 70. In each instance of the problem, the set of destination nodes was generated randomly and had between 1 and 5 elements. The approximate shortest path lengths found by our algorithm were rounded down to the nearest integer and compared with the exact solution. The number of mismatches, expressed as a percent of the number of nodes and averaged over the 500 repetitions, is plotted in black. For large values of ρ the approximation becomes exact, as expected from Eq. **14** . However, ρ cannot be set too large, because our algorithm multiplies by exp(−ρ), thus some elements of _z_ may become numerically zero. The percentage of such numerical errors is plotted in green. There is a comfortable range of ρ where neither type of error is observed. 

The second application is a method for continuous embedding of traditional MDPs with symbolic actions. It is reminiscent of linear programming relaxation in integer programming. Denote the symbolic actions in the traditional MDP with _a_ , the transition probabilities with _x_[′] | _x_ , _a_ ), and the immediate costs with _ℓ_ ( _x_ , _a_ ). We seek an MDP in our class such that for each ( _x_ , _a_ ) the action 

·| _x_ , _a_ ) has cost _ℓ_ ( _x_ , _a_ ): 

**Applications.** The first application is an algorithm for finding shortest paths in graphs (recall Fig. 1 _B_ ). Let _s_ ( _x_ ) denote the length of the shortest path from state _x_ to the nearest terminal state. The passive dynamics _p_ correspond to the random walk on the graph. The state costs are _q_ = ρ _>_ 0 for non-terminal states and _q_ = 0 for terminal states. Let _v_ ρ( _x_ ) denote the optimal cost-to-go function for given ρ. If the action costs were 0, the shortest path lengths would be _s_ ( _x_ ) = ρ[1] _[v]_[ρ][(] _[x]_[) for all][ ρ][. Here, the action costs are] not 0, but nevertheless they are bounded. Because we are free to choose ρ arbitrarily large, we can make the state costs dominate the cost-to-go function, and so 

**==> picture [158 x 22] intentionally omitted <==**

The construction above involves a limit and does not yield the shortest paths directly. However, we can obtain arbitrarily accurate (modulo numerical errors) approximations by setting ρ large enough. The method is illustrated in Fig. 2 on the graph of internet routers. There is a range of values of ρ for which all shortest path lengths are exactly recovered. Although a thorough comparison with dedicated shortest-path algorithms remains to be done, we suspect that they will not be as efficient as linear solvers. Problems with weighted edges can be handled with the general embedding method presented next. 

**==> picture [195 x 10] intentionally omitted <==**

For each _x_ this yields a system of linear equations in _q_ and log _p_ , which has a unique solution under a mild nondegeneracy condition ( _SI Appendix_ ). If we keep the number of symbolic actions per state fixed while increasing the number of states (for example, by making a grid world larger and larger), the amount of computation needed to construct the embedding scales linearly with the number of states. Once the embedding is constructed, the optimal actions are computed and replaced with the nearest (in the sense of transition probabilities) symbolic actions. This yields an approximately optimal policy for the traditional MDP. We do not yet have theoretical error bounds but have found the approximation to be very accurate in practice. This method is illustrated in Fig. 3 on a machine repair problem adapted from ref. 3. The _R_[2] between the correct and approximate cost-to-go is 0.993. 

The third application is a Monte Carlo method for learning _z_ from experience in the absence of a model of the passive dynamics _p_ and state costs _q_ . Unlike the previous two applications, where we started with traditional MDPs and approximated them with MDPs in our class, here we assume that the problem is already in our class. The linear Bellman Eq. **7** can be unfolded recursively by replacing _z_ ( _x_[′] ) with the expectation over the state following _x_[′] 

**11480** www.pnas.org / cgi / doi / 10.1073 / pnas.0710743106 

Todorov 

**Fig. 3.** Embedding traditional MDPs. The continuous embedding of traditional MDPs is illustrated here on a machine repair problem adapted from ref. 3. We have a machine whose state _xt_ at time _t_ is an integer between 1 and 100. Larger _xt_ means that the machine is more broken and more costly to operate: we incur an operation cost of 0.02 _xt_ . There are 50 time steps (this is a finite-horizon problem). The state of the machine has a tendency to deteriorate over time: if we do nothing, _xt_ +1 has a probability 0.9 of being one of _xt_ · · · _xt_ + 8 (chosen uniformly) and probability 0.1 of being one of _xt_ − 9 · · · _xt_ − 1. When _xt_ is near the edges we clip this distribution and renormalize it to sum to 1. The symbolic actions _ut_ are integers between 0 and 9 corresponding to how much we invest in repairing the machine in each time step. The repair cost is 0.1 _ut_ . The effect of the repairs is to circularly left-shift the above transition probability distribution by _ut_ positions. Thus, _ut_ = 0 corresponds to doing nothing; larger _ut_ causes larger expected improvement in the state of the machine. ( _A_ ) The traditional MDP described above was embedded within our class, as outlined in the main text and described in detail in ( _SI Appendix_ ). Then, _zt_ ( _x_ ) was computed and the approximation − log( _z_ ) to the optimal cost-to-go was plotted. Blue is small, red is large. ( _B_ ) The traditional MDP was also solved by using dynamic programming and the optimal cost-to-go _vt_ ( _x_ ) was plotted in the same format as in _A_ . ( _C_ ) Scatter plot of the optimal versus approximate costs-to-go at 5,000 space-time points (blue). The _R_[2] between the two is 0.993, that is, the optimal values account for 99.3% of the variance in the approximate values. The red diagonal line corresponds to the ideal solution. We also computed (via extensive sampling) the performance of the optimal policy found by dynamic programming, the approximately optimal policy derived from our embedding, and a random policy. The performance of our approximation was 0.9% worse than optimal, whereas the performance of the random policy was 64% worse than optimal. 

and so on, and then pushing all state costs inside the expectation operators. This yields the path-integral representation 

**==> picture [202 x 33] intentionally omitted <==**

( _x_ 0, _x_ 1 · · · _xtf_ ) are trajectories initialized at _x_ 0 = _x_ and sampled from the passive dynamics, and _tf_ is the time when a goal state is first reached. A similar result holds in continuous settings, where the Feynman–Kac theorem states that the unique positive solution to Eq. **12** has a path-integral representation. The use of Monte Carlo methods for solving continuous optimal control problems was pioneered in ref. 7. Our result (Eq. **16** ) makes it possible to apply such methods to discrete problems with non-Gaussian noise. 

The fourth application is related to the path-integral approach above but aims to achieve faster convergence. It is motivated by Reinforcement Learning (2) where faster convergence is often observed by using Temporal Difference (TD) methods. A TD-like method for our MDPs can be obtained from Eq. **7** . It constructs an approximation using triplets ( _xt_ , _qt_ , _xt_ +1). Note that measuring the action costs is not necessary. is updated online as follows: 

**==> picture [199 x 10] intentionally omitted <==**

η _t_ is a learning rate which decreases over time. We call this algorithm Z learning. Despite the resemblance to TD learning, there is an important difference. Our method learns the optimal costto-go directly, whereas TD methods are limited to learning the cost-to-go of a specific policy—which then needs to be improved, the cost-to-go relearned, and so on. Indeed Z learning is an offpolicymethod,meaningthatitlearnsthecost-to-gofortheoptimal policy while sampling according to the passive dynamics. The only 

**Fig. 4.** Z learning and Q learning. Z learning and Q learning are compared in the context of a grid-world MDP. The goal state is marked “X.” State transitions are allowed to all neighbors (including diagonal neighbors) and to the current state. Thus, there are at most 9 possible next states, less when the current state is adjacent to the obstacles shown in black or to the edges of the grid. _p_ corresponds to a random walk. All state costs are _q_ = 1 except for the goal state where _q_ = 0. This MDP is within our class so Z learning can be applied directly. To apply Q learning we first need to construct a corresponding traditional MDP with symbolic actions. This is done as follows. For each state _x_ we define a symbolic action with transition probability distribution matching the optimal _u_[∗] (·| _x_ ). We also define _N_ ( _x_ ) − 1 other symbolic actions, where _N_ ( _x_ ) is the number of possible next states following _x_ . Their transition probability distributions are obtained from _u_[∗] (·| _x_ ) by circular shifting; thus, they have the same shape as _u_[∗] but peak at different next states. All these symbolic actions incur cost _q_ ( _x_ ) + KL( _u_[∗] (·| _x_ )|| _p_ (·| _x_ )) matching the cost in our MDP. The resulting traditional MDP is guaranteed to have the same optimal cost-to-go as our MDP. ( _A_ ) The grayscale image shows the optimal cost-togo _v_ = − log _z_ where _z_ is computed with our model-based method. Darker colors correspond to smaller values. Both Z learning and Q learning aim to approximate this function. ( _B_ ) Error is defined as the average absolute difference between each approximation and the optimal costs-to-go, normalized by the average optimal cost-to-go. All approximations to _z_ are initialized at 0. The learning rate decays as η _t_ = _c/_ ( _c_ + _t_ ), where _c_ = 5, 000 for Z learning and _c_ = 40, 000 for Q learning. Each simulation is repeated 10 times. The state is reset randomly whenever the goal state is reached. Each learning algorithm is tested by using a random policy corresponding to _p_ , as well as a greedy policy. Q learning requires exploration; thus, we use an ε-greedy policy with ε = 0.1. The values of _c_ and ε are optimized manually for each algorithm. Z learning implicitly contains exploration so we can directly use the greedy policy, i.e., the policy _x_[′] | _x_ ) which appears optimal given the current approximation Greedy Z learning requires importance sampling: the last term in Eq. **17** must be weighted by _p_ ( _xt_ +1| _xt_ ) _/_ ( _xt_ +1| _xt_ ). Such weighting requires access to _p_ . ( _C_ ) Empirical performance of the policies resulting from each approximation method at each iteration. Z learning outperforms Q learning, and greedy methods outperform random sampling. 

Reinforcement Learning method capable of doing this is Q learning (15). However, Q learning has the disadvantage of operating in the product space of states and actions, and is therefore less efficient. This is illustrated in Fig. 4 on a navigation problem. 

The fifth application accelerates MDP approximations to continuous problems (16). Such MDPs are obtained via discretization and tend to be very large, calling for efficient numerical methods. Because continuous problems of the form (Eqs. **9** and **10** ) are limits of MDPs in our class, they can be approximated with MDPs in our class, which, in turn, are reduced to linear equations and solved efficiently. The same continuous problems can also be approximated with traditional MDPs and solved via dynamic programming. Both approximations converge to the same solution in the limit of infinitely fine discretization, and turn out to be equally accurate away from the limit, but our approximation is faster to compute. This is shown in Fig. 5 on a car-on-a-hill problem, where our method is ≈10 times faster than policy iteration and 100 times faster than value iteration. 

The remaining applications have been developed recently. Below we summarize the key results and refer the reader to online preprints (12–14). The sixth application is a deterministic method for computing the most likely trajectory of the optimaly controlled stochastic system. Combining Eqs. **6** and **7** , the optimal control law can be written as _u_[∗] ( _x_[′] | _x_ ) = exp(− _q_ ( _x_ )) _p_ ( _x_[′] | _x_ ) _[z] z_[(] ( _[x] x_[′] )[)][. Given a fixed] 

Todorov 

PNAS **July 14, 2009** vol. 106 no. 28 **11481** 

The eighth application concerns inverse optimal control, where the goal is to infer _q_ ( _x_ ) given a dataset { _xk_ , _xk_[′][}] _[k]_[=][1][···] _[K]_[of][state] transitions generated by the optimal controller. Existing methods rely on guessing the cost function, solving the forward problem, comparing the solution with data, and improving the guess and iterating (18, 19). This indirect procedure can be inefficient when the forward problem is hard to solve. For our MDPs the inverse problem can be solved directly, by minimizing the convex function 

**==> picture [186 x 12] intentionally omitted <==**

5:(~’ passive dynamics matrix defined earlier, andwhere **v** is the vector of (unknown) optimal **d** costs-to-go, and **c** are the his- _P_ is the a“a , tograms of _xk_[′][and] _[ x][k]_[(i.e.,] _[ d][i]_[is the number of times that] _[ x] k_[′][=] _[i]_[).] , — It can be shown that _L_ ( **v** ) is the negative log-likelihood of the 9 dataset. We have found empirically that its Hessian tends to be -3 horizontal pos. +3 diagonally dominant, which motivates an efficient quasi-Newton Continuous problems. Comparison of our MDP approximation and method by using a diagonal approximation to the Hessian. Once a traditional MDP approximation on a continuous car-on-a-hill problem. ( _A_ ) the minimum is found, we can compute **z** and then find **q** from moves along a curved road in the presence of gravity. The control the linear Bellman equation. Fig. 5 _D_ illustrates this inverse optiis tangential acceleration. The goal is to reach the parking lot with mal control method on the car-on-a-hill problem. See ref. 14 for velocity. ( _B_ ) Z iteration (blue), policy iteration (red), and value iteradetails. 

**Fig. 5.** Continuous problems. Comparison of our MDP approximation and a traditional MDP approximation on a continuous car-on-a-hill problem. ( _A_ ) The car moves along a curved road in the presence of gravity. The control signal is tangential acceleration. The goal is to reach the parking lot with small velocity. ( _B_ ) Z iteration (blue), policy iteration (red), and value iteration (black) converge to control laws with identical performance; however, Z iteration is 10 times faster than policy iteration and 100 times faster than value iteration. Note the log-scale on the horizontal axis. ( _C_ ) The optimal cost-to-go for our approximation. Blue is small, red is large. The two black curves are stochastic trajectories resulting from the optimal control law. The thick magenta curve is the most likely trajectory of the optimally controlled stochastic system. It is computed by solving the deterministic optimal control problem described in the main text. ( _D_ ) The optimal cost-to-go is inferred from observed state transitions by using our algorithm for inverse optimal control. Brown pixels correspond to states where we did not have data (i.e., no state transitions landed there); thus, the cost-to-go could not be inferred. The details are given in ( _SI Appendix_ ). 

The ninth application is a method for constructing optimal control laws as combinations of certain primitives. This can be done in finite-horizon as well as total-cost problems with terminal/goal states, where the final cost plays the role of a boundary condition. Suppose we have a collection of component final costs _gi_ ( **x** ) for which we have somehow computed the desirability functions _zi_ ( **x** ). Linearity implies that, if the composite final cost _g_ ( **x** ) 

**==> picture [186 x 18] intentionally omitted <==**

for some set of _wi_ , then the composite desirability function is _z_ ( **x** ) = _i[w][i][z][i]_[(] **[x]**[).][This][approach][is][particularly][useful][when][the] component problems can be solved analytically, as in the linearquadratic-Gaussian (LQG) framework (4). In that case the component desirabilities _zi_ ( **x** ) are Gaussians. By mixing them linearly, we can obtain analytical solutions to finite-horizon problems of the form Eqs. **9** and **10** where **a** ( **x** ) is linear, _B_ is constant, _q_ ( **x** ) is quadratic; however, the final cost _g_ ( **x** ) is not constrained to be quadratic. Instead _g_ ( **x** ) can equal the negative log of any Gaussian mixture. This is a nontrivial extension to the widely used LQG framework. See ref. 13 for details. 

initial state _x_ 0 and final time _T_ , the probability that the optimal control law _u_[∗] generates trajectory _x_ 1, _x_ 2, · · · _xT_ is 

**==> picture [225 x 28] intentionally omitted <==**

Omitting _z_ ( _x_ 0), which is fixed, and noting that _z_ ( _xT_ ) = exp(− _q_ ( _xT_ )), the negative log of Eq. **18** can be interpreted as the cumulative cost for a deterministic optimal control problem with immediate cost _q_ ( _x_ ) − log( _p_ ( _x_[′] | _x_ )). A related result is obtained in continuous settings when _B_ is constant:˙ the corresponding deterministic problem has dynamics **x** = **a** ( **x** ) + _B_ **u** and cost _ℓ_ ( **x** , **u** ) + 2[1][div(] **[a]**[(] **[x]**[)). These results are important because optimal] trajectories for deterministic problems can be found with efficient numerical methods (17) that avoid the curse of dimensionality. Our framework makes it possible to apply deterministic methods to stochastic control for the first time. The most likely trajectory in the car-on-a-hill problem is shown in Fig. 5 _C_ in magenta. See ref. 12 for details. 

## **Discussion** 

We formulated the problem of stochastic optimal control in a way which is rather general and yet affords substantial simplifications. Exhaustive search over actions was replaced with an analytical solution and the computation of the optimal cost-to-go function was reduced to a linear problem. This gave rise to efficient new algorithms speeding up the construction of optimal control laws. Furthermore, our framework enabled a number of computations that were not possible previously: solving problems with nonquadratic final costs by mixing LQG primitives, finding the most likely trajectories of optimally controlled stochastic systems via deterministic methods, solving inverse optimal control problems via convex optimization, quantifying the benefits of error tolerance, and applying off-policy learning in the state space as opposed to the state-action space. 

The seventh application exploits the duality between Bayesian estimation and stochastic optimal control. This duality is wellknown for linear systems (4) and was recently generalized (8, 10) to nonlinear continuous systems of the form Eqs. **9** and **10** . Duality also holds for our MDPs. Indeed, Eq. **18** can be interpreted as the posterior probability of a trajectory in a Bayesian smoothing problem, where _p_ ( _xt_ +1| _xt_ ) are the prior probabilities of the state transitionsandexp(− _q_ ( _xt_ ))arethelikelihoodsofsomeunspecified measurements. The desirability function in the control problem can be shown to be proportional to the backward filtering density in the dual estimation problem. Thus, stochastic optimal control problems can be solved by using Bayesian inference. See refs. 10 and 12 for details. 

These advances were made possible by imposing a certain structure on the problem formulation. First, the control cost must be a KL divergence—which reduces to the familiar quadratic energy cost in continuous settings. This is a sensible way to measure control energy and is not particularly restrictive. Second, the controls and the noise must be able to cause the same state transitions; the analog in continuous settings is that both the controls and the 

**11482** www.pnas.org / cgi / doi / 10.1073 / pnas.0710743106 

Todorov 

noise act in the subspace spanned by the columns of _B_ ( **x** ). This is a more significant limitation. It prevents us from modeling systems subject to disturbances outside the actuation space. We are now pursuing an extension that aims to relax this limitation while preserving many of the appealing properties of our framework. Third, the noise amplitude and the control costs are coupled, and, in particular, the control costs are large when the noise amplitude is small. This can be compensated to some extent by increasing the state costs while ensuring that exp(− _q_ ( _x_ )) does not become numerically zero. Fourth, with regard to Z learning, following a policy other than the passive dynamics _p_ requires importancesampling correction based on a model of _p_ . Such a model could presumably be learned online; however, this extension remains to be developed. 

1. Todorov E (2004) Optimality principles in sensorimotor control. _Nat Neurosci_ 7(9):907– 915. 

2. Sutton R, Barto A (1998) _Reinforcement Learning: An Introduction_ (MIT Press, Cambridge MA). 

3. Bertsekas D (2001) _Dynamic Programming and Optimal Control_ (Athena Scientific, Bellmont, MA), 2nd Ed. 

4. Stengel R (1994) _Optimal Control and Estimation_ (Dover, New York). 

5. Korn R (1997) _Optimal Portfolios: Stochastic Models for Optimal Investment and Risk Management in Continuous Time_ (World Scientific, Teaneck, NJ). 

6. Fleming W, Mitter S (1982) Optimal control and nonlinear filtering for nondegenerate diffusion processes. _Stochastics_ 8:226–261. 

7. Kappen HJ (2005) Linear theory for control of nonlinear stochastic systems. _Phys Rev Lett_ 95:200201. 

8. Mitter S, Newton N (2003) A variational approach to nonlinear estimation. _SIAM J Control Opt_ 42:1813–1833. 

9. Todorov E (2006) Linearly-solvable Markov decision problems. _Adv Neural Information Proc Syst_ 19:1369–1376. 

This framework has many potential applications and we hope that the list of examples will grow as other researchers begin to use it. Our current focus is on high-dimensional continuous problems such as those arising in biomechanics and robotics, where the discrete-time continuous-state MDP approximation is particularly promising. It leads to linear integral equations rather than differential equations, resulting in robust numerical methods. Furthermore it is well suited to handle discontinuities due to rigid-body collisions. Initial results using mixture-of-Gaussian approximations to the desirability function are encouraging (11), yet a lot more work remains. 

**ACKNOWLEDGMENTS.** We thank Surya Ganguli, Javier Movellan, and Yuval Tassa for discussions and comments on the manuscript. This work was supported by the National Science Foundation. 

10. Todorov E (2008) General duality between optimal control and estimation. _IEEE Conf Decision Control_ 47:4286–4292. 

11. Todorov E (2009) Eigen-function approximation methods for linearly-solvable optimal control problems, _IEEE Int Symp Adapt Dynam Programm Reinforce Learning_ 2:161–168. 

12. Todorov E (2009) _Classic Maximum Principles and Estimation-Control Dualities for nonlinear Stochastic Systems_ , preprint. 

13. Todorov E (2009) _Compositionality of Optimal Control Laws_ , preprint. 

14. Todorov E (2009) _Efficient Algorithms for Inverse Optimal Control_ , preprint. 

15. Watkins C, Dayan P (1992) Q-learning. _Mach Learn_ 8:279–292. 

16. Kushner H, Dupuis P (2001) _Numerical Methods for Stochastic Optimal Control Problems in Continuous Time_ (Springer, New York). 

17. Bryson A, Ho Y (1969) _Applied Optimal Control_ (Blaisdell Publishing Company, Waltham, MA). 

18. Ng A, Russell S (2000) Algorithms for inverse reinforcement learning. _Int Conf Mach Learn_ 17:663–670. 

19. Liu K, Hertzmann A, Popovic Z (2005) Learning physics-based motion style with nonlinear inverse optimization. _ACM Trans Graphics_ 24:1071–1081. 

Todorov 

PNAS **July 14, 2009** vol. 106 no. 28 **11483** 

