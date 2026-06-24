_Mathematical Geology, Vol. 35, No. 3, April 2003 (_[⃝][C] _2003)_ 

# **Isometric Logratio Transformations for Compositional Data Analysis[1]** 

## **J. J. Egozcue,[2] V. Pawlowsky-Glahn,[3] G. Mateu-Figueras,[3] and C. Barcel´o-Vidal[3]** 

_Geometry in the simplex has been developed in the last 15 years mainly based on the contributions due to J. Aitchison. The main goal was to develop analytical tools for the statistical analysis of compositional data. Our present aim is to get a further insight into some aspects of this geometry in order to clarify the way for more complex statistical approaches. This is done by way of orthonormal bases, which allow for a straightforward handling of geometric elements in the simplex. The transformation into real coordinates preserves all metric properties and is thus called isometric logratio transformation (ilr). An important result is the decomposition of the simplex, as a vector space, into orthogonal subspaces associated with nonoverlapping subcompositions. This gives the key to join compositions with different parts into a single composition by using a balancing element. The relationship between ilr transformations and the centered-logratio (clr) and additive-logratio (alr) transformations is also studied. Exponential growth or decay of mass is used to illustrate compositional linear processes, parallelism and orthogonality in the simplex._ 

**KEY WORDS:** Aitchison distance, Aitchison geometry, geodesic, orthogonal subcompositions, ternary diagram. 

## **INTRODUCTION** 

The statistical analysis of compositional data got an independent status when Aitchison (1986) introduced the additive-logratio (alr) and centered-logratio (clr) transformations, as well as an appropriate distance in the simplex, the sample space of compositional data without zero parts. He showed that these transformations from the simplex into multidimensional real space exhibit important properties. Among them, invariance under scale group of transformations, subcompositional consistency, and correspondence of the group of translations in multidimensional 

> 1Received 5 April 2002; accepted 17 February 2002 

> 2Dept. de Matem`atica Aplicada III, Universitat Polit`ecnica de Catalunya, Barcelona, Spain; e-mail: juan.jose.egozcue@upc.es. 

> 3Dept. d’Inform`atica i Matem`atica Aplicada, Universitat de Girona, Girona, Spain; e-mail: vera.pawlowsky@udg.es; gloria.mateu@udg.es; carles.barcelo@udg.es. 

**279** 

0882-8121/03/0400-0279/1[⃝][C] 2003 International Association for Mathematical Geology 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**280** 

real space with the group of perturbations in the simplex were enough to consider those transformations as firm candidates to define the standard way of analyzing compositional data. He also developed special strategies for dealing with data sets including zeros, hence all possible types of compositional data could be studied using his approach. As a consequence, in order to analyze a given data set, a widely extended approach now is to apply first an appropriate strategy when zeroes are present (see Mart´ın-Fern´andez, Barcel´o-Vidal and Pawlowsky-Glahn, 2003, for details), and then either to alr- or clr-transform the data. Transformed data are then analyzed in the same way as standard data. Statistical models based on those transformations were developed successfully in most cases, as can be seen in the monograph by Aitchison (1986) and later developments (Aitchison, 1989, 1990, 1992, 1997, 2002; Aitchison et al., 2000; Aitchison and Thomas, 1998; Barcel´oVidal, Mart´ın-Fern´andez, and Pawlowsky-Glahn, 2001; Billheimer, Guttorp, and Fagan, 2001; Pawlowsky-Glahn, 2002; Pawlowsky-Glahn and Egozcue, 2001, 2002; von Eynatten, Pawlowsky-Glahn, and Egozcue, 2002). However, there are a number of researchers who argue against Aitchison’s methods, mainly due to difficulties in interpretation of the transformed data. 

In fact, the alr and clr transformations have some shortcomings that make interpretation difficult. The alr transformation—defined as the logarithm of the ratio of parts over a given one—is asymmetric in the parts of the composition. By changing the part in the denominator, we obtain different alr transformations. But the main drawback of the alr transformation is not the asymmetry in its definition, but the fact that it is not an isometric transformation from the simplex, with the Aitchison metric, onto the real alr-space, with the ordinary Euclidean metric. Certainly, to overcome this problem one could use an appropriate metric with oblique coordinates in real alr-space, but that is not standard practice. As a consequence, when one does not take into account the absence of isometry, the interpretation of transformed data is not intuitive at all, as results occasionally do not match properties expected in the simplex (see Mart´ın-Fern´andez, Olea-Meneses, and Pawlowsky-Glahn, 2001, for an example). Nevertheless, it is important to note that consistency of results is guaranteed, even in the presence of zeros, when inference is based on the likelihood of the additive logistic normal distribution (Aitchison, 1986). 

The clr transformation is symmetric with respect to the compositional parts and keeps the same number of components as the number of parts in the composition. A composition with _D_ parts is transformed into _D_ real components adding up to 0. Thus, for example, for _D_ = 3, clr-transformed data should be represented in a three-dimensional real space, although the linear restriction in the components would allow a two-dimensional representation. The advantage of the clr is that it is an isometric transformation of the simplex with the Aitchison metric, onto a subspace of real space with the ordinary Euclidean metric. Nevertheless, orthogonal references in that subspace are not obtained in a straightforward manner. 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**281** 

Our aim is to overcome these shortcomings giving new tools for interpreting compositional data by introducing a new family of logratio transformations of the simplex. This family is called _isometric_ because it allows us to associate _angles_ and _distances_ in the simplex (following the Aitchison geometry) to _angles_ and _distances_ in real space, where we feel more comfortable from an intuitive point of view. This is of particular interest with respect to concepts of orthogonality. 

In order to motivate the of the new family of isometric logratio (ilr) transformations and exploit the underlying intuitive ideas, we first introduce simple compositional models. These models help us understand the meaning of orthogonality in the simplex and, simultaneously, the role of perturbation. 

