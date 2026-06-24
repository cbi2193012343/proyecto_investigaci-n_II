# **Lecture Notes on Compositional Data Analysis** 

## **Vera Pawlowsky-Glahn** 

_University of Girona, Spain_ 

## **Juan Jos Egozcue** 

_Technical University of Catalonia, Spain_ 

## **Raimon Tolosana-Delgado** 

_Technical University of Catalonia, Spain_ 

March 2011 

ii 

i 

**Prof. Dr. Vera Pawlowsky-Glahn** Catedr´atica de Universidad (full professor) University of Girona Dept. of Computer Science and Applied Mathematics Campus Montilivi — P-4, E-17071 Girona, Spain vera.pawlowsky@udg.edu 

**Prof. Dr. Juan Jos´e Egozcue** Catedr´atico de Universidad (full professor) Technical University of Catalonia Dept. of Applied Mathematics III Campus Nord c/Jordi Girona 1-3, C-2, E-08034 Barcelona, Spain juan.jose.egozcue@upc.edu 

**Dr. Raimon Tolosana-Delgado** Investigador Juan de la Cierva Technical University of Catalonia Maritime Engineering Laboratory (LIM-UPC) Campus Nord c/Jordi Girona 1-3, D-1, E-08034 Barcelona, Spain raimon.tolosana@upc.edu 

ii 

## **Preface** 

These notes have been prepared as support to a short course on compositional data analysis. The first version dates back to the year 2000. Their aim is to transmit the basic concepts and skills for simple applications, thus setting the premises for more advanced projects. The notes have been updated over the years. But one should be aware that frequent updates will be still required in the near future, as the theory presented here is a field of active research. 

The notes are based both on the monograph by John Aitchison, _Statistical analysis of compositional data_ (1986), and on recent developments that complement the theory developed there, mainly those by Aitchison (1997); Barcel´o-Vidal et al. (2001); Billheimer et al. (2001); Pawlowsky-Glahn and Egozcue (2001, 2002); Aitchison et al. (2002); Egozcue et al. (2003); Pawlowsky-Glahn (2003) and Egozcue and Pawlowsky-Glahn (2005). To avoid constant references to mentioned documents, only complementary references will be given within the text. 

Readers should take into account that for a thorough understanding of compositional data analysis, a good knowledge in standard univariate statistics, basic linear algebra and calculus, complemented with an introduction to applied multivariate statistical analysis, is a must. The specific subjects of interest in multivariate statistics in real space can be learned in parallel from standard textbooks, like for instance Krzanowski (1988) and Krzanowski and Marriott (1994) (in English), Fahrmeir and Hamerle (1984) (in German), or Pe˜na (2002) (in Spanish). Thus, the intended audience goes from advanced students in applied sciences to practitioners. 

Concerning notation, it is important to note that, to conform to the standard praxis of registering samples as a matrix where each row is a sample and each column is a variate, vectors will be considered as row vectors to make the transfer from theoretical concepts to practical computations easier. 

Most chapters end with a list of exercises. They are formulated in such a way that they have to be solved using an appropriate software. CoDaPack is a user friendly freeware to facilitate this task and it can be downloaded from the web. Details about this package can be found in Thi´o-Henestrosa and Mart´ınFern´andez (2005) or Thi´o-Henestrosa et al. (2005). Those interested in working with R (or S-plus) may use the full-fledged package “compositions” by van den Boogaart and Tolosana-Delgado (2005). 

Girona, Barcelona, March 2011 

_Vera Pawlowsky-Glahn Juan Jos´e Egozcue Raimon Tolosana-Delgado_ 

iii 

