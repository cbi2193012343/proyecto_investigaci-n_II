_**axioms**_ 

_Article_ 

## **A Unified Approach to Aitchison’s, Dually Affine, and Transport Geometries of the Probability Simplex** 

**Giovanni Pistone[1] and Muhammad Shoaib[2,] *** 

- 1 De Castro Statistics Initiative, Collegio Carlo Alberto, 10122 Torino, Italy; giovanni.pistone@carloalberto.org 2 Department of Mathematics—DIMA, University of Genova, 16146 Genova, Italy 

- Correspondence: muhammad.shoaib@dima.unige.it 

**Abstract:** A critical processing step for AI algorithms is mapping the raw data to a landscape where the similarity of two data points is conveniently defined. Frequently, when the data points are compositions of probability functions, the similarity is reduced to affine geometric concepts; the basic notion is that of the straight line connecting two data points, defined as a zero-acceleration line segment. This paper provides an axiomatic presentation of the probability simplex’s most commonly used affine geometries. One result is a coherent presentation of gradient flow in Aichinson’s compositional data, Amari’s information geometry, the Kantorivich distance, and the Lagrangian optimization of the probability simplex. 

**Keywords:** affine geometry; Bayes space; information geometry 

**MSC:** 53B12; 62B11; 94A16 

## **1. Introduction** 

**Citation:** Pistone, G.; Shoaib, M. A Unified Approach to Aitchison’s, Dually Affine, and Transport Geometries of the Probability Simplex. _Axioms_ **2024** , _13_ , 823. https://doi.org/ 10.3390/axioms13120823 

Academic Editors: Anna Maria Fino and Sidney A. Morris 

Received: 5 September 2024 Revised: 1 November 2024 Accepted: 21 November 2024 Published: 25 November 2024 

This paper discusses the geometry of the set of all probability measures whose support is a given finite set. The _sample space_ Ω is the set of possible outcomes of the experiment of interest. While the use of a geometric language is well established in statistics, the formalization of a specific _affine_ structure is due to the work of Amari, particularly in [1,2]. Amari defines a dually affine atlas of charts in the precise sense to be described below. This structure is fascinating because it gives an intrinsically geometric meaning to classical Fischerian objects such as log-likelihood, Fisher’s score, and Fisher’s information. This paper is based on a non-parametric representation of Amari’s seminal work, which was introduced in a series of papers, starting with [3]. 

## _1.1. Probability Simplex_ 

On the finite sample space Ω, a probability is characterized by its _probability function q ∈_ R[Ω] , that is, the mapping Ω _→_ R _≥_ 0 (the set of non-negative real numbers) in which the sum of the probabilities over all outcomes equals 1. Hence, the set of all probability functions, the _probability simplex_ , is 

**==> picture [286 x 21] intentionally omitted <==**

**Copyright:** © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

The probability simplex is a convex set, which means it contains all mixtures. Given two probability functions, _p_ , _q ∈P_ (Ω), the line segment joining _p_ and _q_ , 

**==> picture [270 x 11] intentionally omitted <==**

lies entirely within _P_ (Ω). 

_Axioms_ **2024** , _13_ , 823. https://doi.org/10.3390/axioms13120823 

https://www.mdpi.com/journal/axioms 

_Axioms_ **2024** , _13_ , 823 

2 of 34 

## _1.2. Compositions_ 

According to [4,5], a _composition_ , _f_ , in the sample space Ω is a positive function of Ω, _f_ : Ω _→_ R _≥_ 0. Two compositions, _f_ and _g_ , are equivalent if there exists a constant, _k ∈_ R _>_ 0, such that _g_ = _k f_ . Each composition, _f_ , is normalized to a probability function via 

**==> picture [270 x 25] intentionally omitted <==**

The above equation holds under the condition that _f_ = 0 on Ω, as normalization requires a non-zero sum of _f[′] s_ values. If _f_ = 0 on Ω, normalization would not be possible. Two compositions are equivalent if and only if the normalized compositions are equal so that the set of equivalent compositions is the same as the probability simplex. However, the notion of the composition suggests a geometric structure other than the mixture of Equation (2). Given compositions _f_ and _g_ , the product _h_ = _f ◦ g_ is a composition, and the proportionality relation holds. If _f_ 1 = _k_ 1 _f_ and _g_ 1 = _k_ 2 _g_ , then _f_ 1 _g_ 1 = ( _k_ 1 _k_ 2) _f g_ . Similarly, for the exponentiation ( _α_ , _f_ ) _�→ f[α]_ , _α ∈_ R. 

These two operations provide a way of connecting two probability functions with the so-called _exponential arc_ , 

**==> picture [279 x 26] intentionally omitted <==**

The set of all compositions with the operations we have just described is sometimes called _Bayes space_ [6] because the Bayes formula is possibly the most important example of a normalized product of compositions. 

The mixture (2) and the exponential arc (4) will be central objects in the geometric presentation of the probability simplex. 

## _1.3. Polytopes and Simplexes_ 

We need to review some basic facts of convex analysis; see, for example, [7,8]. A set, _S_ , in a Euclidean space R _[n]_ is _convex_ if, for any two points, _p_ , _q ∈ S_ , the line segment joining _p_ and _q_ of Equation (2) lies entirely within _S_ . The _convex hull_ of a set, _P ∈_ R _[n]_ , is the set of all convex combinations of points in _P_ , 

**==> picture [242 x 31] intentionally omitted <==**

where the non-negative real numbers _λi_ are the weights or coefficients of the convex combination, and _pi_ are points in _P_ . In particular, a _polytope_ is the convex hull of a finite set of points. A minimal set of such points is the set of vertices. The probability simplex on Ω (also called the standard simplex in other fields) is the polytope whose vertices are the delta probability functions _δa_ ( _x_ ) = ( _x_ = _a_ ) for all _a ∈_ Ω; that is, 

**==> picture [252 x 31] intentionally omitted <==**

Each _δa_ represents a probability for which the entire probability mass is concentrated at _a_ . An _affine combination_ of the vectors _p_ 1, . . . , _pk ∈_ R[Ω] is a vector of the form ∑ _[k] j_ =1 _[t][j][p][j]_[,] with ∑ _[k] j_ =1 _[t][j]_[=][ 1.][The given vectors are] _[ affinely independent]_[ if no affine combination is zero.] A _simplex_ is a polytope generated via _affinely independent_ points _a_ 1, . . . , _an_ . All simplexes with the same number of vertices can be transformed into one another through a suitable affine function. Thus, any _n_ -vertex simplex in any _n_ -dimensional space is essentially the same shape, differing only by scaling, rotation, and translation. 

The probability simplex is a closed set in its ambient Euclidean space. The topological border is a union of simplexes of smaller dimensions, each one corresponding to a reduced support of the probability functions. In statistical modeling, one usually assumes that the 

_Axioms_ **2024** , _13_ , 823 

3 of 34 

support of each probability function in the model of interest is the same. For this reason, we will mainly consider the open probability simplex _P>_ (Ω), which is the set of strictly positive probability functions. 

## _1.4. Overview_ 

This piece of research presents, in a coordinated and principled way, some basic topics in the geometrical calculus of the probability simplex. The specific topics are Aitchison’s theory of compositional data and Bayes spaces, Amari’s dually affine information geometry, and transport theory in product sample spaces. We define a differential geometric structure with an explicitly defined expression of the tangent bundle and discuss the relevant calculus operations, especially the notions of a natural gradient and gradient flow. 

Section 2 is devoted to the definition of _affine space_ as a set, _M_ , endowed with a _displacement_ function that maps every couple of points to a vector in such a way that the rule of addition of vectors holds. An affine space is a differentiable manifold for which the displacement function with the first point fixed provides a chart from _M_ to a vector space. The Aitchison geometry of compositional data is an instance of such a geometry. 

Section 3 presents a generalization of the notion of affine space to a more complex object, which allows us to set information geometry within this geometric framework. In affine spaces, the tangent space is the same at each point. However, the classical Fisher’s methodology, together with Amari’s methodology, suggests taking the Fisher’s score as a definition of the tangent vector. As a consequence, it is convenient to assume that the primary expression of the tangent bundle is the set of weighted contrasts. This natural setting requires an extra structure, that is, an identification between tangent spaces, called a _parallel transport_ . This section contains the main computational results, particularly the notions of natural gradient, duality of transports, and gradient flow. 

Section 4 presents the analysis of the affine statistical bundle when the sample space is of product type. In this case, we introduce the notions of ANOVA decomposition and an optimal transport plan. 

Section 5 deals with the second-order geometric analysis of the probability simplex, that is, the first-order geometric analysis of the statistical bundle. It is well known from differential geometry that second-order objects, such as accelerations, are not uniquely defined from the given atlas of charts on the base space. In our case, we have charts defined on a vector bundle expressing the probability functions and Fisher’s scores, which allows for statistically natural definitions of accelerations. The availability of second-order objects prompts the development of results inspired by notions of mechanics, such as the calculus of Lagrangian functions. It should be noted that the use of a language inspired by physics here does not refer to the push-up of the probability simplex of a dynamic on the sample space; rather, it refers to an irreducible dynamic of the probability simplex. 

## **2. Affine Geometry of the Probability Simplex** 

The geometries we are going to discuss are supported on the probability simplex _P_ (Ω) or on the open probability simplex _P>_ (Ω) of a finite sample space Ω. The latter open convex set is the interior of the former full probability simplex (1). The term “geometry” is ambiguous and should be qualified by stating which type of geometry we are talking about. Actually, the field of statistics uses many types of geometries, such as linear, affine, metric, geodesic, Riemannian, and differential geometries. We discuss here affine geometry, to be precisely defined below. Our general references are the monographs [2,9,10] (Ch. I–II). The tutorials [11,12] present similar material as the present one but in a more restricted scope. 

Affine geometry is a special instance of differential geometry. The former inherits the language of the latter: chart, atlas, expression, tangent space, and bundle. . . We refer to the non-parametric version of differential geometry as presented in [13,14]. Below, we list the basic concepts. 

_Axioms_ **2024** , _13_ , 823 

4 of 34 

Given a set, _M_ , and a real vector space, _V_ , a _chart_ is a one-to-one mapping, _s_ : _U → V_ , where _U ⊆ M_ , and _s_ ( _U_ ) is open in _V_ . Two charts, _s_ 1 : _U_ 1 _→ V_ 1 and _s_ 2 : _U_ 2 _→ V_ 2, are _C[k]_ -compatible if the change in chart mapping 

**==> picture [161 x 14] intentionally omitted <==**

is either empty or a _C[k]_ -diffeomorphism of open sets. (As usual, _◦_ stands for the composition of functions.) A family of two by two _C[k]_ -compatible charts is a _C[k]_ - _atlas_ . Two atlases are compatible if their union is an atlas. A maximal _C[k]_ -atlas is a _C[k]_ - _manifold_ . 

A _curve_ is a map from a real interval to the manifold. We assume, unless otherwise stated, that the interval is an open neighborhood of 0. Given a curve, _γ_ : _t_ - _γ_ ( _t_ ) _∈ M_ , and a chart, _s_ , in the atlas, the curve _s ◦ γ_ : _t_ > _s_ ( _γ_ ( _t_ )) _∈ V_ is the _expression_ of the curve in _d_ the chart _s_ . If one expression (hence, all) is differentiable, then _t_ aS _dt[s][ ◦][γ]_[(] _[t]_[)] _[∈][V]_[is the] expression of the velocity at _t_ of the curve _γ_ in the chart _s_ . The vector space of all possible expressions of velocities for curves passing through a given _p ∈ M_ is the expression of the _tangent space_ at _p_ . 

## _2.1. Affine Space_ 

The open probability simplex _P>_ (Ω) and the probability simplex are, respectively, an open convex subset and a closed convex subset of the generated affine plane, 

**==> picture [276 x 22] intentionally omitted <==**

where _A_ (Ω) consists of all vectors in the vector space R[Ω] whose components sum to 1. Probability functions are non-negative and sum to 1. As _A_ (Ω) is an Euclidean space, the open probability simplex inherits Euclidean geometry. In some contexts, it is useful to relax the non-negativity constraint and allow the “probabilities” to take on negative values while maintaining the sum-to-one condition. By allowing _v_ ( _x_ ) to be negative, we extend our consideration from the standard probability simplex to a larger space. 

