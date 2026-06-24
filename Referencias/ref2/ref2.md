_**entropy**_ 

_Article_ 

## **Lagrangian Function on the Finite State Space Statistical Bundle** 

## **Giovanni Pistone** 

## **ID** 

De Castro Statistics, Collegio Carlo Alberto, 10122 Torino, Italy; giovanni.pistone@carloalberto.org Received: 26 December 2017; Accepted: 24 January 2018; Published: 22 February 2018 

**Abstract:** The statistical bundle is the set of couples ( _Q_ , _W_ ) of a probability density _Q_ and a random variable _W_ such that E _Q_ [ _W_ ] = 0. On a finite state space, we assume _Q_ to be a probability density with respect to the uniform probability and give an affine atlas of charts such that the resulting manifold is a model for Information Geometry. Velocity and acceleration of a one-dimensional statistical model are computed in this set up. The Euler–Lagrange equations are derived from the Lagrange action integral. An example Lagrangian using minus the entropy as potential energy is briefly discussed. 

**Keywords:** Information Geometry; statistical bundle; Lagrangian function 

## **1. Introduction** 

The set-up of classical Lagrangian Mechanics is a finite-dimensional Riemannian manifold. For example, see the monographs by V.I. Arnold ([1], Chapters III–IV), R. Abraham and J.E. Mardsen ([2], Chapter 3), J.E. Marsden and T.S. Ratiu ([3], Chapter 7). Classical Information geometry, as it was first defined in the monograph by S.-I. Amari and H. Nagaoka [4], views parametric statistical models as a manifold endowed with a dually-flat connection. In a recent paper, M. Leok and J. Zhang [5] have pointed out the natural relation between these two topics and have given a wide overview of the mathematical structures involved. 

In the present paper, we take up the same research program with two further qualifications. First, we assume a non-parametric approach by considering the full set of positive probability functions on a finite set, as it was done, for example, in our review paper [6]. The discussion is restricted here to a finite state space to avoid difficult technical problems. Second, we consider a specific expression of the tangent space of the statistical manifold, which is a Hilbert bundle that we call a statistical bundle. Our aim is to emphasize the basic statistical intuition of the geometric quantities involved. Because of that, we chose to systematically use the language of non-parametric differential geometry as it is developed in the monography of S. Lang [7]. 

Herein, we use our version of Information Geometry; see the review paper [6]. Preliminary versions of this paper have been presented at the SigmaPhy2017 Conference held in Corfu, Greece, 10–14 July 2017, and at a seminar held at Collegio Carlo Alberto, Moncalieri, on 5 September 2017. In these early versions, we did not refer to Leok and Zhang’s work, which we were unaware of at that time. 

In Section 2, we review the definition and properties of the statistical bundle, and of the affine atlas that endows it with both a manifold structure and a natural family of transports between the fibers. In Section 3, we develop the formalism of the tangent space of the statistical bundle and derive the expression of the velocity and the acceleration of a one-dimensional statistical model in the given affine atlas. The derivation of the Euler–Lagrange equations, together with a relevant example, is discussed in Section 4. 

_Entropy_ **2018** , _20_ , 139; doi:10.3390/e20020139 

www.mdpi.com/journal/entropy 

2 of 9 

_Entropy_ **2018** , _20_ , 139 

## **2. Statistical Bundle** 

We consider a finite sample space Ω, with #Ω = _N_ . The probability simplex is ∆(Ω), and ∆ _[◦]_ (Ω) is its interior. The uniform probability on Ω is denoted as _µ_ , _µ_ ( _x_ ) = _N_[1][,] _[ x][∈]_[Ω][.][The] _[ maximal exponential] family E_ ( _µ_ ) is the set of all strictly positive probability densities of (Ω, _µ_ ). The expected value of _f_ : Ω _→_ R with respect to the density _P ∈E_ ( _µ_ ) is denoted E _P_ [ _f_ ] = E _µ_ [ _f P_ ] = _N_[1][∑] _[x][∈]_[Ω] _[f]_[ (] _[x]_[)] _[P]_[(] _[x]_[)][.] 