**Acknowledgements.** We acknowledge the many comments made by readers, pointing at small and at important errors in the text. They all have contributed to improve the Lecture Notes presented here. We appreciate also the support received from our Universities, research groups, from the _Spanish Ministry of Education and Science_ under projects: ‘Ingenio Mathematica (i-MATH)’ Ref. No. CSD2006-00032 and ‘CODA-RSS’ Ref. MTM2009-13272; and from the _Ag`encia de Gesti´o d’Ajuts Universitaris i de Recerca_ of the _Generalitat de Catalunya_ under the project with Ref: 2009SGR424. 

iv 

## **Contents** 

|**1**|**Introduction**|**Introduction**||**1**|
|---|---|---|---|---|
|**2**|**Compositional data and their sample space**|||**5**|
||2.1|Basic concepts<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . . .|5|
||2.2|Principles of compositional analysis . . . . .|. . . . . . . . . . . .|7|
|||2.2.1<br>Scale invariance . . . . . . . . . . . .|. . . . . . . . . . . .|7|
|||2.2.2<br>Permutation invariance<br>. . . . . . .|. . . . . . . . . . . .|9|
|||2.2.3<br>Subcompositional coherence . . . . .|. . . . . . . . . . . .|10|
||2.3|Exercises<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .|10|
|**3**|**The **|**Aitchison geometry**||**13**|
||3.1|General comments . . . . . . . . . . . . . .|. . . . . . . . . . . .|13|
||3.2|Vector space structure . . . . . . . . . . . .|. . . . . . . . . . . .|14|
||3.3|Inner product, norm and distance . . . . . .|. . . . . . . . . . . .|16|
||3.4|Geometric fgures . . . . . . . . . . . . . . .|. . . . . . . . . . . .|17|
||3.5|Exercises<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .|18|
|**4**|**Coordinate representation**|||**21**|
||4.1|Introduction . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .|21|
||4.2|Compositional observations in real space . .|. . . . . . . . . . . .|22|
||4.3|Generating systems . . . . . . . . . . . . . .|. . . . . . . . . . . .|22|
||4.4|Orthonormal coordinates<br>. . . . . . . . . .|. . . . . . . . . . . .|24|
||4.5|Working in coordinates . . . . . . . . . . . .|. . . . . . . . . . . .|28|
||4.6|Additive log-ratio coordinates . . . . . . . .|. . . . . . . . . . . .|31|
||4.7|Simplicial matrix notation . . . . . . . . . .|. . . . . . . . . . . .|32|
||4.8|Exercises<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .|34|
|**5**|**Exploratory data analysis**|||**37**|
||5.1|General remarks<br>. . . . . . . . . . . . . . .|. . . . . . . . . . . .|37|
||5.2|Centre, total variance and variation matrix|. . . . . . . . . . . .|38|
||5.3|Centring and scaling . . . . . . . . . . . . .|. . . . . . . . . . . .|39|
||5.4|The biplot: a graphical display . . . . . . .|. . . . . . . . . . . .|40|
|||5.4.1<br>Construction of a biplot . . . . . . .|. . . . . . . . . . . .|40|
|||5.4.2<br>Interpretation of a compositional biplot . . . . . . . . . .||42|



v 

_CONTENTS_ 

|vi||_CONTEN_|_TS_|
|---|---|---|---|
||5.5|Exploratory analysis of coordinates . . . . . . . . . . . . . . . . .|43|
||5.6|Illustration<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|44|
||5.7|Linear trend using principal components . . . . . . . . . . . . . .|50|
||5.8|Exercises<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|52|
|**6**|**Distributions on the simplex**||**55**|
||6.1|The normal distribution on _SD_ . . . . . . . . . . . . . . . . . . .|55|
||6.2|Other distributions . . . . . . . . . . . . . . . . . . . . . . . . . .|56|
||6.3|Tests of normality on _SD_<br>. . . . . . . . . . . . . . . . . . . . . .|56|
|||6.3.1<br>Marginal univariate distributions . . . . . . . . . . . . . .|57|
|||6.3.2<br>Bivariate angle distribution . . . . . . . . . . . . . . . . .|59|
|||6.3.3<br>Radius test . . . . . . . . . . . . . . . . . . . . . . . . . .|60|
||6.4|Exercises<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
|**7**|**Statistical inference**||**63**|
||7.1|Testing hypothesis about two groups . . . . . . . . . . . . . . . .|63|
||7.2|Probability and confdence regions for compositional data . . . .|66|
||7.3|Exercises<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|67|
|**8**|**Compositional processes**||**69**|
||8.1|Linear processes: exponential growth or decay of mass . . . . . .|69|
||8.2|Complementary processes . . . . . . . . . . . . . . . . . . . . . .|72|
||8.3|Mixture process . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|**9**|**Linear compositional models**||**79**|
||9.1|Linear regression with compositional variables . . . . . . . . . . .|80|
||9.2|Regression with compositional covariates . . . . . . . . . . . . . .|83|
||9.3|Analysis of variance with compositional response . . . . . . . . .|84|
||9.4|Linear discrimination with compositional predictor . . . . . . . .|86|
|**A **|**Plotting a ternary diagram**||**91**|
|**B **|**Parametrisation of an elliptic region**||**93**|



## **Chapter 1** 

## **Introduction** 

The awareness of problems related to the statistical analysis of compositional data analysis dates back to a paper by Karl Pearson (1897) which title began _”_ significantly with the words _“On a form of spurious correlation ..._ . Since then, as stated in Aitchison and Egozcue (2005), the way to deal with this type of data has gone through roughly four phases, which they describe as follows: 

The pre-1960 phase rode on the crest of the developmental wave of standard multivariate statistical analysis, an appropriate form of analysis for the investigation of problems with real sample spaces. Despite the obvious fact that a compositional vector—with components the proportions of some whole—is subject to a constant-sum constraint, and so is entirely different from the unconstrained vector of standard unconstrained multivariate statistical analysis, scientists and statisticians alike seemed almost to delight in applying all the intricacies of standard multivariate analysis, in particular correlation analysis, to compositional vectors. We know that Karl Pearson, in his definitive 1897 paper on spurious correlations, had pointed out the pitfalls of interpretation of such activity, but it was not until around 1960 that specific condemnation of such an approach emerged. 

In the second phase, the primary critic of the application of standard multivariate analysis to compositional data was the geologist Felix Chayes (1960), whose main criticism was in the interpretation of product-moment correlation between components of a geochemical composition, with negative bias the distorting factor from the viewpoint of any sensible interpretation. For this problem of negative bias, often referred to as the closure problem, Sarmanov and Vistelius (1959) supplemented the Chayes criticism in geological applications and Mosimann (1962) drew the attention of biologists to it. However, even conscious researchers, instead of working towards an appropriate methodology, adopted what can only be described as 

1 

_CHAPTER 1. INTRODUCTION_ 

2 

a pathological approach: distortion of standard multivariate techniques when applied to compositional data was the main goal of study. 

The third phase was the realisation by Aitchison in the 1980’s that compositions provide information about relative, not absolute, values of components, that therefore every statement about a composition can be stated in terms of ratios of components (Aitchison, 1981, 1982, 1983, 1984). The facts that logratios are easier to handle mathematically than ratios and that a logratio transformation provides a one-to-one mapping on to a real space led to the advocacy of a methodology based on a variety of logratio transformations. These transformations allowed the use of standard unconstrained multivariate statistics applied to transformed data, with inferences translatable back into compositional statements. 

The fourth phase arises from the realisation that the internal simplicial operation of perturbation, the external operation of powering, and the simplicial metric, define a metric vector space (indeed a Hilbert space) (Billheimer et al., 1997, 2001; Pawlowsky-Glahn and Egozcue, 2001). So, many compositional problems can be investigated within this space with its specific algebraic-geometric structure. There has thus arisen a staying-in-the-simplex approach to the solution of many compositional problems (Mateu-Figueras, 2003; Pawlowsky-Glahn, 2003). This staying-in-the-simplex point of view proposes to represent compositions by their coordinates, as they live in an Euclidean space, and to interpret them and their relationships from their representation in the simplex. Accordingly, the sample space of random compositions is identified to be the simplex with a simplicial metric and measure, different from the usual Euclidean metric and Lebesgue measure in real space. 

The third phase, which mainly deals with (log-ratio) transformation of raw data, deserves special attention because these techniques have been very popular and successful over more than a century; from the Galton-McAlister introduction of such an idea in 1879 in their logarithmic transformation for positive data, through variancestabilising transformations for sound analysis of variance, to the general Box-Cox transformation (Box and Cox, 1964) and the implied transformations in generalised linear modeling. The logratio transformation principle was based on the fact that there is a one-toone correspondence between compositional vectors and associated logratio vectors, so that any statement about compositions can be reformulated in terms of logratios, and vice versa. The advantage of the transformation is that it removes the problem of a constrained sample space, the unit simplex, to one of an unconstrained space, multivariate real space, opening up all available standard multivariate techniques. The original transformations were principally the additive logratio transformation (Aitchison, 1986, p.113) and the 

3 

centred logratio transformation (Aitchison, 1986, p.79). The logratio transformation methodology seemed to be accepted by the statistical community; see for example the discussion of Aitchison (1982). The logratio methodology, however, drew fierce opposition from other disciplines, in particular from sections of the geological community. The reader who is interested in following the arguments that have arisen should examine the Letters to the Editor of Mathematical Geology over the period 1988 through 2002. 

The notes presented here correspond to the fourth phase. They pretend to summarise the state-of-the-art in the staying-in-the-simplex approach. Therefore, the first part will be devoted to the algebraic-geometric structure of the simplex, which we call _Aitchison geometry_ . 

4 

# _CHAPTER 1. INTRODUCTION_ 

## **Chapter 2 Compositional data and their sample space** 

## **2.1 Basic concepts** 

Definition 2.1.1 _A row vector,_ **x** = [ _x_ 1 _, x_ 2 _, . . . , xD_ ] _, is defined as a D-part composition when all its components are_ strictly positive real numbers _and they carry only_ relative information _._ 

Indeed, that compositional information is relative is implicitly stated in the units, as they are usually parts of a whole, like weight or volume percent, ppm, ppb, or molar proportions. The most common examples have _a constant sum κ_ and are known in the geological literature as _closed data_ (Chayes, 1971). Frequently, _κ_ = 1, which means that measurements have been made in, or transformed to, parts per unit, or _κ_ = 100, for measurements in percent. Other units are possible, like ppm or ppb, which are typical examples for compositional data where only a part of the composition has been recorded; or, as recent studies have shown, even concentration units (mg/L, meq/L, molarities and molalities), where no constant sum can be feasibly defined (Buccianti and Pawlowsky-Glahn, 2005; Otero et al., 2005). 

Definition 2.1.2 _The sample space of compositional data is the simplex, defined as_ 

**==> picture [325 x 31] intentionally omitted <==**

However, this definition does not include compositions in e.g. meq/L. Therefore, a more general definition, together with its interpretation, is given in Section 2.2. 

The components of a vector in _S[D]_ are called **parts** to remark their compositional character. 

5 

6 _CHAPTER 2. COMPOSITIONAL DATA AND THEIR SAMPLE SPACE_ 

**==> picture [276 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
C<br>P'<br>x2<br>P B p2 p1<br>P<br>constant sum<br>p3<br>A x1 B<br>**----- End of picture text -----**<br>


Figure 2.1: Left: Simplex imbedded in R[3] . Right: Ternary diagram. 

Definition 2.1.3 _For any vector of D real positive components_ 

**==> picture [108 x 13] intentionally omitted <==**

**==> picture [262 x 12] intentionally omitted <==**

**==> picture [185 x 30] intentionally omitted <==**

The result is the same vector re-scaled so that the sum of its components is _κ_ . This operation is required for a formal definition of subcomposition and for inverse transformations. Note that _κ_ depends on the units of measurement: usual values are 1 (proportions), 100 (%), 10[6] (ppm) and 10[9] (ppb). 

Definition 2.1.4 _Given a composition_ **x** _, a subcomposition_ **x** _s with s parts is obtained applying the closure operation to a subvector_ [ _xi_ 1 _, xi_ 2 _, . . . , xis_ ] _of_ **x** _. Subindexes i_ 1 _, . . . , is tell which parts are selected in the subcomposition, not necessarily the first s ones._ 

Very often, compositions contain many parts; e.g., the major oxide bulk composition of igneous rocks has around 10 elements, and they are but a few of the total possible. Nevertheless, one seldom represents the full composition. In fact, most of the applied literature on compositional data analysis (mainly in geology) restricts their figures to 3-part (sub)compositions. For 3 parts, the simplex can be represented as an equilateral triangle (Figure 2.1 left), with vertices at _A_ = [ _κ,_ 0 _,_ 0], _B_ = [0 _, κ,_ 0] and _C_ = [0 _,_ 0 _, κ_ ]. But this is commonly visualised in the form of a _ternary diagram_ —which is an equivalent representation—. A ternary diagram is an equilateral triangle such that a generic sample **p** = [ _p_ 1 _, p_ 2 _, p_ 3] will plot at a distance _p_ 1 from the opposite side of vertex _A_ , at a distance _p_ 2 from the opposite side of vertex _B_ , and at a distance _p_ 3 from the opposite side of vertex _C_ (Figure 2.1 right). The triplet [ _p_ 1 _, p_ 2 _, p_ 3] is commonly called the _barycentric coordinates_ of **p** , easily interpretable but useless in plotting (plotting them would yield the three-dimensional left-hand 

_2.2. PRINCIPLES OF COMPOSITIONAL ANALYSIS_ 

7 

plot of Figure 2.1). What is needed to get the right-hand plot of Figure 2.1) is the expression of the coordinates of the vertices and of the samples in a 2- dimensional Cartesian coordinate system [ _u, v_ ], and this is given in Appendix A. 

Finally, if only some parts of the composition are available, a fill up or residual value can be defined, or simply the observed subcomposition can be closed. Note that, since one seldom analyses every possible part, in practice only subcompositions are analysed. In any case, both methods (fill-up or closure) should lead to identical, or at least compatible, results. 

## **2.2 Principles of compositional analysis** 

Three conditions should be fulfilled by any statistical method to be applied to compositions: scale invariance, permutation invariance, and subcompositional coherence (Aitchison, 1986). 

## **2.2.1 Scale invariance** 

The most important characteristic of compositional data is that _they carry only relative information_ . Let us explain this concept with an example. In a paper with the suggestive title of “unexpected trend in the compositional maturity of second-cycle sands”, Solano-Acosta and Dutta (2005) the lithologic composition of a sandstone and of its derived recent sands is analysed looking at the percentage of grains made up of only quartz, of only feldspar, or of rock fragments. For medium sized grains coming from the parent sandstone, they report an average composition [ _Q, F, R_ ] = [53 _,_ 41 _,_ 6] %, whereas for the daughter sands the mean values are [37 _,_ 53 _,_ 10] %. One expects that feldspar and rock fragments decrease as the sediment matures, thus they should be less important in a second generation sand. “Unexpectedly” (or apparently), this does not happen in their example. To pass from the parent sandstone to the daughter sand, several different changes are possible, yielding exactly the same final composition. Assume those values were weight percent (in g/100 g of bulk sediment). Then, one of the following might have happened: 

- Q suffered no change passing from sandstone to sand, but per 100 g parent sandstone 35 g F and 8 g R were added to the sand (for instance, due to comminution of coarser grains of F and R from the sandstone), 

- F was unchanged, but per 100 g parent sandstone 25 g Q were depleted and at the same time 2 g R were added (for instance, because Q was better cemented in the sandstone, thus it tends to form coarser grains), 

- any combination of the former two extremes. 

The first two cases yield, per 100 g parent sandstone, final masses of [53 _,_ 76 _,_ 14] g, respectively [28 _,_ 41 _,_ 8] g. In a purely compositional data set, we do not know whether mass was added or subtracted from the sandstone to the sand. Thus, 

## 8 _CHAPTER 2. COMPOSITIONAL DATA AND THEIR SAMPLE SPACE_ 

which of these cases really occurred cannot be decided. Without further (noncompositional) information, there is no way to distinguish between [53 _,_ 76 _,_ 14] g and [28 _,_ 41 _,_ 8] g, as we only have the value of the sand composition _after closure_ . Closure is a projection of any point in the positive orthant of _D_ -dimensional real space onto the simplex. All points on a ray starting at the origin ( _e.g._ , [53 _,_ 76 _,_ 14] and [28 _,_ 41 _,_ 8]) are projected onto the same point of _S[D]_ ( _e.g._ , [37 _,_ 53 _,_ 10] %). The ray is an _equivalence class_ and the point on _S[D]_ a _representant_ of the class: Figure 2.2 shows this relationship. Moreover, to change the units of the data 

**==> picture [99 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
F<br>A<br>B<br>Q<br>**----- End of picture text -----**<br>


Figure 2.2: Representation of the compositional equivalence relationship. A represents the original sandstone composition, B the final sand composition, F the amount of each part if feldspar was added to the system (first hypothesis), and Q the amount of each part if quartz was depleted from the system (second hypothesis). Note that the points B, Q and F are compositionally equivalent. 

(for instance, from % to ppm), simply multiply all the points by the constant of change of units, moving them along their rays to the intersections with another triangle, parallel to the plotted one. 

Definition 2.2.1 _Two vectors of D positive real components_ **x** _,_ **y** _∈_ R _[D]_ + _[(][x][i][, y][i][≥]_ 0 _for all i_ = 1 _,_ 2 _, . . . , D), are_ compositionally equivalent _if there exists a positive scalar λ ∈_ R[+] _such that_ **x** = _λ ·_ **y** _and, equivalently, C_ ( **x** ) = _C_ ( **y** ) _._ 

It is highly reasonable to expect analyses to yield the same results, independently of the value of _λ_ . This is known as _scale invariance_ (Aitchison, 1986): 

Definition 2.2.2 _A function f_ ( _·_ ) _is scale-invariant if for any positive real value λ ∈_ R[+] _and for any composition_ **x** _∈S[D] , the function satisfies f_ ( _λ_ **x** ) = _f_ ( **x** ) _,_ i.e. _it yields the same result for all vectors compositionally equivalent._ 

Mathematically speaking, this is achieved if _f_ ( _·_ ) is a 0-degree homogeneous function of the parts in **x** . Practical choices of such functions are log-ratios of the parts in **x** (Aitchison, 1997; Barcel´o-Vidal et al., 2001). For instance, assume that **x** = [ _x_ 1 _, x_ 2 _, . . . , xD_ ] is a composition given in percentages. The ratio _f_ ( **x** ) = _x_ 1 _/x_ 2 = ( _λ · x_ 1) _/_ ( _λ · x_ 2) is scale invariant and yields the same results if the composition is given in different units, e.g. in parts per unit or in 

_2.2. PRINCIPLES OF COMPOSITIONAL ANALYSIS_ 

9 

parts per million, because units cancel in the ratio. However, ratios depend on the ordering of parts because _x_ 1 _/x_ 2 = _x_ 2 _/x_ 1. A convenient transformation of ratios is the corresponding log-ratio, _f_ ( **x** ) = ln( _x_ 1 _/x_ 2). Now, the inversion of the ratio only produces a change of sign, thus giving a symmetry to _f_ ( _·_ ) with respect to the ordering of parts. 

More complicated log-ratios are useful. For instance, define 

**==> picture [218 x 30] intentionally omitted <==**

where powers _αi_ are real constants (positive or negative). In the ratio expression, for _i_ = _s_ + 1 _, s_ + 2 _, . . . , D_ , _αi_ are assumed negative, thus appearing in the denominator with a positive value _−αi_ . For this log-ratio to be scale invariant, the sum of all powers should be null. Scale invariant log-ratios are called logcontrasts (Aitchison, 1986). 

Definition 2.2.3 _Consider a composition_ **x** = [ _x_ 1 _, x_ 2 _, . . . , xD_ ] _. A log-contrast is a function_ 

**==> picture [177 x 30] intentionally omitted <==**

In applications, some log-contrasts may be easily interpreted. A typical example is chemical equilibrium. Consider a chemical _D_ -part composition, denoted **x** expressed in ppm of mass. A chemical reaction involving four species may be 

**==> picture [131 x 9] intentionally omitted <==**

where other parts are not involved. The _αi_ ’s, called stoichiometric coefficients, are normally known. If the reaction is mass preserving, then _α_ 1 + _α_ 2 = _α_ 3 + _α_ 4. Whenever this chemical reaction is in equilibrium, the log-contrast 

**==> picture [50 x 25] intentionally omitted <==**

should be constant and, therefore, it is readily interpreted. 

## **2.2.2 Permutation invariance** 

A function is _permutation-invariant_ if it yields equivalent results when the ordering of the parts in the composition is changed. Two examples might illustrate what “ _equivalent_ ” means here. The _distance_ between the initial sandstone and the final sand compositions should be the same working with [ _Q, F, R_ ] or working with [ _F, R, Q_ ] (or any other _permutation_ of the parts). On the other side, if interest lies in the _change_ occurred from sandstone to sand, results should be equal after reordering. A classical way to get rid of the singularity of the classical covariance matrix of compositional data is to erase one component: this 

## 10 _CHAPTER 2. COMPOSITIONAL DATA AND THEIR SAMPLE SPACE_ 

procedure is not permutation-invariant, as results will largely depend on which component is erased. 

However, ordered compositional data are frequent. A typical case corresponds to the discretisation of a continuous variable. Some interval categories are defined on the span of the variable, and then the number of occurrences in each category are recorded as frequencies. These frequencies can be considered as a composition although categories are still ordered. The information concerning the ordering will be lost in a standard compositional analysis. 

## **2.2.3 Subcompositional coherence** 

The final condition is _subcompositional coherence_ : subcompositions should behave like orthogonal projections in conventional real analysis. The size of a projected segment is less than or equal to the size of the segment itself. This general principle, though shortly stated, has several practical implications, explained in the next chapters. The most illustrative, however, are the following. 

- The distance measured between two full compositions must be greater than (or at least equal to) the distance between them when considering any subcomposition. This particular behaviour of the distance is called _subcompositional dominance_ . Exercise 2.3.4 proves that the Euclidean distance between compositional vectors does not fulfill this condition, and it is thus ill-suited to measure distance between compositions. 

- If a non-informative part is erased, results should not change; for instance if hydrogeochemical data are available, and interest lies in classifying the kind of rocks washed by the water, in general the relations between some major oxides and ions will be used (SO[2+] 4[,][HCO] _[−]_ 3[,][Cl] _[−]_[,][to][mention][a] few), and the same results should be obtained taking meq/L (including implicitly water content), or weight percent of the ions of interest. 

Subcompositional coherence can be summarized as: (a) distances between two compositions should decrease when subcompositions of the original ones are considered; (b) scale invariance is preserved within arbitrary subcompositions (Egozcue, 2009). This means that the ratios between any parts in the subcomposition should be equal to the ratios in the original composition. 

## **2.3 Exercises** 

Exercise 2.3.1 _If data are measured in ppm, what is the value of the constant κ in definition (2.1.2)?_ 

Exercise 2.3.2 _Plot a ternary diagram using different values for the constant sum κ._ 

Exercise 2.3.3 _Verify that data in table 2.1 satisfy the conditions for being compositional. Plot them in a ternary diagram._ 

_2.3. EXERCISES_ 

11 

Table 2.1: Simulated data set (3 parts, 20 samples). 

||1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|_x_1|79.07|31.74|18.61|49.51|29.22|21.99|11.74|24.47|5.14|15.54|
|_x_2|12.83|56.69|72.05|15.11|52.36|59.91|65.04|52.53|38.39|57.34|
|_x_3|8.10|11.57|9.34|35.38|18.42|18.10|23.22|23.00|56.47|27.11|
||11|12|13|14|15|16|17|18|19|20|
|_x_1|57.17|52.25|77.40|10.54|46.14|16.29|32.27|40.73|49.29|61.49|
|_x_2|3.81|23.73|9.13|20.34|15.97|69.18|36.20|47.41|42.74|7.63|
|_x_3|39.02|24.02|13.47|69.12|37.89|14.53|31.53|11.86|7.97|30.88|



Exercise 2.3.4 _Compute the Euclidean distance between the first two vectors of table 2.1. Imagine originally a fourth variable x_ 4 _was measured, constant for all samples and equal to 5%. Take the first two vectors, close them to sum up to 95%, add the fourth variable to them (so that they sum up to 100%) and compute the Euclidean distance between the closed vectors. If the Euclidean distance is subcompositionally dominant, the distance measured in 4 parts must be greater or equal to the distance measured in the 3 part subcomposition._ 

12 _CHAPTER 2. COMPOSITIONAL DATA AND THEIR SAMPLE SPACE_ 

## **Chapter 3** 

## **The Aitchison geometry** 

## **3.1 General comments** 

In real space we are used to add vectors, to multiply them by a constant or scalar value, to look for properties like orthogonality, or to compute the distance between two points. All this, and much more, is possible because the real space is a linear vector space with an Euclidean metric structure. We are familiar with its geometric structure, the Euclidean geometry, and we represent our observations within this geometry. But this geometry is not a proper geometry for compositional data. 

To illustrate this assertion, consider the compositions 

## [5 _,_ 65 _,_ 30], [10 _,_ 60 _,_ 30], [50 _,_ 20 _,_ 30], and [55 _,_ 15 _,_ 30]. 

Intuitively we would say that the difference between [5 _,_ 65 _,_ 30] and [10 _,_ 60 _,_ 30] is not the same as the difference between [50 _,_ 20 _,_ 30] and [55 _,_ 15 _,_ 30]. The Euclidean distance between them is certainly the same, as there is a difference of 5 units both between the first and the second components, but in the first case the proportion in the first component is doubled, while in the second case the relative increase is about 10%, and this relative difference seems more adequate to describe compositional variability. This is not the only reason for discarding Euclidean geometry as a proper tool for analysing compositional data. Problems might appear in many situations, like those where results end up outside the sample space, e.g. when translating compositional vectors, or computing joint confidence regions for random compositions under assumptions of normality, or using hexagonal confidence regions. This last case is paradigmatic, as such hexagons are often naively cut when they lay partly outside the ternary diagram, and this without regard to any probability adjustment. This kind of problems are not just theoretical: they are practical and interpretative. 

What is needed is a sensible geometry to work with compositional data. In the simplex, things appear not as simple as they (apparently) are in real space, 

13 

_CHAPTER 3. THE AITCHISON GEOMETRY_ 

14 

but it is possible to find a way of working in it that is completely analogous. In fact, it is possible to define two operations which give the simplex a vector space structure. The first one is perturbation, which is analogous to addition in real space, the second one is powering, which is analogous to multiplication by a scalar in real space. Both require in their definition the closure operation; recall that closure is nothing else but the projection of a vector with positive components onto the simplex. Moreover, it is possible to obtain a Euclidean vector space structure on the simplex, just adding an inner product, a norm and a distance to the previous definitions. With the inner product compositions can be projected onto particular directions, one can check for orthogonality and determine angles between compositional vectors; with the norm the _length_ of a composition can be computed; the possibilities of a distance should be clear. With all together one can operate in the simplex in the same way as one operates in real space. 

## **3.2 Vector space structure** 

The basic operations required for a vector space structure of the simplex follow. They use the closure operation given in Definition 2.1.3. 

Definition 3.2.1 _Perturbation of a composition_ **x** _∈S[D] by a composition_ **y** _∈ S[D] ,_ 

**==> picture [147 x 11] intentionally omitted <==**

Definition 3.2.2 _Power transformation or powering of a composition_ **x** _∈S[D] by a constant α ∈_ R _,_ 

_α ⊙_ **x** = _C_ [ _x[α]_ 1 _[, x][α]_ 2 _[, . . . , x][α] D_[]] _[ .]_ 

For an illustration of the effect of perturbation and powering on a set of compositions, see Figure 3.1. 

Figure 3.1: Left: Perturbation of initial compositions ( _◦_ ) by **p** = [0 _._ 1 _,_ 0 _._ 1 _,_ 0 _._ 8] resulting in compositions ( _⋆_ ). Right: Powering of compositions ( _⋆_ ) by _α_ = 0 _._ 2 resulting in compositions ( _◦_ ). 

_3.2. VECTOR SPACE STRUCTURE_ 

15 

The simplex , ( _S[D] , ⊕, ⊙_ ), with perturbation and powering, is a vector space. This means the following properties hold, making them analogous to translation and scalar multiplication: 

Property 3.2.1 ( _S[D] , ⊕_ ) _has a commutative group structure; i.e., for_ **x** _,_ **y** _,_ **z** _∈S[D] it holds_ 

_1. commutative property:_ **x** _⊕_ **y** = **y** _⊕_ **x** _;_ 

_2. associative property:_ ( **x** _⊕_ **y** ) _⊕_ **z** = **x** _⊕_ ( **y** _⊕_ **z** ) _;_ 

_3. neutral element:_ 

**==> picture [163 x 25] intentionally omitted <==**

**n** _is the barycentre of the simplex and is unique;_ 

_4. inverse of_ **x** _:_ **x** _[−]_[1] = _C_ � _x[−]_ 1[1] _[, x][−]_ 2[1] _[, . . . , x][−] D_[1] � _; thus,_ **x** _⊕_ **x** _[−]_[1] = **n** _. By analogy with standard operations in real space, we will write_ **x** _⊕_ **y** _[−]_[1] = **x** _⊖_ **y** _._ 

Property 3.2.2 _Powering satisfies the properties of an external product. For_ **x** _,_ **y** _∈S[D] , α, β ∈_ R _it holds_ 

_1. associative property: α ⊙_ ( _β ⊙_ **x** ) = _α · β_ ) _⊙_ **x** _;_ 

_2. distributive property 1: α ⊙_ ( **x** _⊕_ **y** ) = ( _α ⊙_ **x** ) _⊕_ ( _α ⊙_ **y** ) _;_ 

_3. distributive property 2:_ ( _α_ + _β_ ) _⊙_ **x** = ( _α ⊙_ **x** ) _⊕_ ( _β ⊙_ **x** ) _;_ 

_4. neutral element:_ 1 _⊙_ **x** = **x** _; the neutral element is unique._ 

Note that the closure operation cancels out any constant and, thus, the closure constant itself is not important from a mathematical point of view. This fact allows us to omit the closure in intermediate steps of any computation without problem. It has also important implications for practical reasons, as shall be seen during simplicial principal component analysis. We can express this property for **z** _∈_ R _[D]_ +[and] **[x]** _[ ∈S][D]_[as] 

**==> picture [237 x 10] intentionally omitted <==**

Nevertheless, one should be always aware that the closure constant is very important for the correct interpretation of the units of the problem at hand. Therefore, controlling for the right units should be the last step in any analysis. 

_CHAPTER 3. THE AITCHISON GEOMETRY_ 

16 

## **3.3 Inner product, norm and distance** 

To obtain a Euclidean vector space structure, we take the following inner product, with associated norm and distance: 

Definition 3.3.1 _Inner product of_ **x** _,_ **y** _∈S[D] ,_ 

**==> picture [141 x 32] intentionally omitted <==**

Definition 3.3.2 _Norm of_ **x** _∈S[D] ,_ 

**==> picture [139 x 36] intentionally omitted <==**

Definition 3.3.3 _Distance between_ **x** _and_ **y** _∈S[D] ,_ 

**==> picture [239 x 37] intentionally omitted <==**

In practice, alternative but equivalent expressions of the inner product, norm and distance may be useful. Three possible alternatives for the inner product follow: 

**==> picture [244 x 106] intentionally omitted <==**

where g( _·_ ) denotes the geometric mean of the arguments. The last expression in 3.2 corresponds to an ordinary inner product of two real vectors. These vectors are called centered log-ratio (clr) of **x** , **y** , as defined in Chapter 4. Note that notation[�] _i<j_[means][exactly][�] _[D] i_ =1 _[−]_[1] � _Dj_ = _i_ +1[.][Moreover,][in][the][previous] expressions, simple logratios, ln( _xi/xj_ ), are null whenever _i_ = _j_ ; in these circumstances,[�] _[D] i_ =1 _[−]_[1] � _Dj_ = _i_ +1[= (1] _[/]_[2)][ �] _[D] i_ =1 � _Dj_ =1[.] 

To refer to the properties of ( _S[D] , ⊕, ⊙_ ) as an Euclidean linear vector space, we shall talk globally about the _Aitchison geometry on the simplex_ , and in particular about the Aitchison distance, norm and inner product. Note that in mathematical textbooks, such a linear vector space is called either real Euclidean space or finite dimensional real Hilbert space. 

_3.4. GEOMETRIC FIGURES_ 

17 

The algebraic-geometric structure of _S[D]_ satisfies standard properties, like compatibility of the distance with perturbation and powering, i.e. 

d _a_ ( **p** _⊕_ **x** _,_ **p** _⊕_ **y** ) = d _a_ ( **x** _,_ **y** ) _,_ d _a_ ( _α ⊙_ **x** _, α ⊙_ **y** ) = _|α|_ d _a_ ( **x** _,_ **y** ) _,_ 

for any **x** _,_ **y** _,_ **p** _∈S[D]_ and _α ∈_ R. Other typical properties of metric spaces are valid for _S[D]_ . Some of them follow: 

1. Cauchy-Schwartz inequality: 

**==> picture [104 x 11] intentionally omitted <==**

2. Pythagoras: If **x** , **y** are orthogonal, i.e. _⟨_ **x** _,_ **y** _⟩a_ = 0, then 

**==> picture [114 x 13] intentionally omitted <==**

3. Triangular inequality: 

**==> picture [135 x 11] intentionally omitted <==**

For a discussion of these and other properties, see Billheimer et al. (2001) or Pawlowsky-Glahn and Egozcue (2001). For a comparison with other measures of difference obtained as restrictions of distances in R _[D]_ to _S[D]_ , see Mart´ınFern´andez et al. (1998, 1999); Aitchison et al. (2000) or Mart´ın-Fern´andez (2001). The Aitchison distance is subcompositionally coherent, as all this set of operations induce the same linear vector space structure in the subspace corresponding to the subcomposition. Finally, the distance is subcompositionally dominant (Exercise 3.5.7). 

## **3.4 Geometric figures** 

Within this framework, we can define lines in _S[D]_ , which we call _compositional lines_ , as **y** = **x** 0 _⊕_ ( _α ⊙_ **x** ), with **x** 0 the starting point and **x** the leading vector. Note that **y** , **x** 0 and **x** are elements of _S[D]_ , while the coefficient _α_ varies in R. To illustrate what we understand by _compositional lines_ , Figure 3.2 shows two families of parallel lines in a ternary diagram, forming a square, orthogonal grid of side equal to one Aitchison distance unit. Recall that parallel lines have the same leading vector, but different starting points, like for instance **y1** = **x** 1 _⊕_ ( _α ⊙_ **x** ) and **y2** = **x** 2 _⊕_ ( _α ⊙_ **x** ), while orthogonal lines are those for which the inner product of the leading vectors is zero, i.e., for **y1** = **x** 0 _⊕_ ( _α_ 1 _⊙_ **x** 1) and **y2** = **x** 0 _⊕_ ( _α_ 2 _⊙_ **x** 2), with **x** 0 their intersection point and **x** 1, **x** 2 the corresponding leading vectors, it holds _⟨_ **x** 1 _,_ **x** 2 _⟩a_ = 0. Thus, _orthogonal_ means here that the inner product given in Definition 3.3.1 of the leading vectors of two lines, one of each family, is zero, and one Aitchison distance unit is measured by the distance given in Definition 3.3.3. 

Once we have a well defined geometry, it is straightforward to define any geometric figure, like for instance circles, ellipses, or rhomboids, as illustrated in Figure 3.3. 

18 

_CHAPTER 3. THE AITCHISON GEOMETRY_ 

**==> picture [270 x 120] intentionally omitted <==**

**----- Start of picture text -----**<br>
z z<br>x y x y<br>**----- End of picture text -----**<br>


Figure 3.2: Orthogonal grids of compositional lines in _S_[3] , equally spaced, 1 unit in Aitchison distance (Def. 3.3.3). The grid in the right is rotated 45 _[o]_ with respect to the grid in the left. 

**==> picture [156 x 126] intentionally omitted <==**

**==> picture [141 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1<br>n<br>x2 x3<br>**----- End of picture text -----**<br>


Figure 3.3: Circles and ellipses (left) and perturbation of a segment (right) in _S_[3] . 

## **3.5 Exercises** 

Exercise 3.5.1 _Consider the two vectors_ [0 _._ 7 _,_ 0 _._ 4 _,_ 0 _._ 8] _and_ [0 _._ 2 _,_ 0 _._ 8 _,_ 0 _._ 1] _. Perturb one vector by the other with and without previous closure. Is there any difference?_ 

Exercise 3.5.2 _Perturb each sample of the data set given in Table 2.1 with_ **x** 1 = _C_ [0 _._ 7 _,_ 0 _._ 4 _,_ 0 _._ 8] _and plot the initial and the resulting perturbed data set. What do you observe?_ 

Exercise 3.5.3 _Apply powering with α ranging from −_ 3 _to_ +3 _in steps of_ 0 _._ 5 _to_ **x** 1 = _C_ [0 _._ 7 _,_ 0 _._ 4 _,_ 0 _._ 8] _and plot the resulting set of compositions. Join them by a line. What do you observe?_ 

Exercise 3.5.4 _Perturb the compositions obtained in Ex. 3.5.3 by_ **x** 2 = _C_ [0 _._ 2 _,_ 0 _._ 8 _,_ 0 _._ 1] _. What is the result?_ 

_3.5. EXERCISES_ 

19 

Exercise 3.5.5 _Compute the Aitchison inner product of_ **x** 1 = _C_ [0 _._ 7 _,_ 0 _._ 4 _,_ 0 _._ 8] _and_ **x** 2 = _C_ [0 _._ 2 _,_ 0 _._ 8 _,_ 0 _._ 1] _. Are they orthogonal?_ 

Exercise 3.5.6 _Compute the Aitchison norm of_ **x** 1 = _C_ [0 _._ 7 _,_ 0 _._ 4 _,_ 0 _._ 8] _and call it a. Compute α ⊙_ **x** 1 _with α_ = 1 _/a. Compute the Aitchison norm of the resulting composition. How do you interpret the result?_ 

Exercise 3.5.7 _Re-do Exercise 2.3.4, but using the Aitchison distance given in Definition 3.3.3. Is it subcompositionally dominant?_ 

Exercise 3.5.8 _In a 2-part composition_ **x** = [ _x_ 1 _, x_ 2] _, simplify the formula for the Aitchison distance, taking x_ 2 = 1 _−x_ 1 _(using κ_ = 1 _). Use it to plot 7 equallyspaced points on the segment_ (0 _,_ 1) = _S_[2] _, from x_ 1 = 0 _._ 014 _to x_ 1 = 0 _._ 986 _._ 

Exercise 3.5.9 _In a mineral assemblage, several radioactive isotopes have been measured, obtaining_ �238U _,_ 232 Th _,_ 40 K� = [150 _,_ 30 _,_ 110] _ppm. Which will be the composition after_ ∆ _t_ = 10[9] _years? And after another_ ∆ _t years? Which was the composition_ ∆ _t years ago? And_ ∆ _t years before that? Close these 5 compositions and represent them in a ternary diagram. What do you see? Could you write the evolution as an equation? (Half-life disintegration periods:_ �238U _,_ 232 Th _,_ 40 K� = [4 _._ 468; 14 _._ 05; 1 _._ 277] _·_ 10[9] _years)_ 

20 

# _CHAPTER 3. THE AITCHISON GEOMETRY_ 

## **Chapter 4** 

## **Coordinate representation** 

## **4.1 Introduction** 

J. Aitchison (1986) used the fact that for compositional data size is irrelevant— as interest lies in relative proportions of the components measured—to introduce transformations based on ratios, the essential ones being the additive log-ratio transformation (alr) and the centred log-ratio transformation (clr). Then, he applied classical statistical analysis to the transformed observations, using the alr transformation for modeling, and the clr transformation for those techniques based on a metric. The underlying reason was, that the alr transformation does not preserve distances, whereas the clr transformation preserves distances but leads to a singular covariance matrix. In mathematical terms, we say that the alr transformation is an isomorphism, but not an isometry, while the clr transformation is an isometry, and thus also an isomorphism, but between _S[D]_ and a subspace of R _[D]_ , leading to degenerate distributions. Thus, Aitchison’s approach opened up a rigorous strategy, but care had to be applied when using either of both transformations. 

Using the Euclidean vector space structure, it is possible to give an algebraicgeometric foundation to his approach, and it is possible to go even a step further. Within this framework, a transformation of coefficients is equivalent to express observations in a different coordinate system. We are used to work in an orthogonal system, known as a Cartesian coordinate system; we know how to change coordinates within this system and how to rotate axis. But neither the clr nor the alr transformations can be directly associated with an orthogonal coordinate system in the simplex, a fact that lead Egozcue et al. (2003) to define a new transformation, called ilr (for _isometric logratio_ ) transformation, which is an isometry between _S[D]_ and R _[D][−]_[1] , thus avoiding the drawbacks of both the alr and the clr. The ilr stands actually for the association of coordinates with compositions in an orthonormal system in general, and this is the framework we are going to present here, together with a particular kind of coordinates, named balances, because of their usefulness for modeling and interpretation. 

21 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

22 

## **4.2 Compositional observations in real space** 

Compositions in _S[D]_ are usually expressed in terms of the canonical basis _{⃗_ **e** 1 _,⃗_ **e** 2 _, . . . ,⃗_ **e** _D}_ of R _[D]_ . In fact, any vector **x** _∈_ R _[D]_ can be written as 

**==> picture [336 x 30] intentionally omitted <==**

and this is the way we are used to interpret it. The problem is, that the set of vectors _{⃗_ **e** 1 _,⃗_ **e** 2 _, . . . ,⃗_ **e** _D}_ is neither a generating system nor a basis with respect to the vector space structure of _S[D]_ defined in Chapter 3. In fact, not every combination of coefficients gives an element of _S[D]_ (negative and zero values are not allowed), and the _⃗_ **e** _i_ do not belong to the simplex as defined in Equation (2.1). Nevertheless, in many cases it is interesting to express results in terms of compositions (4.1), so that interpretations are feasible in usual units, and therefore one of our purposes is to find a way to state statistically rigorous results in this coordinate system. 

## **4.3 Generating systems** 

A first step for defining an appropriate orthonormal basis consists in finding a generating system which can be used to build the basis. A natural way to obtain such a generating system is to take _{_ **w** 1 _,_ **w** 2 _, . . . ,_ **w** _D}_ , with 

**==> picture [298 x 11] intentionally omitted <==**

where in each **w** _i_ the number _e_ is placed in the _i_ -th column, and the operation exp( _·_ ) is assumed to operate component-wise on a vector. In fact, taking into account Equation (3.1) and the usual rules of precedence for operations in a vector space, i.e., first the external operation, _⊙_ , and afterwards the internal operation, _⊕_ , any vector **x** _∈S[D]_ can be written 

**==> picture [329 x 45] intentionally omitted <==**

It is known that the coefficients with respect to a generating system are not unique; thus, the following equivalent expression can be used as well, 

where 

**==> picture [259 x 104] intentionally omitted <==**

_4.3. GENERATING SYSTEMS_ 

23 

is the component-wise geometric mean of the composition. One recognises in the coefficients of this second expression the centred logratio transformation defined by Aitchison (1986). Note that one could indeed replace the denominator _by any constant_ . This non-uniqueness is consistent with the concept of compositions as equivalence classes (Barcel´o-Vidal et al., 2001). 

We will denote by clr the transformation that gives the expression of a composition in centred logratio coefficients 

**==> picture [268 x 25] intentionally omitted <==**

The inverse transformation, which gives us the coefficients in the canonical basis of real space, is then 

**==> picture [277 x 12] intentionally omitted <==**

The centred logratio transformation is symmetrical in the components, but the price is a new constraint on the transformed sample: the sum of the components has to be zero. This means that the transformed sample will lie on a plane, which goes through the origin of R _[D]_ and is orthogonal to the vector of unities [1 _,_ 1 _, . . . ,_ 1]. But, more importantly, it means also that for random compositions the covariance matrix of _**ξ**_ is singular, i.e. the determinant is zero. Certainly, generalised inverses can be used in this context when necessary, but not all statistical packages are designed for it and problems might arise during computation. Furthermore, clr coefficients are not subcompositionally coherent, because the geometric mean of the parts of a subcomposition g( **x** _s_ ) is not necessarily equal to that of the full composition, and thus the clr coefficients are in general not the same. A formal definition of the clr coefficients follows. 

Definition 4.3.1 _For a composition_ **x** _∈S[D] , the_ clr _coefficients are the components of_ _**ξ**_ = [ _ξ_ 1 _, ξ_ 2 _, . . . , ξD_ ] = clr( **x** ) _, the unique vector satisfying_ 

**==> picture [174 x 30] intentionally omitted <==**

_The i-th_ clr _coefficient is_ 

**==> picture [59 x 21] intentionally omitted <==**

_being_ g( **x** ) _the geometric mean of the components of_ **x** _._ 

Although the clr coefficients are not coordinates with respect to a basis of the simplex, they have very important properties. Among them the translation of operations and metrics from the simplex into the real space deserves special attention. Denote ordinary distance, norm and inner product in R _[D][−]_[1] by d( _·, ·_ ), _∥· ∥_ , and _⟨·, ·⟩_ respectively. The following property holds. 

24 

# _CHAPTER 4. COORDINATE REPRESENTATION_ 

Property 4.3.1 _Consider_ **x** _k ∈S[D] and real constants α, β; then_ 

clr( _α ⊙_ **x** 1 _⊕ β ⊙_ **x** 2) = _α ·_ clr( **x** 1) + _β ·_ clr( **x** 2) ; 

**==> picture [294 x 28] intentionally omitted <==**

## **4.4 Orthonormal coordinates** 

Omitting one vector of the generating system given in Equation (4.2) a basis is obtained. For example, omitting **w** _D_ results in _{_ **w** 1 _,_ **w** 2 _, . . . ,_ **w** _D−_ 1 _}_ . This basis is not orthonormal, as can be shown computing the inner product of any two of its vectors. But a new basis, orthonormal with respect to the inner product, can be readily obtained using the well-known Gram-Schmidt procedure (Egozcue et al., 2003). The basis thus obtained will be just one out of the infinitely many orthonormal basis which can be defined in any Euclidean space. Therefore, it is convenient to study their general characteristics. 

Let _{_ **e** 1 _,_ **e** 2 _, . . . ,_ **e** _D−_ 1 _}_ be a generic orthonormal basis of the simplex _S[D]_ and consider the ( _D −_ 1 _, D_ )-matrix **Ψ** whose rows are clr( **e** _i_ ). An orthonormal basis satisfies that _⟨_ **e** _i,_ **e** _j⟩a_ = _δij_ ( _δij_ is the Kronecker-delta, which is null for _i_ = _j_ , and one whenever _i_ = _j_ ). This can be expressed using (4.5), 

_⟨_ **e** _i,_ **e** _j⟩a_ = _⟨_ clr( **e** _i_ ) _,_ clr( **e** _j_ ) _⟩_ = _δij ._ 

It implies that the ( _D −_ 1 _, D_ )-matrix **Ψ** satisfies **ΨΨ** _[′]_ = _ID−_ 1, being _ID−_ 1 the identity matrix of dimension _D −_ 1. When the product of these matrices is reversed, then **Ψ** _[′]_ **Ψ** = _ID −_ (1 _/D_ ) **1** _[′] D_ **[1]** _[D]_[,][with] _[I][D]_[the][identity][matrix][of] dimension _D_ , and **1** _D_ a _D_ -row-vector of ones; note this is a matrix of rank _D −_ 1. The compositions of the basis are recovered from **Ψ** using clr _[−]_[1] in each row of the matrix. Recall that these rows of **Ψ** also add up to 0 because they are clr coefficients (see Definition 4.3.1). 

Once an orthonormal basis has been chosen, a composition **x** _∈S[D]_ is expressed as 

**==> picture [244 x 30] intentionally omitted <==**

where **x** _[∗]_ = � _x[∗]_ 1 _[, x][∗]_ 2 _[, . . . , x][∗] D−_ 1� is the vector of coordinates of **x** with respect to the selected basis. The function ilr : _S[D] →_ R _[D][−]_[1] , assigning the coordinates **x** _[∗]_ to **x** has been called ilr (isometric log-ratio) transformation, as it is an isometric isomorphism of vector spaces. For simplicity, sometimes this function is also denoted by _h_ , i.e. ilr _≡ h_ and also the asterisk ( _[∗]_ ) is used to denote coordinates if convenient. The following properties hold. 

Property 4.4.1 _Consider_ **x** _k ∈S[D] and real constants α, β; then_ 

_h_ ( _α ⊙_ **x** 1 _⊕ β ⊙_ **x** 2) = _α · h_ ( **x** 1) + _β · h_ ( **x** 2) = _α ·_ **x** _[∗]_ 1[+] _[ β][ ·]_ **[ x]** _[∗]_ 2[;] 

_4.4. ORTHONORMAL COORDINATES_ 

25 

**==> picture [165 x 11] intentionally omitted <==**

**==> picture [313 x 11] intentionally omitted <==**

The main difference between Property 4.3.1 for clr and Property 4.4.1 for ilr is that the former refers to vectors of coefficients in R _[D]_ , whereas the latter deals with vectors of coordinates in R _[D][−]_[1] , thus matching the actual dimension of _S[D]_ . 

Taking into account Properties 4.3.1 and 4.4.1, and using the clr image matrix of the basis, **Ψ** , the coordinates of a composition **x** can be expressed in a compact way. As written in (4.6), a coordinate is an Aitchison inner product, and it can be expressed as an ordinary inner product of the clr coefficients. Grouping all coordinates in a vector 

**==> picture [244 x 11] intentionally omitted <==**

a simple matrix product is obtained. 

Inversion of ilr, i.e. recovering the composition from its coordinates, corresponds to Equation (4.6). In fact, taking clr coefficients in both sides of (4.6) and taking into account Property 4.3.1, 

**==> picture [250 x 11] intentionally omitted <==**

A suitable algorithm to recover **x** from its coordinates **x** _[∗]_ consists of the following steps: (i) construct the clr-matrix of the basis, **Ψ** ; (ii) carry out the matrix product **x** _[∗]_ **Ψ** ; and (iii) apply clr _[−]_[1] to obtain **x** . 

There are several ways to define orthonormal bases in the simplex. The main criterion for the selection of an orthonormal basis is that it enhances the interpretability of the representation in coordinates. For instance, when performing principal component analysis an orthogonal basis is selected so that the first coordinate (principal component) represents the direction of maximum variability, etc. Particular cases deserving our attention are those bases linked to a sequential binary partition of the compositional vector (Egozcue and PawlowskyGlahn, 2005). The main interest of such bases is that they are easily interpreted in terms of grouped parts of the composition. The Cartesian coordinates of a composition in such a basis are called _balances_ and the compositions of the basis _balancing elements_ . A _sequential binary partition_ is a hierarchy of the parts of a composition. In the first order of the hierarchy, all parts are split into two groups. In the following steps, each group is in turn split into two groups, and the process continues until all groups have a single part, as illustrated in Table 4.1. For each order of the partition, it is possible to define the _balance_ between the two sub-groups formed at that level: if _i_ 1 _, i_ 2 _, . . . , ir_ are the _r_ parts of the first sub-group (coded by +1), and _j_ 1 _, j_ 2 _, . . . , js_ the _s_ parts of the second (coded by _−_ 1), the balance is defined as the normalised logratio of the geometric mean of each group of parts: 

**==> picture [296 x 30] intentionally omitted <==**

_CHAPTER 4. COORDINATE REPRESENTATION_ 

26 

Table 4.1: Example of sign matrix, used to encode a sequential binary partition and build an orthonormal basis. The lower part of the table shows the matrix **Ψ** of the basis. 

||order<br>_x_1<br>_x_2<br>_x_3<br>_x_4<br>_x_5<br>_x_6<br>r<br>s<br>1<br>+1<br>+1<br>_−_1<br>_−_1<br>+1<br>+1<br>4<br>2<br>2<br>+1<br>_−_1<br>0<br>0<br>_−_1<br>_−_1<br>1<br>3<br>3<br>0<br>+1<br>0<br>0<br>_−_1<br>_−_1<br>1<br>2<br>4<br>0<br>0<br>0<br>0<br>+1<br>_−_1<br>1<br>1<br>5<br>0<br>0<br>+1<br>_−_1<br>0<br>0<br>1<br>1|
|---|---|
|order|_x_1<br>_x_2<br>_x_3<br>_x_4<br>_x_5<br>_x_6<br><br><br><br><br><br>|
|1<br>2<br>3<br>4<br>5|1<br>4<br>~~�~~<br>4_·_2<br>4+2<br>1<br>4<br>~~�~~<br>4_·_2<br>4+2<br>_−_1<br>2<br>~~�~~<br>4_·_2<br>4+2<br>_−_1<br>2<br>~~�~~<br>4_·_2<br>4+2<br>1<br>4<br>~~�~~<br>4_·_2<br>4+2<br>1<br>4<br>~~�~~<br>4_·_2<br>4+2<br>+<br>_√_<br>3<br>2<br>_−_<br>1<br>~~_√_~~<br>12<br>0<br>0<br>_−_<br>1<br>~~_√_~~<br>12<br>_−_<br>1<br>~~_√_~~<br>12<br>0<br>+<br>~~_√_~~<br>2<br>~~_√_~~<br>3<br>0<br>0<br>_−_1<br>~~_√_~~<br>6<br>_−_1<br>~~_√_~~<br>6<br>0<br>0<br>0<br>0<br>+ 1<br>~~_√_~~<br>2<br>_−_1<br>~~_√_~~<br>2<br>0<br>0<br>+ 1<br>~~_√_~~<br>2<br>_−_1<br>~~_√_~~<br>2<br>0<br>0|



where 

**==> picture [285 x 25] intentionally omitted <==**

_a_ + for parts in the numerator, _a−_ for parts in the denominator, and _a_ 0 for parts not involved in that splitting. The balance is then 

**==> picture [77 x 32] intentionally omitted <==**

where _aij_ equals _a_ + if the code, at the _i_ -th order partition, is +1 for the _j_ -th part; the value is _a−_ if the code is _−_ 1; and _a_ 0 = 0 if the code is null, using the values of _r_ and _s_ at the _i_ -th order partition. Note that the matrix with entries _aij_ is just the matrix **Ψ** , as shown in the lower part of Table 4.1. 

Example 4.4.1 _In Egozcue et al. (2003) an orthonormal basis of the simplex was obtained using a Gram-Schmidt technique. It corresponds to the sequential binary partition shown in Table 4.2. The main feature is that the entries of the_ **Ψ** _matrix can be easily expressed as_ 

**==> picture [217 x 64] intentionally omitted <==**

_and_ **Ψ** _ij_ = 0 _otherwise. This matrix is closely related to Helmert matrices._ 

_4.4. ORTHONORMAL COORDINATES_ 

27 

Table 4.2: Example of sign matrix for _D_ = 5, used to encode a sequential binary partition in a standard way. The lower part of the table shows the matrix **Ψ** of the basis. 

|level||_x_1||_x_2|||_x_3|||_x_4|_x_5|r|s|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1||+1||+1|||+1|||+1|_−_1|4|1|
|2||+1||+1|||+1|||_−_1|0|3|1|
|3||+1||+1|||_−_1|||0|0|2|1|
|4||+1||_−_1|||0|||0|0|1|1|
|1|+|1<br>~~_√_~~<br>20|+|1<br>~~_√_~~<br>20|+|1<br>~~_√_~~<br>20||+|1<br>~~_√_~~<br>20||_−_2<br>~~_√_~~<br>5|||
|2|+|1<br>~~_√_~~<br>12|+|1<br>~~_√_~~<br>12|+|1<br>~~_√_~~<br>12||_−_||_√_<br>3<br>~~_√_~~<br>4|0|||
|3<br>4|+ 1<br>~~_√_~~<br>6<br>+ 1<br>~~_√_~~<br>2||+ 1<br>~~_√_~~<br>6<br>_−_1<br>~~_√_~~<br>2||_−_||~~_√_~~<br>2<br>~~_√_~~<br>3<br>0|||0<br>0|0<br>0|||



The interpretation of balances relays on some of its properties. The first one is the expression itself, specially when using geometric means in the numerator and denominator as in 

**==> picture [141 x 26] intentionally omitted <==**

The geometric means are central values of the parts in each group of parts; its ratio measures the relative weight of each group; the logarithm provides the appropriate scale; and the square root coefficient is a normalising constant which allows to compare numerically different balances. A positive balance means that, in (geometric) mean, the group of parts in the numerator has more weight in the composition than the group in the denominator (and conversely for negative balances). 

A second interpretative element is related to the intuitive idea of balance. Imagine that in an election, the parties have been divided into two groups, the left and the right wing ones (there are more than one party in each wing). If, from a journal, you get only the percentages within each group, you are unable to know which wing, and obviously which party, has won the elections. You probably are going to ask for the balance between the two wings as the information you need to complete the actual state of the elections. The balance, as defined here, permits you to complete the information. The balance is the remaining relative information about the elections once the information within the two wings has been removed. To be more precise, assume that the parties are six and the composition of the votes is **x** _∈S_[6] ; assume the left wing contested with 4 parties represented by the group of parts _{x_ 1 _, x_ 2 _, x_ 5 _, x_ 6 _}_ and only two parties correspond to the right wing _{x_ 3 _, x_ 4 _}_ . Consider the sequential binary partition in Table 4.1. The first partition just separates the two wings and thus the balance informs us about the equilibrium between the two wings. If one 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

28 

leaves out this balance, the remaining balances inform us only about the left wing (balances 3,4) and only about the right wing (balance 5). Therefore, to retain only balance 5 is equivalent to know the relative information within the subcomposition called right wing. Similarly, balances 2, 3 and 4 only inform about what happened within the left wing. The conclusion is that the balance 1, the forgotten information in the journal, does not inform us about relations within the two wings: it only conveys information about the _balance_ between the two groups representing the wings. 

Many questions can be stated which can be handled easily using the balances. For instance, suppose we are interested in the relationships between the parties within the left wing and, consequently, we want to remove the information within the right wing. A traditional approach to this is to remove parts _x_ 3 and _x_ 4 and then close the remaining subcomposition. However, this is equivalent to project the composition of 6 parts orthogonally onto the subspace associated with the left wing, what is easily done by setting _b_ 5 = 0. If we do so, the obtained projected composition is 

**==> picture [293 x 13] intentionally omitted <==**

i.e. each part in the right wing has been substituted by the geometric mean within the right wing. This composition still has the information on the leftright balance, _b_ 1. If we are also interested in removing it ( _b_ 1 = 0), the remaining information will be only that within the left-wing subcomposition which is represented by the orthogonal projection 

**==> picture [245 x 11] intentionally omitted <==**

with g( _x_ 1 _, x_ 2 _, x_ 5 _, x_ 6) = ( _x_ 1 _, x_ 2 _, x_ 5 _, x_ 6)[1] _[/]_[4] _._ The conclusion is that the balances can be very useful to project compositions onto special subspaces just by retaining some balances and making other ones null. 

## **4.5 Working in coordinates** 

Coordinates with respect to an orthonormal basis in a linear vector space underly standard rules of operation in real space. As a consequence, perturbation in _S[D]_ is equivalent to translation in real space, and power transformation in _S[D]_ is equivalent to multiplication. Thus, if we consider the vector of coordinates _h_ ( **x** ) = **x** _[∗] ∈_ R _[D][−]_[1] of a compositional vector **x** _∈S[D]_ with respect to an arbitrary orthonormal basis, it holds (Property 4.4.1) 

**==> picture [333 x 11] intentionally omitted <==**

and we can think about perturbation as having the same properties in the simplex as translation has in real space, and of the power transformation as having the same properties as multiplication. 

Furthermore, 

**==> picture [161 x 11] intentionally omitted <==**

29 

## _4.5. WORKING IN COORDINATES_ 

where d stands for the usual Euclidean distance in real space. This means that, when performing analysis of compositional data, results that could be obtained using compositions and the Aitchison geometry are exactly the same as those obtained using the coordinates of the compositions and using the ordinary Euclidean geometry. This latter possibility reduces the computations to the ordinary operations in real spaces thus facilitating the applied procedures. The duality of the representation of compositions, in the simplex and by coordinates, introduces a rich framework where both representations can be interpreted to extract conclusions from the analysis (see Figures 4.1, 4.2, 4.3, and 4.4, for illustration). The price is that the basis selected for representation should be carefully selected for an enhanced interpretation. 

Working on coordinates can be also done in a blind way, just selecting a default basis and coordinates and, when the results in coordinates are obtained, translating the results back into the simplex for interpretation. This blind strategy, although acceptable, hides to the analyst features of the analysis that may be relevant. For instance, when detecting a linear dependence of compositional data on an external covariate, data can be expressed in coordinates and then the dependence estimated using standard linear regression. Back in the simplex, data can be plotted with the estimated regression line in a ternary diagram. The procedure is completely acceptable but the visual picture of the residuals and a possible non-linear trend in them can be hidden or distorted in the ternary diagram. A plot of the fitted line and the data in coordinates may reveal new interpretable features. 

**==> picture [279 x 119] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1 2<br>1<br>0<br>n<br>-1<br>-2<br>x2 x3 -2 -1 0 1 2<br>**----- End of picture text -----**<br>


Figure 4.1: Perturbation of a segment in _S_[3] (left) and in coordinates (right). 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

30 

**==> picture [330 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1<br>3 2<br>3<br>2<br>2<br>1<br>1<br>1<br>0<br>0<br>-1<br>0<br>-2<br>-1 -1<br>-2 -3<br>-3 -2<br>x2 x3 -4 -3 -2 -1 0 1 2 3 4<br>**----- End of picture text -----**<br>


Figure 4.2: Powering of a vector in _S_[3] (left) and in coordinates (right). 

**==> picture [139 x 112] intentionally omitted <==**

**==> picture [121 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>3<br>2<br>1<br>0<br>-2 -1 0 1 2 3<br>-1<br>-2<br>**----- End of picture text -----**<br>


Figure 4.3: Circles and ellipses in _S_[3] (left) and in coordinates (right). 

_4.6. ADDITIVE LOG-RATIO COORDINATES_ 

31 

**==> picture [279 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1 4<br>2<br>0<br>-4 -2 0 2 4<br>n -2<br>x2 x3 -4<br>**----- End of picture text -----**<br>


Figure 4.4: Couples of parallel lines in _S_[3] (left) and in coordinates (right). 

One point is essential in the proposed approach: no zero values are allowed, as neither division by zero is admissible, nor taking the logarithm of zero. We are not going to discuss this subject here. Methods on how to approach the problem have been discussed by Aitchison (1986); Aitchison and Kay (2003); Bacon-Shone (2003); Fry et al. (1996); Mart´ın-Fern´andez (2001) and Mart´ınFern´andez et al. (2000; 2003). 

## **4.6 Additive log-ratio coordinates** 

In section 4.3 we considered the generating system of the simplex (4.2). One of the elements, e.g. the last one, can be suppressed to obtain a basis: _{_ **w** 1 _,_ **w** 2 _, . . . ,_ **w** _D−_ 1 _}_ . Then, any composition **x** _∈S[D]_ can be written 

**==> picture [274 x 54] intentionally omitted <==**

The coordinates correspond to the well known additive log-ratio transformation (alr) introduced by Aitchison (1986). We will denote by alr the transformation that gives the expression of a composition in additive log-ratio coordinates 

**==> picture [180 x 25] intentionally omitted <==**

Note that the alr transformation is not symmetrical in the components. But the essential problem with alr coordinates is the non-isometric character of this transformation. In fact, they are coordinates in an oblique basis, something that affects distances if the usual Euclidean distance is computed from the alr coordinates. This approach is frequent in many applied sciences and should be avoided (see for example Albar`ede (1995), p. 42). 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

