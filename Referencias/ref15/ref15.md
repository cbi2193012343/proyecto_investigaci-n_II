## **Optimal control as a graphical model inference problem** 

**Hilbert J. Kappen** _**·**_ **Vicen¸c G´omez** _**·**_ **Manfred Opper** 

**Abstract** We reformulate a class of non-linear stochastic optimal control problems introduced by Todorov (2007) as a Kullback-Leibler (KL) minimization problem. As a result, the optimal control computation reduces to an inference computation and approximate inference methods can be applied to efficiently compute approximate optimal controls. We show how this KL control theory contains the path integral control method as a special case. We provide an example of a block stacking task and a multi-agent cooperative game where we demonstrate how approximate inference can be successfully applied to instances that are too complex for exact computation. We discuss the relation of the KL control approach to other inference approaches to control. 

**Keywords** optimal control _·_ uncontrolled dynamics _·_ Kullback-Leibler divergence _·_ graphical model _·_ approximate inference _·_ cluster variation method _·_ belief propagation 

Hilbert J. Kappen Donders Institute for Brain Cognition and Behaviour Radboud University Nijmegen 6525 EZ Nijmegen, The Netherlands E-mail: b.kappen@science.ru.nl 

Vicen¸c G´omez Donders Institute for Brain Cognition and Behaviour Radboud University Nijmegen 6525 EZ Nijmegen, The Netherlands E-mail: v.gomez@science.ru.nl 

Manfred Opper Department of Computer Science D-10587 Berlin, TU Berlin, Germany 

E-mail: opperm@cs.tu-berlin.de 

Hilbert J. Kappen et al. 

2 

## **1 Introduction** 

Stochastic optimal control theory deals with the problem to compute an optimal set of actions to attain some future goal. With each action and each state a cost is associated and the aim is to minimize the total future cost. Examples are found in many contexts such as motor control tasks for robotics, planning and scheduling tasks or managing a financial portfolio. The computation of the optimal control is typically very difficult due to the size of the state space and the stochastic nature of the problem. 

The most common approach to compute the optimal control is through the Bellman equation. For the finite horizon discrete time case, this equation results from a dynamic programming argument that expresses the optimal cost-to-go (or value function) at time _t_ in terms of the optimal cost-to-go at time _t_ + 1. For the infinite horizon case, the value function is independent of time and the Bellman equation becomes a recursive equation. In continuous time, the Bellman equation becomes a partial differential equation. 

For high dimensional systems or for continuous systems the state space is huge and the above procedure cannot be directly applied. A common approach to make the computation tractable is a function approximation approach where the value function is parameterized in terms of a number of parameters (Bertsekas and Tsitsiklis, 1996). Another promising approach is to exploit graphical structure that is present in the problem to make the computation more efficient (Boutilier et al., 1995; Koller and Parr, 1999). However, this graphical structure is in general not inherited by the value function, and thus the graphical representation of the value function may not be appropriate. 

In this paper, we introduce a class of stochastic optimal control problems where the control is expressed as a probability distribution _p_ over future trajectories given the current state and where the control cost can be written as a Kullback-Leibler (KL) divergence between _p_ and some interaction terms. The optimal control is given by minimizing the KL divergence, which is equivalent to solving a probabilistic inference problem in a dynamic Bayesian network. The optimal control is given in terms of (marginals of) a probability distribution over future trajectories. The formulation of the control problem as an inference problem directly suggests exact inference methods such as the Junction Tree method (JT) (Lauritzen and Spiegelhalter, 1988) or a number of well-known approximation methods, such as the variational method (Jordan, 1999), belief propagation (BP) (Murphy et al., 1999), the cluster variation method (CVM) or generalized belief propagation (GBP) (Yedidia et al., 2001) or Markov Chain Monte Carlo (MCMC) sampling methods. We refer to this class of problems as KL control problems. 

The class of control problems considered in this paper is identical as in Todorov (2008, 2007, 2009), who shows that the Bellman equation can be written as a KL divergence of probability distributions between two adjacent time slices and that the Bellman equation computes backward messages in a chain as if it were an inference problem. The novel contribution of the present paper is to identify the control cost with a KL divergence instead of making 

Optimal control as a graphical model inference problem 

3 

this identification in the Bellman equation. The immediate consequence is that the optimal control problem _is identical to_ a graphical model inference problem that can be approximated using standard methods. 

We also show how KL control reduces to the previously proposed path integral control problem (Kappen, 2005) when noise is Gaussian in the limit of continuous space and time. This class of control problem has been applied to multi-agent problems using a graphical model formulation and junction tree inference in Wiegerinck et al. (2006, 2007) and approximate inference in van den Broek et al. (2008b,a). In robotics, Theodorou et al. (2009, 2010a,b) has shown the the path integral method has great potential for application. They have compared the path integral method with some state-of-the-art reinforcement learning methods, showing very significant improvements. In addition, they have successful implemented the path integral control method to a walking robot dog. The path integral approach has recently been applied to the control of character animation (da Silva et al., 2009). 

## **2 Control as KL minimization** 

Let _x_ = 1 _, . . . , N_ be a finite set of states, _x[t]_ denotes the state at time _t_ . Denote by _p[t]_ ( _x[t]_[+1] _|x[t] , u[t]_ ) the Markov transition probability at time _t_ under control _u[t]_ from state _x[t]_ to state _x[t]_[+1] . Let _p_ ( _x_[1:] _[T] |x_[0] _, u_[0:] _[T][ −]_[1] ) denote the probability to observe the trajectory _x_[1:] _[T]_ given initial state _x_[0] and control trajectory _u_[0:] _[T][ −]_[1] . 

If the system at time _t_ is in state _x_ and takes action _u_ to state _x[′]_ , there is an associated cost _R_[ˆ] ( _x, u, x[′] , t_ ). The control problem is to find the sequence _u_[0:] _[T][ −]_[1] that minimizes the expected future cost 

**==> picture [296 x 66] intentionally omitted <==**

with the convention that _R_[ˆ] ( _x[T] , u[T] , x[T]_[ +1] _, T_ ) = _R_ ( _x[T] , T_ ) is the cost of the final state and _⟨⟩_ denotes expectation with respect to _p_ . Note, that _C_ depends on _u_ in two ways: through _R_[ˆ] and through the probability distribution of the controlled trajectories _p_ ( _x_[1:] _[T] |x_[0] _, u_[0:] _[T][ −]_[1] ). 

The optimal control is normally computed using the Bellman equation, which results from a dynamic programming argument (Bertsekas and Tsitsiklis, 1996). Instead, we will consider the restricted class of control problems for which _C_ in Equation (1) can be written as a KL divergence. As a particular case, we consider that _R_[ˆ] is the sum of a control dependent term and a state dependent term. We further assume the existence of a ’free’ (uncontrolled) dynamics _q[t]_ ( _x[t]_[+1] _|x[t]_ ), which can be any first order Markov process that assigns zero probability to physically impossible state transitions. 

Hilbert J. Kappen et al. 

4 

We quantify the control cost as the amount of deviation between _p[t]_ ( _x[t]_[+1] _|x[t] , u[t]_ ) and _q[t]_ ( _x[t]_[+1] _|x[t]_ ) in KL sense. Thus, 

**==> picture [323 x 25] intentionally omitted <==**

with _R_ ( _x, t_ ) an arbitrary state dependent control cost. Equation (1) becomes 

**==> picture [267 x 97] intentionally omitted <==**

Note, that _C_ depends on the control _u_ only through _p_ . Thus, minimizing _C_ with respect to _u_ yields: 0 = _[dC] du_[=] _[dC] dp dudp_[, where the minimization with respect] to _p_ is subject to the normalization constraint[�] _x_[1:] _[T][p]_[(] _[x]_[1:] _[T][ |][x]_[0][) = 1. Therefore,] a sufficient condition for the optimal control is to set _[dC] dp_[=][0.][The][result][of] this KL minimization is well known and yields the “Boltzmann distribution” 

**==> picture [320 x 88] intentionally omitted <==**

and the optimal cost 