In [6,8,9], we made the case for the statistical bundle being the key structure of Information Geometry. The _statistical bundle_ with base Ω is 

**==> picture [193 x 14] intentionally omitted <==**

The statistical bundle is a semi-algebraic subset of R[2] _[N]_ ; i.e., it is defined by algebraic equations and strict inequalities. It is trivially a real manifold. At each _Q ∈E_ ( _µ_ ), the fiber _SQ E_ ( _µ_ ) is endowed with the scalar product 

**==> picture [228 x 13] intentionally omitted <==**

To this structure we add a special affine atlas of charts in order to show a structure of affine manifold, which is of interest in the statistical applications. The _exponential atlas_ of the statistical manifold _S E_ ( _µ_ ) is the collection of charts given for each _P ∈E_ ( _µ_ ) by 

**==> picture [358 x 15] intentionally omitted <==**

where (with a slight abuse of notation) 

**==> picture [342 x 25] intentionally omitted <==**

As _sP_ ( _P_ , _V_ ) = (0, _V_ ), we say that _sP_ is the chart _centered at P_ . If _sP_ ( _Q_ ) = _U_ , it is easy to derive the exponential form of _Q_ as a density with respect to _P_ ; namely, _Q_ = e _[U][−]_[E] _[P]_ �log _[Q] P_ � _· P_ . As E _µ_ [ _Q_ ] = 1, then 1 = E _p_ e _[U][−]_[E] _[P]_ �log _Q[P]_ � = E _p_ �e _[U]_[�] e _[−]_[E] _[P]_ �log _Q[P]_ �, so that the _cumulant function KP_ is defined on � � _SP E_ ( _µ_ ) by 

**==> picture [219 x 25] intentionally omitted <==**

that is, _KP_ ( _V_ ) is the expression in the chart at _P_ of Kullback–Leibler divergence of _Q �→_ D ( _P ∥Q_ ), and we can write 

**==> picture [127 x 14] intentionally omitted <==**

The _patch centered at P_ is 

**==> picture [287 x 16] intentionally omitted <==**

In statistical terms, the random variable log ( _Q_ / _P_ ) is the relative point-wise information about _Q_ relative to the reference _P_ , while _sP_ ( _Q_ ) is the deviation from its mean value at _P_ . The expression of the other divergence in the chart centered at _P_ is 

**==> picture [281 x 25] intentionally omitted <==**

The equation above shows that the two divergences are convex conjugate functions in the proper charts; see [10]. 

3 of 9 

_Entropy_ **2018** , _20_ , 139 

The transition maps of the exponential atlas in Equations (1) and (2) are 

**==> picture [395 x 63] intentionally omitted <==**

so that the exponential atlas is indeed affine. Notice that the linear part is[e] U _[P] P_[2] 1[.] 

## **3. The Tangent Space of the Statistical Bundle** 

Let us compute the expression of the velocity at time _t_ of a smooth curve _t �→ γ_ ( _t_ ) = ( _Q_ ( _t_ ), _W_ ( _t_ )) _∈ S E_ ( _µ_ ) in the chart centered at _P_ . The expression of the curve is 

**==> picture [200 x 19] intentionally omitted <==**

and hence we have, by denoting the derivative in R _[N]_ by the dot, 

**==> picture [406 x 26] intentionally omitted <==**

and 

_dtd_ eU _QP_ ( _t_ ) _[W]_[(] _[t]_[) =] _dt[d]_[(] _[W]_[(] _[t]_[)] _[ −]_[E] _[P]_[ [] _[W]_[(] _[t]_[)]) =] _[W]_[˙][(] _[t]_[)] _[ −]_[E] _[P]_ � _W_ ˙ ( _t_ )� = eU _QP_ ( _t_ ) � _W_ ˙ ( _t_ ) _−_ E _Q_ ( _t_ ) � _W_ ˙ ( _t_ )�[�] . (4) If we define the _velocity_ of _t �→ Q_ ( _t_ ) = e _[U]_[(] _[t]_[)] _[−][K][p]_[(] _[U]_[(] _[t]_[))] _× P_ to be 