32 

## **4.7 Simplicial matrix notation** 

Many operations in real spaces are expressed in matrix notation. Since the simplex is an Euclidean space, matrix notations may be also useful. However, in this framework a vector of real constants cannot be considered in the simplex although in the real space they are readily identified. This produces two kind of matrix products which are introduced in this section. The first is simply the expression of a perturbation-linear combination of compositions which appears as a power-multiplication of a real vector by a compositional matrix whose rows are in the simplex. The second one is the expression of a linear transformation in the simplex: a composition is transformed by a matrix, involving perturbation and powering, to obtain a new composition. The real matrix implied in this case is not a general one but when expressed in coordinates it is completely general. 

## **Perturbation-linear combination of compositions** 

For a row vector of _ℓ_ scalars **a** = [ _a_ 1 _, a_ 2 _, . . . , aℓ_ ] and an array of row vectors **V** = ( **v1** _,_ **v2** _, . . . ,_ **v** _ℓ_ ) _[′]_ , i.e. an ( _ℓ, D_ )-matrix, 

**==> picture [143 x 55] intentionally omitted <==**

**==> picture [251 x 55] intentionally omitted <==**

The components of this matrix product are 

**==> picture [199 x 37] intentionally omitted <==**

In coordinates this simplicial matrix product takes the form of a linear combination of the coordinate vectors. In fact, if _h_ is the function assigning the coordinates, 

**==> picture [195 x 31] intentionally omitted <==**

Example 4.7.1 _A composition in S[D] can be expressed as a perturbation-linear combination of the elements of the basis_ **e** _i, i_ = 1 _,_ 2 _, . . . , D −_ 1 _as in Equation (4.6). Consider the_ ( _D −_ 1 _, D_ ) _-matrix_ **E** = ( **e** 1 _,_ **e** 2 _, . . . ,_ **e** _D−_ 1) _[′] and the vector of coordinates_ **x** _[∗]_ = ilr( **x** ) _. Equation (4.6) can be re-written as_ 

**x** = **x** _[∗] ⊙_ **E** _._ 

_4.7. SIMPLICIAL MATRIX NOTATION_ 

33 

## **Perturbation-linear transformation of** _S[D]_ **: endomorphisms** 

Consider a row vector of coordinates **x** _[∗] ∈_ R _[D][−]_[1] and a general ( _D −_ 1 _, D −_ 1)matrix _A[∗]_ . In the real space setting, **y** _[∗]_ = **x** _[∗] A[∗]_ expresses an endomorphism, obviously linear in the real sense. Given the isometric isomorphism of the real space of coordinates onto the simplex, the _A[∗]_ endomorphism has an expression in the simplex. Taking ilr _[−]_[1] = _h[−]_[1] in the expression of the real endomorphism and using Equation (4.8) 

**==> picture [268 x 12] intentionally omitted <==**

where **Ψ** is the clr matrix of the selected basis and the right-most member has been obtained applying Equation (4.7) to **x** _[∗]_ . The ( _D, D_ )-matrix _A_ = **Ψ** _[′] A[∗]_ **Ψ** has entries 

**==> picture [204 x 31] intentionally omitted <==**

Substituting clr( **x** ) by its expression as a function of the logarithms of parts, the composition **y** is 

**==> picture [190 x 37] intentionally omitted <==**

which, taking into account that products and powers match the definitions of _⊕_ and _⊙_ , deserves the definition 

**==> picture [232 x 12] intentionally omitted <==**

where _◦_ is the perturbation-matrix product representing an endomorphism in the simplex. This matrix product in the simplex should not be confused with that defined between a vector of scalars and a matrix of compositions and denoted by _⊙_ . 

An important conclusion is that endomorphisms in the simplex are represented by matrices with a peculiar structure given by _A_ = **Ψ** _[′] A[∗]_ **Ψ** , which have some remarkable properties: 

- (a) it is a ( _D, D_ ) real matrix; 

- (b) each row and each column of _A_ adds to 0; 

- (c) rank( _A_ ) = rank( _A[∗]_ ); particularly, when _A[∗]_ is full-rank, rank( _A_ ) = _D −_ 1; 

- (d) the identity endomorphism corresponds to _A[∗]_ = _ID−_ 1, the identity in R _[D][−]_[1] , and to _A_ = **Ψ** _[′]_ **Ψ** = _ID −_ (1 _/D_ ) **1** _[′] D_ **[1]** _[D]_[,][where] _[I][D]_[is][the][identity] ( _D, D_ )-matrix, and **1** _D_ is a row vector of ones. 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

34 

The matrix _A[∗]_ can be recovered from _A_ as _A[∗]_ = **Ψ** _A_ **Ψ** _[′]_ . However, _A_ is not the only matrix corresponding to _A[∗]_ in this transformation. Consider the following ( _D, D_ )-matrix 

**==> picture [167 x 32] intentionally omitted <==**

where, _A_ 0 satisfies the above conditions, _⃗ei_ = [0 _,_ 0 _, . . . ,_ 1 _, . . . ,_ 0 _,_ 0] is the _i_ -th row-vector in the canonical basis of R _[D]_ , and _ci_ , _dj_ are arbitrary constants. Each additive term in this expression adds a constant row or column, being the remaining entries null. A simple development proves that _A[∗]_ = **Ψ** _A_ **Ψ** _[′]_ = **Ψ** _A_ 0 **Ψ** _[′]_ . This means that **x** _◦ A_ = **x** _◦ A_ 0, i.e. _A_ , _A_ 0 define the same linear transformation in the simplex. To obtain _A_ 0 from _A_ , first compute _A[∗]_ = **Ψ** _A_ **Ψ** _[′]_ and then compute 

**==> picture [315 x 12] intentionally omitted <==**

where the second member is the required computation and the third member explains that the computation is equivalent to add constant rows and columns to _A_ . 

Example 4.7.2 _Consider the matrix_ 

**==> picture [76 x 25] intentionally omitted <==**

_representing a linear transformation in S_[2] _. The matrix_ **Ψ** _is_ 

**==> picture [85 x 25] intentionally omitted <==**

_In coordinates, this corresponds to a_ (1 _,_ 1) _-matrix A[∗]_ = ( _−_ ( _a_ 1 + _a_ 2) _/_ 2) _. The equivalent matrix A_ 0 = **Ψ** _[′] A[∗]_ **Ψ** _is_ 

**==> picture [135 x 25] intentionally omitted <==**

_whose columns and rows add to_ 0 _._ 

## **4.8 Exercises** 

Exercise 4.8.1 _Consider the data set given in Table 2.1. Compute the_ clr _coefficients (Eq. 4.3) to compositions with no zeros. Verify that the sum of the transformed components equals zero._ 

Exercise 4.8.2 _Using the sign matrix of Table 4.1 and Equation (4.10), compute the coefficients for each part at each level. Arrange them in a_ 6 _×_ 5 _matrix. Which are the vectors of this basis?_ 

_4.8. EXERCISES_ 

35 

Exercise 4.8.3 _Consider the 6-part composition_ 

[ _x_ 1 _, x_ 2 _, x_ 3 _, x_ 4 _, x_ 5 _, x_ 6] = [3 _._ 74 _,_ 9 _._ 35 _,_ 16 _._ 82 _,_ 18 _._ 69 _,_ 23 _._ 36 _,_ 28 _._ 04] % _._ 

_Using the binary partition of Table 4.1 and Eq. (4.9), compute its 5 balances. Compare with what you obtained in the preceding exercise._ 

Exercise 4.8.4 _Consider the log-ratios c_ 1 = ln _x_ 1 _/x_ 3 _and c_ 2 = ln _x_ 2 _/x_ 3 _in a simplex S_[3] _. They are coordinates when using the_ alr _transformation. Find two unitary vectors_ **e** 1 _and_ **e** 2 _such that ⟨_ **x** _,_ **e** _i⟩a_ = _ci, i_ = 1 _,_ 2 _. Compute the inner product ⟨_ **e** 1 _,_ **e** 2 _⟩a and determine the angle between them. Does the result change if the considered simplex is S_[7] _?_ 

Exercise 4.8.5 _When computing the_ clr _of a composition_ **x** _∈S[D] , a_ clr _coefficient is ξi_ = ln( _xi/g_ ( **x** )) _. This can be consider as a balance between two groups of parts, which are they and which is the corresponding balancing element?_ 

Exercise 4.8.6 _Six parties have contested elections. In five districts they have obtained the votes in Table 4.3. Parties are divided into left (L) and right (R) wings. Is there some relationship between the L-R balance and the relative votes of R1-R2? Select an adequate sequential binary partition to analyse this question and obtain the corresponding balance coordinates. Find the correlation matrix of the balances and give an interpretation to the maximum correlated two balances. Compute the distances between the five districts; which are the two districts with the maximum and minimum inter-distance. Are you able to distinguish some cluster of districts?_ 

Table 4.3: Votes obtained by six parties in five districts. 

||L1|L2|R1|R2|L3|L4|
|---|---|---|---|---|---|---|
|d1|10|223|534|23|154|161|
|d2|43|154|338|43|120|123|
|d3|3|78|29|702|265|110|
|d4|5|107|58|598|123|92|
|d5|17|91|112|487|80|90|



Exercise 4.8.7 _Consider the data set given in Table 2.1. Check the data for zeros. Apply the_ alr _transformation to compositions with no zeros. Plot the transformed data in_ R[2] _._ 

Exercise 4.8.8 _Consider the data set given in table 2.1 and take the components in a different order. Apply the_ alr _transformation to compositions with no zeros. Plot the transformed data in_ R[2] _. Compare the result with those obtained in Exercise 4.8.7._ 

_CHAPTER 4. COORDINATE REPRESENTATION_ 

36 

Exercise 4.8.9 _Consider the data set given in table 2.1. Apply the_ ilr _transformation to compositions with no zeros. Plot the transformed data in_ R[2] _. Compare the result with the scatterplots obtained in exercises 4.8.7 and 4.8.8 using the_ alr _transformation._ 

Exercise 4.8.10 _Compute the_ alr _and_ ilr _coordinates, as well as the_ clr _coefficients of the 6-part composition_ 

**==> picture [271 x 11] intentionally omitted <==**

Exercise 4.8.11 _Consider the 6-part composition of the preceding exercise. Using the binary partition of Table 4.1 and Equation (4.9), compute its 5 balances. Compare with the results of the preceding exercise._ 

## **Chapter 5** 

## **Exploratory data analysis** 

## **5.1 General remarks** 

In this chapter we are going to address the first steps that should be performed whenever the study of a compositional data set **X** is initiated. Essentially, these steps are five. They consist in (1) computing descriptive statistics, i.e. the centre and variation matrix of a data set, as well as its total variability; (2) centring the data set for a better visualisation of subcompositions in ternary diagrams; (3) looking at the biplot of the data set to discover patterns; (4) defining an appropriate representation in orthonormal coordinates and computing the corresponding coordinates; and (5) compute the summary statistics of the coordinates and represent the results in a balance-dendrogram. In general, the last two steps will be based on a particular sequential binary partition, defined either a priori or as a result of the insights provided by the preceding three steps. The last step consist of a graphical representation of the sequential binary partition, including a graphical and numerical summary of descriptive statistics of the associated coordinates. 

Before starting, let us make some general considerations. The first thing in standard statistical analysis is to check the data set for errors, and we assume this part has been already done using standard procedures (e.g. using the minimum and maximum of each component to check whether the values are within an acceptable range). Another, quite different thing is to check the data set for outliers, a point that is outside the scope of this short-course. See Barcel´o et al. (1994, 1996) for details. Recall that outliers can be considered as such only with respect to a given distribution. Furthermore, we assume there are no zeros in our samples. Zeros require specific techniques (Aitchison and Kay, 2003; Bacon-Shone, 2003; Fry et al., 1996; Mart´ın-Fern´andez, 2001; Mart´ınFern´andez et al., 2000; Mart´ın-Fern´andez et al., 2003) and will be addressed in future editions of this short course. 

37 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

38 