where _Z_ ( _x_[0] ) is a normalization constant (see Appendix A). In other words, the optimal control solution is the (normalized) product of the free dynamics and the exponentiated costs. It is a distribution that avoids states of high _R_ , at the same time deviating from _q_ as little as possible. Note that since _q_ is a first order Markov process, _p_ in Equation (5) is a first order Markov process as well. 

The optimal control in the current state _x_[0] at the current time _t_ = 0 is given by the marginal probability 

**==> picture [224 x 23] intentionally omitted <==**

This is a standard graphical model inference problem, with _p_ given by Equation (5). Since _ψ_ is a chain, we can compute _p_ ( _x_[1] _|x_[0] ) by backward message 

Optimal control as a graphical model inference problem 

5 

Dynamics: _p[t]_ ( _x[t] |x[t][−]_[1] _, u[t][−]_[1] ) _→_ dynamic programming _→_ Bellman Equation ˆ Cost: _C_ ( _x_[0] _, u_ ) = _R_ Cost-to-go: _J_ ( _x_[0] ) � � _↓ ↓_ restricted class of problems approximate _J ↓ ↓_ Dynamics: _p[t]_ ( _x[t] |x[t][−]_[1] ) _→_ approximate inference _→_ approximation _C_ ( _x_[0] _, p_ ) = _KL_ ( _p||ψ_ ) of optimal _u_ 

**Fig. 1** Overview of the approaches to computing the optimal control. Top left) The general optimal control problem is formulated as a state transition model _p_ that depends on the control (or policy) _u_ and a cost _C_ ( _u_ ) that is the expected _R_[ˆ] with respect to the controlled dynamics _p_ . The optimal control is given by the _u_ that minimizes a cost _C_ ( _u_ ). Top right) The traditional approach is to introduce the notion of cost-to-go or value function _J_ , which satisfies the Bellman equation. The Bellman equation is derived using a dynamic programming argument. Bottom right) For large problems, an approximate representation of _J_ is used to solve the Bellman equation which yields the optimal control. Bottom left) The approach in this paper is to consider a class of control problems for which _C_ is written as a KL divergence. The computation of the optimal control (optimal _p_ ) becomes a statistical inference problem, that can be approximated using standard approximate inference methods. 

passing: 

**==> picture [174 x 56] intentionally omitted <==**

The interpretation of the Bellman equation as message passing for the KL control problems was first established in Todorov (2008). The difference between the KL control computation and the standard computation using the Bellman equation is schematically illustrated in Figure 1. 

The optimal cost, Equation (6), is minus the log partition sum and is the expectation value of the exponentiated state costs[�] _[T] t_ =0 _[R]_[(] _[x][t][, t]_[)][under][the] _uncontrolled_ dynamics _q_ . This is a surprising result, because it means that we have a closed form solution for the optimal cost-to-go _C_ ( _x_[0] _, p_ ) in terms of the known quantities _q_ and _R_ . 

A result of this type was previously obtained in Kappen (2005) for a class of continuous non-linear stochastic control problems. Here, we show that a slight generalization of this problem ( _gai_ ( _x, t_ ) = 1 in Kappen (2005)) is obtained as a special case of the present KL control formulation. Let _x_ denote an _n_ - dimensional real vector with components _xi_ . We define the stochastic dynamics 

**==> picture [260 x 22] intentionally omitted <==**

with _fi_ an arbitrary function, _dξa_ an _m_ -dimensional Gaussian process with covariance matrix _⟨dξadξb⟩_ = _νabdt_ and _ua_ an _m_ -dimensional control vector. 

Hilbert J. Kappen et al. 

6 

The distribution over trajectories is given by 

**==> picture [322 x 30] intentionally omitted <==**

with _f[t]_ = _f_ ( _x[t] , t_ ) and the distribution over trajectories under the uncontrolled dynamics is defined as _q_ ( _x[dt]_[:] _[T] |x_[0] ) = _p_ ( _x[dt]_[:] _[T] |x_[0] _, u_[0:] _[T][ −][dt]_ = 0). 

For this particular choice of _p_ and _q_ , the control cost in Equation (3) becomes (see Appendix B for a derivation) 

**==> picture [337 x 43] intentionally omitted <==**

where _⟨⟩_ denotes expectation with respect to the controlled dynamics _p_ , where the sums become integrals and where we have defined _φ_ ( _x_ ) = _R_ ( _x, T_ ). 

Equations (8) and (10) define a stochastic optimal control problem. The solution for the optimal cost-to-go for this class of control problems can be shown to be given as a so-called path integral, an integral over trajectories, which is the continuous time equivalent of the sum over trajectories in Equation (6). Note, that the cost of control is quadratic in _u_ , but of a particular form with the matrix _ν[−]_[1] in agreement with Kappen (2005). Thus, the KL control theory contains the path integral control method as a particular limit. As is shown in Kappen (2005), this class of problems admits a solution of the optimal cost-to-go as an integral over paths, which is similar to Equation (6). 

## 2.1 Graphical model inference 

In typical control problems, _x_ has a modular structure with components _x_ = _x_ 1 _, . . . , xn_ . For instance, for a multi-joint arm, _xi_ may denote the state of each joint. For a multi-agent system, _xi_ may denote the state of each agent. In all such examples, _xi_ itself may be a multi-dimensional state vector. In such cases, the optimal control computation, Equation (7), is intractable. However, the following assumptions are likely to be true: 

- The uncontrolled dynamics factorizes over components 

**==> picture [124 x 29] intentionally omitted <==**

- The interaction between components has a (sparse) graphical structure _R_ ( _x, t_ ) =[�] _α[R][α]_[(] _[x][α][, t]_[)][with] _[α]_[a][subset][of][the][indices][1] _[, . . . , n]_[and] _[x][α]_[the] corresponding variables. 

Optimal control as a graphical model inference problem 

7 

**==> picture [135 x 31] intentionally omitted <==**

**Fig. 2** Block stacking problem: the objective can be (but is not restricted to) to stack the initial block configuration (left) into a single stack (right) through a sequence of single block moves to adjacent positions (middle). 

Typical examples are multi-agent systems and robot arms. In both cases the dynamics of the individual components (the individual agents and the different joints, respectively) are independent _a priori_ . It is only through the execution of the task that the dynamics become coupled. 

Thus, _ψ_ in Equation (4) has a graphical structure that we can exploit when computing the marginals in Equation (7). For instance, one may use the junction tree (JT) method, which can be more efficient than simply using the backward messages. Alternatively, we can use any of a large number of approximate graphical model inference methods to compute the optimal control. In the following sections, we will illustrate this idea by applying several approximate inference algorithms in two different tasks. 

## **3 Stacking blocks (KL-blocks-world)** 

Consider the example of piling blocks into a tower. This is a classic AI planning task (Russell et al., 1996). It will be instructive to see how a variant of this problem is solved as a stochastic control problem, As we will see, the optimal control solution will in general be a mixture over several actions. We define the KL-blocks-world problem in the following way: let there be _n_ possible block locations on the one dimensional ring (line with periodic boundaries) as in Figure 2, and let _x[t] i[≥]_[0] _[, i]_[ = 1] _[, . . . , n, t]_[ = 0] _[, . . . , T]_[denote][the][height][of][stack] _[i]_ at time _t_ . Let _m_ be the total number of blocks. 

At iteration _t_ , we allow to move one block from location _k[t]_ and move it to a neighboring location _k[t]_ + _l[t]_ with _l[t]_ = _−_ 1 _,_ 0 _,_ 1 (periodic boundary conditions). Given _k[t] , l[t]_ and the old state _x[t][−]_[1] , the new state is given as 

**==> picture [198 x 13] intentionally omitted <==**

**==> picture [210 x 14] intentionally omitted <==**

and all other stacks unaltered. We use the uncontrolled distribution _q_ to implement these allowed moves. For the purpose of memory efficiency, we introduce auxiliary variables _s[t] i_[=] _[−]_[1] _[,]_[ 0] _[,]_[ 1][that][indicate][whether][the][stack][height] _[x][i]_[is] decremented, unchanged or incremented, respectively. The uncontrolled dy- 