˙ _Q⋆_ ( _t_ ) = _Q_ ( _t_ ) _[d][U]_[˙][(] _[t]_[)] _[ −][dK][P]_[(] _[U]_[(] _[t]_[))[] _[U]_[˙][(] _[t]_[)]] _[ ∈][S][Q]_[(] _[t]_[)] _[ E]_[ (] _[µ]_[)][,] _Q_ ( _t_ )[=] _dt_[log] _[ Q]_[(] _[t]_[) =] _⋆_ then _t �→_ ( _Q_ ( _t_ ), _Q_ ( _t_ )) is a curve in the statistical bundle whose expression in the chart centered at _P_ is _t �→_ ( _U_ ( _t_ ), _U_[˙] ( _t_ )). The velocity as defined above is nothing else as the _score function_ of the one-dimensional statistical model; see e.g., the textbook by B. Efron and T. Haste (Section 4.2, [11]). _⋆_ The variance of the score function (i.e., the squared norm of _Q_ ( _t_ ) in _SQ_ ( _t_ ) _E_ ( _µ_ )) is classically known as _Fisher information_ at _t_ . 

_second statistical bundle_ to be 

**==> picture [273 x 14] intentionally omitted <==**

with charts 

**==> picture [193 x 19] intentionally omitted <==**

we can identify the second bundle with the tangent space of the first bundle as follows. 

For each curve _t �→ γ_ ( _t_ ) = ( _Q_ ( _t_ ), _W_ ( _t_ )) in the statistical bundle, define its _velocity at t_ to be 

**==> picture [217 x 19] intentionally omitted <==**

because _t �→ γ⋆_ ( _t_ ) is a curve in the second statistical bundle, and its expression in the chart at _P_ has the last two components equal to the values given in Equations (3) and (4). 

_⋆_ In particular, consider the a curve _t �→ χ_ ( _t_ ) = ( _Q_ ( _t_ ), _Q_ ( _t_ )). The velocity is 

**==> picture [145 x 19] intentionally omitted <==**

4 of 9 

_Entropy_ **2018** , _20_ , 139 

_∗∗_ where the _acceleration Q_ ( _t_ ) is 

**==> picture [376 x 26] intentionally omitted <==**

It should be noted that the acceleration has been defined without explicitly mentioning the relevant connection. In fact, the connection here is implicitly defined by the transports[e] U _[Q] P_[, which is unusual] in Differential Geometry, but is quite natural from the probabilistic point of view; see P. Gibilisco and G. Pistone [12]. We shall see below that the non-parametric approach to Information Geometry allows the definition of a dual transport, hence a dual connection as it was in [4]. Because of that, we could have defined other types of acceleration together with the one we have defined. Namely, we could _∗∗_ consider an _exponential acceleration[e]_ D[2] _Q_ ( _t_ ) = _Q_ ( _t_ ), a _mixture acceleration[m]_ D[2] _Q_ ( _t_ ) = _Q_[¨] ( _t_ )/ _Q_ ( _t_ ), and a _Riemannian acceleration_ 

**==> picture [407 x 31] intentionally omitted <==**

each acceleration being associated with a specific connection; see the review paper [6]. We do not further discuss the different second-order geometries associated with the statistical bundle in this paper. 

**Example 1** (Boltzmann–Gibbs) **.** Let us compare the formalism we have introduced above with standard computations in Statistical Physics. The _Boltzmann–Gibbs distribution_ gives to point _x ∈_ Ω the probability e _[−]_[(][1/] _[θ]_[)] _[H]_[(] _[x]_[)] / _Z_ ( _θ_ ), with _Z_ ( _θ_ ) = ∑ _x∈_ Ω e _[−]_[(][1/] _[θ]_[)] _[H]_[(] _[x]_[)] and _θ >_ 0, see Landau and Lifshitz ([13], Chapter 3). As a curve in _E_ ( _µ_ ), it is _Q_ ( _θ_ ) = _N_ e _[−]_[(][1/] _[θ]_[)] _[H]_ / _Z_ ( _θ_ ) because of the reference to the _⋆_ uniform probability. The velocity defined above becomes in this case _Q_ ( _θ_ ) = _θ[−]_[2] ( _H −_ E _θ_ [ _H_ ]), _∗∗_ while the acceleration of Equation (5) is _Q_ ( _θ_ ) = _−θ[−]_[3] ( _H −_ E _θ_ [ _H_ ]). Notice that we have the equation _∗∗ ⋆ θQ_ ( _θ_ ) + _Q_ ( _θ_ ) = 0. 