## **5.2 Centre, total variance and variation matrix** 

Standard descriptive statistics are not very informative in the case of compositional data. In particular, the arithmetic mean and the variance or standard deviation of individual components do not fit with the Aitchison geometry as measures of central tendency and dispersion. The skeptic reader might convince himself/herself by doing exercise 5.8.1 immediately. These statistics were defined as such in the framework of Euclidean geometry in real space, which is not a sensible geometry for compositional data. Therefore, it is necessary to introduce alternatives, which we find in the concepts of _centre_ (Aitchison, 1997), _variation matrix_ , and _total variance_ (Aitchison, 1986). 

Definition 5.2.1 _A measure of central tendency for compositional data is the closed geometric mean. For a data set of size n it is called_ centre _and is defined as_ 

**==> picture [97 x 11] intentionally omitted <==**

_with gi_ = ([�] _[n] j_ =1 _[x][ij]_[)][1] _[/n][,][i]_[ = 1] _[,]_[ 2] _[, . . . , D][.]_ 

Note that in the definition of centre of a data set the geometric mean is considered column-wise (i.e. by parts), while in the clr transformation, given in equation (4.3), the geometric mean is considered row-wise (i.e. by samples). 

Definition 5.2.2 _Dispersion in a compositional data set can be described either by the_ variation matrix _, originally defined by Aitchison (1986) as_ 

**==> picture [252 x 139] intentionally omitted <==**

_or by the_ normalised variation matrix 

_As can be seen, tij stands for the usual experimental variance of the log-ratio of parts i and j, while t[∗] ij[stands][for][the][usual][experimental][variance][of][the] normalised log-ratio of parts i and j, so that the log ratio is a balance._ 

Note that 

**==> picture [131 x 26] intentionally omitted <==**

and thus **T** _[∗]_ = 12 **[T]**[.] Normalised variations have squared Aitchison distance units (see Figure 3.3). 

_5.3. CENTRING AND SCALING_ 

39 

Definition 5.2.3 _A measure of global dispersion is the_ total variance _given by_ 

**==> picture [303 x 31] intentionally omitted <==**

By definition, **T** and **T** _[∗]_ are symmetric and their diagonal will contain only zeros. Furthermore, neither the total variance nor any single entry in both variation matrices depend on the constant _κ_ associated with the sample space _S[D]_ , as constants cancel out when taking ratios. Consequently, rescaling has no effect. These statistics have further connections. From their definition, it is clear that the total variation summarises the variation matrix in a single quantity, both in the normalised and non-normalised version, and it is possible (and natural) to define it because all parts in a composition share a common scale (it is by no means so straightforward to define a total variation for a pressure-temperature random vector, for instance). Conversely, the variation matrix, again in both versions, explains how the total variation is split among the parts (or better, among all log-ratios). 

## **5.3 Centring and scaling** 

A usual way in geology to visualise data in a ternary diagram is to rescale the observations in such a way that their range is approximately the same. This is nothing else but applying a perturbation to the data set, a perturbation which is usually chosen by trial and error. To overcome this somehow arbitrary approach, note that, as mentioned in Proposition 3.2.1, for a composition **x** and its inverse **x** _[−]_[1] it holds that **x** _⊕_ **x** _[−]_[1] = **n** , the neutral element. This means that perturbation allows to move any composition to the barycentre of the simplex, in the same way that translation moves real data in real space to the origin. This property, together with the definition of centre, allows to design a strategy to better visualise the structure of the sample. In fact, computing the centre **g** of the data set, as in Definition 5.2.1, and perturbing each sample composition by the inverse **g** _[−]_[1] , the centre of a data set is shifted to the barycentre of the simplex, and the sample will gravitate around the barycentre. 

This property was first introduced by Mart´ın-Fern´andez et al. (1999) and used by Buccianti et al. (1999). An extensive discussion can be found in von Eynatten et al. (2002), where it is shown that a perturbation transforms straight lines into straight lines. This allows the inclusion of gridlines and compositional fields in the graphical representation without the risk of a nonlinear distortion. See Figure 5.1 for an example of a data set before and after perturbation with the inverse of the closed geometric mean and the effect on the gridlines. 

In the same way in real space a centred variable can be scaled to unit variance dividing it by the standard deviation, a (centred) compositional data set **X** can be scaled by powering it with totvar[ **X** ] _[−]_[1] _[/]_[2] . In this way, a data set with unit total variance is obtained, but with the same relative contribution of each logratio in the variation array. This is a significant difference with conventional 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

40 

Figure 5.1: Simulated data set before (left) and after (right) centring. 

standardisation: with real vectors, the relative contributions are an artifact of the units of each variable, and most usually should be ignored; in contrast, in compositional vectors, all parts share the same “units”, and their relative contribution to the total variation is a rich information. 

## **5.4 The biplot: a graphical display** 

Gabriel (1971) introduced the biplot to represent simultaneously the rows and columns of any matrix by means of a rank-2 approximation. Aitchison (1997) adapted it for compositional data and proved it to be a useful exploratory and expository tool. Here we briefly describe first the philosophy and mathematics of this technique, and then its interpretation in depth. 

## **5.4.1 Construction of a biplot** 

Consider the data matrix **X** with _n_ rows and _D_ columns. Thus, _D_ measurements have been obtained from each one of _n_ samples. Centre the data set as described in Section 5.3, and find the coefficients **Z** in clr coordinates (Eq. 4.3). Note that **Z** is of the same order as **X** , i.e. it has _n_ rows and _D_ columns and recall that clr coordinates preserve distances. Thus, standard results can be applied to **Z** , and in particular the fact that the best rank-2 approximation **Y** to **Z** , in the least squares sense, is provided by the singular value decomposition of **Z** (Krzanowski, 1988, p. 126-128). 

The singular value decomposition of a matrix **Z** is obtained from the matrix of eigenvectors **U** of **ZZ** _[′]_ , the matrix of eigenvectors **V** of **Z** _[′]_ **Z** and the square roots of the _s_ , _s ≤_ min _{_ ( _D −_ 1) _, n}_ positive eigenvalues _λ_ 1 _, λ_ 2 _, . . . , λs_ of either **ZZ** _[′]_ or **Z** _[′]_ **Z** , which are equal up to additional null eigenvalues. As a result, taking _ki_ = _λ_[1] _i[/]_[2] , we can write 

**==> picture [241 x 55] intentionally omitted <==**

_5.4. THE BIPLOT: A GRAPHICAL DISPLAY_ 

41 

where _s_ is the rank of **Z** and the singular values _k_ 1 _, k_ 2 _, . . . , ks_ are in descending order of magnitude. The matrix **U** has dimensions ( _n, s_ ) and **V** is a ( _D, s_ )- matrix. Both matrices **U** and **V** are orthonormal, i.e. **UU** _[′]_ = _Is_ , **VV** _[′]_ = _Is_ . When **Z** is made of centered clr’s of compositional data, its rows add to zero and consequently its rank is _s ≤ D −_ 1 being the common case _s_ = _D −_ 1. The interpretation of SVD (5.1) is straightforward. Each row of matrix **V** _[′]_ is the clr of an element of an orthonormal basis of the simplex. This kind of matrices have been denoted Ψ in chapter 4, section 4.4. The matrix product **U** diag( _k_ 1 _, k_ 2 _, · · · , ks_ ) is an ( _n, s_ )-matrix whose _n_ rows contain the coordinates of each compositional data point with respect to the orthonormal basis described by **V** _[′]_ . Therefore, **U** diag( _k_ 1 _, k_ 2 _, · · · , ks_ ) contains ilr-coordinates of the (centered)-compositional data set. Note that these ilr-coordinates are not balances but general orthonormal coordinates. Singular values _λ_ 1 = _k_ 1[2][,] _[λ]_[2][=] _[k]_ 2[2][,] . . . , _λs_ = _ks_[2][,][are][proportional][to][the][sample][variance][of][the][coordinates.] 

In order to reduce the dimension of the compositional data set, we can suppress some orthogonal coordinates, typically those with associated low variance. This can be thought as a deletion of small square-singular values. Assume that we retain singular values _k_ 1, _k_ 2, . . . , _kt_ , ( _t ≤ s_ ). Then the proportion of retained variance is 

**==> picture [181 x 25] intentionally omitted <==**

The biplot is normally drawn in two dimensions, or at most three dimensions, and then we normally take _t_ = 2, provided that the proportion of explained variance is high. This rank-2 approximation is then obtained by simply substituting all singular values with index larger then 2 by zero. As a result we get a rank-2 approximation of **Z** 

**==> picture [290 x 55] intentionally omitted <==**

The proportion of variability retained by this approximation is ( _λ_ 1+ _λ_ 2) _/_ ([�] _[s] i_ =1 _[λ][i]_[)] _[ .]_ 

To obtain a biplot, it is first necessary to write **Y** as the product of two matrices **GH** _[′]_ , where **G** is an ( _n,_ 2) matrix and **H** is an ( _D,_ 2) matrix. There are different possibilities to obtain such a factorisation, one of which is 

**==> picture [244 x 117] intentionally omitted <==**

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

42 

The biplot consists simply in representing the vectors **g** _i_ , _i_ = 1 _,_ 2 _, ..., n_ (row vectors of two components), and **h** _j_ , _j_ = 1 _,_ 2 _, ..., D_ (column vectors of two components), on a plane. The vectors **g** 1, **g** 2, ..., **g** _n_ are termed the row markers of **Y** and correspond to the projections of the _n_ samples on the plane defined by the first two eigenvectors of **ZZ** _[′]_ . The vectors **h** 1, **h** 2, ..., **h** _D_ are the column markers, which correspond to the projections of the _D_ clr-parts on the plane defined by the first two eigenvectors of **Z** _[′]_ **Z** . Both planes can be superposed for a visualisation of the relationship between samples and parts. 

## **5.4.2 Interpretation of a compositional biplot** 

The biplot graphically displays the rank-2 approximation **Y** to **Z** given by the singular value decomposition. A biplot of compositional data consists of 

1. an _origin O_ which represents the centre of the compositional data set, 

2. a _vertex_ at position **h** _j_ for each of the _D_ parts, and 

3. a _case marker_ at position **g** _i_ for each of the _n_ samples or cases. 

We term the join of _O_ to a vertex **h** _j_ the _ray O_ **h** _j_ and the join of two vertices **h** _j_ and **h** _k_ the _link_ **h** _j_ **h** _k_ . These features constitute the basic characteristics of a biplot with the following main properties for the interpretation of compositional variability. 

1. Links and rays provide information on the relative variability in a compositional data set, as 

**==> picture [250 x 25] intentionally omitted <==**

Nevertheless, one has to be careful in interpreting rays, which cannot be identified neither with var( _xj_ ) nor with var(ln _xj_ ), as they depend on the full composition through g( _x_ ) and vary when a subcomposition is considered. 

2. Links provide information on the correlation of subcompositions: if links **h** _j_ **h** _k_ and **h** _i_ **h** _ℓ_ intersect at _M_ then 

**==> picture [154 x 25] intentionally omitted <==**

Furthermore, if the two links are at right angles, then cos( **h** _jM_ **h** _i_ ) _≈_ 0, and zero correlation of the two log-ratios can be expected. This is useful in investigation of subcompositions for possible independence. 

3. Subcompositional analysis: The centre _O_ is the centroid (centre of gravity) of the _D_ vertices **h** 1 _,_ **h** 2 _, . . . ,_ **h** _D_ ; ratios are preserved under formation of subcompositions; it follows that the biplot for any subcomposition is 

_5.5. EXPLORATORY ANALYSIS OF COORDINATES_ 

43 

simply formed by selecting the vertices corresponding to the parts of the subcomposition and taking the centre of the subcompositional biplot as the centroid of these vertices. 

4. Coincident vertices: If vertices **h** _j_ and **h** _k_ coincide, or nearly so, this means that var(ln( _xj/xk_ )) is zero, or nearly so, and the ratio _xj/xk_ is constant, or nearly so. Then, the two involved parts, _xj_ and _xk_ can be assumed to be redundant. If the proportion of variance captured by the biplot is not very high, two coincident vertices suggest that ln( _xj/xk_ ) is orthogonal to the plane of the biplot, and this might be an indication of the possible independence of that log-ratio and the two first principal directions of the singular value decomposition. 

5. Collinear vertices: If a subset of vertices is collinear, it might indicate that the associated subcomposition has a biplot that is one-dimensional, which might mean that the subcomposition has one-dimensional variability, i.e. compositions plot along a compositional line. 

From the above aspects of interpretation, it should be clear that links are fundamental elements of a compositional biplot. The lengths of links are (approximately) proportional to variance of simple log-ratios between single elements, as they appear in the variation matrix. The complete constellation of links informs about the compositional covariance structure of simple log-ratios and provides hints about subcompositional variability and independence. Interpretation of the biplot is concerned with its internal geometry and is unaffected by any rotation or mirror-imaging of the diagram. For an illustration, see Section 5.6. 

For some applications of biplots to compositional data in a variety of geological contexts see Aitchison (1990), and for a deeper insight into biplots of compositional data, with applications in other disciplines and extensions to conditional biplots, see Aitchison and Greenacre (2002). 

## **5.5 Exploratory analysis of coordinates** 

Either as a result of the preceding descriptive analysis, or due to a priori knowledge of the problem at hand, we may consider a given sequential binary partition as particularly interesting. In this case, its associated orthonormal coordinates, being a vector of real variables, can be treated with the existing battery of conventional descriptive analysis. If **X** _[∗]_ = _h_ ( **X** ) represents the coordinates of the data set—rows contain the coordinates of an individual observation—then its experimental moments satisfy 

**==> picture [165 x 27] intentionally omitted <==**

with **Ψ** the matrix whose rows contain the clr coefficients of the orthonormal basis chosen (see Section 4.4 for its construction); **g** the centre of the dataset as 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

44 

defined in Definition 5.2.1, and **T** _[∗]_ the normalised variation matrix as introduced in Definition 5.2.2. 

There is a graphical representation, with the specific aim of representing a system of coordinates based on a sequential binary partition: the CoDa- or balance-dendrogram (Egozcue and Pawlowsky-Glahn, 2006; Pawlowsky-Glahn and Egozcue, 2006). A balance-dendrogram is the joint representation of the following elements: 

1. a sequential binary partition, in the form of a tree structure; 

2. the sample mean and variance of each balance; 

3. a box-plot, summarising the order statistics of each balance. 

Each coordinate is represented in a horizontal axis, which limits correspond to a certain range (the same for every coordinate). The vertical bar going up from each one of these coordinate axes represents the variance of that specific coordinate, and the contact point is the coordinate mean. Figure 5.2 shows these elements in an illustrative example. 

Given that the range of each coordinate is symmetric (in Figure 5.2 it goes from _−_ 3 to +3), the box plots closer to one part (or group) indicate that part (or group) is more abundant. Thus, in Figure 5.2, SiO2 is slightly more abundant than Al2O3, there is more FeO than Fe2O3, and much more structural oxides (SiO2 and Al2O3) than the rest. Another feature easily read from a balance-dendrogram is symmetry: it can be assessed both by comparison between the several quantile boxes, and looking at the difference between the median (marked as “Q2” in Figure 5.2 right) and the mean. 

## **5.6 Illustration** 

We are going to use, both for illustration and for the exercises, the data set **X** given in table 5.1. They correspond to 17 samples of chemical analysis of rocks from Kilauea Iki lava lake, Hawaii, published by Richter and Moore (1966) and cited by Rollinson (1995). 

Originally, 14 parts had been registered, but H2O[+] and H2O _[−]_ have been omitted because of the large amount of zeros. CO2 has been kept in the table, to call attention upon parts with some zeros, but has been omitted from the study precisely because of the zeros. This is the strategy to follow if the part is not essential in the characterisation of the phenomenon under study. If the part is essential and the proportion of zeros is high, then we are dealing with two populations, one characterised by zeros in that component and the other by non-zero values. If the part is essential and the proportion of zeros is small, then we can look for input techniques, as explained in the beginning of this chapter. 

The centre of this data set is 

**g** = (48 _._ 57 _,_ 2 _._ 35 _,_ 11 _._ 23 _,_ 1 _._ 84 _,_ 9 _._ 91 _,_ 0 _._ 18 _,_ 13 _._ 74 _,_ 9 _._ 65 _,_ 1 _._ 82 _,_ 0 _._ 48 _,_ 0 _._ 22) _,_ 

_5.6. ILLUSTRATION_ 

45 