Hilbert J. Kappen et al. 

8 

**==> picture [226 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
k [1] k [2] k [T]<br>l [1] l [2] l [T]<br>s [1] 1 s [2] 1 s [T] 1<br>\ \ e x [1] 1 x [2] 1 x [T] 1<br>\ a<br>\\N\ \\| s [1] i \ \\\\N)|\ q s [2] i : \\ \Xé\| \ |vo s [T] i |<br>|<br>\\s \ \<br>x [1] i x [2] i x [T] i<br>\\we \AL\\ XYas \\\\:<br>\\ 3 \i<br>\ s [1] n Na, \\ s [2] n Ned| s [T] n<br>=<br>Na, x [1] n eo x [2] n x [T] n<br>**----- End of picture text -----**<br>


**Fig. 3** Block stacking problem: Graphical model representation as a dynamic Bayesian network. Time runs horizontal and stack positions vertical. At each time, the transition probability of _x[t]_ to _x[t]_[+1] is a mixture over the variables _k[t] , l[t]_ . The initial state is “clamped” to a given configuration by conditioning on the variables _x_[1] . To force a goal state or final configuration, the final state _x[T]_ can also be “clamped” (see Section 3.1.1). 

namics _q_ becomes _q_ ( _k[t]_ ) = _U_ (1 _, . . . , n_ ), _q_ ( _l[t]_ ) = _U_ ( _−_ 1 _,_ 0 _,_ +1), 

**==> picture [204 x 77] intentionally omitted <==**

where _U_ ( _·_ ) denotes the uniform distribution. The transition from _x[t][−]_[1] to _x[t]_ is a mixture over the values of _k[t] , l[t]_ : 

**==> picture [281 x 80] intentionally omitted <==**

Note, that there are combinations of _xi[t][−]_[1] and _s[t] i_[that are forbidden: we cannot] remove a block from a stack of size zero ( _x[t] i[−]_[1] = 0 and _s[t] i_[=] _[ −]_[1) and we cannot] move a block to a stack of size _m_ ( _x[t] i[−]_[1] = _m_ and _s[t] i_[=][1).][If][we][restrict][the] values of _x[t] i_[and] _[x][t] i[−]_[1] in the last line above to 0 _, . . . , m_ these combinations are automatically forbidden. 

Figure 3 shows the graphical model associated with this representation. Notice that the graphical structure for _q_ is efficient compared to the naive 

Optimal control as a graphical model inference problem 

9 

implementation of _q_ ( _x[t] |x[t][−]_[1] ) as a full table. Whereas the joint table requires _m[n]_ entries, the graphical model implementation requires _Tn_ tables of sizes _n×_ 3 _×_ 3 for _p_ ( _s[t] |k[t] , l[t]_ ) and _n×n×_ 3 for _p_ ( _x[t] |x[t][−]_[1] _, s[t]_ ). In addition, the graphical structure can be exploited by efficient approximate inference methods. 

Finally, a possible state cost can be defined as the entropy of the distribution of blocks: 

**==> picture [223 x 24] intentionally omitted <==**

with _λ_ a positive number to indicate the strength. Since[�] _i[x][i]_[is][constant][(no] blocks are lost), the minimum entropy solution puts all blocks on one stack (if enough time is available). The control problem is to find the distribution _p_ that minimizes _C_ in Equation (3). 

## 3.1 Numerical results 

In the next section, we consider two particular problems. First, we are interested in finding a sequence of actions that, starting in a given initial state _x_[0] , reach a given goal state _x[T]_ , without state cost. Then we consider the case of entropy minimization, with no defined goal state and nonzero state cost. 

## _3.1.1 Goal state and λ_ = 0 

Figure 4 shows a small example where the planning task is to shift a tower composed of four blocks which initially is at position 1 to the final position 3. 

To find the KL control we first condition the model both on the initial state and the final state variables by “clamping” all variables _x_[1] and _x[T]_ . The KL control solution is obtained by computing for _t_ = 1 _, . . . , T_ the marginal _p_ ( _k[t] , l[t] |x[t][−]_[1] ). In this case, we can find the exact solution via the junction tree (JT) algorithm (Lauritzen and Spiegelhalter, 1988; Mooij, 2010). The _k[t] , l[t]_ is obtained by taking the MAP state of _p_ ( _k[t] , l[t] |x[t][−]_[1] ) breaking ties at random, which results in a new state _xt_ . 

These probabilities _p_ ( _k[t] , l[t] |x[t][−]_[1] ) are shown in Figure 4b. Notice that the symmetry in the problem is captured in the optimal control, which assigns equal probability when moving the first block to left or right (Figure 4b,c, t=1). Figure 4d shows the strategy resulting from the MAP estimate, which first unpacks the tower at position 1 leaving all four locations with one block at _t_ = 4, and then re-builds it again at the goal position 3. 

For larger instances, the JT method is not feasible because of too large tree widths. For instance, to stack 4 blocks on 6 locations within a horizon of 11, the junction tree has a maximal width of 12, requiring about 15 Gbytes of memory. We can nevertheless obtain approximate solutions using different approximate inference methods. In this work, we use the belief propagation algorithm (BP) and a generalization known as the Cluster Variation method 

Hilbert J. Kappen et al. 

10 