There are also mathematical reasons for introducing this new family of transformations. In fact, all Hilbert spaces are isometric whenever they have the same dimension (Berberian, 1961). Thus, a natural undertaking is to find an isometry between the simplex, which is a Hilbert space—and hence an Euclidean space— and a real space of the same dimension (Billheimer, Guttorp, and Fagan, 2001; Pawlowsky-Glahn and Egozcue, 2001, 2002). Note that this task is neither solved by alr—it is not isometric—nor by clr—it is not expressed in terms of a basis neither of the simplex nor of the image subspace. 

Second, we recall some important aspects of the Aitchison geometry in the simplex. Then introduce simple processes in the simplex, to help us understand orthogonality and perturbation. The section that follows builds up orthonormal bases that allow the explicit definition of the family of ilr transformations. Finally, we give the relationships between a given ilr, the clr and a given alr transformation. 

## **AITCHISON GEOMETRY IN THE SIMPLEX** 

## **Vector Space Structure** 

The _D_ 

**==> picture [315 x 31] intentionally omitted <==**

where κ is an arbitrary positive constant, e.g. 1 if measurements are performed in parts per 1 or 100 if they are in percentages. The elements of S _[D]_ , which are considered to be row vectors, will be called _D_ -part compositions. The ( _D_ − 1)dimensional vector space structure of S _[D]_ on ℜ is based on the _perturbation_ operation, defined for any two compositions **x** , **y** ∈ S _[D]_ , as 

**==> picture [231 x 10] intentionally omitted <==**

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**282** 

and on an external operation called _power transformation_ , given for **x** ∈ S _[D]_ and α ∈ℜ by 

**==> picture [220 x 13] intentionally omitted <==**

where C(·) denotes the _closure_ of the vector in the argument (i.e. each component is divided by the sum of all the components and then multiplied by κ, so that the resulting row vector is in S _[D]_ ) (Aitchison, 2002; Billheimer, Guttorp, and Fagan, 2001; Pawlowsky-Glahn and Egozcue, 2001, 2002). Note that perturbation can be defined between positive vectors that are not necessarily normalized to κ, because the closure operator is explicitly included in definition (2), and that the neutral element with respect to perturbation is C[1, 1, . . . , 11]. In what follows **x** ⊖ **y** will denote perturbation of **x** with the opposite element of **y** , which is (−1) ⊗ **y** = C( **y**[−][1] ), i.e. 

**==> picture [145 x 11] intentionally omitted <==**

## **Hilbert Space Structure** 

is an Euclidean space and is complete. Now, for any two compositions **x** , **y** ∈ S _[D]_ , 

**==> picture [267 x 30] intentionally omitted <==**

where _g_ ( **x** ) = [ _x_ 1 _x_ 2 · · · _x D_ ][1][/] _[D]_ is the geometric mean of the parts of **x** . It is straightforward to show that Equation (4) is an inner product, and thus S _[D]_ is a ( _D_ − 1)dimensional Hilbert space (Pawlowsky-Glahn and Egozcue, 2001, 2002). The expression (4) involving logratios of parts over geometric means of parts is related to the clr transformation defined by Aitchison (1986): 

**==> picture [274 x 25] intentionally omitted <==**

whereas an expression using the alr transformation, i.e. 

**==> picture [242 x 25] intentionally omitted <==**

**Isometric Logratio Transformations for Compositional Data Analysis** 

**283** 

was found by Billheimer, Guttorp, and Fagan (2001), who developed the algebra for compositions and the proof of the Hilbert space structure of the simplex in terms of this transformation. 

The inner product (4) induces a norm and a distance in S _[D]_ in the standard way, 

**==> picture [240 x 13] intentionally omitted <==**

Note that the inner product (4), and thus the norm and the distance (7), are invariant under permutation of the parts of a composition. The extensive expression for _da_ is 

**==> picture [318 x 43] intentionally omitted <==**

The distance (8) is known as Aitchison distance in S _[D]_ and, therefore, the Hilbert geometry mentioned here will be called Aitchison geometry. The Aitchison geometry in S _[D]_ is an Euclidean geometry because the distance comes from an inner product. However, when representing _straight lines, rectangles_ , and _circles_ in this geometry (Fig. 1(A)–5(A)) one can observe features that differ from what commonly feels an Euclidean geometry (Fig. 1(B)–5(B)). To avoid confusion, from now on, we term Euclidean distance, geometry, etc., only those which are standard in real space. 

**Figure 1.** (A) Representation of compositional parallel processes in vector space S[3] ; dashed lines correspond to orthogonal coordinate axes. (B) Same processes after ilr transformation; _y_ 1 = 2[−][2] ln(v1/v2), _y_ 2 = 6[−][2] ln((v1v2)/(v3v3)). 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**284** 

**Figure 2.** (A) Representation of centered compositional square in vector space S[3] , dashed lines correspond to orthogonal coordinate axes. Diagonals of square coincident with coordinate axes. (B) Same square after ilr transformation; _y_ 1 = 2[−][2] ln(v1/v2), _y_ 2 = 6[−][2] ln((v1v2)/(v3v3)). 