**Example 1.** _Consider a simple three-dimensional space with outcomes_ Ω = _{_ 1, 2, 3 _}. A probability vector v ∈_ R[3] _in this space might look like v_ = ( _v_ 1, _v_ 2, _v_ 3) _, where v_ 1 + _v_ 2 + _v_ 3 = 1 _. For standard probabilities, we require v_ 1, _v_ 2, _v_ 3 _≥_ 0 _. However, if we relax this constraint, v_ 1, _v_ 2, _v_ 3 _can assume negative values as long as they sum to 1. In the plot of Figure 1, the blue triangle represents the standard probability simplex where v_ 1, _v_ 2, _v_ 3 _≥_ 0 _. The red points represent example vectors in the generalized affine space, including one where v_ 3 _is negative and another where v_ 1 _exceeds 1._ 

**Figure 1.** The blue triangle represents the probability simplex. The red points represent vectors in the generalized affine space, including points with negative values or values exceeding 1. 

_Axioms_ **2024** , _13_ , 823 

5 of 34 

**Example 2.** _A_ score function _, S, can be defined on the space of these generalized probability vectors. For a given vector, v, and an outcome, x, the score S_ ( _v_ , _x_ ) _quantifies how well the vector v predicts the outcome x. A common example of a score function is the Brier score [15], defined as follows:_ 

**==> picture [127 x 23] intentionally omitted <==**

_where δx is the indicator function of x, that is, 1 if y_ = _x and 0 otherwise._ 

The following definition, due to [16], extends the notion of geometry on a hyperplane to a more general situation. 

**Definition 1** (Weyl’s affine space) **.** _Given a set, M, and a real finite-dimensional vector space, V, an affine space,_ ( _M_ , _V_ , _[−→] ··_ ) _, consists of_ displacement mapping _,_ 

**==> picture [122 x 14] intentionally omitted <==**

_such that the following two assumptions hold._ 

_1. For each point p ∈ M, the partial mapping sp_ : _M ∋ q �→ sp_ ( _q_ ) = _[−→] pq is injective (one-to-one) with the open image sp_ ( _M_ ) _._ 

_2. Given points p, q, and r, the displacement vectors satisfy the parallelogram law,_ 

_−→ pq_ + _[−→] qr_ = _[−→] pr_ . 

Property 1 ensures that, for a fixed point, _p_ , the mapping from points in _M_ to the vector space, _V_ , via the displacement vector _[−→] pq_ does not map different points to the same vector. In the language of differential geometry, the mapping _sp_ is a _chart_ , and _v_ = _sp_ ( _q_ ) is the coordinate of _q_ in the _p_ -chart. As _sp_ ( _p_ ) = 0, we will say that _p_ is the _origin_ of the chart. The inverse chart, also called a _patch_ , is _s[−] p_[1][:] _[s][p]_[(] _[M]_[)] _[ →][M]_[.] 

Property 2 means that the vector displacement from _p_ to _r_ is the same as the sum of the vector displacement from _p_ to _q_ and from _q_ to _r_ ; see Figure 2. This property ensures that adding displacements is consistent with the geometric intuition of moving along a path from one point to another via an intermediate point. In terms of the charts, 

**==> picture [247 x 12] intentionally omitted <==**