**==> picture [164 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Initial state Goal state<br>6 6<br>4 4<br>2 2<br>0 0<br>1 2 3 4 1 2 3 4<br>(b) t = 1 n t = 2 t = 3 n t = 4<br>2 2 2 2<br>4 PULLS 4 4 4<br>−1 0 1 −1 0 1 −1 0 1 −1 0 1<br>l l l l<br>t = 5 t = 6 t = 7 t = 8<br>2 2 2 2<br>4 LS 4 4 4<br>−1 0 1 −1 0 1 −1 0 1 −1 0 1<br>(c) l l l l<br>1<br>2<br>3<br>4<br>0 1 2 3 4 5 6 7 8<br>(d) T<br>1<br>2<br>3<br>4<br>0 1 2 3 4 5 6 7 8<br>T<br>m m<br>k k k k<br>k k k k<br>x<br>xr<br>**----- End of picture text -----**<br>


**Fig. 4** Control for the KL-blocks-world problem with end-cost: example with _m_ = 4 _, n_ = 4 and _T_ = 8. **(a)** Initial and goal states. **(b)** Probability of action _p_ ( _k[t] , l[t] |x[t][−]_[1] ) for each time step _t_ = 1 _. . . T_ . **(c)** Expected value _⟨x[t] i[⟩][, i]_[=][1] _[, . . . , n]_[given][the][initial][position][and][desired] final position and **(d)** the MAP solution for all times using a gray scale coding with white coding for zero and darker colors coding for higher values. 

**==> picture [198 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
% BP solved instances cpu−time CVM (seconds)<br>1<br>n = 4<br>n = 6<br>n = 8 103<br>0.75<br>n = 10<br>0.5 102<br>0.25<br>101<br>0<br>10 15 20 10 15 20<br>m m<br>**----- End of picture text -----**<br>


**Fig. 5** Control for the KL-blocks-world problem with end-cost: results on approximate inference using random initial and goal states. **(Left)** percent of instances where BP converges for all _t_ = 1 : _T_ as a function of _m_ for different values of _n_ . **(Right)** CPU-time required for CVM to find a correct plan for different values of _n, m_ . _T_ was set to _⌈[m]_ 4 _[·][n][⌉]_[.][We][run][50] instances for each pair ( _m, n_ ). 

Optimal control as a graphical model inference problem 

11 

**==> picture [307 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
t = 0 t = 1 t = 2 t = 3 t = 4 t = 5 t = 6 t = 7 t = 8 t = 9<br>n = 8 m = 40<br>t = 10 t = 11 t = 12 t = 13 t = 14 t = 15 t = 16 t = 17 t = 18 t = 19<br>t = 20 t = 21 t = 22 t = 23 t = 24 t = 25 t = 26 t = 27 t = 28 t = 29<br>t = 30 t = 31 t = 32 t = 33 t = 34 t = 35 t = 36 t = 37 t = 38 t = 39<br>t = 40 t = 41 t = 42 t = 43 t = 44 t = 45 t = 46 t = 47 t = 48 t = 49<br>t = 50 t = 51 t = 52 t = 53 t = 54 t = 55 t = 56 t = 57 t = 58 t = 59<br>t = 60 t = 61 t = 62 t = 63 t = 64 t = 65 t = 66 t = 67 t = 68<br>**----- End of picture text -----**<br>


**Fig. 6** Example of a large block stacking instance without end cost. _n_ = 8 _, m_ = 40 _, T_ = 80 _, λ_ = 10 using CVM. 

(CVM). We briefly summarize the main idea of the CVM method in Appendix C. We use the minimal cluster size, that is, the outer clusters are equal to the interaction potentials _ψ_ as shown in the graphical model Figure 3. 

To compute the sequence of actions we follow again a sequential approach. Figure 5 shows results using BP and CVM. For _n_ = 4, BP converges fast and finds a correct plan for all instances. For larger _n_ , BP fails to converge, more or less independently of _m_ . Thus, BP can be applied successfully to small instances only. Conversely, CVM is able to find a correct plan in all run instances, although at the cost of more CPU time, as Figure 5 shows. The variance in the CPU error bars is explained by the randomness in the number of actual moves required to solve each instance, which is determined by the initial and goal states. 

## _3.1.2 No goal state and λ >_ 0 _: entropy minimization_ 

We now consider the problem without conditioning on _x[T]_ and _λ >_ 0. Although this may seem counter intuitive, removing the end constraint in fact makes this problem harder, as the number of states that have significant probability for large _t_ is much larger. BP is not able to produce any reliable result for this problem. We applied CVM to a large block stacking problem with _n_ = 8 _, m_ = 40 _, T_ = 80 and _λ_ = 10. We use again the minimal cluster size and the double loop method of Heskes et al. (2003). The results are shown in Figure 6. 

Hilbert J. Kappen et al. 

12 

The computation time was approximately 1 hour per _t_ iteration and memory use was approximately 27 Mb. This instance was too large to obtain exact results. We conclude that, although the CPU time is large, the CVM method is capable to yield an apparently accurate control solution for this large instance. 

## **4 Multi Agent cooperative game (KL-stag-hunt)** 

In this section we consider a variant of the stag hunt game, a prototype game of social conflict between personal risk and mutual benefit (Skyrms, 2004). The original two-player stag hunt game proceeds as follows: there are two hunters and each of them can choose between hunting hare or hunting stag, without knowing in advance the choice of the other hunter. The hunters can catch a hare on their own, giving them a small reward. The stag has a much larger reward, but it requires both hunters to cooperate in catching it. 

**Table 1** Two-player stag hunt payoff matrix example: rows and columns indicate actions of one and the other player respectively. The payoff describes the reward for each hunter. For instance, if both go for the stag, they both get a reward of 3. If one hunter goes for the stag and the other for the hare, they get a reward of 0 and 1 respectively. 

||Stag|Hare|
|---|---|---|
|Stag<br>Hare|**3**_,_**3**<br>1_,_0|0_,_1<br>**1**_,_**1**|



Table 1 displays a possible payoff matrix for a stag hunt game. It shows that both stag hunting and hare hunting are _Nash equilibria_ , that is, if the other player chooses stag, it is best to choose stag ( _payoff_ equilibrium, top-left), and if the other player chooses hare, it is best to choose hare ( _risk-dominant_ equilibrium, bottom-right). It is argued that these two possible outcomes makes the game socially more interesting, than for example the _prisoners dilemma_ , which has only one Nash equilibrium. The stag hunt allows for the study of cooperation within social structures (Skyrms, 1996) and for studying the collaborative behavior of multi-agent systems (Yoshida et al., 2008). 

We define the KL-stag-hunt game as a multi-agent version of the original stag hunt game where _M_ agents live in a grid of _N_ locations and can move to adjacent locations on the grid. The grid also contains _H_ hares and _S_ stags at certain fixed locations. Two agents can cooperate and catch a stag together with a high payoff _Rs_ . Catching a stag with more than two agents is also possible, but it does not increase the payoff. The agents can also catch a hare individually, obtaining a lower payoff _Rh_ . The game is played for a finite time _T_ and at each time-step all the agents perform an action. The optimal strategy is thus to coordinate pairs of agents to go for different stags. 

Formally, let _x[t] i_[=][1] _[, . . . , N, i]_[=][1] _[, . . . , M, t]_[=][1] _[, . . . , T]_[denote][the][position] of agent _i_ at time _t_ on the grid. Also, let _sj_ = 1 _, . . . , N, j_ = 1 _, . . . , S_ , and _hk_ = 1 _, . . . , N, k_ = 1 _, . . . , H_ denote the positions of the _j_ th stag and the _k_ th 

Optimal control as a graphical model inference problem 

13 

hare respectively. We define the following state dependent reward as: 

**==> picture [261 x 32] intentionally omitted <==**

where _I{·}_ denotes the indicator function. The first term accounts for the agents located at the position of a hare. The second one accounts for the rewards of the stags, which require that at least two agents to be on the same location of the stag. Note that the reward for a stag is not increased further if more than two agents go for the same stag. Conversely, the reward corresponding to a hare is proportional to the number of agents at its position. 

The uncontrolled dynamics factorizes among the agents. It allows an agent to stay on the current position or move to an adjacent position (if possible) with equal probability, thus performing a random walk on the grid. Consider the state variables of an agent in two subsequent time-steps expressed in Cartesian coordinates, _x[t] i_[=] _[ ⟨][l, m][⟩][, x][t] i_[+1] = _⟨l[′] , m[′] ⟩_ . We define the following function: 

**==> picture [289 x 93] intentionally omitted <==**

that evaluates to one if the agent does not move (first condition), or if it moves left, down, right, up (subsequent conditions) inside the grid boundaries. The uncontrolled dynamics for one agent can be written as conditional probabilities after proper normalization: 

**==> picture [239 x 26] intentionally omitted <==**

and the joint uncontrolled dynamics become: 

**==> picture [119 x 30] intentionally omitted <==**

Since we are interested in the final configuration at end time _T_ , we set the state dependent path cost to zero for _t_ = 1 _, . . . , T −_ 1 and to exp � _− λ_[1] _[R]_[(] _[x][T]_[ )] � for the end time. 

To minimize _C_ in Equation (3), exact inference in the joint space can be done by backward message passing, using the following equations: 

**==> picture [268 x 49] intentionally omitted <==**

Hilbert J. Kappen et al. 

14 

**==> picture [219 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ = 10, logZ = 0.06 λ = 0.1, logZ = 93<br>5 5<br>4 4<br>3 3<br>2 2<br>1 1<br>1 2 3 4 5 1 2 3 4 5<br>**----- End of picture text -----**<br>


**Fig. 7** Exact inference KL-stag-hunt: Two hunters in a small grid. There are four hares at each corner of the grid (small diamonds) and one stag in the middle (big diamond). Initial positions of the hunters are denoted by small circles. One hunter is close to a hare and the other is at the same distance of the stag and two hares. Final positions are denoted by asterisks. The optimal paths are drawn in blue and red (Color online). ( **Left** ) For _λ_ = 10, the optimal control is risk dominant, and hunters go for the hares. ( **Right** ) For _λ_ = 0 _._ 1, the payoff dominant control is optimal and hunters cooperate. _N_ = 25 _, T_ = 4 _, Rs_ = _−_ 10 and _Rh_ = _−_ 2. 

and the desired marginal probabilities can be obtained from the _β_ -messages: 

**==> picture [238 x 12] intentionally omitted <==**

To illustrate this game, we consider a small 5 _×_ 5 grid with two hunters and apply equations (17) and (18). There are four hares at each corner of the grid and one stag in the middle. The initial positions of the hunters are selected in a way that one hunter is close to a hare and the other is at the same distance of the stag and two hares. Starting from the initial fixed state _x_[1] , we select the next state according to the most probable state from _p_ ( _x[t] i_[+1] _|x[t] i_[)][until][the] end time. We break ties randomly. Figure 7 shows one resulting trajectory for two values of _λ_ . 

For high values of _λ_ (left plot), each hunter catches one of the hares. In this case, the cost function is dominated by KL term. For small enough values of _λ_ (right plot), both hunters cooperate to catch the stag. In this case, the state cost, function _R_ ( _x[T]_ ), governs the optimal control cost. Thus _λ_ can be seen as a parameter that controls whether the optimal strategy is risk dominant or payoff dominant. 

Note that computing the exact solution using this procedure becomes infeasible even for small number of agents, since the joint state space scales as _N[M]_ . In the next section, we show a more efficient representation using a factor graph for which approximate inference is tractable. 

Optimal control as a graphical model inference problem 

15 

**==> picture [264 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
exp � − λ [1] [R] �<br>ψR<br>x [1] 1 ψq x [1] 1 ψq x [T] 1 [ −] [1] ψq x [T] 1<br>x [1] 2 ψq x [2] 2 ψq x [T] 2 [ −] [1] ψq x [T] 2<br>x [1] M ψq x [2] M ψq x [T] M [ −] [1] ψq x [T] M<br>**----- End of picture text -----**<br>


**Fig. 8** Factor graph representation of the KL-stag-hunt problem. Circles denote variable nodes (states of the agents at a given time-step) and squares denote factor nodes. There are two types of factor nodes: the ones corresponding to the uncontrolled dynamics _ψq_ and the one corresponding to the state cost _ψR_ . Initial configuration in gray denotes the states “clamped” to an initial given value. Despite being a tree, exact inference and approximate inference are intractable in this model due to the complex factor _ψR_ . 

## 4.1 Graphical model for the KL-stag-hunt game 

The corresponding graphical model of the KL-stag-hunt game is depicted in Figure 8 as a factor graph. Since the uncontrolled dynamics factorizes over the agents, the joint state can be split in different variable nodes. Note that since there is only state cost at the end time, the graphical model becomes a tree. However, the factor node associated to the state cost function _ψR_ ( _x[T]_ ) := exp( _− λ_[1] _[R]_[(] _[x][T]_[ ))][involves][all][the][agent][states,][which][still][makes][the][problem] intractable. Even approximate inference algorithms such as BP can not be applied, since messages from _ψR_ to one of the state variables _x[T] i_[would require] a marginalization involving a sum of ( _N −_ 1) _[M]_ terms. 

However, we can exploit the particular structure of that factor by decomposing it in smaller factors defined on small sets of (at most three) auxiliary variables of small cardinality. This transformation becomes intuitive once the graphical model representation for the problem is identified. The procedure defines indicator functions for the allowed configurations which are weighted according to the corresponding cost. Figure 9 illustrates the procedure for the case of one stag. 

1. First, we add _H × M_ factors _ψhk_ ( _x[T] i_[),][defined][for][each][hare][location] _[h][k]_ and each agent variable _x[T] i_[.][These][factors][account][for][the][hare][costs:] 

**==> picture [176 x 31] intentionally omitted <==**

2. Second, we add factors _ψsj_ ( _x[T] i[, d][i,j]_[)][for][each][stag] _[j]_[defined][on][each][state] variable _x[T] i_[and][new][introduced][binary][variables] _[d][i,j]_[= 0] _[,]_[ 1.][These][factors] 

Hilbert J. Kappen et al. 

16 

**==> picture [159 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
exp � − λ [1] [R] �<br>x [T] 1 ψs 1 d 1 , 1<br>ψh 1<br>ψhH<br>x [T] 2 ψs 1 d 2 , 1 ψr 1 u 1 , 1<br>ψh 1<br>ψhH<br>x [T] 3 ψs 1 d 3 , 1 ψr 2 u 2 , 1<br>ψh 1<br>ψhH<br>x [T] M ψs 1 dM, 1 ψrM − 1 uM − 1 , 1 ψ rM<br>ψh 1<br>ψhH<br>**----- End of picture text -----**<br>


**Fig. 9** Decomposition of the complex factor _ψR_ into simple factors involving at most three variables of small cardinality. Each state variable is linked to _H_ factors corresponding to the hares locations. For each stag there is a chain of factors _ψri , i_ = 1 _, . . . , M −_ 1 which evaluates to one for the allowed configurations and to zero otherwise. Factor _ψrM_ weights the configuration of having zero, one or more agents being at the stag position (figure shows the case of one stag only). 

evaluate to one when variable _di,j_ takes the value of a Kronecker _δ_ of the agent’s state _x[T] i_[and][the][position][of][a][stag] _[s][j]_[,][and][zero][otherwise:] 

**==> picture [153 x 19] intentionally omitted <==**

3. Third, for each stag, we introduce a chain of factors that involve the binary variables _di,j_ and additional variables _ui,j_ = 0 _,_ 1 _,_ 2. The new variables _ui,j_ encode whether the stag _j_ has zero, one, or more agents after considering the ( _i_ + 1)th agent. The new factors are: 

**==> picture [298 x 132] intentionally omitted <==**

Optimal control as a graphical model inference problem 

17 

**==> picture [253 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ = 10 λ = 0.1<br>20 20<br>15 15<br>10 10<br>5 5<br>1 1<br>1 5 10 15 20 1 5 10 15 20<br>**----- End of picture text -----**<br>


**Fig. 10** Approximate inference KL-stag-hunt: Control obtained using BP for _M_ = 10 hunters in a large grid. See Figure 7 for a description of the symbols. ( **Left** ) Risk dominant control is obtained for _λ_ = 10, where all hunters go for a hare. ( **Right** ) Payoff dominant control is obtained for _λ_ = 0 _._ 1. In this case, all hunters cooperate to capture the stags except the ones on the upper-right corner, who are too far away from the stag to reach it in _T_ = 10 steps. Their optimal choice is to go for a hare. _N_ = 400 _, S_ = _M/_ 2 _, Rs_ = _−_ 10 _, H_ = 2 _M_ and _Rh_ = _−_ 2. 

4. Finally, we define factors _ψrM_ that weight the allowed configurations: 

**==> picture [209 x 31] intentionally omitted <==**

The original factor can be rewritten marginalizing the auxiliary variables _di,j, ui,j_ over the product of the previous factors _ψsj , ψhk , ψri_ : 

**==> picture [354 x 146] intentionally omitted <==**

where for clarity of notation we have grouped the factors related to the stags and hares in _ψS_ ( _x[T]_ ) and _ψH_ ( _x[T]_ ), respectively. 

The extended factor graph is tractable since it involves factors of no more than three variables of small cardinality. Note that this transformation can also be applied if additional state costs are incorporated at each time-step 

Hilbert J. Kappen et al. 

18 

_ψR_ ( _x[t]_ ) = 0 _, t_ = 1 _, . . . , T_ . However, such a representation is not of practical interest, since it complicates the model unnecessarily. 

Finally, note that the tree-width of the extended graph still grows fast with the number of agents _M_ because variables _di,j_ and _ui,j_ are coupled. Thus, exact inference using the JT algorithm is still possible on small instances only. 

## 4.2 Approximate inference of the KL-stag-hunt problem 

In this section we analyze large systems for which exact inference is not possible using the JT algorithm. The belief propagation (BP) algorithm is an alternative approximate algorithm that we can run on the previously described extended factor graph. 

We use the following setup: for a fixed number of agents _M_ , we set the number of stags _H_ = 2 _M_ and the number of hares _S_ = _[M]_ 2[.][Their][locations,] as well as the initial states _x_[1] are chosen randomly and non-overlapping. We then construct a factor graph with initial states “clamped” to _x_[1] and build instance-dependent factors _ψsj_ and _ψhk_ . We run BP using sequential updates of the messages. If BP converges in less than 500 iterations, the optimal trajectories of the agents are computed using the estimated marginals (factor beliefs) for _ψq_ ( _x[t]_[+1] _|x[t]_ ) after convergence. Starting from _x_[1] , we select the next state according to the most probable state from _pBP_ ( _x[t] i_[+1] _|x[t] i_[)][until][the][end][time.] We break ties randomly. We analyze the system as a function of parameter _λ_ for a several number of realizations. 

The global observed behavior is qualitatively similar to the one of a small system: for _λ_ very large, a risk-dominant control is obtained and for _λ_ small enough, payoff control dominates. This is behavior is illustrated in Figure 10, where an example for _λ_ = 10 and _λ_ = 0 _._ 1 are shown. We can thus conclude that BP provides an efficient and good approximation for large systems where exact inference is not feasible. 

To characterize the solutions, we compute the approximated expected cost as in (6), that is _−_ log _ZBP_ . We observe that for large systems that quantity changes abruptly at _λ ≈_ 1. Qualitatively, the optimal control obtained on the boundary between risk-dominant and payoff-dominant strategies differs maximally between individual instances and strongly depends on the initial configuration. This suggests a phase transition phenomenon typical of complex physical systems, in this case separating the two kind of optimal behaviors, where _λ_ plays the role of a “temperature” parameter. 

Figure 11 shows this effect. The left plot shows the derivative of the expected approximated cost averaged over 20 instances. The curve becomes sharper and its maximum gets closer to _λ_ = 1 for larger systems. Error bars of the number of iterations required for convergence is shown on the right. The number of BP iterations quickly increases as we decrease _λ_ , indicating that the solution for which agents cooperate is more complex to obtain. For _λ_ very small, BP may fail to converge after 500 iterations. 

Optimal control as a graphical model inference problem 

19 

**==> picture [237 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
∂ −log ZBP/ ∂ λ # BP iterations<br>3<br>10 10<br>Payoff dominant Risk dominant M = 4<br>M = 10<br>2<br>5 10<br>1<br>0 10<br>−1 0 1 −1 0 1<br>10 10 10 10 10 10<br>λ λ<br>**----- End of picture text -----**<br>


**Fig. 11** Approximate inference KL-stag-hunt: ( **Left** ) Change in the expected cost with respect to _λ_ as a function of _λ_ for _⟨M_ = 4 _, N_ = 100 _⟩_ and _⟨M_ = 10 _, N_ = 225 _⟩_ . The curve becomes sharper and its maximum gets closer to _λ_ = 1 for larger systems, suggesting a phase transition phenomenon between the risk dominant and the payoff dominant regimes. ( **Right** ) Number of BP iterations required for convergence as a function of _λ_ . Results are averages over 20 runs with random initial states. _Rs_ = _−_ 10 _, Rh_ = _−_ 2 and _T_ = 10. 

## **5 Related work** 

The idea to treat a control problem as an inference problem has a long history. The best known example is the linear quadratic control problem, which is mathematically equivalent to an inference problem and can be solved as a Kalman smoothing problem (Stengel, 1994). The key insight is that the value function that is iterated in the Bellman equation becomes the (log of the) backward message in the Kalman filter. The exponential relation was generalized in Kappen (2005) for the non-linear continuous space and time (Gaussian case) and in Todorov (2007) for a class of discrete problems. 

There is a line of research on how to compute optimal action sequences in influence diagrams using the idea of probabilistic inference (Cooper, 1988; Tatman and Shachter, 1990; Shachter and Peot, 1992). Although this technique can be implemented efficiently using the junction tree approach for single decisions, the approach does not generalize in an efficient way to optimal decisions, in the expected-reward sense, in multi-step tasks. The reason is that the order in which one marginalizes and optimizes strongly affects the efficiency of the computation. For a Markov decision process (MDP) there is an efficient solution in terms of the Bellman equation[1] . For a general influence diagram, the marginalization approach as proposed in Cooper (1988); Tatman and Shachter (1990); Shachter and Peot (1992) will result in an intractable optimization problem over _u_[0:] _[T][ −]_[1] that cannot be solved efficiently (using dynamic programming), unless the influence diagram has an MDP structure. 

> 1 Here we mean by efficient, that the sum or min over a sequence of states or actions can be performed as a sequence of sums or mins over states. 

Hilbert J. Kappen et al. 

20 

The KL control theory shares similarities with work in reinforcement learning for policy updating. The notion of KL divergence appears naturally in the work of Bagnell and Schneider (2003) who proposes an information geometric approach to compute the natural policy gradient (for small step sizes). This idea is further developed into an Expectation-Maximization (EM) type algorithm (Dayan and Hinton, 1997) in recent work (Peters et al., 2010; Kober and Peters, 2011) using a relative entropy term. The KL divergence acts here as a regularization that weights the relative dependence of the new policy on the data observed and the old policy, respectively. 

It is interesting to compare the the notion of free energy in continuous-time dynamical systems with Gaussian noise considered in Friston et al. (2009) with the path integral formalism of Kappen (2005), which is a special case of KL control theory. Friston et al. (2009) advocate the optimization of free energy as a guiding principle to describe behavior of agents. The main difference between the KL control theory and Friston’s free energy principle is that in KL control theory, the KL divergence plays the role of an expected future cost and its optimization yields a (time dependent) optimal control trajectory, whereas Friston’s free energy computes a control that yields a time-independent equilibrium distribution, corresponding to the minimal free energy. Friston’s free energy formulation is obtained as a special case of KL control theory when the dynamics and the reward/cost is time-independent and the horizon time is 

The KL control approach proposed in this paper also bears some relation to the EM approach of Toussaint and Storkey (2006), who consider the discounted reward case with 0,1 rewards. The posterior can be considered a mixture over times at which rewards are incorporated. For an homogeneous Markov process and time independent costs, the backward message passing can be effectively done in a single chain and not the full mixture distribution needs to be considered. We can compare the EM approach of Toussaint and Storkey (2006) (TS) and the KL control approach (KL): 

- The TS approach is more general than the KL approach, in the sense that the reward considered in TS is an arbitrary function of state and action _R_ ( _x, u_ ), whereas the reward considered in KL is a sum of a state dependent term _R_ ( _x_ ) and a KL divergence. 

- The KL approach is significantly more efficient than the TS approach. In the TS approach, the backward messages are computed for a fixed policy _π_ (E-step), from which an improved policy is computed (M-step). This procedure is iterated until convergence. In the KL approach, the backward messages give the optimal control directly, with no further need for iteration. 

- In addition, the KL approach is more efficient than the TS approach for time-dependent problems. Using the TS approach for time-dependent problems makes the computation a factor _T_ more time-consuming than for the time-independent case, since all mixture components must be computed. 

Optimal control as a graphical model inference problem 

21 

The complexity of the KL control approach does not depend on whether the problem is time-dependent or not. 

**–** The TS and KL approach optimize with respect to a different quantity. The TS approach writes the state transition _p_ ( _y|x_ ) =[�] _u[p]_[(] _[y][|][x, u]_[)] _[π]_[(] _[u][|][x]_[)] and optimizes with respect to _π_ . The KL approach optimizes the state transition probability _p_ ( _y|x_ ) directly either as a table or in a parametrized way. 

## **6 Discussion** 

In this paper, we have shown the equivalence of a class of stochastic optimal control problems to a graphical model inference problem. As a result, exact or approximate inference methods can directly be applied to the intractable stochastic control computation. The class of KL control problems contains interesting special cases such as the continuous non-linear Gaussian stochastic control problems introduced in Kappen (2005), discrete planning tasks and multi-agent games, as illustrated in this paper. 

We notice, that there exist many stochastic control problems that are outside of this class. In the basic formulation of Equation (1), one can construct control problems where the functional form of the controlled dynamics _p[t]_ ( _x[t]_[+1] _|x[t] , u[t]_ ) is given as well as the cost of control _R_ ( _x[t] , u[t] , x[t]_[+1] _, t_ ). In general, there may then not exist a _q[t]_ ( _x[t]_[+1] _|x[t]_ ) such that Equation (2) holds. 

In this paper, we have considered the model based case only. The extension to the model free case would require a sampling based procedure. See Bierkens and Kappen (2012) for initial work in this direction. 

We have demonstrated the effectiveness of approximate inference methods to compute the approximate control in a block stacking task and a multi-agent cooperative task. 

For the KL-blocks-world, we have shown that an entropy minimization task is more challenging than stacking blocks at a fixed location (goal state), because the control computation needs to find out where the optimal location is. Standard BP does not give any useful results if no goal state was specified, but apparently good optimal control solutions were obtained using generalized belief propagation (CVM). We found that the marginal computation using CVM is quite difficult compared to other problems that have been studied in the past (Albers et al., 2007), in the sense that relatively many inner loop iterations were required for convergence. One can improve the CVM accuracy, if needed, by considering larger clusters (Yedidia et al., 2005) as has been demonstrated in other contexts (Albers et al., 2006), at the cost of more computational complexity. 

We have given evidence that the KL control formulation is particularly attractive for multi-agent problems, where _q_ naturally factorizes over agents and where interaction results from the fact that the reward depends on the state of more than one agent. A first step in this direction was already made in Wiegerinck et al. (2006); van den Broek et al. (2008a). In this case, we 

Hilbert J. Kappen et al. 

22 

have considered the KL-stag-hunt game and shown that BP provides a good approximation and allows to analyze the behavior of large systems, where exact inference is not feasible. 

We found that, if the game setting strongly penalizes large deviations from the baseline (random) policy, the coordinated solution is sub-optimal. That means that the optimal solution distributes the agents among the different hares rather than bringing them jointly to the stags (risk-dominant regime). On the contrary, if the agents are not constrained by deviating too much from the baseline policy to maximize _⟨R⟩_ , the coordinated solution becomes optimal (payoff dominant regime). We believe that this is an interesting result, since it provides a explanation of the emergence of cooperation in terms of an effective temperature parameter _λ_ . 

## _Acknowledgments_ 

We would like to thank anonymous reviewers for helping on improving the manuscript, Kees Albers for making available his sparse CVM code, Joris Mooij for making available the libDAI software and Stijn Tonk for useful discussions. The work was supported in part by the ICIS/BSIK consortium. 

## **A Boltzmann distribution** 

Consider the KL divergence between a normalized probability distribution _p_ ( _x_ ) and some positive function _ψ_ ( _x_ ): 

**==> picture [92 x 22] intentionally omitted <==**

_C_ is a function of the distribution _p_ . We compute the distribution that minimizes _C_ with respect to _p_ subject to normalization[�] _x[p]_[(] _[x]_[) = 1][by][adding][a][Lagrange][multiplier:] 

**==> picture [126 x 49] intentionally omitted <==**

Setting the derivative equal to zero yields _p_ ( _x_ ) = _ψ_ ( _x_ ) exp( _−β −_ 1) = _ψ_ ( _x_ ) _/Z_ , where we have defined _Z_ = exp( _β_ + 1). The normalization condition[�] _x[p]_[(] _[x]_[) = 1][fixes] _[Z]_[=][ �] _x[ψ]_[(] _[x]_[).] Substituting the solution for _p_ in the cost _C_ yields _C_ = _−_ log _Z_ . 

Optimal control as a graphical model inference problem 

23 

## **B Relation to continuous path integral model** 

We write _p_ ( _x[′] |x_ ) = _N_ ( _x[′] |x_ + _f_ ( _x, t_ ) _dt_ + _g_ ( _x, t_ ) _u_ ( _x, t_ ) _dt, Ξdt_ ) with _Ξ_ ( _x, t_ ) = _g_ ( _x, t_ ) _νg_ ( _x, t_ ) _[T]_ in Equation (9) as 

**==> picture [301 x 71] intentionally omitted <==**

with _x_ ˙ = ( _x[′] − x_ ) _/dt_ . In order to make the link to Equation (3) we compute 

**==> picture [338 x 92] intentionally omitted <==**

**==> picture [237 x 85] intentionally omitted <==**

In the limit of _dt →_ 0 the KL divergence between _p_ and _q_ becomes 

**==> picture [179 x 21] intentionally omitted <==**

in agreement with Equation (10). 

## **C Cluster Variation Method** 

In this appendix, we give a brief summary of the CVM method and the double loop approach. For a more complete description see Yedidia et al. (2001); Kappen and Wiegerinck (2002); Heskes et al. (2003). 

The cluster variation method replaces the probability distribution _p_ ( _x_ ) in the minimization Equation (3) by a large number of (overlapping) probability distributions (clusters), each describing the interaction between a small number of variables. 

**==> picture [101 x 9] intentionally omitted <==**

> 2 When _g_ is not a square matrix (when the number of controls is less than the dimension of _x_ ), _g[−]_[1] denotes the pseudo-inverse of _g_ . For any _u_ , the pseudo-inverse has the property that _g[−]_[1] _gu_ = _u_ . 

Hilbert J. Kappen et al. 

24 

**==> picture [309 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2<br>1  2  3 2  3  5 3  4  5 1  4  5 F        F~CVMx0<br>2 1.5<br>4 1<br>2  3    3  5    4  5    1<br>3 0.5<br>5 3       5       −1.50 −1 −0.5 0 0.5 1 1.5<br>x<br>**----- End of picture text -----**<br>


**Fig. 12 (Left)** Example of a small network and a choice of clusters for CVM. **(Middle)** Intersections of clusters recursively define a set of sub-clusters. **(Right)** _F_ cvm is non-convex (blue curve) and is bounded by a convex function _F_[˜] _x_ 0 (Color online). 

with each _α_ a subset of the indices 1 _, . . . , n_ , _xα_ the corresponding subset of variables and _pα_ the probability distribution on _xα_ . The set of clusters is denoted by _B_ , and must be such that any interaction term _ψα_ ( _xα_ ), with _ψ_ ( _x_ ) =[�] _α[ψ][α]_[(] _[x][α]_[)][from][Equation][(4),][is][contained] in at least one cluster. One denotes the set of all pairwise intersections of clusters in _B_ , as well as intersections of intersections by _M_ . Figure 12 (left) gives an example of a small directed graphical model, where _B_ consists of 4 clusters and _M_ consists of 5 sub-clusters, Figure 12 (middle). 

The CVM approximates the KL divergence, Equation (3), as 

**==> picture [275 x 38] intentionally omitted <==**

_F_ cvm is minimized with respect to all _{pα}_ subject to normalization and consistency constraints: 

**==> picture [237 x 19] intentionally omitted <==**

The numbers _aβ_ are called the M¨obius or overcounting numbers. They can be recursively computed from the formula 

**==> picture [138 x 19] intentionally omitted <==**

Since _aα_ can be both positive and negative, _F_ cvm is not convex. A guaranteed convergent approach to minimize _F_ cvm is a double loop approach where the outer loop is to upper-bound _F_ cvm by a convex function _F_[˜] _p_ 0 that touches at the current cluster solution _p_[0] = _{p_[0] _α[}]_[.] Optimizing _F_[˜] _p_ 0 ( _p_ ) is a convex problem that can be solved using the dual approach (inner loop) and is guaranteed to decrease _F_ cvm to a local minimum. The solution _p[∗]_ ( _p_[0] ) of this convex sub-problem is guaranteed to decrease _F_ cvm: 

**==> picture [191 x 12] intentionally omitted <==**

Based on _p[∗]_ ( _p_ 0) a new convex upper bound is computed (outer loop). This is called a double loop method. The approach is illustrated in Figure 12 (right). 

Alternatively, one can choose to ignore the non-convexity issue. Adding Lagrange multipliers _λ_ to enforce the constraints one can minimize with respect to _p_ = _{pα}_ and obtain an explicit solution of _p_ in terms of the interactions _ψ_ and the _λ_ ’s. Inserting this solution in the 

Optimal control as a graphical model inference problem 

25 

above constraints results in a set of non-linear equations for the _λ_ ’s, which one may attempt to solve by fixed point iteration. It can be shown that these equations are equivalent to the message passing equations of belief propagation. Unlike the above double loop approach, belief propagation does not converge in general, but tends to give a fast and accurate solution for those problems for which it does converge. 

## **References** 

- Albers, C. A., Heskes, T., and Kappen, H. J. (2007). Haplotype inference in general pedigrees using the cluster variation method. _Genetics_ , 177(2):1101–1118. 

- Albers, C. A., Leisink, M. A. R., and Kappen, H. J. (2006). The cluster variation method for efficient linkage analysis on extended pedigrees. _BMC Bioinformatics_ , 7(S-1). 

- Bagnell, J. A. and Schneider, J. (2003). Covariant policy search. In _IJCAI’03: Proceedings of the 18th international joint conference on Artificial intelligence_ , pages 1019–1024, San Francisco, CA, USA. Morgan Kaufmann. 

- Bertsekas, D. P. and Tsitsiklis, J. N. (1996). _Neuro-Dynamic Programming_ . Athena ScienBelmont. Massachusetts. 

- Bierkens, J. and Kappen, B. (2012). Kl-learning: Online solution of Kullback-Leibler control problems. http://arxiv.org/abs/1112.1996. 

- Boutilier, C., Dearden, R., and Goldszmidt, M. (1995). Exploiting structure in policy construction. In _IJCAI’95: Proceedings of the 14th international joint conference on Artificial intelligence_ , pages 1104–1111, San Francisco, USA. Morgan Kaufmann. 

- Cooper, G. (1988). A method for using belief networks as influence diagrams. In _Proceedings of the Workshop on Uncertainty in Artificial Intelligence (UAI’88)_ , pages 55–63. 

- da Silva, M., Durand, F., and Popovi´c, J. (2009). Linear Bellman combination for control of character animation. _ACM Transactions on Graphics_ , 28(3):82:1–82:10. 

- Dayan, P. and Hinton, G. E. (1997). Using expectation-maximization for reinforcement learning. _Neural Computation_ , 9(2):271–278. 

- Friston, K. J., Daunizeau, J., and Kiebel, S. J. (2009). Reinforcement learning or active inference? _PLoS ONE_ , 4(7):e6421. 

- Heskes, T., Albers, K., and Kappen, H. J. (2003). Approximate inference and constrained optimization. In _Proceedings of the 19th Conference on Uncertainty in Artificial Intelligence (UAI’03)_ , pages 313–320, Acapulco, Mexico. Morgan Kaufmann. 

- Jordan, M. I., editor (1999). _Learning in graphical models_ . MIT Press, Cambridge, MA, USA. 

- Kappen, H. J. (2005). Linear theory for control of nonlinear stochastic systems. _Physical Review Letters_ , 95(20):200201. 

- Kappen, H. J. and Wiegerinck, W. (2002). Novel iteration schemes for the cluster variation method. In _Advances in Neural Information Processing Systems 14_ , pages 415–422. MIT Press, Cambridge, MA. 

- Kober, J. and Peters, J. (2011). Policy search for motor primitives in robotics. _Machine Learning_ , 84(1-2):171–203. 

- Koller, D. and Parr, R. (1999). Computing factored value functions for policies in structured mdps. In _IJCAI ’99: Proceedings of the 16th International Joint Conference on Artificial Intelligence_ , pages 1332–1339, San Francisco, CA, USA. Morgan Kaufmann. 

- Lauritzen, S. L. and Spiegelhalter, D. J. (1988). Local computations with probabilities on graphical structures and their application to expert systems. _Journal of the Royal Statistical society. Series B-Methodological_ , 50(2):154–227. 

- Mooij, J. M. (2010). libDAI: A free and open source C++ library for discrete approximate inference in graphical models. _Journal of Machine Learning Research_ , 11:2169–2173. 

- Murphy, K., Weiss, Y., and Jordan, M. (1999). Loopy belief propagation for approximate inference: An empirical study. In _Proceedings of the 15th Conference on Uncertainty in Artificial Intelligence (UAI’99)_ , pages 467–47, San Francisco, CA. Morgan Kaufmann. 

- Peters, J., M¨ulling, K., and Alt¨un, Y. (2010). Relative entropy policy search. In _Proceedings of the 24th AAAI Conference on Artificial Intelligence (AAAI 2010)_ , pages 1607–1612. AAAI Press. 

Hilbert J. Kappen et al. 

26 

Russell, S. J., Norvig, P., Candy, J. F., Malik, J. M., and Edwards, D. D. (1996). _Artificial intelligence: a modern approach_ . Prentice-Hall, Inc., Upper Saddle River, NJ, USA. Shachter, R. D. and Peot, M. A. (1992). Decision making using probabilistic inference methods. In _Proceedings of the 8th conference on Uncertainty in Artificial Intelligence (UAI’92)_ , pages 276–283, San Francisco, CA, USA. Morgan Kaufmann. 

- Skyrms, B. (1996). _Evolution of the Social Contract_ . Cambridge University Press, Cambridge/New York. 

- Skyrms, B., editor (2004). _The Stag Hunt and Evolution of Social Structure_ . Cambridge University Press, Cambridge, MA, USA. 

- Stengel, R. F. (1994). _Optimal Control and Estimation_ . Dover Publications, Inc. 

- Tatman, J. and Shachter, R. (1990). Dynamic programming and influence diagrams. _Systems, Man and Cybernetics, IEEE Transactions on_ , 20(2):365 –379. 

- Theodorou, E. A., Buchli, J., and Schaal, S. (2009). Path integral-based stochastic optimal control for rigid body dynamics. In _adaptive dynamic programming and reinforcement learning, 2009. ADPRL ’09. IEEE symposium on_ , pages 219–225. 

- Theodorou, E. A., Buchli, J., and Schaal, S. (2010a). Learning policy improvements with path integrals. In _International conference on artificial intelligence and statistics (AISTATS 2010)_ . 

- Theodorou, E. A., Buchli, J., and Schaal, S. (2010b). Reinforcement learning of motor skills in high dimensions: A path integral approach. In _Proceedings of the International Conference on Robotics and Automation (ICRA 2010)_ , pages 2397–2403. IEEE Press. 

- Todorov, E. (2007). Linearly-solvable markov decision problems. In _Advances in Neural Information Processing Systems 19_ , pages 1369–1376. MIT Press, Cambridge, MA. 

- Todorov, E. (2008). General duality between optimal control and estimation. In _47th IEEE Conference on Decision and Control_ , pages 4286–4292. 

- Todorov, E. (2009). Efficient computation of optimal actions. _Proceedings of the National Academy of Sciences of the United States of America_ , 106(28):11478–11483. 

Toussaint, M. and Storkey, A. (2006). Probabilistic inference for solving discrete and continuous state Markov Decision Processes. In _ICML ’06: Proceedings of the 23rd international conference on Machine learning_ , pages 945–952, New York, NY, USA. ACM. 

van den Broek, B., Wiegerinck, W., and Kappen, H. J. (2008a). Graphical model inference in optimal control of stochastic multi-agent systems. _Journal of Artificial Intelligence Research_ , 32(1):95–122. 

van den Broek, B., Wiegerinck, W., and Kappen, H. J. (2008b). Optimal control in large stochastic multi-agent systems. _Adaptive Agents and Multi-Agent Systems III. Adaptation and Multi-Agent Learning_ , 4865:15–26. 

- Wiegerinck, W., van den Broek, B., and Kappen, H. J. (2006). Stochastic optimal control in continuous space-time multi-agent systems. In _Proceedings of the 22nd Conference on Uncertainty in Artificial Intelligence (UAI’06)_ , pages 528–535, Arlington, Virginia. AUAI Press. 

- Wiegerinck, W., van den Broek, B., and Kappen, H. J. (2007). Optimal on-line scheduling in stochastic multi-agent systems in continuous space and time. _Proceedings of the 6th international joint conference on Autonomous agents and multiagent systems AAMAS 07_ , 5:1. 

Yedidia, J., Freeman, W., and Weiss, Y. (2001). Generalized belief propagation. In T.K. Leen, T. D. and Tresp, V., editors, _Advances in Neural Information Processing Systems 13_ , pages 689–995. MIT Press, Cambridge, MA. 

- Yedidia, J., Freeman, W., and Weiss, Y. (2005). Constructing free-energy approximations and generalized belief propagation algorithms. _Information Theory, IEEE Transactions on_ , 51(7):2282 – 2312. 

Yoshida, W., Dolan, R. J., and Friston, K. J. (2008). Game theory of mind. _PLoS Computational Biology_ , 4(12):e1000254. 