The ( _D_ − positional straight lines, orthogonal lines, angles between lines and all standard elements in an Euclidean geometry. Special attention is now paid to compositional lines and relations of orthogonality and parallelism between them. 

**Figure 3.** (A) Representation of centered compositional square in vector space S[3] , dashed lines correspond to orthogonal coordinate axes. Sides of square parallel to coordinate axes. (B) Same square after ilr transformation; _y_ 1 = 2[−][2] ln(v1/v2), _y_ 2 = 6[−][2] ln((v1v2)/(v3v3)). 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**285** 

**Figure 4.** (A) Representation of centered compositional rectangle in vector space S[3] , dashed lines correspond to orthogonal coordinate axes. Sides rotated with respect to coordinate axes. (B) Same rectangle after ilr transformation; _y_ 1 = 2[−][2] ln(v1/v2), _y_ 2 = 6[−][2] ln((v1v2)/(v3v3)). 

## **Straight, Parallel and Orthogonal Lines** 

Recall that in any dimensional Hilbert space, a geodesic curve connecting two points is understood to be the only continuous curve whose length is minimum with respect to the distance of the space. Such a geodesic is a segment of 

**Figure 5.** (A) Representation of compositional circles at different positions in vector space S[3] , dashed lines correspond to orthogonal coordinate axes. (B) Same circles after ilr transformation; _y_ 1 = 2[−][2] ln(v1/v2), _y_ 2 = 6[−][2] ln((v1v2)/(v3v3)). 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**286** 

a straight line within the geometry of the space considered. The parametric curve 

**==> picture [250 x 12] intentionally omitted <==**

is a straight line containing the geodesic—with respect to the Aitchison distance (8)—going from **x** 0 to **x** ( _t_ ) in **S** _[D]_ , for a given _t_ . This will become self-evident after defining the family of isometric logratio transformations, ilr. (see under Isometric Logratio Transformations). We will say that the composition **p** is the direction of suchageodesicorofthelinecontainingit.Allcurvesin S[3] showninFigure1(A)are straight lines with respect to the Aitchison geometry, which we call _compositional lines_ to avoid confusion. 

We can define orthogonal compositional lines at **x** 0 ∈ S _[D]_ as follows. Let **p** 1, **p** 2 ∈ S _[D]_ be two orthogonal directions in S _[D]_ , i.e. ⟨ **p** 1, **p** 2⟩ _a_ = 0. Then, **x** 1( _t_ ) = **x** 0 ⊕ ( _t_ ⊗ **p** 1) and **x** 2( _t_ ) = **x** 0 ⊕ ( _t_ ⊗ **p** 2) are orthogonal compositional lines at **x** 0 because for any _t_ 1, _t_ 2 ∈ℜ, 

**==> picture [256 x 10] intentionally omitted <==**

In our ordinary Euclidean space, such a statement means that segments along orthogonal straight lines (orthogonal directions) are perpendicular. 

position **p** ∈ S _[D]_ and two fixed points **x** 0, **x**[∗] 0[∈][S] _[ D]_[, the compositional lines] **[ x]**[(] _[t]_[)][ =] **x** 0 ⊕ ( _t_ ⊗ **p** ) and **x**[∗] ( _t_ ) = **x**[∗] 0[⊕][(] _[t]_[⊗] **[p]**[), are parallel, i.e. either they are coincident] or they do not intersect in the simplex. Graphically, for _D_ = 3, these parallel compositional lines converge either to the same vertices (Fig. 1(A)), or to one single vertex (Fig. 3(A)) (vertices and edges are placed at an infinite Aitchison distance from any point in the simplex). 

After introducing these concepts about compositional lines in the simplex, we look for examples of natural processes whose compositional evolution is described by compositional lines and for the meaning of orthogonality and parallelism of such processes. 

## **EXPONENTIAL GROWTH AND DECAY OF MASS AS COMPOSITIONAL PROCESSES** 

## **Linear Compositional Processes** 

Nature presents a large number of cases where some mass is lost or increases (approximately) exponentially in time. There are important examples in biology (population growth), in physics (radioactive decomposition of isotopes), or in geology (sedimentation or deposition). The mass deposition of different materials suspended in a steady water flow can be used as an example. If the conditions are 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**287** 

stationary and the different types of material do not interact, we can assume that the total mass of each material deposited instantaneously is proportional to the mass of this material suspended at the same instant. This leads to an exponential decrease of the total mass suspended in the water flow for each type of material. Denote by **z** ( _t_ ) = [ _z_ 1( _t_ ), . . . , _z D_ ( _t_ )] the mass suspended at time _t_ for each material type. Then, the exponential loss of material can be modelled as 

**==> picture [245 x 10] intentionally omitted <==**

where [ _a_ 1, _a_ 2, . . . , _aD_ ] = **a** is a vector of negative constants representing the mass loss rate. We can assume the components of **a** to be all negative, i.e. all masses decrease. The model (11) for masses allows us to obtain the compositional evolution in time of the different types of material by simply applying the closure operator to Equation (11), i.e. by dividing each component by the total sum of the vector: 

**==> picture [256 x 10] intentionally omitted <==**

where the closure in the exponential vector has been removed because perturbation includes it. We immediately identify the compositional evolution (12) with the expression of a compositional line (9) in the simplex by defining **p** = C(exp[ **a** ]), and thus obtaining _t_ ⊗ **p** = _t_ ⊗ C(exp[ **a** ]) = C(exp[ **a** _t_ ]). 

A second example would be the growth of noninteracting species of bacteria in a rich medium, which can be assumed proportional to the existing population of each species, thus producing an exponential growth in each component. The mass model (11) is still valid simply taking positive values in the rate vector **a** . Obviously, the compositional evolution is again that represented by Equation (12) and, therefore, this kind of process also follows a compositional line in the simplex. Naturally, we can imagine physical processes in which some components increase exponentially their mass, while others decrease exponentially and some of them remain constant. All these processes, when viewed as compositions, evolve following compositional lines in the simplex whatever the rate vector **a** . 

## **Parallel Compositional Processes** 

An important feature of linear compositional processes is that the direction **p** = C(exp[ **a** ]) does not depend on additive terms in the rate vector. This is due to the fact that 

**==> picture [229 x 10] intentionally omitted <==**

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**288** 

for any real δ and for **1** = [1, 1, . . . , 1]. Thus, different exponential evolutions of mass represent parallel compositional processes whenever their rate vectors differ in the same constant in all the components. Moreover, they follow the same compositional line whenever the initial condition is equal for the two processes or whenever they coincide in some evolutionary state. For instance, the following four rate vectors correspond to the same direction in S[3] : **a** 1 = [1, 2, 3], **a** 2 = [0, 1, 2], **a** 3 = [−1, 0, 1], **a** 4 = [−2, −1, 0]. Compositional lines following directions exp[ **a** _i_ ], _i_ = 1, 2, 3, are shown in Figure 1(A) and they are parallel. 

## **Constant Compositional Processes** 

Constant processes have also different meanings for mass processes and their compositional counterpart. For instance, the total mass in process (11) cannot be constant except for **a** being null. If **a** is null, both the mass process (11) and the compositional process (12) are constant. But, if a has the same value in each component, the mass process changes in time, but the composition remains constant. 

## **Orthogonal Compositional Processes** 

Different interpretations of orthogonality are required when observing processes in real space, with the standard Euclidean geometry, and the corresponding compositional processes. For instance, again in S[3] , consider two rate vectors **a** 1 = [1, 0, 0] and **a** 2 = [0, −1, −1] and the corresponding exponential mass processes **z** 1( _t_ ), **z** 2( _t_ ) as defined in Equation (11). One can observe that for any _t_ 1 and _t_ 2, **z** 1( _t_ 1) − **z** 1(0) is an orthogonal vector (ordinary Euclidean sense) to **z** 2( _t_ 2) − **z** 2(0). In fact, 

**==> picture [190 x 31] intentionally omitted <==**

and they are orthogonal (ordinary Euclidean sense) for any _t_ 1 and _t_ 2. Therefore, intuitively speaking, the mass change in the first component would be considered not to be related (linearly) to the variation of mass in the second and third components. But this orthogonality between the two mass processes is completely lost when the two processes are viewed as compositional: since the rate vectors **a** 1 and **a** 2 differ in an additive constant, they follow parallel compositional lines and, if initial conditions are equal or they coincide in some evolutionary state, they follow the same compositional line. The conclusion is clear: ordinary Euclidean orthogonality of mass processes does not imply orthogonality of the corresponding 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**289** 

compositional processes. Furthermore, ordinary Euclidean geometry of mass processes is not adapted to previously stated requirements on the geometry of compositional processes. We remark that mass processes are real positive valued and, following ideas in Pawlowsky-Glahn and Egozcue (2001), it is possible to define an alternative geometry for mass processes compatible with the compositional geometry. 

## **ORTHOGONALITY AND SUBCOMPOSITIONS** 

After discussing what _should not be_ orthogonality in S _[D]_ , a natural question is what should orthogonality be? Some intuitive ideas about subcompositions may point out desirable properties of orthogonality in the simplex. To this end, recall the example of deposition of masses. The statement _different materials do not interact_ implies that separating **x** ( _t_ ) into two subvectors, each one containing at least two components, **x** ( _t_ ) = ( **r** ( _t_ ), **s** ( _t_ )), should give two subcompositions, C( **r** ( _t_ )) ∈ S _[r]_ , C( **s** ( _t_ )) ∈ S _[s]_ , _D_ = _r_ + _s_ , that intuitively are not related. In our approach to the Aitchison geometry, this fact is equivalent to the statement C( **r** ( _t_ )) _and_ C( **s** ( _t_ )) _are orthogonal_ . 

In order to establish an orthogonality relationship between nonoverlapping compositions in S _[r]_ and S _[s]_ , it is necessary to imbed both spaces in a larger one, which we identify as S _[D]_ , with _D_ = _r_ + _s_ . The way of doing this is to define compositions in S _[D]_ associated with C( **r** ( _t_ )) and C( **s** ( _t_ )), respectively, 

**==> picture [245 x 11] intentionally omitted <==**

where **c** _s_ , denotes a vector whose _s_ components are equal to an arbitrary constant _c_ > 0, and analogously for **c** _r_[∗][,][made][up][of] _[r]_[equal][constants] _[c]_[∗][>][ 0.][This][con-] struction of **R** ( _t_ ) and **S** ( _t_ ) corresponds to compositional linear processes in S _[D]_ in which some components reproduce the evolution of the selected subcomposition but the remaining components are constant in time (i.e. they do not play any role both in the deposition of masses and in the corresponding compositional process). A requirement on **R** ( _t_ ) and **S** ( _t_ ) would be that the compositions 

**==> picture [255 x 9] intentionally omitted <==**

should be orthogonal whenever **R** 0( _t_ ) and **S** 0( _t_ ) are not constant processes. A valid question, which arises at this point, is the possible connection between this subcompositional orthogonality and partition independence (Aitchison, 1986), at least under certain model assumptions, particularly of additive logistic normality. Although we have preliminary results in this direction, they are not mature enough to be included in the present paper. 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**290** 

## **ORTHONORMAL BASES IN THE SIMPLEX** 

The aim of this section is to build up orthonormal bases—both general and associated to a partition of the full composition into subcompositions—of S _[D]_ in a practical way; these orthonormal bases will be the starting point to define isometric logratio transformations mapping S _[D]_ onto ℜ _[D]_[−][1] . 

## **General Expression** 

Orthonormal bases can be readily obtained by the standard Gram–Schmidt procedure once an independent set of _D_ − 1 compositions in S _[D]_ is given. This is known to be so for any vector space with an inner product. But we are interested in carrying out this process explicitly so that the orthonormal basis can be written immediately for any dimension. Once an orthonormal basis is obtained, we will study a special kind of orthonormal basis associated with a subcomposition. 

The step is to get a expression for the orthogonality of two compositions. The clr transformation (5) gives an adequate way. The clr transformation assigns each composition in S _[D]_ to a row vector **a** = clr( **x** ) in ℜ _[D]_ , satisfying _D_ � _i_ =1 _[a][i]_[=][ 0. Vectors satisfying such a condition constitute a (] _[D]_[ −][1)-dimensional] subspace of ℜ _[D]_ , denoted here by _V_ S . We remark that the ratio of the compositional parts to their geometric mean in the clr transformation is convenient because the clr image of the neutral composition **e** = C[1, 1, . . . , 1] is clr( **e** ) = [0, 0, . . . , 0], the neutral element in ℜ _[D]_ ; this is necessary to define an isomorphism of linear spaces between S _[D]_ and _V_ S . The inner product (4) can be expressed in the clr-transformed space as follows: for **a** = clr( **x** ) and **b** = clr( **y** ) 

**==> picture [257 x 27] intentionally omitted <==**

where the _D_ × _D_ matrix **M** is 

**==> picture [198 x 67] intentionally omitted <==**

The right hand side of Equation (16) defines a degenerate inner product in ℜ _[D]_ , whose metric matrix is **M** . Degeneracy of **M** is easily checked. It has two eigenvalues:0withmultiplicity1,and _D_ withmultiplicity _D_ − 1and,consequently, **M** is positive semidefinite. The eigenspace associated with the eigenvalue _D_ is 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**291** 

precisely the linear subspace _V_ S , defined by the condition[�] _i[D]_ =1 _[a][i]_[=][ 0 and, con-] sequently, clr( **y** ) **M** = _D_ clr( **y** ). This means that, when carrying out inner products by means of Equation (16), the result does not depend on the scaling value _g_ ( **x** ) used in the clr transformation. Consequently, for computing Aitchison inner products as indicated in Equation (16), we can change **a** = clr( **x** ) simply to **a** = ln( **x** ) = [ln _x_ 1, ln _x_ 2, . . . , ln _x D_ ] and ⟨ **x** , **y** ⟩ _a_ remains unaltered. This result is consistent with the fact that a composition **x** is just a representant of an equivalence class, as stated by Barcel´o-Vidal, Mart´ın-Fern´andez, and Pawlowsky-Glahn (2001). 

In order to obtain an orthonormal basis of the linear subspace associated with the eigenvalue _D_ (i.e. _V_ S ), we select a set of _D_ − 1 linearly independent vectors in that subspace. Let them be **v** 1, **v** 2, . . . , **v** _D_ −1 defined as **v** _i_ = [0, . . . , 0, 1, −1, 0, . . . , 0], the first non-null element being placed in the _i_ -th column. For any two vectors, **a** and **b** in _V_ S , the ordinary Euclidean inner product is ⟨ **a** , **b** ⟩= _D_[−][1] **aMb**[′] as pointed out before. Therefore, the Gram–Schmidt procedure, with respect to the ordinary Euclidean inner product, can be applied to **v** 1, **v** 2, . . . , **v** _D_ −1 and we obtain the following result. 

_Proposition 1. Let_ **u** _i_ ∈ℜ _[D]_ , _i_ = 1, 2, . . . , _D_ − 1 _, be the vectors_ 

**==> picture [246 x 49] intentionally omitted <==**

_The vectors_ **u** _i are orthonormal with respect to the ordinary Euclidean inner product in_ ℜ _[D] and constitute a basis of_ ( _D_ − 1 _)-dimensional linear subspace V_ S _._ 

_Proof:_ The vector **u** 1 = **v** 1/∥ **v** 1∥ is in _V_ S because its components add to zero. Assume now that the vectors **u** _i_ , _i_ = 1, 2, . . . , _k_ , are in _V_ S and that they are orthonormal. Applying the Gram–Schmidt procedure we obtain the next orthonormal vector 

**==> picture [242 x 29] intentionally omitted <==**

where ⟨·, ·⟩ denotes the ordinary Euclidean inner product in ℜ _[D]_ . The inner products in the summation vanish and the resulting expression defines **u** _k_ + _r_ ∈ _V_ S as stated in Equation (17). This completes the proof by induction. � 

As a consequence of the previous proposition, we can obtain an Aitchisonorthonormal basis in the simplex by applying clr[−][1] to the orthonormal vectors in _V_ S . 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**292** 

_Proposition 2. Let_ **e** _i_ , _i_ = 1, 2, . . . , _D_ − 1 _, be the following compositions in_ S _[D] :_ 

**==> picture [322 x 66] intentionally omitted <==**

_The compositions_ **e** _i_ , _i_ = 1, . . . , _D_ − 1 _, are orthonormal with respect to the Aitchison inner product (4) and they are a basis of_ S _[D] ._ 

_Proof:_ The Aitchison inner product between e _i_ , e _j_ can be computed using Equation (16): 

**==> picture [231 x 22] intentionally omitted <==**

for _i_ ̸= _j_ due to the orthogonality of **u** _i_ , **u** _j_ in ℜ _[D]_ with respect to both the standard metric in ℜ _[D]_ in and the metric _D_[−][1] **M** as stated in Proposition 1. Normalization to unity of e _i_ follows from the same expression by taking _i_ = _j_ . � 

Representations in S[3] of the axes associated with the orthonormal basis obtained are plotted as dashed lines in Figures 1(A)–5(A), with several geometric figures (squares, rectangle, circles) for illustration. 

Alternative choices of **v** _i_ can produce different orthonormal bases in the simplex. For instance, permutation of parts in the simplex permute the components of the basis, but we remark that different choices of **v** _i_ may lead to the same orthogonal basis. See e.g. Barcel´o-Vidal, Mart´ın-Fern´andez, and Pawlowsky-Glahn (2001) and Pawlowsky-Glahn (2002). 

## **Orthonormal Bases Associated to a Partition** 

Although Equation (18) gives an explicit Aitchison-orthonormal basis in S _[D]_ , its meaning is hardly intuitive. An alternative and interesting example is obtained whenever one tries to associate an orthonormal basis with a partition of the compositional vector **x** into two subcompositions, **x** = ( **r** , **s** ), where C( **r** ) ∈ S _[r]_ , C( **s** ) ∈ S _[s]_ , _D_ = _r_ + _s_ , _r_ ≥ 2, _s_ ≥ 2. Note that for _r_ = _D_ − 1 we get _s_ = 1, which corresponds to a degenerate case in the sense that we have a subcomposition with only one part. In the nondegenerate case, we look for an orthonormal basis such that the compositions of the form 

**293** 

## **Isometric Logratio Transformations for Compositional Data Analysis** 

**==> picture [200 x 86] intentionally omitted <==**

can be expressed by using _r_ − 1 elements of the orthonormal basis, denoted by **h** 1, **h** 2, . . . , **h** _r_ −1 forthefirstone,and _s_ − 1elements,denotedby **h** _r_ +1, **h** _r_ +2, . . . , **h** _D_ −1, for the second one. In this way, we associate the first _r_ − 1 elements of the basis with the subcomposition C( **r** ) and the last _s_ − 1 with the complementary subcomposition C( **s** ). To complete the orthonormal basis, we need an additional orthonormal vector, which we call _balancing element_ and denote by **h** _r_ ; the orthogonal projection—within the Aitchison geometry—of **x** on this element defines the mass ratio between the subcompositions **r** and **s** to reconstruct **x** . We claim that such an 

_Proposition 3. Let r_ ≥ 2, _s_ ≥ 2 _, be such that D_ = _r_ + _s. The compositions in_ S _[D] defined as_ 

**==> picture [305 x 55] intentionally omitted <==**

_for i_ = 1, 2, . . . , _r_ − 1 _,_ 

**==> picture [284 x 49] intentionally omitted <==**

_and, for j_ = 1, 2, . . . , _s_ − 1 _,_ 

**==> picture [316 x 61] intentionally omitted <==**

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**294** 

_are Aitchison-orthonormal and constitute a basis of_ S _[D] associated with a partition into two orthogonal subcompositions with, respectively, r and s components._ 

_Proof:_ Elements **h** _i_ in Equation (20) are orthonormal due to Proposition 2. The same argument applies to **h** _D_ − _j_ in Equation (22) after a reversion of components. We readily check orthogonality of the two sets of compositions by carrying out the inner product defined in Equation (16). Also the balancing **h** _r_ , is shown to have Aitchison-norm equal to 1 and to be orthogonal to the other elements by using Equation (16). � 

Proposition 3 is still valid in the degenerate case _r_ = _D_ − 1, _s_ = 1. The orthonormal basis consists then of those vectors given in Equations (20) and (21), whereas the vectors given by Equation (22) do not appear at all. Note that the orthogonal bases represented in Figures 1(A)–5(A) correspond to the degenerate case _r_ = 2, _s_ = 1, the straight dashed axis in an Euclidean sense corresponding to the balancing element and the other axis associated to the subcomposition ( _x_ 1, _x_ 2). 

The result can be easily generalized to more than two subcompositions. Thus, the main consequence of Proposition 3 is that any **x** ∈ S _[D]_ , _D_ > 3, can always be decom-posed into three orthogonal parts: two of them in orthogonal subspaces associated with two subcompositions and a balancing one. This was stated as an intuitive requirement of orthogonality in the simplex in the preceding section. This decomposition is 

**==> picture [283 x 47] intentionally omitted <==**

where the symbol ⊕ stands for repeated perturbation. 

## **ISOMETRIC LOGRATIO TRANSFORMATION** 

An isometry between S _[D]_ and ℜ _[D]_[−][1] can be obtained in a standard way if an Aitchison-orthonormal basis, **e** 1, **e** 2, . . . , **e** _D_ −1, is given. In fact, we look for a transformation, that we call isometric logratio transformation (ilr), such that ilr( **e** _i_ ) = ⃗e _i_ for _i_ = 1, 2, . . . , _D_ − 1; ⃗e _i_ being the _i_ th vector of the canonical basis in ℜ _[D]_[−][1] . Therefore, the desired transformation is defined as follows: 

_Definition 1. For any composition_ **x** ∈ S _[D] , the isometric logratio (ilr) transformation associated to an Aitchison-orthonormal basis in_ S _[D]_ , **e** _i_ , _i_ = 1, 2, . . . , _D_ − 1 _, is the transformation from_ S _[D] to_ ℜ _[D]_[−][1] _given by_ 

**==> picture [258 x 10] intentionally omitted <==**

**Isometric Logratio Transformations for Compositional Data Analysis** 

**295** 

The real vector ilr( **x** ) ∈ℜ _[D]_[−][1] can be identified with the coordinates of **x** ∈ S _[D]_ with respect to the basis **e** 1, **e** 2, . . . **e** _D_ −1. It can also be identified with coordinates with respect to the canonical basis in ℜ _[D]_[−][1] , leading to the equivalent expression: ⃗ ilr( **x** ) =[�] ⟨ **x** , **e** _i_ ⟩ _aei_ . Furthermore, from Equation (23) and orthonormality of the basis in S _[D]_ , we obtain the desired property ilr( **e** _i_ ) = ⃗ _ei_ for all _i_ . Then, the inverse ilr transformation corresponds to the expression of **x** in the reference basis of S _[D]_ 

**==> picture [228 x 28] intentionally omitted <==**

where ⟨ **y** , ⃗ _ei_ ⟩= ⟨ **x** , **e** _i_ ⟩ _a_ = _yi_ . From definition (23) isomorphism holds, i.e. if δ ∈ ℜ; **x** 1, **x** 2 ∈ S _[D]_ ; and **y** 1 = ilr( **x** 1), **y** 2 = ilr( **x** 2), then 

**==> picture [186 x 10] intentionally omitted <==**

The Aitchison inner product is transformed into the ordinary Euclidean one 

**==> picture [137 x 29] intentionally omitted <==**

where _y ji_ is the _i_ th component of row vector **y** _j_ and ⟨·, ·⟩ stands for the usual Euclidean inner product in ℜ _[D]_[−][1] Aitchison norms and distances are translated into ordinary ones in ilr-space, 

**==> picture [174 x 11] intentionally omitted <==**

where ∥ **y** _j_ ∥[2] =[�] _i[y]_[2] _ji_[is the ordinalry Euclidean norm of a vector in][ ℜ] _[D]_[−][1][.] The explicit expression of the ilr transformation is an important interpretative and computational tool. In order to obtain it, let us define 

**==> picture [283 x 49] intentionally omitted <==**

The square norm of such a composition is ∥ **h** ∥ _a_[2][=][ (] _[r]_[+] _[ s]_[)][/] _[rs]_[, as obtained using] 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**296** 

Equation (16). From Equation (16), and after some simple algebra we obtain 

**==> picture [246 x 25] intentionally omitted <==**

where _g_ (·) denotes geometric mean. The elements of the bases (18) and (20)–(22) have the form ∥ **h** ∥ _a_[−][1] ⊗ **h** ; then, ilr transformations with respect to these bases can be expressed using Equation (25). For instance, the components of **y** = ilr( **x** ) with respect to the basis (18) are 

**==> picture [230 x 26] intentionally omitted <==**

i.e. the ilr coordinates are logratios. 

basis in S _[D]_ . Particularly, this basis can be the one defined in Equation (18) in the previous section. Other bases can be used and they can be obtained from Equation (18) by using unitary transformations in S _[D]_ . But unitary transformations in S _[D]_ are easily obtained taking into account that ilr is actually an isometry. To see that this is so, let **P** be the matrix associated with an unitary transformation in ℜ _[D]_[−][1] ( _i.e_ . **PP**[′] = **P**[′] **P** = **I** where **I** stands for the identity matrix in ℜ _[D]_[−][1] ). It transforms the canonical basis into another orthonormal basis _h_[⃗] _i_ = ⃗ _ei_ **P** , _i_ = 1, 2, . . . , _D_ − 1. The inverse ilr transformation gives the transformed orthonormal basis in S _[D]_ . 

## **RELATIONSHIP BETWEEN TRANSFORMATIONS** 

Since alr and clr transformation have been extensively used in compositional data analysis, the relationship between them and the ilr family of transformations may be useful. Given that Aitchison-orthonormal bases are related through unitary transformations, it suffices to work with one of them. Therefore, we will work in what follows with a generic orthonormal basis **e** _i_ = C(exp **u** _i_ ) in S _[D]_ . Particularly, **u** _i_ can be taken as the basis (17) in ℜ _[D]_[−][1] or **e** _i_ as (18) in S _[D]_ . A first important aspect is the fact that clr( **e** _i_ ) = **u** _i_ . This can be easily checked by using the definition of the clr transformation (5). A second aspect, previously stated by Aitchison (1986), is that, for any **x** 1, **x** 2 ∈ S _[D]_ and α1, α2 ∈ℜ, 

**==> picture [265 x 10] intentionally omitted <==**

**==> picture [254 x 11] intentionally omitted <==**

**Isometric Logratio Transformations for Compositional Data Analysis** 

**297** 

**==> picture [74 x 28] intentionally omitted <==**

and its clr transformation is 

**==> picture [252 x 28] intentionally omitted <==**

where the ( _D_ − 1) × _D_ matrix **U** has the vectors clr( **e** _i_ ) = **u** _i_ as row vectors. Equation (27) allows us to go from the ilr representation of **x** to its representation by means of clr. The inverse relationship is not easily obtained from Equation (27) because it requires a generalized inversion of the rectangular matrix **U** . However, it has been implicitly found in Equation (16). In fact, 

**==> picture [312 x 21] intentionally omitted <==**

In order to determine the relationship between the ilr transformation and the alr transformation—with respect to the last component—let us recall its definition (Eq. (6)). 

The relationship between alr and clr is well known (Aitchison, 1986) and it is given by 

**==> picture [244 x 11] intentionally omitted <==**

where **I** _D_ −1 is the identity matrix of dimension ( _D_ − 1) and **1** _D_ −1 is a ( _D_ − 1) row vector of units. The inverse relationship between clr and alr can be expressed as 

**==> picture [196 x 10] intentionally omitted <==**

where the ( _D_ − 1) × _D_ matrix **A** is the Moore–Penrose generalized inverse of matrix **F** ; that is 

**==> picture [230 x 67] intentionally omitted <==**

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**298** 

Therefore, using Equations (27), (28), (29), and (30), we have 

**==> picture [167 x 11] intentionally omitted <==**

## Above results can be summarized as follows. 

_Proposition 4. Let_ _**x** be any composition in_ S _[D] and consider an orthonormal basis_ **e** _i_ , = C(exp **u** _i_ ), _i_ = 1, . . . , _D_ − 1, **e** _i_ ∈ S _[D]_ , **u** _i_ ∈ℜ _[D] . The logratio transformations,_ ilr _(_ **x** _)—with respect to the basis (Eq. 18)—_ clr _(_ **x** _) and_ alr _(_ **x** _)—with respect to the last component—are related by the following formulae_ 

**==> picture [159 x 27] intentionally omitted <==**

## **DISCUSSION** 

Geometry in the simplex—the sample space of compositional data—has been developed in the last 15 years mainly based on the contributions due to J. Aitchison. The main goal was to develop analytical tools for the statistical analysis of this type ofdata.MorerecentcontributionshaveidentifiedthesimplexasanEuclideanlinear space, being the perturbation and the power transformation, the internal operation and the product by scalars of the linear space. Particularly, the association of the Aitchison distance with a norm and an inner product has been made evident. Once these geometrical elements for the simplex are available, further efforts in interpretation and practical application of Aitchison geometry in the simplex are required, just clarifying the way for more complex statistical models within the logratio approach. 

Parallelism and orthogonality are properties of primary interest in Euclidean spaces. This motivated the interpretative results in the section on Exponential Growth and Decay of Mass as Compositional Processes, where the processes of exponential growth or decay of mass have been interpreted as linear in the simplex, i.e. as straight lines in the sense of Aitchison geometry. Parallelism and orthogonality are also briefly studied. 

The main theoretical result is the presentation of an explicit orthonormal basis in the simplex. An orthonormal basis allows us to represent any element of the simplex, a composition, by its coordinates in orthogonal axes as we normally do in real spaces. We only need to project the composition on each element of the basis by using the inner product. This representation, associated to the particular orthonormal basis, may be viewed as a transformation that assigns to each element in the simplex its coordinates; this transformation is a bijection and is isometric, i.e. Aitchison distances and angles in the simplex are transformed into ordinary 

**Isometric Logratio Transformations for Compositional Data Analysis** 

**299** 

Euclidean distances and angles in the real space of the coordinates. Moreover, the expression of the coordinates are log-contrasts, which motivates the name of _isometric logratio transformation_ , ilr, for this representation. 

The ilr coordinate expression of the elements of the simplex allows an effective and practical handling of compositional data. Once an orthonormal basis is selected, compositional data can be ilr-transformed, i.e. represented by their coordinates, and then analyzed as a standard multivariate data set in real space. 

The classical transformations clr (centered logratio) and alr (additive logratio) have been used in a similar way to analyze compositional data without zero parts: they are bijections, thus allowing the representation of compositions in real space. However, the image of S _[D]_ using the clr transformation, which is isometric, remains constrained to a subspace; and the alr transformation, leading to a representation free of constrains, is not isometric. The only difficulty in using ilr representation is the selection of the orthonormal basis of reference. 

However, the selection of a particular orthonormal basis may help interpretation of the ilr coordinates. The decomposition of the vector space S _[D]_ into orthogonal subspaces associated with nonoverlapping subcompositions is a particular but important result related to this issue. In fact, the presented result identifies a given subcomposition with an orthogonal projection in the simplex. It also gives the key to join compositions with different parts into a single composition by using a _balancing element_ . This is an important point to define independence of random compositions. 

Principal component analysis and singular value decomposition on the ilr coordinates (also on clr-transformed data) of compositional data without zero parts can also be interpreted as a particular selection of an orthonormal basis, which allows us dimension reduction and straightforward interpretations in data analysis. 

## **ACKNOWLEDGMENTS** 

This research has been supported by the Directi´on General de Ense˜anza Superior (DGES) of the Spanish Ministry for Education and Culture through the project BFM2000-0540. 

The authors thank J. Aitchison for his encouragement and challenging discussion. The authors also thank the reviewers D. Billheimer and R. M. Renner for their constructive and valuable advising. 

## **REFERENCES** 

> Aitchison, J., 1986, The statistical analysis of compositional data: Monographs on statistics and applied probability: Chapman & Hall Ltd., London, 416 p. 

> Aitchison, J., 1989, Measures of location of compositional data sets: Math. Geol., v. 21, no. 7, p. 787– 790. 

**Egozcue, Pawlowsky-Glahn, Mateu-Figueras, and Barcel´o-Vidal** 

**300** 

- Aitchison, J., 1990, Relative variation diagrams for describing patterns of compositional variability: Math. Geol., v. 22, no. 4, p. 487–511. 

- Aitchison, J., 1992, On criteria for measures of compositional difference: Math. Geol., v. 24, no. 4, p. 365–379. 

- Aitchison, J., 1997, The one-hour course in compositional data analysis or compositional data analysis is simple, _in_ V. Pawlowsky-Glahn, ed., Proceedings of the third annual conference of the International Association for Mathematical Geology, Vol. I, II and addendum: International Center for Numerical Methods in Engineering (CIMNE), Barcelona, p. 3–35. 

- Aitchison, J., 2002, Simplicial inference, _in_ M. A. G. Viana and D. S. P. Richards, eds., Contemporary Mathematics Series, Vol. 287: Algebraic Methods in Statistics and Probability: American Mathematical Society, Providence, Rhode Island, p. 1–22. 

- Aitchison, J., Barcel´o-Vidal, C., Mart´ın-Fern´andez, J. A., and Pawlowsky-Glahn, V., 2000, Logratio analysis and compositional distance: Math. Geol. v. 32, no. 3, p. 271–275. 

- Aitchison, J., and Thomas, C. W., 1998, Differential perturbation processes: A tool for the study of compositional processes, _in_ A. Buccianti, G. Nardi, and R. Potenza, eds., Proceedings of the fourth annual conference of the International Association for Mathematical Geology, Vol. I and II: De Frede Editore, Napoli, p. 499–504. 

- Barcel´o-Vidal, C., Mart´ın-Fernindez, J. A., and Pawlowsky-Glahn, V., 2001, Mathematical foundations of compositional data analysis: in G. Ross, ed., Proceedings of the sixth annual conference of the International Association for Mathematical Geology Cancun (Mexico) CD-Rom. 

- Berberian, S. K., 1961, Introduction to Hilbert space: Oxford University Press, New York, NY, 206 p. 

- Billheimer, D., Guttorp, P., and Fagan, W. F., 2001, Statistical interpretation of species composition: J. Am. Stat. Assoc., v. 96, no. 456, p. 1205–1214. 

- Mart´ın-Fern´andez, J. A., Olea-Meneses, R. A., and Pawlowsky-Glahn, V., 2001, Criteria to compare estimation methods of regionalized compositions: Math. Geol., v. 33, no. 8, p. 889–909. 

- Mart´ın-Fern´andez, J. A., Barcel´o-Vidal, C., and Pawlowsky-Glahn, V., 2003, Dealing with zeros and missing values in compositional data sets using nonparametric imputation: Math. Geol., v. 35, no. 3, p. 253–278. 

- Pawlowsky-Glahn, V., 2002, Lecture notes on statistical analysis of compositional data: Freie Universit¨at Berlin. 

- Pawlowsky-Glahn, V., and Egozcue, J. J., 2001, Geometric approach to statistical analysis on the simplex: Stoch. Environ. Res. Risk Assess., v. 15, no. 5, p. 384–398. 

- Pawlowsky-Glahn, V., and Egozcue, J. J., 2002, BLU estimators and compositional data: Math. Geol., v. 34, no. 3, p. 259–274. 

- von Eynatten, H., Pawlowsky-Glahn, V., and Egozcue, J. J., 2002, Understanding perturbation on the simplex: A simple method to better visualise and interpret compositional data in ternary diagrams: Math. Geol., v. 34, no. 3, p. 249–275. 