Following the original construction of Amari’s Information Geometry [4], we have defined on the statistical bundle a manifold structure which is both an affine and a Riemannian manifold. The base manifold _E_ ( _µ_ ) is actually a Hessian manifold with respect to any of the convex functions _Kp_ ( _U_ ) = log E _p_ �e _[U]_[�] , _U ∈ Sp E_ ( _µ_ ) (see [14]). Many computations are actually performed using the Hessian structure. The following equations are easily checked and frequently used: 

**==> picture [377 x 79] intentionally omitted <==**

We have defined a centering operation that can be thought of as a _transport_ among fibers, 

**==> picture [119 x 15] intentionally omitted <==**

whose adjoint is[m] U _q[p][V]_[=] _[q] p[V]_[.][In fact, is the adjoint of][e][U] _[q] p_[,] 

**==> picture [369 x 25] intentionally omitted <==**

5 of 9 

_Entropy_ **2018** , _20_ , 139 

Moreover, iff _U_ , _V ∈ SP E_ ( _µ_ ), then 

**==> picture [225 x 21] intentionally omitted <==**

**Example 2** (Entropy flow) **.** This example is taken from [8]. In the scalar field _H_ ( _Q_ ) = _−_ E _Q_ [log _Q_ ], there is no dependence on the fiber. If _t �→ Q_ ( _t_ ) = e _[V]_[(] _[t]_[)] _[−][K][P]_[(] _[V]_[(] _[t]_[))] _· P_ is a smooth curve in _E_ ( _µ_ ) expressed in the chart centered at _P_ , then we can write 

**==> picture [181 x 12] intentionally omitted <==**

**==> picture [243 x 26] intentionally omitted <==**

where the argument of the last expectation belongs to the fiber _SP E_ ( _µ_ ) and we have expressed the expected value as a derivative by using Equation (7). 

Again using Equations (7) and (9), we compute the derivative of the entropy along the given curve as 

**==> picture [406 x 61] intentionally omitted <==**

We use now the equations 

e _V_ ( _t_ ) + log _P_ = log _Q_ ( _t_ ) + _KP_ ( _V_ ( _t_ )) , U _[Q] P_[(] _[t]_[)] (log _Q_ ( _t_ ) + _KP_ ( _V_ ( _t_ ))) = log _Q_ ( _t_ ) + _H_ ( _Q_ ( _t_ )) , and[e] U _[Q] P_[(] _[t]_[)] _V_ ˙ ( _t_ ) = _Q⋆_ ( _t_ ) to obtain 

**==> picture [225 x 24] intentionally omitted <==**

We have identified the gradient of the entropy in the statistical bundle, 

**==> picture [295 x 12] intentionally omitted <==**

Notice that the previous computation could have been done using the exponential family _Q_ ( _t_ ) = e _P_ ( _tV_ ). See the computation of the gradient flow in [8]. 

In the next section, we extend the computation illustrated in the example above to scalar fields on the statistical bundle. 

## **4. Lagrangian Function** 

A _Lagrangian function_ is a smooth scalar field on the statistical bundle 

**==> picture [166 x 11] intentionally omitted <==**

**==> picture [233 x 11] intentionally omitted <==**

**==> picture [278 x 13] intentionally omitted <==**

is defined on the vector space _Sq E_ ( _µ_ ); hence, we can use the ordinary derivative, which in this case is called the _fiber derivative_ , 

6 of 9 

_Entropy_ **2018** , _20_ , 139 