**==> picture [234 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
q<br>−→<br>r qr<br>p<br>M V<br>O<br>−→<br>pr<br>−→pq<br>**----- End of picture text -----**<br>


**Figure 2.** Parallelogram law in an affine space. 

In particular, we have _sp_ ( _p_ ) = _[−→] pp_ = 0; hence _sp_ is the chart centered at _p_ . Also, _sp_ ( _q_ ) + _sq_ ( _p_ ) = 0. The change-of-chart transformation from origin _p_ to origin _q_ follows from Equation (7). 

**==> picture [328 x 15] intentionally omitted <==**

The change-of-chart from origin _p_ to origin _q_ is the translation via _sq_ ( _p_ ) = _−sp_ ( _q_ ). 

## _2.2. Affine Manifold_ 

In the affine space ( _M_ , _V_ , _[−→] ··_ ), the displacement ( _p_ , _q_ ) _�→[−→] pq_ defines a system of charts, _sp_ : _M ∋ q �→[−→] pq_ , as _p_ varies in _M_ . Each _sp_ is one-to-one, and the change-of-charts (8) are translations; hence, they are highly smooth. The _affine manifold_ is defined by the atlas 

_Axioms_ **2024** , _13_ , 823 

6 of 34 

of charts _sp_ : _M → V_ , _p ∈ M_ . The affine manifold differs from the _C[k]_ -manifold that it generates because the former is not maximal, while the latter is. Any vector basis of _V_ provides a version of the affine space, where the vector space is a real vector space of parameters, producing a faithful parametrization of _M_ . 

Consider a curve, _t �→ ρ_ ( _t_ ) _∈ M_ , in the affine manifold. For any reference point _p ∈ M_ , the curve _t �→ sp_ ( _ρ_ ( _t_ )) is the _sp_ -expression of the curve. The derivative _dt[d][s][p]_[(] _[ρ]_[(] _[t]_[))][ does not] depend on the choice of the point _p_ : 

**==> picture [209 x 22] intentionally omitted <==**

Thus, the derivative _[d] dt[s][p]_[(] _[ρ]_[(] _[t]_[))][ is independent of the choice of] _[ p]_[ and is called the] _[ affine] velocity of the curve_ . It is denoted as 

**==> picture [80 x 22] intentionally omitted <==**

The vector space of all velocities evaluated at _t_ = 0 of all curves _t �→ ρ_ ( _t_ ) _∈ M_ , such that _ρ_ (0) = _p_ , is the _tangent space_ at _p_ of the affine manifold, namely 

**==> picture [280 x 14] intentionally omitted <==**

Conversely, given any _v ∈ V_ , the curve _t �→ s[−] p_[1][(] _[tv]_[)][has][affine][velocity] _[v]_[,][so][that] _T M_ = _V_ . _p_ 

**Example 3.** _Let us discuss a basic elementary example that is relevant in the statistical literature on the design of experiments and regression modeling. If we take as base set M the hyperplane A_ (Ω) _of Equation_ (6) _and as vector space the vector space parallel to the probability simplex, that is, the space of_ contrasts _,_ 

**==> picture [280 x 31] intentionally omitted <==**

_the displacement is[−→] pq_ = _q − p ∈ V. In fact,_ ∑ _x_ ( _q_ ( _x_ ) _− p_ ( _x_ )) = 1 _−_ 1 = 0 _. And the mapping sp_ ( _q_ ) = _q − p is one-to-one. The parallelogram law is_ ( _q − p_ ) + ( _r − q_ ) = ( _r − p_ ) _. The tangent space is defined in Equation_ (10) _. In the case with_ Ω = _{_ 1, 2, 3 _}, a vector basis of_ CO(Ω) _is_ 

**==> picture [147 x 11] intentionally omitted <==**

_so that_ 

**==> picture [282 x 37] intentionally omitted <==**

_The chart at p in parametric coordinates is_ 

**==> picture [134 x 25] intentionally omitted <==**

_Often, the interpretability of regression models depends on the suitable choice of vector space bases of_ CO(Ω) _and charts._ 

Interestingly, many types of affine manifolds on the open probability simplex are of statistical interest. They all use the space of contrasts (10) as vector space. Various vector bases of CO(Ω) are commonly used in applications. One option is to choose a component _a ∈_ Ω and use the _reduced basis_ ( _δx_ ) _x_ = _a_ . With this basis, the components of the projection of _v ∈_ CO(Ω) are ( _v_ ( _x_ ) _− v_ ( _a_ )) _x_ = _a_ . A second option is the _preferred point basis_ . Fix _a ∈_ Ω. If _v_ is a contrast, it holds that _v_ ( _a_ ) = _−_ ∑ _x_ = _a v_ ( _x_ ); hence _v_ = ∑ _x_ = _a v_ ( _x_ )( _δx − δa_ ) and ( _δx − δa_ ) _x_ = _a_ is a basis. 

_Axioms_ **2024** , _13_ , 823 

7 of 34 

The space of contrasts is a Euclidean space, for example, with the restriction of the inner product in R[Ω] . Other inner products can be used. While not part of the affine geometry, these metrics, applied to the vector space of contrasts, provide various useful instances of metric on the affine space; see Example 2. It is important to realize that the choice of an affine displacement and the choice of an inner product are independent modeling choices. 

**Example 4** (Open probability simplex) **.** _The construction in Example 3 is not feasible for the probability simplex because the image of the restricted mapping_ 

**==> picture [122 x 11] intentionally omitted <==**

_is closed. We can use the same construction as before if we restrict to the open probability simplex,_ 

**==> picture [263 x 11] intentionally omitted <==**

Aitchison’s Centered Log Ratio [5] 

In this section, a key notion for statistical usage of Aitchison’s geometry, namely the centered log ratio (CLR), is interpreted as a displacement. This allows for the interpretation of the moments of a random variable of the cumulant function in this framework. 

If _f_ and _f_ 1 = _k_ 1 _f_ are equivalent positive compositions, then log _f_ 1 = log _f_ + log _k_ 1. The logarithms of equivalent compositions differ by an additive constant. This remark suggests using a logarithmic scale by considering the set of positive probability functions _P>_ (Ω), the vector space of contrasts CO(Ω), _n_ = #Ω, and the _centered log ratio_ displacement 

**==> picture [329 x 27] intentionally omitted <==**

If _f_ is a composition and _ϕ_ is a random variable of Ω, then, if we define the E-notation to include normalization, 

**==> picture [258 x 27] intentionally omitted <==**

Let us check that all conditions for an affine manifold hold. The partial mapping at p is a chart with 

**==> picture [355 x 53] intentionally omitted <==**

The axioms for affine geometry are satisfied, as the equality _sp_ ( _q_ ) + _sq_ ( _r_ ) = _sp_ ( _r_ ) is easily checked, 

**==> picture [372 x 53] intentionally omitted <==**

The patch mapping is a non-parametric exponential model [17,18] (§ 5.5) in which the sufficient-statistics _v_ is a contrast. The convex mapping Ψ _p_ is sometimes called a cumulant function. The first and second derivatives of Ψ _p_ in the direction _h_ and the directions _h_ and _k_ , respectively, are (as computed in the references above), 

**==> picture [307 x 14] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

8 of 34 

The velocity of the curve _t �→ q_ ( _t_ ) is 

**==> picture [294 x 25] intentionally omitted <==**

where _q_ ˙( _t_ ) is the derivative computed in _A_ (Ω). The random variable _q_ ˙( _t_ )/ _q_ ( _t_ ) is called _Fisher’s score_ [18], and it has the remarkable property 

**==> picture [134 x 26] intentionally omitted <==**

In the reduced basis, with Ω = _{_ 1, . . . , _n}_ , each _j ̸_ = _n_ component of the CLR displacement becomes 

**==> picture [372 x 53] intentionally omitted <==**

## See [4] for a detailed treatment. 

Within Aitchison’s paradigm, we presented the idea of the centered log-ratio (CLR) transformation (12). Determining displacement mappings between probability distributions on the simplex depends critically on this transformation. By mapping compositions into a Euclidean space, the CLR makes the comparison and analysis of probability distributions easier in a way that makes sense with respect to the inherent geometry of the simplex (referring to the unique geometric properties of the probability simplex—a space that consists of probability distributions where all components are positive and sum to one). Aitchison geometry’s mathematical foundations are explored in more detail in Section 3.6 with special attention to how it relates to information geometry (IG). We discuss how Aitchison geometry may be considered a specific example of IG, simplifying the displacement mappings with a fixed reference chart and deriving important conclusions, including the parallelogram law that guarantees these mappings to be consistent over a wide range of distributions. A further explanation and detailed connections with the centered log-ratio transformation are provided in Section 3.6 below. 

## _2.3. Tangent Bundle_ 

The motivation for defining a manifold structure, _M_ , through an atlas, _A_ , is the availability of a coherent setup for performing calculus operations. A typical problem in our interest is minimizing a smooth scalar field _G_ : _M →_ R via a gradient-flow algorithm. To this end, we must consider points on the manifold and derivatives, which exist in a vector space attached to each point. 

The _tangent bundle TM_ is defined as a set of pairs, 

**==> picture [156 x 14] intentionally omitted <==**

where _TqM_ is the tangent space at _q_ , that is, the vector space of all possible velocities of curves through _q_ . The situation is straightforward in all the examples of affine manifolds we have seen up to now, as the tangent space identifies with the space of contrasts CO(Ω). 

**Example 5** (Exponential arc) **.** _Let t �→ p_ ( _t_ ) _be the exponential arc in Equation_ (4) _connecting the points q and r ∈P>_ (Ω) _. In the CLR affine manifold, we represent the two equivalent probability densities with the CLR patch centered at p, as in Equation_ (15) _,_ 

**==> picture [260 x 14] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

9 of 34 

_and hence, the arc t �→ p_ ( _t_ ) _is expressed in terms of a mixture of two random variables, v and w, and the convex mapping_ Ψ _p, that is, two canonical statistics and the cumulant function,_ 

**==> picture [313 x 15] intentionally omitted <==**

_The affine velocity is constant,_ 

**==> picture [230 x 22] intentionally omitted <==**

_The exponential arc is the line segment with constant velocity connecting q and r in the CLR affine geometry. The set of all possible velocities at a given point is an expression of the tangent space._ 

**Example 6** (Gradient of the KL-divergence) **.** _For any p ∈P>_ (Ω) _, the Kullback–Leibler divergence, in short KL-divergence (see [19] or § 3.3–4 in [9]), of q and p is the scalar field_ 

**==> picture [186 x 25] intentionally omitted <==**

_The patch at p for the CLR displacement is Equation_ (15) _; hence, the expression at p of the KL-divergence is_ 

**==> picture [286 x 19] intentionally omitted <==**

_The expression is defined on the vector space_ CO(Ω) _, and hence, we can compute the ordinary derivative in the direction h ∈_ CO(Ω) _using Equation (16) and q_ = e _[v][−]_[Ψ] _[p]_[(] _[v]_[)] _· p,_ 

**==> picture [374 x 69] intentionally omitted <==**

_As_ ( _np_ (e _[v][−]_[Ψ][1][(] _[v]_[)] _−_ 1) _∈_ CO(Ω) _, if we define the inner product of_ CO(Ω) _to be_ ( _v_ , _w_ ) _�→ ⟨v_ , _w⟩_ = E1[ _vw_ ] _, then np_ (e _[v][−]_[Ψ][1][(] _[v]_[)] _−_ 1) _is the_ gradient _of G,_ 

**==> picture [132 x 19] intentionally omitted <==**

_The gradient is also defined on the affine manifold as follows. If t �→ q_ ( _t_ ) _is a smooth curve with expression in the CLR, the expression at p is t �→_ CLR _p_ ( _q_ ( _t_ )) _, and the affine velocity is q⋆_ ( _t_ ) = _dtd_[CLR] _[p]_[(] _[q]_[(] _[t]_[)) =] _q[q]_[˙] ([(] _t[t]_ )[)] _[−]_[E][1] � _qq_ ˙(( _tt_ )) � _. Hence,_ 

**==> picture [245 x 22] intentionally omitted <==**

**Example 7** (Entropy) **.** _The expression of the entropy [19]_ 

**==> picture [217 x 25] intentionally omitted <==**

_in the chart at p becomes, using the first Equation_ (16) _,_ 

**==> picture [374 x 35] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

10 of 34 

_and hence, using the second Equation_ (16) _,_ 

**==> picture [393 x 101] intentionally omitted <==**

## **3. Affine Statistical Bundle** 

We define other affine geometries on the open probability simplex, using a richer atlas of charts and introducing an essential notion of duality. This approach highlights the relationship between our topic and Fisher’s statistics and Boltzmann and Gibbs’s statistical physics [20]. 

Our geometry definitions are kinematic, based on calculating the velocity and acceleration of curves. A one-dimensional statistical model is a curve, that is, a mapping, _I ∋ t �→ q_ ( _t_ ) _∈P_ (Ω), where _P_ (Ω) is the probability simplex on the finite sample space Ω, and _I_ is an open interval of R. Higher dimensional statistical models are treated according to the usual conventions of multivariate analysis. 

## _3.1. Fisher’s Score_ 

As _P_ (Ω) _⊂_ R[Ω] , the affine velocity _t �→ q_ ˙( _t_ ) is well defined and takes values in the space of contrasts CO(Ω), as shown in the previous section. 

Smooth curves in R[Ω] , whose values stay in the probability simplex, have a notable property related to their support. If the curve stays in the open simplex, then the support is Ω; that is, _q_ ( _x_ ; _t_ ) _̸_ = 0 for all _x ∈_ Ω and all _t ∈ I_ [21]. 

Otherwise, the curve hits the boundary of the probability simplex; that is, there exists at least a pair, ( _a_ , _t_[¯] )) _∈_ Ω _× I_ , such that _q_ ( _a_ ; _t_[¯] ) = 0. This implies _q_ ( _a_ ; _t_ ) _≥ q_ ( _a_ , _t_[¯] ); hence, _q_ ˙( _a_ ; _t_[¯] ) = 0 [3]. In conclusion, 

**==> picture [113 x 11] intentionally omitted <==**

In the language of measure theory, _q_ ˙( _t_ ) is absolutely continuous with respect to _q_ ( _t_ ), _q_ ˙( _t_ ) _≪ q_ ( _t_ ) [22]. 

Hence, given any R[Ω] -smooth curve in the probability complex, there exists a curve, _t �→ q⋆_ ( _t_ ) _∈_ RΩ, called _Fisher’s score_ , such that the following applies: 

**==> picture [69 x 13] intentionally omitted <==**

Fisher’s score has two remarkable properties [23]. First, if _q_ ( _x_ ; _t_ ) _>_ 0, _t ∈ I_ , then 

and second, 

**==> picture [315 x 68] intentionally omitted <==**

Specifically, if _t �→ q_ ( _t_ ) _∈P>_ (Ω) (the open probability simplex), then Fisher’s score is given by _q⋆_ ( _t_ ) = _dtd_[log] _[ q]_[(] _[t]_[)][ .] 

There are many statistical reasons to take the Fisher score as a proper notion of the parameter rate of change in a statistical model. See the textbook [18] (Ch. 4) and the monograph [22]. 

_Axioms_ **2024** , _13_ , 823 

11 of 34 

## _3.2. Statistical Bundle and Parallel Transports_ 

For the general notion of a bundle, see, for example, [14]. The previous discussion leads us to consider, for each positive probability function _q ∈P>_ (Ω), the vector space of _q-contrasts_ , that is, the random variables that are centered for _q_ , 

**==> picture [278 x 32] intentionally omitted <==**

The _statistical bundle SP>_ (Ω) is the bundle _SP>_ (Ω) _→P>_ (Ω) of _q_ -contrasts, 

**==> picture [313 x 20] intentionally omitted <==**

Each fiber _SqP>_ (Ω) = _Bq_ will represent all Fisher’s scores at the point _q_ . In turn, the Fisher’s score will be interpreted as velocities. 

**Example 8.** _The plot in Figure 3 illustrates the probability simplex for two outcomes, the point q_ = _{q_ (1), _q_ (2) _} within the simplex, and the vectors u_ 1 _and u_ 2 _representing q-contrasts._ 

**==> picture [322 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
 q (1) + q (2) = 1<br> qu ((11)) q∧ (1) q (+2) u≥ (2)0 q (2) = 0<br>1<br>u = {u (1),  u (2) } q = {q (1),  q (2) }<br>1<br>B ( q )<br>SP{ (1, 2) }<br>**----- End of picture text -----**<br>


**Figure 3.** Example 8: the vector _u_ is an element of the fiber at point _q_ of the probability simplex. 

Each fiber _Bq_ is equipped with a natural _inner product_ , the covariance at _q_ , 

**==> picture [136 x 13] intentionally omitted <==**

This inner product measures the angles and lengths of vectors within each fiber, contributing to the metric structure of the statistical bundle. The mapping ( _q_ , _u_ , _v_ ) _�→⟨u_ , _v⟩q_ is the _metric_ of the statistical bundle. 

**Example 9** (Fisher’s metric) **.** _Given a smooth curve, t �→ q_ ( _t_ ) _∈P>_ (Ω) _, the Fisher’s score q⋆_ ( _t_ ) = _dtd_[log] _[ q]_[(] _[t]_[) =] _[q]_[˙][(] _[t]_[)][/] _[q]_[(] _[t]_[)] _[ provides a curve in the statistical bundle [][24][],]_ 

**==> picture [117 x 13] intentionally omitted <==**

_The variance in the Fisher’s score is called_ Fisher’s information _[25,26],_ 

**==> picture [240 x 31] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

12 of 34 

Each fiber is a different vector space in the statistical bundle. Because of that, the mapping _t �→_ ( _q_ ( _t_ ), _q⋆_ ( _t_ )) _∈ SP>_ (Ω) requires a special handling of differentiation with a construction called _connection_ . We define this notion as follows. 

**Definition 2** (Parallel transport) **.** _A_ parallel transport _of the statistical bundle SP>_ (Ω) _is a collection of bijective linear mappings between the fibers_ 

**==> picture [258 x 14] intentionally omitted <==**

_such that, for all p_ , _q_ , _r ∈P>_ (Ω) _, the_ cocycle relation _holds,_ 

**==> picture [226 x 15] intentionally omitted <==**

Given a parallel transport, if _v ∈ SqP>_ (Ω) is proportional to U _[q] p[u]_[,] _[ u][ ∈][S] p[P] >_[(][Ω][)][, we] say that _u_ and _v_ are _parallel_ . 

## _3.3. Affine Bundle_ 

Here, we generalize Weyl’s definition of affine space to adapt it to the statistical bundle. The novelty is that there is a different vector space at each point of the space. 

**Definition 3.** _Consider the statistical bundle SP>_ (Ω) _and a cocycle of parallel transports,_ U _[q] p[,] p_ , _q ∈P>_ (Ω) _. An_ affine displacement _is a mapping,_ 

**==> picture [222 x 12] intentionally omitted <==**

_such that the following applies:_ 

_1. For each fixed p, the mapping sp_ : _q �→ sp_ ( _q_ ) _is 1-to-1, and it has an open image; 2. The_ parallelogram law _holds,_ 

**==> picture [109 x 14] intentionally omitted <==**

The affine displacement on the statistical bundle provides an atlas of charts, _sp_ , _p ∈ P>_ (Ω). Each chart is a local coordinate system around the origin point _p_ . The _change-ofchart map_ is _sp ◦ sq[−]_[1][.][At] _[ ρ]_[ =] _[s][−] q_[1][(] _[w]_[)][,] _[ w][ ∈][S][q][P][>]_[(][Ω][)][, it holds that] 

**==> picture [320 x 15] intentionally omitted <==**

The change-of-origin map restricts an affine map to R[Ω] , whose linear part is the parallel transport (Figure 4). 

**==> picture [339 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>q<br>w<br>v<br>B<br>p<br>l<br>p q<br>**----- End of picture text -----**<br>


**Figure 4.** In the affine statistical manifold (the triangle), each point, for example, _p_ , corresponds to a reference space, _Bp_ . Given two reference spaces, _Bp_ and _Bq_ , the same point, _l_ , has two different coordinates, _v ∈ Bp_ and _w ∈ Bq_ . 

_Axioms_ **2024** , _13_ , 823 

13 of 34 

**Example 10** (Barycenter and convex combination) **.** _Given points q_ 1, . . . , _qn ∈P>_ (Ω) _, coefficients λ_ 1, . . . , _λn with_ ∑ _i λi_ = 1 _, and a reference, p, the convex combination of p-coordinates,_ ∑ _i λisp_ ( _qi_ ) _, is the p-coordinate of a point, called the_ barycenter _,_ 

**==> picture [248 x 30] intentionally omitted <==**

_which does not depend on p. In fact, for q_ = _p, we can use the change-of-chart of Equation_ (22) _to obtain_ 

**==> picture [374 x 65] intentionally omitted <==**

**Example 11** (Single fiber) **.** _If s is an affine displacement with parallel transports_ U _[q] p[, and]_[ (][1][)] _[ is] the uniform probability function, then_ 

**==> picture [88 x 16] intentionally omitted <==**

_defines an affine displacement with vector space_ CO(Ω) _. In fact,_ 

**==> picture [374 x 38] intentionally omitted <==**

_3.4. Velocity and Natural Gradient_ 

If _t �→ q_ ( _t_ ) is a curve in the open probability simplex, and _sp_ is a chart according to Definition 3, the expression of the velocity in the chart is, then, 

**==> picture [121 x 22] intentionally omitted <==**

If we change the chart and use the second equations in Definition 3, the change in the expression of the velocity follows the parallel transport 

**==> picture [123 x 22] intentionally omitted <==**

Let us define an intrinsic notion of velocity using the so-called _moving frame_ . 

**Definition 4** (Velocity) **.** _The_ velocity _of the curve t �→ q_ ( _t_ ) _is_ 

**==> picture [116 x 22] intentionally omitted <==**

_which does not depend on p. The velocity provides a lifting of the curve to the statistical bundle,_ 

**==> picture [122 x 13] intentionally omitted <==**

The function _F_ : _P>_ (Ω) _→_ R is smooth if its expression in the chart at _p_ , _Fp_ = _F ◦ s[−] p_[1][:] _[S][p][P][>]_[(][Ω][)] _[→]_[R][is][differentiable.][Let][us][recall][that][the][gradient] _[∇][f]_[of][a] smooth function, _f_ : R _[n] →_ R, is defined by the equation _dt[d][f]_[ (] _[x]_[(] _[t]_[))][=] _[∇][f]_[ (] _[x]_[(] _[t]_[))] _[ ·][x]_[˙][(] _[t]_[)][ for] all smooth curves in R _[n]_ . The same definition applies to any other inner product. After Amari, we call the _natural gradient_ the gradient associated with the inner product on the statistical bundle. 

_Axioms_ **2024** , _13_ , 823 

14 of 34 

_⋆ ⋆_ **Definition 5** (Natural gradient) **.** _If t �→ q_ ( _t_ ) _∈P>_ (Ω) _, q_ = _q_ (0) _and q_ = _q_ (0) _, and FP>_ (Ω) _→_ R _is smooth, then_ 

**==> picture [383 x 44] intentionally omitted <==**

_where q �→_ grad _F_ ( _q_ ) _is the_ natural gradient _of F; that is,_ grad _F_ ( _q_ ) _is the element of SqP>_ (Ω) _identified with the linear operator dF_ (0) _in the covariance inner product._ 

**Definition 6** (Exponential of a parallel transport) **.** _Assume that, for each given_ ( _q_ , _v_ ) _∈ SP>_ (Ω) _, the differential equation_ 

**==> picture [112 x 17] intentionally omitted <==**

_has a unique global solution. Such a curve is_ auto-parallel _, q⋆_ ( _t_ ) = _α_ ( _t_ )U _qq_ (( _ts_ )) _q⋆_ ( _s_ ) _, with_ relative velocity _α_ ( _t_ ) = 1 _. The mapping_ 

**==> picture [231 x 14] intentionally omitted <==**

_is called the_ exponential _of the affine bundle._ 

The previous construction, leading from the affine bundle to the moving frame velocity and the natural gradient, is essential to the non-parametric version of Amari’s information geometry. This specific construction is qualified below as the dually affine geometry of the probability simplex. It admits a number of immediate generalizations. In particular, it can be used to define a second-order calculus, as sketched in the example below. 

**Example 12** (Second-order affine geometry) **.** _As a basic set, let us assume the statistical bundle with the cocycle of parallel transports and, as a vector space, the product of the fibers. The following equation defines a displacement:_ 

**==> picture [262 x 14] intentionally omitted <==**

**==> picture [373 x 12] intentionally omitted <==**

**==> picture [126 x 25] intentionally omitted <==**

_In particular, if v_ ( _t_ ) = _q⋆_ ( _t_ ) _, the second-order derivative is defined in the chart at p by_ 

**==> picture [140 x 25] intentionally omitted <==**

In the moving frame, the _acceleration_ is defined by 

**==> picture [252 x 28] intentionally omitted <==**

## _3.5. Dually Affine Atlases on the Open Probability Simplex_ 

According to the works of Amari [1] and Amari and Nagaoka [2], there are two main types of affine geometry on the probability simplex, the exponential one and the mixture one. We axiomatically describe such geometries via the notion of the statistical bundle endowed with parallel transport. This approach was initially presented in [27]. Each fiber of the statistical bundle is endowed with the covariance inner product to identify each fiber with its dual. In this identification, the two parallel transports are dual to each other. 

_Axioms_ **2024** , _13_ , 823 

15 of 34 

- **Theorem 1** (Exponential transport and mixture transport) **.** 

- _1. The equation_ 

> _e_ U _[q] p_[:] _[S] p[P] >_[(][Ω][)] _[ ∋][u][ �→][u][ −]_[E] _q_[[] _[u]_[]] _[ ∈][S] q[P] >_[(][Ω][)] 

_defines a cocycle of parallel transports. It is the_ exponential transport _. 2. The equation_ 

**==> picture [171 x 22] intentionally omitted <==**

_defines a cocycle of parallel transports. It is the_ mixture transport _._ 

_3. The exponential transport and the mixture transports are dual to each other in the covariance pairing. Namely, if u ∈ SpP>_ (Ω) _and v ∈ SqP>_ (Ω) _,_ 

**==> picture [119 x 21] intentionally omitted <==**

**Proof.** All checks for Definition 2 are immediate. The duality follows from 

**==> picture [339 x 25] intentionally omitted <==**

For each parallel transport, we define an affine displacement. Each affine displacement maps the open probability simplex onto a vector space of contrasts. Conversely, the inverse maps are statistical models parametrized by a vector space of contrasts. The normalizing constants are interpreted in terms of statistical information. 

- **Theorem 2** (Exponential chart and mixture chart) **.** 

- _1. The mapping_ 

**==> picture [304 x 25] intentionally omitted <==**

_is an affine displacement for the exponential parallel transport Theorem 1 item 1. The inverse of the_ exponential chart _sp is the exponential model_ 

**==> picture [251 x 15] intentionally omitted <==**

_2. The mapping_ 

**==> picture [249 x 22] intentionally omitted <==**

_is an affine displacement for the mixture displacement Theorem 1 item 2. The inverse of the_ mixture chart _ηp is the mixture model_ 

**==> picture [207 x 15] intentionally omitted <==**

## **Proof.** 

1. The generalized parallelogram law for the exponential displacement is 

**==> picture [351 x 81] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

16 of 34 

2. The generalized parallelogram law for mixture displacement is 

**==> picture [271 x 25] intentionally omitted <==**

The inverse exponential chart is defined on all _p_ -contrasts by 

**==> picture [160 x 15] intentionally omitted <==**

where 

**==> picture [83 x 12] intentionally omitted <==**

_K_ is usually called the cumulant generating functional of _v_ with respect to _p_ . The inverse chart _s[−] p_[1][(] _[v]_[)][maps][a][vector] _[p]_[-contrast] _[v]_[back][to][a][probability][function.][The][expression] exp( _v − Kp_ ( _v_ )) _· p_ involves an exponential map adjusted by a normalization factor _Kp_ ( _v_ ). The quantity exp( _v − Kp_ ( _v_ )) ensures that the resulting vector after exponentiation is properly normalized to be a valid probability distribution. The term _ep_ ( _v_ ) = _s[−] p_[1] denotes this normalized exponential family. 

Kullback–Leibler Divergence 

The _Kullback–Leibler divergence_ between two positive probability functions, _p_ and _q_ , is D( _p ∥q_ ) = E _p_ �log _q[p]_ �. Both partial functions 

**==> picture [149 x 12] intentionally omitted <==**

are commonly used in statistical optimization procedures. The primary reference is [28]. 

**Example 13** (Expression of KL divergence) **.** _Let us find an expression for the Kullback–Leibler divergence by using a mixture chart on the first variable and the exponential chart on the second variable. Namely, if p_ = (1 + _u_ ) _· m and q_ = e _[v][−][K][m]_[(] _[v]_[)] _· m, the expression in the charts at m is_ 

**==> picture [247 x 11] intentionally omitted <==**

**==> picture [124 x 25] intentionally omitted <==**

**==> picture [264 x 27] intentionally omitted <==**

**==> picture [143 x 12] intentionally omitted <==**

_where Hm_ ( _u_ ) = E _m_ [(1 + _u_ ) log(1 + _u_ )] _._ 

_If we let p_ = _q in Equation (26), that is,_ 1 + _u_ = e[(] _[v][−][K][−][m]_[)(] _[v]_[)] _and_ E _m_ [ _u_ ] = E _m_ [ _v_ ] = 0 _, then Hm_ ( _u_ ) + _Km_ ( _v_ ) = _⟨u_ , _v⟩m._ 

**Example 14** (Divergence and displacement) **.** _In Equation_ (26) _, we can turn back to the probability densities to obtain the_ generalized parallelogram theorem _[29]_ 

**==> picture [363 x 12] intentionally omitted <==**

_In particular, the_ generalized Pythagorean _theorem holds,_ 

**==> picture [330 x 12] intentionally omitted <==**

The cumulant function _Kp_ ( _u_ ) is central to the theory. It is the exponential normalizing constant of the exponential model _ep_ ( _u_ ) = e _[u][−][K][p]_[(] _[u]_[)] _· p_ , and it equals D� _p ∥ep_ ( _u_ )�. Moreover, it has remarkable computational properties, summarized in the following theorem. 

_Axioms_ **2024** , _13_ , 823 

17 of 34 

Notice that it is a formalism well known in statistical physics, where it is used to discuss the Gibbs–Boltzmann distribution. See, for example, [30]. 

**Theorem 3** (Calculus of the cumulant functional) **.** 

_1. The derivative of Kp at v in the direction h is_ 

**==> picture [279 x 29] intentionally omitted <==**

_2. The second derivative of Kp at v in the directions h and k is_ 

**==> picture [362 x 48] intentionally omitted <==**

_3. The third derivative of Kp at v in the directions h_ 1, _h_ 2, _and h_ 3 _is_ 

**==> picture [285 x 19] intentionally omitted <==**

_4. The cumulant functional Kp is convex, and its gradient is the covariance at p given by ∇Kp_ ( _v_ ) = _[e][p] p_[(] _[v]_[)] _−_ 1 _. The inverse gradient mapping is_ 

**==> picture [253 x 14] intentionally omitted <==**

_and the convex conjugate is_ 

**==> picture [362 x 21] intentionally omitted <==**

**Proof.** The proof of the first three items follows through direct computation. 1. 

**==> picture [350 x 85] intentionally omitted <==**

2. 

**==> picture [351 x 95] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

18 of 34 

3. 

**==> picture [375 x 142] intentionally omitted <==**

4. The convexity follows from items 1 and 2. The last statement is, in essence, a summary of the theorem itself. 

## _3.6. Aitchison Geometry and Information Geometry_ 

In Section Aitchison’s Centered Log Ratio [5], we have shown that the Aitchison geometry of the probability simplex is an instance of affine geometry. The present section shows how to interpret the same formalism as using a particular atlas on the statistical bundle. For clarity, we admit some overlapping between the two sections. 

Let _P>_ (Ω) be the positive probability simplex over a finite set Ω, and let _TP>_ (Ω) be its tangent space. Define the displacement mapping, _sp_ : _P>_ (Ω) _→ TP>_ (Ω), for a reference point, _p ∈P>_ (Ω), and any _q ∈P>_ (Ω) as follows: 

**==> picture [150 x 29] intentionally omitted <==**

where log _[q] p_[denotes the element-wise logarithm of the ratio of the probability distributions] _q_ and _p_ , and ∑ _y∈_ Ω #1Ω[log] _[q] p_[(] ( _[y] y_[)] )[is the average of the log ratios over all elements] _[ y][ ∈]_[Ω][.][This] can also be written as follows: 

**==> picture [259 x 25] intentionally omitted <==**

where E�log _[q] p_ � is the uniform expectation of the log ratio. 

The critical difference with exponential charts is the centering term, which is an expectation with respect to the uniform measure instead of the initial point, _p_ . 

The displacement mapping _sp_ of Equation (31) is surjective. For every _u ∈ TP>_ (Ω), there exists a _q ∈P>_ (Ω), such that _sp_ ( _q_ ) = _u_ . The inverse mapping _s[−] p_[1] is given as follows: 

**==> picture [123 x 15] intentionally omitted <==**

where the normalizing function _K_ ( _u_ ) is defined as follows: 

**==> picture [170 x 23] intentionally omitted <==**

Notice the relationship between the two forms of the normalizing constant: 

**==> picture [87 x 25] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

19 of 34 

This means that the normalizing constant _K_ ( _u_ ) can be expressed as the _p_ -expectation of the log ratio of the probability distributions _q_ and _p_ . 

The parallelogram law holds true: 

**==> picture [306 x 25] intentionally omitted <==**

This law states that the sum of the centered log ratios between distributions _q_ and _p_ , and _r_ and _q_ , is equal to the centered log ratio between _r_ and _p_ . It ensures consistency in the displacement mappings across different distributions. 

**Example 15** (Uniform Distribution Case) **.** _If p is uniform, that is, p_ ( _x_ ) = _D[−]_[1] _, where D_ = #Ω _(the number of elements in the set_ Ω _), then the displacement mapping is simplified as follows:_ 

**==> picture [282 x 35] intentionally omitted <==**

_The displacement mapping sD−_ 1 ( _q_ )( _x_ ) _involves taking the log of q_ ( _x_ ) _and subtracting the average log of all q_ ( _y_ ) _. This is simplified to the_ log _of q_ ( _x_ ) _, divided by the geometric mean of q_ ( _y_ ) _over all y ∈_ Ω _._ 

A few comments are relevant at this point. The particular chart, derived from the displacement mapping when _p_ is uniform, matches a chart in the exponential atlas used in information geometry. Exponential affine geometry, which deals with exponential families of probability distributions, and Aitchison geometry, which deals with compositional data, are fundamentally the same, but they are represented differently. The tangent space is viewed as a statistical bundle in the exponential affine geometry. In Aitchison geometry, it is viewed as the tangent space of the simplex. This observation highlights the equivalence of these geometric frameworks when analyzing probability distributions or compositional data. 

## 3.6.1. Mapping of n-Sequences 

In Aitchison’s geometry, the coordinates given in the chart above are called centered log-ratio CLR coefficients. In the present section, the CLR map transforms a set of (data) points in the (interior of the) simplex into vectors with #Ω _−_ 1 real-valued components. Statistical models for compositional data are often built and interpreted onto this set of transformed vectors. See, for example, [4,5]. 

Any _n_ -sequence (n-sample) _q_ 1, . . . , _qn ∈P>_ (Ω) is mapped to an _n_ -sequence in the space of coordinates (contrasts) via the CLR operation as follows: 

**==> picture [202 x 12] intentionally omitted <==**

The mapping translates the original probability distributions in the simplex _P>_ (Ω) into coordinates in the tangent space _TP>_ (Ω). 

The _space of contrasts TP>_ (Ω) is a vector space with an _inner product_ defined as follows: 

**==> picture [126 x 11] intentionally omitted <==**

In the space of contrasts, _⟨u_ , _v⟩_ denotes the inner product of vectors _u_ and _v_ , E( _uv_ ) represents the expected value of their product, and Cov( _u_ , _v_ ) represents their covariance. This inner product allows the computations required by us to perform all computations that require a vector-space structure: (1) vector addition and scalar multiplication are well defined in _TP>_ (Ω); (2) the inner product induces a norm, making _TP>_ (Ω) a normed 

_Axioms_ **2024** , _13_ , 823 

20 of 34 

vector space; and (3) it can compute angles between vectors and project one vector onto another using this inner product. 

In the compositional data literature, the formalism described above is called a _Bayes space_ . See, for example, [6]. 

## 3.6.2. Mean, Variance, Velocity, and Velocity Curve 

When data are analyzed, providing statistics (data summaries) such as the mean and variances is essential. In Aitchison geometry, these are computed into the tangent space. To fully appreciate their meaning, we highlight that the mean in _TP>_ (Ω) is a function of geometric means in the original simplex, _P>_ (Ω). 

The _sample mean_ of _n_ sequences in centered log-ratio (CLR) coordinates is given as follows: 

**==> picture [359 x 99] intentionally omitted <==**

It can also be written as follows: 

**==> picture [230 x 50] intentionally omitted <==**

The _sample variance_ is based on the squared norm: 

- _⟨_ CLR( _q_ ), CLR( _p_ ) _⟩_ = E(CLR( _q_ )CLR( _r_ )) = E(log _q_ log _r_ ) _−_ E(log _q_ )E(log _r_ ) = Cov(log _q_ , log _r_ ) . 

For CLR-transformed distributions, _⟨_ clr( _q_ ), clr( _p_ ) _⟩_ denotes their inner product, E(clr( _q_ )clr( _r_ )) is the expectation of their product, E(log _q_ log _r_ ) is the expectation of the product of log-transformed distributions, E(log _q_ )E(log _r_ ) is the product of their expectations, and Cov(log _q_ , log _r_ ) represents their covariance. 

A statistical model is a curve into _P>_ (Ω), often inverse-mapped from a statistical bundle in _TP>_ (Ω). In turn, the statistical bundle is estimated from some CLR-transformed data points. 

Most differential algorithms for model estimation and optimization are based on the computation of the parametric rate of change of statistics, which, in turn, are based on the computation of velocities, accelerations, and gradients. 

The _velocity_ is as follows: 

**==> picture [191 x 25] intentionally omitted <==**

where _[D][d] dt[q]_[(] _[t]_[)][ represents the velocity of the distribution] _[ q]_[(] _[t]_[)][,] _dt_[clr][(] _[q]_[(] _[t]_[))][ is the time deriva-] tive of the clr-transformed distribution _q_ ( _t_ ), _[q] q_[˙][(] ( _[t] t_[)] )[denotes the element-wise derivative of] _q_ ( _t_ ) divided by _q_ ( _t_ ), and E� _qq_ ˙(( _tt_ )) � is the expectation of _[q] q_[˙][(] ( _[t] t_[)] )[,][ensuring][that][the][result][has] null expectation. 

_Axioms_ **2024** , _13_ , 823 

21 of 34 

The _acceleration_ is defined in the usual way. The velocity curve _t �→ dt[D][q]_[(] _[t]_[)][ is a curve in] a vector space, and its derivative is the acceleration, 

**==> picture [234 x 31] intentionally omitted <==**

In this context, _dtd dtD[q]_[(] _[t]_[)][denotes][the][acceleration][of][the][distribution] _[q]_[(] _[t]_[)][,][with] _[q] q_[¨][(] ( _[t] t_[)] ) ˙ 2 representing the element-wise second derivative of _q_ ( _t_ ) normalized by _q_ ( _t_ ), � _qq_ (( _tt_ )) � as the ¨ ˙ 2[�] square of the element-wise first derivative term and E� _qq_ (( _tt_ )) _[−]_ � _qq_ (( _tt_ )) � as the expectation of the acceleration term, ensuring that the result is centered. Notice that the velocity is a deviation from a mean value in the uniform probability. The corresponding intensity is the variance of _dt[d]_[log] _[ q]_[(] _[t]_[)][ in the uniform probability.][This is] a legitimate and consistent estimation of the rate of variation, which is different from the more standard estimation using Fisher’s information, which is a variance computed in the current probability, not the uniform probability. 

The curves of zero acceleration are the curves of constant velocity. Such curves are commonly called _geodesics_ . A geodesic from _p_ = CLR( _u_ ) and initial velocity _v_ has the following form: _q_ ( _t_ ) = CLR _[−]_[1] ( _tv_ + _u_ ) = exp( _tu − Kp_ ( _u_ )) _· p_ , 

where CLR _[−]_[1] denotes the inverse centered log-ratio invertible chart, _u_ represents the initial point in CLR coordinates, _v_ indicates the initial velocity in CLR coordinates, _Kp_ ( _u_ ) serves as the normalizing constant, and exp( _tu − Kp_ ( _u_ )) _· p_ defines the geodesic point at time _t_ . 

Most optimization algorithms look for a critical point of a scalar field, that is, a point where the gradient is null. Given a definition of the inner product in the vector space of an affine space, the gradient of a real function Φ on the base set (scalar field) is a mapping grad Φ from the base set to the vector space or the tangent space, that is, a vector field, such that, for all smooth curves _q_ ( _t_ ), the following holds: 

**==> picture [167 x 25] intentionally omitted <==**

where grad Φ denotes the gradient of Φ, mapping from the base set to the tangent space to create a vector field. For a smooth curve, _q_ ( _t_ ), _dt[d]_[Φ][(] _[q]_[(] _[t]_[))][ represents the time derivative of] Φ along _q_ ( _t_ ), while the inner product �grad Φ( _q_ ( _t_ )), _dt[D][q]_[(] _[t]_[)] � quantifies the rate of change of Φ in the direction of the velocity _dt[D][q]_[(] _[t]_[)][.] 

In Aitchison geometry, if CLR( _q_ ( _t_ )) = _u_ ( _t_ ) and _q_ ( _t_ ) = CLR _[−]_[1] ( _u_ ( _t_ )), then the following applies: 

**==> picture [424 x 26] intentionally omitted <==**

The composition Φ _◦_ CLR _[−]_[1] represents the function Φ applied to the inverse CLR transformation, where E grad Φ _◦_ CLR _[−]_[1] ( _u_ ( _t_ )) _u_ ˙( _t_ ) denotes the expected value of the � � product of the gradient of Φ composed with CLR _[−]_[1] , and the derivative of _u_ ( _t_ ); #1Ω[∑] _[x][∈]_[Ω] represents the average over all elements _x_ in Ω, with grad Φ _◦_ CLR _[−]_[1] ( _u_ ( _x_ ; _t_ )) being the gradient of Φ composed with CLR _[−]_[1] at the point _u_ ( _x_ ; _t_ ), and _u_ ˙( _x_ ; _t_ ) denoting the time derivative of _u_ ( _x_ ; _t_ ). 

It follows that 

**==> picture [220 x 25] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

22 of 34 

or, equivalently, 

1 #Ω[grad][ Φ][(] _[q]_[) =] _[ ∇]_[(][Φ] _[ ◦]_[CLR] _[−]_[1][)] _[ ◦]_[CLR ,] 

_∂_ where[represents][the][partial][derivative][of][Φ] _[ ◦]_[CLR] _[−]_[1][with][respect] _∂u_ ( _x_ )[Φ] _[ ◦]_[CLR] _[−]_[1][(] _[u]_[)] to _u_ ( _x_ ), #1Ω[grad][ Φ] _[ ◦]_[CLR] _[−]_[1][(] _[u]_[)(] _[x]_[)][is][the][averaged][gradient][of][Φ][composed][with][CLR] _[−]_[1] at _u_ ( _x_ ), _∇_ (Φ _◦_ CLR _[−]_[1] ) denotes the gradient of the composed function Φ _◦_ CLR _[−]_[1] , and _∇_ (Φ _◦_ CLR _[−]_[1] ) _◦_ CLR is the gradient applied to CLR-transformed variables. 

## **4. Product-Sample Spaces** 

The traditional presentation of the probability simplex’s convex geometry uses the language of linear programming (LP); see, for example, [7] (Ch. IV). The following section is an aside about LP from [7] (§ IV.10) to be skipped if the reader knows this topic. 

## _4.1. Short Recap of Linear Programming_ 

Linear programming deals with function optimization under equality and inequality constraints, where both the objective function and the constraints are linear functions. Every LP problem admits two forms: primal and dual forms. 

The _primal problem in the canonical form_ is 

**==> picture [112 x 20] intentionally omitted <==**

**==> picture [344 x 20] intentionally omitted <==**

where _X_ and _Y_ are finite sets, _A_ , _β_ , and _c_ are given real functions that define the problem, and _r_ is a vector is the _primal plan_ , representing the decision variables in the optimization problem. 

_Y_ typically represents the index set for the constraints in the optimization problem. Specifically, _Y_ is the set of indices that correspond to the linear constraints ∑ _x∈X A_ ( _y_ , _x_ ) _r_ ( _x_ ) = _β_ ( _y_ ) that must be satisfied for each _y ∈ Y_ . Each _y_ in _Y_ corresponds to a different constraint, where _A_ ( _y_ , _x_ ) represents the coefficients in the constraint matrix, and _β_ ( _y_ ) represents the right-hand side values for the constraints. 

The objective is to find the value _c_ , which is the lower bound of the total cost ∑ _x c_ ( _x_ ) _r_ ( _x_ ), where _c_ ( _x_ ) represents the cost associated with _x_ , and _r_ ( _x_ ) represents the amount or level of activity at _x_ . A plan, _r_ , is _feasible_ if it satisfies both constraints. That is, the linear equations must hold for all _y ∈ Y_ , and _r_ ( _x_ ) must be non-negative for all _x ∈ X_ . 

The _dual problem in standard form_ is as follows: 

**==> picture [121 x 22] intentionally omitted <==**

**==> picture [222 x 22] intentionally omitted <==**

where _λ_ is the _dual plan_ . The objective is to find the value _β_ , which is the upper bound of the sum ∑ _y β_ ( _y_ ) _λ_ ( _y_ ). 

Here, _β_ ( _y_ ) represents the benefit or value associated with _y_ , and _λ_ ( _y_ ) represents the level or intensity at _y_ . The constraint ∑ _y A_ ( _y_ , _x_ ) _λ_ ( _y_ ) _≤ c_ ( _x_ ) ensures that the linear combination of _λ_ ( _y_ ) with coefficients _A_ ( _y_ , _x_ ) does not exceed _c_ ( _x_ ) for each _x ∈ X_ . 

A general theorem relates the primal and dual problems. The _strong duality theorem_ states that the values are equal, _c_ = _β_ , provided that a feasible primal plan exists. If, moreover, _c > −_ ∞, then primal and dual optimal plans exist. 

## _4.2. Product Sample Space_ 

In this section, we assume a product of two finite sample spaces, Ω = Ω1 _×_ Ω2, and discuss the probability simplex on such a sample space, _P_ (Ω1 _×_ Ω2). 

_Axioms_ **2024** , _13_ , 823 

23 of 34 

The two _marginalization mappings_ are, 

**==> picture [222 x 46] intentionally omitted <==**

and the product marginalization mapping is 

**==> picture [214 x 11] intentionally omitted <==**

Given marginal distributions _q_ 1 _∈P_ (Ω)1 and _q_ 2 _∈P_ (Ω)2, their counter images for Π are called _transport plans_ , and 

**==> picture [315 x 12] intentionally omitted <==**

is the _set of transport plans_ . It contains the probability functions of all joint distributions on Ω1 _×_ Ω2 with the marginals specified as _q_ 1 and _q_ 2. For each _q ∈_ Π( _q_ 1, _q_ 2) the conditional _ω_ 1 _�→ q_ ( _ω_ 1, _·_ )/ _q_ 1( _ω_ ) is seen as a rule to move a given mass from _ω_ 1 to Ω2, which justifies the name of the transport plan. 

The set of transport plans, Π( _q_ 1, _q_ 2), is non-empty (because it contains the product of the two given marginals), and it is a convex, closed, and bounded set in the real space (because it is the intersection of the probability simplex with a hyperplane). 

We can rewrite the marginalization conditions using the indicator function ( _ξ_ = _ω_ ), which is 1 if _ξ_ = _ω_ and 0 otherwise, 

**==> picture [190 x 50] intentionally omitted <==**

Define a function, _A_ : (Ω1 _∪_ Ω2) _×_ (Ω1 _×_ Ω2) _→_ R, as 

**==> picture [226 x 24] intentionally omitted <==**

that is, 

**==> picture [177 x 31] intentionally omitted <==**

so that we can write the marginalization equations into a single equation, 

**==> picture [226 x 23] intentionally omitted <==**

which provides a better form of LP formalism. 

Given the _transport cost c_ : Ω1 _×_ Ω2 _→_ R, the optimal transport problem or Kantorovich problem looks for a transport plan with a minimal expected cost for a transport plan with given marginals, that is, with value the inf E _q_ [ _c_ ], where _q_ varies in Π( _q_ 1, _q_ 2). It is a primal problem in canonical form, 

**==> picture [380 x 48] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

24 of 34 

The dual problem in standard form is 

**==> picture [328 x 47] intentionally omitted <==**

A feasible transport plan exists, and the set of transport plans is closed and bounded. Hence, according to the strong duality theorem, the optimal values of the primal and dual problems are equal, and both primal and dual optimal solutions exist. 

We can derive a more explicit statement. The optimal value of the primal problem equals the optimal value of the dual problem, namely 

**==> picture [372 x 47] intentionally omitted <==**

where _q_ ¯ is the optimal transport plan, and _λ_[¯] 1( _ω_ 1) are the dual variables. The inequality 

**==> picture [177 x 12] intentionally omitted <==**

ensures that, for the optimal transport plan, the cost _c_ ( _ω_ 1, _ω_ 2) is equal to the sum of the dual variables _λ_[¯] 1( _ω_ 1) and _λ_[¯] 2( _ω_ 2) whenever _q_ ¯( _ω_ 1, _ω_ 2) _̸_ = 0, namely 

**==> picture [256 x 12] intentionally omitted <==**

In the transport literature, the equation above is called Kantorovich’s theorem, which specifies that the cost equals the sum of two single variable functions in support of an optimal plan. See, for example, [31]. 

## _4.3. ANOVA Splitting of the Statistical Bundle_ 

In this section, we use the language of effects’ decomposition to analyze categorical tabular data. A classical treatment of this topic is [32]. 

> The space of real random variables on Ω1 _×_ Ω2 is endowed with the inner product with weights provided via a strictly positive density, _q ∈P>_ (Ω1 _×_ Ω2), and the resulting Euclidean space is denoted as _L_[2] ( _q_ ). The linear sub-spaces of _L_[2] ( _q_ ), which respectively express the _q_ - _grand mean_ , the two _q_ - _simple effects_ , and the _q_ - _interaction_ , are 

**==> picture [156 x 63] intentionally omitted <==**

where _◦_ stands for the operation of functions composition, _f ◦ g_ ( _x_ ) = _f_ ( _g_ ( _x_ )), and the orthogonality is computed in the _q_ -probability function, that is, in the inner product of _L_[2] ( _q_ ), for which _⟨u_ , _v⟩q_ = E _q_ [ _uv_ ]. Each element of the space _B_ 0( _q_ ) + _B_ 1( _q_ ) + _B_ 2( _q_ ) has the form _u_ = _u_ 0 + _f_ 1 _◦_ Π1 + _f_ 2 _◦_ Π2, where _u_ 0 = E _q_ [ _u_ ] and _f_ 1, _f_ 2 are uniquely defined. 

For each _q ∈P>_ (Ω), there exists a unique orthogonal splitting: 

**==> picture [169 x 13] intentionally omitted <==**

Namely, each _u ∈ L_[2] ( _q_ ) can be written uniquely as follows: 

**==> picture [114 x 12] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

25 of 34 

where _u_ 0 = _Eq_ [ _u_ ], and ( _u_ 1 + _u_ 2) is the _q_ -orthogonal projection of _u − u_ 0 onto ( _B_ 1( _q_ ) + _B_ 2( _q_ )). That is, 

E _q_ ( _u_ 12 _|_ Π1) = 0 and E _q_ ( _u_ 12 _|_ Π2) = 0 . 

In conclusion, the ANOVA splitting of the statistical bundle is 

**==> picture [282 x 12] intentionally omitted <==**

and we can interpret each factor in the decomposition as a vector space of velocities. 

**Example 16.** _Given q_ 1 _∈P>_ (Ω1) _and q_ 2 _∈P>_ (Ω2) _, consider_ Π _[◦]_ ( _q_ 1, _q_ 2) _to be the open set consisting of all (strictly) positive probability densities in the set of transport plans_ Π( _q_ 1, _q_ 2) _._ 

_Consider a smooth curve with values in the interior of the open set of transport plans t �→ ⋆ q_ ( _t_ ) _∈_ Π _[◦]_ ( _q_ 1, _q_ 2) _with q_ (0) = _q. The velocity at q is given by q_ (0) _. Such a velocity is an ⋆ ⋆ interaction, q_ (0) _∈ B_ 12( _q_ (0)) _. In fact,_ E _q_ 0 � _q_ (0)� _, and for all fi_ = _gi ◦_ Π _i ∈ Bi, i_ = 1, 2 _,_ 

**==> picture [191 x 22] intentionally omitted <==**

_Conversely, given any interaction v ∈ B_ 12( _q_ ) _, consider the curve t �→ q_ ( _t_ ) = (1 + _tv_ ) _q. This curve stays in_ Π _[◦]_ ( _q_ 1, _q_ 2) _for t in a neighborhood of 0. Moreover, the interaction v is equal to the ⋆ velocity at t_ = 0 _; i.e., v_ = _q_ (0) _._ 

We define the _statistical bundle of positive transport plans_ as 

**==> picture [227 x 11] intentionally omitted <==**

�( _q_ , _v_ ) �� _q ∈_ Π _◦_ ( _q_ 1, _q_ 2), E _q_ ( _v|_ Π1) = E _q_ ( _v|_ Π2) = 0� . 

The mixture transport can be restricted to _S_ Π _[◦]_ ( _q_ 1, _q_ 2) to provide a parallel transport between the fibers. If _q_ , _r ∈_ Π _[◦]_ ( _q_ 1, _q_ 2) and _v ∈ B_ 12( _q_ ), let us compute _w_ =[m] U _[r] q[v]_[ =] _[q] r[v]_[ and] check that _w ∈ B_ 12( _r_ ). If _f_ is a function of Ω _i_ only, _i_ = 1, 2, then 

**==> picture [190 x 19] intentionally omitted <==**

In particular, it follows that the mixture affine displacement ( _q_ , _r_ ) _�→ ηq_ ( _r_ ) = _q[r][−]_[1 is] well defined in the open transport plan; that is, _ηq_ ( _r_ ) _∈ B_ 12( _q_ ). In fact, for all _f_ = _g ◦_ Π _i ∈ Bi_ ( _q_ ), _i_ = 1, 2, 

**==> picture [308 x 28] intentionally omitted <==**

The open transport statistical model is a sub-affine space of the mixture affine space. The literature frequently describes it as “flat” in the sense that each mixture’s auto-parallel curve between two points with the same margins has constant margins. 

**Example 17** (Mixed parametrization) **.** _The ANOVA splitting of the statistical bundle_ (37) _suggests a mixed parameterization of P>_ (Ω1 _×_ Ω2) _. Mixed parametrization combines elements of different parameterization schemes to describe the space. This approach is classical in the statistics of contingency tables, where mixed parametrizations are often used to model complex dependencies and interactions between variables._ 

_For each reference q ∈_ Π _[◦]_ ( _q_ 1, _q_ 2) _, consider the probability densities of the form_ 

**==> picture [226 x 14] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

26 of 34 

_The set of such densities is a sub-manifold of the exponential affine manifold usually termed an_ additive model _(§ 17.5 in [18]). The set of velocities at q is q-orthogonal to the space of transport plans that contain q._ 

**Example 18** (Optimal transport) **.** _Kantorovich’s problem can be studied as a gradient-flow problem. Let c_ : Ω1 _×_ Ω2 _→_ R _be a transport cost with ANOVA decomposition at q:_ 

**==> picture [121 x 11] intentionally omitted <==**

_The function q �→ C_ ( _q_ ) = E _q_ [ _c_ ] _restricted to the open transport model_ Π _[◦]_ ( _q_ 1, _q_ 2) _has a (statistical) gradient in S_ Π _[◦]_ ( _q_ 1, _q_ 2) _. For each generic smooth curve in_ Π _[◦]_ ( _q_ 1, _q_ 2) _with q_ (0) = _q, namely_ 

**==> picture [255 x 24] intentionally omitted <==**

_The natural gradient in the bundle is_ 

**==> picture [244 x 13] intentionally omitted <==**

_and the gradient flow equation is_ 

**==> picture [72 x 15] intentionally omitted <==**

_The natural gradient mapping q �→ c_ 12, _q is an orthogonal projection on the complete set of transport plans_ Π( _q_ 1, _q_ 2) _. It is remarkable to note that, in the more extensive set, the condition of zero gradients is compatible with the form of the optimal transport cost, according to Kantorivich._ 

## **5. Second-Order Computations and Mechanical Models** 

The notion of acceleration in the statistical bundle was introduced in Example 12 via the simple idea of computing the velocity’s velocity. This was feasible because we deal with affine spaces. This section analyzes the definition in detail and considers its possible application to models inspired by mechanics. The term “mechanics” refers to the applications discussed, for example, the notion of a curve with minimal Fisher information, where we interpret the Fisher information along a curve as a Lagrangian function. This section requires an introductory notion of the language of analytic mechanics. See, for example, the monograph [33] or the introductions of the papers [12,34]. 

Consider a statistical bundle, _SP>_ (Ω), with a cocycle of parallel transports, U _[q] p_[,] _[p]_[,] _[ q][ ∈] P>_ (Ω), and a compatible affine atlas, _sp_ , _p ∈P>_ (Ω). The statistical bundle is an affine space for the charts 

**==> picture [300 x 19] intentionally omitted <==**

If Γ : _t �→_ ( _q_ ( _t_ ), _v_ ( _t_ )) is a curve in the statistical bundle, its expression at ( _p_ , _u_ ) is 

**==> picture [156 x 18] intentionally omitted <==**

and the expression of the velocity at ( _p_ , _u_ ) is 

**==> picture [173 x 25] intentionally omitted <==**

The velocity in the _moving frame_ centered at ( _p_ , _u_ ) = ( _q_ ( _t_ ), _v_ ( _t_ )) is 

**==> picture [154 x 31] intentionally omitted <==**

Especially if Γ( _t_ ) = ( _q_ ( _t_ ), _q⋆_ ( _t_ )), we have the definition of _affine acceleration_ , 

_Axioms_ **2024** , _13_ , 823 

27 of 34 

**==> picture [256 x 28] intentionally omitted <==**

In conclusion, each system of parallel transports has its own acceleraation. Precisely, the following applies: 

- The _exponential acceleration is_ 

**==> picture [361 x 87] intentionally omitted <==**

- The _mixture acceleration_ is 

**==> picture [331 x 27] intentionally omitted <==**

**Remark 1.** _It should be noted that, because of the very definition, the acceleration is zero if and ⋆ q_ ( _s_ ) _⋆ only if the curve has a constant velocity in the proper parallel transport; that is, q_ ( _s_ ) = U _q_ ( _t_ ) _q_ ( _t_ ) _. In particular, the exponential acceleration is null for 1-dimensional exponential models, and the mixture acceleration is null for 1-dimensional mixture models._ 

The acceleration is appropriately defined as a triple of curves: the model, the velocity, and the acceleration. It is convenient to define a vector bundle whose fibers are products of two fibers of the statistical bundle. Moreover, to identify each fiber and to prepare for the use of the covariance inner product as a duality pairing, the two fibers are denoted, respectively, as _SpP>_ (Ω) and _[∗] SpP>_ (Ω). 

The _full bundle_ is 

**==> picture [298 x 14] intentionally omitted <==**

With such a notation, any twice-smooth curve, _q_ , is lifted to a curve in the full bundle, 

**==> picture [96 x 14] intentionally omitted <==**

**Remark 2.** _The derivation of curves in the statistical bundle is also called_ covariant derivation _. The treatment of covariant derivatives in standard monographs of differential geometry, such as, for example, [14,35], is considerably more involved than ours because we are considering the particular case of affine manifold endowed with an inner product instead of a general differentiable manifold or a general Riemannian manifold. In some cases, we must distinguish between exponential and mixture covariant derivatives._ 

Below, we provide an example of a problem of interest that requires a second-order formalism. After that, we discuss how general arguments originating in mechanics can help solve such problems. 

## _5.1. Curves with Minimal Fisher’s Information_ 

Let us consider a smooth curve in the open probability simplex, _q_ : [0, 1] _∋ t �→ q_ ( _t_ ) _∈ P>_ (Ω), connecting _q_ 0 = _q_ (0) to _q_ 1 = _q_ (1). The velocity of the curve in the statistical bundle is ]0, 1[ _∋ t �→ q⋆_ ( _t_ ) = _dtd_[log] _[ q]_[(] _[t]_[)] _[∈][S][q]_[(] _[t]_[)] _[P][>]_[(][Ω][)][,][the][Fisher’s][score.][Each][fiber] _SqP>_ (Ω) of the statistical bundle _SP>_ (Ω) is endowed with the covariance inner product _⟨v_ , _w⟩q_ = Cov _q_ ( _v_ , _w_ ), which defines the Riemannian metric of the statistical bundle. 

_Axioms_ **2024** , _13_ , 823 

28 of 34 

With a mechanical analogy, the (kinetic) _energy_ of the curve _q_ ( _·_ ) is the squared norm of the velocity, while the integral of the energy along the curve is the _action_ , 

**==> picture [313 x 28] intentionally omitted <==**

We can find a necessary condition for a minimum of the action by performing the classical Euler computation in the current context. Consider a curve in the statistical bundle _t �→_ ( _q_ ( _t_ ), _v_ ( _t_ )) _∈ SP>_ (Ω), such that _v_ (0) = _v_ (1) = 0. For each real _θ_ , let us consider 

**==> picture [152 x 14] intentionally omitted <==**

_·_ Such a perturbed smooth curve has the same endpoints as _q_ ( ), and the velocity is 

**==> picture [374 x 47] intentionally omitted <==**

At any external point of the action, we must have 

**==> picture [152 x 26] intentionally omitted <==**

The derivative of the integrand is 

**==> picture [373 x 85] intentionally omitted <==**

The derivatives _[d][d] d_[2] _dt_[,] _dθ_[,] _dtdθ_[of the cumulant function are, respectively,] 

**==> picture [373 x 64] intentionally omitted <==**

**==> picture [373 x 83] intentionally omitted <==**

The values at _θ_ = 0 are, respectively, 0, 0, and E _q_ ( _t_ )� _v_ ˙( _t_ ) + _v_ ( _t_ ) _q⋆_ ( _t_ )�. The _θ_ -derivative of the energy at _θ_ = 0 is 

**==> picture [320 x 53] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

29 of 34 

**==> picture [264 x 22] intentionally omitted <==**

The variation in the energy in the direction _v_ ( _·_ ) is 

**==> picture [362 x 85] intentionally omitted <==**

where the first integral vanishes, 

In conclusion, 

**==> picture [226 x 28] intentionally omitted <==**

for all _v_ ( _·_ ). One can easily check that the Euler–Lagrange equation holds, 

**==> picture [160 x 25] intentionally omitted <==**

**Remark 3.** _The LHS of the equation above is the semi-sum of the two accelerations of Equations (39) and (40). As S.-I Amari first discussed, this particular acceleration is the Levi–Civita acceleration of the open probability simplex. See the monograph [2]. The present paper does not discuss geometries other than the affine ones._ 

## _5.2. Lagrangian and Hamiltonian Formalism on the Probability Simplex_ 

Consider a smooth curve, _t �→_ ( _q_ ( _t_ ), _η_ ( _t_ ), _w_ ( _t_ )), in the full statistical bundle[1] _S_[1] _P>_ (Ω). Here, _q_ ( _t_ ) represents the probability distribution, _w_ ( _t_ ) is an element of the fiber at _q_ ( _t_ ), interpreted as a velocity, and _η_ ( _t_ ) is an element of the fiber at _q_ ( _t_ ), interpreted as an acceleration. This second instance of the fiber is interpreted as a cotangent space in duality with the tangent space via the covariance inner product. 

The derivative of the inner product _⟨η_ ( _t_ ), _w_ ( _t_ ) _⟩q_ ( _t_ ) is given by the sum of the mixture covariant derivative of _η_ ( _t_ ) and the exponential covariant derivative of _w_ ( _t_ ), 

**==> picture [384 x 85] intentionally omitted <==**

Recall that, for a given scalar field, _F_ : _P>_ (Ω) _→_ R, the natural gradient of _F_ is a section of the statistical bundle, such that, for all smooth curves, _t �→ q_ ( _t_ ), 

**==> picture [159 x 22] intentionally omitted <==**

This formulation ensures that the gradient grad _F_ captures the rate of change of the scalar field _F_ along the curve _q_ ( _t_ ). We will need a more general gradient form that includes both the natural gradient and Equation (42). 

Let there be given a real function, _F_ :[1] _S_[1] _P>_ (Ω) _× D →_ R, where _D_ is a domain of R _[k]_ . For a generic smooth curve, 

**==> picture [182 x 13] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

30 of 34 

we want to write 

**==> picture [373 x 83] intentionally omitted <==**

These terms collectively describe the total derivative: how the function _F_ changes along the curve with values in the full bundle and a parametric set, _D_ . The four gradient components can be computed in the proper chart by varying only one component at a time. 

The dually affine geometry of the statistical bundle is naturally well suited to describing the dynamics of probability densities in Lagrangian and Hamiltonian formalism, as presented, for example, in the textbook [33]. The Lagrangian formulation of mechanics derives the fundamental laws of force equilibrium from variational principles. In this analogy, the open probability simplex _P>_ (Ω) corresponds to the configuration space, while the statistical bundle _SP>_ (Ω), which includes velocities, is associated with the mechanical phase space. In this section, we describe the general methodology in an analogy with the standard treatment in mechanics, and we apply it to a specific but quite general example. For the full proof, see [12]. 

Given a _Lagrangian function_ , 

**==> picture [112 x 12] intentionally omitted <==**

for each smooth curve _q_ : [0, 1] _∋ t �→ q_ ( _t_ ) _∈P>_ (Ω), we consider its lift _t �→_ ( _q_ ( _t_ ), _q⋆_ ( _t_ )) _∈ SP>_ (Ω). The action is the integral of the Lagrangian along the lifted curve over the fixed time interval [0, 1], 

**==> picture [160 x 23] intentionally omitted <==**

In mechanical terms, the action encapsulates the system’s dynamics in the Lagrangian function and the path taken by the curve in the configuration space. The discussion of Section 5.1 is an instance of this approach applied to statistics. Two further examples follow. 

**Example 19** (Mixture curve) **.** _The mixture curve q_ ( _t_ ) = _q_ 0 + _t_ ( _q_ 1 _− q_ 0) _has the velocity_ 

**==> picture [214 x 24] intentionally omitted <==**

_⋆ ⋆ ⋆ The action of this curve for the Lagrangian L_ ( _q_ , _q_ ) = � _q_ , _q_ � _q[is]_ 

**==> picture [374 x 70] intentionally omitted <==**

**Example 20** (Exponential curve) **.** _The exponential curve q_ ( _t_ ) = _e[tu][−][K][q]_[0][(] _[tu]_[)] _· q_ 0 _connects q_ 0 _to q_ 1 = _q_ (1) _. The velocity is_ 

**==> picture [138 x 13] intentionally omitted <==**

_Axioms_ **2024** , _13_ , 823 

31 of 34 

_⋆ ⋆ ⋆ The action of this curve for the Lagrangian L_ ( _q_ , _q_ ) = � _q_ , _q_ � _q[is]_ 

_We use the equality_ 

**==> picture [170 x 67] intentionally omitted <==**

_and_ E _q_ 0 [ _u_ ] = 0 _to get_ 

**==> picture [374 x 53] intentionally omitted <==**

Hamilton’s principle states that the action _A_ ( _q_ ) has a critical point at the solution _q_ in the space of curves on _P>_ (Ω) if the Euler–Lagrange equation holds, 

**==> picture [192 x 22] intentionally omitted <==**

This follows from a general principle in mechanics. See [36] for a detailed proof in the statistical case. 

Let us define the Hamiltonian corresponding to a Lagrangian with the usual duality argument. The gradient mapping and Legendre transform are applied at each fixed density _q ∈P>_ (Ω) and each time _t_ . The partial mapping _SqP>_ (Ω) _∋ w �→ Lq_ , _t_ ( _w_ ) = _L_ ( _q_ , _w_ , _t_ ) has a gradient mapping in the covariance duality of _[∗] SqP>_ (Ω) _× SqP>_ (Ω), namely _w �→ ∇e L_ ( _q_ , _w_ , _t_ ). 

The Hamiltonian _H_ ( _q_ , _η_ , _t_ ) is the Legendre transform of the Lagrangian, 

**==> picture [240 x 21] intentionally omitted <==**

Here, ( _∇e Lq_ , _t_ ) _[−]_[1] ( _η_ ) denotes the inverse of the exponential gradient mapping applied 

to _η_ . 

These components collectively describe the system’s dynamics in terms of Hamilton’s principle and Hamiltonian formalism. 

If the curve _t �→ q_ ( _t_ ) is a solution of the Euler–Lagrange equation, then the curve _t �→ ζ_ ( _t_ ) = ( _q_ ( _t_ ), _η_ ( _t_ )) lies in the cotangent bundle _[∗] SE_ ( _µ_ ). The momentum _η_ ( _t_ ) is defined as: 

**==> picture [108 x 14] intentionally omitted <==**

In this context, the mixture bundle _[∗] SE_ ( _µ_ ) acts as the cotangent bundle in classical mechanics. The Hamilton equations describe the evolution of the system: 

**==> picture [136 x 32] intentionally omitted <==**

These equations describe the system’s evolution in terms of the Hamiltonian function _H_ ( _q_ , _η_ , _t_ ). The time derivative of the Hamiltonian _H_ along the trajectory is given by the following: 

**==> picture [167 x 22] intentionally omitted <==**

This equation indicates that the system’s total energy changes according to the Hamiltonian’s explicit time dependence. 

_Axioms_ **2024** , _13_ , 823 

32 of 34 

**Example 21** (Compare with Section 5.1) **.** _Given the Lagrangian L_ ( _q_ , _w_ ) = 12 _[⟨][w]_[,] _[ w][⟩][q][,][the] Hamiltonian obtained via the Legendre transform is H_ ( _q_ , _η_ ) =[1] 2 _[⟨][η]_[,] _[ η][⟩][q][. The Lagrangian represents] the kinetic energy, while the Hamiltonian represents the system’s total energy. The gradients of the Hamiltonian and Lagrangian are computed as follows:_ 

**==> picture [134 x 79] intentionally omitted <==**

_⋆ ∗ The Euler–Lagrange equation for q_ = _w ∈ SE_ ( _µ_ ) _is given by the following:_ 

**==> picture [149 x 22] intentionally omitted <==**

_where_ 

**==> picture [73 x 25] intentionally omitted <==**

_The Hamilton equations are_ 

**==> picture [122 x 31] intentionally omitted <==**

_The conserved energy is H_ ( _q_ ( _t_ ), _η_ ( _t_ )) = 2[1] _[E][q]_ � _q_ ˙ _q_ (( _tt_ ))2 � _; that is, the Fisher’s information is constant in the solution._ 

## **6. Conclusions** 

This research has provided a general and cohesive geometric framework for studying several geometries of the probability simplex, including Aitchison’s and Amari’s dual affine and transport geometries. By providing a cogent presentation of these various geometric approaches, the framework has the potential to significantly improve the comprehension and manipulation of probability distributions in statistical modeling and machine learning. 

This unified approach is based on an axiomatic approach called the affine geometry of the statistical bundle. This approach is beneficial when the accurate handling of compositional data is crucial, such as when developing computational tools, statistical model optimization, and gradient flow optimization are involved. In particular, our formalism provides a principled treatment of second-order computations, such as accelerations. 

As a notable contribution, we have shown that Aitchison CLR provides the charts of an affine space isomorphic to the information geometry space defined by the exponential presentation of probability functions. Moreover, both approaches allow for a statistically natural calculus concerning gradients of scalar fields and gradient flows. 

The framework can increase performance in activities ranging from data processing to implementing sophisticated machine learning algorithms by facilitating more accurate and efficient modeling, providing a consistent geometric perspective. Moreover, we have shown how other geometries of great current interest, those associated with optimal transport, fit into the scheme of gradient flows in the statistical bundle. 

The paper’s final part contributed to discussing simple but relevant examples of statistical models controlled via second-order differential equations. This opens the discussion of dynamic statistical models with unusual time behavior, such as periodicity, without any reference to any dynamical system in the sample space. 

_Axioms_ **2024** , _13_ , 823 

33 of 34 

**Author Contributions:** Conceptualization, G.P.; formal analysis, G.P.; investigation, G.P.; writing—original draft, G.P. and M.S.; writing—review and editing, G.P. and M.S.; supervision, G.P.; project administration, G.P. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This project received funding from the European Union’s Horizon 2020 research and innovation program under Marie Skłodowska-Curie GA No. 101034449. 

**Data Availability Statement:** The original contributions presented in the study are included in the article, further inquiries can be directed to the corresponding author. 

**Acknowledgments:** The present paper is partly based on unpublished lecture notes by M. Shoaib after G. Pistone’s lectures at the seminar that Eva Riccomagno organized in 2022–2023. The authors gratefully thank Eva Riccomagno for her invitation, support, supervision, and revision of an early version of the manuscript. Collegio Carlo Alberto, Italy, partially supports G. Pistone. He is a member of GNAFA-INDAM. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **References** 

1. Amari, S. Dual connections on the Hilbert bundles of statistical models. In _Geometrization of Statistical Theory_ ; ULDM Publishing: Lancaster, PA, USA, 1987; pp. 123–151. 

2. Amari, S.; Nagaoka, H. _Methods of Information Geometry_ ; Translated from the 1993 Japanese original by Daishi Harada; American Mathematical Society: Providence, RI, USA, 2000; Volume 191, 206p. 

3. Pistone, G.; Sempi, C. An infinite-dimensional geometric structure on the space of all the probability measures equivalent to a given one. _Ann. Statist._ **1995** , _23_ , 1543–1561. [CrossRef] 

4. Pawlowsky-Glahn, V.; Egozcue, J.J.; Tolosana-Delgado, R. _Modelling and Analysis of Compositional Data_ ; John Wiley & Sons, Ltd.: Hoboken, NJ, USA, 2015. [CrossRef] 

5. Aitchison, J. _The Statistical Analysis of Compositional Data_ ; Monographs on Statistics and Applied Probability; Chapman & Hall: London, UK, 1986; 416p. 

6. Egozcue, J.J.; Pawlowsky-Glahn, V.; Tolosana-Delgado, R.; Ortego, M.I.; van den Boogaart, K.G. Bayes spaces: Use of improper distributions and exponential families. _Rev. Real Acad. Cienc. Exactas Fis. Nat. Ser. Mat._ **2012** , _107_ , 475–486. [CrossRef] 

7. Barvinok, A. _A Course in Convexity_ ; Graduate Studies in Mathematics; American Mathematical Society: Providence, RI, USA, 2002; Volume 54, 366p. 

8. Lay, S.R. _Convex Sets and Their Applications_ ; Courier Corporation: North Chelmsford, MA, USA, 2007. 

9. Amari, S.I. _Information Geometry and Its Applications_ ; Applied Mathematical Sciences; Springer: Tokyo, Japan, 2016; 374p. 

10. Nomizu, K.; Sasaki, T. _Affine Differential Geometry: Geometry of Affine Immersions_ ; Cambridge Tracts in Mathematics; Cambridge University Press: Cambridge, UK, 1994. 

11. Pistone, G. Information Geometry of the Probability Simplex: A Short Course. _Nonlinear Phenom. Complex Syst._ **2020** , _23_ , 221–242. [CrossRef] 

12. Chirco, G.; Malagò, L.; Pistone, G. Lagrangian and Hamiltonian dynamics for probabilities on the statistical bundle. _Int. J. Geom. Methods Mod. Phys._ **2022** , _19_ , 2250214. [CrossRef] 

13. Bourbaki, N. _Variétés Differentielles et Analytiques. Fascicule de réSultats/Paragraphes 1 à 7_ ; Springer Science and Business Media: New York, NY, USA, 1971. 

14. Lang, S. _Differential and Riemannian Manifolds_ , 3rd ed.; Graduate Texts in Mathematics; Springer: New York, NY, USA, 1995; 364p. 

15. Brier, G.W. Verification of forecasts expressed in terms of probability. _Mon. Weather. Rev._ **1950** , _78_ , 1–3. [CrossRef] 

16. Weyl, H. _Space—Time—Matter_ ; Translation of the 1921 raum zeit materie; Dover: New York, NY, USA, 1952. 

17. Brown, L.D. _Fundamentals of Statistical Exponential Families with Applications in Statistical Decision Theory_ ; Institute of Mathematical Statistics: Beachwood, OH, USA, 1986; 283p. 

18. Efron, B.; Hastie, T. _Computer Age Statistical Inference_ ; IMS Monographs; Cambridge University Press: Cambridge, UK, 2016; Volume 19, 475p. 

19. Cover, T.M.; Thomas, J.A. _Elements of Information Theory_ , 2nd ed.; Wiley-Interscience: Hoboken, NJ, USA, 2006; 748p. 

20. Ohara, A.; Amari, S. Differential geometric structures of stable state feedback systems with dual connections. _Kybernetika_ **1994** , _30_ , 369–386. 

21. Cafaro, C.; Alsing, P.M. Decrease of Fisher information and the information geometry of evolution equations for quantum mechanical probability amplitudes. _Phys. Rev. E_ **2018** , _97_ , 042110. [CrossRef] [PubMed] 

22. Ay, N.; Jost, J.; Lê, H.V.; Schwachhöfer, L. _Information Geometry_ ; Ergebnisse der Mathematik und ihrer Grenzgebiete; Springer: Cham, Switzerland, 2017; 407p. [CrossRef] 

23. Ohara, A. On Affine Immersions of the Probability Simplex and Their Conformal Flattening; In Proceedings of the Geometric Science of Information: Third International Conference, GSI 2017, Paris, France, 7–9 November 2017; Springer: Cham, Switzerland, 2017; pp. 247–254. [CrossRef] 

_Axioms_ **2024** , _13_ , 823 

34 of 34 

24. Duy, T.T.; Nguyen, L.V.; Nguyen, V.; Trung, N.; Abed-Meraim, K. Fisher information neural estimation. In Proceedings of the 30th European Signal Processing Conference (EUSIPCO), Belgrade, Serbia, 29 August–2 September 2022; pp. 2111–2115. [CrossRef] 

25. Ly, A.; Marsman, M.; Verhagen, J.; Grasman, R.; Wagenmakers, E. A Tutorial on Fisher Information. _J. Math. Psychol._ **2017** , _80_ , 40–55. [CrossRef] 

26. Wei, X.X.; Stocker, A. Mutual Information, Fisher Information, and Efficient Coding. _Neural Comput._ **2016** , _28_ , 305–326. [CrossRef] [PubMed] 

27. Gibilisco, P.; Pistone, G. Connections on non-parametric statistical manifolds by Orlicz space geometry. _Infin. Dimens. Anal. Quantum Probab. Relat. Top._ **1998** , _1_ , 325–347. [CrossRef] 

28. Kullback, S.; Leibler, R.A. On information and sufficiency. _Ann. Math. Stat._ **1951** , _22_ , 79–86. [CrossRef] 

29. Csiszár, I. I-divergence geometry of probability distributions and minimization problems. _Ann. Probability_ **1975** , _3_ , 146–158. [CrossRef] 

30. Landau, L.D.; Lifshits, E.M. _Statistical Physics_ , 3rd ed.; Course of Theoretical Physics; Butterworth-Heinemann: Oxford, UK, 1980; Volume 5. 

31. Peyré, G.; Cuturi, M. Computational Optimal Transport. _Found. Trends Mach. Learn._ **2019** , _11_ , 355–607. [CrossRef] 

32. Fienberg, S.E. _The Analysis of Cross-Classified Categorical Data_ ; MIT Press: Cambridge, MA, USA, 1980; 198p. 

33. Arnold, V.I. _Mathematical Methods of Classical Mechanics_ ; Graduate Texts in Mathematics; Translated from the 1974 Russian original by K. Vogtmann and A. Weinstein; Springer: New York, NY, USA, 1989; 516p. 

34. Pistone, G. Lagrangian Function on the Finite State Space Statistical Bundle. _Entropy_ **2018** , _20_ , 139. [CrossRef] [PubMed] 

35. Do Carmo, M.P. _Riemannian Geometry_ ; Mathematics: Theory & Applications; Translated from the second Portuguese edition by Francis Flaherty; Birkhäuser Boston Inc.: Basel, Switzerland, 1992; 300p. 

36. Chirco, G.; Pistone, G. Dually affine Information Geometry modeled on a Banach space. _arXiv_ **2022** , arXiv:2204.00917. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