**==> picture [333 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
line length = coordinate variance<br>coordinate mean<br>range lower limit range upper limit<br>FeO * Fe2O3 TiO2<br>0.060<br>0.08<br>0.055<br>0.06<br>0.050<br>0.04<br>0.045<br>0.02<br>0.00 0.040<br>FeO Fe2O3 TiO2 Al2O3 SiO2 sample min Q1 Q2 Q3sample max<br>**----- End of picture text -----**<br>


Figure 5.2: Illustration of elements included in a balance-dendrogram. The left subfigure represents a full dendrogram, and the right figure is a zoomed part, corresponding to the balance of (FeO,Fe2O3) against TiO2. 

the total variance is totvar[ **X** ] = 0 _._ 3275 and the normalised variation matrix **T** _[∗]_ is given in Table 5.2. 

The biplot (Fig. 5.3), shows an essentially two dimensional pattern of variability, two sets of parts that cluster together, A = [TiO2, Al2O3, CaO, Na2O, P2O5] and B = [SiO2, FeO, MnO], and a set of one dimensional relationships between parts. 

The two dimensional pattern of variability is supported by the fact that the first two axes of the biplot reproduce about 90% of the total variance, as captured in the scree plot in Fig. 5.3, left. The orthogonality of the link between Fe2O3 and FeO (i.e., the oxidation state) with the link between MgO and any of the parts in set A might help in finding an explanation for this behaviour and in decomposing the global pattern into two independent processes. 

Concerning the two sets of parts we can observe short links between them and, at the same time, that the variances of the corresponding log-ratios (see the normalised variation matrix **T** _[∗]_ , Table 5.2) are very close to zero. Consequently, we can say that they are essentially redundant, and that some of them could be either grouped to a single part or simply omitted. In both cases the dimensionality of the problem would be reduced. 

Another aspect to be considered is the diverse patterns of one-dimensional variability that can be observed. Examples that can be visualised in a ternary diagram are Fe2O3, K2O and any of the parts in set A, or MgO with any of 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

46 

Table 5.1: Chemical analysis of rocks from Kilauea Iki lava lake, Hawaii 

|SiO2|TiO2|Al2O3|Fe2O3|FeO|MnO|MgO|CaO|Na2O|K2O|P2O5|CO2|
|---|---|---|---|---|---|---|---|---|---|---|---|
|48.29|2.33|11.48|1.59|10.03|0.18|13.58|9.85|1.90|0.44|0.23|0.01|
|48.83|2.47|12.38|2.15|9.41|0.17|11.08|10.64|2.02|0.47|0.24|0.00|
|45.61|1.70|8.33|2.12|10.02|0.17|23.06|6.98|1.33|0.32|0.16|0.00|
|45.50|1.54|8.17|1.60|10.44|0.17|23.87|6.79|1.28|0.31|0.15|0.00|
|49.27|3.30|12.10|1.77|9.89|0.17|10.46|9.65|2.25|0.65|0.30|0.00|
|46.53|1.99|9.49|2.16|9.79|0.18|19.28|8.18|1.54|0.38|0.18|0.11|
|48.12|2.34|11.43|2.26|9.46|0.18|13.65|9.87|1.89|0.46|0.22|0.04|
|47.93|2.32|11.18|2.46|9.36|0.18|14.33|9.64|1.86|0.45|0.21|0.02|
|46.96|2.01|9.90|2.13|9.72|0.18|18.31|8.58|1.58|0.37|0.19|0.00|
|49.16|2.73|12.54|1.83|10.02|0.18|10.05|10.55|2.09|0.56|0.26|0.00|
|48.41|2.47|11.80|2.81|8.91|0.18|12.52|10.18|1.93|0.48|0.23|0.00|
|47.90|2.24|11.17|2.41|9.36|0.18|14.64|9.58|1.82|0.41|0.21|0.01|
|48.45|2.35|11.64|1.04|10.37|0.18|13.23|10.13|1.89|0.45|0.23|0.00|
|48.98|2.48|12.05|1.39|10.17|0.18|11.18|10.83|1.73|0.80|0.24|0.01|
|48.74|2.44|11.60|1.38|10.18|0.18|12.35|10.45|1.67|0.79|0.23|0.01|
|49.61|3.03|12.91|1.60|9.68|0.17|8.84|10.96|2.24|0.55|0.27|0.01|
|49.20|2.50|12.32|1.26|10.13|0.18|10.51|11.05|2.02|0.48|0.23|0.01|



the parts in set A and any of the parts in set B. Let us select one of those subcompositions, e.g. Fe2O3, K2O and Na2O. After closure, the samples plot in a ternary diagram as shown in Figure 5.4 and we recognise the expected trend and two outliers corresponding to samples 14 and 15, which require further explanation. Regarding the trend itself, notice that it is in fact a line of isoproportion Na2O/K2O: thus we can conclude that the ratio of these two parts is independent of the amount of Fe2O3. 

As a last step, we compute the conventional descriptive statistics of the orthonormal coordinates in a specific reference system (either a priori chosen or derived from the previous steps). In this case, due to our knowledge of the typical geochemistry and mineralogy of basaltic rocks, we choose a priori the set of balances of Table 5.3, where the resulting balance will be interpreted as 

1. an oxidation state proxy (Fe[3+] against Fe[2+] ); 

2. silica saturation proxy (when Si is lacking, Al takes its place); 

3. distribution within heavy minerals (rutile or apatite?); 

4. importance of heavy minerals relative to silicates; 

5. distribution within plagioclase (albite or anortite?); 

6. distribution within feldspar (K-feldspar or plagioclase?); 

7. distribution within mafic non-ferric minerals; 

8. distribution within mafic minerals (ferric vs. non-ferric); 

_5.6. ILLUSTRATION_ 

47 

Table 5.2: Normalised variation matrix of data given in table 5.1. For simplicity, only the upper triangle is represented, omitting the first column and last row. 

|var( 1<br>~~_√_~~<br>2 ln _xi_<br>_xj_ )|TiO2<br>Al2O3<br>Fe2O3<br>FeO<br>MnO<br>MgO<br>CaO<br>Na2O<br>K2O<br>P2O5|
|---|---|
|SiO2<br>TiO2<br>Al2O3<br>Fe2O3<br>FeO<br>MnO<br>MgO<br>CaO<br>Na2O<br>K2O|0.012<br>0.006<br>0.036<br>0.001<br>0.001<br>0.046<br>0.007<br>0.009<br>0.029<br>0.011<br>0.003<br>0.058<br>0.019<br>0.016<br>0.103<br>0.005<br>0.002<br>0.015<br>0.000<br>0.050<br>0.011<br>0.008<br>0.084<br>0.000<br>0.002<br>0.017<br>0.002<br>0.044<br>0.035<br>0.053<br>0.054<br>0.050<br>0.093<br>0.059<br>0.001<br>0.038<br>0.012<br>0.015<br>0.034<br>0.017<br>0.040<br>0.009<br>0.012<br>0.033<br>0.015<br>0.086<br>0.092<br>0.130<br>0.100<br>0.003<br>0.016<br>0.004<br>0.024<br>0.002<br>0.014|



Table 5.3: A possible sequential binary partition for the data set of table 5.1. 

|balance|SiO2<br>TiO2<br>Al2O3<br>Fe2O3<br>FeO<br>MnO<br>MgO<br>CaO<br>Na2O<br>K2O<br>P2O5|
|---|---|
|v1<br>v2<br>v3<br>v4<br>v5<br>v6<br>v7<br>v8<br>v9<br>v10|0<br>0<br>0<br>+1<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>0<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>-1<br>+1<br>-1<br>+1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>+1<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>+1<br>-1<br>-1<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>+1<br>+1<br>+1<br>+1<br>-1<br>-1<br>-1<br>0<br>+1<br>+1<br>+1<br>-1<br>-1<br>-1<br>-1<br>-1<br>-1<br>-1<br>+1|



9. importance of mafic minerals against feldspar; 

10. importance of cation oxides (those filling the crystalline structure of minerals) against frame oxides (those forming that structure, mainly Al and Si). 

One should be aware that such an interpretation is totally problem-driven: if we were working with sedimentary rocks, it would have no sense to split MgO and CaO (as they would mainly occur in limestones and associated lithologies), or to group Na2O with CaO (as they would probably come from different rock types, e.g. siliciclastic against carbonate). 

Using the sequential binary partition given in Table 5.3, Figure 5.5 represents the balance-dendrogram of the sample, within the range ( _−_ 3 _,_ +3). This range translates for two part compositions to proportions of (1 _._ 4 _,_ 98 _._ 6)%; i.e. if we look at the balance MgO-MnO the variance bar is placed at the lower extreme of the balance axis, which implies that in this subcomposition MgO represents in average more than 98%, and MnO less than 2%. Looking at the lengths of the 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

48 

**==> picture [292 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.0 −0.5 0.0 0.5 1.0<br>11<br>2 8 12 Fe2O3<br>7<br>16 5 10<br>TiO2P2O5Na2OAl2O3CaO 9 6<br>SiO2MnO<br>K2O 1 FeO 3<br>MgO<br>17<br>14<br>15<br>4<br>13<br>−0.4 −0.2 0.0 0.2 0.4<br>Comp.1<br>0.20<br> 71 % 0.4<br>1.0<br>0.15 0.2<br>0.5<br>Variances 0.10 Comp.2 0.0 0.0<br> 90 % −0.2 −0.5<br>0.05<br> 98 % −1.0<br>100 % −0.4<br>0.00<br>**----- End of picture text -----**<br>


Figure 5.3: Biplot of data of Table 5.1 (right), and scree plot of the variances of all principal components (left), with indication of cumulative explained variance. 

Figure 5.4: Plot of subcomposition (Fe2O3,K2O,Na2O). Left: before centring. Right: after centring. 

several variance bars, one easily finds that the balances P2O5-TiO2 and SiO2Al2O3 are almost constant, as their bars are very short and their box-plots extremely narrow. Again, the balance between the subcompositions (P2O5, TiO2) vs. (SiO2, Al2O3) does not display any box-plot, meaning that it is above +3 (thus, the second group of parts represents more than 98% with respect to the first group). The distribution between K2O, Na2O and CaO tells us that Na2O and CaO keep a quite constant ratio (thus, we should interpret that there are no strong variations in the plagioclase composition), and the ratio of these two against K2O is also fairly constant, with the exception of some values below the first quartile (probably, a single value with an particularly high K2O content). The other balances are well equilibrated (in particular, see how centred is the proxy balance between feldspar and mafic minerals), all with moderate dispersions. 

**==> picture [345 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
5.6. ILLUSTRATION 49<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br>K2O Na2O CaO MgO MnO FeO Fe2O3 P2O5 TiO2 Al2O3 SiO2<br>**----- End of picture text -----**<br>


Figure 5.5: Balance-dendrogram of data from Table 5.1 using the balances of Table 5.3. 

Table 5.4: Covariance (lower triangle) and correlation (upper triangle) matrices of balances 

|v1|v2|v3|v4|v5|v6|v7|v8|v9|v10|
|---|---|---|---|---|---|---|---|---|---|
|v1<br>0.047<br>v2<br>0.002<br>v3<br>0.002<br>v4<br>0.003<br>v5<br>-0.004<br>v6<br>0.013<br>v7<br>-0.009<br>v8<br>0.018<br>v9<br>0.032<br>v10<br>-0.015|0.120|0.341<br>-0.125|0.111<br>0.788<br>-0.345|-0.283<br>0.077<br>-0.380<br>0.461|0.358<br>0.234<br>0.018<br>0.365<br>-0.450|-0.212<br>-0.979<br>0.181<br>-0.832<br>-0.087<br>-0.328|0.557<br>-0.695<br>0.423<br>-0.663<br>-0.385<br>-0.029<br>0.668|0.423<br>0.920<br>-0.091<br>0.821<br>-0.029<br>0.505<br>-0.961<br>-0.483|-0.387<br>-0.899<br>0.141<br>-0.882<br>-0.275<br>-0.243<br>0.936<br>0.516<br>-0.936|
||0.006<br>-0.000<br>0.007<br>0.000<br>0.003<br>-0.016<br>-0.008<br>0.025<br>-0.013|||||||||
|||0.000<br>-0.001<br>-0.000<br>0.000<br>0.001<br>0.001<br>-0.001<br>0.001||||||||
||||0.012<br>0.003<br>0.007<br>-0.019<br>-0.011<br>0.031<br>-0.017|||||||
|||||0.003<br>-0.004<br>-0.001<br>-0.003<br>-0.001<br>-0.003||||||
||||||0.027<br>-0.011<br>-0.001<br>0.029<br>-0.007|||||
|||||||0.042<br>0.021<br>-0.069<br>0.035||||
||||||||0.023<br>-0.026<br>0.014|||
|||||||||0.123<br>-0.059||
||||||||||0.032|



Once the marginal empirical distribution of the balances has been analysed, the biplot can be used to explore their relations (Figure 5.6), and the conventional covariance or correlation matrices (Table 5.4). From these, we can see, for instance: 

- The constant behaviour of v3 (balance TiO2-P2O5), with a variance below 10 _[−]_[4] , and in a lesser degree, of v5 (anortite-albite relation, or balance CaO-Na2O). 

- The orthogonality of the pairs of rays v1-v2, v1-v4, v1-v7, and v6-v8, suggests the lack of correlation of their respective balances, confirmed by Table 5.4, where correlations of less than _±_ 0 _._ 3 are reported. In particular, the pair v6-v8 has a correlation of _−_ 0 _._ 029. These facts would imply that silica saturation (v2), the presence of heavy minerals (v4) and the MnO- 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

50 

**==> picture [292 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
−1.5 −1.0 −0.5 0.0 0.5 1.0<br>11<br>12v1 8 2<br>7<br>v8<br>10 5 16<br>v6 v7<br>v9 6 9 v3 v10<br>v4v2 v5<br>3 1<br>17<br>14<br>15<br>4<br>13<br>−0.4 −0.2 0.0 0.2 0.4<br>Comp.1<br>0.20  71 % 0.4<br>1.0<br>0.15 0.2 0.5<br>Variances 0.10 Comp.2 0.0 0.0<br>−0.5<br> 90 % −0.2<br>0.05<br>−1.0<br> 98 %<br>100 % −0.4<br>0.00 −1.5<br>**----- End of picture text -----**<br>


Figure 5.6: Biplot of data of table 5.1 expressed in the balance coordinate system of Table 5.3 (right), and scree plot of the variances of all principal components (left), with indication of cumulative explained variance. Compare with Figure 5.3, in particular: the scree plot, the configuration of data points, and the links between the variables related to balances v1, v2, v3, v5 and v7. 

MgO balance (v7) are uncorrelated with the oxidation state (v1); and that the type of feldspars (v6) is unrelated to the type of mafic minerals (v8). 

- The balances v9 and v10 are opposite, and their correlation is _−_ 0 _._ 936, implying that the ratio mafic oxides/feldspar oxides is high when the ratio Silica-Alumina/cation oxides is low, i.e. mafics are poorer in Silica and Alumina. 

A final comment regarding balance descriptive statistics: since the balances are chosen due to their interpretability, we are no more just “describing” patterns here. Balance statistics represent a step further towards modeling: all our conclusions in these last three points heavily depend on the preliminary interpretation (=“model”) of the computed balances. 

## **5.7 Linear trend using principal components** 

Singular value decomposition (SVD) applied to centered clr-data has been presented in section 5.4 as a technique for dimension reduction of compositional data. In a statistical framework, this technique is known as principal component analysis (PC). As a result the compositional biplot has been shown to be a powerful exploratory tool. Additionally, PC-SVD can be used as the appropriate modeling tool whenever the presence of a trend in the compositional data 

_5.7. LINEAR TREND USING PRINCIPAL COMPONENTS_ 

51 

set is suspected, but no external variable has been measured on which it might depend (Otero et al., 2003; Tolosana-Delgado et al., 2005). To illustrate this fact let us consider the most simple case, in which one PC (i.e. one squaresingular value) explains a large proportion of the total variance, e.g. more then 98%, like the one in Figure 5.7, where the subcomposition [Fe2O3,K2O,Na2O] from Table 5.1 has been used without samples 14 and 15. Consider the SVD 

Figure 5.7: Principal components in _S_[3] . Left: before centring. Right: after centring 

of the centered clr-data as in eq. (5.1). The first PC are the clr-coordinates on the unitary clr-vector **v** 1 (first column of **V** ). The composition **a1** = clr _[−]_[1] ( **v** 1) determines the direction of the first PC in the simplex. The compositional line going through the barycentre of the simplex, _α ⊙_ **a** 1, describes the trend shown by the centred sample, and **g** _⊕α⊙_ **a** 1, with **g** the centre of the sample, describes the trend shown in the non-centred data set. The evolution of the proportion per unit volume of each part, as described by the first principal component, is shown in Figure 5.8 left. The cumulative proportion is drawn in Figure 5.8 right. 

**==> picture [316 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fe2O3 Na2O K2O Fe2O3 Fe2O3+Na2O Fe2O3+Na2O+K2O<br>1,00 1,20<br>0,80 1,00<br>0,80<br>0,60<br>0,60<br>0,40<br>0,40<br>0,20 0,20<br>0,00 0,00<br>-3 -2 -1 0 1 2 3 -3 -2 -1 0 1 2 3<br>alpha alpha<br>proporciones<br>cumulated proportions<br>**----- End of picture text -----**<br>


Figure 5.8: Evolution of proportions as described by the first principal component. Left: proportions. Right: cumulated proportions. 

To interpret a trend we can use Equation (3.1), which allows us to re-scale the direction of the first PC, assuming whatever is convenient according to the process under study, e.g. that one part is stable. A representation of the result is also possible, as can be seen in Figure 5.9. The part assumed to be stable, K2O, has a constant, unit perturbation coefficient. We see that under this assumption, within the range of variation of the observations, Na2O has only a very small increase, while Fe2O3 shows a considerable increase compared to 

52 

_CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

**==> picture [241 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fe2O3/K2O Na2O/K2O K2O/K2O<br>40<br>30<br>20<br>10<br>0<br>-3 -2 -1 0 1 2 3<br>**----- End of picture text -----**<br>


Figure 5.9: Interpretation of a principal component in _S_[2] under the assumption of stability of K2O. 

the other two parts. In other words, one possible explanation for the observed pattern of variability is that Fe2O3 varies significantly, while the other two parts remain stable. 

The graph gives additional information: the relative behaviour will be preserved under any assumption. If the assumption is that K2O increases (decreases), then Na2O will show the same behaviour as K2O, while Fe2O3 will always change from _below_ to _above_ . 

Note that, although we can represent a perturbation process described by a PC only in a ternary diagram, we can extend the representation in Figure 5.9 to as many parts as we might be interested in. 

## **5.8 Exercises** 

Exercise 5.8.1 _This exercise pretends to illustrate the problems of classical statistics if applied to compositional data. Using the data given in Table 5.1, compute the classical correlation coefficients between the following pairs of parts: (MnO vs. CaO), (FeO vs. Na_ 2 _O), (MgO vs. FeO) and (MgO vs. Fe_ 2 _O_ 3 _). Now ignore the structural oxides Al_ 2 _O_ 3 _and SiO_ 2 _from the data set, reclose the remaining variables, recompute the same correlation coefficients as above. Compare the results. Compare the correlation matrix between the feldspar-constituent parts (CaO,Na_ 2 _O,K_ 2 _O), as obtained from the original data set, and after closing this 3-part subcomposition._ 

Exercise 5.8.2 _For the data given in Table 2.1 compute and plot the centre with the samples in a ternary diagram. Compute the total variance and the variation matrix._ 

Exercise 5.8.3 _Perturb the data given in table 2.1 with the inverse of the centre. Compute the centre of the perturbed data set and plot it with the samples in_ 

_5.8. EXERCISES_ 

53 

_a ternary diagram. Compute the total variance and the variation matrix. Compare your results numerically and graphically with those obtained in exercise 5.8.2._ 

Exercise 5.8.4 _Make a biplot of the data given in Table 2.1 and give an interpretation._ 

Exercise 5.8.5 _Figure 5.3 shows the biplot of the data given in Table 5.1. How would you interpret the different patterns that can be observed?_ 

Exercise 5.8.6 _Select 3-part subcompositions that behave in a particular way in Figure 5.3 and plot them in a ternary diagram. Do they reproduce properties mentioned in the previous description?_ 

Exercise 5.8.7 _Do a scatter plot of the log-ratios_ 

**==> picture [164 x 24] intentionally omitted <==**

_identifying each point. Compare with the biplot. Compute the total variance of the subcomposition (K_ 2 _O,MgO,Fe_ 2 _O_ 3 _,FeO) and compare it with the total variance of the full data set._ 

Exercise 5.8.8 _How would you recast the data in table 5.1 from mass proportion of oxides (as they are) to molar proportions? You may need the following molar weights. Any idea of how to do that with a perturbation?_ 

|_SiO_2|_TiO_2|_Al_2_O_3|_Fe_2_O_3|_FeO_|_MnO_|
|---|---|---|---|---|---|
|_60.085_|_79.899_|_101.961_|_159.692_|_71.846_|_70.937_|
|_MgO_|_CaO_|_Na_2_O_|_K_2_O_|_P_2_O_5||
|_40.304_|_56.079_|_61.979_|_94.195_|_141.945_||



Exercise 5.8.9 _Re-do all the descriptive analysis (and the related exercises) with the Kilauea data set expressed in molar proportions. Compare the results._ 

Exercise 5.8.10 _Compute the vector of arithmetic means of the_ ilr _transformed data from table 2.1. Apply the_ ilr _[−]_[1] _backtransformation and compare it with the centre._ 

Exercise 5.8.11 _Take the parts of the compositions in table 2.1 in a different order. Compute the vector of arithmetic means of the_ ilr _transformed sample. Apply the_ ilr _[−]_[1] _backtransformation. Compare the result with the previous one._ 

Exercise 5.8.12 _Centre the data set of table 2.1. Compute the vector of arithmetic means of the_ ilr _transformed data. What do you obtain?_ 

Exercise 5.8.13 _Compute the covariance matrix of the_ ilr _transformed data set of table 2.1 before and after perturbation with the inverse of the centre. Compare both matrices._ 

54 

# _CHAPTER 5. EXPLORATORY DATA ANALYSIS_ 

## **Chapter 6** 

## **Distributions on the simplex** 

The usual way to pursue any statistical analysis after an exhaustive exploratory analysis consists in assuming and testing distributional assumptions for the random phenomena. This can be easily done for compositional data, as the linear vector space structure of the simplex allows us to express observations with respect to an orthonormal basis, a property that guarantees the proper application of standard statistical methods. The only thing that has to be done is to perform any standard analysis on orthonormal coefficients and to interpret the results in terms of coefficients of the orthonormal basis. Once obtained, the inverse can be used to get the same results in terms of the canonical basis of R _[D]_ (i.e. as compositions summing up to a constant value). The justification of this approach lies in the fact that standard mathematical statistics relies on real analysis, and real analysis is performed on the coefficients with respect to an orthonormal basis in a linear vector space, as discussed by Pawlowsky-Glahn (2003). 

There are other ways to justify this approach coming from the side of measure theory and the definition of density function as the Radon-Nikod´ym derivative of a probability measure (Eaton, 1983), but they would divert us too far from practical applications. 

Given that most multivariate techniques rely on the assumption of multivariate normality, we will concentrate on the expression of this distribution in the context of random compositions and address briefly other possibilities. 

## **6.1 The normal distribution on** _S[D]_ 

Definition 6.1.1 _Given a random vector_ **x** _which sample space is S[D] , we say that_ **x** _follows a_ normal distribution _on S[D] if, and only if, the vector of orthonormal coordinates,_ **x** _[∗]_ = _h_ ( **x** ) _, follows a multivariate normal distribution on_ R _[D][−]_[1] _._ 

55 

_CHAPTER 6. DISTRIBUTIONS ON THE SIMPLEX_ 

56 

To characterise a multivariate normal distribution we need to know its parameters, i.e. the vector of expected values _µ_ and the covariance matrix Σ. In practice, they are seldom, if ever, known, and have to be estimated from the sample. Here the maximum likelihood estimates will be used, which are the vector of arithmetic means **x** ¯ _[∗]_ for the vector of expected values, and the sample covariance matrix _S_ **x** _[∗]_ with the sample size _n_ as divisor. Remember that, in the case of compositional data, the estimates are computed using the orthonormal coordinates **x** _[∗]_ of the data and not the original measurements. 

As we have considered coordinates **x** _[∗]_ , we will obtain results in terms of coefficients of **x** _[∗]_ coordinates. To obtain them in terms of the canonical basis of R _[D]_ we have to backtransform whatever we compute by using the inverse transformation _h[−]_[1] ( **x** _[∗]_ ). In particular, we can backtransform the arithmetic mean **x** ¯ _[∗]_ , which is an adequate measure of central tendency for data which follow reasonably well a multivariate normal distribution. But _h[−]_[1] (¯ **x** _[∗]_ ) = **g** , the centre of a compositional data set introduced in Definition 5.2.1, which is an unbiased, minimum variance estimator of the expected value of a random composition (Pawlowsky-Glahn and Egozcue, 2002). Also, as stated in Aitchison (2002), **g** is an estimate of _C_ [exp(E[ln( **x** )])], which is the theoretical definition of the closed geometric mean, thus justifying its use. 

## **6.2 Other distributions** 

Many other distributions on the simplex have been defined (using on _S[D]_ the classical Lebesgue measure on R _[D]_ ), like e.g. the additive logistic skew normal, the Dirichlet and its extensions, the multivariate normal based on Box-Cox transformations, among others. Some of them have been recently analysed with respect to the linear vector space structure of the simplex (Mateu-Figueras, 2003). This structure has important implications, as the expression of the corresponding density differs from standard formulae when expressed in terms of the metric of the simplex and its associated Lebesgue measure (PawlowskyGlahn, 2003). As a result, appealing invariance properties appear: for instance, a normal density on the real line does not change its shape by translation, and thus a normal density in the simplex is also invariant under perturbation; this property is not obtained if one works with the classical Lebesgue measure on R _[D]_ . These densities and the associated properties shall be addressed in future extensions of this short course. 

## **6.3 Tests of normality on** _S[D]_ 

Testing distributional assumptions of normality on _S[D]_ is equivalent to test multivariate normality of _h_ transformed compositions. Thus, interest lies in the following test of hypothesis: 

_H_ 0 **:** the sample comes from a normal distribution on _S[D]_ , 

57 

## _6.3. TESTS OF NORMALITY ON S[D]_ 

_H_ 1 **:** the sample comes not from a normal distribution on _S[D]_ , 

which is equivalent to 

- _H_ 0 **:** the sample of _h_ coordinates comes from a multivariate normal distribution, 

- _H_ 1 **:** the sample of _h_ coordinates comes not from a multivariate normal distribution. 

Out of the large number of published tests, for **x** _[∗] ∈_ R _[D][−]_[1] , Aitchison selected the Anderson-Darling, Cramer-von Mises, and Watson forms for testing hypothesis on samples coming from a uniform distribution. We repeat them here for the sake of completeness, but only in a synthetic form. For clarity we follow the approach used by Pawlowsky-Glahn and Buccianti (2002) and present each case separately; in Aitchison (1986) an integrated approach can be found, in which the orthonormal basis selected for the analysis comes from the singular value decomposition of the data set. 

The idea behind the approach is to compute statistics which under the initial hypothesis should follow a uniform distribution in each of the following three cases: 

1. all ( _D −_ 1) marginal, univariate distributions, 

2. all[1][bivariate][angle][distributions,] 2[(] _[D][ −]_[1)(] _[D][ −]_[2)] 

3. the ( _D −_ 1)-dimensional radius distribution, 

and then use mentioned tests. 

Another approach is implemented in the R “compositions” library ( **?** ), where all pair-wise log-ratios are checked for normality, in the fashion of the variation 1 matrix. This gives 2[(] _[D][−]_[1)(] _[D][−]_[2)][tests][of][univariate][normality:][for][the] hypothesis _H_ 0 to hold, all marginal distributions must be also normal. This condition is thus necessary, but not sufficient (although it is a good indication). Here we will not explain the details of this approach: they are equivalent to marginal univariate distribution tests. 

## **6.3.1 Marginal univariate distributions** 

We are interested in the distribution of each one of the components of _h_ ( **x** ) = **x** _[∗] ∈_ R _[D][−]_[1] , called the marginal distributions. For the _i_ -th of those variables, the observations are given by _⟨_ **x** _,_ **e** _i⟩a_ , which explicit expression can be found in Equation 4.7. To perform mentioned tests, proceed as follows: 

1. Compute the maximum likelihood estimates of the expected value and the variance: 

**==> picture [184 x 29] intentionally omitted <==**

_CHAPTER 6. DISTRIBUTIONS ON THE SIMPLEX_ 

58 

Table 6.1: Critical values for marginal test statistics. 

|Signifcance level|(%)|10|5|2.5|1|
|---|---|---|---|---|---|
|Anderson-Darling|_Qa_|0.656|0.787|0.918|1.092|
|Cramer-von Mises|_Qc_|0.104|0.126|0.148|0.178|
|Watson|_Qw_|0.096|0.116|0.136|0.163|



2. Obtain from the corresponding tables or using a computer built-in function the values 

**==> picture [156 x 25] intentionally omitted <==**

where Φ( _._ ) is the _N_ (0; 1) cumulative distribution function. 

3. Rearrange the values _zr_ in ascending order of magnitude to obtain the ordered values _z_ ( _r_ ). 

4. Compute the Anderson-Darling statistic for marginal univariate distributions: 

**==> picture [308 x 31] intentionally omitted <==**

5. Compute the Cramer-von Mises statistic for marginal univariate distributions 

**==> picture [216 x 31] intentionally omitted <==**

6. Compute the Watson statistic for marginal univariate distributions 

**==> picture [186 x 33] intentionally omitted <==**

7. Compare the results with the critical values in table 6.1. The null hypothesis will be rejected whenever the test statistic lies in the critical region for a given significance level, i.e. it has a value that is larger than the value given in the table. 

The underlying idea is that if the observations are indeed normally distributed, then the _z_ ( _r_ ) should be approximately the order statistics of a uniform distribution over the interval (0 _,_ 1). The tests make such comparisons, making due allowance for the fact that the mean and the variance are estimated. Note that to follow the **?** approach, one should apply this scheme to all pair-wise log-ratios, _y_ = log( _xi/xj_ ) _,_ with _i < j_ , instead of to the _x[∗]_ coordinates of the observations. 

_6.3. TESTS OF NORMALITY ON S[D]_ 

59 

A visual representation of each test can be given in the form of a plot in the unit square of the _z_ ( _r_ ) against the associated order statistic (2 _r −_ 1) _/_ (2 _n_ ), _r_ = 1 _,_ 2 _, ..., n_ , of the uniform distribution (a PP plot). Conformity with normality on _S[D]_ corresponds to a pattern of points along the diagonal of the square. 

## **6.3.2 Bivariate angle distribution** 

The next step consists in analysing the bivariate behaviour of the ilr coordinates. For each pair of indices ( _i, j_ ), with _i < j_ , we can form a set of bivariate observations ( _x[∗] ri[, x][∗] rj_[),] _[r]_[=][1] _[,]_[ 2] _[, ..., n]_[.][The][test][approach][here][is][based][on][the] following idea: if ( _ui, uj_ ) is distributed as _N_[2] ( **0** ; **I**[2] ), called a circular normal distribution, then the radian angle between the vector from (0 _,_ 0) to ( _ui, uj_ ) and the _u_ 1-axis is distributed uniformly over the interval (0 _,_ 2 _π_ ). Since any bivariate normal distribution can be reduced to a circular normal distribution by a suitable transformation, we can apply such a transformation to the bivariate observations and ask if the hypothesis of the resulting angles following a uniform distribution can be accepted. Proceed as follows: 

1. For each pair of indices ( _i, j_ ), with _i < j_ , compute the maximum likelihood estimates 

**==> picture [333 x 99] intentionally omitted <==**

2. Compute, for _r_ = 1 _,_ 2 _, ..., n_ , 

**==> picture [237 x 48] intentionally omitted <==**

3. Compute the radian angles _θ_[ˆ] _r_ required to rotate the _ur_ -axis anticlockwise about the origin to reach the points ( _ur, vr_ ). If arctan( _t_ ) denotes the angle between _−_[1][and][1][whose][tangent][is] _[t]_[,][then] 2 _[π]_ 2 _[π]_ 

**==> picture [301 x 25] intentionally omitted <==**

4. Rearrange the values of _θ_[ˆ] _r/_ (2 _π_ ) in ascending order of magnitude to obtain the ordered values _z_ ( _r_ ). 

_CHAPTER 6. DISTRIBUTIONS ON THE SIMPLEX_ 

60 

Table 6.2: Critical values for the bivariate angle test statistics. 

|Signifcance level|(%)|10|5|2.5|1|
|---|---|---|---|---|---|
|Anderson-Darling|_Qa_|1.933|2.492|3.070|3.857|
|Cramer-von Mises|_Qc_|0.347|0.461|0.581|0.743|
|Watson|_Qw_|0.152|0.187|0.221|0.267|



5. Compute the Anderson-Darling statistic for bivariate angle distributions: 

**==> picture [232 x 28] intentionally omitted <==**

6. Compute the Cramer-von Mises statistic for bivariate angle distributions 

**==> picture [238 x 31] intentionally omitted <==**

7. Compute the Watson statistic for bivariate angle distributions 

**==> picture [353 x 37] intentionally omitted <==**

8. Compare the results with the critical values in Table 6.2. The null hypothesis will be rejected whenever the test statistic lies in the critical region for a given significance level, i.e. it has a value that is larger than the value given in the table. 

The same representation as mentioned in the previous section can be used for visual appraisal of conformity with the hypothesis tested. 

## **6.3.3 Radius test** 

To perform an overall test of multivariate normality, the radius test is going to be used. The basis for it is that, under the assumption of multivariate normality of the orthonormal coordinates, **x** _[∗] r_[,][the][radii] _[−]_[or][squared][deviations][from][the] mean _−_ are approximately distributed as _χ_[2] ( _D−_ 1); using the cumulative function of this distribution we can obtain again values that should follow a uniform distribution. The steps involved are: 

1. Compute the maximum likelihood estimates for the vector of expected values and for the covariance matrix, as described in the previous tests. 

2. Compute the radii _ur_ = ( **x** _[∗] r[−][µ]_[ˆ][)] _[′]_[ ˆΣ] _[−]_[1][(] **[x]** _[∗] r[−][µ]_[ˆ][),] _[r]_[= 1] _[,]_[ 2] _[, ..., n]_[.] 

_6.4. EXERCISES_ 

61 

Table 6.3: Critical values for the radius test statistics. 

|Signifcance level|(%)|10|5|2.5|1|
|---|---|---|---|---|---|
|Anderson-Darling|_Qa_|1.933|2.492|3.070|3.857|
|Cramer-von Mises|_Qc_|0.347|0.461|0.581|0.743|
|Watson|_Qw_|0.152|0.187|0.221|0.267|



3. Compute _zr_ = _F_ ( _ur_ ), _r_ = 1 _,_ 2 _, ..., n_ , where _F_ is the distribution function of the _χ_[2] ( _D −_ 1) distribution. 

4. Rearrange the values of _zr_ in ascending order of magnitude to obtain the ordered values _z_ ( _r_ ). 

5. Compute the Anderson-Darling statistic for radius distributions: 

**==> picture [232 x 29] intentionally omitted <==**

6. Compute the Cramer-von Mises statistic for radius distributions 

**==> picture [238 x 31] intentionally omitted <==**

7. Compute the Watson statistic for radius distributions 

**==> picture [353 x 37] intentionally omitted <==**

8. Compare the results with the critical values in table 6.3. The null hypothesis will be rejected whenever the test statistic lies in the critical region for a given significance level, i.e. it has a value that is larger than the value given in the table. 

Use the same representation described before to assess visually normality on _S[D]_ . 

## **6.4 Exercises** 

Exercise 6.4.1 _Test the hypothesis of normality of the marginals of the_ ilr _transformed sample of table 2.1._ 

Exercise 6.4.2 _Test the bivariate normality of each variable pair_ ( _x[∗] i[, x][∗] j_[)] _[,][i <] j, of the_ ilr _transformed sample of table 2.1._ 

Exercise 6.4.3 _Test the variables of the_ ilr _transformed sample of table 2.1 for joint normality._ 

62 

# _CHAPTER 6. DISTRIBUTIONS ON THE SIMPLEX_ 

## **Chapter 7** 

## **Statistical inference** 

## **7.1 Testing hypothesis about two groups** 

When a sample has been divided into two or more groups, interest may lie in finding out whether there is a real difference between those groups and, if it is the case, whether it is due to differences in the centre, in the covariance structure, or in both. Consider for simplicity two samples of size _n_ 1 and _n_ 2, which are realisation of two random compositions **x** 1 and **x** 2, each with an normal distribution on the simplex. Consider the following hypothesis: 

1. there is no difference between both groups; 

2. the covariance structure is the same, but centres are different; 

3. the centres are the same, but the covariance structure is different; 

4. the groups differ in their centres and in their covariance structure. 

Note that if we accept the first hypothesis, it makes no sense to test the second or the third; the same happens for the second with respect to the third, although these two are exchangeable. This can be considered as a lattice structure in which we go from the bottom or lowest level to the top or highest level until we accept one hypothesis. At that point it makes no sense to test further hypothesis and it is advisable to stop. 

To perform tests on these hypothesis, we are going to use coordinates **x** _[∗]_ and to assume they follow each a multivariate normal distribution. For the parameters of the two multivariate normal distributions, the four hypothesis are expressed, in the same order as above, as follows: 

1. the vectors of expected values and the covariance matrices are the same: _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2; 

2. the covariance matrices are the same, but not the vectors of expected values: 

   - _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2; 

63 

_CHAPTER 7. STATISTICAL INFERENCE_ 

64 

3. the vectors of expected values are the same, but not the covariance matrices: _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2; 

4. neither the vectors of expected values, nor the covariance matrices are the same: _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2. 

The last hypothesis is called the model, and the other hypothesis will be confronted with it, to see which one is more plausible. In other words, for each test, the model will be the alternative hypothesis _H_ 1. 

For each single case we can use either unbiased or maximum likelihood estimates of the parameters. Under assumptions of multivariate normality, they are identical for the expected values and have a different divisor of the covariance matrix (the sample size _n_ in the maximum likelihood approach, and _n −_ 1 in the unbiased case). Here developments will be presented in terms of maximum likelihood estimates, as those have been used in the previous chapter. Note that estimators change under each of the possible hypothesis, so each case will be presented separately. The following developments are based on Aitchison (1986, p. 153-158) and Krzanowski (1988, p. 323-329), although for a complete theoretical proof Mardia et al. (1979, section 5.5.3) is recommended. The primary computations from the coordinates, _h_ ( **x** 1) = **x** _[∗]_ 1[, of the] _[ n]_[1][samples in one group,] and _h_ ( **x** 2) = **x** _[∗]_ 2[,][of][the] _[n]_[2][samples][in][the][other][group,][are] 

1. the separate sample estimates 

   - (a) of the vectors of expected values: 

**==> picture [154 x 28] intentionally omitted <==**

- (b) of the covariance matrices: 

**==> picture [150 x 65] intentionally omitted <==**

2. the pooled covariance matrix estimate: 

**==> picture [88 x 25] intentionally omitted <==**

3. the combined sample estimates 

**==> picture [178 x 51] intentionally omitted <==**

_7.1. TESTING HYPOTHESIS ABOUT TWO GROUPS_ 

65 

To test the different hypothesis, we will use the generalised likelihood ratio test, which is based on the following principles: consider the maximised likelihood function for data **x** _[∗]_ under the null hypothesis, _L_ 0( **x** _[∗]_ ) and under the model with no restrictions (case 4), _Lm_ ( **x** _[∗]_ ). The test statistic is then _R_ ( **x** _[∗]_ ) = _Lm_ ( **x** _[∗]_ ) _/L_ 0( **x** _[∗]_ ), and the larger the value is, the more critical or resistant to accept the null hypothesis we shall be. In some cases the exact distribution of this cases is known. In those cases where it is not known, we shall use Wilks asymptotic approximation: under the null hypothesis, which places _c_ constraints on the parameters, the test statistic _Q_ ( **x** _[∗]_ ) = 2 ln( _R_ ( **x** _[∗]_ )) is distributed approximately as _χ_[2] ( _c_ ). For the cases to be studied, the approximate generalised ratio test statistic then takes the form: 

**==> picture [198 x 31] intentionally omitted <==**

1. Equality of centres and covariance structure: The null hypothesis is that _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2, thus we need the estimates of the common paˆ 

rameters _**µ**_ = _**µ**_ 1 = _**µ**_ 2 and Σ = Σ1 = Σ2, which are, respectively, _**µ** c_ for _**µ**_ and Σ[ˆ] _c_ for Σ under the null hypothesis, and _**µ**_ ˆ _i_ for _**µ** i_ and Σ[ˆ] _i_ for Σ _i_ , _i_ = 1 _,_ 2, under the model, resulting in a test statistic 

**==> picture [278 x 31] intentionally omitted <==**

to be compared against the upper percentage points of the _χ_[2][ �] 2[1] _[D]_[(] _[D][ −]_[1)] � distribution. 

2. Equality of covariance structure with different centres: The null hypothesis is that _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2, thus we need the estimates of _**µ**_ 1, _**µ**_ 2 and of the common covariance matrix Σ = Σ1 = Σ2, which are Σ[ˆ] _p_ for Σ under the null hypothesis and Σ[ˆ] _i_ for Σ _i_ , _i_ = 1 _,_ 2, under the model, resulting in a test statistic 

**==> picture [303 x 31] intentionally omitted <==**

3. Equality of centres with different covariance structure: The null hypothesis is that _**µ**_ 1 = _**µ**_ 2 and Σ1 = Σ2, thus we need the estimates of the common centre _**µ**_ = _**µ**_ 1 = _**µ**_ 2 and of the covariance matrices Σ1 and Σ2. In this case no explicit form for the maximum likelihood estimates exists. Hence the need for a simple iterative method which requires the following steps: 

   - (a) Set the initial value Σ[ˆ] _ih_ = Σ[ˆ] _i_ , _i_ = 1 _,_ 2; 

   - (b) compute the common mean, weighted by the variance of each group: 

**==> picture [218 x 14] intentionally omitted <==**

_CHAPTER 7. STATISTICAL INFERENCE_ 

66 

- (c) compute the variances of each group with respect to the common mean: 

ˆ ˆ ˆΣ _ih_ = ˆΣ _i_ + (ˆ _**µ** i −_ _**µ** h_ )(ˆ _**µ** i −_ _**µ** h_ ) _[′] , i_ = 1 _,_ 2 ; 

- (d) Repeat steps 2 and 3 until convergence. 

Thus we have Σ[ˆ] _i_ 0 for Σ _i_ , _i_ = 1 _,_ 2, under the null hypothesis and Σ[ˆ] _i_ for Σ _i_ , _i_ = 1 _,_ 2, under the model, resulting in a test statistic 

**==> picture [254 x 31] intentionally omitted <==**

## **7.2 Probability and confidence regions for compositional data** 

Like confidence intervals, confidence regions are a measure of variability, although in this case it is a measure of joint variability for the variables involved. They can be of interest in themselves, to analyse the precision of the estimation obtained, but more frequently they are used to visualise differences between groups. Recall that for compositional data with three components, confidence regions can be plotted in the corresponding ternary diagram, thus giving evidence of the relative behaviour of the various centres, or of the populations themselves. The following method to compute confidence regions assumes either multivariate normality, or the size of the sample to be large enough for the multivariate central limit theorem to hold. 

Consider a composition **x** _∈S[D]_ and assume it follows a normal distribution on _S[D]_ as defined in section 6.1.1. Then, the ( _D −_ 1)-variate vector **x** _[∗]_ = _h_ ( **x** ) follows a multivariate normal distribution. 

Three different cases might be of interest: 

1. we know the true mean vector and the true variance matrix of the random vector **x** _[∗]_ , and want to plot a probability region; 

2. we do not know the mean vector and variance matrix of the random vector, and want to plot a confidence region for its mean using a sample of size _n_ , 

3. we do not know the mean vector and variance matrix of the random vector, and want to plot a probability region (incorporating our uncertainty). 

In the first case, if a random vector **x** _[∗]_ follows a multivariate normal distribution with known parameters _**µ**_ and Σ, then 

**==> picture [157 x 12] intentionally omitted <==**

is a chi square distribution of _D −_ 1 degrees of freedom. Thus, for given _α_ , we may obtain (through software or tables) a value _κ_ such that 

**==> picture [259 x 13] intentionally omitted <==**

_7.3. EXERCISES_ 

67 

This defines a (1 _− α_ )100% probability region centred at _**µ**_ in R _[D]_ , and consequently **x** = _h[−]_[1] ( **x** _[∗]_ ) defines a (1 _− α_ )100% probability region centred at the mean in the simplex. 

Regarding the second case, it is well known that for a sample of size _n_ (and **x** _[∗]_ normally-distributed or _n_ big enough), the maximum likelihood estimates **x** ¯ _[∗]_ and Σ[ˆ] satisfy that 

**==> picture [248 x 21] intentionally omitted <==**

follows a Fisher _F_ distribution on ( _D −_ 1 _, n − D_ + 1) degrees of freedom (Krzanowski, 1988, see p. 227-228 for further details). Again, for given _α_ , we may obtain a value _c_ such that 

**==> picture [289 x 46] intentionally omitted <==**

with _κ_ = _n−DD−_ +11 _[c]_[.][But][(¯] **[x]** _[∗][−]_ _**[µ]**_[)ˆΣ] _[−]_[1][(¯] **[x]** _[∗][−]_ _**[µ]**_[)] _[′]_[=] _[κ]_[(constant)][defines][a][(1] _[ −] α_ )100% confidence region centred at **x** ¯ _[∗]_ in R _[D]_ , and consequently _ξ_ = _h[−]_[1] ( _**µ**_ ) defines a (1 _− α_ )100% confidence region around the centre in the simplex. 

Finally, in the third case, one should actually use the multivariate StudentSiegel predictive distribution: a new value of **x** _[∗]_ will have as density 

**==> picture [304 x 27] intentionally omitted <==**

This distribution is unfortunately not commonly tabulated, and it is only available in some specific packages. On the other side, if _n_ is large with respect to _D_ , the differences between the first and third options are negligible. 

Note that for _D_ = 3, _D −_ 1 = 2 and we have an ellipse in real space, in any of the first two cases: the only difference between them is how the constant _κ_ is computed. The parameterisation equations in polar coordinates, which are necessary to plot these ellipses, are given in Appendix B. 

## **7.3 Exercises** 

Exercise 7.3.1 _Divide the sample of Table 5.1 into two groups (at your will) and perform the different tests on the centres and covariance structures._ 

Exercise 7.3.2 _Compute and plot a confidence region for the_ ilr _transformed mean of the data from table 2.1 in_ R[2] _._ 

Exercise 7.3.3 _Transform the confidence region of exercise 7.3.2 back into the ternary diagram using_ ilr _[−]_[1] _._ 

_CHAPTER 7. STATISTICAL INFERENCE_ 

68 

Exercise 7.3.4 _Compute and plot a 90% probability region for the_ ilr _transformed data of table 2.1 in_ R[2] _, together with the sample. Use the chi square distribution._ 

Exercise 7.3.5 _For each of the four hypothesis in section 7.1, compute the number of parameters to be estimated if the composition has D parts. The fourth hypothesis needs more parameters than the other three. How many, with respect to each of the three simpler hypothesis? Compare with the degrees of freedom of the χ_[2] _distributions of page 65._ 

## **Chapter 8** 

## **Compositional processes** 

Compositions can evolve depending on an external parameter like space, time, temperature, pressure, global economic conditions and many other ones. The external parameter may be continuous or discrete. In general, the evolution is expressed as a function **x** ( _t_ ), where _t_ represents the external variable and the image is a composition in _S[D]_ . In order to model compositional processes, the study of simple models appearing in practice is very important. However, apparently complicated behaviours represented in ternary diagrams may be close to linear processes in the simplex. The main challenge is frequently to identify compositional processes from available data. This is done using a variety of techniques that depend on the data, the selected model of the process and the prior knowledge about them. Next subsections present three simple examples of such processes. The most important is the linear process in the simplex, that follows a straight-line in the simplex. Other frequent process are the complementary processes and mixtures. In order to identify the models, two standard techniques are presented: regression and principal component analysis in the simplex. The first one is adequate when compositional data are completed with some external covariates. Contrarily, principal component analysis tries to identify directions of maximum variability of data, i.e. a linear process in the simplex with some unobserved covariate. 

## **8.1 Linear processes: exponential growth or decay of mass** 

Consider _D_ different species of bacteria which reproduce in a rich medium and assume there are no interaction between the species. It is well-known that the mass of each species grows proportionally to the previous mass and this causes an exponential growth of the mass of each species. If _t_ is time and each component of the vector **x** ( _t_ ) represents the mass of a species at the time _t_ , the model is 

**==> picture [221 x 11] intentionally omitted <==**

69 

_CHAPTER 8. COMPOSITIONAL PROCESSES_ 

70 

where _**λ**_ = [ _λ_ 1 _, λ_ 2 _, . . . , λD_ ] contains the rates of growth corresponding to the species. In this case, _λi_ will be positive, but one can imagine _λi_ = 0, the _i_ -th species does not vary; or _λi <_ 0, the _i_ -th species decreases with time. Model (8.1) represents a process in which both the total mass of bacteria and the composition of the mass by species are specified. Normally, interest is centred in the compositional aspect of (8.1) which is readily obtained applying a closure to the equation (8.1). From now on, we assume that **x** ( _t_ ) is in _S[D]_ . 

A simple inspection of (8.1) permits to write it using the operations of the simplex, 

**==> picture [248 x 11] intentionally omitted <==**

where a straight-line is identified: **x** (0) is a point on the line taken as the origin; **p** is a constant vector representing the direction of the line; and _t_ is a parameter with values on the real line (positive or negative). 

The linear character of this process is enhanced when it is represented using coordinates. Select a basis in _S[D]_ , for instance, using balances determined by a sequential binary partition, and denote the coordinates **u** ( _t_ ) = ilr( **x** )( _t_ ), **q** = ilr( **p** ). The model for the coordinates is then 

**==> picture [216 x 11] intentionally omitted <==**

a typical expression of a straight-line in R _[D][−]_[1] . The processes that follow a straight-line in the simplex are more general than those represented by Equations (8.2) and (8.3), because changing the parameter _t_ by any function _φ_ ( _t_ ) in the expression, still produces images on the same straight-line. 

Example 8.1.1 (growth of bacteria population) _Set D_ = 3 _and consider species 1, 2, 3, whose relative masses were_ 82 _._ 7% _,_ 16 _._ 5% _and_ 0 _._ 8% _at the initial observation (t_ = 0 _). The rates of growth are known to be λ_ 1 = 1 _, λ_ 2 = 2 _and λ_ 3 = 3 _. Select the sequential binary partition and balances specified in Table 8.1._ 

Table 8.1: Sequential binary partition and balance-coordinates used in the example _growth of bacteria population_ 

**==> picture [189 x 52] intentionally omitted <==**

_The process of growth is shown in Figure 8.1, both in a ternary diagram (left) and in the plane of the selected coordinates (right). Using coordinates it is easy to identify that the process corresponds to a straight-line in the simplex. Figure 8.2 shows the evolution of the process in time in two usual plots: the one on the left shows the evolution of each part-component in per unit; on the right,_ 

_8.1. LINEAR PROCESSES: EXPONENTIAL GROWTH OR DECAY OF MASS_ 71 

**==> picture [339 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1<br>2<br>t=0<br>t=0 1<br>0<br>-1<br>-2<br>t=5<br>t=5<br>-3<br>-4 -3 -2 -1 0 1 2 3 4<br>x2 x3 u1<br>u2<br>**----- End of picture text -----**<br>


Figure 8.1: Growth of 3 species of bacteria in 5 units of time. Left: ternary diagram; axis used are shown (thin lines). Right: process in coordinates. 

**==> picture [335 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 1<br>0.9<br>0.8 0.8<br>0.7 x1 x3 x3<br>0.6 0.6<br>x2<br>0.5<br>x2<br>0.4 0.4<br>0.3 x1<br>0.2 0.2<br>0.1<br>0 0<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 0 1 2 3 4 5<br>time time<br>mass (per unit) cumulated per unit<br>**----- End of picture text -----**<br>


Figure 8.2: Growth of 3 species of bacteria in 5 units of time. Evolution of per unit of mass for each species. Left: per unit of mass. Right: cumulated per unit of mass; _x_ 1, lower band; _x_ 2, intermediate band; _x_ 3 upper band. Note the inversion of abundances of species 1 and 3. 

_the same evolution is presented as parts adding up to one in a cumulative form. Normally, the graph on the left is more understandable from the point of view of evolution._ 

Example 8.1.2 (washing process) _A liquid reservoir of constant volume V receives an input of the liquid of Q (volume per unit time) and, after a very active mixing inside the reservoir, an equivalent output Q is released. At time t_ = 0 _, volumes (or masses) x_ 1(0) _, x_ 2(0) _, x_ 3(0) _of three contaminants are stirred in the reservoir. The contaminant species are assumed non-reactive. Attention is paid to the relative content of the three species at the output in time. The output concentration is proportional to the mass in the reservoir (Albar`ede, 1995, p.346),_ 

**==> picture [185 x 25] intentionally omitted <==**

_After closure, this process corresponds to an exponential decay of mass in S_[3] _. The peculiarity is that, in this case, λi_ = _−Q/V for the three species. A repre-_ 

_CHAPTER 8. COMPOSITIONAL PROCESSES_ 

72 

_sentation in orthogonal balances, as functions of time, is_ 

**==> picture [203 x 61] intentionally omitted <==**

_Therefore, from the compositional point of view, the relative concentration of the contaminants in the subcomposition associated with the three contaminants is constant. This is not in contradiction to the fact that the mass of contaminants decays exponentially in time._ 

Exercise 8.1.1 _Select two arbitrary 3-part compositions,_ **x** (0) _,_ **x** ( _t_ 1) _, and consider the linear process from_ **x** (0) _to_ **x** ( _t_ 1) _. Determine the direction of the process normalised to one and the time, t_ 1 _, necessary to arrive to_ **x** ( _t_ 1) _. Plot the process in a) a ternary diagram, b) in balance-coordinates, c) evolution in time of the parts normalised to a constant._ 

Exercise 8.1.2 _Chose_ **x** (0) _and_ **p** _in S_[3] _. Consider the process_ **x** ( _t_ ) = **x** (0) _⊕ t ⊙_ **p** _with_ 0 _≤ t ≤_ 1 _. Assume that the values of the process at t_ = _j/_ 49 _, j_ = 1 _,_ 2 _, . . . ,_ 50 _are perturbed by observation errors,_ **y** ( _t_ ) _distributed as a normal on the simplex Ns_ ( _µ,_ Σ) _, with µ_ = _C_ [1 _,_ 1 _,_ 1] _and_ Σ = _σ_[2] _I_ 3 _(I_ 3 _unit_ (3 _×_ 3) _- matrix). Observation errors are assumed independent of t and_ **x** ( _t_ ) _. Plot_ **x** ( _t_ ) _and_ **z** ( _t_ ) = **x** ( _t_ ) _⊕_ **y** ( _t_ ) _in a ternary diagram and in a balance-coordinate plot. Try with different values of σ_[2] _._ 

## **8.2 Complementary processes** 

Apparently simple compositional processes appear to be non-linear in the simplex. This is the case of systems in which the mass from some components are transferred into other ones, possibly preserving the total mass. For a general instance, consider the radioactive isotopes _{x_ 1 _, x_ 2 _, . . . , xn}_ that disintegrate into non-radioactive materials _{xn_ +1, _xn_ +2, _. . . , xD}_ . The process in time _t_ is described by 

**==> picture [341 x 29] intentionally omitted <==**

with 1 _≤ i ≤ n_ and _n_ + 1 _≤ j ≤ D_ . From the compositional point of view, the subcomposition corresponding to the first group behaves as a linear process. The second group of parts _{xn_ +1 _, xn_ +2 _, . . . , xD}_ is called complementary because it sums up to preserve the total mass in the system and does not evolve linearly despite of its simple form. 

_8.2. COMPLEMENTARY PROCESSES_ 

73 

Example 8.2.1 (one radioactive isotope) _Consider the radioactive isotope x_ 1 _which is transformed into the non-radioactive isotope x_ 3 _, while the element x_ 2 _remains unaltered. This situation, with λ_ 1 _<_ 0 _, corresponds to_ 

**==> picture [316 x 11] intentionally omitted <==**

_that is mass preserving. The group of parts behaving linearly is {x_ 1 _, x_ 2 _}, and a complementary group is {x_ 3 _}. Table 8.2 shows parameters of the model and Figures 8.3 and 8.4 show different aspects of the compositional process from t_ = 0 _to t_ = 10 _._ 

Table 8.2: Parameters for Example 8.2.1: _one radioactive isotope._ Disintegration rate is ln 2 times the inverse of the half-lifetime. Time units are arbitrary. The lower part of the table represents the sequential binary partition used to define the balance-coordinates. 

|parameter|_x_1|_x_2|_x_3|
|---|---|---|---|
|disintegration rate|0_._5|0_._0|0_._0|
|initial mass|1_._0|0_._4|0_._5|
|balance 1|+1|+1|_−_1|
|balance 2|+1|_−_1|0|



**==> picture [339 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1<br>1<br>t=0<br>0<br>-1<br>t=0<br>-2<br>-3<br>t=10<br>-4<br>-3 -2.5 -2 -1.5 -1 -0.5 0 0.5<br>x2 t=5 x3 u1<br>u2<br>**----- End of picture text -----**<br>


Figure 8.3: Disintegration of one isotope _x_ 1 into _x_ 3 in 10 units of time. Left: ternary diagram; axis used are shown (thin lines). Right: process in coordinates. The mass in the system is constant and the mass of _x_ 2 is constant. 

_A first inspection of the Figures reveals that the process appears as a segment in the ternary diagram (Fig. 8.3, right). This fact is essentially due to the constant mass of x_ 2 _in a conservative system, thus appearing as a constant per-unit. In figure 8.3, left, the evolution of the coordinates shows that the process is not linear; however, except for initial times, the process may be approximated by a linear one. The linear or non-linear character of the process is hardly detected in Figures 8.4 showing the evolution in time of the composition._ 

_CHAPTER 8. COMPOSITIONAL PROCESSES_ 

74 

**==> picture [334 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.9 1<br>0.8<br>x3<br>0.7 0.8<br>0.6 0.6 x3<br>0.5<br>0.4<br>0.4<br>0.3<br>x2<br>0.20.1 0.2 x1 x2<br>x1<br>0 0<br>0 1 2 3 4 5 6 7 8 9 10 0 1 2 3 4 5 6 7 8 9 10<br>time time<br>mass (per unit) cumulated per unit<br>**----- End of picture text -----**<br>


Figure 8.4: Disintegration of one isotope _x_ 1 into _x_ 3 in 10 units of time. Evolution of per unit of mass for each species. Left: per unit of mass. Right: cumulated per unit of mass; _x_ 1, lower band; _x_ 2, intermediate band; _x_ 3 upper band. Note the inversion of abundances of species 1 and 3. 

Example 8.2.2 (three radioactive isotopes) _Consider three radioactive isotopes that we identify with a linear group of parts, {x_ 1 _, x_ 2 _, x_ 3 _}. The disintegrated mass of x_ 1 _is distributed on the non-radioactive parts {x_ 4 _, x_ 5 _, x_ 6 _} (complementary group). The whole disintegrated mass from x_ 2 _and x_ 3 _is assigned to x_ 4 _and x_ 5 _respectively. The values of the parameters considered are shown in Table_ 

Table 8.3: Parameters for Example 8.2.2: _three radioactive isotopes._ Disintegration rate is ln 2 times the inverse of the half-lifetime. Time units are arbitrary. The middle part of the table corresponds to the coefficients _aij_ indicating the part of the mass from _xi_ component transformed into the _xj_ . Note they add to one and the system is mass conservative. The lower part of the table shows the sequential binary partition to define the balance coordinates. 

|parameter|_x_1|_x_2|_x_3|_x_4|_x_5|_x_6|
|---|---|---|---|---|---|---|
|disintegration rate|0_._2|0_._04|0_._4|0_._0|0_._0|0_._0|
|initial mass|30_._0|50_._0|13_._0|1_._0|1_._2|0_._7|
|mass from _x_1|0_._0|0_._0|0_._0|0_._7|0_._2|0_._1|
|mass from _x_2|0_._0|0_._0|0_._0|0_._0|1_._0|0_._0|
|mass from _x_3|0_._0|0_._0|0_._0|0_._0|0_._0|1_._0|
|balance 1|+1|+1|+1|_−_1|_−_1|_−_1|
|balance 2|+1|+1|_−_1|0|0|0|
|balance 3|+1|_−_1|0|0|0|0|
|balance 4|0|0|0|+1|+1|_−_1|
|balance 5|0|0|0|+1|_−_1|0|



_8.3. Figure 8.5 (left) shows the evolution of the subcomposition of the complementary group in 20 time units; no special conclusion is got from it. Contrarily, Figure 8.5 (right), showing the evolution of the coordinates of the subcomposition, reveals a loop in the evolution with a double point (the process passes two times through this compositional point); although less clearly, the same fact can be observed in the representation of the ternary diagram in Figure 8.6. This is a quite surprising and involved behaviour despite of the very simple character_ 

_8.2. COMPLEMENTARY PROCESSES_ 

75 

**==> picture [335 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.5 0.2<br>x5<br>0.4<br>x4 0.0<br>0.3<br>x6 t=0<br>0.2<br>-0.2<br>0.1<br>t=20<br>0.0 -0.4<br>0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0 20.0 -0.2 -0.1 0.0 0.1 0.2 0.3 0.4 0.5<br>time y4<br>y5<br>per unit mass<br>**----- End of picture text -----**<br>


Figure 8.5: Disintegration of three isotopes _x_ 1 _, x_ 2 _, x_ 3. Disintegration products are masses added to _x_ 4 _, x_ 5 _, x_ 6 in 20 units of time. Left: evolution of per unit of mass of _x_ 4 _, x_ 5 _, x_ 6. Right: _x_ 4 _, x_ 5 _, x_ 6 process in coordinates; a loop and a double point are revealed. 

**==> picture [139 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
x4<br>x5 x6<br>**----- End of picture text -----**<br>


Figure 8.6: Disintegration of three isotopes _x_ 1 _, x_ 2 _, x_ 3. Products are masses added to _x_ 4 _, x_ 5 _, x_ 6, in 20 units of time, represented in the ternary diagram. Loop and double point are visible. 

_of the complementary process. Changing the parameters of the process one can obtain more simple behaviours, for instance without double points or exhibiting less curvature. However, these processes only present one possible double point or a single bend point; the branches far from these points are suitable for a linear approximation._ 

Example 8.2.3 (washing process (continued)) _Consider the washing process. Let us assume that the liquid is water with density equal to one and define the mass of water x_ 0( _t_ ) = _V ·_ 1 _−_[�] _xi_ ( _t_ ) _, that may be considered as a complementary process. The mass concentration at the output is the closure of the four components, being the closure constant proportional to V . The compositional process is not a straight-line in the simplex, because the new balance now needed to represent the process is_ 

**==> picture [141 x 25] intentionally omitted <==**

_that is neither a constant nor a linear function of t._ 

_CHAPTER 8. COMPOSITIONAL PROCESSES_ 

76 

Exercise 8.2.1 _In the washing process example, set x_ 1(0) = 1 _., x_ 2(0) = 2 _., x_ 3(0) = 3 _., V_ = 100 _., Q_ = 5 _.. Find the sequential binary partition used in the example. Plot the evolution in time of the coordinates and mass concentrations including the water x_ 0( _t_ ) _. Plot, in a ternary diagram, the evolution of the subcomposition x_ 0 _, x_ 1 _, x_ 2 _._ 

## **8.3 Mixture process** 

Another kind of non-linear process in the simplex is that of the mixture processes. Consider two large containers partially filled with _D_ species of materials or liquids with mass (or volume) concentrations given by **x** and **y** in _S[D]_ . The total masses in the containers are _m_ 1 and _m_ 2 respectively. Initially, the concentration in the first container is **z** 0 = **x** . The content of the second container is steadily poured and stirred in the first one. The mass transferred from the second to the first container is _φm_ 2 at time _t_ , i.e. _φ_ = _φ_ ( _t_ ). The evolution of mass in the first container, is 

**==> picture [191 x 11] intentionally omitted <==**

where **z** ( _t_ ) is the process of the concentration in the first container. Note that **x** , **y** , **z** are considered closed to 1. The final composition in the first container is 

**==> picture [234 x 22] intentionally omitted <==**

The mixture process can be alternatively expressed as mixture of the initial and final compositions (often called end-points): 

**==> picture [129 x 11] intentionally omitted <==**

for some function of time, _α_ ( _t_ ), where, to fit the physical statement of the process, 0 _≤ α ≤_ 1. But there is no problem in assuming that _α_ may take values on the whole real-line. 

Example 8.3.1 (Obtaining a mixture) _A mixture of three liquids is in a large container A. The numbers of volume units in A for each component are_ [30 _,_ 50 _,_ 13] _, i.e. the composition in ppu (parts per unit) is_ **z** 0 = **z** (0) = [0 _._ 3226 _,_ 0 _._ 5376 _,_ 0 _._ 1398] _. Another mixture of the three liquids,_ **y** _, is in container B. The content of B is poured and stirred in A. The final concentration in A is_ **z** 1 = [0 _._ 0411 _,_ 0 _._ 2740 _,_ 0 _._ 6849] _. One can ask for the composition_ **y** _and for the required volume in container B. Using the notation introduced above, the initial volume in A is m_ 1 = 93 _, the volume and concentration in B are unknown. Equation (8.4) is now a system of three equations with three unknowns: m_ 2 _, y_ 1 _, y_ 2 _(the closure condition implies y_ 3 = 1 _− y_ 1 _− y_ 2 _):_ 

**==> picture [276 x 36] intentionally omitted <==**

_8.3. MIXTURE PROCESS_ 

77 

_which, being a simple system, is not linear in the unknowns. Note that (8.5) involves masses or volumes and, therefore, it is not a purely compositional equation. This situation always occurs in mixture processes. Figure 8.7 shows the process of mixing (M) both in a ternary diagram (left) and in the balancecoordinates u_ 1 = 6 _[−]_[1] _[/]_[2] ln( _z_ 1 _z_ 2 _/z_ 3) _, u_ 2 = 2 _[−]_[1] _[/]_[2] ln( _z_ 1 _/z_ 2) _(right). Fig. 8.7 also_ 

**==> picture [329 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
x1 0.0<br>-0.2<br>z0<br>-0.4<br>-0.6<br>M<br>-0.8<br>P<br>-1.0<br>z0<br>-1.2<br>M z1<br>-1.4<br>P<br>z1 -1.6<br>-2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5<br>x2 x3 u1<br>u2<br>**----- End of picture text -----**<br>


Figure 8.7: Two processes going from **z** 0 to **z** 1. (M) mixture process; (P) linear perturbation process. Representation in the ternary diagram, left; using balance-coordinates _u_ 1 = 6 _[−]_[1] _[/]_[2] ln( _z_ 1 _z_ 2 _/z_ 3), _u_ 2 = 2 _[−]_[1] _[/]_[2] ln( _z_ 1 _/z_ 2), right. 

_shows a perturbation-linear process, i.e. a straight-line in the simplex, going from_ **z** 0 _to_ **z** 1 _(P)._ 

Exercise 8.3.1 _In the example obtaining a mixture find the necessary volume m_ 2 _and the composition in container B,_ **y** _. Find the direction of the perturbation-linear process to go from_ **z** 0 _to_ **z** 1 _._ 

Exercise 8.3.2 _A container has a constant volume V_ = 100 _volume units and initially contains a liquid whose composition is_ **x** (0) = _C_ [1 _,_ 1 _,_ 1] _. A constant flow of Q_ = 1 _volume unit per second with volume composition_ **x** = _C_ [80 _,_ 2 _,_ 18] _gets into the box. After a complete mixing there is an output whose flow equals Q with the volume composition_ **x** ( _t_ ) _at the time t. Model the evolution of the volumes of the three components in the container using ordinary linear differential equations and solve them (Hint: these equations are easily found in textbooks, e.g. Albar`ede (1995, p. 345–350)). Are you able to plot the curve for the output composition_ **x** ( _t_ ) _in the simplex without using the solution of the differential equations? Is it a mixture?_ 

78 

# _CHAPTER 8. COMPOSITIONAL PROCESSES_ 

## **Chapter 9** 

## **Linear compositional models** 

Linear models are intended to relate two sets of random variables using linear relationships. They are very general and appear routinely in many statistical applications. A first set of variables, called response variables, are to be predicted from a second set of variables, called predictors or covariates. Linear combinations of the predictors, transformed by some non-linear function, frequently called _link function_ , are used to get a predictor function approaching responses. Errors or residuals are measured as Euclidean differences between responses and the predictor function. There is a extensive literature on general linear models, for instance Anderson (1984). The two sets of variables may have very different characteristics (categorical, real, discrete) and the link functions choices are also multiple. We are here interested in cases where responses or predictors have compositional character. When the response is compositional we must be aware that residuals should be measured with compositional distances, i.e. within the framework of Aitchison geometry of the simplex. Section 9.1 treats the case where the response is compositional and the covariates are real or discrete thus corresponding to a multiple regression. Response is handled using its coordinates. The ilr transformation plays the role of a link function. Section 9.2 assumes a single real response and a compositional predictor. Again ilr plays an important role. Section 9.3 discusses the case in which the response is compositional and the predictors reduce to a categorical variable indicating a treatment or a subpopulation. The goal of such an analysis of variance (ANOVA) model is to decide whether the center of compositions across the treatments are equal or not. Section 9.4 deals with discriminant analysis. In this case, response is a category to which a compositional observation (predictor) is assigned. The model is then a rule to assign an observed composition to categories or treatments and it provides a probability of belonging for each category. 

79 

_CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

80 

## **9.1 Linear regression with compositional variables** 

Linear regression is intended to identify and estimate a linear model from response data that depend linearly on one or more covariates. The assumption is that responses are affected by errors or random deviations of the mean model. The most usual methods to fit the regression coefficients are the well-known least-squares techniques. 

The problem of regression when the response is compositional is stated as follows. A compositional sample in _S[D]_ is available and it is denoted by **x** 1, **x** 2 _, . . ._ , **x** _n_ . The _i_ -th data-point **x** _i_ is associated with one or more external variables or covariates grouped in the vector **t** _i_ = [ _ti_ 0 _, ti_ 1 _, . . . , tir_ ], where _ti_ 0 = 1. The goal is to estimate the coefficients of a curve or surface in _S[D]_ whose equation is 

**==> picture [294 x 30] intentionally omitted <==**

where **t** = [ _t_ 0 _, t_ 1 _, . . . , tr_ ] are real covariates and are identified as the parameters of the curve or surface; the first parameter is defined as the constant _t_ 0 = 1, as assumed for observations. The compositional coefficients of the model, _**β** j ∈S[D]_ , are to be estimated from the data. The model (9.1) is very general and takes different forms depending on how the covariates _tj_ are defined. For instance, defining _tj_ = _t[j]_ , being _t_ a covariate, the model is a polynomial, particularly, if _r_ = 1, it is a straight-line in the simplex (8.2). 

The most popular fitting method of the model (9.1) is the least-squares deviation criterion. As the response **x** ( **t** ) is compositional, it is natural to measure deviations also in the simplex using the concepts of the Aitchison geometry. The deviation of the model (9.1) from the data is defined as **x** ˆ( **t** _i_ ) _⊖_ **x** _i_ and its size by the Aitchison norm _∥_ **x** ˆ( **t** _i_ ) _⊖_ **x** _i∥_[2] _a_[=][d][2] _a_[(ˆ] **[x]**[(] **[t]** _[i]_[)] _[,]_ **[ x]** _[i]_[).][The][target][function] (sum of squared errors, SSE) is 

**==> picture [113 x 29] intentionally omitted <==**

toimplicitbe minimisedin **x** ˆ( **t** _i_ ).asThea functionnumberofofthecoefficientscompositionalto becoefficientsestimated in _**β** j_ thiswhichlinearare model is ( _r_ + 1) _·_ ( _D −_ 1). 

This least-squares problem is reduced to _D −_ 1 ordinary least-squares problems when the compositions are expressed in coordinates with respect to an orthonormal basis of the simplex. Assume that an orthonormal basis has been chosen inˆ _S[D]_ and that the coordinates of ˆ **x** ( **t** ), **x** _i_ and _**β** j_ are **x** _[∗] i_[= [] _[x][∗] i_ 1 _[, x][∗] i_ 2 _[, . . . , x][∗] i,D−_ 1[],] **x** _[∗]_ ( **t** ) = [ˆ _x[∗]_ 1[(] **[t]**[)] _[,]_[ ˆ] _[x][∗]_ 2[(] **[t]**[)] _[, . . . ,]_[ ˆ] _[x][∗] D−_ 1[(] **[t]**[)]][and] _**[β]**[∗] j_[=][[] _[β] j[∗]_ 1 _[, β] j[∗]_ 2 _[, . . . , β] j,D[∗] −_ 1[],][being][these] vectors in R _[D][−]_[1] . Since perturbation and powering in the simplex are translated into the ordinary sum and product by scalars in the coordinate real space, the 

_9.1. LINEAR REGRESSION WITH COMPOSITIONAL VARIABLES_ 81 

model (9.1) is expressed in coordinates as 

**==> picture [201 x 29] intentionally omitted <==**

For each coordinate, this expression becomes 

**==> picture [297 x 11] intentionally omitted <==**

Also Aitchison norm and distance become the ordinary norm and distance in real space. Then, using coordinates, the target function is expressed as 

**==> picture [295 x 31] intentionally omitted <==**

where _∥· ∥_ is the norm of a real vector. The last right-hand member of (9.3) has been obtained permuting the order of the sums on the components of the vectors and on the data. All sums in (9.3) are non-negative and, therefore, the minimisation of SSE implies the minimisation of each term of the sum in _k_ , 

**==> picture [213 x 29] intentionally omitted <==**

This is, the fitting of the compositional model (9.1) reduces to the _D −_ 1 ordinary least-squares problems in (9.2). 

## **Example:** Vulnerability of a system. 

A system is subjected to external actions. The response of the system to such actions is frequently a major concern in engineering. For instance, the system may be a dike under the action of ocean-wave storms; the response may be the level of service of the dike after one event. In a simplified scenario, three responses of the system may be considered: _θ_ 1, service; _θ_ 2, damage; _θ_ 3 collapse. The dike can be designed for a design action, e.g. wave-height, _d_ , ranging 3 _≤ d ≤_ 20 (metres wave-height). Actions, parameterised by some wave-height of the storm, _h_ , also ranging 3 _≤ d ≤_ 20 (metres wave-height). Vulnerability of the system is described by the conditional probabilities 

**==> picture [247 x 30] intentionally omitted <==**

where, for any _d, h_ , **p** ( _d, h_ ) = [ _p_ 1( _d, h_ ) _, p_ 2( _d, h_ ) _, p_ 3( _d, h_ )] _∈S_[3] . In practice, **p** ( _d, h_ ) only is approximately known for a limited number of values **p** ( _di, hi_ ), _i_ = 1 _, . . . , n_ . The whole model of vulnerability can be expressed as a regression model 

**==> picture [252 x 11] intentionally omitted <==**

_CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

82 

**==> picture [321 x 292] intentionally omitted <==**

**----- Start of picture text -----**<br>
Design 3.5 Design 6.0<br>1.2 1.2<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>3 7 11 15 19 3 7 11 15 19<br>wave-height, h wave-height, h<br>service damage collapse service damage collapse<br>Design 8.5 Design 11.0<br>1.2 1.2<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>3 7 11 15 19 3 7 11 15 19<br>wave-height, h wave-height, h<br>service damage collapse service damage collapse<br>Design 13.5 Design 16.0<br>1.2 1.2<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>3 7 11 15 19 3 7 11 15 19<br>wave-height, h wave-height, h<br>service damage collapse service damage collapse<br>Probability Probability<br>Probability Probability<br>Probability Probability<br>**----- End of picture text -----**<br>


Figure 9.1: Vulnerability models obtained by regression in the simplex from the data in the Table 9.1. Horizontal axis: incident wave-height in m. Vertical axis: probability of the output response. Shown designs are 3.5, 6.0, 8.5, 11.0, 13.5, 16.0 (m design wave-height). 

so that it can be estimated by regression in the simplex. 

Consider the data in Table 9.1 containing _n_ = 9 probabilities. Figure 9.1 shows the vulnerability probabilities obtained by regression for six design values. An inspection of these Figures reveals that a quite realistic model has been obtained from a really poor sample: service probabilities decrease as the level of action increases and conversely for collapse. This changes smoothly for increasing design level. Despite the challenging shapes of these curves describing the vulnerability, they come from a linear model as can be seen in Figure 9.2 (left). In Figure 9.2 (right) these straight-lines in the simplex are shown in a ternary diagram. In these cases, the regression model has shown its smoothing capabilities. 

_9.2. REGRESSION WITH COMPOSITIONAL COVARIATES_ 

83 

**==> picture [337 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
service<br>4<br>3<br>2<br>1<br>0<br>-1<br>-2<br>-10 -8 -6 -4 -2 0 2 4 6 8 10<br>6^(1/2) ln(p0^2/ p1 p2) damage collapse<br>2^(1/2) ln(p1/p2)<br>**----- End of picture text -----**<br>


Figure 9.2: Vulnerability models in Figure 9.1 in coordinates (left) and in the ternary diagram (right). Design 3.5 (circles); 16.0 (thick line). 

## **9.2 Regression with compositional covariates** 

The model with compositional covariates appears when the goal is to predict one external variable as a function of a composition. Assume a compositional data set **x** 1, **x** 2 _, . . ._ , **x** _n_ is available, and that the _i_ -th data-point **x** _i_ is associated with an observation _yi_ of an external response variable (with support the _whole real line_ , i.e. possibly transformed with logs or any other suitable transformation). The goal is to estimate a surface on _S[D] ×_ R with equation 

**==> picture [215 x 11] intentionally omitted <==**

where _**β** ∈S[D]_ is the (simplicial) gradient of _y_ with respect to **x** , and _β_ 0 is a real intercept. In this case, since the response is a real value, the classical least squares fitting criterion may be applied, which yields the target function 

**==> picture [141 x 29] intentionally omitted <==**

As the Aitchison inner product can be computed easily from clr coefficients or ilr coordinates of **x** _i_ , this sum of squares becomes 

**==> picture [316 x 28] intentionally omitted <==**

This suggests that the actual fitting can be done using ilr coordinates without further ado. One simply fits a linear regression to the response _y_ as a linear function of ilr( **x** ). The estimated version of ilr( _**β**_ ) contains slope coefficients of the response _y_ with respect the coordinates ilr( **x** ). The simplicial gradient _**β**_ is then easily computed using ilr _[−]_[1] . The clr transformation should be avoided in this case, as its correct handling in the scope of regression requires the generalized inversion of singular matrices (something that most statistical packages are not able to do). 

_CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

84 

Tests on the coefficients of the model (9.5) may be used as usual, for instance to obtain a simplified model depending on less variables. However, one should be aware that they are related to the particular basis used, and that these simplified models will be different depending on the basis. One should thus carefully select the basis: for instance, a basis of balances may be adequate to check the dependence of _y_ on a particular subcomposition of **x** . 

Exercise 9.2.1 (sand-silt-clay from a lake) _Consider the data in Table 9.2. They are sand-silt-clay compositions from an Arctic lake taken at different depths (adapted from Coakley and Rust (1968) and cited in Aitchison (1986)). The goal is to check whether there is some trend in the composition related to the depth. Particularly, using the standard hypothesis testing in regression, check the constant and the straight-line models_ 

**==> picture [151 x 11] intentionally omitted <==**

_being t_ = _depth. Plot both models, the fitted model and the residuals, in coordinates and in the ternary diagram._ 

Exercise 9.2.2 (sand-silt-clay from a lake: second sight) _One can equivalently check whether the sediment composition brings any information about the depth at which that sample was taken. Using the data from the previous excercise, fit a linear model to explain depth as a function of the composition. Analyse the residuals as usual, as they may be considered real values._ 

_To display the model, you can follow these steps. Split the range of observed depths in several segments of the same length (four to six will be enough in CoDaPack), and give each sample a number corresponding to its depth cathegory. Plot the compositional data in a ternary diagram, using colors for each depth interval. Draw a line on the simplex, from the center of the data set along the gradient of the fitted model_ 

## **9.3 Analysis of variance with compositional response** 

ANalysis Of the VAriance (ANOVA) is the name given to a linear model where a continuous response is explained as a function of a (set of) discrete variable(s). Compositional ANOVA follows the same steps that were used to predict a composition from a continuous covariable. Notation in multi-way ANOVA (with more than one discrete covariable) can become quite difficult, therefore only one-way compositional ANOVA will be addressed here. Textbooks on multivariate ANOVA may be then useful to extend this material. 

As in the preceding section, assume a compositional sample **x** 1, **x** 2 _, . . ._ , **x** _n_ in _S[D]_ is available. These observations are classified into _K_ categories across an external categorical variable _z_ . Category _z_ may represent different treatments 

## _9.3. ANALYSIS OF VARIANCE WITH COMPOSITIONAL RESPONSE_ 85 

or subpopulations. In other words, for each composition one has also available a category _zi_ . ANOVA deals with the centres (compositional means) of the composition for each category, _**µ**_ 1 _, . . . ,_ _**µ** K_ . Following the classical notation, a compositional ANOVA model, for a given _z_ , is 

**==> picture [279 x 11] intentionally omitted <==**

where the indicator _I_ ( _z_ = _k_ ) equals 1 when the condition is true and 0 otherwise. This means that only one of the _K −_ 1 terms may be taken into account for each possible _z_ value (as the other will be powered by zero). Note that the first category does not explicitly appear in the equation: when _z_ = 1, then the = predictor is only _**β**_ 1 _**µ**_ 1 the centre of the first group. The remaining coefficients are then interpreted as increments of the composition from the reference first ˆ level to the category actually observed, **x** _|k_ = _**µ** k_ = _**β**_ 1 _⊕_ _**β** k_ , or equivalently _**β** k_ = _**µ** k ⊖_ _**µ**_ 1. The variable _**ϵ**_ is the compositional residual of the model. 

ANOVA notation may be quite cumbersome, but its fitting is straightforward. For each observation _zi_ one just constructs a vector **t** _i_ with the _K −_ 1 indicators, i.e. with many zeroes and a single 1 in the position of the observed category. With these vectors, one applies the same steps as with linear regression with compositional response (section 9.1). An important consequence of this procedure is that we implicitly assume equal total variance within each category (compare with chapter 7). 

The practice of compositional ANOVA follows the principle of working on coordinates. One first selects a basis and computes the corresponding coordinates of the observations. Then classical ANOVA is applied to explain each ilr coordinate as a mean reference level plus _K −_ 1 mean differences between categories. Tests may be applied to conclude that some of these differences are not significative, i.e. that the mean of a particular coordinate at two categories may be taken as equal. Finally, all coefficients associated with category _k_ can be back-transformed to obtain its associated compositional coefficient _**β** k_ . 

Exercise 9.3.1 (distinguishing mean rivers hydrogeochemistry) _In the course accessory files you can find a file named “Hydrochem.csv”, containing an extensive data set of the geochemical composition of water samples from several rivers and tributaries of the Llobregat river, the most important river in the Barcelona province (NE Spain). This data was studied in detail by Otero et al. (2005); Tolosana-Delgado et al. (2005), and placed, with the authors’ consent, in the public domain within the R package “compositions” (van den Boogaart and Tolosana-Delgado, 2008). Table 9.3 provides a random sample, in case the whole data set is not accessible._ 

_Fit an ANOVA model to this 3-part composition. Draw the data set using colours to distinguish between the four rivers. Plot the means of the four groups, as estimated by the ANOVA fit._ 

_CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

86 

**Advanced excercise:** _Extract the variance-covariance matrix of each mean. Draw confidence regions for them, as explained in section B._ 

## **9.4 Linear discrimination with compositional predictor** 

A composition can also be used to predict a categorical variable. Following the preceding section notation, the goal is now to estimate **p** ( **x** ), the probability that _z_ takes each of its possible _K_ values given an observed composition **x** . There are many techniques to obtain this result, like the Fisher rule, linear or quadratic discriminant analysis, or multinomial logistic regression. But essentially, we would always apply the principle of working on coordinates (take ilr’s, apply your favourite method to the coordinates, and back-transform the coefficients if they may be interpreted as compositions). This section illustrates this procedure with linear discriminant analysis (LDA), a technique available in most basic statistical packages. 

First, LDA assumes some prior probabilities _p_[0] _k_[of data-points corresponding] to each one of the _K_ categories. These are typically taken as _pk_ = 1 _/K_ (equally probable) or _pk_ = _nk/n_ (where _nk_ is the number of samples in _k_ th-category). Then, it assumes that the ilr-transformed composition has a normal distribution, with ilr mean _**µ**[∗] k_[=][ilr(] _**[µ]** k_[)][and][common][ilr-coordinates][covariance] **[Σ]**[(i.e.,][all] categories have the same covariance and possibly different mean). Applying Bayes’ Theorem, it is verified that the posterior probability vector of belonging to each class for a particular composition **x** , can be derived from the discriminant functions 

**==> picture [197 x 21] intentionally omitted <==**

with 

**==> picture [193 x 27] intentionally omitted <==**

Again, as happened with ANOVA, one category is typically placed as a sort of reference level. For instance, take _j_ = _K_ fix. Then LDA just computes the logodds of the the other _K −_ 1 categories with respect to the last one. The desired probabilities can be obtained with the inverse alr transformation, as explained in section 4.6. 

Obtained probabilities can be then used to decide which category is more probable for each possible composition **x** : typically we classify each point in _S[D]_ into the most likely group, the one with largest probability. In this sense, the discriminant functions can be used to draw the boundaries between regions _j_ and _k_ , by identifying the set of points where _djk_ ( **x** ) = 0. Some linear algebra shows that this boundary is the affine hyperplane of _S[D]_ orthogonal to the vector 

_9.4. LINEAR DISCRIMINATION WITH COMPOSITIONAL PREDICTOR_ 87 

**v** _dj_ and passing through the point **x**[0] _jk_[obtained][as] 

**==> picture [238 x 42] intentionally omitted <==**

Note that these equations are only useful to draw boundaries between neighbouring categories, i.e. between the two most probable categories of a given point in _S[D]_ . For more than 2 categories, care should be taken to draw them by segments. 

Exercise 9.4.1 (drawing borders between three groups) _Between three groups we can draw three borders (A with B, B with C, A with C). Show that these three boundaries intersect in one single point (a_ triple junction _). Find the equation of that point. Now assume that the discriminating composition has three components: note that in this case, the boundaries could be drawn as segments from the triple junction along the directions of some vectors_ **v** _jk[⊥] orthogonal to_ **v** _jk._ 

Exercise 9.4.2 (the hydrochemical data set revisited) _Using the data set from exercise 9.3.1, obtain the discriminant functions between rivers A, U and L (remove C for this exercise). This may be easily done by computing the ilr coordinates in CoDaPack, and exporting them to your favourite statistical software. Draw the data in the ilr plane and in a ternary diagram, using colours to distinguish between rivers. Add the group centers, and the boundaries between groups. If you use R, linear discriminant analysis is available with function “lda” in the package “MASS”._ 

_CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

88 

Table 9.1: Assumed vulnerability for a dike with only three outputs or responses. Probability values of the response _θk_ conditional to values of design _d_ and level of the storm _h_ . 

|_di_|_hi_|service|damage|collapse|
|---|---|---|---|---|
|3.0|3.0|0.50|0.49|0.01|
|3.0|10.0|0.02|0.10|0.88|
|5.0|4.0|0.95|0.049|0.001|
|6.0|9.0|0.08|0.85|0.07|
|7.0|5.0|0.97|0.027|0.003|
|8.0|3.0|0.997|0.0028|0.0002|
|9.0|9.0|0.35|0.55|0.01|
|10.0|3.0|0.999|0.0009|0.0001|
|10.0|10.0|0.30|0.65|0.05|



Table 9.2: Sand, silt, clay composition of sediment samples at different water depths in an Arctic lake. 

|Arctic lake.||
|---|---|
|sample no.<br>sand<br>silt<br>clay<br>depth (m)|sample no.<br>sand<br>silt<br>clay<br>depth (m)|
|1<br>77.5<br>19.5<br>3.0<br>10.4<br>2<br>71.9<br>24.9<br>3.2<br>11.7<br>3<br>50.7<br>36.1<br>13.2<br>12.8<br>4<br>52.2<br>40.9<br>6.9<br>13.0<br>5<br>70.0<br>26.5<br>3.5<br>15.7<br>6<br>66.5<br>32.2<br>1.3<br>16.3<br>7<br>43.1<br>55.3<br>1.6<br>18.0<br>8<br>53.4<br>36.8<br>9.8<br>18.7<br>9<br>15.5<br>54.4<br>30.1<br>20.7<br>10<br>31.7<br>41.5<br>26.8<br>22.1<br>11<br>65.7<br>27.8<br>6.5<br>22.4<br>12<br>70.4<br>29.0<br>0.6<br>24.4<br>13<br>17.4<br>53.6<br>29.0<br>25.8<br>14<br>10.6<br>69.8<br>19.6<br>32.5<br>15<br>38.2<br>43.1<br>18.7<br>33.6<br>16<br>10.8<br>52.7<br>36.5<br>36.8<br>17<br>18.4<br>50.7<br>30.9<br>37.8<br>18<br>4.6<br>47.4<br>48.0<br>36.9<br>19<br>15.6<br>50.4<br>34.0<br>42.2<br>20<br>31.9<br>45.1<br>23.0<br>47.0|21<br>9.5<br>53.5<br>37.0<br>47.1<br>22<br>17.1<br>48.0<br>34.9<br>48.4<br>23<br>10.5<br>55.4<br>34.1<br>49.4<br>24<br>4.8<br>54.7<br>40.5<br>49.5<br>25<br>2.6<br>45.2<br>52.2<br>59.2<br>26<br>11.4<br>52.7<br>35.9<br>60.1<br>27<br>6.7<br>46.9<br>46.4<br>61.7<br>28<br>6.9<br>49.7<br>43.4<br>62.4<br>29<br>4.0<br>44.9<br>51.1<br>69.3<br>30<br>7.4<br>51.6<br>41.0<br>73.6<br>31<br>4.8<br>49.5<br>45.7<br>74.4<br>32<br>4.5<br>48.5<br>47.0<br>78.5<br>33<br>6.6<br>52.1<br>41.3<br>82.9<br>34<br>6.7<br>47.3<br>46.0<br>87.7<br>35<br>7.4<br>45.6<br>47.0<br>88.1<br>36<br>6.0<br>48.9<br>45.1<br>90.4<br>37<br>6.3<br>53.8<br>39.9<br>90.6<br>38<br>2.5<br>48.0<br>49.5<br>97.7<br>39<br>2.0<br>47.8<br>50.2<br>103.7|



## _9.4. LINEAR DISCRIMINATION WITH COMPOSITIONAL PREDICTOR_ 89 

Table 9.3: Main anion composition of some water samples from 4 different rivers in Barcelona province (NE Spain). 

|province (NE Spain).||
|---|---|
|river<br>Cl<br>SO4<br>HCO3|river<br>Cl<br>SO4<br>HCO3|
|A<br>197.43<br>857.99<br>348.39<br>A<br>312.37<br>487.83<br>377.13<br>A<br>15.49<br>239.93<br>146.00<br>A<br>118.09<br>445.63<br>341.50<br>A<br>352.84<br>341.68<br>557.50<br>A<br>309.78<br>371.71<br>538.50<br>A<br>432.24<br>357.35<br>393.70<br>L<br>142.80<br>120.34<br>210.30<br>L<br>305.74<br>199.97<br>222.45<br>L<br>309.67<br>164.40<br>206.32<br>L<br>325.76<br>151.63<br>201.90<br>L<br>256.18<br>145.33<br>189.20<br>L<br>242.42<br>196.08<br>187.10<br>L<br>373.26<br>166.62<br>249.70<br>L<br>382.45<br>222.31<br>219.96<br>L<br>228.30<br>181.83<br>368.40<br>L<br>14.02<br>55.52<br>245.90<br>L<br>445.39<br>455.62<br>286.67<br>L<br>300.05<br>469.89<br>287.40<br>L<br>1133.39<br>581.08<br>613.60<br>L<br>652.03<br>517.47<br>410.78|U<br>16.54<br>71.88<br>182.20<br>U<br>27.29<br>93.35<br>197.97<br>U<br>26.00<br>96.81<br>176.96<br>U<br>29.15<br>76.87<br>188.60<br>U<br>37.14<br>94.72<br>179.60<br>U<br>22.86<br>84.46<br>244.80<br>U<br>33.29<br>116.76<br>180.10<br>U<br>9.57<br>42.96<br>197.31<br>U<br>7.79<br>25.75<br>171.29<br>U<br>6.07<br>36.85<br>174.20<br>U<br>108.14<br>96.16<br>180.45<br>U<br>24.79<br>109.86<br>209.70<br>C<br>15.22<br>83.35<br>177.40<br>C<br>265.84<br>116.69<br>188.70<br>C<br>385.13<br>118.58<br>191.70<br>C<br>634.93<br>164.80<br>232.56<br>C<br>519.88<br>397.32<br>220.10<br>C<br>844.45<br>154.68<br>175.10<br>C<br>10.22<br>83.98<br>180.44<br>C<br>194.83<br>228.07<br>293.60|



# 90 _CHAPTER 9. LINEAR COMPOSITIONAL MODELS_ 

## **Appendix A** 

## **a Plotting ternary diagram** 

Denote the three vertices of the ternary diagram counter-clockwise from the upper vertex as _A_ , _B_ and _C_ (see Figure A.1). The scale of the plot is arbitrary 

**==> picture [197 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.2<br>A=[u0+0.5, v0+3^0.5/2]<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>B=[u0,v0] C=[u0+1, v0]<br>0<br>0 0.2 0.4 0.6 0.8 1 1.2 1.4<br>u<br>v<br>**----- End of picture text -----**<br>


Figure A.1: Plot of the frame of a ternary diagram. The shift plotting coordinates are [ _u_ 0 _, v_ 0] = [0 _._ 2 _,_ 0 _._ 2], and the length of the side is 1. 

and a unitary equilateral triangle can be chosen. Assume that [ _u_ 0 _, v_ 0] are the plotting coordinates of the _B_ vertex. The _C_ vertex is then _C_ = [ _u_ 0 + 1 _, v_ 0]; and the vertex _A_ has abscissa _u_ 0 + 0 _._ 5 and the square-height is obtained using Pythagorean Theorem: 1[2] _−_ 0 _._ 5[2] = 3 _/_ 4. Then, the vertex _A_ = [ _u_ 0 + 0 _._ 5 _, v_ 0 + _√_ 3 _/_ 2]. These are the vertices of the triangle shown in Figure A.1, where the origin has been shifted to [ _u_ 0 _, v_ 0] in order to centre the plot. The figure is obtained plotting the segments _AB_ , _BC_ , _CA_ . 

To plot a sample point **x** = [ _x_ 1 _, x_ 2 _, x_ 3], closed to a constant _κ_ , the corresponding plotting coordinates [ _u, v_ ] are needed. They are obtained as a convex 

91 

_APPENDIX A. PLOTTING A TERNARY DIAGRAM_ 

92 

linear combination of the plotting coordinates of the vertices 

**==> picture [135 x 22] intentionally omitted <==**

with 

**==> picture [259 x 13] intentionally omitted <==**

Note that the coefficients of the convex linear combination must be closed to 1 as obtained dividing by _κ_ . Deformed ternary diagrams can be obtained just changing the plotting coordinates of the vertices and maintaining the convex linear combination. 

## **Appendix B Parametrisation of an elliptic region** 

To plot an ellipse in R[2] , and to plot its backtransform in the ternary diagram, we need to give to the plotting program a sequence of points that it can join by a smooth curve. This requires the points to be in a certain order, so that they can be joint consecutively. The way to do this is to use polar coordinates, as they allow to give a consecutive sequence of angles which will follow the border of the ellipse in one direction. The degree of approximation of the ellipse will depend on the number of points used for discretisation. 

The algorithm is based on the following reasoning. Imagine an ellipse located in R[2] with principal axes not parallel to the axes of the Cartesian coordinate system. What we have to do to express it in polar coordinates is (a) translate the ellipse to the origin; (b) rotate it in such a way that the principal axis of the ellipse coincide with the axis of the coordinate system; (c) stretch the axis corresponding to the shorter principal axis in such a way that the ellipse becomes a circle in the new coordinate system; (d) transform the coordinates into polar coordinates using the simple expressions _x[∗]_ = _r_ cos _ρ_ , _y[∗]_ = _r_ sin _ρ_ ; (e) undo all the previous steps in inverse order to obtain the expression of the original equation in terms of the polar coordinates. Although this might sound tedious and complicated, in fact we have results from matrix theory which tell us that this procedure can be reduced to a problem of eigenvalues and eigenvectors. 

In fact, any symmetric matrix can be decomposed into the matrix product _Q_ Λ _Q[′]_ , where Λ is the diagonal matrix of eigenvalues and _Q_ is the matrix of orthonormal eigenvectors associated with them. For _Q_ we have that _Q[′]_ = _Q[−]_[1] and therefore ( _Q[′]_ ) _[−]_[1] = _Q_ . This can be applied to either the first or the second options of the last section. 

In general, we are interested in ellipses whose matrix is related to the sample covariance matrix Σ,[ˆ] particularly its inverse. We have Σ[ˆ] _[−]_[1] = _Q_ Λ _[−]_[1] _Q[′]_ and substituting into the equation of the ellipse (7.1), (7.2): 

(¯ **x** _[∗] −_ _**µ**_ ) _Q_ Λ _[−]_[1] _Q[′]_ (¯ **x** _[∗] −_ _**µ**_ ) _[′]_ = ( _Q[′]_ (¯ **x** _[∗] −_ _**µ**_ ) _[′]_ ) _[′]_ Λ _[−]_[1] ( _Q[′]_ (¯ **x** _[∗] −_ _**µ**_ ) _[′]_ ) = _κ ,_ 

93 

_APPENDIX B. PARAMETRISATION OF AN ELLIPTIC REGION_ 

94 

where **x** ¯ _[∗]_ is the estimated centre or mean and _**µ**_ describes the ellipse. The vector _Q[′]_ (¯ **x** _[∗] −_ _**µ**_ ) _[′]_ corresponds to a rotation in real space in such a way, that the new coordinate axis are precisely the eigenvectors. Given that Λ is a diagonal matrix, the next step consists in writing Λ _[−]_[1] = Λ _[−]_[1] _[/]_[2] Λ _[−]_[1] _[/]_[2] , and we get: 

**==> picture [205 x 31] intentionally omitted <==**

This transformation is equivalent to a re-scaling of the basis vectors in such a way, that the ellipse becomes a circle of radius _[√] κ_ , which is easy to express in polar coordinates: 

**==> picture [315 x 25] intentionally omitted <==**

The parametrisation that we are looking for is thus given by: 

**==> picture [143 x 25] intentionally omitted <==**

Note that _Q_ Λ[1] _[/]_[2] is the upper triangular matrix of the Cholesky decomposition of Σ:[ˆ] 

**==> picture [195 x 13] intentionally omitted <==**

thus, from Σ =[ˆ] _UL_ and _L_ = _U[′]_ we get the condition: 

**==> picture [183 x 26] intentionally omitted <==**

which implies 

**==> picture [159 x 84] intentionally omitted <==**

and for each component of the vector _**µ**_ we obtain: 

**==> picture [199 x 53] intentionally omitted <==**

The points describing the ellipse in the simplex are ilr _[−]_[1] ( _**µ**_ ) (see Section 4.4). The procedures described apply to the three cases studied in section 7.2, just using the appropriate covariance matrix Σ.[ˆ] Finally, recall that _κ_ will be obtained from a chi-square distribution. 

## **Bibliography** 

- Aitchison, J. (1981). A new approach to null correlations of proportions. _Mathematical Geology 13_ (2), 175–189. 

- Aitchison, J. (1982). The statistical analysis of compositional data (with discussion). _Journal of the Royal Statistical Society, Series B (Statistical Methodology) 44_ (2), 139–177. 

- Aitchison, J. (1983). Principal component analysis of compositional data. _Biometrika 70_ (1), 57–65. 

- Aitchison, J. (1984). The statistical analysis of geochemical compositions. _Mathematical Geology 16_ (6), 531–564. 

- Aitchison, J. (1986). _The Statistical Analysis of Compositional Data_ . Monographs on Statistics and Applied Probability. Chapman & Hall Ltd., London (UK). (Reprinted in 2003 with additional material by The Blackburn Press). 416 p. 

- Aitchison, J. (1990). Relative variation diagrams for describing patterns of compositional variability. _Mathematical Geology 22_ (4), 487–511. 

- Aitchison, J. (1997). The one-hour course in compositional data analysis or compositional data analysis is simple. In V. Pawlowsky-Glahn (Ed.), _Proceedings of IAMG’97 — The third annual conference of the International Association for Mathematical Geology_ , Volume I, II and addendum, pp. 3–35. International Center for Numerical Methods in Engineering (CIMNE), Barcelona (E), 1100 p. 

- Aitchison, J. (2002). Simplicial inference. In M. A. G. Viana and D. S. P. Richards (Eds.), _Algebraic Methods in Statistics and Probability_ , Volume 287 of _Contemporary Mathematics Series_ , pp. 1–22. American Mathematical Society, Providence, Rhode Island (USA), 340 p. 

- Aitchison, J., C. Barcel´o-Vidal, J. J. Egozcue, and V. Pawlowsky-Glahn (2002). A concise guide for the algebraic-geometric structure of the simplex, the sample space for compositional data analysis. In U. Bayer, H. Burger, and W. Skala (Eds.), _Proceedings of IAMG’02 — The eigth annual conference of_ 

95 

_BIBLIOGRAPHY_ 

96 

_the International Association for Mathematical Geology_ , Volume I and II, pp. 387–392. Selbstverlag der Alfred-Wegener-Stiftung, Berlin, 1106 p. 

- Aitchison, J., C. Barcel´o-Vidal, J. A. Mart´ın-Fern´andez, and V. PawlowskyGlahn (2000). Logratio analysis and compositional distance. _Mathematical Geology 32_ (3), 271–275. 

- Aitchison, J. and J. J. Egozcue (2005). Compositional data analysis: where are we and where should we be heading? _Mathematical Geology 37_ (7), 829–850. 

- Aitchison, J. and M. Greenacre (2002). Biplots for compositional data. _Journal of the Royal Statistical Society, Series C (Applied Statistics) 51_ (4), 375–392. 

- Aitchison, J. and J. W. Kay (2003). Possible solution of some essential zero problems in compositional data analysis. See Thi´o-Henestrosa and Mart´ınFern´andez (2003). 

- Albar`ede, F. (1995). _Introduction to geochemical modeling_ . Cambridge University Press (UK). 543 p. 

- Anderson, T. W. (1984). _An introduction to multivariate statistical analysis_ . Second ed., John Wiley and Sons, New York, USA. 

- Bacon-Shone, J. (2003). Modelling structural zeros in compositional data. See Thi´o-Henestrosa and Mart´ın-Fern´andez (2003). 

- Barcel´o, C., V. Pawlowsky, and E. Grunsky (1994). Outliers in compositional data: a first approach. In C. J. Chung (Ed.), _Papers and extended abstracts of IAMG’94 — The First Annual Conference of the International Association for Mathematical Geology_ , Mont Tremblant, Qu´ebec, Canad´a, pp. 21–26. IAMG. 

- Barcel´o, C., V. Pawlowsky, and E. Grunsky (1996). Some aspects of transformations of compositional data and the identification of outliers. _Mathematical Geology 28_ (4), 501–518. 

- Barcel´o-Vidal, C., J. A. Mart´ın-Fern´andez, and V. Pawlowsky-Glahn (2001). Mathematical foundations of compositional data analysis. In G. Ross (Ed.), _Proceedings of IAMG’01 — The sixth annual conference of the International Association for Mathematical Geology_ , pp. 20 p. CD-ROM. 

- Billheimer, D., P. Guttorp, and W. Fagan (1997). Statistical analysis and interpretation of discrete compositional data. Technical report, NRCSE technical report 11, University of Washington, Seattle (USA), 48 p. 

- Billheimer, D., P. Guttorp, and W. Fagan (2001). Statistical interpretation of species composition. _Journal of the American Statistical Association 96_ (456), 1205–1214. 

_BIBLIOGRAPHY_ 

97 

- Box, G. E. P. and D. R. Cox (1964). The analysis of transformations. _Journal of the Royal Statistical Society, Series B (Statistical Methodology) 26_ (2), 211– 252. 

- Buccianti, A. and V. Pawlowsky-Glahn (2005). New perspectives on water chemistry and compositional data analysis. _Mathematical Geology 37_ (7), 703– 727. 

- Buccianti, A., V. Pawlowsky-Glahn, C. Barcel´o-Vidal, and E. Jarauta-Bragulat (1999). Visualization and modeling of natural trends in ternary diagrams: a geochemical case study. See Lippard et al. (1999), pp. 139–144. 

- Chayes, F. (1960). On correlation between variables of constant sum. _Journal of Geophysical Research 65_ (12), 4185–4193. 

- Chayes, F. (1971). _Ratio Correlation_ . University of Chicago Press, Chicago, IL (USA). 99 p. 

- Coakley, J. P. and B. R. Rust (1968). Sedimentation in an Arctic lake. _Journal of Sedimentary Petrology 38_ , 1290–1300. 

- Eaton, M. L. (1983). _Multivariate Statistics. A Vector Space Approach_ . John Wiley & Sons. 

- Egozcue, J. J. (2009). Reply to ”On the Harker variation diagrams; ...” by J. A. Cort´es. _Mathematical Geosciences 41_ (7), 829–834. 

- Egozcue, J. J. and V. Pawlowsky-Glahn (2005). Groups of parts and their balances in compositional data analysis. _Mathematical Geology 37_ (7), 795– 828. 

- Egozcue, J. J. and V. Pawlowsky-Glahn (2006). Exploring compositional data with the coda-dendrogram. In E. Pirard (Ed.), _Proceedings of IAMG’06 — The XIth annual conference of the International Association for Mathematical Geology_ . 

- Egozcue, J. J., V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barcel´o-Vidal (2003). Isometric logratio transformations for compositional data analysis. _Mathematical Geology 35_ (3), 279–300. 

- Fahrmeir, L. and A. Hamerle (Eds.) (1984). _Multivariate Statistische Verfahren_ . Walter de Gruyter, Berlin (D), 796 p. 

- Fry, J. M., T. R. L. Fry, and K. R. McLaren (1996). Compositional data analysis and zeros in micro data. Centre of Policy Studies (COPS), General Paper No. G-120, Monash University. 

- Gabriel, K. R. (1971). The biplot — graphic display of matrices with application to principal component analysis. _Biometrika 58_ (3), 453–467. 

_BIBLIOGRAPHY_ 

98 

- Galton, F. (1879). The geometric mean, in vital and social statistics. _Proceedings of the Royal Society of London 29_ , 365–366. 

- Krzanowski, W. J. (1988). _Principles of Multivariate Analysis: A user’s perspective_ , Volume 3 of _Oxford Statistical Science Series_ . Clarendon Press, Oxford (UK). 563 p. 

- Krzanowski, W. J. and F. H. C. Marriott (1994). _Multivariate Analysis, Part 2 - Classification, covariance structures and repeated measurements_ , Volume 2 of _Kendall’s Library of Statistics_ . Edward Arnold, London (UK). 280 p. 

- Lippard, S. J., A. Næss, and R. Sinding-Larsen (Eds.) (1999). _Proceedings of IAMG’99 — The fifth annual conference of the International Association for Mathematical Geology_ , Volume I and II. Tapir, Trondheim (N), 784 p. 

- Mardia, K. V., J. T. Kent, and J. M. Bibby (1979). _Multivariate Analysis_ . Academic Press, London (GB). 518 p. 

- Mart´ın-Fern´andez, J., C. Barcel´o-Vidal, and V. Pawlowsky-Glahn (1998). A critical approach to non-parametric classification of compositional data. In A. Rizzi, M. Vichi, and H.-H. Bock (Eds.), _Advances in Data Science and Classification (Proceedings of the 6th Conference of the International Federation of Classification Societies (IFCS’98), Universit`a “La Sapienza”, Rome, 21–24 July_ , pp. 49–56. Springer-Verlag, Berlin (D), 677 p. 

- Mart´ın-Fern´andez, J. A. (2001). _Medidas de diferencia y clasificaci´on no param´etrica de datos composicionales_ . Ph. D. thesis, Universitat Polit`ecnica de Catalunya, Barcelona (E). 

- Mart´ın-Fern´andez, J. A., C. Barcel´o-Vidal, and V. Pawlowsky-Glahn (2000). Zero replacement in compositional data sets. In H. Kiers, J. Rasson, P. Groenen, and M. Shader (Eds.), _Studies in Classification, Data Analysis, and Knowledge Organization (Proceedings of the 7th Conference of the International Federation of Classification Societies (IFCS’2000), University of Namur, Namur, 11-14 July_ , pp. 155–160. Springer-Verlag, Berlin (D), 428 p. 

- Mart´ın-Fern´andez, J. A., C. Barcel´o-Vidal, and V. Pawlowsky-Glahn (2003). Dealing with zeros and missing values in compositional data sets using nonparametric imputation. _Mathematical Geology 35_ (3), 253–278. 

- Mart´ın-Fern´andez, J. A., M. Bren, C. Barcel´o-Vidal, and V. Pawlowsky-Glahn (1999). A measure of difference for compositional data based on measures of divergence. See Lippard et al. (1999), pp. 211–216. 

- Mateu-Figueras, G. (2003). _Models de distribuci´o sobre el s´ımplex_ . Ph. D. thesis, Universitat Polit`ecnica de Catalunya, Barcelona, Spain. 

- McAlister, D. (1879). The law of the geometric mean. _Proceedings of the Royal Society of London 29_ , 367–376. 

_BIBLIOGRAPHY_ 

99 

- Mosimann, J. E. (1962). On the compound multinomial distribution, the multivariate _β_ -distribution and correlations among proportions. _Biometrika 49_ (12), 65–82. 

- Otero, N., R. Tolosana-Delgado, and A. Soler (2003). A factor analysis of hidrochemical composition of Llobregat river basin. See Thi´o-Henestrosa and Mart´ın-Fern´andez (2003). 

- Otero, N., R. Tolosana-Delgado, A. Soler, V. Pawlowsky-Glahn, and A. Canals (2005). Relative vs. absolute statistical analysis of compositions: a comparative study of surface waters of a mediterranean river. _Water Research Vol 39_ (7), 1404–1414. 

- Pawlowsky-Glahn, V. (2003). Statistical modelling on coordinates. See Thi´oHenestrosa and Mart´ın-Fern´andez (2003). 

- Pawlowsky-Glahn, V. and A. Buccianti (2002). Visualization and modeling of subpopulations of compositional data: statistical methods illustrated by means of geochemical data from fumarolic fluids. _International Journal of Earth Sciences (Geologische Rundschau) 91_ (2), 357–368. 

- Pawlowsky-Glahn, V. and J. J. Egozcue (2001). Geometric approach to statistical analysis on the simplex. _Stochastic Environmental Research and Risk Assessment (SERRA) 15_ (5), 384–398. 

- Pawlowsky-Glahn, V. and J. J. Egozcue (2002). BLU estimators and compositional data. _Mathematical Geology 34_ (3), 259–274. 

- Pawlowsky-Glahn, V. and J. J. Egozcue (2006). Anlisis de datos composicionales con el coda-dendrograma. In J. Sicilia-Rodr´ıguez, C. Gonz´alez-Mart´ın, M. A. Gonz´alez-Sierra, and D. Alcaide (Eds.), _Actas del XXIX Congreso de la Sociedad de Estad´ıstica e Investigaci´on Operativa (SEIO’06)_ , pp. 39–40. Sociedad de Estad´ıstica e Investigaci´on Operativa, Tenerife (ES), CD-ROM. 

- Pe˜na, D. (2002). _An´alisis de datos multivariantes_ . McGraw Hill. 539 p. 

- Pearson, K. (1897). Mathematical contributions to the theory of evolution. on a form of spurious correlation which may arise when indices are used in the measurement of organs. _Proceedings of the Royal Society of London LX_ , 489–502. 

- Richter, D. H. and J. G. Moore (1966). Petrology of the Kilauea Iki lava lake, Hawaii. U.S. Geol. Surv. Prof. Paper 537-B, B1-B26, cited in Rollinson (1995). 

- Rollinson, H. R. (1995). _Using geochemical data: Evaluation, presentation, interpretation_ . Longman Geochemistry Series, Longman Group Ltd., Essex (UK). 352 p. 

- Sarmanov, O. V. and A. B. Vistelius (1959). On the correlation of percentage values. _Doklady of the Academy of Sciences of the USSR – Earth Sciences Section 126_ , 22–25. 

_BIBLIOGRAPHY_ 

100 

Solano-Acosta, W. and P. K. Dutta (2005). Unexpected trend in the compositional maturity of second-cycle sand. _Sedimentary Geology 178_ (3-4), 275–283. 

- Thi´o-Henestrosa, S. and J. A. Mart´ın-Fern´andez (Eds.) (2003). _Compositional Data Analysis Workshop – CoDaWork’03, Proceedings_ . Universitat de Girona, ISBN 84-8458-111-X, http://ima.udg.es/Activitats/CoDaWork03/. 

- Thi´o-Henestrosa, S. and J. A. Mart´ın-Fern´andez (2005). Dealing with compositional data: the freeware codapack. _Mathematical Geology 37_ (7), 773–793. 

- Thi´o-Henestrosa, S., R. Tolosana-Delgado, and O. G´omez (2005). New features of codapack—a compositional data package. Volume 2, pp. 1171–1178. 

- Tolosana-Delgado, R., N. Otero, V. Pawlowsky-Glahn, and A. Soler (2005). Latent compositional factors in the Llobregat river basin (Spain) hydrogeoeochemistry. _Mathematical Geology 37_ (7), 681–702. 

- van den Boogaart, G. and R. Tolosana-Delgado (2005). A compositional data analysis package for R providing multiple approaches. In G. MateuFigueras and C. Barcel´o-Vidal (Eds.), _Compositional Data Analysis Workshop – CoDaWork’05, Proceedings_ . Universitat de Girona, ISBN 84-8458-222-1, http://ima.udg.es/Activitats/CoDaWork05/. 

- van den Boogaart, K. G. and R. Tolosana-Delgado (2008). “compositions”: a unified R package to analyze compositional data. _Computers & Geosciences 34_ (4), 320–338. 

- von Eynatten, H., V. Pawlowsky-Glahn, and J. J. Egozcue (2002). Understanding perturbation on the simplex: a simple method to better visualise and interpret compositional data in ternary diagrams. _Mathematical Geology 34_ (3), 249–257. 