**==> picture [350 x 26] intentionally omitted <==**

**Example 3** (Running Example 1) **.** If 

**==> picture [318 x 22] intentionally omitted <==**

then _d_ 2 _L_ ( _Q_ , _W_ )[ _H_ 2] = _⟨W_ , _H_ 2 _⟩Q_ . The example is suggested by the form of the classical Lagrangian function in mechanics, where the first term is the kinetic energy and _−κ H_ ( _Q_ ) is the potential energy. 

As the statistical bundle _S E_ ( _µ_ ) is non-trivial, the computation of the partial derivative of the Lagrangian with respect to the first variable requires some care. We want to compute the expression of the total derivative in a chart of the affine atlas defined in Equations (1) and (2). 

Let _t �→ γ_ ( _t_ ) = ( _Q_ ( _t_ ), _W_ ( _t_ )) be a smooth curve in the statistical bundle. In the chart centered at _P_ , we have 

**==> picture [282 x 16] intentionally omitted <==**

with _t �→ γP_ ( _t_ ) = ( _U_ ( _t_ ), _V_ ( _t_ )) being a smooth curve in ( _SP E_ ( _µ_ ))[2] . Let us compute the velocity of variation of the Lagrangian _L_ along the curve _γ_ . 

**==> picture [370 x 22] intentionally omitted <==**

with _LP_ ( _U_ , _V_ ) = _L_ (e _P_ ( _U_ ),[e] U[e] _P[P]_[(] _[U]_[)] _V_ ). It follows that 

**==> picture [373 x 22] intentionally omitted <==**

If we write _Q_ = e _P_ ( _U_ ) and _W_ =[e] U[e] _P[P]_[(] _[U]_[)] _V_ , then we have 

_d_ 2 _LP_ ( _U_ , _V_ )[ _H_ 2] = _dtd[L][P]_[(] _[U]_[,] _[ V]_[ +] _[ tH]_[2][)] ��� _t_ =0[=] _dtd[L]_[(] _[Q]_[,] _[ W]_[ +] _[ t]_[ e][U] _[Q] P[H]_[2][)] ��� _t_ =0[=] _[d]_[2] _[L]_[(] _[Q]_[,] _[ W]_[)[][e][U] _[Q] P[H]_[2][]][ ,] (17) _⋆_ ˙ _⋆_ where _d_ 2 _L_ is the fiber derivative of _L_ . As _U_[˙] ( _t_ ) =[e] U _Q[P]_ ( _t_ ) _Q_ ( _t_ ) and[e] U[e] _P[P]_[(] _[U]_[(] _[t]_[))] _V_ ( _t_ ) = _W_ ( _t_ ), it follows from Equations (16) and (17) that 

**==> picture [330 x 22] intentionally omitted <==**

In the equation above, the first term on the RHS does not depend on _P_ because the LHS and the second term of the RHS do not depend on _P_ . Hence, we define the first partial derivative of the Lagrangian function to be 

**==> picture [351 x 16] intentionally omitted <==**

so that the derivative of _L_ along _γ_ becomes 

**==> picture [370 x 22] intentionally omitted <==**

_⋆_ In particular, if _W_ ( _t_ ) = _Q_ ( _t_ ), then 

**==> picture [292 x 22] intentionally omitted <==**

see Equation (5). 

7 of 9 

_Entropy_ **2018** , _20_ , 139 

**Example 4** (Running Example 2) **.** With the Lagrangian of Equation (15), we have 

**==> picture [333 x 48] intentionally omitted <==**

see Equations (9) and (11). The first partial derivative is 

**==> picture [68 x 10] intentionally omitted <==**

**==> picture [344 x 84] intentionally omitted <==**

where we have used Equations (9) and (10) together with[e] U[e] _P[P]_[(] _[U]_[)] ( _U_ + log _P_ + _H_ ( _P_ )) = log _Q_ + _H_ ( _Q_ ). We have found that 

**==> picture [420 x 27] intentionally omitted <==**

and also 

**==> picture [364 x 27] intentionally omitted <==**

Using the fiber derivative computed in the first part of the running example, we find 

**==> picture [414 x 26] intentionally omitted <==**

Notice that Equation (12) shows that one of the terms in the equations above is grad _H_ ( _Q_ ). 

## **5. Action Integral** 

If [0, 1] _∋ t �→ Q_ ( _t_ ) is a smooth curve in the exponential manifold, then the _action integral_ 

**==> picture [124 x 24] intentionally omitted <==**

is well defined. We consider the expression of _Q_ in the chart centered at _P_ , _Q_ ( _t_ ) = e _[U]_[(] _[t]_[)] _[−][K][P]_[(] _[U]_[(] _[t]_[))] _× P_ . Given _ϕ ∈ C_[1] ([0, 1]) with _ϕ_ (0) = _ϕ_ (1) = 0, for each _δ ∈_ R and _H ∈ SP E_ ( _µ_ ), we define the perturbed curve 

**==> picture [189 x 14] intentionally omitted <==**

We have _Qδ_ (0) = _Q_ (0), _Qδ_ (1) = _Q_ (1), and 

**==> picture [232 x 17] intentionally omitted <==**

whose expression in the chart centered at _P_ is _U_[˙] ( _t_ ) + _δϕ_ ˙ ( _t_ ) _H_ . 

Let us consider the variation in _δ_ of the action integral. We apply Equation (19) applied to the smooth curve in _S E_ ( _µ_ ) given by 

**==> picture [89 x 15] intentionally omitted <==**

8 of 9 

_Entropy_ **2018** , _20_ , 139 

where _t_ As 

and 

**==> picture [398 x 66] intentionally omitted <==**

we obtain 

**==> picture [396 x 78] intentionally omitted <==**

_d_ If _t �→ Q_ ( _t_ ) is a critical curve of the action integral, then _dδ[A]_[(] _[Q][δ]_[)] ��� _δ_ =0[=][ 0; hence, for all] _[ϕ]_[ and] _[H]_[,] we have 

**==> picture [420 x 74] intentionally omitted <==**

This in turn implies that for each _t ∈_ [0, 1] and _H ∈ SQ_ ( _t_ ) _E_ ( _µ_ ), the Euler–Lagrange equation holds: 

**Example 5** (Running Example 3) **.** For the Lagrangian of Equation (15), we can use Equation (20) in the form 

**==> picture [423 x 47] intentionally omitted <==**

with _H ∈ SP E_ ( _µ_ ). For the other term, we have 

**==> picture [371 x 22] intentionally omitted <==**

whose derivative is 

**==> picture [323 x 60] intentionally omitted <==**

Dropping the generic _H_ , the Euler–Lagrange equation becomes 

_Q∗∗_ ( _t_ ) + � _Q⋆_ ( _t_ )2 _−_ E _Q_ ( _t_ ) � _Q⋆_ ( _t_ )2�� =[1] 2 � _Q⋆_ ( _t_ )2 _−_ E _Q_ ( _t_ ) � _Q⋆_ ( _t_ )2�� _− κ_ (log ( _Q_ ( _t_ )) + _H_ ( _Q_ ( _t_ ))) ; that is, 

_Q∗∗_ ( _t_ ) + 12 � _Q⋆_ ( _t_ )2 _−_ E _Q_ ( _t_ ) � _Q⋆_ ( _t_ )2�� = _−κ_ (log ( _Q_ ( _t_ )) + _H_ ( _Q_ ( _t_ ))) . The equation above has been derived using the exponential affine geometry of the statistical _∗∗_ bundle and involves _Q_ ( _t_ ). However, by using Equations (5), (6), and (12), we find the equivalent form 0D2 _Q_ ( _t_ ) = _κ_ grad _H_ ( _Q_ ( _t_ )) . 

9 of 9 

_Entropy_ **2018** , _20_ , 139 

## **6. Discussion** 

We have shown that the research program consisting of applying concepts taken from Classical Mechanics to Statistics makes sense, even if no practical application has been produced in this paper. Some simple examples have been discussed in order to show clearly that the language from classical mechanics is indeed suggestive when applied to typical concepts in Statistics such as Fisher score and statistical entropy. The derivation of the Euler–Lagrange equations is classically done in the set-up of the Riemannian geometry, while here we have used the affine structure of Information Geometry. The present provisional results prompt a generalization to non-finite sample spaces and the development of applications. Finally, the related Hamiltonian formalism remains to be investigated. 

> **Acknowledgments:** The Author gratefully thanks Hiroshi Matsuzoe (Nagoya Institute of Technology, Japan), Lamberto Rondoni (Politecnico di Torino, Italy), Antonio Scarfone (CNR and Politecnico di Torino, Italy), Tatsuaki Wada (Ibaraki University, Japan), for their interesting comments on early versions of this piece of research. He thanks two anonymous referees for their useful and enlightening comments. He acknowledges the support of de Castro Statistics, Collegio Carlo Alberto, and of GNAMPA-INdAM. 

## **References** 

1. Arnold, V.I. _Mathematical Methods of Classical Mechanics_ , 2nd ed.; Graduate Texts in Mathematics; Springer: New York, NY, USA, 1989; Volume 60, p. xvi+516. 

2. Abraham, R.; Marsden, J.E. _Foundations of Mechanics_ , 2nd ed.; Advanced Book Program, Reading, Mass; Benjamin/Cummings Publishing Co., Inc.: San Francisco, CA, USA, 1978; pp. xxii+m–xvi+806. 

3. Marsden, J.E.; Ratiu, T.S. _Introduction to Mechanics and Symmetry: A Basic Exposition of Classical Mechanical Systems_ , 2nd ed.; Texts in Applied Mathematics; Springer: New York, NY, USA, 1999; Volume 17, p. xviii+582. 

4. Amari, S.; Nagaoka, H. _Methods of Information Geometry_ ; American Mathematical Society: Providence, RI, USA, 2000; p. x+206. 

5. Leok, M.; Zhang, J. Connecting Information Geometry and Geometric Mechanics. _Entropy_ **2017** , _19_ , 518, doi:10.3390/e19100518. 

6. Pistone, G. Nonparametric information geometry. In _Geometric Science of Information, Proceedings of the First International Conference, GSI 2013, Paris, France, 28–30 August 2013_ ; Nielsen, F., Barbaresco, F., Eds.; Lecture Notes in Computer Science; Springer: Heidelberg, Germany, 2013; Volume 8085, pp. 5–36. 

7. Lang, S. _Differential and Riemannian Manifolds_ , 3rd ed.; Graduate Texts in Mathematics; Springer: Berlin, Germany, 1995; Volume 160, p. xiv+364. 

8. Pistone, G. Examples of the application of nonparametric information geometry to statistical physics. _Entropy_ **2013** , _15_ , 4042–4065. 

9. Lods, B.; Pistone, G. Information Geometry Formalism for the Spatially Homogeneous Boltzmann Equation. _Entropy_ **2015** , _17_ , 4323–4363. 

10. Pistone, G.; Rogantin, M. The exponential statistical manifold: mean parameters, orthogonality and space transformations. _Bernoulli_ **1999** , _5_ , 721–760. 

11. Efron, B.; Hastie, T. _Computer Age Statistical Inference: Algorithms, Evidence, and Data Science_ ; Cambridge University Press: New York, NY, USA, 2016; Volume 5, p. xix+475. 

12. Gibilisco, P.; Pistone, G. Connections on non-parametric statistical manifolds by Orlicz space geometry. _IDAQP_ **1998** , _1_ , 325–347. 

13. Landau, L.D.; Lifshits, E.M. _Course of Theoretical Physics. Statistical Physics_ , 3rd ed.; Butterworth-Heinemann: Oxford, UK, 1980; Volume 5. 

14. Shima, H. _The Geometry of Hessian Structures_ ; World Scientific Publishing Co. Pte. Ltd.: Hackensack, NJ, USA, 2007; p. xiv+246. 

_⃝_ c 2018 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). 

