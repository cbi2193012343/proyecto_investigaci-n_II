## _An Introduction to Measure Theory_ 

## Terence Tao 

This is a preliminary version of the book _**An Introduction to Measure Theory**_ published by the American Mathematical Society (AMS). This preliminary version is made available with the permission of the AMS and may not be changed, edited, or reposted at any other website without explicit written permission from the author and the AMS. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

To Garth Gaudry, who set me on the road; To my family, for their constant support; And to the readers of my blog, for their feedback and contributions. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

## **Contents** 

|Preface||ix|
|---|---|---|
|Notation||x|
|Acknowledgments||xvi|
|Chapter|1.<br>Measure theory|1|
|_§_1.1.|Prologue: The problem of measure|2|
|_§_1.2.|Lebesgue measure|17|
|_§_1.3.|The Lebesgue integral|46|
|_§_1.4.|Abstract measure spaces|79|
|_§_1.5.|Modes of convergence|114|
|_§_1.6.|Diferentiation theorems|131|
|_§_1.7.|Outer measures, pre-measures, and product measures|179|
|Chapter|2.<br>Related articles|209|
|_§_2.1.|Problem solving strategies|210|
|_§_2.2.|The Rademacher diferentiation theorem|226|
|_§_2.3.|Probability spaces|232|
|_§_2.4.|Infnite product spaces and the Kolmogorov extension||
||theorem|235|
|Bibliography||243|
|||vii|



Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

|viii|**Contents**|
|---|---|
|Index|245|



Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

## **Preface** 

In the fall of 2010, I taught an introductory one-quarter course on graduate real analysis, focusing in particular on the basics of measure and integration theory, both in Euclidean spaces and in abstract measure spaces. This text is based on my lecture notes of that course, which are also available online on my blog `terrytao.wordpress.com` , together with some supplementary material, such as a section on problem solving strategies in real analysis (Section 2.1) which evolved from discussions with my students. 

This text is intended to form a prequel to my graduate text [ **Ta2010** ] (henceforth referred to as _An epsilon of room, Vol. I_ ), which is an introduction to the analysis of Hilbert and Banach spaces (such as _L[p]_ and Sobolev spaces), point-set topology, and related topics such as Fourier analysis and the theory of distributions; together, they serve as a text for a complete first-year graduate course in real analysis. 

The approach to measure theory here is inspired by the text [ **StSk2005** ], which was used as a secondary text in my course. In particular, the first half of the course is devoted almost exclusively to measure theory on Euclidean spaces **R** _[d]_ (starting with the more elementary Jordan-Riemann-Darboux theory, and only then moving on to the more sophisticated Lebesgue theory), deferring the abstract aspects of measure theory to the second half of the course. I found 

ix 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Preface** 

x 

that this approach strengthened the student’s intuition in the early stages of the course, and helped provide motivation for more abstract constructions, such as Carath´eodory’s general construction of a measure from an outer measure. 

Most of the material here is self-contained, assuming only an undergraduate knowledge in real analysis (and in particular, on the Heine-Borel theorem, which we will use as the foundation for our construction of Lebesgue measure); a secondary real analysis text can be used in conjunction with this one, but it is not strictly necessary. A small number of exercises however will require some knowledge of point-set topology or of set-theoretic concepts such as cardinals and ordinals. 

A large number of exercises are interspersed throughout the text, and it is intended that the reader perform a significant fraction of these exercises while going through the text. Indeed, many of the key results and examples in the subject will in fact be presented through the exercises. In my own course, I used the exercises as the basis for the examination questions, and signalled this well in advance, to encourage the students to attempt as many of the exercises as they could as preparation for the exams. 

The core material is contained in Chapter 1, and already comprises a full quarter’s worth of material. Section 2.1 is a much more informal section than the rest of the book, focusing on describing problem solving strategies, either specific to real analysis exercises, or more generally applicable to a wider set of mathematical problems; this section evolved from various discussions with students throughout the course. The remaining three sections in Chapter 2 are optional topics, which require understanding of most of the material in Chapter 1 as a prerequisite (although Section 2.3 can be read after completing Section 1.4. 

## **Notation** 

For reasons of space, we will not be able to define every single mathematical term that we use in this book. If a term is italicised for reasons other than emphasis or for definition, then it denotes a standard mathematical object, result, or concept, which can be easily 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Notation** 

xi 

looked up in any number of references. (In the blog version of the book, many of these terms were linked to their Wikipedia pages, or other on-line reference pages.) 

Given a subset _E_ of a space _X_ , the _indicator function_ 1 _E_ : _X →_ **R** is defined by setting 1 _E_ ( _x_ ) equal to 1 for _x ∈ E_ and equal to 0 for _x ̸∈ E_ . 

For any natural number _d_ , we refer to the vector space **R** _[d]_ := _{_ ( _x_ 1 _, . . . , xd_ ) : _x_ 1 _, . . . , xd ∈_ **R** _}_ as _(d-dimensional) Euclidean space_ . A vector ( _x_ 1 _, . . . , xd_ ) in **R** _[d]_ has length 

**==> picture [149 x 12] intentionally omitted <==**

and two vectors ( _x_ 1 _, . . . , xd_ ) _,_ ( _y_ 1 _, . . . , yd_ ) have _dot product_ 

**==> picture [202 x 11] intentionally omitted <==**

The _extended non-negative real axis_ [0 _,_ + _∞_ ] is the non-negative real axis [0 _,_ + _∞_ ) := _{x ∈_ **R** : _x ≥_ 0 _}_ with an additional element adjointed to it, which we label + _∞_ ; we will need to work with this system because many sets (e.g. **R** _[d]_ ) will have infinite measure. Of course, + _∞_ is not a real number, but we think of it as an _extended_ real number. We extend the addition, multiplication, and order structures on [0 _,_ + _∞_ ) to [0 _,_ + _∞_ ] by declaring 

**==> picture [116 x 8] intentionally omitted <==**

for all _x ∈_ [0 _,_ + _∞_ ], 

**==> picture [106 x 8] intentionally omitted <==**

for all non-zero _x ∈_ (0 _,_ + _∞_ ], 

**==> picture [96 x 10] intentionally omitted <==**

and 

**==> picture [124 x 11] intentionally omitted <==**

Most of the laws of algebra for addition, multiplication, and order continue to hold in this extended number system; for instance addition and multiplication are commutative and associative, with the latter distributing over the former, and an order relation _x ≤ y_ is preserved under addition or multiplication of both sides of that relation by the same quantity. However, we caution that the laws of 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Preface** 

xii 

cancellation do _not_ apply once some of the variables are allowed to be infinite; for instance, we cannot deduce _x_ = _y_ from + _∞_ + _x_ = + _∞_ + _y_ or from + _∞· x_ = + _∞· y_ . This is related to the fact that the forms + _∞−_ + _∞_ and + _∞/_ + _∞_ are indeterminate (one cannot assign a value to them without breaking a lot of the rules of algebra). A general rule of thumb is that if one wishes to use cancellation (or proxies for cancellation, such as subtraction or division), this is only safe if one can guarantee that all quantities involved are finite (and in the case of multiplicative cancellation, the quantity being cancelled also needs to be non-zero, of course). However, as long as one avoids using cancellation and works exclusively with non-negative quantities, there is little danger in working in the extended real number system. 

We note also that once one adopts the convention + _∞·_ 0 = 0 _·_ + _∞_ = 0, then multiplication becomes _upward continuous_ (in the sense that whenever _xn ∈_ [0 _,_ + _∞_ ] increases to _x ∈_ [0 _,_ + _∞_ ], and _yn ∈_ [0 _,_ + _∞_ ] increases to _y ∈_ [0 _,_ + _∞_ ], then _xnyn_ increases to _xy_ ) but not _downward continuous_ (e.g. 1 _/n →_ 0 but 1 _/n ·_ + _∞̸→_ 0 _·_ + _∞_ ). This asymmetry will ultimately cause us to define integration from below rather than from above, which leads to other asymmetries (e.g. the monotone convergence theorem (Theorem 1.4.44) applies for monotone increasing functions, but not necessarily for monotone decreasing ones). 

**Remark 0.0.1.** Note that there is a tradeoff here: if one wants to keep as many useful laws of algebra as one can, then one can add in infinity, or have negative numbers, but it is difficult to have both at the same time. Because of this tradeoff, we will see two overlapping types of measure and integration theory: the _non-negative_ theory, which involves quantities taking values in [0 _,_ + _∞_ ], and the _absolutely integrable_ theory, which involves quantities taking values in ( _−∞,_ + _∞_ ) or **C** . For instance, the fundamental convergence theorem for the former theory is the monotone convergence theorem (Theorem 1.4.44), while the fundamental convergence theorem for the latter is the dominated convergence theorem (Theorem 1.4.49). Both branches of the theory are important, and both will be covered in later notes. 

One important feature of the extended nonnegative real axis is that all sums are convergent: given any sequence _x_ 1 _, x_ 2 _, . . . ∈_ [0 _,_ + _∞_ ], 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

xiii 

## **Notation** 

we can always form the sum 

**==> picture [74 x 28] intentionally omitted <==**

as the limit of the partial sums[�] _[N] n_ =1 _[x][n]_[,][which][may][be][either][finite] or infinite. An equivalent definition of this infinite sum is as the supremum of all finite subsums: 

**==> picture [128 x 28] intentionally omitted <==**

Motivated by this, given any collection ( _xα_ ) _α∈A_ of numbers _xα ∈_ [0 _,_ + _∞_ ] indexed by an arbitrary set _A_ (finite or infinite, countable or uncountable), we can define the sum[�] _α∈A[x][α]_[by][the][formula] 

**==> picture [215 x 23] intentionally omitted <==**

Note from this definition that one can relabel the collection in an arbitrary fashion without affecting the sum; more precisely, given any bijection _φ_ : _B → A_ , one has the change of variables formula 

**==> picture [193 x 24] intentionally omitted <==**

Note that when dealing with signed sums, the above rearrangement identity can fail when the series is not absolutely convergent (cf. the _Riemann rearrangement theorem_ ). 

**Exercise 0.0.1.** If ( _xα_ ) _α∈A_ is a collection of numbers _xα ∈_ [0 _,_ + _∞_ ] such that[�] _α∈A[x][α][<][∞]_[,][show][that] _[x][α]_[=][0][for][all][but][at][most] countably many _α ∈ A_ , even if _A_ itself is uncountable. 

We will rely frequently on the following basic fact (a special case of the _Fubini-Tonelli theorem_ , Corollary 1.7.23): 

**Theorem 0.0.2** (Tonelli’s theorem for series) **.** _Let_ ( _xn,m_ ) _n,m∈_ **N** _be a doubly infinite sequence of extended non-negative reals xn,m ∈_ [0 _,_ + _∞_ ] _. Then_ 

**==> picture [202 x 31] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Preface** 

xiv 

Informally, Tonelli’s theorem asserts that we may rearrange infinite series with impunity as long as all summands are non-negative. 

**Proof.** We shall just show the equality of the first and second expressions; the equality of the first and third is proven similarly. 

We first show that 

**==> picture [132 x 31] intentionally omitted <==**

Let _F_ be any finite subset of **N**[2] . Then _F ⊂{_ 1 _, . . . , N } × {_ 1 _, . . . , N }_ for some finite _N_ , and thus (by the non-negativity of the _xn,m_ ) 

**==> picture [188 x 25] intentionally omitted <==**

The right-hand side can be rearranged as 

**==> picture [60 x 30] intentionally omitted <==**

which is clearly at most[�] _[∞] n_ =1 � _∞m_ =1 _[x][n,m]_[(again][by][non-negativity] of _xn,m_ ). This gives 

**==> picture [128 x 30] intentionally omitted <==**

for any finite subset _F_ of **N**[2] , and the claim then follows from (0.1). 

It remains to show the reverse inequality 

**==> picture [132 x 30] intentionally omitted <==**

It to show that 

**==> picture [129 x 32] intentionally omitted <==**

for each _N_ . 

Fix _N_ . As each[�] _[∞] m_ =1 _[x][n,m]_[is][the][limit][of][�] _[M] m_ =1 _[x][n,m]_[,][the][left-] hand side is the limit of[�] _[N] n_ =1 � _Mm_ =1 _[x][n,m]_[as] _[M][→∞]_[.] Thus it 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

xv 

## **Notation** 

to show that 

**==> picture [129 x 32] intentionally omitted <==**

for each finite _M_ . But the left-hand side is[�] ( _n,m_ ) _∈{_ 1 _,...,N }×{_ 1 _,...,M }[x][n,m]_[,] and the claim follows. □ 

**Remark 0.0.3.** Note how important it was that the _xn,m_ were nonnegative in the above argument. In the signed case, one needs an additional assumption of absolute summability of _xn,m_ on **N**[2] before one is permitted to interchange sums; this is _Fubini’s theorem for series_ , which we will encounter later in this text. Without absolute summability or non-negativity hypotheses, the theorem can fail (consider for instance the case when _xn,m_ equals +1 when _n_ = _m_ , _−_ 1 when _n_ = _m_ + 1, and 0 otherwise). 

**Exercise 0.0.2** (Tonelli’s theorem for series over arbitrary sets) **.** Let _A, B_ be sets (possibly infinite or uncountable), and ( _xn,m_ ) _n∈A,m∈B_ be a doubly infinite sequence of extended non-negative reals _xn,m ∈_ [0 _,_ + _∞_ ] indexed by _A_ and _B_ . Show that 

**==> picture [214 x 24] intentionally omitted <==**

( _Hint:_ although not strictly necessary, you may find it convenient to first establish the fact that if[�] _n∈A[x][n]_[is][finite,][then] _[x][n]_[is][non-zero] for at most countably many _n_ .) 

Next, we recall the _axiom of choice_ , which we shall be assuming throughout the text: 

**Axiom 0.0.4** (Axiom of choice) **.** _Let_ ( _Eα_ ) _α∈A be a family of nonempty sets Eα, indexed by an index set A. Then we can find a family_ ( _xα_ ) _α∈A of elements xα of Eα, indexed by the same set A._ 

This axiom is trivial when _A_ is a singleton set, and from mathematical induction one can also prove it without difficulty when _A_ is finite. However, when _A_ is infinite, one cannot deduce this axiom from the other axioms of set theory, but must explicitly add it to the list of axioms. We isolate the countable case as a particularly useful 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Preface** 

xvi 

corollary (though one which is strictly weaker than the full axiom of choice): 

**Corollary 0.0.5** (Axiom of countable choice) **.** _Let E_ 1 _, E_ 2 _, E_ 3 _, . . . be a sequence of non-empty sets. Then one can find a sequence x_ 1 _, x_ 2 _, . . . such that xn ∈ En for all n_ = 1 _,_ 2 _,_ 3 _, . . .._ 

**Remark 0.0.6.** The question of how much of real analysis still survives when one is not permitted to use the axiom of choice is a delicate one, involving a fair amount of logic and descriptive set theory to answer. We will not discuss these matters in this text. We will however note a theorem of G¨odel[ **Go1938** ] that states that any statement that can be phrased in the first-order language of _Peano arithmetic_ , and which is proven with the axiom of choice, can also be proven without the axiom of choice. So, roughly speaking, G¨odel’s theorem tells us that for any “finitary” application of real analysis (which includes most of the “practical” applications of the subject), it is safe to use the axiom of choice; it is only when asking questions about “infinitary” objects that are beyond the scope of Peano arithmetic that one can encounter statements that are provable using the axiom of choice, but are not provable without it. 

## **Acknowledgments** 

This text was strongly influenced by the real analysis text of Stein and Shakarchi[ **StSk2005** ], which was used as a secondary text when teaching the course on which these notes were based. In particular, the strategy of focusing first on Lebesgue measure and Lebesgue integration, before moving onwards to abstract measure and integration theory, was directly inspired by the treatment in [ **StSk2005** ], and the material on differentiation theorems also closely follows that in [ **StSk2005** ]. On the other hand, our discussion here differs from that in [ **StSk2005** ] in other respects; for instance, a far greater emphasis is placed on Jordan measure and the Riemann integral as being an elementary precursor to Lebesgue measure and the Lebesgue integral. 

I am greatly indebted to my students of the course on which this text was based, as well as many further commenters on my blog, including Maria Alfonseca, Marco Angulo, J. Balachandran, 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

xvii 

## **Acknowledgments** 

Farzin Barekat, Marek Bern´at, Lewis Bowen, Chris Breeden, Danny Calegari, Yu Cao, Chandrasekhar, David Chang, Nick Cook, Damek Davis, Eric Davis, Marton Eekes, Wenying Gan, Nick Gill, Ulrich Groh, Tim Gowers, Laurens Gunnarsen, Tobias Hagge, Xueping Huang, Bo Jacoby, Apoorva Khare, Shiping Liu, Colin McQuillan, David Milovich, Hossein Naderi, Brent Nelson, Constantin Niculescu, Mircea Petrache, Walt Pohl, Jim Ralston, David Roberts, Mark Schwarzmann, Vladimir Slepnev, David Speyer, Blake Stacey, Tim Sullivan, Jonathan Weinstein, Duke Zhang, Lei Zhang, Pavel Zorin, and several anonymous commenters, for providing corrections and useful commentary on the material here. These comments can be viewed online at 

```
terrytao.wordpress.com/category/teaching/245a-real-analysis
```

The author is supported by a grant from the MacArthur Foundation, by NSF grant DMS-0649473, and by the NSF Waterman award. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Chapter 1 

## **Measure theory** 

1 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

2 

## **1.1. Prologue: The problem of measure** 

One of the most fundamental concepts in Euclidean geometry is that of the _measure m_ ( _E_ ) of a solid body _E_ in one or more dimensions. In one, two, and three dimensions, we refer to this measure as the _length_ , _area_ , or _volume_ of _E_ respectively. In the classical approach to geometry, the measure of a body was often computed by partitioning that body into finitely many components, moving around each component by a rigid motion (e.g. a translation or rotation), and then reassembling those components to form a simpler body which presumably has the same area. One could also obtain lower and upper bounds on the measure of a body by computing the measure of some inscribed or circumscribed body; this ancient idea goes all the way back to the work of Archimedes at least. Such arguments can be justified by an appeal to geometric intuition, or simply by postulating the existence of a measure _m_ ( _E_ ) that can be assigned to all solid bodies _E_ , and which obeys a collection of geometrically reasonable axioms. One can also justify the concept of measure on “physical” or “reductionistic” grounds, viewing the measure of a macroscopic body as the sum of the measures of its microscopic components. 

With the advent of _analytic geometry_ , however, Euclidean geometry became reinterpreted as the study of Cartesian products **R** _[d]_ of the real line **R** . Using this analytic foundation rather than the classical geometrical one, it was no longer intuitively obvious how to define the measure _m_ ( _E_ ) of a general[1] subset _E_ of **R** _[d]_ ; we will refer to this (somewhat vaguely defined) problem of writing down the “correct” definition of measure as the _problem of measure_ . 

To see why this problem exists at all, let us try to formalise some of the intuition for measure discussed earlier. The physical intuition of defining the measure of a body _E_ to be the sum of the measure of its component “atoms” runs into an immediate problem: a typical solid body would consist of an infinite (and uncountable) number of points, each of which has a measure of zero; and the product _∞·_ 0 is indeterminate. To make matters worse, two bodies that have exactly 

1One can also pose the problem of measure on other domains than Euclidean space, such as a Riemannian manifold, but we will focus on the Euclidean case here for simplicity, and refer to any text on Riemannian geometry for a treatment of integration on manifolds. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

3 

the same number of points, need not have the same measure. For instance, in one dimension, the intervals _A_ := [0 _,_ 1] and _B_ := [0 _,_ 2] are in one-to-one correspondence (using the bijection _x �→_ 2 _x_ from _A_ to _B_ ), but of course _B_ is twice as long as _A_ . So one can disassemble _A_ into an uncountable number of points and reassemble them to form a set of twice the length. 

Of course, one can point to the infinite (and uncountable) number of components in this disassembly as being the cause of this breakdown of intuition, and restrict attention to just finite partitions. But one still runs into trouble here for a number of reasons, the most striking of which is the _Banach-Tarski paradox_ , which shows that the unit ball _B_ := _{_ ( _x, y, z_ ) _∈_ **R**[3] : _x_[2] + _y_[2] + _z_[2] _≤_ 1 _}_ in three dimensions[2] can be disassembled into a finite number of pieces (in fact, just five pieces suffice), which can then be reassembled (after translating and rotating each of the pieces) to form two disjoint copies of the ball _B_ . 

Here, the problem is that the pieces used in this decomposition are highly pathological in nature; among other things, their construction requires use of the _axiom of choice_ . (This is in fact necessary; there are models of set theory without the axiom of choice in which the Banach-Tarski paradox does not occur, thanks to a famous theorem of Solovay[ **So1970** ].) Such pathological sets almost never come up in practical applications of mathematics. Because of this, the standard solution to the problem of measure has been to abandon the goal of measuring _every_ subset _E_ of **R** _[d]_ , and instead to settle for only measuring a certain subclass of “non-pathological” subsets of **R** _[d]_ , which are then referred to as the _measurable sets_ . The problem of measure then divides into several subproblems: 

- (i) What does it mean for a subset _E_ of **R** _[d]_ to be measurable? 

- (ii) If a set _E_ is measurable, how does one define its measure? 

- (iii) What nice properties or axioms does measure (or the concept of measurability) obey? 

> 2The paradox only works in three dimensions and higher, for reasons having to do with the group-theoretic property of _amenability_ ; see _§_ 2.2 of _An epsilon of room, Vol. I_ for further discussion. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

4 

- (iv) Are “ordinary” sets such as cubes, balls, polyhedra, etc. measurable? 

- (v) Does the measure of an “ordinary” set equal the “naive geometric measure” of such sets? (e.g. is the measure of an _a × b_ rectangle equal to _ab_ ?) 

These questions are somewhat open-ended in formulation, and there is no unique answer to them; in particular, one can expand the class of measurable sets at the expense of losing one or more nice properties of measure in the process (e.g. finite or countable additivity, translation invariance, or rotation invariance). However, there are two basic answers which, between them, suffice for most applications. The first is the concept of _Jordan measure_ (or _Jordan content_ ) of a Jordan measurable set, which is a concept closely related to that of the _Riemann integral_ (or _Darboux integral_ ). This concept is elementary enough to be systematically studied in an undergraduate analysis course, and suffices for measuring most of the “ordinary” sets (e.g. the area under the graph of a continuous function) in many branches of mathematics. However, when one turns to the type of sets that arise in _analysis_ , and in particular those sets that arise as _limits_ (in various senses) of other sets, it turns out that the Jordan concept of measurability is not quite adequate, and must be extended to the more general notion of _Lebesgue measurability_ , with the corresponding notion of _Lebesgue measure_ that extends Jordan measure. With the Lebesgue theory (which can be viewed as a _completion_ of the Jordan-Darboux-Riemann theory), one keeps almost all of the desirable properties of Jordan measure, but with the crucial additional property that many features of the Lebesgue theory are preserved under limits (as exemplified in the fundamental _convergence theorems_ of the Lebesgue theory, such as the _monotone convergence theorem_ (Theorem 1.4.44) and the _dominated convergence theorem_ (Theorem 1.4.49), which do not hold in the Jordan-Darboux-Riemann setting). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

5 

As such, they are particularly well suited[3] for applications in analysis, where limits of functions or sets arise all the time. 

In later sections, we will formally define Lebesgue measure and the Lebesgue integral, as well as the more general concept of an abstract measure space and the associated integration operation. In the rest of the current section, we will discuss the more elementary concepts of Jordan measure and the Riemann integral. This material will eventually be superceded by the more powerful theory to be treated in later sections; but it will serve as motivation for that later material, as well as providing some continuity with the treatment of measure and integration in undergraduate analysis courses. 

**1.1.1. Elementary measure.** Before we discuss Jordan measure, we discuss the even simpler notion of _elementary measure_ , which allows one to measure a very simple class of sets, namely the _elementary sets_ (finite unions of boxes). 

**Definition 1.1.1** (Intervals, boxes, elementary sets) **.** An _interval_ is a subset of **R** of the form [ _a, b_ ] := _{x ∈_ **R** : _a ≤ x ≤ b}_ , [ _a, b_ ) := _{x ∈_ **R** : _a ≤ x < b}_ , ( _a, b_ ] := _{x ∈_ **R** : _a < x ≤ b}_ , or ( _a, b_ ) := _{x ∈_ **R** : _a < x < b}_ , where _a ≤ b_ are real numbers. We define the _length_[4] _|I|_ of an interval _I_ = [ _a, b_ ] _,_ [ _a, b_ ) _,_ ( _a, b_ ] _,_ ( _a, b_ ) to be _|I|_ := _b − a_ . A _box_ in **R** _[d]_ is a Cartesian product _B_ := _I_ 1 _× . . . × Id_ of _d_ intervals _I_ 1 _, . . . , Id_ (not necessarily of the same length), thus for instance an interval is a one-dimensional box. The _volume |B|_ of such a box _B_ is defined as _|B|_ := _|I_ 1 _| × . . . × |Id|_ . An _elementary set_ is any subset of **R** _[d]_ which is the union of a finite number of boxes. **Exercise 1.1.1** (Boolean closure) **.** Show that if _E, F ⊂_ **R** _[d]_ are elementary sets, then the union _E ∪ F_ , the intersection _E ∩ F_ , and the set theoretic difference _E\F_ := _{x ∈ E_ : _x ̸∈ F }_ , and the symmetric difference _E_ ∆ _F_ := ( _E\F_ ) _∪_ ( _F \E_ ) are also elementary. If _x ∈_ **R** _[d]_ , show that the translate _E_ + _x_ := _{y_ + _x_ : _y ∈ E}_ is also an elementary set. 

3There are other ways to extend Jordan measure and the Riemann integral, see for instance Exercise 1.6.53 or Section 1.7.3, but the Lebesgue approach handles limits and rearrangement better than the other alternatives, and so has become the standard approach in analysis; it is also particularly well suited for providing the rigorous foundations of probability theory, as discussed in Section 2.3. 4Note we allow degenerate intervals of zero length. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

6 

We now give each elementary set a measure. 

**Lemma 1.1.2** (Measure of an elementary set) **.** _Let E ⊂_ **R** _[d] be an elementary set._ 

- (i) _E can be expressed as the finite union of_ disjoint _boxes._ 

- (ii) _If E is partitioned as the finite union B_ 1 _∪. . .∪Bk of disjoint boxes, then the quantity m_ ( _E_ ) := _|B_ 1 _|_ + _. . ._ + _|Bk| is independent of the partition. In other words, given any other partition B_ 1 _[′][∪][. . .][ ∪][B] k[′][′][of][E][,][one][has][|][B]_[1] _[|]_[ +] _[ . . .]_[ +] _[ |][B][k][|]_[=] _|B_ 1 _[′][|]_[ +] _[ . . .]_[ +] _[ |][B] k[′][′][|][.]_ 

_We refer to m_ ( _E_ ) _as the_ elementary measure _of E. (We occasionally write m_ ( _E_ ) _as m[d]_ ( _E_ ) _to emphasise the d-dimensional nature of the measure.) Thus, for example, the elementary measure of_ (1 _,_ 2) _∪_ [3 _,_ 6] _is_ (2 _−_ 1) + (6 _−_ 3) = 4 _._ 

**Proof.** We first prove (i) in the one-dimensional case _d_ = 1. Given any finite collection of intervals _I_ 1 _, . . . , Ik_ , one can place the 2 _k_ endpoints of these intervals in increasing order (discarding repetitions). Looking at the open intervals between these endpoints, together with the endpoints themselves (viewed as intervals of length zero), we see that there exists a finite collection of disjoint intervals _J_ 1 _, . . . , Jk′_ such that each of the _I_ 1 _, . . . , Ik_ are a union of some subcollection of the _J_ 1 _, . . . , Jk′_ . This already gives (i) when _d_ = 1. To prove the higher dimensional case, we express _E_ as the union _B_ 1 _, . . . , Bk_ of boxes _Bi_ = _Ii,_ 1 _× . . . × Ii,d_ . For each _j_ = 1 _, . . . , d_ , we use the onedimensional argument to express _I_ 1 _,j, . . . , Ik,j_ as the union of subcollections of a collection _J_ 1 _,j, . . . , Jkj[′][,j]_[of][disjoint][intervals.][Taking] Cartesian products, we can express the _B_ 1 _, . . . , Bk_ as finite unions of boxes _Ji_ 1 _,_ 1 _× . . . × Jid,d_ , where 1 _≤ ij ≤ kj[′]_[for][all][1] _[≤][j][≤][d]_[.][Such] boxes are all disjoint, and the claim follows. 

To prove (ii) we use a discretisation argument. Observe (exercise!) that for any interval _I_ , the length of _I_ can be recovered by the limiting formula 

**==> picture [112 x 21] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

7 

where 1 _[n]_[and][#] _[A]_[denotes][the][cardinality][of][a][finite] _N_ **[Z]**[ :=] _[ {] N_[:] _[ n][ ∈]_ **[Z]** _[}]_ set _A_ . Taking Cartesian products, we see that 

**==> picture [126 x 21] intentionally omitted <==**

for any box _B_ , and in particular that 

**==> picture [188 x 21] intentionally omitted <==**

Denoting the right-hand side as _m_ ( _E_ ), we obtain the claim (ii). □ 

**Exercise 1.1.2.** Give an alternate proof of Lemma 1.1.2(ii) by showing that any two partitions of _E_ into boxes admit a mutual refinement into boxes that arise from taking Cartesian products of elements from finite collections of disjoint intervals. 

**Remark 1.1.3.** One might be tempted to now define the measure _m_ ( _E_ ) of an arbitrary set _E ⊂_ **R** _[d]_ by the formula 

**==> picture [222 x 21] intentionally omitted <==**

since this worked well for elementary sets. However, this definition is not particularly satisfactory for a number of reasons. Firstly, one can concoct examples in which the limit does not exist (Exercise!). Even when the limit does exist, this concept does not obey reasonable properties such as translation invariance. For instance, if _d_ = 1 and _E_ := **Q** _∩_ [0 _,_ 1] := _{x ∈_ **Q** : 0 _≤ x ≤_ 1 _}_ , then this definition would give _E_ a measure of 1, but would give the translate _E_ + _√_ 2 := _{x_ + _√_ 2 : _x ∈_ **Q** ; 0 _≤ x ≤_ 1 _}_ a measure of zero. Nevertheless, the formula (1.1) will be valid for all Jordan measurable sets (see Exercise 1.1.13). It also makes precise an important intuition, namely that the continuous concept of measure can be viewed[5] as a limit of the discrete concept of (normalised) cardinality. 

From the definitions, it is clear that _m_ ( _E_ ) is a non-negative real number for every elementary set _E_ , and that 

**==> picture [118 x 11] intentionally omitted <==**

> 5Another way to obtain continuous measure as the limit of discrete measure is via _Monte Carlo integration_ , although in order to rigorously introduce the probability theory needed to set up Monte Carlo integration properly, one already needs to develop a large part of measure theory, so this perspective, while intuitive, is not suitable for foundational purposes. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

8 

whenever _E_ and _F_ are disjoint elementary sets. We refer to the latter property as _finite additivity_ ; by induction it also implies that 

**==> picture [182 x 11] intentionally omitted <==**

whenever _E_ 1 _, . . . , Ek_ are disjoint elementary sets. We also have the obvious degenerate case 

**==> picture [44 x 11] intentionally omitted <==**

Finally, elementary measure clearly extends the notion of volume, in the sense that 

**==> picture [52 x 11] intentionally omitted <==**

for all boxes _B_ . 

From non-negativity and finite additivity (and Exercise 1.1.1) we conclude the _monotonicity property_ 

**==> picture [62 x 11] intentionally omitted <==**

whenever _E ⊂ F_ are nested elementary sets. From this and finite additivity (and Exercise 1.1.1) we easily obtain the _finite subadditivity property_ 

**==> picture [118 x 11] intentionally omitted <==**

whenever _E, F_ are elementary sets (not necessarily disjoint); by induction one then has 

**==> picture [182 x 11] intentionally omitted <==**

whenever _E_ 1 _, . . . , Ek_ are elementary sets (not necessarily disjoint). 

It is also clear from the definition that we have the _translation invariance_ 

**==> picture [82 x 11] intentionally omitted <==**

for all elementary sets _E_ and _x ∈_ **R** _[d]_ . 

These properties in fact define elementary measure up to normalisation: 

**Exercise 1.1.3** (Uniqueness of elementary measure) **.** Let _d ≥_ 1. Let _m[′]_ : _E_ ( **R** _[d]_ ) _→_ **R**[+] be a map from the collection _E_ ( **R** _[d]_ ) of elementary subsets of **R** _[d]_ to the nonnegative reals that obeys the non-negativity, finite additivity, and translation invariance properties. Show that there exists a constant _c ∈_ **R**[+] such that _m[′]_ ( _E_ ) = _cm_ ( _E_ ) for all 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

9 

elementary sets _E_ . In particular, if we impose the additional normalisation _m[′]_ ([0 _,_ 1) _[d]_ ) = 1, then _m[′] ≡ m_ . ( _Hint:_ Set _c_ := _m[′]_ ([0 _,_ 1) _[d]_ ), and then compute _m[′]_ ([0 _, n_[1][)] _[d]_[)][for][any][positive][integer] _[n]_[.)] 

**Exercise 1.1.4.** Let _d_ 1 _, d_ 2 _≥_ 1, and let _E_ 1 _⊂_ **R** _[d]_[1] , _E_ 2 _⊂_ **R** _[d]_[2] be elementary sets. Show that _E_ 1 _× E_ 2 _⊂_ **R** _[d]_[1][+] _[d]_[2] is elementary, and _m[d]_[1][+] _[d]_[2] ( _E_ 1 _× E_ 2) = _m[d]_[1] ( _E_ 1) _× m[d]_[2] ( _E_ 2). 

**1.1.2. Jordan measure.** We now have a satisfactory notion of measure for elementary sets. But of course, the elementary sets are a very restrictive class of sets, far too small for most applications. For instance, a solid triangle or disk in the plane will not be elementary, or even a rotated box. On the other hand, as essentially observed long ago by Archimedes, such sets _E_ can be _approximated_ from within and without by elementary sets _A ⊂ E ⊂ B_ , and the inscribing elementary set _A_ and the circumscribing elementary set _B_ can be used to give lower and upper bounds on the putative measure of _E_ . As one makes the approximating sets _A, B_ increasingly fine, one can hope that these two bounds eventually match. This gives rise to the following definitions. 

**Definition 1.1.4** (Jordan measure) **.** Let _E ⊂_ **R** _[d]_ be a bounded set. 

- The _Jordan inner measure m∗,_ ( _J_ )( _E_ ) of _E_ is defined as 

**==> picture [166 x 21] intentionally omitted <==**

**==> picture [252 x 13] intentionally omitted <==**

**==> picture [168 x 21] intentionally omitted <==**

- If _m∗,_ ( _J_ )( _E_ ) = _m[∗][,]_[(] _[J]_[)] ( _E_ ), then we say that _E_ is _Jordan measurable_ , and call _m_ ( _E_ ) := _m∗,_ ( _J_ )( _E_ ) = _m[∗][,]_[(] _[J]_[)] ( _E_ ) the _Jordan measure_ of _E_ . As before, we write _m_ ( _E_ ) as _m[d]_ ( _E_ ) when we wish to emphasise the dimension _d_ . 

By convention, we do not consider unbounded sets to be Jordan measurable (they will be deemed to have infinite Jordan outer measure). 

Jordan measurable sets are those sets which are “almost elementary” with respect to Jordan outer measure. More precisely, we have 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

10 

**Exercise 1.1.5** (Characterisation of Jordan measurability) **.** Let _E ⊂_ **R** _[d]_ be bounded. Show that the following are equivalent: 

- (1) _E_ is Jordan measurable. 

- (2) For every _ε >_ 0, there exist elementary sets _A ⊂ E ⊂ B_ such that _m_ ( _B\A_ ) _≤ ε_ . 

- (3) For every _ε >_ 0, there exists an elementary set _A_ such that _m[∗][,]_[(] _[J]_[)] ( _A_ ∆ _E_ ) _≤ ε_ . 

As one corollary of this exercise, we see that every elementary set _E_ is Jordan measurable, and that Jordan measure and elementary measure coincide for such sets; this justifies the use of _m_ ( _E_ ) to denote both. In particular, we still have _m_ ( _∅_ ) = 0. 

Jordan measurability also inherits many of the properties of elementary measure: 

**Exercise 1.1.6.** Let _E, F ⊂_ **R** _[d]_ be Jordan measurable sets. 

- (1) (Boolean closure) Show that _E ∪ F_ , _E ∩ F_ , _E\F_ , and _E_ ∆ _F_ are Jordan measurable. 

- (2) (Non-negativity) _m_ ( _E_ ) _≥_ 0. 

- (3) (Finite additivity) If _E, F_ are disjoint, then _m_ ( _E ∪ F_ ) = _m_ ( _E_ ) + _m_ ( _F_ ). 

- (4) (Monotonicity) If _E ⊂ F_ , then _m_ ( _E_ ) _≤ m_ ( _F_ ). 

- (5) (Finite subadditivity) _m_ ( _E ∪ F_ ) _≤ m_ ( _E_ ) + _m_ ( _F_ ). 

- (6) (Translation invariance) For any _x ∈_ **R** _[d]_ , _E_ + _x_ is Jordan measurable, and _m_ ( _E_ + _x_ ) = _m_ ( _E_ ). 

Now we give some examples of Jordan measurable sets: 

**Exercise 1.1.7** (Regions under graphs are Jordan measurable) **.** Let _B_ be a closed box in **R** _[d]_ , and let _f_ : _B →_ **R** be a continuous function. 

- (1) Show that the graph _{_ ( _x, f_ ( _x_ )) : _x ∈ B} ⊂_ **R** _[d]_[+1] is Jordan measurable in **R** _[d]_[+1] with Jordan measure zero. ( _Hint:_ on a compact metric space, continuous functions are uniformly continuous.) 

- (2) Show that the set _{_ ( _x, t_ ) : _x ∈ B_ ; 0 _≤ t ≤ f_ ( _x_ ) _} ⊂_ **R** _[d]_[+1] is Jordan measurable. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

11 

**Exercise 1.1.8.** Let _A, B, C_ be three points in **R**[2] . 

- (1) Show that the solid triangle with vertices _A, B, C_ is Jordan measurable. 

- (2) Show that the Jordan measure of the solid triangle is equal to[1][where] _[|]_[(] _[a, b]_[)] _[ ∧]_[(] _[c, d]_[)] _[|]_[ :=] _[ |][ad][ −][bc][|]_[.] 2 _[|]_[(] _[B][ −][A]_[)] _[ ∧]_[(] _[C][ −][A]_[)] _[|]_[,] 

( _Hint:_ It may help to first do the case when one of the edges, say _AB_ , is horizontal.) 

**Exercise 1.1.9.** Show that every compact convex polytope[6] in **R** _[d]_ is Jordan measurable. 

**Exercise 1.1.10.** (1) Show that all open and closed Euclidean balls _B_ ( _x, r_ ) := _{y ∈_ **R** _[d]_ : _|y − x| < r}_ , _B_ ( _x, r_ ) := _{y ∈_ **R** _[d]_ : _|y − x| ≤ r}_ in **R** _[d]_ are Jordan measurable, with Jordan measure _cdr[d]_ for some constant _cd >_ 0 depending only on _d_ . 

- (2) Establish the crude bounds 

**==> picture [84 x 27] intentionally omitted <==**

(An exact formula for _cd_ is _cd_ = _d_[1] _[ω][d]_[,][where] _[ω][d]_[:=] Γ(2 _πd/[d/]_ 2)[2][is][the] volume of the unit sphere _S[d][−]_[1] _⊂_ **R** _[d]_ and Γ is the _Gamma function_ , but we will not derive this formula here.) 

**Exercise 1.1.11.** This exercise assumes familiarity with linear algebra. Let _L_ : **R** _[d] →_ **R** _[d]_ be a linear transformation. 

- (1) Show that there exists a non-negative real number _D_ such that _m_ ( _L_ ( _E_ )) = _Dm_ ( _E_ ) for every elementary set _E_ (note from previous exercises that _L_ ( _E_ ) is Jordan measurable). ( _Hint:_ apply Exercise 1.1.3 to the map _E �→ m_ ( _L_ ( _E_ )).) 

- (2) Show that if _E_ is Jordan measurable, then _L_ ( _E_ ) is also, and _m_ ( _L_ ( _E_ )) = _Dm_ ( _E_ ). 

> 6A _closed convex polytope_ is a subset of **R** _d_ formed by intersecting together finitely many closed half-spaces of the form _{x ∈_ **R** _[d]_ : _x · v ≤ c}_ , where _v ∈_ **R** _[d]_ , _c ∈_ **R** , and _·_ denotes the usual dot product on **R** _[d]_ . A _compact convex polytope_ is a closed convex polytope which is also bounded. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

12 

- (3) Show that _D_ = _|_ det _L|_ . ( _Hint:_ Work first with the case when _L_ is an elementary transformation, using Gaussian elimination. Alternatively, work with the cases when _L_ is a diagonal transformation or an orthogonal transformation, using the unit ball in the latter case, and use the polar decomposition.) 

**Exercise 1.1.12.** Define a _Jordan null set_ to be a Jordan measurable set of Jordan measure zero. Show that any subset of a Jordan null set is a Jordan null set. 

**Exercise 1.1.13.** Show that (1.1) holds for all Jordan measurable _E ⊂_ **R** _[d]_ . 

**Exercise 1.1.14** (Metric entropy formulation of Jordan measurability) **.** Define a _dyadic cube_ to be a half-open box of the form 

**==> picture [152 x 25] intentionally omitted <==**

for some integers _n, i_ 1 _, . . . , id_ . Let _E ⊂_ **R** _[d]_ be a bounded set. For each integer _n_ , let _E∗_ ( _E,_ 2 _[−][n]_ ) denote the number of dyadic cubes of sidelength 2 _[−][n]_ that are contained in _E_ , and let _E[∗]_ ( _E,_ 2 _[−][n]_ ) be the number of dyadic cubes[7] of sidelength 2 _[−][n]_ that intersect _E_ . Show that _E_ is Jordan measurable if and only if 

**==> picture [180 x 16] intentionally omitted <==**

in which case one has 

**==> picture [236 x 16] intentionally omitted <==**

**Exercise 1.1.15** (Uniqueness of Jordan measure) **.** Let _d ≥_ 1. Let _m[′]_ : _J_ ( **R** _[d]_ ) _→_ **R**[+] be a map from the collection _J_ ( **R** _[d]_ ) of Jordanmeasurable subsets of **R** _[d]_ to the nonnegative reals that obeys the non-negativity, finite additivity, and translation invariance properties. Show that there exists a constant _c ∈_ **R**[+] such that _m[′]_ ( _E_ ) = _cm_ ( _E_ ) for all Jordan measurable sets _E_ . In particular, if we impose the additional normalisation _m[′]_ ([0 _,_ 1) _[d]_ ) = 1, then _m[′] ≡ m_ . 

> 7This quantity could be called the (dyadic) _metric entropy_ of _E_ at scale 2 _−n_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

13 

**Exercise 1.1.16.** Let _d_ 1 _, d_ 2 _≥_ 1, and let _E_ 1 _⊂_ **R** _[d]_[1] , _E_ 2 _⊂_ **R** _[d]_[2] be Jordan measurable sets. Show that _E_ 1 _× E_ 2 _⊂_ **R** _[d]_[1][+] _[d]_[2] is Jordan measurable, and _m[d]_[1][+] _[d]_[2] ( _E_ 1 _× E_ 2) = _m[d]_[1] ( _E_ 1) _× m[d]_[2] ( _E_ 2). 

**Exercise 1.1.17.** Let _P, Q_ be two polytopes in **R** _[d]_ . Suppose that _P_ can be partitioned into finitely many sub-polytopes _P_ 1 _, . . . , Pn_ which, after being rotated and translated, form new polytopes _Q_ 1 _, . . . , Qn_ which are an _almost disjoint cover_ of _Q_ , which means that _Q_ = _Q_ 1 _∪ . . . ∪ Qn_ , and for any 1 _≤ i < j ≤ n_ , _Qi_ and _Qj_ only intersect at the boundary (i.e. the interior of _Qi_ is disjoint from the interior of _Qj_ ). Conclude that _P_ and _Q_ have the same Jordan measure. The converse statement is true in one and two dimensions _d_ = 1 _,_ 2 (this is the _Bolyai-Gerwien theorem_ ), but false in higher dimensions (this was Dehn’s negative answer[ **De1901** ] to _Hilbert’s third problem_ ). 

The above exercises give a fairly large class of Jordan measurable sets. However, not every subset of **R** _[d]_ is Jordan measurable. First of all, the unbounded sets are not Jordan measurable, by construction. But there are also bounded sets that are not Jordan measurable: 

**Exercise 1.1.18.** Let _E ⊂_ **R** _[d]_ be a bounded set. 

- (1) Show that _E_ and the closure _E_ of _E_ have the same Jordan outer measure. 

- (2) Show that _E_ and the interior _E[◦]_ of _E_ have the same Jordan inner measure. 

- (3) Show that _E_ is Jordan measurable if and only if the topological boundary _∂E_ of _E_ has Jordan outer measure zero. 

- (4) Show that the _bullet-riddled square_ [0 _,_ 1][2] _\_ **Q**[2] , and set of bullets [0 _,_ 1][2] _∩ Q_[2] , both have Jordan inner measure zero and Jordan outer measure one. In particular, both sets are not Jordan measurable. 

Informally, any set with a lot of “holes”, or a very “fractal” boundary, is unlikely to be Jordan measurable. In order to measure such sets we will need to develop _Lebesgue measure_ , which is done in the next set of notes. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

14 

**Exercise 1.1.19** (Carath´eodory type property) **.** Let _E ⊂_ **R** _[d]_ be a bounded set, and _F ⊂_ **R** _[d]_ be an elementary set. Show that _m[∗][,]_[(] _[J]_[)] ( _E_ ) = _m[∗][,]_[(] _[J]_[)] ( _E ∩ F_ ) + _m[∗][,]_[(] _[J]_[)] ( _E\F_ ). 

**1.1.3. Connection with the Riemann integral.** To conclude this section, we briefly discuss the relationship between Jordan measure and the _Riemann integral_ (or the equivalent _Darboux integral_ ). For simplicity we will only discuss the classical one-dimensional Riemann integral on an interval [ _a, b_ ], though one can extend the Riemann theory without much difficulty to higher-dimensional integrals on Jordan measurable sets. (In later sections, this Riemann integral will be superceded by the _Lebesgue integral_ .) 

**Definition 1.1.5** (Riemann integrability) **.** Let [ _a, b_ ] be an interval of positive length, and _f_ : [ _a, b_ ] _→_ **R** be a function. A _tagged partition P_ = (( _x_ 0 _, x_ 1 _, . . . , xn_ ) _,_ ( _x[∗]_ 1 _[, . . . , x][∗] n_[))][of][[] _[a, b]_[]][is][a][finite][sequence][of][real] numbers _a_ = _x_ 0 _< x_ 1 _< . . . < xn_ = _b_ , together with additional numbers _xi−_ 1 _≤ x[∗] i[≤][x][i]_[ for each] _[ i]_[ = 1] _[, . . . , n]_[.][We abbreviate] _[ x][i][−][x][i][−]_[1] as _δxi_ . The quantity ∆( _P_ ) := sup1 _≤i≤n δxi_ will be called the _norm_ of the tagged partition. The _Riemann sum R_ ( _f, P_ ) of _f_ with respect to the tagged partition _P_ is defined as 

**==> picture [108 x 29] intentionally omitted <==**

We say that _f_ is _Riemann integrable_ on [ _a, b_ ] if there exists a real _b_ number, denoted � _a[f]_[(] _[x]_[)] _[dx]_[and][referred][to][as][the] _[Riemann][integral]_ of _f_ on [ _a, b_ ], for which we have 

**==> picture [130 x 26] intentionally omitted <==**

by which we mean that for every _ε >_ 0 there exists _δ >_ 0 such _b_ that _|R_ ( _f, P_ ) _−_ � _a[f]_[(] _[x]_[)] _[dx][|][≤][ε]_[for][every][tagged][partition] _[P]_[with] ∆( _P_ ) _≤ δ_ . 

If [ _a, b_ ] is an interval of zero length, we adopt the convention that every function _f_ : [ _a, b_ ] _→_ **R** is Riemann integrable, with a Riemann integral of zero. 

Note that unbounded functions cannot be Riemann integrable (why?). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.1. Prologue: The problem of measure** 

15 

The above definition, while geometrically natural, can be awkward to use in practice. A more convenient formulation of the Riemann integral can be formulated using some additional machinery. 

**Exercise 1.1.20** (Piecewise constant functions) **.** Let [ _a, b_ ] be an interval. A _piecewise constant function f_ : [ _a, b_ ] _→_ **R** is a function for which there exists a partition of [ _a, b_ ] into finitely many intervals _I_ 1 _, . . . , In_ , such that _f_ is equal to a constant _ci_ on each of the intervals _Ii_ . If _f_ is piecewise constant, show that the expression 

**==> picture [38 x 28] intentionally omitted <==**

is independent of the choice of partition used to demonstrate the piecewise constant nature of _f_ . We will denote this quantity by _b_ p.c. � _a[f]_[(] _[x]_[)] _[dx]_[,][and][refer][to][it][as][the] _[piecewise][constant][integral]_[of] _[f]_ on [ _a, b_ ]. 

**Exercise 1.1.21** (Basic properties of the piecewise constant integral) **.** Let [ _a, b_ ] be an interval, and let _f, g_ : [ _a, b_ ] _→_ **R** be piecewise constant functions. Establish the following statements: 

- (1) (Linearity) For any real number _c_ , _cf_ and _f_ + _g_ are piece- _b b_ 

- wise constant, with p.c. � _a[cf]_[(] _[x]_[)] _[dx]_[=] _[c]_[p.c.] � _a[f]_[(] _[x]_[)] _[dx]_[and] _b b b_ 

- p.c. � _a[f]_[(] _[x]_[) +] _[ g]_[(] _[x]_[)] _[dx]_[ = p.c.] � _a[f]_[(] _[x]_[)] _[dx]_[ + p.c.] � _a[g]_[(] _[x]_[)] _[dx]_[.] 

- (2) (Monotonicity) If _f ≤ g_ pointwise (i.e. _f_ ( _x_ ) _≤ g_ ( _x_ ) for all _b b_ 

- _x ∈_ [ _a, b_ ]) then p.c. � _a[f]_[(] _[x]_[)] _[dx][ ≤]_[p.c.] � _a[g]_[(] _[x]_[)] _[dx]_[.] 

- (3) (Indicator) If _E_ is an elementary subset of [ _a, b_ ], then the indicator function 1 _E_ : [ _a, b_ ] _→_ **R** (defined by setting 1 _E_ ( _x_ ) := 1 when _x ∈ E_ and 1 _E_ ( _x_ ) := 0 otherwise) is piecewise con- _b_ 

- stant, and p.c. � _a_[1] _[E]_[(] _[x]_[)] _[dx]_[ =] _[ m]_[(] _[E]_[).] 

**Definition 1.1.6** (Darboux integral) **.** Let [ _a, b_ ] be an interval, and _f_ : [ _a, b_ ] _→_ **R** be a bounded function. The _lower Darboux integral b_ � _a f_ ( _x_ ) _dx_ of _f_ on [ _a, b_ ] is defined as 

**==> picture [235 x 29] intentionally omitted <==**

where _g_ ranges over all piecewise constant functions that are pointwise bounded above by _f_ . (The hypothesis that _f_ is bounded ensures that 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

16 

the supremum is over a non-empty set.) Similarly, we define the _upper b Darboux integral_ � _a[f]_[(] _[x]_[)] _[dx]_[of] _[f]_[on][[] _[a, b]_[]][by][the][formula] 

**==> picture [236 x 27] intentionally omitted <==**

_b b_ Clearly � _a f_ ( _x_ ) _dx ≤_ � _a[f]_[(] _[x]_[)] _[dx]_[.][If][these][two][quantities][are][equal,] we say that _f_ is _Darboux integrable_ , and refer to this quantity as the _Darboux integral_ of _f_ on [ _a, b_ ]. 

Note that the upper and lower Darboux integrals are related by the reflection identity 

**==> picture [132 x 26] intentionally omitted <==**

**Exercise 1.1.22.** Let [ _a, b_ ] be an interval, and _f_ : [ _a, b_ ] _→_ **R** be a bounded function. Show that _f_ is Riemann integrable if and only if it is Darboux integrable, in which case the Riemann integral and Darboux integrals are equal. 

**Exercise 1.1.23.** Show that any continuous function _f_ : [ _a, b_ ] _→_ **R** is Riemann integrable. More generally, show that any bounded, piecewise continuous[8] function _f_ : [ _a, b_ ] _→_ **R** is Riemann integrable. 

Now we connect the Riemann integral to Jordan measure in two ways. First, we connect the Riemann integral to one-dimensional Jordan measure: 

**Exercise 1.1.24** (Basic properties of the Riemann integral) **.** Let [ _a, b_ ] be an interval, and let _f, g_ : [ _a, b_ ] _→_ **R** be Riemann integrable. Establish the following statements: 

- (1) (Linearity) For any real number _c_ , _cf_ and _f_ + _g_ are Riemann _b b b_ 

- integrable, with � _a[cf]_[(] _[x]_[)] _[dx]_[ =] _[ c][ ·]_ � _a[f]_[(] _[x]_[)] _[dx]_[and] � _a[f]_[(] _[x]_[) +] _b b_ 

- _g_ ( _x_ ) _dx_ = � _a[f]_[(] _[x]_[)] _[dx]_[ +] � _a[g]_[(] _[x]_[)] _[dx]_[.] 

- (2) (Monotonicity) If _f ≤ g_ pointwise (i.e. _f_ ( _x_ ) _≤ g_ ( _x_ ) for all _b b_ 

- _x ∈_ [ _a, b_ ]) then � _a[f]_[(] _[x]_[)] _[dx][ ≤]_ � _a[g]_[(] _[x]_[)] _[dx]_[.] 

> 8A function _f_ : [ _a, b_ ] _→_ **R** is _piecewise continuous_ if one can partition [ _a, b_ ] into finitely many intervals, such that _f_ is continuous on each interval. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

17 

- (3) (Indicator) If _E_ is a Jordan measurable of [ _a, b_ ], then the indicator function 1 _E_ : [ _a, b_ ] _→_ **R** (defined by setting 1 _E_ ( _x_ ) := 1 when _x ∈ E_ and 1 _E_ ( _x_ ) := 0 otherwise) is Riemann inte- _b_ 

- grable, and � _a_[1] _[E]_[(] _[x]_[)] _[dx]_[ =] _[ m]_[(] _[E]_[).] 

Finally, show that these properties uniquely define the Riemann inte- _b_ gral, in the sense that the functional _f �→_ � _a[f]_[(] _[x]_[)] _[dx]_[is][the][only][map] from the space of Riemann integrable functions on [ _a, b_ ] to **R** which obeys all three of the above properties. 

Next, we connect the integral to two-dimensional Jordan measure: 

**Exercise 1.1.25** (Area interpretation of the Riemann integral) **.** Let [ _a, b_ ] be an interval, and let _f_ : [ _a, b_ ] _→_ **R** be a bounded function. Show that _f_ is Riemann integrable if and only if the sets _E_ + := _{_ ( _x, t_ ) : _x ∈_ [ _a, b_ ]; 0 _≤ t ≤ f_ ( _x_ ) _}_ and _E−_ := _{_ ( _x, t_ ) : _x ∈_ [ _a, b_ ]; _f_ ( _x_ ) _≤ t ≤_ 0 _}_ are both Jordan measurable in **R**[2] , in which case one has 

**==> picture [148 x 26] intentionally omitted <==**

where _m_[2] denotes two-dimensional Jordan measure. ( _Hint:_ First establish this in the case when _f_ is non-negative.) 

**Exercise 1.1.26.** Extend the definition of the Riemann and Darboux integrals to higher dimensions, in such a way that analogues of all the previous results hold. 

## **1.2. Lebesgue measure** 

In Section 1.1, we recalled the classical theory of _Jordan measure_ on Euclidean spaces **R** _[d]_ . This theory proceeded in the following stages: 

- (i) First, one defined the notion of a box _B_ and its volume _|B|_ . 

- (ii) Using this, one defined the notion of an elementary set _E_ (a finite union of boxes), and defines the elementary measure _m_ ( _E_ ) of such sets. 

- (iii) From this, one defined the inner and Jordan outer measures _m∗,_ ( _J_ )( _E_ ) _, m[∗][,]_[(] _[J]_[)] ( _E_ ) of an arbitrary bounded set _E ⊂_ **R** _[d]_ . If those measures match, we say that _E_ is _Jordan measurable_ , 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

18 

and call _m_ ( _E_ ) = _m∗,_ ( _J_ )( _E_ ) = _m[∗][,]_[(] _[J]_[)] ( _E_ ) the _Jordan measure_ of _E_ . 

As long as one is lucky enough to only have to deal with Jordan measurable sets, the theory of Jordan measure works well enough. However, as noted previously, not all sets are Jordan measurable, even if one restricts attention to bounded sets. In fact, we shall see later in these notes that there even exist bounded open sets, or compact sets, which are not Jordan measurable, so the Jordan theory does not cover many classes of sets of interest. Another class that it fails to cover is countable unions or intersections of sets that are already known to be measurable: 

**Exercise 1.2.1.** Show that the countable union[�] _[∞] n_ =1 _[E][n]_[or][count-] able intersection[�] _[∞] n_ =1 _[E][n]_[of][Jordan][measurable][sets] _[E]_[1] _[, E]_[2] _[, . . .][ ⊂]_ **[R]** need not be Jordan measurable, even when bounded. 

This creates problems with Riemann integrability (which, as we saw in Section 1.1, was closely related to Jordan measure) and pointwise limits: 

**Exercise 1.2.2.** Give an example of a sequence of uniformly bounded, Riemann integrable functions _fn_ : [0 _,_ 1] _→_ **R** for _n_ = 1 _,_ 2 _, . . ._ that converge pointwise to a bounded function _f_ : [0 _,_ 1] _→_ **R** that is _not_ Riemann integrable. What happens if we replace pointwise convergence with uniform convergence? 

These issues can be rectified by using a more powerful notion of measure than Jordan measure, namely _Lebesgue measure_ . To define this measure, we first tinker with the notion of the Jordan outer measure 

**==> picture [164 x 21] intentionally omitted <==**

of a set _E ⊂_ **R** _[d]_ (we adopt the convention that _m[∗][,]_[(] _[J]_[)] ( _E_ ) = + _∞_ if _E_ is unbounded, thus _m[∗][,]_[(] _[J]_[)] now takes values in the extended nonnegative reals [0 _,_ + _∞_ ], whose properties we will briefly review below). Observe from the finite additivity and subadditivity of elementary measure that we can also write the Jordan outer measure as 

**==> picture [248 x 21] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

19 

i.e. the Jordan outer measure is the infimal cost required to cover _E_ by a finite union of boxes. (The natural number _k_ is allowed to vary freely in the above infimum.) We now modify this by replacing the finite union of boxes by a countable union of boxes, leading to the _Lebesgue outer measure_[9] _m[∗]_ ( _E_ ) of _E_ : 

**==> picture [192 x 28] intentionally omitted <==**

thus the Lebesgue outer measure is the infimal cost required to cover _E_ by a _countable_ union of boxes. Note that the countable sum � _∞n_ =1 _[|][B][n][|]_[ may be infinite, and so the Lebesgue outer measure] _[ m][∗]_[(] _[E]_[)] could well equal + _∞_ . 

Clearly, we always have _m[∗]_ ( _E_ ) _≤ m[∗][,]_[(] _[J]_[)] ( _E_ ) (since we can always pad out a finite union of boxes into an infinite union by adding an infinite number of empty boxes). But _m[∗]_ ( _E_ ) can be a lot smaller: 

**Example 1.2.1.** Let _E_ = _{x_ 1 _, x_ 2 _, x_ 3 _, . . .} ⊂_ **R** _[d]_ be a countable set. We know that the Jordan outer measure of _E_ can be quite large; for instance, in one dimension, _m[∗][,]_[(] _[J]_[)] ( **Q** ) is infinite, and _m[∗][,]_[(] _[J]_[)] ( **Q** _∩_ [ _−R, R_ ]) = _m[∗][,]_[(] _[J]_[)] ([ _−R, R_ ]) = 2 _R_ since **Q** _∩_ [ _−R, R_ ] has [ _−R, R_ ] as its closure (see Exercise 1.1.18). On the other hand, all countable sets _E_ have Lebesgue outer measure zero. Indeed, one simply covers _E_ by the degenerate boxes _{x_ 1 _}, {x_ 2 _}, . . ._ of sidelength and volume zero. 

Alternatively, if one does not like degenerate boxes, one can cover each _xn_ by a cube _Bn_ of sidelength _ε/_ 2 _[n]_ (say) for some arbitrary _ε >_ 0, leading to a total cost of[�] _[∞] n_ =1[(] _[ε/]_[2] _[n]_[)] _[d]_[,][which][converges][to] _Cdε[d]_ for some absolute constant _Cd_ . As _ε_ can be arbitrarily small, we see that the Lebesgue outer measure must be zero. We will refer to this type of trick as the _ε/_ 2 _[n] trick_ ; it will be used many further times in this text. 

From this example we see in particular that a set may be unbounded while still having Lebesgue outer measure zero, in contrast to Jordan outer measure. 

> 9Lebesgue outer measure is also denoted _m∗_ ( _E_ ) in some texts. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

20 

As we shall see in Section 1.7, Lebesgue outer measure (also known as _Lebesgue exterior measure_ ) is a special case of a more general concept known as an _outer measure_ . 

In analogy with the Jordan theory, we would also like to define a concept of “Lebesgue inner measure” to complement that of outer measure. Here, there is an asymmetry (which ultimately arises from the fact that elementary measure is subadditive rather than superadditive): one does not gain any increase in power in the Jordan inner measure by replacing finite unions of boxes with countable ones. But one can get a sort of Lebesgue inner measure by taking complements; see Exercise 1.2.18. This leads to one possible definition for Lebesgue measurability, namely the _Carath´eodory criterion_ for Lebesgue measurability, see Exercise 1.2.17. However, this is not the most intuitive formulation of this concept to work with, and we will instead use a different (but logically equivalent) definition of Lebesgue measurability. The starting point is the observation (see Exercise 1.1.13) that Jordan measurable sets can be efficiently contained in elementary sets, with an error that has small Jordan outer measure. In a similar vein, we will define Lebesgue measurable sets to be sets that can be efficiently contained in _open_ sets, with an error that has small _Lebesgue_ outer measure: 

**Definition 1.2.2** (Lebesgue measurability) **.** A set _E ⊂_ **R** _[d]_ is said to be _Lebesgue measurable_ if, for every _ε >_ 0, there exists an open set _U ⊂_ **R** _[d]_ containing _E_ such that _m[∗]_ ( _U \E_ ) _≤ ε_ . If _E_ is Lebesgue measurable, we refer to _m_ ( _E_ ) := _m[∗]_ ( _E_ ) as the _Lebesgue measure_ of _E_ (note that this quantity may be equal to + _∞_ ). We also write _m_ ( _E_ ) as _m[d]_ ( _E_ ) when we wish to emphasise the dimension _d_ . 

**Remark 1.2.3.** The intuition that measurable sets are almost open is also known as _Littlewood’s first principle_ , this principle is a triviality with our current choice of definitions, though less so if one uses other, equivalent, definitions of Lebesgue measurability. See Section 1.3.5 for a further discussion of Littlewood’s principles. 

As we shall see later, Lebesgue measure extends Jordan measure, in the sense that every Jordan measurable set is Lebesgue measurable, 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

21 

and the Lebesgue measure and Jordan measure of a Jordan measurable set are always equal. We will also see a few other equivalent descriptions of the concept of Lebesgue measurability. 

In the notes below we will establish the basic properties of Lebesgue measure. Broadly speaking, this concept obeys all the intuitive properties one would ask of measure, so long as one restricts attention to countable operations rather than uncountable ones, and as long as one restricts attention to Lebesgue measurable sets. The latter is not a serious restriction in practice, as almost every set one actually encounters in analysis will be measurable (the main exceptions being some pathological sets that are constructed using the axiom of choice). In the next set of notes we will use Lebesgue measure to set up the Lebesgue integral, which extends the Riemann integral in the same way that Lebesgue measure extends Jordan measure; and the many pleasant properties of Lebesgue measure will be reflected in analogous pleasant properties of the Lebesgue integral (most notably the convergence theorems). 

We will treat all dimensions _d_ = 1 _,_ 2 _, . . ._ equally here, but for the purposes of drawing pictures, we recommend to the reader that one sets _d_ equal to 2. However, for this topic at least, no additional mathematical difficulties will be encountered in the higher-dimensional case (though of course there are significant _visual_ difficulties once _d_ exceeds 3). 

**1.2.1. Properties of Lebesgue outer measure.** We begin by studying the Lebesgue outer measure _m[∗]_ , which was defined earlier, and takes values in the extended non-negative real axis [0 _,_ + _∞_ ]. We first record three easy properties of Lebesgue outer measure, which we will use repeatedly in the sequel without further comment: 

**Exercise 1.2.3** (The outer measure axioms) **.** 

- (i) (Empty set) _m[∗]_ ( _∅_ ) = 0. 

- (ii) (Monotonicity) If _E ⊂ F ⊂_ **R** _[d]_ , then _m[∗]_ ( _E_ ) _≤ m[∗]_ ( _F_ ). 

- (iii) (Countable subadditivity) If _E_ 1 _, E_ 2 _, . . . ⊂_ **R** _[d]_ is a countable sequence of sets, then _m[∗]_ ([�] _[∞] n_ =1 _[E][n]_[)] _[≤]_[�] _[∞] n_ =1 _[m][∗]_[(] _[E][n]_[).] ( _Hint:_ Use the axiom of countable choice, Tonelli’s theorem 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

22 

for series, and the _ε/_ 2 _[n]_ trick used previously to show that countable sets had outer measure zero.) 

Note that countable subadditivity, when combined with the empty set axiom, gives as a corollary the finite subadditivity property 

**==> picture [196 x 11] intentionally omitted <==**

for any _k ≥_ 0. These subadditivity properties will be useful in establishing _upper_ bounds on Lebesgue outer measure. Establishing _lower_ bounds will often be a bit trickier. (More generally, when dealing with a quantity that is defined using an infimum, it is usually easier to obtain upper bounds on that quantity than lower bounds, because the former requires one to bound just one element of the infimum, whereas the latter requires one to bound _all_ elements.) 

**Remark 1.2.4.** Later on in this text, when we study abstract measure theory on a general set _X_ , we will define the concept of an _outer measure_ on _X_ , which is an assigment _E �→ m[∗]_ ( _E_ ) of element of [0 _,_ + _∞_ ] to arbitrary subsets _E_ of a space _X_ that obeys the above three axioms of the empty set, monotonicity, and countable subadditivity; thus Lebesgue outer measure is a model example of an abstract outer measure. On the other hand (and somewhat confusingly), Jordan outer measure will not be an abstract outer measure (even after adopting the convention that unbounded sets have Jordan outer measure + _∞_ ): it obeys the empty set and monotonicity axioms, but is only finitely subadditive rather than countably subadditive. (For instance, the rationals **Q** have infinite Jordan outer measure, despite being the countable union of points, each of which have a Jordan outer measure of zero.) Thus we already see a major benefit of allowing countable unions of boxes in the definition of Lebesgue outer measure, in contrast to the finite unions of boxes in the definition of Jordan outer measure, in that finite subadditivity is upgraded to countable subadditivity. 

Of course, one cannot hope to upgrade countable subadditivity to uncountable subadditivity: **R** _[d]_ is an uncountable union of points, each of which has Lebesgue outer measure zero, but (as we shall shortly see), **R** _[d]_ has infinite Lebesgue outer measure. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

23 

It is natural to ask whether Lebesgue outer measure has the finite additivity property, that is to say that _m[∗]_ ( _E ∪ F_ ) = _m[∗]_ ( _E_ ) + _m[∗]_ ( _F_ ) whenever _E, F ⊂_ **R** _[d]_ are disjoint. The answer to this question is somewhat subtle: as we shall see later, we have finite additivity (and even countable additivity) when all sets involved are Lebesgue measurable, but that finite additivity (and hence also countable additivity) can break down in the non-measurable case. The difficulty here (which, incidentally, also appears in the theory of Jordan outer measure) is that if _E_ and _F_ are sufficiently “entangled” with each other, it is not always possible to take a countable cover of _E ∪ F_ by boxes and split the total volume of that cover into separate covers of _E_ and _F_ without some duplication. However, we can at least recover finite additivity if the sets _E, F_ are separated by some positive distance: 

**Lemma 1.2.5** (Finite additivity for separated sets) **.** _Let E, F ⊂_ **R** _[d] be such that_ dist( _E, F_ ) _>_ 0 _, where_ 

dist( _E, F_ ) := inf _{|x − y|_ : _x ∈ E, y ∈ F }_ 

_is the distance_[10] _between E and F . Then m[∗]_ ( _E ∪ F_ ) = _m[∗]_ ( _E_ ) + _m[∗]_ ( _F_ ) _._ 

**Proof.** From subadditivity one has _m[∗]_ ( _E ∪ F_ ) _≤ m[∗]_ ( _E_ )+ _m[∗]_ ( _F_ ), so it suffices to prove the other direction _m[∗]_ ( _E_ ) + _m[∗]_ ( _F_ ) _≤ m[∗]_ ( _E ∪ F_ ). This is trivial if _E ∪ F_ has infinite Lebesgue outer measure, so we may assume that it has finite Lebesgue outer measure (and then the same is true for _E_ and _F_ , by monotonicity). 

We use the standard “give yourself an epsilon of room” trick (see Section 2.7 of _An epsilon of room, Vol I._ ). Let _ε >_ 0. By definition of Lebesgue outer measure, we can cover _E ∪ F_ by a countable family _B_ 1 _, B_ 2 _, . . ._ of boxes such that 

**==> picture [116 x 28] intentionally omitted <==**

Suppose it was the case that each box intersected at most one of _E_ and _F_ . Then we could divide this family into two subfamilies _B_ 1 _[′][, B]_ 2 _[′][, . . .]_ 

10Recall from the preface that we use the usual Euclidean metric _|_ ( _x_ 1 _, . . . , xd_ ) _|_ := � _x_[2] 1[+] _[ . . .]_[ +] _[ x]_[2] _d_[on] **[R]** _[d]_[.] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

24 

and _B_ 1 _[′′][, B]_ 2 _[′′][, B]_ 3 _[′′][, . . .]_[,][the][first][of][which][covered] _[E]_[,][and][the][second][of] which covered _F_ . From definition of Lebesgue outer measure, we have 

**==> picture [78 x 29] intentionally omitted <==**

and 

**==> picture [82 x 28] intentionally omitted <==**

summing, we obtain 

**==> picture [120 x 28] intentionally omitted <==**

and thus 

**==> picture [152 x 11] intentionally omitted <==**

Since _ε_ was arbitrary, this gives _m[∗]_ ( _E_ ) + _m[∗]_ ( _F_ ) _≤ m[∗]_ ( _E ∪ F_ ) as required. 

Of course, it is quite possible for some of the boxes _Bn_ to intersect both _E_ and _F_ , particularly if the boxes are big, in which case the above argument does not work because that box would be doublecounted. However, observe that given any _r >_ 0, one can always partition a large box _Bn_ into a finite number of smaller boxes, each of which has diameter[11] at most _r_ , with the total volume of these sub-boxes equal to the volume of the original box. Applying this observation to each of the boxes _Bn_ , we see that given any _r >_ 0, we may assume without loss of generality that the boxes _B_ 1 _, B_ 2 _, . . ._ covering _E ∪F_ have diameter at most _r_ . In particular, we may assume that all such boxes have diameter strictly less than dist( _E, F_ ). Once we do this, then it is no longer possible for any box to intersect both _E_ and _F_ , and then the previous argument now applies. □ 

In general, disjoint sets _E, F_ need not have a positive separation from each other (e.g. _E_ = [0 _,_ 1) and _F_ = [1 _,_ 2]). But the situation improves when _E, F_ are closed, and at least one of _E, F_ is compact: 

11The _diameter_ of a set _B_ is defined as sup _{|x − y|_ : _x, y ∈ B}_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

25 

**Exercise 1.2.4.** Let _E, F ⊂_ **R** _[d]_ be disjoint closed sets, with at least one of _E, F_ being compact. Show that dist( _E, F_ ) _>_ 0. Give a counterexample to show that this claim fails when the compactness hypothesis is dropped. 

We already know that countable sets have Lebesgue outer measure zero. Now we start computing the outer measure of some other sets. We begin with elementary sets: 

**Lemma 1.2.6** (Outer measure of elementary sets) **.** _Let E be an elementary set. Then the Lebesgue outer measure m[∗]_ ( _E_ ) _of E is equal to the elementary measure m_ ( _E_ ) _of E: m[∗]_ ( _E_ ) = _m_ ( _E_ ) _._ 

**Remark 1.2.7.** Since countable sets have zero outer measure, we note that we have managed to give a proof of _Cantor’s theorem_ that **R** _[d]_ is uncountable. Of course, much quicker proofs of this theorem are available. However, this observation shows that the proof this lemma must somehow use some crucial fact about the real line which is not true for countable subfields of **R** , such as the rationals **Q** . In the proof we give here, the key fact about the real line we use is the Heine-Borel theorem, which ultimately exploits the important fact that the reals are _complete_ . In the one-dimensional case _d_ = 1, it is also possible to exploit the fact that the reals are _connected_ as a substitute for completeness (note that proper subfields of the reals are neither connected nor complete). 

**Proof.** We already know that _m[∗]_ ( _E_ ) _≤ m[∗][,]_[(] _[J]_[)] ( _E_ ) = _m_ ( _E_ ), so it suffices to show that _m_ ( _E_ ) _≤ m[∗]_ ( _E_ ). 

We first establish this in the case when the elementary set _E_ is closed. As the elementary set _E_ is also bounded, this allows us to use the powerful _Heine-Borel theorem_ , which asserts that every open cover of _E_ has a finite subcover (or in other words, _E_ is _compact_ ). 

We again use the epsilon of room strategy. Let _ε >_ 0 be arbitrary, then we can find a countable family _B_ 1 _, B_ 2 _, . . ._ of boxes that cover _E_ , 

**==> picture [54 x 29] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

26 

and such that 

**==> picture [98 x 28] intentionally omitted <==**

We would like to use the Heine-Borel theorem, but the boxes _Bn_ need not be open. But this is not a serious problem, as one can spend another epsilon to enlarge the boxes to be open. More precisely, for each box _Bn_ one can find an open box _Bn[′]_[containing] _[B][n]_[such][that] _|Bn[′][| ≤|][B][n][|]_[ +] _[ ε/]_[2] _[n]_[(say).][The] _[B] n[′]_[still][cover] _[E]_[,][and][we][have] 

**==> picture [262 x 28] intentionally omitted <==**

As the _Bn[′]_[are][open,][we][may][apply][the][Heine-Borel][theorem][and] conclude that 

**==> picture [51 x 30] intentionally omitted <==**

for some finite _N_ . Using the finite subadditivity of elementary measure, we conclude that 

**==> picture [74 x 30] intentionally omitted <==**

and thus 

**==> picture [92 x 11] intentionally omitted <==**

Since _ε >_ 0 was arbitrary, the claim follows. 

Now we consider the case when the elementary _E_ is not closed. Then we can write _E_ as the finite union _Q_ 1 _∪ . . . ∪ Qk_ of disjoint boxes, which need not be closed. But, similarly to before, we can use the epsilon of room strategy: for every _ε >_ 0 and every 1 _≤ j ≤ k_ , one can find a closed sub-box _Q[′] j_[of] _[Q][j]_[such][that] _[|][Q][′] j[|][≥|][Q][j][| −][ε/k]_ (say); then _E_ contains the finite union of _Q[′]_ 1 _[∪][. . .][∪][Q][′] k_[disjoint] _[ closed]_ boxes, which is a closed elementary set. By the previous discussion and the finite additivity of elementary measure, we have 

**==> picture [206 x 61] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

27 

Applying by monotonicity of Lebesgue outer measure, we conclude that 

**==> picture [84 x 11] intentionally omitted <==**

for every _ε >_ 0. Since _ε >_ 0 was arbitrary, the claim follows. □ 

The above lemma allows us to compute the Lebesgue outer measure of a finite union of boxes. From this and monotonicity we conclude that the Lebesgue outer measure of any set is bounded below by its Jordan inner measure. As it is also bounded above by the Jordan outer measure, we have 

**==> picture [221 x 14] intentionally omitted <==**

for every _E ⊂_ **R** _[d]_ . 

**Remark 1.2.8.** We are now able to explain why not every bounded open set or compact set is Jordan measurable. Consider the countable set **Q** _∩_ [0 _,_ 1], which we enumerate as _{q_ 1 _, q_ 2 _, q_ 3 _, . . .}_ , let _ε >_ 0 be a small number, and consider the set 

**==> picture [140 x 28] intentionally omitted <==**

This is the union of open sets and is thus open. On the other hand, by countable subadditivity, one has 

**==> picture [110 x 28] intentionally omitted <==**

Finally, as _U_ is dense in [0 _,_ 1] (i.e. _U_ contains [0 _,_ 1]), we have 

**==> picture [188 x 13] intentionally omitted <==**

For _ε_ small enough (e.g. _ε_ := 1 _/_ 3), we see that the Lebesgue outer measure and Jordan outer measure of _U_ disagree. Using (1.2), we conclude that the bounded open set _U_ is not Jordan measurable. This in turn implies that the complement of _U_ in, say, [ _−_ 2 _,_ 2], is also not Jordan measurable, despite being a compact set. 

Now we turn to countable unions of boxes. It is convenient to introduce the following notion: two boxes are _almost disjoint_ if their 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

28 

interiors are disjoint, thus for instance [0 _,_ 1] and [1 _,_ 2] are almost disjoint. As a box has the same elementary measure as its interior, we see that the finite additivity property 

**==> picture [230 x 11] intentionally omitted <==**

holds for _almost_ disjoint boxes _B_ 1 _, . . . , Bk_ , and not just for disjoint boxes. This (and Lemma 1.2.6) has the following consequence: 

**Lemma 1.2.9** (Outer measure of countable unions of almost disjoint boxes) **.** _Let E_ =[�] _[∞] n_ =1 _[B][n][be][a][countable][union][of][almost][disjoint] boxes B_ 1 _, B_ 2 _, . . .. Then_ 

**==> picture [82 x 28] intentionally omitted <==**

Thus, for instance, **R** _[d]_ itself has an infinite outer measure. 

**Proof.** From countable subadditivity and Lemma 1.2.6 we have 

**==> picture [146 x 28] intentionally omitted <==**

so it to show that 

**==> picture [82 x 29] intentionally omitted <==**

But for each natural number _N_ , _E_ contains the elementary set _B_ 1 _∪ . . . ∪ BN_ , so by monotonicity and Lemma 1.2.6, 

**==> picture [126 x 27] intentionally omitted <==**

and thus by (1.3), one has 

**==> picture [300 x 47] intentionally omitted <==**

**Remark 1.2.10.** The above lemma has the following immediate corollary: if _E_ =[�] _[∞] n_ =1 _[B][n]_[=][�] _[∞] n_ =1 _[B] n[′]_[can][be][decomposed][in][two] different ways as the countable union of almost disjoint boxes, then 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

29 

� _∞n_ =1 _[|][B][n][|]_[ =][ �] _[∞] n_ =1 _[|][B] n[′][|]_[.][Although this statement is intuitively obvi-] ous and does not explicitly use the concepts of Lebesgue outer measure or Lebesgue measure, it is remarkably difficult to prove this statement rigorously without essentially using one of these two concepts. (Try it!) 

**Exercise 1.2.5.** Show that if a set _E ⊂_ **R** _[d]_ is expressible as the countable union of almost disjoint boxes, then the Lebesgue outer measure of _E_ is equal to the Jordan inner measure: _m[∗]_ ( _E_ ) = _m∗,_ ( _J_ )( _E_ ), where we extend the definition of Jordan inner measure to unbounded sets in the obvious manner. 

Not every set can be expressed as the countable union of almost disjoint boxes (consider for instance the irrationals **R** _\_ **Q** , which contain no boxes other than the singleton sets). However, there is an important class of sets of this form, namely the _open sets_ : 

**Lemma 1.2.11.** _Let E ⊂_ **R** _[d] be an open set. Then E can be expressed as the countable union of almost disjoint boxes (and, in fact, as the countable union of almost disjoint closed cubes)._ 

**Proof.** We will use the _dyadic mesh_ structure of the Euclidean space **R** _[d]_ , which is a convenient tool for “discretising” certain aspects of real analysis. 

Define a _closed dyadic cube_ to be a cube _Q_ of the form 

**==> picture [168 x 25] intentionally omitted <==**

for some integers _n, i_ 1 _, . . . , id_ . To avoid some technical issues we shall restrict attention here to “small” cubes of sidelength at most 1, thus we restrict _n_ to the non-negative integers, and we will completely ignore “large” cubes of sidelength greater than one. Observe that the closed dyadic cubes of a fixed sidelength 2 _[−][n]_ are almost disjoint, and cover all of **R** _[d]_ . Also observe that each dyadic cube of sidelength 2 _[−][n]_ is contained in exactly one “parent” cube of sidelength 2 _[−][n]_[+1] (which, conversely, has 2 _[d]_ “children” of sidelength 2 _[−][n]_ ), giving the dyadic cubes a structure analogous to that of a binary tree (or more precisely, an infinite forest of 2 _[d]_ -ary trees). As a consequence of these facts, we also obtain the important _dyadic nesting property_ : given 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

30 

any two closed dyadic cubes (possibly of different sidelength), either they are almost disjoint, or one of them is contained in the other. 

If _E_ is open, and _x ∈ E_ , then by definition there is an open ball centered at _x_ that is contained in _E_ , and it is easy to conclude that there is also a closed dyadic cube containing _x_ that is contained in _E_ . Thus, if we let _Q_ be the collection of all the dyadic cubes _Q_ that are contained in _E_ , we see that the union[�] _Q∈Q[Q]_[of][all][these][cubes] is exactly equal to _E_ . 

As there are only countably many dyadic cubes, _Q_ is at most countable. But we are not done yet, because these cubes are not almost disjoint (for instance, any cube _Q_ in _Q_ will of course overlap with its child cubes). But we can deal with this by exploiting the dyadic nesting property. Let _Q[∗]_ denote those cubes in _Q_ which are _maximal_ with respect to set inclusion, which means that they are not contained in any other cube in _Q_ . From the nesting property (and the fact that we have capped the maximum size of our cubes) we see that every cube in _Q_ is contained in exactly one maximal cube in _Q[∗]_ , and that any two such maximal cubes in _Q[∗]_ are almost disjoint. Thus, we see that _E_ is the union _E_ =[�] _Q∈Q[∗][Q]_[of][almost][disjoint] cubes. As _Q[∗]_ is at most countable, the claim follows (adding empty boxes if necessary to pad out the cardinality). □ 

We now have a formula for the Lebesgue outer measure of any open set: it is exactly equal to the Jordan inner measure of that set, or of the total volume of any partitioning of that set into almost disjoint boxes. Finally, we have a formula for the Lebesgue outer measure of an arbitrary set: 

**Lemma 1.2.12** (Outer regularity) **.** _Let E ⊂_ **R** _[d] be an arbitrary set. Then one has_ 

**==> picture [126 x 17] intentionally omitted <==**

**Proof.** From monotonicity one trivially has 

**==> picture [124 x 17] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

31 

so it to show that 

inf _E⊂U,U_ open _[m][∗]_[(] _[U]_[)] _[ ≤][m][∗]_[(] _[E]_[)] _[.]_ 

This is trivial for _m[∗]_ ( _E_ ) infinite, so we may assume that _m[∗]_ ( _E_ ) is 

Let _ε >_ 0. By definition of outer measure, there exists a countable family _B_ 1 _, B_ 2 _, . . ._ of boxes covering _E_ such that 

**==> picture [98 x 28] intentionally omitted <==**

We use the _ε/_ 2 _[n]_ trick again. We can enlarge each of these boxes _Bn_ to an _open_ box _Bn[′]_[such][that] _[|][B] n[′][|][≤|][B][n][|]_[ +] _[ ε/]_[2] _[n]_[.][Then][the][set] � _∞n_ =1 _[B] n[′]_[,][being][a][union][of][open][sets,][is][itself][open,][and][contains] _[E]_[;] and 

**==> picture [212 x 28] intentionally omitted <==**

By countable subadditivity, this implies that 

**==> picture [116 x 28] intentionally omitted <==**

and thus 

inf _E⊂U,U_ open _[m][∗]_[(] _[U]_[)] _[ ≤][m][∗]_[(] _[E]_[) + 2] _[ε.]_ As _ε >_ 0 was arbitrary, we obtain the claim. □ 

**Exercise 1.2.6.** Give an example to show that the reverse statement 

**==> picture [126 x 19] intentionally omitted <==**

is false. (For the corrected version of this statement, see Exercise 1.2.15.) 

**1.2.2. Lebesgue measurability.** We now define the notion of a Lebesgue measurable set as one which can be efficiently contained in open sets in the sense of Definition 1.2.2, and set out their basic properties. 

First, we show that there are plenty of Lebesgue measurable sets. **Lemma 1.2.13** (Existence of Lebesgue measurable sets) **.** 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

32 

- (i) _Every open set is Lebesgue measurable._ 

- (ii) _Every closed set is Lebesgue measurable._ 

- (iii) _Every set of Lebesgue outer measure zero is measurable. (Such sets are called_ null sets _.)_ 

- (iv) _The empty set ∅ is Lebesgue measurable._ 

- (v) _If E ⊂_ **R** _[d] is Lebesgue measurable, then so is its complement_ **R** _[d] \E._ 

- (vi) _If E_ 1 _, E_ 2 _, E_ 3 _, . . . ⊂_ **R** _[d] are a sequence of Lebesgue measurable sets, then the union_[�] _[∞] n_ =1 _[E][n][is][Lebesgue][measurable.]_ 

- (vii) _If E_ 1 _, E_ 2 _, E_ 3 _, . . . ⊂_ **R** _[d] are a sequence of Lebesgue measurable sets, then the intersection_[�] _[∞] n_ =1 _[E][n][is][Lebesgue][mea-] surable._ 

**Proof.** Claim (i) is obvious from definition, as are Claims (iii) and (iv). 

To prove Claim (vi), we use the _ε/_ 2 _[n]_ trick. Let _ε >_ 0 be arbitrary. By hypothesis, each _En_ is contained in an open set _Un_ whose difference _Un\En_ has Lebesgue outer measure at most _ε/_ 2 _[n]_ . By countable subadditivity, this implies that[�] _[∞] n_ =1 _[E][n]_[is contained in][ �] _[∞] n_ =1 _[U][n]_[, and] the difference ([�] _[∞] n_ =1 _[U][n]_[)] _[\]_[(][�] _[∞] n_ =1 _[E][n]_[)][has][Lebesgue][outer][measure][at] most _ε_ . The set[�] _[∞] n_ =1 _[U][n]_[,][being][a][union][of][open][sets,][is][itself][open,] and the claim follows. 

Now we establish Claim (ii). Every closed set _E_ is the countable union of closed and bounded sets (by intersecting _E_ with, say, the closed balls _B_ (0 _, n_ ) of radius _n_ for _n_ = 1 _,_ 2 _,_ 3 _, . . ._ ), so by (vi), it suffices to verify the claim when _E_ is closed and bounded, hence compact by the Heine-Borel theorem. Note that the boundedness of _E_ implies that _m[∗]_ ( _E_ ) is finite. 

Let _ε >_ 0. By outer regularity (Lemma 1.2.12), we can find an open set _U_ containing _E_ such that _m[∗]_ ( _U_ ) _≤ m[∗]_ ( _E_ ) + _ε_ . It suffices to show that _m[∗]_ ( _U \E_ ) _≤ ε_ . 

The set _U \E_ is open, and so by Lemma 1.2.11 is the countable union[�] _[∞] n_ =1 _[Q][n]_[of][almost][disjoint][closed][cubes.] By Lemma 1.2.9, _m[∗]_ ( _U \E_ ) =[�] _[∞] n_ =1 _[|][Q][n][|]_[.][So it will suffice to show that][ �] _[N] n_ =1 _[|][Q][n][| ≤][ε]_ for every finite _N_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

33 

The set[�] _[N] n_ =1 _[Q][n]_[is][a][finite][union][of][closed][cubes][and][is][thus] closed. It is disjoint from the compact set _E_ , so by Exercise 1.2.4 followed by Lemma 1.2.5 one has _N N m[∗]_ ( _E ∪_ � _Qn_ ) = _m[∗]_ ( _E_ ) + _m[∗]_ ( � _Qn_ ) _. n_ =1 _n_ =1 By monotonicity, the left-hand side is at most _m[∗]_ ( _U_ ), which is in turn at most _m[∗]_ ( _E_ ) + _ε_ . Since _m[∗]_ ( _E_ ) is finite, we may cancel it and conclude that _m[∗]_ ([�] _[N] n_ =1 _[Q][n]_[)] _[ ≤][ε]_[,][as][required.] 

Next, we establish Claim (v). If _E_ is Lebesgue measurable, then for every _n_ we can find an open set _Un_ containing _E_ such that _m[∗]_ ( _Un\E_ ) _≤_ 1 _/n_ . Letting _Fn_ be the complement of _Un_ , we conclude that the complement **R** _[d] \E_ of _E_ contains all of the _Fn_ , and that _m[∗]_ (( **R** _[d] \E_ ) _\Fn_ ) _≤_ 1 _/n_ . If we let _F_ :=[�] _[∞] n_ =1 _[F][n]_[,][then] **[R]** _[d][\][E]_ contains _F_ , and from monotonicity _m[∗]_ (( **R** _[d] \E_ ) _\F_ ) = 0, thus **R** _[d] \E_ is the union of _F_ and a set of Lebesgue outer measure zero. But _F_ is in turn the union of countably many closed sets _Fn_ . The claim now follows from (ii), (iii), (iv). 

Finally, Claim (vii) follows from (v), (vi), and _de Morgan’s laws_ ([�] _α∈A[E][α]_[)] _[c]_[=][�] _α∈A[E] α[c]_[,][(][�] _α∈A[E][α]_[)] _[c]_[=][�] _α∈A[E] α[c]_[,][(which][work][for] infinite unions and intersections without any difficulty). □ 

Informally, the above lemma asserts (among other things) that if one starts with such basic subsets of **R** _[d]_ as open or closed sets and then takes at most countably many boolean operations, one will always end up with a Lebesgue measurable set. This is already enough to ensure that the majority of sets that one actually encounters in real analysis will be Lebesgue measurable. (Nevertheless, using the axiom of choice one can construct sets that are not Lebesgue measurable; we will see an example of this later. As a consequence, we cannot generalise the countable closure properties here to uncountable closure properties.) 

**Remark 1.2.14.** The properties (iv), (v), (vi) of Lemma 1.2.13 assert that the collection of Lebesgue measurable subsets of **R** _[d]_ form a _σalgebra_ , which is a strengthening of the more classical concept of a 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

34 

_boolean algebra_ . We will study abstract _σ_ -algebras in more detail in Section 1.4. 

Note how this Lemma 1.2.13 is significantly stronger than the counterpart for Jordan measurability (Exercise 1.1.6), in particular by allowing countably many boolean operations instead of just finitely many. This is one of the main reasons why we use Lebesgue measure instead of Jordan measure. 

**Exercise 1.2.7** (Criteria for measurability) **.** Let _E ⊂_ **R** _[d]_ . Show that the following are equivalent: 

- (i) _E_ is Lebesgue measurable. 

- (ii) (Outer approximation by open) For every _ε >_ 0, one can contain _E_ in an open set _U_ with _m[∗]_ ( _U \E_ ) _≤ ε_ . 

- (iii) (Almost open) For every _ε >_ 0, one can find an open set _U_ such that _m[∗]_ ( _U_ ∆ _E_ ) _≤ ε_ . (In other words, _E_ differs from an open set by a set of outer measure at most _ε_ .) 

- (iv) (Inner approximation by closed) For every _ε >_ 0, one can find a closed set _F_ contained in _E_ with _m[∗]_ ( _E\F_ ) _≤ ε_ . 

- (v) (Almost closed) For every _ε >_ 0, one can find a closed set _F_ such that _m[∗]_ ( _F_ ∆ _E_ ) _≤ ε_ . (In other words, _E_ differs from a closed set by a set of outer measure at most _ε_ .) 

- (vi) (Almost measurable) For every _ε >_ 0, one can find a Lebesgue measurable set _Eε_ such that _m[∗]_ ( _Eε_ ∆ _E_ ) _≤ ε_ . (In other words, _E_ differs from a measurable set by a set of outer measure at most _ε_ .) 

( _Hint:_ Some of these deductions are either trivial or very easy. To deduce (i) from (vi), use the _ε/_ 2 _[n]_ trick to show that _E_ is contained in a Lebesgue measurable set _Eε[′]_[with] _[m][∗]_[(] _[E] ε[′]_[∆] _[E]_[)] _[≤][ε]_[,][and][then] take countable intersections to show that _E_ differs from a Lebesgue measurable set by a null set.) 

**Exercise 1.2.8.** Show that every Jordan measurable set is Lebesgue measurable. 

**Exercise 1.2.9** (Middle thirds Cantor set) **.** Let _I_ 0 := [0 _,_ 1] be the unit interval, let _I_ 1 := [0 _,_ 1 _/_ 3] _∪_ [2 _/_ 3 _,_ 1] be _I_ 0 with the interior of 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

35 

the middle third interval removed, let _I_ 2 := [0 _,_ 1 _/_ 9] _∪_ [2 _/_ 9 _,_ 1 _/_ 3] _∪_ [2 _/_ 3 _,_ 7 _/_ 9] _∪_ [8 _/_ 9 _,_ 1] be _I_ 1 with the interior of the middle third of each of the two intervals of _I_ 1 removed, and so forth. More formally, write 

**==> picture [172 x 31] intentionally omitted <==**

Let _C_ :=[�] _[∞] n_ =1 _[I][n]_[be][the][intersection][of][all][the][elementary][sets] _[I][n]_[.] Show that _C_ is compact, uncountable, and a null set. 

**Exercise 1.2.10.** (This exercise presumes some familiarity with pointset topology.) Show that the half-open interval [0 _,_ 1) cannot be expressed as the countable union of disjoint closed intervals. ( _Hint:_ It is easy to prevent [0 _,_ 1) from being expressed as the finite union of disjoint closed intervals. Next, assume for sake of contradiction that [0 _,_ 1) is the union of infinitely many closed intervals, and conclude that [0 _,_ 1) is homeomorphic to the middle thirds Cantor set, which is absurd. It is also possible to proceed using the _Baire category theorem_ ( _§_ 1.7 of _An epsilon of room_ , Vol. I.) For an additional challenge, show that [0 _,_ 1) cannot be expressed as the countable union of disjoint closed _sets_ . 

Now we look at the Lebesgue measure _m_ ( _E_ ) of a Lebesgue measurable set _E_ , which is defined to equal its Lebesgue outer measure _m[∗]_ ( _E_ ). If _E_ is Jordan measurable, we see from (1.2) that the Lebesgue measure and the Jordan measure of _E_ coincide, thus Lebesgue measure extends Jordan measure. This justifies the use of the notation _m_ ( _E_ ) to denote both Lebesgue measure of a Lebesgue measurable set, and Jordan measure of a Jordan measurable set (as well as elementary measure of an elementary set). 

Lebesgue measure obeys significantly better properties than Lebesgue outer measure, when restricted to Lebesgue measurable sets: 

**Lemma 1.2.15** (The measure axioms) **.** 

- (i) _(Empty set) m_ ( _∅_ ) = 0 _._ 

- (ii) _(Countable additivity) If E_ 1 _, E_ 2 _, . . . ⊂_ **R** _[d] is a countable sequence of disjoint Lebesgue measurable sets, then m_ ([�] _[∞] n_ =1 _[E][n]_[) =] � _∞n_ =1 _[m]_[(] _[E][n]_[)] _[.]_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

36 

**Proof.** The first claim is trivial, so we focus on the second. We deal with an easy case when all of the _En_ are compact. By repeated use of Lemma 1.2.5 and Exercise 1.2.4, we have 

**==> picture [108 x 29] intentionally omitted <==**

Using monotonicity, we conclude that 

**==> picture [108 x 30] intentionally omitted <==**

(We can use _m_ instead of _m[∗]_ throughout this argument, thanks to Lemma 1.2.13). Sending _N →∞_ we obtain 

**==> picture [108 x 28] intentionally omitted <==**

On the other hand, from countable subadditivity one has 

**==> picture [108 x 28] intentionally omitted <==**

and the claim follows. 

Next, we handle the case when the _En_ are bounded but not necessarily compact. We use the _ε/_ 2 _[n]_ trick. Let _ε >_ 0. Applying Exercise 1.2.7, we know that each _En_ is the union of a compact set _Kn_ and a set of outer measure at most _ε/_ 2 _[n]_ . Thus 

and hence 

**==> picture [134 x 58] intentionally omitted <==**

Finally, from the compact case of this lemma we already know that 

**==> picture [108 x 28] intentionally omitted <==**

while from monotonicity 

**==> picture [110 x 29] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

37 

Putting all this together we see that 

**==> picture [122 x 29] intentionally omitted <==**

for every _ε >_ 0, while from countable subadditivity we have 

**==> picture [108 x 28] intentionally omitted <==**

The claim follows. 

Finally, we handle the case when the _En_ are not assumed to be bounded or closed. Here, the basic idea is to decompose each _En_ as a countable disjoint union of bounded Lebesgue measurable sets. First, decompose **R** _[d]_ as the countable disjoint union **R** _[d]_ =[�] _[∞] m_ =1 _[A][m]_[of] bounded measurable sets _Am_ ; for instance one could take the annuli _Am_ := _{x ∈_ **R** _[d]_ : _m −_ 1 _≤|x| < m}_ . Then each _En_ is the countable disjoint union of the bounded measurable sets _En ∩ Am_ for _m_ = 1 _,_ 2 _, . . ._ , and thus 

**==> picture [118 x 28] intentionally omitted <==**

by the previous arguments. In a similar vein,[�] _[∞] n_ =1 _[E][n]_[is][the][count-] able disjoint union of the bounded measurable sets _En ∩ Am_ for _n, m_ = 1 _,_ 2 _, . . ._ , and thus 

**==> picture [227 x 45] intentionally omitted <==**

and the claim follows. 

From Lemma 1.2.15 one of course can conclude finite additivity 

**==> picture [182 x 11] intentionally omitted <==**

whenever _E_ 1 _, . . . , Ek ⊂_ **R** _[d]_ are Lebesgue measurable sets. We also have another important result: 

**Exercise 1.2.11** (Monotone convergence theorem for measurable sets) **.** 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

38 

- (i) (Upward monotone convergence) Let _E_ 1 _⊂ E_ 2 _⊂ . . . ⊂_ **R** _[n]_ be a countable non-decreasing sequence of Lebesgue measurable sets. Show that _m_ ([�] _[∞] n_ =1 _[E][n]_[)][=][lim] _[n][→∞][m]_[(] _[E][n]_[).] ( _Hint:_ Express[�] _[∞] n_ =1 _[E][n]_[as the countable union of the lacu-] nae _En\_[�] _[n] n[−][′]_ =1[1] _[E][n][′]_[.)] 

- (ii) (Downward monotone convergence) Let **R** _[d] ⊃ E_ 1 _⊃ E_ 2 _⊃ . . ._ be a countable non-increasing sequence of Lebesgue measurable sets. If at least one of the _m_ ( _En_ ) is finite, show that _m_ ([�] _[∞] n_ =1 _[E][n]_[) = lim] _[n][→∞][m]_[(] _[E][n]_[).] 

- (iii) Give a counterexample to show that the hypothesis that at least one of the _m_ ( _En_ ) is finite in the downward monotone convergence theorem cannot be dropped. 

**Exercise 1.2.12.** Show that any map _E �→ m_ ( _E_ ) from Lebesgue measurable sets to elements of [0 _,_ + _∞_ ] that obeys the above empty set and countable additivity axioms will also obey the monotonicity and countable subadditivity axioms from Exercise 1.2.3, when restricted to Lebesgue measurable sets of course. 

**Exercise 1.2.13.** We say that a sequence _En_ of sets in **R** _[d] converges pointwise_ to another set _E_ in **R** _[d]_ if the _indicator functions_ 1 _En_ converge pointwise to 1 _E_ . 

- (i) Show that if the _En_ are all Lebesgue measurable, and converge pointwise to _E_ , then _E_ is Lebesgue measurable also. ( _Hint:_ use the identity 1 _E_ ( _x_ ) = lim inf _n→∞_ 1 _En_ ( _x_ ) or 1 _E_ ( _x_ ) = lim sup _n→∞_ 1 _En_ ( _x_ ) to write _E_ in terms of countable unions and intersections of the _En_ .) 

- (ii) (Dominated convergence theorem) Suppose that the _En_ are all contained in another Lebesgue measurable set _F_ of finite measure. Show that _m_ ( _En_ ) converges to _m_ ( _E_ ). ( _Hint:_ use the upward and downward monotone convergence theorems, Exercise 1.2.11.) 

- (iii) Give a counterexample to show that the dominated convergence theorem fails if the _En_ are not contained in a set of finite measure, even if we assume that the _m_ ( _En_ ) are all uniformly bounded. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

39 

In later sections we will generalise the monotone and dominated convergence theorems to measurable functions instead of measurable sets; see Theorem 1.4.44 and Theorem 1.4.49. 

**Exercise 1.2.14.** Let _E ⊂_ **R** _[d]_ . Show that _E_ is contained in a Lebesgue measurable set of measure exactly equal to _m[∗]_ ( _E_ ). 

**Exercise 1.2.15** (Inner regularity) **.** Let _E ⊂_ **R** _[d]_ be Lebesgue measurable. Show that 

**==> picture [138 x 20] intentionally omitted <==**

**Remark 1.2.16.** The inner and outer regularity properties of measure can be used to define the concept of a _Radon measure_ (see _§_ 1.10 of _An epsilon of room, Vol. I._ ). 

**Exercise 1.2.16** (Criteria for finite measure) **.** Let _E ⊂_ **R** _[d]_ . Show that the following are equivalent: 

- (i) _E_ is Lebesgue measurable with finite measure. 

- (ii) (Outer approximation by open) For every _ε >_ 0, one can contain _E_ in an open set _U_ of finite measure with _m[∗]_ ( _U \E_ ) _≤ ε_ . 

- (iii) (Almost open bounded) _E_ differs from a bounded open set by a set of arbitrarily small Lebesgue outer measure. (In other words, for every _ε >_ 0 there exists a bounded open set _U_ such that _m[∗]_ ( _E_ ∆ _U_ ) _≤ ε_ .) 

- (iv) (Inner approximation by compact) For every _ε >_ 0, one can find a compact set _F_ contained in _E_ with _m[∗]_ ( _E\F_ ) _≤ ε_ . 

- (v) (Almost compact) _E_ differs from a compact set by a set of arbitrarily small Lebesgue outer measure. 

- (vi) (Almost bounded measurable) _E_ differs from a bounded Lebesgue measurable set by a set of arbitrarily small Lebesgue outer measure. 

- (vii) (Almost finite measure) _E_ differs from a Lebesgue measurable set with finite measure by a set of arbitrarily small Lebesgue outer measure. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

40 

- (viii) (Almost elementary) _E_ differs from an elementary set by a set of arbitrarily small Lebesgue outer measure. 

- (ix) (Almost dyadically elementary) For every _ε >_ 0, there exists an integer _n_ and a finite union _F_ of closed dyadic cubes of sidelength 2 _[−][n]_ such that _m[∗]_ ( _E_ ∆ _F_ ) _≤ ε_ . 

One can interpret the equivalence of (i) and (ix) in the above exercise as asserting that Lebesgue measurable sets are those which look (locally) “pixelated” at sufficiently fine scales. This will be formalised in later sections with the _Lebesgue differentiation theorem_ (Exercise 1.6.24). 

**Exercise 1.2.17** (Carath´eodory criterion, one direction) **.** Let _E ⊂_ **R** _[d]_ . Show that the following are equivalent: 

- (i) _E_ is Lebesgue measurable. 

- (ii) For every elementary set _A_ , one has _m_ ( _A_ ) = _m[∗]_ ( _A ∩ E_ ) + _m[∗]_ ( _A\E_ ). 

- (iii) For every box _B_ , one has _|B|_ = _m[∗]_ ( _B ∩ E_ ) + _m[∗]_ ( _B\E_ ). 

**Exercise 1.2.18** (Inner measure) **.** Let _E ⊂_ **R** _[d]_ be a bounded set. Define the _Lebesgue inner measure m∗_ ( _E_ ) of _E_ by the formula 

_m∗_ ( _E_ ) := _m_ ( _A_ ) _− m[∗]_ ( _A\E_ ) 

for any elementary set _A_ containing _E_ . 

- (i) Show that this definition is well defined, i.e. that if _A, A[′]_ are two elementary sets containing _E_ , that _m_ ( _A_ ) _− m[∗]_ ( _A\E_ ) is equal to _m_ ( _A[′]_ ) _− m[∗]_ ( _A[′] \E_ ). 

- (ii) Show that _m∗_ ( _E_ ) _≤ m[∗]_ ( _E_ ), and that equality holds if and only if _E_ is Lebesgue measurable. 

Define a _Gδ set_ to be a countable intersection[�] _[∞] n_ =1 _[U][n]_[of][open] sets, and an _Fσ set_ to be a countable union[�] _[∞] n_ =1 _[F][n]_[of][closed][sets.] 

**Exercise 1.2.19.** Let _E ⊂_ **R** _[d]_ . Show that the following are equivalent: 

- (i) _E_ is Lebesgue measurable. 

- (ii) _E_ is a _Gδ_ set with a null set removed. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

41 

## (iii) _E_ is the union of a _Fσ_ set and a null set. 

**Remark 1.2.17.** From the above exercises, we see that when describing what it means for a set to be Lebesgue measurable, there is a tradeoff between the type of approximation one is willing to bear, and the type of things one can say about the approximation. If one is only willing to approximate to within a null set, then one can only say that a measurable set is approximated by a _Gδ_ or a _Fσ_ set, which is a fairly weak amount of structure. If one is willing to add on an epsilon of error (as measured in the Lebesgue outer measure), one can make a measurable set open; dually, if one is willing to take away an epsilon of error, one can make a measurable set closed. Finally, if one is willing to both add and subtract an epsilon of error, then one can make a measurable set (of finite measure) elementary, or even a finite union of dyadic cubes. 

**Exercise 1.2.20** (Translation invariance) **.** If _E ⊂_ **R** _[d]_ is Lebesgue measurable, show that _E_ + _x_ is Lebesgue measurable for any _x ∈_ **R** _[d]_ , and that _m_ ( _E_ + _x_ ) = _m_ ( _E_ ). 

**Exercise 1.2.21** (Change of variables) **.** If _E ⊂_ **R** _[d]_ is Lebesgue measurable, and _T_ : **R** _[d] →_ **R** _[d]_ is a linear transformation, show that _T_ ( _E_ ) is Lebesgue measurable, and that _m_ ( _T_ ( _E_ )) = _|_ det _T |m_ ( _E_ ). We caution that if _T_ : **R** _[d] →_ **R** _[d][′]_ is a linear map to a space **R** _[d][′]_ of strictly smaller dimension than **R** _[d]_ , then _T_ ( _E_ ) need not be Lebesgue measurable; see Exercise 1.2.27. 

**Exercise 1.2.22.** Let _d, d[′] ≥_ 1 be natural numbers. 

- (i) If _E ⊂_ **R** _[d]_ and _F ⊂_ **R** _[d][′]_ , show that ( _m[d]_[+] _[d][′]_ ) _[∗]_ ( _E × F_ ) _≤_ ( _m[d]_ ) _[∗]_ ( _E_ )( _m[d][′]_ ) _[∗]_ ( _F_ ), where ( _m[d]_ ) _[∗]_ denotes _d_ -dimensional Lebesgue measure, etc. 

- (ii) Let _E ⊂_ **R** _[d]_ , _F ⊂_ **R** _[d][′]_ be Lebesgue measurable sets. Show that _E×F ⊂_ **R** _[d]_[+] _[d][′]_ is Lebesgue measurable, with _m[d]_[+] _[d][′]_ ( _E× F_ ) = _m[d]_ ( _E_ ) _· m[d][′]_ ( _F_ ). (Note that we allow _E_ or _F_ to have infinite measure, and so one may have to divide into cases or take advantage of the monotone convergence theorem for Lebesgue measure, Exercise 1.2.11.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

42 

**Exercise 1.2.23** (Uniqueness of Lebesgue measure) **.** Show that Lebesgue measure _E �→ m_ ( _E_ ) is the only map from Lebesgue measurable sets to [0 _,_ + _∞_ ] that obeys the following axioms: 

- (i) (Empty set) _m_ ( _∅_ ) = 0. 

- (ii) (Countable additivity) If _E_ 1 _, E_ 2 _, . . . ⊂_ **R** _[d]_ is a countable sequence of disjoint Lebesgue measurable sets, then _m_ ([�] _[∞] n_ =1 _[E][n]_[) =] � _∞n_ =1 _[m]_[(] _[E][n]_[).] 

- (iii) (Translation invariance) If _E_ is Lebesgue measurable and _x ∈_ **R** _[d]_ , then _m_ ( _E_ + _x_ ) = _m_ ( _E_ ). 

- (iv) (Normalisation) _m_ ([0 _,_ 1] _[d]_ ) = 1. 

_Hint:_ First show that _m_ must match elementary measure on elementary sets, then show that _m_ is bounded by outer measure. 

**Exercise 1.2.24** (Lebesgue measure as the completion of elementary measure) **.** The purpose of the following exercise is to indicate how Lebesgue measure can be viewed as a metric completion of elementary measure in some sense. To avoid some technicalities we will not work in all of **R** _[d]_ , but in some fixed elementary set _A_ (e.g. _A_ = [0 _,_ 1] _[d]_ ). 

- (i) Let 2 _[A]_ := _{E_ : _E ⊂ A}_ be the power set of _A_ . We say that two sets _E, F ∈_ 2 _[A]_ are _equivalent_ if _E_ ∆ _F_ is a null set. Show that this is a equivalence relation. 

- (ii) Let 2 _[A] / ∼_ be the set of equivalence classes [ _E_ ] := _{F ∈_ 2 _[A]_ : _E ∼ F }_ of 2 _[A]_ with respect to the above equivalence relation. Define a distance _d_ : 2 _[A] / ∼×_ 2 _[A] / ∼→_ **R**[+] between two equivalence classes [ _E_ ] _,_ [ _E[′]_ ] by defining _d_ ([ _E_ ] _,_ [ _E[′]_ ]) := _m[∗]_ ( _E_ ∆ _E[′]_ ). Show that this distance is well-defined (in the sense that _m_ ( _E_ ∆ _E[′]_ ) = _m_ ( _F_ ∆ _F[′]_ ) whenever [ _E_ ] = [ _F_ ] and [ _E[′]_ ] = [ _F[′]_ ]) and gives 2 _[A] / ∼_ the structure of a complete metric space. 

- (iii) Let _E ⊂_ 2 _[A]_ be the elementary subsets of _A_ , and let _L ⊂_ 2 _[A]_ be the Lebesgue measurable subsets of _A_ . Show that _L/ ∼_ is the closure of _E/ ∼_ with respect to the metric defined above. In particular, _L/ ∼_ is a complete metric space that contains _E/ ∼_ as a dense subset; in other words, _L/ ∼_ is a _metric completion_ of _E/ ∼_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

43 

- (iv) Show that Lebesgue measure _m_ : _L →_ **R**[+] descends to a continuous function _m_ : _L/ ∼→_ **R**[+] , which by abuse of notation we shall still call _m_ . Show that _m_ : _L/ ∼→_ **R**[+] is the unique continuous extension of the analogous elementary measure function _m_ : _E/ ∼→_ **R**[+] to _L/ ∼_ . 

For a further discussion of how measures can be viewed as completions of elementary measures, see _§_ 2.1 of _An epsilon of room, Vol. I_ . 

**Exercise 1.2.25.** Define a _continuously differentiable curve_ in **R** _[d]_ to be a set of the form _{γ_ ( _t_ ) : _a ≤ t ≤ b}_ where [ _a, b_ ] is a closed interval and _γ_ : [ _a, b_ ] _→_ **R** _[d]_ is a continuously differentiable function. 

- (i) If _d ≥_ 2, show that every continuously differentiable curve has Lebesgue measure zero. (Why is the condition _d ≥_ 2 necessary?) 

- (ii) Conclude that if _d ≥_ 2, then the unit cube [0 _,_ 1] _[d]_ cannot be covered by countably many continuously differentiable curves. 

We remark that if the curve is only assumed to be continuous, rather than continuously differentiable, then these claims fail, thanks to the existence of _space-filling curves_ . 

**1.2.3. Non-measurable sets.** In the previous section we have set out a rich theory of Lebesgue measure, which enjoys many nice properties when applied to Lebesgue measurable sets. 

Thus far, we have not ruled out the possibility that every single set is Lebesgue measurable. There is good reason for this: a famous theorem of Solovay[ **So1970** ] asserts that, if one is willing to drop the axiom of choice, there exist models of set theory in which all subsets of **R** _[d]_ are measurable. So any demonstration of the existence of nonmeasurable sets must use the axiom of choice in some essential way. 

That said, we can give an informal (and highly non-rigorous) motivation as to why non-measurable sets should exist, using intuition from probability theory rather than from set theory. The starting point is the observation that Lebesgue sets of finite measure (and in particular, bounded Lebesgue sets) have to be “almost elementary”, in the sense of Exercise 1.2.16. So all we need to do to build 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

44 

a non-measurable set is to exhibit a bounded set which is not almost elementary. Intuitively, we want to build a set which has oscillatory structure even at arbitrarily fine scales. 

We will non-rigorously do this as follows. We will work inside the unit interval [0 _,_ 1]. For each _x ∈_ [0 _,_ 1], we imagine that we flip a coin to give either heads or tails (with an independent coin flip for each _x_ ), and let _E ⊂_ [0 _,_ 1] be the set of all the _x ∈_ [0 _,_ 1] for which the coin flip came up heads. We suppose for contradiction that _E_ is Lebesgue measurable. Intuitively, since each _x_ had a 50% chance of being heads, _E_ should occupy about “half” of [0 _,_ 1]; applying the _law of large numbers_ (see e.g. [ **Ta2009** , _§_ 1.4]) in an extremely nonrigorous fashion, we thus expect _m_ ( _E_ ) to equal 1 _/_ 2. 

Moreover, given any subinterval [ _a, b_ ] of [0 _,_ 1], the same reasoning leads us to expect that _E ∩_ [ _a, b_ ] should occupy about half of [ _a, b_ ], so that _m_ ( _E ∩_ [ _a, b_ ]) should be _|_ [ _a, b_ ] _|/_ 2. More generally, given any elementary set _F_ in [0 _,_ 1], we should have _m_ ( _E ∩ F_ ) = _m_ ( _F_ ) _/_ 2. This makes it very hard for _E_ to be approximated by an elementary set; indeed, a little algebra then shows that _m_ ( _E_ ∆ _F_ ) = 1 _/_ 2 for any elementary _F ⊂_ [0 _,_ 1]. Thus _E_ is not Lebesgue measurable. 

Unfortunately, the above argument is terribly non-rigorous for a number of reasons, not the least of which is that it uses an uncountable number of coin flips, and the rigorous probabilistic theory that one would have to use to model such a system of random variables is too weak[12] to be able to assign meaningful probabilities to such events as “ _E_ is Lebesgue measurable”. So we now turn to more rigorous arguments that establish the existence of non-measurable sets. The arguments will be fairly simple, but the sets constructed are somewhat in nature. 

**Proposition 1.2.18.** _There exists a subset E ⊂_ [0 _,_ 1] _which is not Lebesgue measurable._ 

**Proof.** We use the fact that the rationals **Q** are an additive subgroup of the reals **R** , and so partition the reals **R** into disjoint cosets _x_ + **Q** . This creates a quotient group **R** _/_ **Q** := _{x_ + **Q** : _x ∈_ **R** _}_ . Each coset _C_ of **R** _/_ **Q** is dense in **R** , and so has a non-empty intersection 

12For some further discussion of this point, see [ **Ta2009** , _§_ 1.10]. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.2. Lebesgue measure** 

45 

with [0 _,_ 1]. Applying the axiom of choice, we may thus find an element _xC ∈ C ∩_ [0 _,_ 1] for each _C ∈_ **R** _/_ **Q** . We then let _E_ := _{xC_ : _C ∈_ **R** _/_ **Q** _}_ be the collection of all these coset representatives. By construction, _E ⊂_ [0 _,_ 1]. 

Let _y_ be any element of [0 _,_ 1]. Then it must lie in some coset _C_ of **R** _/_ **Q** , and thus differs from _xC_ by some rational number in [ _−_ 1 _,_ 1]. In other words, we have 

**==> picture [206 x 25] intentionally omitted <==**

On the other hand, we clearly have 

**==> picture [210 x 25] intentionally omitted <==**

Also, the different translates _E_ + _q_ are disjoint, because _E_ contains only one element from each coset of **Q** . 

We claim that _E_ is not Lebesgue measurable. To see this, suppose for contradiction that _E_ was Lebesgue measurable. Then the translates _E_ + _q_ would also be Lebesgue measurable. By countable additivity, we thus have 

**==> picture [194 x 24] intentionally omitted <==**

and thus by translation invariance and (1.4), (1.5) 

**==> picture [108 x 25] intentionally omitted <==**

On the other hand, the sum[�] _q∈_ **Q** _∩_ [ _−_ 1 _,_ 1] _[m]_[(] _[E]_[)][is][either][zero][(if] _m_ ( _E_ ) = 0) or infinite (if _m_ ( _E_ ) _>_ 0), leading to the desired contradiction. □ 

**Exercise 1.2.26** (Outer measure is not finitely additive) **.** Show that there exists disjoint bounded subsets _E, F_ of the real line such that _m[∗]_ ( _E ∪ F_ ) _̸_ = _m[∗]_ ( _E_ ) + _m[∗]_ ( _F_ ). ( _Hint:_ Show that the set constructed in the proof of the above proposition has positive outer measure.) 

**Exercise 1.2.27** (Projections of measurable sets need not be measurable) **.** Let _π_ : **R**[2] _→_ **R** be the coordinate projection _π_ ( _x, y_ ) := _x_ . Show that there exists a measurable subset _E_ of **R**[2] such that _π_ ( _E_ ) is not measurable. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

46 

**Remark 1.2.19.** The above discussion shows that, in the presence of the axiom of choice, one cannot hope to extend Lebesgue measure to arbitrary subsets of **R** while retaining both the countable additivity and the translation invariance properties. If one drops the translation invariant requirement, then this question concerns the theory of _measurable cardinals_ , and is not decidable from the standard ZFC axioms. On the other hand, one can construct _finitely additive_ translation invariant extensions of Lebesgue measure to the power set of **R** by use of the _Hahn-Banach theorem_ ( _§_ 1.5 of _An epsilon of room, Vol. I_ ) to extend the integration functional, though we will not do so here. 

## **1.3. The Lebesgue integral** 

In Section 1.2, we defined the _Lebesgue measure m_ ( _E_ ) of a Lebesgue measurable set _E ⊂_ **R** _[d]_ , and set out the basic properties of this measure. In this set of notes, we use Lebesgue measure to define the _Lebesgue integral_ 

**==> picture [54 x 24] intentionally omitted <==**

of functions _f_ : **R** _[d] →_ **C** _∪{∞}_ . Just as not every set can be measured by Lebesgue measure, not every function can be integrated by the Lebesgue integral; the function will need to be _Lebesgue measurable_ . Furthermore, the function will either need to be unsigned (taking values on [0 _,_ + _∞_ ]), or absolutely integrable. 

To motivate the Lebesgue integral, let us first briefly review two simpler integration concepts. The first is that of an infinite summation 

**==> picture [27 x 28] intentionally omitted <==**

of a sequence of numbers _cn_ , which can be viewed as a discrete analogue of the Lebesgue integral. Actually, there are two overlapping, but different, notions of summation that we wish to recall here. The first is that of the _unsigned infinite sum_ , when the _cn_ lie in the extended non-negative real axis [0 _,_ + _∞_ ]. In this case, the infinite sum 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

47 

can be defined as the limit of the partial sums 

**==> picture [195 x 30] intentionally omitted <==**

or equivalently as a supremum of arbitrary finite partial sums: 

**==> picture [213 x 29] intentionally omitted <==**

The unsigned infinite sum[�] _[∞] n_ =1 _[c][n]_[always][exists,][but][its][value][may] be infinite, even when each term is individually finite (consider e.g. � _∞n_ =1[1).] 

The second notion of a summation is the _absolutely summable infinite sum_ , in which the _cn_ lie in the complex plane **C** and obey the absolute summability condition 

**==> picture [58 x 28] intentionally omitted <==**

where the left-hand side is of course an unsigned infinite sum. When this occurs, one can show that the partial sums[�] _[N] n_ =1 _[c][n]_[converge][to] a limit, and we can then define the infinite sum by the same formula (1.6) as in the unsigned case, though now the sum takes values in **C** rather than [0 _,_ + _∞_ ]. The absolute summability condition confers a number of useful properties that are not obeyed by sums that are merely conditionally convergent; most notably, the value of an absolutely convergent sum is unchanged if one rearranges the terms in the series in an arbitrary fashion. Note also that the absolutely summable infinite sums can be defined in terms of the unsigned infinite sums by taking advantage of the formulae 

**==> picture [164 x 28] intentionally omitted <==**

for complex absolutely summable _cn_ , and 

**==> picture [108 x 29] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

48 

for real absolutely summable _cn_ , where _c_[+] _n_[:=][max(] _[c][n][,]_[ 0)][and] _[c][−] n_[:=] max( _−cn,_ 0) are the (magnitudes of the) positive and negative parts of _cn_ . 

In an analogous spirit, we will first define an _unsigned Lebesgue integral_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[of][(measurable)][unsigned][functions] _[f]_[ :] **[R]** _[d][→]_ [0 _,_ + _∞_ ], and then use that to define the _absolutely convergent Lebesgue integral_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[of] _[absolutely][integrable]_[functions] _[f]_[ :] **[R]** _[d][→]_ **[C]** _[ ∪] {∞}_ . (In contrast to absolutely summable series, which cannot have any infinite terms, absolutely integrable functions will be allowed to occasionally become infinite. However, as we will see, this can only happen on a set of Lebesgue measure zero.) 

To define the unsigned Lebesgue integral, we now turn to another _b_ more basic notion of integration, namely the � _a[f]_[(] _[x]_[)] _[ dx]_[ of a Riemann] integrable function _f_ : [ _a, b_ ] _→_ **R** . Recall from Section 1.1 that this integral is equal to the _lower Darboux integral_ 

**==> picture [288 x 29] intentionally omitted <==**

(It is also equal to the upper Darboux integral; but much as the theory of Lebesgue measure is easiest to define by relying solely on outer measure and not on inner measure, the theory of the unsigned Lebesgue integral is easiest to define by relying solely on lower integrals rather than upper ones; the upper integral is somewhat problematic when dealing with “improper” integrals of functions that are unbounded or are supported on sets of infinite measure.) Compare this formula _b_ also with (1.7). The integral p.c. � _a[g]_[(] _[x]_[)] _[dx]_[is][a] _[piecewise][constant]_ integral, formed by breaking up the piecewise constant functions _g, h_ into finite linear combinations of _indicator functions_ 1 _I_ of intervals _I_ , and then measuring the length of each interval. 

It turns out that virtually the same definition allows us to define a _lower Lebesgue integral_ � **R** _[d] f_ ( _x_ ) _dx_ of any unsigned function _f_ : **R** _[d] →_ [0 _,_ + _∞_ ], simply by replacing intervals with the more general class of Lebesgue measurable sets (and thus replacing piecewise constant functions with the more general class of _simple functions_ ). If the function is _Lebesgue measurable_ (a concept that we will define presently), then we refer to the lower Lebesgue integral simply as the 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

49 

_Lebesgue integral_ . As we shall see, it obeys all the basic properties one expects of an integral, such as monotonicity and additivity; in subsequent notes we will also see that it behaves quite well with respect to limits, as we shall see by establishing the two basic convergence theorems of the unsigned Lebesgue integral, namely _Fatou’s lemma_ (Corollary 1.4.47) and the _monotone convergence theorem_ (Theorem 1.4.44). 

Once we have the theory of the unsigned Lebesgue integral, we will then be able to define the absolutely convergent Lebesgue integral, similarly to how the absolutely convergent infinite sum can be defined using the unsigned infinite sum. This integral also obeys all the basic properties one expects, such as linearity and compatibility with the more classical Riemann integral; in subsequent notes we will see that it also obeys a fundamentally important convergence theorem, the _dominated convergence theorem_ (Theorem 1.4.49). This convergence theorem makes the Lebesgue integral (and its abstract generalisations to other measure spaces than **R** _[d]_ ) particularly suitable for analysis, as well as allied fields that rely heavily on limits of functions, such as PDE, probability, and ergodic theory. 

**Remark 1.3.1.** This is not the only route to setting up the unsigned and absolutely convergent Lebesgue integrals. For instance, one can proceed with the unsigned integral but then making an auxiliary stop at integration of functions that are bounded and are supported on a set of finite measure, before going to the absolutely convergent Lebesgue integral; see e.g. [ **StSk2005** ]. Another approach (which will not be discussed here) is to take the metric completion of the Riemann integral with respect to the _L_[1] metric. 

The Lebesgue integral and Lebesgue measure can be viewed as _completions_ of the Riemann integral and Jordan measure respectively. This means three things. Firstly, the Lebesgue theory _extends_ the Riemann theory: every Jordan measurable set is Lebesgue measurable, and every Riemann integrable function is Lebesgue measurable, with the measures and integrals from the two theories being compatible. Conversely, the Lebesgue theory can be _approximated_ by the Riemann theory; as we saw in Section 1.2, every Lebesgue measurable set can be approximated (in various senses) by simpler sets, such 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

50 

as open sets or elementary sets, and in a similar fashion, Lebesgue measurable functions can be approximated by nicer functions, such as Riemann integrable or continuous functions. Finally, the Lebesgue theory is _complete_ in various ways; this is formalised in _§_ 1.3 of _An epsilon of room, Vol. I_ , but the convergence theorems mentioned above already hint at this completeness. A related fact, known as _Egorov’s theorem_ , asserts that a pointwise converging sequence of functions can be approximated as a (locally) uniformly converging sequence of functions. The facts listed here manifestations of _Littlewood’s three principles of real analysis_ (Section 1.3.5), which capture much of the essence of the Lebesgue theory. 

**1.3.1. Integration of simple functions.** Much as the Riemann integral was set up by first using the integral for piecewise constant functions, the Lebesgue integral is set up using the integral for simple functions. 

**Definition 1.3.2** (Simple function) **.** A (complex-valued) _simple function f_ : **R** _[d] →_ **C** is a finite linear combination 

**==> picture [201 x 11] intentionally omitted <==**

of indicator functions 1 _Ei_ of Lebesgue measurable sets _Ei ⊂_ **R** _[d]_ for _i_ = 1 _, . . . , k_ , where _k ≥_ 0 is a natural number and _c_ 1 _, . . . , ck ∈_ **C** are complex numbers. An _unsigned simple function f_ : **R** _[d] →_ [0 _,_ + _∞_ ], is defined similarly, but with the _ci_ taking values in [0 _,_ + _∞_ ] rather than **C** . 

It is clear from construction that the space Simp( **R** _[d]_ ) of complexvalued simple functions forms a complex vector space; also, Simp( **R** _[d]_ ) also closed under pointwise product _f, g �→ fg_ and complex conjugation _f �→ f_ . In short, Simp( **R** _[d]_ ) is a _commutative ∗-algebra_ . Meanwhile, the space Simp[+] ( **R** _[d]_ ) of unsigned simple functions is a [0 _,_ + _∞_ ]- module; it is closed under addition, and under scalar multiplication by elements in [0 _,_ + _∞_ ]. 

In this definition, we did not require the _E_ 1 _, . . . , Ek_ to be disjoint. However, it is easy enough to arrange this, basically by exploiting Venn diagrams (or, to use fancier language, finite boolean algebras). Indeed, any _k_ subsets _E_ 1 _, . . . , Ek_ of **R** _[d]_ partition **R** _[d]_ into 2 _[k]_ disjoint 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

51 

sets, each of which is an intersection of _Ei_ or the complement **R** _[d] \Ei_ for _i_ = 1 _, . . . , k_ (and in particular, is measurable). The (complex or unsigned) simple function is constant on each of these sets, and so can easily be decomposed as a linear combination of the indicator function of these sets. One easy consequence of this is that if _f_ is a complexvalued simple function, then its absolute value _|f |_ : _x �→|f_ ( _x_ ) _|_ is an unsigned simple function. 

It is geometrically intuitive that we should define the integral � **R** _[d]_[ 1] _[E]_[(] _[x]_[)] _[dx]_[of][an][indicator][function][of][a][measurable][set] _[E]_[to][equal] _m_ ( _E_ ): 

**==> picture [100 x 24] intentionally omitted <==**

Using this and applying the laws of integration formally, we are led to propose the following definition for the integral of an unsigned simple function: 

**Definition 1.3.3** (Integral of a unsigned simple function) **.** If _f_ = _c_ 11 _E_ 1+ _. . ._ + _ck_ 1 _Ek_ is an unsigned simple function, the integral Simp � **R** _[d][ f]_[(] _[x]_[)] _[ dx]_ is defined by the formula 

**==> picture [253 x 41] intentionally omitted <==**

However, one has to actually check that this definition is welldefined, in the sense that different representations 

**==> picture [207 x 14] intentionally omitted <==**

of a function as a finite unsigned combination of indicator functions of measurable sets will give the same value for the integral Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[.][This][is][the][purpose][of][the][following][lemma:] 

**Lemma 1.3.4** (Well-definedness of simple integral) **.** _Let k, k[′] ≥_ 0 _be natural numbers, c_ 1 _, . . . , ck, c[′]_ 1 _[, . . . , c][′] k[′][∈]_[[0] _[,]_[ +] _[∞]_[]] _[, and let][ E]_[1] _[, . . . , E][k][, E]_ 1 _[′][, . . . , E] k[′][′][⊂]_ **R** _[d] be Lebesgue measurable sets such that the identity_ 

**==> picture [243 x 30] intentionally omitted <==**

**==> picture [244 x 12] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

52 

**Proof.** We again use a Venn diagram argument. The _k_ + _k[′]_ sets _E_ 1 _, . . . , Ek, E_ 1 _[′][, . . . , E] k[′][′]_[partition] **[R]** _[d]_[into][2] _[k]_[+] _[k][′]_[disjoint][sets,][each][of] which is an intersection of some of the _E_ 1 _, . . . , Ek, E_ 1 _[′][, . . . , E] k[′][′]_[and] their complements. We throw away any sets that are empty, leaving us with a partition of **R** _[d]_ into _m_ non-empty disjoint sets _A_ 1 _, . . . , Am_ for some 0 _≤ m ≤_ 2 _[k]_[+] _[k][′]_ . As the _E_ 1 _, . . . , Ek, E_ 1 _[′][, . . . , E] k[′]_[are][Lebesgue] measurable, the _A_ 1 _, . . . , Am_ are too. By construction, each of the _E_ 1 _, . . . , Ek, E_ 1 _[′][, . . . , E][k][′]_[arise][as][unions][of][some][of][the] _[A]_[1] _[, . . . , A][m]_[,] thus we can write 

**==> picture [54 x 24] intentionally omitted <==**

and 

**==> picture [65 x 26] intentionally omitted <==**

for all _i_ = 1 _, . . . , k_ and _i[′]_ = 1 _, . . . , k[′]_ , and some subsets _Ji, Ji[′][′][⊂] {_ 1 _, . . . , m}_ . By finite additivity of Lebesgue measure, we thus have 

**==> picture [88 x 24] intentionally omitted <==**

and 

**==> picture [94 x 26] intentionally omitted <==**

Thus, our objective is now to show that 

**==> picture [234 x 35] intentionally omitted <==**

To obtain this, we fix 1 _≤ j ≤ m_ and evaluate (1.9) at a point _x_ in the non-empty set _Aj_ . At such a point, 1 _Ei_ ( _x_ ) is equal to 1 _Ji_ ( _j_ ), and similarly 1 _Ei[′][′]_[is][equal][to][1] _[J] i[′][′]_[(] _[j]_[).][From][(1.9)][we][conclude][that] 

**==> picture [122 x 31] intentionally omitted <==**

Multiplying this by _m_ ( _Aj_ ) and then summing over all _j_ = 1 _, . . . , m_ we obtain (1.10). □ 

We now make some important definitions that we will use repeatedly in this text: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

53 

**Definition 1.3.5** (Almost everywhere and support) **.** A property _P_ ( _x_ ) of a point _x ∈_ **R** _[d]_ is said to hold _(Lebesgue) almost everywhere_ in **R** _[d]_ , or _for (Lebesgue) almost every point x ∈_ **R** _[d]_ , if the set of _x ∈_ **R** _[d]_ for which _P_ ( _x_ ) fails has Lebesgue measure zero (i.e. _P_ is true outside of a null set). We usually omit the prefix Lebesgue, and often abbreviate “almost everywhere” or “almost every” as a.e. 

Two functions _f, g_ : **R** _[d] → Z_ into an arbitrary range _Z_ are said to _agree almost everywhere_ if one has _f_ ( _x_ ) = _g_ ( _x_ ) for almost every _x ∈_ **R** _[d]_ . 

The _support_ of a function _f_ : **R** _[d] →_ **C** or _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is defined to be the set _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _̸_ = 0 _}_ where _f_ is non-zero. 

Note that if _P_ ( _x_ ) holds for almost every _x_ , and _P_ ( _x_ ) implies _Q_ ( _x_ ), then _Q_ ( _x_ ) holds for almost every _x_ . Also, if _P_ 1( _x_ ) _, P_ 2( _x_ ) _, . . ._ are an at most countable family of properties, each of which individually holds for almost every _x_ , then they will _simultaneously_ be true for almost every _x_ , because the countable union of null sets is still a null set. Because of these properties, one can (as a rule of thumb) treat the almost universal quantifier “for almost every” as if it was the truly universal quantifier “for every”, as long as one is only concatenating at most countably many properties together, and as long as one never specialises the free variable _x_ to a null set. Observe also that the property of agreeing almost everywhere is an equivalence relation, which we will refer to as _almost everywhere equivalence_ . 

In _An epsilon of room, Vol. I_ we will also see the notion of the _closed support_ of a function _f_ : **R** _[d] →_ **C** , defined as the closure of the support. 

The following properties of the simple unsigned integral are easily obtained from the 

**Exercise 1.3.1** (Basic properties of the simple unsigned integral) **.** Let _f, g_ : **R** _[d] →_ [0 _,_ + _∞_ ] be simple unsigned functions. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

54 

## (i) (Unsigned linearity) We have 

**==> picture [204 x 51] intentionally omitted <==**

**==> picture [203 x 54] intentionally omitted <==**

- (ii) (Finiteness) We have Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx][<][∞]_[if][and][only] if _f_ is finite almost everywhere, and its support has finite measure. 

- (iii) (Vanishing) We have Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[=][0][if][and][only][if] _[f]_ is zero almost everywhere. 

- (iv) (Equivalence) If _f_ and _g_ agree almost everywhere, then Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[ = Simp] � **R** _[d][ g]_[(] _[x]_[)] _[dx]_[.] 

- (v) (Monotonicity) If _f_ ( _x_ ) _≤ g_ ( _x_ ) for almost every _x ∈_ **R** _[d]_ , then Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx][ ≤]_[Simp] � **R** _[d][ g]_[(] _[x]_[)] _[dx]_[.] 

- (vi) (Compatibility with Lebesgue measure) For any Lebesgue measurable _E_ , one has Simp � **R** _[d]_[ 1] _[E]_[(] _[x]_[)] _[dx]_[ =] _[ m]_[(] _[E]_[).] 

Furthermore, show that the simple unsigned integral _f �→_ Simp � **R** _[d][ f]_[(] _[x]_[)] _[ dx]_ is the only map from the space Simp[+] ( **R** _[d]_ ) of unsigned simple functions to [0 _,_ + _∞_ ] that obeys all of the above properties. 

We can now define an absolutely convergent counterpart to the simple unsigned integral. This integral will soon be superceded by the absolutely Lebesgue integral, but we give it here as motivation for that more general notion of integration. 

**Definition 1.3.6** (Absolutely convergent simple integral) **.** A complexvalued simple function _f_ : **R** _[d] →_ **C** is said to be _absolutely integrable_ of Simp � **R** _[d][ |][f]_[(] _[x]_[)] _[|][dx <][ ∞]_[.][If] _[f]_[is][absolutely][integrable,][the][integral] Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[is][defined][for][real][signed] _[f]_[by][the][formula] 

**==> picture [268 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

55 

where _f_ +( _x_ ) := max( _f_ ( _x_ ) _,_ 0) and _f−_ ( _x_ ) := max( _−f_ ( _x_ ) _,_ 0) (note that these are unsigned simple functions that are pointwise dominated by _|f |_ and thus have finite integral), and for complex-valued _f_ by the formula[13] 

**==> picture [196 x 51] intentionally omitted <==**

Note from the preceding exercise that a complex-valued simple function _f_ is absolutely integrable if and only if it has finite measure support (since finiteness almost everywhere is automatic). In particular, the space Simp _[abs]_ ( **R** _[d]_ ) of absolutely integrable simple functions is closed under addition and scalar multiplication by complex numbers, and is thus a complex vector space. 

The properties of the unsigned simple integral then can be used to deduce analogous properties for the complex-valued integral: 

**Exercise 1.3.2** (Basic properties of the complex-valued simple integral) **.** Let _f, g_ : **R** _[d] →_ **C** be absolutely integrable simple functions. 

(i) (*-linearity) We have 

**==> picture [204 x 51] intentionally omitted <==**

and 

**==> picture [244 x 67] intentionally omitted <==**

(ii) (Equivalence) If _f_ and _g_ agree almost everywhere, then Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[ = Simp] � **R** _[d][ g]_[(] _[x]_[)] _[dx]_[.] 

13Strictly speaking, this is an abuse of notation as we have now defined the simple integral Simp � **R** _[d]_[three][different][times,][for][unsigned,][real][signed,][and][complex-valued] simple functions, but one easily verifies that these three definitions agree with each other on their common domains of definition, so it is safe to use a single notation for all three. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

56 

(iii) (Compatibility with Lebesgue measure) For any Lebesgue measurable _E_ , one has Simp � **R** _[d]_[ 1] _[E]_[(] _[x]_[)] _[dx]_[ =] _[ m]_[(] _[E]_[).] 

( _Hints:_ Work out the real-valued counterpart of the linearity property first. To establish (1.11), treat the cases _c >_ 0 _, c_ = 0 _, c_ = _−_ 1 separately. To deal with the additivity for real functions _f, g_ , start with the identity 

**==> picture [236 x 11] intentionally omitted <==**

and rearrange the second inequality so that no subtraction appears.) Furthermore, show that the complex-valued simple integral _f �→_ Simp � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[is][the][only][map][from][the][space][Simp] _[abs]_[(] **[R]** _[d]_[)][of][ab-] solutely integrable simple functions to **C** that obeys all of the above properties. 

We now comment further on the fact that (simple) functions that agree almost everywhere, have the same integral. We can view this as an assertion that integration is a _noise-tolerant_ operation: one can have “noise” or “errors” in a function _f_ ( _x_ ) on a null set, and this will not affect the final value of the integral. Indeed, once one has this noise tolerance, one can even integrate functions _f_ that are not defined _everywhere_ on **R** _[d]_ , but merely defined _almost everywhere_ on **R** _[d]_ (i.e. _f_ is defined on some set **R** _[d] \N_ where _N_ is a null set), simply by extending _f_ to all of **R** _[d]_ in some arbitrary fashion (e.g. by setting _f_ equal to zero on _N_ ). This is extremely convenient for analysis, as there are many natural functions (e.g.[sin] _x[ x]_ in one dimension, or _|x_ 1 _|[α]_ for various _α >_ 0 in higher dimensions) that are only defined almost everywhere instead of everywhere (often due to “division by zero” problems when a denominator vanishes). While such functions cannot be evaulated at certain singular points, they can still be integrated (provided they obey some integrability condition, of course, such as absolute integrability), and so one can still perform a large portion of analysis on such functions. 

In fact, in the subfield of analysis known as _functional analysis_ , it is convenient to abstract the notion of an almost everywhere defined function somewhat, by replacing any such function _f_ with the _equivalence class_ of almost everywhere defined functions that are equal to _f_ almost everywhere. Such classes are then no longer functions in the 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

57 

standard set-theoretic sense (they do not map each point in the domain to a unique point in the range, since points in **R** _[d]_ have measure zero), but the properties of various function spaces improve when one does this (various semi-norms become norms, various topologies become Hausdorff, and so forth). See _§_ 1.3 of _An epsilon of room, Vol. I_ for further discussion. 

**Remark 1.3.7.** The “Lebesgue philosophy” that one is willing to lose control on sets of measure zero is a perspective that distinguishes Lebesgue-type analysis from other types of analysis, most notably that of _descriptive set theory_ , which is also interested in studying subsets of **R** _[d]_ , but can give completely different structural classifications to a pair of sets that agree almost everywhere. This loss of control on null sets is the price one has to pay for gaining access to the powerful tool of the Lebesgue integral; if one needs to control a function at absolutely _every_ point, and not just almost every point, then one often needs to use other tools than integration theory (unless one has some regularity on the function, such as continuity, that lets one pass from almost everywhere true statements to everywhere true statements). 

**1.3.2. Measurable functions.** Much as the piecewise constant integral can be completed to the Riemann integral, the unsigned simple integral can be completed to the unsigned Lebesgue integral, by extending the class of unsigned simple functions to the larger class of unsigned Lebesgue measurable functions. One of the shortest ways to this class is as follows: 

**Definition 1.3.8** (Unsigned measurable function) **.** An unsigned function _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is _unsigned Lebesgue measurable_ , or _measurable_ for short, if it is the pointwise limit of unsigned simple functions, i.e. if there exists a sequence _f_ 1 _, f_ 2 _, f_ 3 _, . . ._ : **R** _[d] →_ [0 _,_ + _∞_ ] of unsigned simple functions such that _fn_ ( _x_ ) _→ f_ ( _x_ ) for every _x ∈_ **R** _[d]_ . 

This particular definition is not always the most tractable. Fortunately, it has many equivalent forms: 

**Lemma 1.3.9** (Equivalent notions of measurability) **.** _Let f_ : **R** _[d] →_ [0 _,_ + _∞_ ] _be an unsigned function. Then the following are equivalent:_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

58 

- (i) _f is unsigned Lebesgue measurable._ 

- (ii) _f is the pointwise limit of unsigned simple functions fn (thus the limit_ lim _n→∞ fn_ ( _x_ ) _exists and is equal to f_ ( _x_ ) _for all x ∈_ **R** _[d] )._ 

- (iii) _f is the pointwise almost everywhere limit of unsigned simple functions fn (thus the limit_ lim _n→∞ fn_ ( _x_ ) _exists and is equal to f_ ( _x_ ) _for almost every x ∈_ **R** _[d] )._ 

- (iv) _f is the supremum f_ ( _x_ ) = sup _n fn_ ( _x_ ) _of an increasing sequence_ 0 _≤ f_ 1 _≤ f_ 2 _≤ . . . of unsigned simple functions fn, each of which are bounded with finite measure support._ 

- (v) _For every λ ∈_ [0 _,_ + _∞_ ] _, the set {x ∈_ **R** _[d]_ : _f_ ( _x_ ) _> λ} is Lebesgue measurable._ 

- (vi) _For every λ ∈_ [0 _,_ + _∞_ ] _, the set {x ∈_ **R** _[d]_ : _f_ ( _x_ ) _≥ λ} is Lebesgue measurable._ 

- (vii) _For every λ ∈_ [0 _,_ + _∞_ ] _, the set {x ∈_ **R** _[d]_ : _f_ ( _x_ ) _< λ} is Lebesgue measurable._ 

- (ix) _For every λ ∈_ [0 _,_ + _∞_ ] _, the set {x ∈_ **R** _[d]_ : _f_ ( _x_ ) _≤ λ} is Lebesgue measurable._ 

- (x) _For every interval I ⊂_ [0 _,_ + _∞_ ) _, the set f[−]_[1] ( _I_ ) := _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _∈ I} is Lebesgue measurable._ 

- (xi) _For every (relatively) open set U ⊂_ [0 _,_ + _∞_ ) _, the set f[−]_[1] ( _U_ ) := _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _∈ U } is Lebesgue measurable._ 

- (xii) _For every (relatively) closed set K ⊂_ [0 _,_ + _∞_ ) _, the set f[−]_[1] ( _K_ ) := _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _∈ K} is Lebesgue measurable._ 

**Proof.** (i) and (ii) are equivalent by definition. (ii) clearly implies (iii). As every monotone sequence in [0 _,_ + _∞_ ] converges, (iv) implies (ii). Now we show that (iii) implies (v). If _f_ is the pointwise almost everywhere limit of _fn_ , then for almost every _x ∈_ **R** _[d]_ one has 

**==> picture [228 x 18] intentionally omitted <==**

This implies that, for any _λ_ , the set _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _> λ}_ is equal to 

**==> picture [176 x 27] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

59 

outside of a set of measure zero; this set in turn is equal to 

**==> picture [176 x 27] intentionally omitted <==**

outside of a set of measure zero. But as each _fn_ is an unsigned simple 1 function, the sets _{x ∈_ **R** _[d]_ : _fn_ ( _x_ ) _> λ_ + _M[}]_[are][Lebesgue][measur-] able. Since countable unions or countable intersections of Lebesgue measurable sets are Lebesgue measurable, and modifying a Lebesgue measurable set on a null set produces another Lebesgue measurable set, we obtain (v). 

To obtain the equivalence of (v) and (vi), observe that 

**==> picture [238 x 24] intentionally omitted <==**

for _λ ∈_ (0 _,_ + _∞_ ] and 

**==> picture [238 x 24] intentionally omitted <==**

_λ ∈_ [0 _,_ + _∞_ ), where **Q**[+] := **Q** _∩_ [0 _,_ + _∞_ ] are the non-negative rationals. The claim then easily follows from the countable nature of **Q**[+] (treating the extreme cases _λ_ = 0 _,_ + _∞_ separately if necessary). A similar argument lets one deduce (v) or (vi) from (ix). 

The equivalence of (v), (vi) with (vii), (viii) comes from the observation that _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _≤ λ}_ is the complement of _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _> λ}_ , and _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _< λ}_ is the complement of _{x ∈_ **R** _[d]_ : _f_ ( _x_ ) _≥ λ}_ . A similar argument shows that (x) and (xi) are equivalent. 

By expressing an interval as the intersection of two half-intervals, we see that (ix) follows from (v)-(viii), and so all of (v)-(ix) are now shown to be equivalent. 

Clearly (x) implies (vii), and hence (v)-(ix). Conversely, because every open set in [0 _,_ + _∞_ ) is the union of countably many open intervals in [0 _,_ + _∞_ ), (ix) implies (x). 

The only remaining task is to show that (v)-(xi) implies (iv). Let _f_ obey (v)-(xi). For each positive integer _n_ , we let _fn_ ( _x_ ) be defined to be the largest integer multiple of 2 _[−][n]_ that is less than or equal to min( _f_ ( _x_ ) _, n_ ) when _|x| ≤ n_ , with _fn_ ( _x_ ) := 0 for _|x| > n_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

60 

From construction it is easy to see that the _fn_ : **R** _[d] →_ [0 _,_ + _∞_ ] are increasing and have _f_ as their supremum. Furthermore, each _fn_ takes on only finitely many values, and for each non-zero value _c_ it attains, the set _fn[−]_[1][(] _[c]_[)][takes][the][form] _[f][ −]_[1][(] _[I][c]_[)] _[ ∩{][x][∈]_ **[R]** _[d]_[:] _[|][x][|][≤][n][}]_[for][some] interval or ray _Ic_ , and is thus measurable. As a consequence, _fn_ is a simple function, and by construction it is bounded and has finite measure support. The claim follows. □ 

With these equivalent formulations, we can now generate plenty of measurable functions: 

## **Exercise 1.3.3.** 

- (i) Show that every continuous function _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable. 

- (ii) Show that every unsigned simple function is measurable. 

- (iii) Show that the supremum, infimum, limit superior, or limit inferior of unsigned measurable functions is unsigned measurable. 

- (iv) Show that an unsigned function that is equal almost everywhere to an unsigned measurable function, is itself measurable. 

- (v) Show that if a sequence _fn_ of unsigned measurable functions converges pointwise almost everywhere to an unsigned limit _f_ , then _f_ is also measurable. 

- (vi) If _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable and _φ_ : [0 _,_ + _∞_ ] _→_ [0 _,_ + _∞_ ] is continuous, show that _φ ◦ f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable. 

- (vii) If _f, g_ are unsigned measurable functions, show that _f_ + _g_ and _fg_ are measurable. 

In view of Exercise 1.3.3(iv), one can define the concept of measurability for an unsigned function that is only defined almost everywhere on **R** _[d]_ , rather than everywhere on **R** _[d]_ , by extending that function arbitrarily to the null set where it is currently undefined. 

**Exercise 1.3.4.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ]. Show that _f_ is a _bounded_ unsigned measurable function if and only if _f_ is the _uniform_ limit of _bounded_ simple functions. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

61 

**Exercise 1.3.5.** Show that an unsigned function _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is a simple function if and only if it is measurable and takes on at most finitely many values. 

**Exercise 1.3.6.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be an unsigned measurable function. Show that the region _{_ ( _x, t_ ) _∈_ **R** _[d] ×_ **R** : 0 _≤ t ≤ f_ ( _x_ ) _}_ is a measurable subset of **R** _[d]_[+1] . (There is a converse to this statement, but we will wait until Exercise 1.7.24 to prove it, once we have the Fubini-Tonelli theorem (Corollary 1.7.23) available to us.) 

**Remark 1.3.10.** Lemma 1.3.9 tells us that if _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable, then _f[−]_[1] ( _E_ ) is Lebesgue measurable for many classes of sets _E_ . However, we caution that it is _not_ necessarily the case that _f[−]_[1] ( _E_ ) is Lebesgue measurable if _E_ is Lebesgue measurable. To see this, we let _C_ be the Cantor set 

**==> picture [168 x 30] intentionally omitted <==**

and let _f_ : **R** _→_ [0 _,_ + _∞_ ] be the function defined by setting 

**==> picture [81 x 29] intentionally omitted <==**

whenever _x ∈_ [0 _,_ 1] is not a terminating binary decimal, and so has a unique binary expansion _x_ =[�] _[∞] j_ =1 _[b][j]_[2] _[−][j]_[for][some] _[b][j][∈{]_[0] _[,]_[ 1] _[}]_[,][and] _f_ ( _x_ ) := 0 otherwise. We thus see that _f_ takes values in _C_ , and is bijective on the set _A_ of non-terminating decimals in [0 _,_ 1]. Using Lemma 1.3.9, it is not difficult to show that _f_ is measurable. On the other hand, by modifying the construction from the previous notes, we can find a subset _F_ of _A_ which is non-measurable. If we set _E_ := _f_ ( _F_ ), then _E_ is a subset of the null set _C_ and is thus itself a null set; but _f[−]_[1] ( _E_ ) = _F_ is non-measurable, and so the inverse image of a Lebesgue measurable set by a measurable function need not remain Lebesgue measurable. 

However, we will later see that it is still true that _f[−]_[1] ( _E_ ) is Lebesgue measurable if _E_ has a slightly stronger measurability property than Lebesgue measurability, namely _Borel measurability_ ; see Exercise 1.4.29(iii). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

62 

Now we can define the concept of a complex-valued measurable function. As discussed earlier, it will be convenient to allow for such functions to only be defined _almost everywhere_ , rather than _everywhere_ , to allow for the possibility that the function becomes singular or otherwise on a null set. 

**Definition 1.3.11** (Complex measurability) **.** An almost everywhere defined complex-valued function _f_ : **R** _[d] →_ **C** is _Lebesgue measurable_ , or _measurable_ for short, if it is the pointwise almost everywhere limit of complex-valued simple functions. 

As before, there are several equivalent definitions: 

**Exercise 1.3.7.** Let _f_ : **R** _[d] →_ **C** be an almost everywhere defined complex-valued function. Then the following are equivalent: 

- (i) _f_ is measurable. 

- (ii) _f_ is the pointwise almost everywhere limit of complex-valued simple functions. 

- (iii) The (magnitudes of the) positive and negative parts of Re( _f_ ) and Im( _f_ ) are unsigned measurable functions. 

- (iv) _f[−]_[1] ( _U_ ) is Lebesgue measurable for every open set _U ⊂_ **C** . 

- (v) _f[−]_[1] ( _K_ ) is Lebesgue measurable for every closed set _K ⊂_ **C** . 

From the above exercise, we see that the notion of complex-valued measurability and unsigned measurability are compatible when applied to a function that takes values in [0 _,_ + _∞_ ) = [0 _,_ + _∞_ ] _∩_ **C** everywhere (or almost everywhere). 

## **Exercise 1.3.8.** 

- (i) Show that every continuous function _f_ : **R** _[d] →_ **C** is measurable. 

- (ii) Show that a function _f_ : **R** _[d] →_ **C** is simple if and only if it is measurable and takes on at most finitely many values. 

- (iii) Show that a complex-valued function that is equal almost everywhere to an measurable function, is itself measurable. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

63 

- (iv) Show that if a sequence _fn_ of complex-valued measurable functions converges pointwise almost everywhere to an complexvalued limit _f_ , then _f_ is also measurable. 

- (v) If _f_ : **R** _[d] →_ **C** is measurable and _φ_ : **C** _→_ **C** is continuous, show that _φ ◦ f_ : **R** _[d] →_ **C** is measurable. 

- (vi) If _f, g_ are measurable functions, show that _f_ + _g_ and _fg_ are measurable. 

**Exercise 1.3.9.** Let _f_ : [ _a, b_ ] _→_ **R** be a Riemann integrable function. Show that if one extends _f_ to all of **R** by defining _f_ ( _x_ ) = 0 for _x ̸∈_ [ _a, b_ ], then _f_ is measurable. 

**1.3.3. Unsigned Lebesgue integrals.** We are now ready to integrate unsigned measurable functions. We begin with the notion of the lower unsigned Lebesgue integral, which can be defined for arbitrary unsigned functions (not necessarily measurable): 

**Definition 1.3.12** (Lower unsigned Lebesgue integral) **.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be an unsigned function (not necessarily measurable). We define the _lower unsigned Lebesgue integral_ � **R** _[d] f_ ( _x_ ) _dx_ to be the quantity 

**==> picture [208 x 27] intentionally omitted <==**

where _g_ ranges over all unsigned simple functions _g_ : **R** _[d] →_ [0 _,_ + _∞_ ] that are pointwise bounded by _f_ . 

One can also define the _upper unsigned Lebesgue integral_ 

**==> picture [198 x 26] intentionally omitted <==**

but we will use this integral much more rarely. Note that both integrals take values in [0 _,_ + _∞_ ], and that the upper Lebesgue integral is always at least as large as the lower Lebesgue integral. 

In the definition of the lower unsigned Lebesgue integral, _g_ is required to be bounded by _f_ pointwise everywhere, but it is easy to see that one could also require _g_ to just be bounded by _f_ pointwise almost everywhere without affecting the value of the integral, since 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

64 

the simple integral is not affected by modifications on sets of measure zero. 

The following properties of the lower Lebesgue integral are easy to establish: 

**Exercise 1.3.10** (Basic properties of the lower Lebesgue integral) **.** Let _f, g_ : **R** _[d] →_ [0 _,_ + _∞_ ] be unsigned functions (not necessarily measurable). 

- (i) (Compatibility with the simple integral) If _f_ is simple, then � **R** _[d] f_ ( _x_ ) _dx_ = � **R** _[d][f]_[(] _[x]_[)] _[dx]_[ = Simp] � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[.] 

- (ii) (Monotonicity) If _f ≤ g_ pointwise almost everywhere, then � **R** _[d] f_ ( _x_ ) _dx ≤_ � **R** _[d] g_ ( _x_ ) _dx_ and � **R** _[d][f]_[(] _[x]_[)] _[dx][ ≤]_ � **R** _[d][g]_[(] _[x]_[)] _[dx]_[.] 

- (iii) (Homogeneity) If _c ∈_ [0 _,_ + _∞_ ), then � **R** _[d] cf_ ( _x_ ) _dx_ = _c_ � **R** _[d] f_ ( _x_ ) _dx_ . (The claim unfortunately fails for _c_ = + _∞_ , but this is somewhat tricky to show.) 

- (iv) (Equivalence) If _f, g_ agree almost everywhere, then � **R** _[d] f_ ( _x_ ) _dx_ = 

- **R** _[d] g_ ( _x_ ) _dx_ and � **R** _[d][f]_[(] _[x]_[)] _[dx]_[ =] � **R** _[d][g]_[(] _[x]_[)] _[dx]_[.] 

- (v) (Superadditivity) � **R** _[d] f_ ( _x_ )+ _g_ ( _x_ ) _dx ≥_ � **R** _[d] f_ ( _x_ ) _dx_ +� **R** _[d] g_ ( _x_ ) _dx_ . 

- (vi) (Subadditivity of upper integral) � **R** _[d][f]_[(] _[x]_[)+] _[g]_[(] _[x]_[)] _[ dx][ ≤]_ � **R** _[d][f]_[(] _[x]_[)] _[ dx]_[+] � **R** _[d][g]_[(] _[x]_[)] _[dx]_ 

- (vii) (Divisibility) For any measurable set _E_ , one has � **R** _[d] f_ ( _x_ ) _dx_ = � **R** _[d] f_ ( _x_ )1 _E_ ( _x_ ) _dx_ + � **R** _[d] f_ ( _x_ )1 **R** _d\E_ ( _x_ ) _dx_ . 

- (viii) (Horizontal truncation) As _n →∞_ , � **R** _[d]_ min( _f_ ( _x_ ) _, n_ ) _dx_ converges to � **R** _[d] f_ ( _x_ ) _dx_ . 

- (ix) (Vertical truncation) As _n →∞_ , � **R** _[d] f_ ( _x_ )1 _|x|≤n dx_ converges to � **R** _[d] f_ ( _x_ ) _dx_ . _Hint:_ From Exercise 1.2.11 one has _m_ ( _E ∩{x_ : _|x| ≤ n}_ ) _→ m_ ( _E_ ) for any measurable set _E_ . 

- (x) (Reflection) If _f_ + _g_ is a simple function that is bounded with finite measure support (i.e. it is absolutely integrable), then Simp � **R** _[d][ f]_[(] _[x]_[) +] _[ g]_[(] _[x]_[)] _[dx]_[ =] � **R** _[d] f_ ( _x_ ) _dx_ + � **R** _[d][g]_[(] _[x]_[)] _[dx]_[.] 

Do the horizontal and vertical truncation properties hold if the lower Lebesgue integral is replaced with the upper Lebesgue integral? 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

65 

Now we restrict attention to measurable functions. 

**Definition 1.3.13** (Unsigned Lebesgue integral) **.** If _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable, we define the unsigned Lebesgue integral � **R** _[d][ f]_[(] _[x]_[)] _[dx]_ of _f_ to equal the lower unsigned Lebesgue integral � **R** _[d] f_ ( _x_ ) _dx_ . (For non-measurable functions, we leave the unsigned Lebesgue integral undefined.) 

One nice feature of measurable functions is that the lower and upper Lebesgue integrals can match, if one also assumes some boundedness: 

**Exercise 1.3.11.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be measurable, bounded, and vanishing outside of a set of finite measure. Show that the lower and upper Lebesgue integrals of _f_ agree. ( _Hint:_ use Exercise 1.3.4.) There is a converse to this statement, but we will defer it to later notes. What happens if _f_ is allowed to be unbounded, or is not supported inside a set of finite measure? 

This gives an important corollary: 

**Corollary 1.3.14** (Finite additivity of the Lebesgue integral) **.** _Let f, g_ : **R** _[d] →_ [0 _,_ + _∞_ ] _be measurable. Then_ � **R** _[d][ f]_[(] _[x]_[)][+] _[g]_[(] _[x]_[)] _[dx]_[=] � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[ +] � **R** _[d][ g]_[(] _[x]_[)] _[dx][.]_ 

**Proof.** From the horizontal truncation property and a limiting argument, we may assume that _f, g_ are bounded. From the vertical truncation property and another limiting argument, we may assume that _f, g_ are supported inside a bounded set. From Exercise 1.3.11, we now see that the lower and upper Lebesgue integrals of _f_ , _g_ , and _f_ + _g_ agree. The claim now follows by combining the superadditivity of the lower Lebesgue integral with the subadditivity of the upper Lebesgue integral. □ 

In the next section we will improve this finite additivity property for the unsigned Lebesgue integral further, to countable additivity; this property is also known as the _monotone convergence theorem_ (Theorem 1.4.44). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

66 

**Exercise 1.3.12** (Upper Lebesgue integral and outer Lebesgue measure) **.** Show that for any set _E ⊂_ **R** _[d]_ , � **R** _[d]_[1] _[E]_[(] _[x]_[)] _[dx]_[=] _[m][∗]_[(] _[E]_[).][Con-] clude that the upper and lower Lebesgue integrals are not necessarily additive if no measurability hypotheses are assumed. 

**Exercise 1.3.13** (Area interpretation of integral) **.** If _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is measurable, show that � **R** _[d][ f]_[(] _[x]_[)] _[ dx]_[ is equal to the] _[ d]_[+1-dimensional] Lebesgue measure of the region _{_ ( _x, t_ ) _∈_ **R** _[d] ×_ **R** : 0 _≤ t ≤ f_ ( _x_ ) _}_ . (This can be used as an alternate, and more geometrically intuitive, definition of the unsigned Lebesgue integral; it is a more convenient formulation for establishing the basic convergence theorems, but not quite as convenient for establishing basic properties such as additivity.) ( _Hint:_ use Exercise 1.2.22.) 

**Exercise 1.3.14** (Uniqueness of the Lebesgue integral) **.** Show that the Lebesgue integral _f �→_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[is][the][only][map][from][measur-] able unsigned functions _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] to [0 _,_ + _∞_ ] that obeys the following properties for measurable _f, g_ : **R** _[d] →_ [0 _,_ + _∞_ ]: 

- (i) (Compatibility with the simple integral) If _f_ is simple, then _[dx]_[ = Simp] _[dx]_[.] 

- � **R** _[d][ f]_[(] _[x]_[)] � **R** _[d][ f]_[(] _[x]_[)] 

- (ii) (Finite additivity) � **R** _[d][ f]_[(] _[x]_[)][+] _[g]_[(] _[x]_[)] _[dx]_[=] � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[+] _[dx]_[.] 

- � **R** _[d][ g]_[(] _[x]_[)] 

- (iii) (Horizontal truncation) As _n →∞_ , � **R** _[d]_[ min(] _[f]_[(] _[x]_[)] _[, n]_[)] _[dx]_ converges to � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[.] 

- (iv) (Vertical truncation) As _n →∞_ , � **R** _[d][ f]_[(] _[x]_[)1] _[|][x][|≤][n][dx]_[con-] verges to � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[.] 

**Exercise 1.3.15** (Translation invariance) **.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be measurable. Show that � **R** _[d][ f]_[(] _[x]_[+] _[y]_[)] _[ dx]_[ =] � **R** _[d][ f]_[(] _[x]_[)] _[ dx]_[ for any] _[ y][∈]_ **[R]** _[d]_[.] 

**Exercise 1.3.16** (Linear change of variables) **.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be measurable, and let _T_ : **R** _[d] →_ **R** _[d]_ be an invertible linear transformation. Show that � **R** _[d][ f]_[(] _[T][ −]_[1][(] _[x]_[))] _[dx]_[=] _[|]_[ det] _[ T][|]_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[,][or] equivalently � **R** _[d][ f]_[(] _[Tx]_[)] _[dx]_[ =] _|_ det1 _T |_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[.] 

**Exercise 1.3.17** (Compatibility with the Riemann integral) **.** Let _f_ : [ _a, b_ ] _→_ [0 _,_ + _∞_ ] be Riemann integrable. If we extend _f_ to **R** by 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

67 

declaring _f_ to equal zero outside of [ _a, b_ ], show that � **R** _[f]_[(] _[x]_[)] _[dx]_[=] _b[dx]_[.] � _a[f]_[(] _[x]_[)] 

We record a basic inequality, known as _Markov’s inequality_ , that asserts that the Lebesgue integral of an unsigned measurable function controls how often that function can be large: 

**Lemma 1.3.15** (Markov’s inequality) **.** _Let f_ : **R** _[d] →_ [0 _,_ + _∞_ ] _be measurable. Then for any_ 0 _< λ < ∞, one has_ 

**==> picture [184 x 23] intentionally omitted <==**

**Proof.** We have the trivial pointwise inequality 

**==> picture [106 x 13] intentionally omitted <==**

From the definition of the lower Lebesgue integral, we conclude that 

**==> picture [300 x 39] intentionally omitted <==**

By sending _λ_ to infinity or to zero, we obtain the following important corollary: 

**Exercise 1.3.18.** Let _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] be measurable. 

- (i) Show that if � **R** _[d][ f]_[(] _[x]_[)] _[dx][<][∞]_[,][then] _[f]_[is][finite][almost][ev-] erywhere. Give a counterexample to show that the converse statement is false. 

- (ii) Show that � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[=][0][if][and][only][if] _[f]_[is][zero][almost] everywhere. 

**Remark 1.3.16.** The use of the integral � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[to][control][the] distribution of _f_ is known as the _first moment method_ . One can also control this distribution using higher moments such as � **R** _[d][ |][f]_[(] _[x]_[)] _[|][p][dx]_ for various values of _p_ , or exponential moments such as � **R** _[d][ e][tf]_[(] _[x]_[)] _[dx]_ or the Fourier moments � **R** _[d][ e][itf]_[(] _[x]_[)] _[dx]_[for][various][values][of] _[t]_[;][such] moment methods are fundamental to probability theory. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

68 

**1.3.4. Absolute integrability.** Having set out the theory of the unsigned Lebesgue integral, we can now define the absolutely convergent Lebesgue integral. 

**Definition 1.3.17** (Absolute integrability) **.** An almost everywhere defined measurable function _f_ : **R** _[d] →_ **C** is said to be _absolutely integrable_ if the unsigned integral 

**==> picture [118 x 24] intentionally omitted <==**

is finite. We refer to this quantity _∥f ∥L_ 1( **R** _d_ ) as the _L_[1] ( **R** _[d]_ ) _norm_ of _f_ , and use _L_[1] ( **R** _[d]_ ) or _L_[1] ( **R** _[d] →_ **C** ) to denote the space of absolutely integrable functions. If _f_ is real-valued and absolutely integrable, we define the Lebesgue integral � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[by][the][formula] 

(1.12) _[dx]_[ :=] _[dx][ −][dx]_ � **R** _[d][ f]_[(] _[x]_[)] � **R** _[d][ f]_[+][(] _[x]_[)] � **R** _[d][ f][−]_[(] _[x]_[)] where _f_ + := max( _f,_ 0), _f−_ := max( _−f,_ 0) are the magnitudes of the positive and negative components of _f_ (note that the two unsigned integrals on the right-hand side are finite, as _f_ + _, f−_ are pointwise dominated by _|f |_ ). If _f_ is complex-valued and absolutely integrable, we define the Lebesgue integral � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[by][the][formula] 

**==> picture [218 x 23] intentionally omitted <==**

where the two integrals on the right are interpreted as real-valued absolutely integrable Lebesgue integrals. It is easy to see that the unsigned, real-valued, and complex-valued Lebesgue integrals defined in this manner are compatible on their common domains of definition. 

Note from construction that the absolutely integrable Lebesgue integral extends the absolutely integrable simple integral, which is now redundant and will not be needed any further in the sequel. 

**Remark 1.3.18.** One can attempt to define integrals for non-absolutely- _∞_ integrable functions, analogous to the improper integrals �0 _f_ ( _x_ ) _dx_ := _R ∞_ lim _R→∞_ �0 _[f]_[(] _[x]_[)] _[ dx]_[ or the principal value integrals] _[ p.v.]_ � _−∞[f]_[(] _[x]_[)] _[ dx]_[ :=] _R_ lim _R→∞_ � _−R[f]_[(] _[x]_[)] _[dx]_[one][sees][in][the][classical][one-dimensional][Rie-] mannian theory. While one can certainly generate any number of such extensions of the Lebesgue integral concept, such extensions tend 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

69 

to be poorly behaved with respect to various important operations, such as change of variables or exchanging limits and integrals, so it is usually not worthwhile to try to set up a systematic theory for such non-absolutely-integrable integrals that is anywhere near as complete as the absolutely integrable theory, and instead deal with such exotic integrals on an _ad hoc_ basis. 

From the pointwise triangle inequality _|f_ ( _x_ ) + _g_ ( _x_ ) _| ≤|f_ ( _x_ ) _|_ + _|g_ ( _x_ ) _|_ , we conclude the _L_[1] triangle inequality 

**==> picture [235 x 12] intentionally omitted <==**

for any almost everywhere defined measurable _f, g_ : **R** _[d] →_ **C** . It is also easy to see that 

**==> picture [114 x 12] intentionally omitted <==**

for any complex number _c_ . As such, we see that _L_[1] ( **R** _[d] →_ **C** ) is a complex vector space. (The _L_[1] norm is then a _seminorm_ on this space; see _§_ 1.3 of _An epsilon of room, Vol. I_ .) From Exercise 1.3.18 we make the important observation that a function _f ∈ L_[1] ( **R** _[d] →_ **C** ) has zero _L_[1] norm, _∥f ∥L_ 1( **R** _d_ ) = 0, if and only if _f_ is zero almost everywhere. 

Given two functions _f, g ∈ L_[1] ( **R** _[d] →_ **C** ), we can define the _L_[1] _distance dL_ 1( _f, g_ ) between them by the formula 

**==> picture [118 x 12] intentionally omitted <==**

Thanks to (1.13), this distance obeys almost all the axioms of a _metric_ on _L_[1] ( **R** _[d]_ ), with one exception: it is possible for two different functions _f, g ∈ L_[1] ( **R** _[d] →_ **C** ) to have a zero _L_[1] distance, if they agree almost everywhere. As such, _dL_ 1 is only a semi-metric (also known as a _pseudo-metric_ ) rather than a metric. However, if one adopts the convention that any two functions that agree almost everywhere are considered equivalent (or more formally, one works in the quotient space of _L_[1] ( **R** _[d]_ ) by the equivalence relation of almost everywhere agreement, which by abuse of notation is also denoted _L_[1] ( **R** _[d]_ )), then one recovers a genuine metric. (Later on, we will establish the important fact that this metric makes the (quotient space) _L_[1] ( **R** _[d]_ ) a 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

70 

complete metric space, a fact known as the _L_[1] _Riesz-Fischer theorem_ ; this completeness is one of the main reasons we spend so much effort setting up Lebesgue integration theory in the first place.) 

The linearity properties of the unsigned integral induce analogous linearity properties of the absolutely convergent Lebesgue integral: 

**Exercise 1.3.19** (Integration is linear) **.** Show that integration _f �→_ � **R** _[d][ f]_[(] _[x]_[)] _[dx]_[is][a][(complex)][linear][operation][from] _[L]_[1][(] **[R]** _[d]_[)][to] **[C]**[.][In] other words, show that 

and 

**==> picture [212 x 61] intentionally omitted <==**

for all absolutely integrable _f, g_ : **R** _[d] →_ **C** and complex numbers _c_ . Also establish the identity 

**==> picture [122 x 24] intentionally omitted <==**

which makes integration not just a linear operation, but a _*-linear_ operation. 

**Exercise 1.3.20.** Show that Exercises 1.3.15, 1.3.16, and 1.3.17 also hold for complex-valued, absolutely integrable functions rather than for unsigned measurable functions. 

**Exercise 1.3.21** (Absolute summability is a special case of absolute integrability) **.** Let ( _cn_ ) _n∈_ **Z** be a doubly infinite sequence of complex numbers, and let _f_ : **R** _→_ **C** be the function 

**==> picture [140 x 22] intentionally omitted <==**

where _⌊x⌋_ is the greatest integer less than _x_ . Show that _f_ is absolutely integrable if and only if the series[�] _n∈_ **Z** _[c][n]_[is][absolutely][convergent,] in which case one has � **R** _[f]_[(] _[x]_[)] _[dx]_[ =][ �] _n∈_ **Z** _[c][n]_[.] 

We can localise the absolutely convergent integral to any measurable subset _E_ of **R** _[d]_ . Indeed, if _f_ : _E →_ **C** is a function, we say that _f_ is measurable (resp. absolutely integrable) if its extension 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

71 

˜ ˜ _f_ : **R** _[d] →_ **C** is measurable (resp. absolutely integrable), where _f_ ( _x_ ) is defined to equal _f_ ( _x_ ) when _x ∈ E_ and zero otherwise, and then we define � _E[f]_[(] _[x]_[)] _[dx]_[:=] � **R** _[d][f]_[˜][(] _[x]_[)] _[dx]_[.][Thus,][for][instance,][the][absolutely] integrable analogue of Exercise 1.3.17 tells us that 

**==> picture [120 x 28] intentionally omitted <==**

for any Riemann-integrable _f_ : [ _a, b_ ] _→_ **C** . 

**Exercise 1.3.22.** If _E, F_ are disjoint measurable subsets of **R** _[d]_ , and _f_ : _E ∪ F →_ **C** is absolutely integrable, show that 

and 

**==> picture [184 x 62] intentionally omitted <==**

We will study the properties of the absolutely convergent Lebesgue integral in more detail in later notes, as a special case of the more general Lebesgue integration theory on abstract measure spaces. For now, we record one very basic inequality: 

**Lemma 1.3.19** (Triangle inequality) **.** _Let f ∈ L_[1] ( **R** _[d] →_ **C** ) _. Then_ 

**==> picture [134 x 24] intentionally omitted <==**

**Proof.** If _f_ is real-valued, then _|f |_ = _f_ + + _f−_ and the claim is obvious from (1.12). When _f_ is complex-valued, one cannot argue quite so simply; a naive mimicking of the real-valued argument would lose a factor of 2, giving the inferior bound 

**==> picture [140 x 24] intentionally omitted <==**

To do better, we exploit the phase rotation invariance properties of the absolute value operation and of the integral, as follows. Note that for any complex number _z_ , one can write _|z|_ as _ze[iθ]_ for some real _θ_ . In particular, we have 

**==> picture [216 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

72 

for some real _θ_ . Taking real parts of both sides, we obtain 

**==> picture [300 x 42] intentionally omitted <==**

**1.3.5. Littlewood’s three principles.** _Littlewood’s three principles_ are informal heuristics that convey much of the basic intuition behind the measure theory of Lebesgue. Briefly, the three principles are as follows: 

- (i) Every (measurable) set is nearly a finite sum of intervals; 

- (ii) Every (absolutely integrable) function is nearly continuous; and 

- (iii) Every (pointwise) convergent sequence of functions is nearly uniformly convergent. 

Various manifestations of the first principle were given in Exercise 1.2.7 and Exercise 1.2.16. Now we turn to the second principle. Define a _step function_ to be a finite linear combination of indicator functions 1 _B_ of boxes _B_ . 

**Theorem 1.3.20** (Approximation of _L_[1] functions) **.** _Let f ∈ L_[1] ( **R** _[d]_ ) _and ε >_ 0 _._ 

- (i) _There exists an absolutely integrable simple function g such that ∥f − g∥L_ 1( **R** _d_ ) _≤ ε._ 

- (ii) _There exists a step function g such that ∥f − g∥L_ 1( **R** _d_ ) _≤ ε._ 

- (iii) _There exists a continuous, compactly supported g such that ∥f − g∥L_ 1( **R** _d_ ) _≤ ε._ 

To put things another way, the absolutely integrable simple functions, the step functions, and the continuous, compactly supported functions are all dense subsets of _L_[1] ( **R** _[d]_ ) with respect to the _L_[1] ( **R** _[d]_ ) (semi-)metric. In _§_ 1.13 of _An epsilon of room, Vol. I_ it is shown that a similar statement holds if one replaces continuous, compactly supported functions with _smooth_ , compactly supported functions, also known as _test functions_ ; this is an important fact for the theory of _distributions_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

73 

**Proof.** We begin with part (i). When _f_ is unsigned, we see from the definition of the lower Lebesgue integral that there exists an unsigned simple function _g_ such that _g ≤ f_ (so, in particular, _g_ is absolutely integrable) and 

**==> picture [138 x 23] intentionally omitted <==**

which by linearity implies that _∥f − g∥L_ 1( **R** _d_ ) _≤ ε_ . This gives (i) when _f_ is unsigned. The case when _f_ is real-valued then follows by splitting _f_ into positive and negative parts (and adjusting _ε_ as necessary), and the case when _f_ is complex-valued then follows by splitting _f_ into real and imaginary parts (and adjusting _ε_ yet again). 

To establish part (ii), we see from (i) and the triangle inequality in _L_[1] that it suffices to show this when _f_ is an absolutely integrable simple function. By linearity (and more applications of the triangle inequality), it then suffices to show this when _f_ = 1 _E_ is the indicator function of a measurable set _E ⊂_ **R** _[d]_ of finite measure. But then, by Exercise (1.2.16), such a set can be approximated (up to an error of measure at most _ε_ ) by an elementary set, and the claim follows. 

To establish part (iii), we see from (ii) and the argument from the preceding paragraph that it suffices to show this when _f_ = 1 _E_ is the indicator function of a box. But one can then establish the claim by direct construction. Indeed, if one makes a slightly larger box _F_ that contains the closure of _E_ in its interior, but has a volume at most _ε_ more than that of _E_ , then one can directly construct a piecewise linear continuous function _g_ supported on _F_ that equals 1 on _E_ (e.g. one can set _g_ ( _x_ ) = max(1 _− R_ dist( _x, E_ ) _,_ 0) for some sufficiently large _R_ ; one may also invoke _Urysohn’s lemma_ , see _§_ 1.10 of _An epsilon of room, Vol. I_ ). It is then clear from construction that _∥f − g∥L_ 1( **R** _d_ ) _≤ ε_ as required. □ 

This is not the only way to make Littlewood’s second principle manifest; we return to this point shortly. For now, we turn to Littlewood’s third principle. We recall three basic ways in which a sequence _fn_ : **R** _[d] →_ **C** of functions can converge to a limit _f_ : **R** _[d] →_ **C** : 

(i) (Pointwise convergence) _fn_ ( _x_ ) _→ f_ ( _x_ ) for every _x ∈_ **R** _[d]_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

74 

- (ii) (Pointwise almost everywhere convergence) _fn_ ( _x_ ) _→ f_ ( _x_ ) for almost every _x ∈_ **R** _[d]_ . 

- (iii) (Uniform convergence) For every _ε >_ 0, there exists _N_ such that _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤ ε_ for all _n ≥ N_ and all _x ∈_ **R** _[d]_ . 

Uniform convergence implies pointwise convergence, which in turn implies pointwise almost everywhere convergence. 

We now add a fourth mode of convergence, that is weaker than uniform convergence but stronger than pointwise convergence: 

**Definition 1.3.21** (Locally uniform convergence) **.** A sequence of functions _fn_ : **R** _[d] →_ **C** converges _locally uniformly_ to a limit _f_ : **R** _[d] →_ **C** if, for every bounded subset _E_ of **R** _[d]_ , _fn_ converges uniformly to _f_ on _E_ . In other words, for every bounded _E ⊂_ **R** _[d]_ and every _ε >_ 0, there exists _N >_ 0 such that _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤ ε_ for all _n ≥ N_ and _x ∈ E_ . 

**Remark 1.3.22.** At least as far as **R** _[d]_ is concerned, an equivalent definition of local uniform convergence is: _fn_ converges locally uniformly to _f_ if, for every point _x_ 0 _∈_ **R** _[d]_ , there exists an open neighbourhood _U_ of _x_ 0 such that _fn_ converges uniformly to _f_ on _U_ . The equivalence of the two definitions is immediate from the _Heine-Borel theorem_ . More generally, the adverb “locally” in mathematics is usually used in this fashion; a propery _P_ is said to hold _locally_ on some domain _X_ if, for every point _x_ 0 in that domain, there is an open neighbourhood of _x_ 0 in _X_ on which _P_ holds. 

One should caution, though, that on domains on which the HeineBorel theorem does not hold, the bounded-set notion of local uniform convergence is not equivalent to the open-set notion of local uniform convergence (though, for _locally compact spaces_ , one can recover equivalence of one replaces “bounded” by “compact”). 

**Example 1.3.23.** The functions _x �→ x/n_ on **R** for _n_ = 1 _,_ 2 _, . . ._ converge locally uniformly (and hence pointwise) to zero on **R** , but do not converge uniformly. 

**Example 1.3.24.** The partial sums[�] _[N] n_ =0 _xn[n]_ ![of][the][Taylor][series] _e[x]_ =[�] _[∞] n_ =0 _xn[n]_ ![converges][to] _[e][x]_[locally][uniformly][(and][hence][point-] wise) on **R** , but not uniformly. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

75 

1 **Example 1.3.25.** The functions _fn_ ( _x_ ) := _nx_[1] _[x>]_[0][for] _[n]_[=][1] _[,]_[ 2] _[, . . .]_ (with the convention that _fn_ (0) = 0) converge pointwise everywhere to zero, but do not converge locally uniformly. 

From the preceding example, we see that pointwise convergence (either everywhere or almost everywhere) is a weaker concept than local uniform convergence. Nevertheless, a remarkable theorem of Egorov, which demonstrates Littlewood’s third principle, asserts that one can recover local uniform convergence as long as one is willing to delete a set of small measure: 

**Theorem 1.3.26** (Egorov’s theorem) **.** _Let fn_ : **R** _[d] →_ **C** _be a sequence of measurable functions that converge pointwise almost everywhere to another function f_ : **R** _[d] →_ **C** _, and let ε >_ 0 _. Then there exists a Lebesgue measurable set A of measure at most ε, such that fn converges locally uniformly to f outside of A._ 

Note that Example 1.3.25 demonstrates that the exceptional set _A_ in Egorov’s theorem cannot be taken to have zero measure, at least if one uses the bounded-set definition of local uniform convergence from Definition 1.3.21. (If one instead takes the “open neighbourhood” definition, then the sequence in Example 1.3.25 does converge locally uniformly on **R** _\{_ 0 _}_ in the open neighbourhood sense, even if it does not do so in the bounded-set sense. On a domain such as **R** _[d] \A_ , bounded-set locally uniform convergence implies open-neighbourhood locally uniform convergence, but not conversely, so for the purposes of applying Egorov’s theorem, the distinction is not too important since one local uniform convergence in both senses.) 

**Proof.** By modifying _fn_ and _f_ on a set of measure zero (that can be absorbed into _A_ at the end of the argument) we may assume that _fn_ converges pointwise everywhere to _f_ , thus for every _x ∈_ **R** _[d]_ and _m >_ 0 there exists _N ≥_ 0 such that _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤_ 1 _/m_ for all _n ≥ N_ . We can rewrite this fact set-theoretically as 

**==> picture [62 x 29] intentionally omitted <==**

for each _m_ , where _EN,m_ := _{x ∈_ **R** _[d]_ : _|fn_ ( _x_ ) _− f_ ( _x_ ) _| >_ 1 _/m_ for some _n ≥ N }._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

76 

It is clear that the _EN,m_ are Lebesgue measurable, and are decreasing in _N_ . Applying downward monotone convergence (Exercise 1.2.11(ii)) we conclude that, for any radius _R >_ 0, one has 

**==> picture [130 x 15] intentionally omitted <==**

(The restriction to the ball _B_ (0 _, R_ ) is necessary, because the downward monotone convergence property only works when the sets involved have finite measure.) In particular, for any _m ≥_ 1, we can find _Nm_ such that 

**==> picture [113 x 19] intentionally omitted <==**

for all _N ≥ Nm_ . 

Now let _A_ :=[�] _[∞] m_ =1 _[E][N] m[,m][ ∩][B]_[(0] _[, m]_[).][Then] _[A]_[is][Lebesgue][mea-] surable, and by countable subadditivity, _m_ ( _A_ ) _≤ ε_ . By construction, we have _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤_ 1 _/m_ whenever _m ≥_ 1, _x ∈_ **R** _[d] \A_ , _|x| ≤ m_ , and _n ≥ Nm_ . In particular, we see for any ball _B_ (0 _, m_ 0) with an integer radius, _fn_ converges uniformly to _f_ on _B_ (0 _, m_ 0) _\A_ . Since every bounded set is contained in such a ball, the claim follows. □ 

**Remark 1.3.27.** Unfortunately, one cannot in general upgrade local uniform convergence to uniform convergence in Egorov’s theorem. A basic example here is the _moving bump_ example _fn_ := 1[ _n,n_ +1] on **R** , which “escapes to horizontal infinity”. This sequence converges pointwise (and locally uniformly) to the zero function _f ≡_ 0. However, for any 0 _< ε <_ 1 and any _n_ , we have _|fn_ ( _x_ ) _− f_ ( _x_ ) _| > ε_ on a set of measure 1, namely on the interval [ _n, n_ + 1]. Thus, if one wanted _fn_ to converge uniformly to _f_ outside of a set _A_ , then that set _A_ has to contain a set of measure 1. In fact, it must contain the intervals [ _n, n_ + 1] for all sufficiently large _n_ and must therefore have infinite measure. 

However, if all the _fn_ and _f_ were supported on a _fixed_ set _E_ of finite measure (e.g. on a ball _B_ (0 _, R_ )), then the above “escape to horizontal infinity” cannot occur, it is easy to see from the above argument that one can recover uniform convergence (and not just locally uniform convergence) outside of a set of arbitrarily small measure. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.3. The Lebesgue integral** 

77 

We now use Theorem 1.3.20 to give another version of Littlewood’s second principle, known as _Lusin’s theorem_ : 

**Theorem 1.3.28** (Lusin’s theorem) **.** _Let f_ : **R** _[d] →_ **C** _be absolutely integrable, and let ε >_ 0 _. Then there exists a Lebesgue measurable set E ⊂_ **R** _[d] of measure at most ε such that the restriction of f to the complementary set_ **R** _[d] \E is continuous on that set._ 

A word of caution: this theorem does _not_ imply that the unrestricted function _f_ is continuous on **R** _[d] \E_ . For instance, the absolutely integrable function 1 **Q** : **R** _→_ **C** is nowhere continuous, so is certainly not continuous on **R** _\E_ for any _E_ of finite measure; but on the other hand, if one deletes the measure zero set _E_ := **Q** from the reals, then the restriction of _f_ to **R** _\E_ is identically zero and thus continuous. 

**Proof.** By Theorem 1.3.20, for any _n ≥_ 1 one can find a continuous, compactly supported function _fn_ such that _∥f − fn∥L_ 1( **R** _d_ ) _≤ ε/_ 4 _[n]_ (say). By Markov’s inequality (Lemma 1.3.15), that implies that _|f_ ( _x_ ) _−fn_ ( _x_ ) _| ≤_ 1 _/_ 2 _[n][−]_[1] for all _x_ outside of a Lebesgue measurable set _En_ of measure at most _ε/_ 2 _[n]_[+1] . Letting _E_ :=[�] _[∞] n_ =1 _[E][n]_[,][we][conclude] that _E_ is Lebesgue measurable with measure at most _ε/_ 2, and _fn_ converges uniformly to _f_ outside of _E_ . But the uniform limit of continuous functions is continuous, and the same is true for local uniform limits (because continuity is itself a local property). We conclude that the restriction _f_ to **R** _[d] \E_ is continuous, as required. □ 

**Exercise 1.3.23.** Show that the hypothesis that _f_ is absolutely integrable in Lusin’s theorem can be relaxed to being locally absolutely integrable (i.e. absolutely integrable on every bounded set), and then relaxed further to that of being measurable (but still finite everywhere or almost everywhere). (To achieve the latter goal, one can replace _f_ locally with a horizontal truncation _f_ 1 _|f |≤n_ ; alternatively, one can replace _f_ with a bounded variant, such as _f_[.)] (1+ _|f |_[2] )[1] _[/]_[2] 

**Exercise 1.3.24.** Show that a function _f_ : **R** _[d] →_ **C** is measurable if and only if it is the pointwise almost everywhere limit of continuous functions _fn_ : **R** _[d] →_ **C** . ( _Hint:_ if _f_ : **R** _[d] →_ **C** is measurable and _n ≥_ 1, show that there exists a continuous function _fn_ : **R** _[d] →_ **C** for 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

78 

which the set _{x ∈ B_ (0 _, n_ ) : _|f_ ( _x_ ) _− fn_ ( _x_ ) _| ≥_ 1 _/n}_ has measure at most 21 _[n]_[.][You][may][find][Exercise][1.3.25][below][to][be][useful][for][this.)] Use this (and Egorov’s theorem, Theorem 1.3.26) to give an alternate proof of Lusin’s theorem for arbitrary measurable functions. 

**Remark 1.3.29.** This is a trivial but important remark: when dealing with unsigned measurable functions such as _f_ : **R** _[d] →_ [0 _,_ + _∞_ ], then Lusin’s theorem does not apply directly because _f_ could be infinite on a set of positive measure, which is clearly in contradiction with the conclusion of Lusin’s theorem (unless one allows the continuous function to also take values in the extended non-negative reals [0 _,_ + _∞_ ] with the extended topology). However, if one knows already that _f_ is almost everywhere finite (which is for instance the case when _f_ is absolutely integrable), then Lusin’s theorem applies (since one can simply zero out _f_ on the null set where it is infinite, and add that null set to the exceptional set of Lusin’s theorem). 

**Remark 1.3.30.** By combining Lusin’s theorem with inner regularity (Exercise 1.2.15) and the _Tietze extension theorem_ (see _§_ 1.10 of _An epsilon of room, Vol. I_ ), one can conclude that every measurable function _f_ : **R** _[d] →_ **C** agrees (outside of a set of arbitrarily small measure) with a continuous function _g_ : **R** _[d] →_ **C** . 

**Exercise 1.3.25** (Littlewood-like principles) **.** The following facts are not, strictly speaking, instances of any of Littlewood’s three principles, but are in a similar spirit. 

- (i) (Absolutely integrable functions almost have bounded support) Let _f_ : **R** _[d] →_ **C** be an absolutely integrable function, and let _ε >_ 0. Show that there exists a ball _B_ (0 _, R_ ) outside of which _f_ has an _L_[1] norm of at most _ε_ , or in other words that � **R** _[d] \B_ (0 _,R_ ) _[|][f]_[(] _[x]_[)] _[|][dx][ ≤][ε]_[.] 

- (ii) (Measurable functions are almost locally bounded) Let _f_ : **R** _[d] →_ **C** be a measurable function supported on a set of finite measure, and let _ε >_ 0. Show that there exists a measurable set _E ⊂_ **R** _[d]_ of measure at most _ε_ outside of which _f_ is locally bounded, or in other words that for every _R >_ 0 there exists _M < ∞_ such that _|f_ ( _x_ ) _| ≤ M_ for all _x ∈ B_ (0 _, R_ ) _\E_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

79 

As with Remark 1.3.29, it is important in the second part of the exercise that _f_ is known to be finite everywhere (or at least almost everywhere); the result would of course fail if _f_ was, say, unsigned but took the value + _∞_ on a set of positive measure. 

## **1.4. Abstract measure spaces** 

Thus far, we have only focused on measure and integration theory in the context of Euclidean spaces **R** _[d]_ . Now, we will work in a more abstract and general setting, in which the Euclidean space **R** _[d]_ is replaced by a more general space _X_ . 

It turns out that in order to properly define measure and integration on a general space _X_ , it is not enough to just specify the set _X_ . One also needs to specify two additional pieces of data: 

- (i) A collection _B_ of subsets of _X_ that one is allowed to measure; and 

- (ii) The measure _µ_ ( _E_ ) _∈_ [0 _,_ + _∞_ ] one assigns to each measurable set _E ∈B_ . 

For instance, Lebesgue measure theory covers the case when _X_ is a Euclidean space **R** _[d]_ , _B_ is the collection _B_ = _L_ [ **R** _[d]_ ] of all Lebesgue measurable subsets of **R** _[d]_ , and _µ_ ( _E_ ) is the Lebesgue measure _µ_ ( _E_ ) = _m_ ( _E_ ) of _E_ . 

The collection _B_ has to obey a number of axioms (e.g. being closed with respect to countable unions) that make it a _σ-algebra_ , which is a stronger variant of the more well-known concept of a _boolean algebra_ . Similarly, the measure _µ_ has to obey a number of axioms (most notably, a countable additivity axiom) in order to obtain a measure and integration theory comparable to the Lebesgue theory on Euclidean spaces. When all these axioms are satisfied, the triple ( _X, B, µ_ ) is known as a _measure space_ . These play much the same role in abstract measure theory that metric spaces or topological spaces play in abstract point-set topology, or that vector spaces play in abstract linear algebra. 

On any measure space, one can set up the unsigned and absolutely convergent integrals in almost exactly the same way as was done in 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

80 

the previous notes for the Lebesgue integral on Euclidean spaces, although the approximation theorems are largely unavailable at this level of generality due to the lack of such concepts as “elementary set” or “continuous function” for an abstract measure space. On the other hand, one _does_ have the fundamental convergence theorems for the subject, namely Fatou’s lemma, the monotone convergence theorem and the dominated convergence theorem, and we present these results here. 

One question that will not be addressed much in this section is how one actually _constructs_ interesting examples of measures. We will return to this issue in Section 1.7 (although one of the most powerful tools for such constructions, namely the _Riesz representation theorem_ , will not be covered here, but instead in _§_ 1.10 of _An epsilon of room, Vol. I_ ). 

**1.4.1. Boolean algebras.** We begin by recalling the concept of a _Boolean algebra_ . 

**Definition 1.4.1** (Boolean algebras) **.** Let _X_ be a set. A (concrete) _Boolean algebra_ on _X_ is a collection _B_ of _X_ which obeys the following properties: 

- (i) (Empty set) _∅∈B_ . 

- (ii) (Complement) If _E ∈B_ , then the complement _E[c]_ := _X\E_ also lies in _B_ . 

- (iii) (Finite unions) If _E, F ∈B_ , then _E ∪ F ∈B_ . 

We sometimes say that _E_ is _B-measurable_ , or _measurable with respect to B_ , if _E ∈B_ . 

Given two Boolean algebras _B, B[′]_ on _X_ , we say that _B[′]_ is _finer than_ , _a sub-algebra of_ , or _a refinement of B_ , or that _B_ is _coarser than_ or _a coarsening of B[′]_ , if _B ⊂B[′]_ . 

We have chosen a “minimalist” definition of a Boolean algebra, in which one is only assumed to be closed under two of the basic Boolean operations, namely complement and finite union. However, by using the laws of Boolean algebra (such as de Morgan’s laws), it is easy to see that a Boolean algebra is also closed under other 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

81 

Boolean algebra operations such as intersection _E ∩F_ , set differerence _E\F_ , and symmetric difference _E_ ∆ _F_ . So one could have placed these additional closure properties inside the definition of a Boolean algebra without any loss of generality. However, when we are _verifying_ that a given collection _B_ of sets is indeed a Boolean algebra, it is convenient to have as minimal a set of axioms as possible. 

**Remark 1.4.2.** One can also consider _abstract Boolean algebras B_ , which do not necessarily live in an ambient domain _X_ , but for which one has a collection of abstract Boolean operations such as meet _∧_ and join _∨_ instead of the concrete operations of intersection _∩_ and union _∪_ . We will not take this abstract perspective here, but see _§_ 2.3 of _An epsilon of room, Vol. I_ for some further discussion of the relationship between concrete and abstract Boolean algebras, which is codified by _Stone’s theorem_ . 

**Example 1.4.3** (Trivial and discrete algebra) **.** Given any set _X_ , the coarsest Boolean algebra is the _trivial algebra {∅, X}_ , in which the only measurable sets are the empty set and the whole set. The finest Boolean algebra is the _discrete algebra_ 2 _[X]_ := _{E_ : _E ⊂ X}_ , in which _every_ set is measurable. All other Boolean algebras are intermediate between these two extremes: finer than the trivial algebra, but coarser than the discrete one. 

**Exercise 1.4.1** (Elementary algebra) **.** Let _E_ [ **R** _[d]_ ] be the collection of those sets _E ⊂_ **R** _[d]_ that are either elementary sets, or co-elementary sets (i.e. the complement of an elementary set). Show that _E_ [ **R** _[d]_ ] is a Boolean algebra. We will call this algebra the _elementary Boolean algebra_ of **R** _[d]_ . 

**Example 1.4.4** (Jordan algebra) **.** Let _J_ [ **R** _[d]_ ] be the collection of subsets of **R** _[d]_ that are either Jordan measurable or co-Jordan measurable (i.e. the complement of a Jordan measurable set). Then _J_ [ **R** _[d]_ ] is a Boolean algebra that is finer than the elementary algebra. We refer to this algebra as the _Jordan algebra_ on **R** _[d]_ (but caution that there is a completely different concept of a Jordan algebra in abstract algebra.) 

**Example 1.4.5** (Lebesgue algebra) **.** Let _L_ [ **R** _[d]_ ] be the collection of Lebesgue measurable subsets of **R** _[d]_ . Then _L_ [ **R** _[d]_ ] is a Boolean algebra 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

82 

that is finer than the Jordan algebra; we refer to this as the _Lebesgue algebra_ on **R** _[d]_ . 

**Example 1.4.6** (Null algebra) **.** Let _N_ ( **R** _[d]_ ) be the collection of subsets of **R** _[d]_ that are either Lebesgue null sets or Lebesgue co-null sets (the complement of null sets). Then _N_ ( **R** _[d]_ ) is a Boolean algebra that is coarser than the Lebesgue algebra; we refer to it as the _null algebra_ on **R** _[d]_ . 

**Exercise 1.4.2** (Restriction) **.** Let _B_ be a Boolean algebra on a set _X_ , and let _Y_ be a subset of _X_ (not necessarily _B_ -measurable). Show that the _restriction B_ ⇂ _Y_ := _{E ∩ Y_ : _E ∈B}_ of _B_ to _Y_ is a Boolean algebra on _Y_ . If _Y_ is _B_ -measurable, show that 

**==> picture [152 x 12] intentionally omitted <==**

**Example 1.4.7** (Atomic algebra) **.** Let _X_ be partitioned into a union _X_ =[�] _α∈I[A][α]_[of][disjoint][sets] _[A][α]_[,][which][we][refer][to][as] _[atoms]_[.][Then] this partition generates a Boolean algebra _A_ (( _Aα_ ) _α∈I_ ), defined as the collection of all the sets _E_ of the form _E_ =[�] _α∈J[A][α]_[for][some] _[J][⊂][I]_[,] i.e. _A_ (( _Aα_ ) _α∈I_ ) is the collection of all sets that can be represented as the union of one or more atoms. This is easily verified to be a Boolean algebra, and we refer to it as the _atomic algebra_ with atoms ( _Aα_ ) _α∈I_ . The trivial algebra corresponds to the trivial partition _X_ = _X_ into a single atom; at the other extreme, the discrete algebra corresponds to the discrete partition _X_ =[�] _x∈X[{][x][}]_[into][singleton][atoms.][More] generally, note that finer (resp. coarser) partitions lead to finer (resp. coarser) atomic algebra. In this definition, we permit some of the atoms in the partition to be empty; but it is clear that empty atoms have no impact on the final atomic algebra, and so without loss of generality one can delete all empty atoms and assume that all atoms are non-empty if one wishes. 

**Example 1.4.8** (Dyadic algebras) **.** Let _n_ be an integer. The _dyadic algebra Dn_ ( **R** _[d]_ ) at scale 2 _[−][n]_ in **R** _[d]_ is defined to be the atomic algebra generated by the half-open dyadic cubes 

**==> picture [152 x 25] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

83 

of length 2 _[−][n]_ (see Exercise 1.1.14). These are Boolean algebras which are increasing in _n_ : _Dn_ +1 _⊃Dn_ . Draw a diagram to indicate how these algebras sit in relation to the elementary, Jordan, and Lebesgue, null, discrete, and trivial algebras. 

**Remark 1.4.9.** The dyadic algebras are analogous to the finite resolution one has on modern computer monitors, which subdivide space into square pixels. A low resolution monitor (in which each pixel has a large size) can only resolve a very small set of “blocky” images, as opposed to the larger class of images that can be resolved by a finer resolution monitor. 

**Exercise 1.4.3.** Show that the non-empty atoms of an atomic algebra are determined up to relabeling. More precisely, show that if _X_ =[�] _α∈I[A][α]_[=][�] _α[′] ∈I[′][ A] α[′][′]_[are][two][partitions][of] _[X]_[into][non-empty] atoms _Aα_ , _A[′] α[′]_[, then] _[ A]_[((] _[A][α]_[)] _[α][∈][I]_[) =] _[ A]_[((] _[A][′] α[′]_[)] _[α][′][∈][I][′]_[) if and only if exists] a bijection _φ_ : _I → I[′]_ such that _A[′] φ_ ( _α_ )[=] _[ A][α]_[for][all] _[α][ ∈][I]_[.] 

While many Boolean algebras are atomic, many are not, as the following two exercises indicate. 

**Exercise 1.4.4.** Show that every finite Boolean algebra is an atomic algebra. (A Boolean algebra _B_ is _finite_ if its cardinality is finite, i.e. there are only finitely many measurable sets.) Conclude that every finite Boolean algebra has a cardinality of the form 2 _[n]_ for some natural number _n_ . From this exercise and Exercise 1.4.3 we see that there is a one-to-one correspondence between finite Boolean algebras on _X_ and finite partitions of _X_ into non-empty sets (up to relabeling). 

**Exercise 1.4.5.** Show that the elementary, Jordan, Lebesgue, and null algebras are _not_ atomic algebras. ( _Hint:_ argue by contradiction. If these algebras were atomic, what must the atoms be?) 

Now we describe some further ways to generate Boolean algebras. 

**Exercise 1.4.6** (Intersection of algebras) **.** Let ( _Bα_ ) _α∈I_ be a family of Boolean algebras on a set _X_ , indexed by a (possibly infinite or uncountable) label set _I_ . Show that the intersection[�] _α∈I[B][α]_[:=] � _α∈I[B][α]_[of][these][algebras][is][still][a][Boolean][algebra,][and][is][the][finest] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

84 

Boolean algebra that is coarser than all of the _Bα_ . (If _I_ is empty, we adopt the convention that[�] _α∈I[B][α]_[is][the][discrete][algebra.)] 

**Definition 1.4.10** (Generation of algebras) **.** Let _F_ be any family of sets in _X_ . We define _⟨F⟩_ bool to be the intersection of all the Boolean algebras that contain _F_ , which is again a Boolean algebra by Exercise 1.4.6. Equivalently, _⟨F⟩_ bool is the coarsest Boolean algebra that contains _F_ . We say that _⟨F⟩_ bool is the Boolean algebra _generated_ by _F_ . 

**Example 1.4.11.** _F_ is a Boolean algebra if and only if _⟨F⟩_ bool = _F_ ; thus each Boolean algebra is generated by itself. 

**Exercise 1.4.7.** Show that the elementary algebra _E_ ( **R** _[d]_ ) is generated by the collection of boxes in **R** _[d]_ . 

**Exercise 1.4.8.** Let _n_ be a natural number. Show that if _F_ is a finite collection of _n_ sets, then _⟨F⟩_ bool is a finite Boolean algebra of cardinality at most 2[2] _[n]_ (in particular, finite sets generate finite algebras). Give an example to show that this bound is best possible. ( _Hint:_ for the latter, it may be convenient to use a discrete ambient space such as the discrete cube _X_ = _{_ 0 _,_ 1 _}[n]_ .) 

The Boolean algebra _⟨F⟩_ bool can be described explicitly in terms of _F_ as follows: 

**Exercise 1.4.9** (Recursive description of a generated Boolean algebra) **.** Let _F_ be a collection of sets in a set _X_ . Define the sets _F_ 0 _, F_ 1 _, F_ 2 _, . . ._ recursively as follows: 

- (i) _F_ 0 := _F_ . 

(ii) For each _n ≥_ 1, we define _Fn_ to be the collection of all sets that either the union of a finite number of sets in _Fn−_ 1 (including the empty union _∅_ ), or the complement of such a union. 

Show that _⟨F⟩_ bool =[�] _[∞] n_ =0 _[F][n]_[.] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

85 

**1.4.2.** _σ_ **-algebras and measurable spaces.** In order to obtain a measure and integration theory that can cope well with limits, the finite union axiom of a Boolean algebra is insufficient, and must be improved to a countable union axiom: 

**Definition 1.4.12** (Sigma algebras) **.** Let _X_ be a set. A _σ-algebra_ on _X_ is a collection _B_ of _X_ which obeys the following properties: 

- (i) (Empty set) _∅∈B_ . 

- (ii) (Complement) If _E ∈B_ , then the complement _E[c]_ := _X\E_ also lies in _B_ . 

- (iii) (Countable unions) If _E_ 1 _, E_ 2 _, . . . ∈B_ , then[�] _[∞] n_ =1 _[E][n][∈B]_[.] 

We refer to the pair ( _X, B_ ) of a set _X_ together with a _σ_ -algebra on that set as a _measurable space_ . 

**Remark 1.4.13.** The prefix _σ_ usually denotes “countable union”. Other instances of this prefix include a _σ-compact topological space_ (a countable union of compact sets), a _σ-finite measure space_ (a countable union of sets of finite measure), or _Fσ set_ (a countable union of closed sets) for other instances of this prefix. 

From de Morgan’s law (which is just as valid for infinite unions and intersections as it is for finite ones), we see that _σ_ -algebras are closed under countable intersections as well as countable unions. 

By padding a finite union into a countable union by using the empty set, we see that every _σ_ -algebra is automatically a Boolean algebra. Thus, we automatically inherit the notion of being measurable with respect to a _σ_ -algebra, or of one _σ_ -algebra being coarser or finer than another. 

**Exercise 1.4.10.** Show that all atomic algebras are _σ_ -algebras. In particular, the discrete algebra and trivial algebra are _σ_ -algebras, as are the finite algebras and the dyadic algebras on Euclidean spaces. 

**Exercise 1.4.11.** Show that the Lebesgue and null algebras are _σ_ - algebras, but the elementary and Jordan algebras are not. 

**Exercise 1.4.12.** Show that any restriction _B_ ⇂ _Y_ of a _σ_ -algebra _B_ to a subspace _Y_ of _X_ (as defined in Exercise 1.4.2) is again a _σ_ -algebra on the subspace _Y_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

86 

There is an exact analogue of Exercise 1.4.6: 

**Exercise 1.4.13** (Intersection of _σ_ -algebras) **.** Show that the intersection[�] _α∈I[B][α]_[:=][ �] _α∈I[B][α]_[of][an][arbitrary][(and][possibly][infinite][or] uncountable) number of _σ_ -algebras _Bα_ is again a _σ_ -algebra, and is the finest _σ_ -algebra that is coarser than all of the _Bα_ . 

Similarly, we have a notion of generation: 

**Definition 1.4.14** (Generation of _σ_ -algebras) **.** Let _F_ be any family of sets in _X_ . We define _⟨F⟩_ to be the intersection of all the _σ_ -algebras that contain _F_ , which is again a _σ_ -algebra by Exercise 1.4.13. Equivalently, _⟨F⟩_ is the coarsest _σ_ -algebra that contains _F_ . We say that _⟨F⟩_ is the _σ_ -algebra _generated_ by _F_ . 

Since every _σ_ -algebra is a Boolean algebra, we have the trivial inclusion 

_⟨F⟩_ bool _⊂⟨F⟩._ 

However, equality need not hold; it only holds if and only if _⟨F⟩_ bool is a _σ_ -algebra. For instance, if _F_ is the collection of all boxes in **R** _[d]_ , then _⟨F⟩_ bool is the elementary algebra (Exercise 1.4.7), but _⟨F⟩_ cannot equal this algebra, as it is not a _σ_ -algebra. 

**Remark 1.4.15.** From the definitions, it is clear that we have the following principle, somewhat analogous to the principle of mathematical induction: if _F_ is a family of sets in _X_ , and _P_ ( _E_ ) is a property of sets _E ⊂ X_ which obeys the following axioms: 

- (i) _P_ ( _∅_ ) is true. 

- (ii) _P_ ( _E_ ) is true for all _E ∈F_ . 

(iii) If _P_ ( _E_ ) is true for some _E ⊂ X_ , then _P_ ( _X\E_ ) is true also. 

(iv) If _E_ 1 _, E_ 2 _, . . . ⊂ X_ are such that _P_ ( _En_ ) is true for all _n_ , then _P_ ([�] _[∞] n_ =1 _[E][n]_[)][is][true][also.] 

Then one can conclude that _P_ ( _E_ ) is true for all _E ∈⟨F⟩_ . Indeed, the set of all _E_ for which _P_ ( _E_ ) holds is a _σ_ -algebra that contains _F_ , whence the claim. This principle is particularly useful for establishing properties of Borel measurable sets (see below). 

We now turn to an important example of a _σ_ -algebra: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

87 

**Definition 1.4.16** (Borel _σ_ -algebra) **.** Let _X_ be a metric space, or more generally a topological space. The _Borel σ-algebra B_ [ _X_ ] of _X_ is defined to be the _σ_ -algebra generated by the open subsets of _X_ . Elements of _B_ [ _X_ ] will be called _Borel measurable_ . 

Thus, for instance, the Borel _σ_ -algebra contains the open sets, the closed sets (which are complements of open sets), the countable unions of closed sets (known as _Fσ sets_ ), the countable intersections of open sets (known as _Gδ sets_ ), the countable intersections of _Fσ_ sets, and so forth. 

In **R** _[d]_ , every open set is Lebesgue measurable, and so we see that the Borel _σ_ -algebra is coarser than the Lebesgue _σ_ -algebra. We will shortly see, though, that the two _σ_ -algebras are not equal. 

We defined the Borel _σ_ -algebra to be generated by the open sets. However, they are also generated by several other sets: 

**Exercise 1.4.14.** Show that the Borel _σ_ -algebra _B_ [ **R** _[d]_ ] of a Euclidean set is generated by any of the following collections of sets: 

- (i) The open subsets of **R** _[d]_ . 

- (ii) The closed subsets of **R** _[d]_ . 

- (iii) The compact subsets of **R** _[d]_ . 

- (iv) The open balls of **R** _[d]_ . 

- (v) The boxes in **R** _[d]_ . 

- (vi) The elementary sets in **R** _[d]_ . 

( _Hint:_ To show that two families _F, F[′]_ of sets generate the same _σ_ -algebra, it suffices to show that every _σ_ -algebra that contains _F_ , contains _F[′]_ also, and conversely.) 

There is an analogue of Exercise 1.4.9, which illustrates the extent to which a generated _σ_ -algebra is “larger” than the analogous generated Boolean algebra: 

**Exercise 1.4.15** (Recursive description of a generated _σ_ -algebra) **.** (This exercise requires familiarity with the theory of _ordinals_ , which is reviewed in _§_ 2.4 of _An epsilon of room, Vol. I_ . Recall that we are assuming the axiom of choice throughout this text.) Let _F_ be 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

88 

a collection of sets in a set _X_ , and let _ω_ 1 be the first uncountable ordinal. Define the sets _Fα_ for every countable ordinal _α ∈ ω_ 1 via induction as follows: 

   - (i) _Fα_ := _F_ . 

   - (ii) For each countable successor ordinal _α_ = _β_ + 1, we define _Fα_ to be the collection of all sets that either the union of an at most countable number of sets in _Fn−_ 1 (including the empty union _∅_ ), or the complement of such a union. 

- (iii) For each countable limit ordinal _α_ = sup _β<α β_ , we define _Fα_ :=[�] _β<α[F][β]_[.] 

- Show that _⟨F⟩_ =[�] _α∈ω_ 1 _[F][α]_[.] 

**Remark 1.4.17.** The first uncountable ordinal _ω_ 1 will make several further cameo appearances here and in _An epsilon of room, Vol. I_ , for instance by generating counterexamples to various plausible statements in point-set topology. In the case when _F_ is the collection of open sets in a topological space, so that _⟨F⟩_ , then the sets _Fα_ are essentially the _Borel hierarchy_ (which starts at the open and closed sets, then moves on to the _Fσ_ and _Gδ_ sets, and so forth); these play an important role in _descriptive set theory_ . 

**Exercise 1.4.16.** (This exercise requires familiarity with the theory of _cardinals_ .) Let _F_ be an infinite family of subsets of _X_ of cardinality _κ_ (thus _κ_ is an infinite cardinal). Show that _⟨F⟩_ has cardinality at most _κ[ℵ]_[0] . ( _Hint:_ use Exercise 1.4.15.) In particular, show that the Borel _σ_ -algebra _B_ [ **R** _[d]_ ] has cardinality at most _c_ := 2 _[ℵ]_[0] . 

Conclude that there exist Jordan measurable (and hence Lebesgue measurable) subsets of **R** _[d]_ which are not Borel measurable. ( _Hint:_ How many subsets of the Cantor set are there?) Use this to place the Borel _σ_ -algebra on the diagram that you drew for Exercise 1.4.8. 

**Remark 1.4.18.** Despite this demonstration that not all Lebesgue measurable subsets are Borel measurable, it is remarkably difficult (though not impossible) to exhibit a _specific_ set that is not Borel measurable. Indeed, a large majority of the explicitly constructible sets that one actually encounters in practice tend to be Borel measurable, and one can view the property of Borel measurability intuitively 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

89 

as a kind of “constructibility” property. (Indeed, as a _very_ crude first approximation, one can view the Borel measurable sets as those sets of “countable descriptive complexity”; in contrast, sets of finite descriptive complexity tend to be Jordan measurable (assuming they are bounded, of course). 

**Exercise 1.4.17.** Let _E, F_ be Borel measurable subsets of **R** _[d]_[1] _,_ **R** _[d]_[2] respectively. Show that _E ×F_ is a Borel measurable subset of **R** _[d]_[1][+] _[d]_[2] . ( _Hint:_ first establish this in the case when _F_ is a box, by using Remark 1.4.15. To obtain the general case, apply Remark 1.4.15 yet again.) 

The above exercise has a partial converse: 

**Exercise 1.4.18.** Let _E_ be a Borel measurable subset of **R** _[d]_[1][+] _[d]_[2] . 

- (i) Show that for any _x_ 1 _∈_ **R** _[d]_[1] , the slice _{x_ 2 _∈_ **R** _[d]_[2] : ( _x_ 1 _, x_ 2) _∈ E}_ is a Borel measurable subset of **R** _[d]_[2] . Similarly, show that for every _x_ 2 _∈_ **R** _[d]_[2] , the slice _{x_ 1 _∈_ **R** _[d]_[1] : ( _x_ 1 _, x_ 2) _∈ E}_ is a Borel measurable subset of **R** _[d]_[1] . 

- (ii) Give a counterexample to show that this claim is _not_ true if “Borel” is replaced with “Lebesgue” throughout. ( _Hint:_ the Cartesian product of any set with a point is a null set, even if the first set was not measurable.) 

**Exercise 1.4.19.** Show that the Lebesgue _σ_ -algebra on **R** _[d]_ is generated by the union of the Borel _σ_ -algebra and the null _σ_ -algebra. 

## **1.4.3. Countably additive measures and measure spaces.** Hav- 

ing set out the concept of a _σ_ -algebra a measurable space, we now endow these structures with a measure. 

We begin with the finitely additive theory, although this theory is too weak for our purposes and will soon be supplanted by the countably additive theory. 

**Definition 1.4.19** (Finitely additive measure) **.** Let _B_ be a Boolean algebra on a space _X_ . An (unsigned) _finitely additive measure µ_ on _B_ is a map _µ_ : _B →_ [0 _,_ + _∞_ ] that obeys the following axioms: 

- (i) (Empty set) _µ_ ( _∅_ ) = 0. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

90 

(ii) (Finite additivity) Whenever _E, F ∈B_ are disjoint, then _µ_ ( _E ∪ F_ ) = _µ_ ( _E_ ) + _µ_ ( _F_ ). 

**Remark 1.4.20.** The empty set axiom is needed in order to rule out the degenerate situation in which every set (including the empty set) has measure. 

**Example 1.4.21.** Lebesgue measure _m_ is a finitely additive measure on the Lebesgue _σ_ -algebra, and hence on all sub-algebras (such as the null algebra, the Jordan algebra, or the elementary algebra). In particular, Jordan measure and elementary measure are finitely additive (adopting the convention that co-Jordan measurable sets have infinite Jordan measure, and co-elementary sets have infinite elementary measure). 

On the other hand, as we saw in previous notes, Lebesgue outer measure is _not_ finitely additive on the discrete algebra, and Jordan outer measure is _not_ finitely additive on the Lebesgue algebra. 

**Example 1.4.22** (Dirac measure) **.** Let _x ∈ X_ and _B_ be an arbitrary Boolean algebra on _X_ . Then the _Dirac measure δx_ at _x_ , defined by setting _δx_ ( _E_ ) := 1 _E_ ( _x_ ), is finitely additive. 

**Example 1.4.23** (Zero measure) **.** The zero measure 0: _E �→_ 0 is a finitely additive measure on any Boolean algebra. 

**Example 1.4.24** (Linear combinations of measures) **.** If _B_ is a Boolean algebra on _X_ , and _µ, ν_ : _B →_ [0 _,_ + _∞_ ] are finitely additive measures on _B_ , then _µ_ + _ν_ : _E �→ µ_ ( _E_ )+ _ν_ ( _E_ ) is also a finitely additive measure, as is _cµ_ : _E �→ c × µ_ ( _E_ ) for any _c ∈_ [0 _,_ + _∞_ ]. Thus, for instance, the sum of Lebesgue measure and a Dirac measure is also a finitely additive measure on the Lebesgue algebra (or on any of its sub-algebras). 

**Example 1.4.25** (Restriction of a measure) **.** If _B_ is a Boolean algebra on _X_ , _µ_ : _B →_ [0 _,_ + _∞_ ] is a finitely additive measure, and _Y_ is a _Bmeasurable_ subset of _X_ , then the restriction _µ_ ⇂ _Y_ : _B_ ⇂ _Y →_ [0 _,_ + _∞_ ] of _B_ to _Y_ , defined by setting _µ_ ⇂ _Y_ ( _E_ ) := _µ_ ( _E_ ) whenever _E ∈B_ ⇂ _Y_ (i.e. if _E ∈B_ and _E ⊂ Y_ ), is also a finitely additive measure. 

**Example 1.4.26** (Counting measure) **.** If _B_ is a Boolean algebra on _X_ , then the function #: _B →_ [0 _,_ + _∞_ ] defined by setting #( _E_ ) to be 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

91 

the cardinality of _E_ if _E_ is finite, and #( _E_ ) := + _∞_ if _E_ is infinite, is a finitely additive measure, known as _counting measure_ . 

As with our definition of Boolean algebras and _σ_ -algebras, we adopted a “minimalist” definition so that the axioms are easy to verify. But they imply several further useful properties: 

**Exercise 1.4.20.** Let _µ_ : _B →_ [0 _,_ + _∞_ ] be a finitely additive measure on a Boolean _σ_ -algebra _B_ . Establish the following facts: 

- (i) (Monotonicity) If _E, F_ are _B_ -measurable and _E ⊂ F_ , then _µ_ ( _E_ ) _≤ µ_ ( _F_ ). 

- (ii) (Finite additivity) If _k_ is a natural number, and _E_ 1 _, . . . , Ek_ are _B_ -measurable and disjoint, then _µ_ ( _E_ 1 _∪ . . . ∪ Ek_ ) = _µ_ ( _E_ 1) + _. . ._ + _µ_ ( _Ek_ ). 

- (iii) (Finite subadditivity) If _k_ is a natural number, and _E_ 1 _, . . . , Ek_ are _B_ -measurable, then _µ_ ( _E_ 1 _∪ . . . ∪ Ek_ ) _≤ µ_ ( _E_ 1) + _. . ._ + _µ_ ( _Ek_ ). 

- (iv) (Inclusion-exclusion for two sets) If _E, F_ are _B_ -measurable, then _µ_ ( _E ∪ F_ ) + _µ_ ( _E ∩ F_ ) = _µ_ ( _E_ ) + _µ_ ( _F_ ). 

( _Caution:_ remember that the cancellation law _a_ + _c_ = _b_ + _c_ = _⇒ a_ = _b_ does not hold in [0 _,_ + _∞_ ] if _c_ is infinite, and so the use of cancellation (or subtraction) should be avoided if possible.) 

One can characterise measures completely for any finite algebra: 

**Exercise 1.4.21.** Let _B_ be a finite Boolean algebra, generated by a finite family _A_ 1 _, . . . , Ak_ of non-empty atoms. Show that for every finitely additive measure _µ_ on _B_ there exists _c_ 1 _, . . . , ck ∈_ [0 _,_ + _∞_ ] such that 

**==> picture [98 x 25] intentionally omitted <==**

Equivalently, if _xj_ is a point in _Aj_ for each 1 _≤ j ≤ k_ , then 

**==> picture [60 x 32] intentionally omitted <==**

Furthermore, show that the _c_ 1 _, . . . , ck_ are uniquely determined by _µ_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

92 

This is about the limit of what one can say about finitely additive measures at this level of generality. We now specialise to the _countably additive measures_ on _σ_ -algebras. 

**Definition 1.4.27** (Countably additive measure) **.** Let ( _X, B_ ) be a measurable space. An (unsigned) _countably additive measure µ_ on _B_ , or _measure_ for short, is a map _µ_ : _B →_ [0 _,_ + _∞_ ] that obeys the following axioms: 

   - (i) (Empty set) _µ_ ( _∅_ ) = 0. 

   - (ii) (Countable additivity) Whenever _E_ 1 _, E_ 2 _, . . . ∈B_ are a countable sequence of disjoint measurable sets, then _µ_ ([�] _[∞] n_ =1 _[E][n]_[) =] � _∞n_ =1 _[µ]_[(] _[E][n]_[).] 

- A triplet ( _X, B, µ_ ), where ( _X, B_ ) is a measurable space and _µ_ : _B →_ [0 _,_ + _∞_ ] is a countably additive measure, is known as a _measure space_ . 

Note the distinction between a measure space and a measurable space. The latter has the _capability_ to be equipped with a measure, but the former is _actually_ equipped with a measure. 

**Example 1.4.28.** Lebesgue measure is a countably additive measure on the Lebesgue _σ_ -algebra, and hence on every sub- _σ_ -algebra (such as the Borel _σ_ -algebra). 

**Example 1.4.29.** The Dirac measures from Exercise 1.4.22 are countably additive, as is counting measure. 

**Example 1.4.30.** Any restriction of a countably additive measure to a measurable subspace is again countably additive. 

**Exercise 1.4.22** (Countable combinations of measures) **.** Let ( _X, B_ ) be a measurable space. 

- (i) If _µ_ is a countably additive measure on _B_ , and _c ∈_ [0 _,_ + _∞_ ], then _cµ_ is also countably additive. 

- (ii) If _µ_ 1 _, µ_ 2 _, . . ._ are a sequence of countably additive measures on _B_ , then the sum[�] _[∞] n_ =1 _[µ][n]_[:] _[E][�→]_[�] _[∞] n_ =1 _[µ][n]_[(] _[E]_[)][is][also][a] countably additive measure. 

Note that countable additivity measures are necessarily finitely additive (by padding out a finite union into a countable union using 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

93 

the empty set), and so countably additive measures inherit all the properties of finitely additive properties, such as monotonicity and finite subadditivity. But one also has additional properties: 

**Exercise 1.4.23.** Let ( _X, B, µ_ ) be a measure space. 

- (i) (Countable subadditivity) If _E_ 1 _, E_ 2 _, . . ._ are _B_ -measurable, then _µ_ ([�] _[∞] n_ =1 _[E][n]_[)] _[ ≤]_[�] _[∞] n_ =1 _[µ]_[(] _[E][n]_[).] 

- (ii) (Upwards monotone convergence) If _E_ 1 _⊂ E_ 2 _⊂ . . ._ are _B_ - measurable, then 

**==> picture [166 x 29] intentionally omitted <==**

- (iii) (Downwards monotone convergence) If _E_ 1 _⊃ E_ 2 _⊃ . . ._ are 

   - _B_ -measurable, and _µ_ ( _En_ ) _< ∞_ for at least one _n_ , then 

**==> picture [162 x 28] intentionally omitted <==**

Show that the downward monotone convergence claim can fail if the hypothesis that _µ_ ( _En_ ) _< ∞_ for at least one _n_ is dropped. ( _Hint:_ mimic the solution to Exercise 1.2.11.) 

**Exercise 1.4.24** (Dominated convergence for sets) **.** Let ( _X, B, µ_ ) be a measure space. Let _E_ 1 _, E_ 2 _, . . ._ be a sequence of _B_ -measurable sets that converge to another set _E_ , in the sense that 1 _En_ converges pointwise to 1 _E_ . 

- (i) Show that _E_ is also _B_ -measurable. 

- (ii) If there exists a _B_ -measurable set _F_ of finite measure (i.e. 

   - _µ_ ( _F_ ) _< ∞_ ) that contains all of the _En_ , show that lim _n→∞ µ_ ( _En_ ) = _µ_ ( _E_ ). ( _Hint:_ Apply downward monotonicity to the sets � _n>N_[(] _[E][n]_[∆] _[E]_[).)] 

- (iii) Show that the previous part of this exercise can fail if the hypothesis that all the _En_ are contained in a set of finite measure is omitted. 

**Exercise 1.4.25.** Let _X_ be an at most countable set with the discrete _σ_ -algebra. Show that every measure _µ_ on this measurable space can 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

94 

be uniquely represented in the form 

**==> picture [57 x 23] intentionally omitted <==**

for some _cx ∈_ [0 _,_ + _∞_ ], thus 

**==> picture [63 x 23] intentionally omitted <==**

for all _E ⊂ X_ . (This claim fails in the uncountable case, although showing this is slightly tricky.) 

A useful technical property, enjoyed by some measure spaces, is that of _completeness_ : 

**Definition 1.4.31** (Completeness) **.** A _null set_ of a measure space ( _X, B, µ_ ) is defined to be a _B_ -measurable set of measure zero. A _subnull set_ is any subset of a null set. A measure space is said to be _complete_ if every sub-null set is a null set. 

Thus, for instance, the Lebesgue measure space ( **R** _[d] , L_ [ **R** _[d]_ ] _, m_ ) is complete, but the Borel measure space ( **R** _[d] , B_ [ **R** _[d]_ ] _, m_ ) is not (as can be seen from the solution to Exercise 1.4.16). 

Completion is a convenient property to have in some cases, particularly when dealing with properties that hold almost everywhere. Fortunately, it is fairly easy to modify any measure space to be complete: 

**Exercise 1.4.26** (Completion) **.** Let ( _X, B, µ_ ) be a measure space. Show that there exists a unique refinement ( _X, B, µ_ ), known as the _completion_ of ( _X, B, µ_ ), which is the coarsest refinement of ( _X, B, µ_ ) that is complete. Furthermore, show that _B_ consists precisely of those sets that differ from a _B_ -measurable set by a _B_ -subnull set. 

**Exercise 1.4.27.** Show that the Lebesgue measure space ( **R** _[d] , L_ [ **R** _[d]_ ] _, m_ ) is the completion of the Borel measure space ( **R** _[d] , B_ [ **R** _[d]_ ] _, m_ ). 

**Exercise 1.4.28** (Approximation by an algebra) **.** Let _A_ be a Boolean algebra on _X_ , and let _µ_ be a measure on _⟨A⟩_ . 

- (i) If _µ_ ( _X_ ) _< ∞_ , show that for every _E ∈⟨A⟩_ and _ε >_ 0 there exists _F ∈A_ such that _µ_ ( _E_ ∆ _F_ ) _< ε_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

95 

- (ii) More generally, if _X_ =[�] _[∞] n_ =1 _[A][n]_[for][some] _[A]_[1] _[, A]_[2] _[, . . .][∈A]_ with _µ_ ( _An_ ) _< ∞_ for all _n_ , _E ∈⟨A⟩_ has finite measure, and _ε >_ 0, show that there exists _F ∈A_ such that _µ_ ( _E_ ∆ _F_ ) _< ε_ . 

## **1.4.4. Measurable functions, and integration on a measure** 

**space.** Now we are ready to define integration on measure spaces. We first need the notion of a _measurable function_ , which is analogous to that of a continuous function in topology. Recall that a function _f_ : _X → Y_ between two topological spaces _X, Y_ is continuous if the inverse image _f[−]_[1] ( _U_ ) of any open set is open. In a similar spirit, we have 

**Definition 1.4.32.** Let ( _X, B_ ) be a measurable space, and let _f_ : _X →_ [0 _,_ + _∞_ ] or _f_ : _X →_ **C** be an unsigned or complex-valued function. We say that _f_ is _measurable_ if _f[−]_[1] ( _U_ ) is _B_ -measurable for every open subset _U_ of [0 _,_ + _∞_ ] or **C** . 

From Lemma 1.3.9, we see that this generalises the notion of a Lebesgue measurable function. 

**Exercise 1.4.29.** Let ( _X, B_ ) be a measurable space. 

- (i) Show that a function _f_ : _X →_ [0 _,_ + _∞_ ] is measurable if and only if the level sets _{x ∈ X_ : _f_ ( _x_ ) _> λ}_ are _B_ -measurable. 

- (ii) Show that an indicator function 1 _E_ of a set _E ⊂ X_ is measurable if and only if _E_ itself is _B_ -measurable. 

- (iii) Show that a function _f_ : _X →_ [0 _,_ + _∞_ ] or _f_ : _X →_ **C** is measurable if and only if _f[−]_[1] ( _E_ ) is _B_ -measurable for every Borel-measurable subset _E_ of [0 _,_ + _∞_ ] or **C** . 

- (iv) Show that a function _f_ : _X →_ **C** is measurable if and only if its real and imaginary parts are measurable. 

- (v) Show that a function _f_ : _X →_ **R** is measurable if and only if the magnitudes _f_ + := max( _f,_ 0), _f−_ := max( _−f,_ 0) of its positive and negative parts are measurable. 

- (vi) If _fn_ : _X →_ [0 _,_ + _∞_ ] are a sequence of measurable functions that converge pointwise to a limit _f_ : _X →_ [0 _,_ + _∞_ ], then show that _f_ is also measurable. Obtain the same claim if [0 _,_ + _∞_ ] is replaced by **C** . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

96 

- (vii) If _f_ : _X →_ [0 _,_ + _∞_ ] is measurable and _φ_ : [0 _,_ + _∞_ ] _→_ [0 _,_ + _∞_ ] is continuous, show that _φ ◦ f_ is measurable. Obtain the same claim if [0 _,_ + _∞_ ] is replaced by **C** . 

- (viii) Show that the sum or product of two measurable functions in [0 _,_ + _∞_ ] or **C** is still measurable. 

**Remark 1.4.33.** One can also view measurable functions in a more _category theoretic_ fashion. Define _measurable morphism_ or _measurable map f_ from one measurable space ( _X, B_ ) to another ( _Y, C_ ) to be a function _f_ : _X → Y_ with the property that _f[−]_[1] ( _E_ ) is _B_ -measurable for every _C_ -measurable set _E_ . Then a measurable function _f_ : _X →_ [0 _,_ + _∞_ ] or _f_ : _X →_ **C** is the same thing as a measurable morphism from _X_ to [0 _,_ + _∞_ ] or **C** , where the latter is equipped with the Borel _σ_ -algebra. Also, one _σ_ -algebra _B_ on a space _X_ is coarser than another _B[′]_ precisely when the identity map id _X_ : _X → X_ is a measurable morphism from ( _X, B[′]_ ) to ( _X, B_ ). The main purpose of adopting this viewpoint is that it is obvious that the composition of measurable morphisms is again a measurable morphism. This is important in those fields of mathematics, such as _ergodic theory_ (discussed in [ **Ta2009** ]), in which one frequently wishes to compose measurable transformations (and in particular, to compose a transformation _T_ : ( _X, B_ ) _→_ ( _X, B_ ) with itself repeatedly); but it will not play a major role in this text. 

Measurable functions are particularly easy to describe on atomic spaces: 

**Exercise 1.4.30.** Let ( _X, B_ ) be a measurable space that is atomic, thus _B_ = _A_ (( _Aα_ ) _α∈I_ ) for some partition _X_ =[�] _α∈I[A][α]_[of] _[X]_[into] disjoint non-empty atoms. Show that a function _f_ : _X →_ [0 _,_ + _∞_ ] or _f_ : _X →_ **C** is measurable if and only if it is constant on each atom, or equivalently if one has a representation of the form 

**==> picture [63 x 23] intentionally omitted <==**

for some constants _cα_ in [0 _,_ + _∞_ ] or in **C** as appropriate. Furthermore, the _cα_ are uniquely determined by _f_ . 

**Exercise 1.4.31** (Egorov’s theorem) **.** Let ( _X, B, µ_ ) be a finite measure space (so _µ_ ( _X_ ) _< ∞_ ), and let _fn_ : _X →_ **C** be a sequence of 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

97 

measurable functions that converge pointwise almost everywhere to a limit _f_ : _X →_ **C** , and let _ε >_ 0. Show that there exists a measurable set _E_ of measure at most _ε_ such that _fn_ converges uniformly to _f_ outside of _E_ . Give an example to show that the claim can fail when the measure _µ_ is not finite. 

In Section 1.3 we defined first an simple integral, then an unsigned integral, and then finally an absolutely convergent integral. We perform the same three stages here. We begin with the simple integral, which in the abstract setting becomes integration in the case when the _σ_ -algebra is finite: 

**Definition 1.4.34** (Simple integral) **.** Let ( _X, B, µ_ ) be a measure space with _B_ finite. By Exercise 1.4.4, _X_ is partitioned into a finite number of atoms _A_ 1 _, . . . , An_ . If _f_ : _X →_ [0 _,_ + _∞_ ] is measurable, then by Exercise 1.4.30 it has a unique representation of the form 

**==> picture [57 x 28] intentionally omitted <==**

for some _c_ 1 _, . . . , cn ∈_ [0 _,_ + _∞_ ]. We then define the _simple integral_ Simp � _X[f][dµ]_[of] _[f]_[by][the][formula] 

**==> picture [128 x 28] intentionally omitted <==**

Note that, thanks to Exercise 1.4.3, the precise decomposition into atoms does not affect the definition of the simple integral. 

**Exercise 1.4.32.** Propose a definition for the simple integral for absolutely convergent complex-valued functions on a measurable space with a finite _σ_ -algebra. 

With this definition, it is clear that one has the monotonicity property 

Simp _f dµ ≤_ Simp _g dµ_ � _X_ � _X_ 

whenever _f ≤ g_ are unsigned measurable, as well as the linearity properties 

**==> picture [220 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

98 

and 

**==> picture [154 x 23] intentionally omitted <==**

for unsigned measurable _f, g_ and _c ∈_ [0 _,_ + _∞_ ]. We also make the following important technical observation: 

**Exercise 1.4.33** (Simple integral unaffected by refinements) **.** Let ( _X, B, µ_ ) be a measure space, and let ( _X, B[′] , µ[′]_ ) be a _refinement_ of ( _X, B, µ_ ), which means that _B[′]_ contains _B_ and _µ[′]_ : _B[′] →_ [0 _,_ + _∞_ ] agrees with _µ_ : _B →_ [0 _,_ + _∞_ ] on _B_ . Suppose that both _B, B[′]_ are finite, and let _f_ : _B →_ [0 _,_ + _∞_ ] be measurable. Show that 

**==> picture [138 x 24] intentionally omitted <==**

This allows one to extend the simple integral to simple functions: 

**Definition 1.4.35** (Integral of simple functions) **.** An (unsigned) _simple function f_ : _X →_ [0 _,_ + _∞_ ] on a measurable space ( _X, B_ ) is a measurable function that takes on finitely many values _a_ 1 _, . . . , ak_ . Note that such a function is then automatically measurable with respect to at least one finite sub- _σ_ -algebra _B[′]_ of _B_ , namely the _σ_ -algebra _B[′]_ generated by the preimages _f[−]_[1] ( _{a_ 1 _}_ ) _, . . . , f[−]_[1] ( _{ak}_ ) of _a_ 1 _, . . . , ak_ . We then define the simple integral Simp � _X[f][dµ]_[by][the][formula] 

**==> picture [154 x 24] intentionally omitted <==**

where _µ_ ⇂ _B′_ : _B[′] →_ [0 _,_ + _∞_ ] is the restriction of _µ_ : _B →_ [0 _,_ + _∞_ ] to _B[′]_ . 

Note that there could be multiple finite _σ_ -algebras with respect to which _f_ is measurable, but Exercise 1.4.33 guarantees that all such extensions will give the same simple integral. Indeed, if _f_ were measurable with respect to two separate finite sub- _σ_ -algebras _B[′]_ and _B[′′]_ of _B_ , then it would also be measurable with respect to their common refinement _B[′] ∨B[′′]_ := _⟨B[′] ∪B[′′] ⟩_ , which is also finite (by Exercise 1.4.8), and then by Exercise 1.4.33, � _X[f][dµ]_[⇂] _[B][′]_[and] � _X[f][dµ]_[⇂] _[B][′′]_[are][both] equal to � _X[f][dµ]_[ ⇂] _[B][′][∨B][′′]_[,][and][hence][equal][to][each][other.] 

From this we can deduce the following properties of the simple integral. As with the Lebesgue theory, we say that a property _P_ ( _x_ ) of an element _x ∈ X_ of a measure space ( _X, B, µ_ ) holds _µ-almost everywhere_ if it holds outside of a sub-null set. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

99 

**Exercise 1.4.34** (Basic properties of the simple integral) **.** Let ( _X, B, µ_ ) be a measure space, and let _f, g_ : _X →_ [0 _,_ + _∞_ ] be simple functions. 

- (i) (Monotonicity) If _f ≤ g_ pointwise, then Simp � _X[f][dµ][≤]_ Simp � _X[g][dµ]_[.] 

- (ii) (Compatibility with measure) For every _B_ -measurable set _E_ , we have Simp � _X_[1] _[E][dµ]_[ =] _[ µ]_[(] _[E]_[).] 

- (iii) (Homogeneity) For every _c ∈_ [0 _,_ + _∞_ ], one has Simp � _X[cf][dµ]_[ =] _c ×_ Simp � _X[f][dµ]_[.] 

- (iv) (Finite additivity) Simp � _X_[(] _[f]_[+] _[g]_[)] _[dµ]_[=][Simp] � _X[f][dµ]_[+] Simp � _X[g][dµ]_[.] 

- (v) (Insensitivity to refinement) If ( _X, B[′] , µ[′]_ ) is a refinement of ( _X, B, µ_ ) (as defined in Exercise 1.4.33), then Simp � _X[f][dµ]_[ =] Simp � _X[f][dµ][′]_[.] 

- (vi) (Almost everywhere equivalence) If _f_ ( _x_ ) = _g_ ( _x_ ) for _µ_ -almost every _x ∈ X_ , then Simp � _X[f][dµ]_[ = Simp] � _X[g][dµ]_[.] 

- (vii) (Finiteness) Simp � _X[f][dµ][<][∞]_[if][and][only][if] _[f]_[is][finite] almost everywhere, and is supported on a set of finite measure. 

- (viii) (Vanishing) Simp � _X[f][dµ]_[ = 0 if and only if] _[ f]_[is zero almost] everywhere. 

**Exercise 1.4.35** (Inclusion-exclusion principle) **.** Let ( _X, B, µ_ ) be a measure space, and let _A_ 1 _, . . . , An_ be _B_ -measurable sets of finite measure. Show that 

**==> picture [216 x 32] intentionally omitted <==**

**==> picture [300 x 13] intentionally omitted <==**

**Remark 1.4.36.** The simple integral could also be defined on finitely additive measure spaces, rather than countably additive ones, and all the above properties would still apply. However, on a finitely additive measure space one would have difficulty extending the integral beyond simple functions, as we will now do. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

100 

From the simple integral, we can now define the unsigned integral, in analogy to how the unsigned Lebesgue integral was constructed in Section 1.3.3. 

**Definition 1.4.37.** Let ( _X, B, µ_ ) be a measure space, and let _f_ : _X →_ [0 _,_ + _∞_ ] be measurable. Then we define the unsigned integral � _X[f][dµ]_ of _f_ by the formula 

**==> picture [239 x 27] intentionally omitted <==**

Clearly, this definition generalises Definition 1.3.13. Indeed, if _f_ : **R** _[d] →_ [0 _,_ + _∞_ ] is Lebesgue measurable, then � **R** _[d][ f]_[(] _[x]_[)] _[ dx]_[ =] � **R** _[d][ f][dm]_[.] 

We record some easy properties of this integral: 

**Exercise 1.4.36** (Easy properties of the unsigned integral) **.** Let ( _X, B, µ_ ) be a measure space, and let _f, g_ : _X →_ [0 _,_ + _∞_ ] be measurable. 

- (i) (Almost everywhere equivalence) If _f_ = _g µ_ -almost everywhere, then � _X[f][dµ]_[ =] � _X[g][dµ]_ 

- (ii) (Monotonicity) If _f ≤ g µ_ -almost everywhere, then � _X[f][dµ][ ≤][dµ]_[.] 

- � _X[g]_ 

- (iii) (Homogeneity) We have � _X[cf][dµ]_[=] _[c]_ � _X[f][dµ]_[for][every] _c ∈_ [0 _,_ + _∞_ ]. 

- (iv) (Superadditivity) We have � _X_[(] _[f]_[+] _[g]_[)] _[ dµ][ ≥]_ � _X[f][dµ]_[+] � _X[g dµ]_[.] (v) (Compatibility with the simple integral) If _f_ is simple, then _[dµ]_[ = Simp] _[dµ]_[.] 

- � _X[f]_ � _X[f]_ 

- (vi) (Markov’s inequality) For any 0 _< λ < ∞_ , one has 

**==> picture [160 x 23] intentionally omitted <==**

In particular, if � _X[f][dµ <][ ∞]_[, then the sets] _[ {][x][ ∈][X]_[:] _[ f]_[(] _[x]_[)] _[ ≥] λ}_ have finite measure for each _λ >_ 0. 

- (vii) (Finiteness) If � _X[f][dµ <][ ∞]_[, then] _[ f]_[(] _[x]_[) is finite for] _[ µ]_[-almost] every _x_ . 

- (viii) (Vanishing) If � _X[f][dµ]_[=][0,][then] _[f]_[(] _[x]_[)][is][zero][for] _[µ]_[-almost] every _x_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

101 

- (ix) (Vertical truncation) We have lim _n→∞_ � _X_[min(] _[f, n]_[)] _[dµ]_[=] _[dµ]_[.] 

- � _X[f]_ 

- (x) (Horizontal truncation) If _E_ 1 _⊂ E_ 2 _⊂ . . ._ is an increasing sequence of _B_ -measurable sets, then 

**==> picture [164 x 24] intentionally omitted <==**

(xi) (Restriction) If _Y_ is a measurable subset of _X_ , then � _X[f]_[1] _[Y][dµ]_[ =] � _Y[f]_[⇂] _[Y][dµ]_[⇂] _[Y]_[ ,][where] _[f]_[⇂] _[Y]_[:] _[Y][→]_[[0] _[,]_[ +] _[∞]_[]][is][the][restric-] tion of _f_ : _X →_ [0 _,_ + _∞_ ] to _Y_ , and the restriction _µ_ ⇂ _Y_ was defined in Example 1.4.25. We will often abbreviate � _Y[f]_[⇂] _[Y][dµ]_[ ⇂] _[Y]_[(by][slight][abuse][of][notation)][as] � _Y[f][dµ]_[.] 

As before, one of the key properties of this integral is its additivity: 

**Theorem 1.4.38.** _Let_ ( _X, B, µ_ ) _be a measure space, and let f, g_ : _X →_ [0 _,_ + _∞_ ] _be measurable. Then_ 

**==> picture [158 x 23] intentionally omitted <==**

**Proof.** In view of superadditivity, it suffices to establish the subad- 

**==> picture [79 x 37] intentionally omitted <==**

**==> picture [149 x 24] intentionally omitted <==**

We establish this in stages. We first deal with the case when _µ_ is a _finite_ measure (which means that _µ_ ( _X_ ) _< ∞_ ) and _f, g_ are bounded. Pick an _ε >_ 0, and let _fε_ be _f_ rounded down to the nearest integer multiple of _ε_ , and _f[ε]_ be _f_ rounded up to the nearest integer multiple. Clearly, we have the pointwise bounds 

**==> picture [94 x 11] intentionally omitted <==**

and 

**==> picture [80 x 11] intentionally omitted <==**

Since _f_ is bounded, _fε_ and _f[ε]_ are simple. Similarly define _gε, g[ε]_ . We then have the pointwise bound 

**==> picture [138 x 11] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

102 

hence by Exercise 1.4.36 and the properties of the simple integral, 

**==> picture [250 x 77] intentionally omitted <==**

From (1.14) we conclude that 

**==> picture [196 x 23] intentionally omitted <==**

Letting _ε →_ 0 and using the assumption that _µ_ ( _X_ ) is finite, we obtain the claim. 

Now we continue to assume that _µ_ is a finite measure, but now do not assume that _f, g_ are bounded. Then for any natural number _n_ , we can use the previous case to deduce that 

**==> picture [290 x 24] intentionally omitted <==**

Since min( _f_ + _g, n_ ) _≤_ min( _f, n_ ) + min( _g, n_ ), we conclude that 

**==> picture [240 x 24] intentionally omitted <==**

Taking limits as _n →∞_ using vertical truncation, we obtain the claim. 

Finally, we no longer assume that _µ_ is of finite measure, and also do not require _f, g_ to be bounded. If either � _X[f][dµ]_[or] � _X[g][dµ]_[is] infinite, then by monotonicity, � _X[f]_[ +] _[ g][dµ]_[is][infinite][as][well,][and][the] claim follows; so we may assume that � _X[f][dµ]_[and] � _X[g][dµ]_[are][both] finite. By Markov’s inequality (Exercise 1.4.36(vi)), we conclude that for each natural number _n_ , the set _En_ := _{x ∈ X_ : _f_ ( _x_ ) _> n_[1] _[} ∪{][x][ ∈] X_ : _g_ ( _x_ ) _> n_[1] _[}]_[ has finite measure.][These sets are increasing in] _[ n]_[,][and] _f, g, f_ + _g_ are supported on[�] _[∞] n_ =1 _[E][n]_[, and so by horizontal truncation] 

**==> picture [172 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

103 

From the previous case, we have 

**==> picture [206 x 24] intentionally omitted <==**

Letting _n →∞_ and using horizontal truncation we obtain the claim. □ 

**Exercise 1.4.37** (Linearity in _µ_ ) **.** Let ( _X, B, µ_ ) be a measure space, and let _f_ : _X →_ [0 _,_ + _∞_ ] be measurable. 

(i) Show that � _X[f][d]_[(] _[cµ]_[) =] _[ c][ ×]_ � _X[f][dµ]_[for][every] _[c][ ∈]_[[0] _[,]_[ +] _[∞]_[].] (ii) If _µ_ 1 _, µ_ 2 _, . . ._ are a sequence of measures on _B_ , show that 

**==> picture [134 x 29] intentionally omitted <==**

**Exercise 1.4.38** (Change of variables formula) **.** Let ( _X, B, µ_ ) be a measure space, and let _φ_ : _X → Y_ be a measurable morphism (as defined in Remark 1.4.33) from ( _X, B_ ) to another measurable space ( _Y, C_ ). Define the _pushforward φ∗µ_ : _C →_ [0 _,_ + _∞_ ] of _µ_ by _φ_ by the formula _φ∗µ_ ( _E_ ) := _µ_ ( _φ[−]_[1] ( _E_ )). 

- (i) Show that _φ∗µ_ is a measure on _C_ , so that ( _Y, C, φ∗µ_ ) is a measure space. 

**==> picture [278 x 25] intentionally omitted <==**

( _Hint:_ the quickest proof here is via the monotone convergence theorem (Theorem 1.4.44) below, but it is also possible to prove the exercise without this theorem.) 

**Exercise 1.4.39.** Let _T_ : **R** _[d] →_ **R** _[d]_ be an invertible linear transformation, and let _m_ be Lebesgue measure on **R** _[d]_ . Show that _T∗m_ = 1[where][the][pushforward] _[T][∗][m]_[of] _[m]_[was][defined][in][Exercise] _|_ det _T |[m]_[,] 1.4.38. 

**Exercise 1.4.40** (Sums as integrals) **.** Let _X_ be an arbitrary set (with the discrete _σ_ -algebra), let # be counting measure (see Exercise 1.4.26), and let _f_ : _X →_ [0 _,_ + _∞_ ] be an arbitrary unsigned function. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

104 

Show that _f_ is measurable with 

**==> picture [92 x 27] intentionally omitted <==**

Once one has the unsigned integral, one can define the absolutely convergent integral exactly as in the Lebesgue case: 

**Definition 1.4.39** (Absolutely convergent integral) **.** Let ( _X, B, µ_ ) be a measure space. A measurable function _f_ : _X →_ **C** is said to be _absolutely integrable_ if the unsigned integral 

**==> picture [112 x 23] intentionally omitted <==**

is finite, and use _L_[1] ( _X, B, µ_ ), _L_[1] ( _X_ ), or _L_[1] ( _µ_ ) to denote the space of absolutely integrable functions. If _f_ is real-valued and absolutely integrable, we define the integral � _X[f][dµ]_[by][the][formula] 

**==> picture [146 x 23] intentionally omitted <==**

where _f_ + := max( _f,_ 0), _f−_ := max( _−f,_ 0) are the magnitudes of the positive and negative components of _f_ . If _f_ is complex-valued and absolutely integrable, we define the integral � _X[f][dµ]_[by][the][formula] 

**==> picture [167 x 24] intentionally omitted <==**

where the two integrals on the right are interpreted as real-valued integrals. It is easy to see that the unsigned, real-valued, and complexvalued integrals defined in this manner are compatible on their common domains of 

Clearly, this definition generalises the Definition 1.3.17. 

We record some of the key facts about the absolutely convergent integral: 

**Exercise 1.4.41.** Let ( _X, B, µ_ ) be a measure space. 

- (i) Show that _L_[1] ( _X, B, µ_ ) is a complex vector space. 

- (ii) Show that the integration map _f �→_ � _X[f][dµ]_[is][a][complex-] linear map from _L_[1] ( _X, B, µ_ ) to **C** . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

105 

- (iii) Establish the triangle inequality _∥f_ + _g∥L_ 1( _µ_ ) _≤∥f ∥L_ 1( _µ_ ) + _∥g∥L_ 1( _µ_ ) and the homogeneity property _∥cf ∥L_ 1( _µ_ ) = _|c|∥f ∥L_ 1( _µ_ ) for all _f, g ∈ L_[1] ( _X, B, µ_ ) and _c ∈_ **C** . 

- (iv) Show that if _f, g ∈ L_[1] ( _X, B, µ_ ) are such that _f_ ( _x_ ) = _g_ ( _x_ ) for _µ_ -almost every _x ∈ X_ , then � _X[f][dµ]_[ =] � _X[g][dµ]_[.] 

- (v) If _f ∈ L_[1] ( _X, B, µ_ ), and ( _X, B[′] , µ[′]_ ) is a refinement of ( _X, B, µ_ ), then _f ∈ L_[1] ( _X, B[′] , µ[′]_ ), and � _X[f][dµ][′]_[=] � _X[f][dµ]_[.][(] _[Hint:]_[it] is easy to get one inequality. To get the other inequality, first work in the case when _f_ is both bounded and has finite measure support (i.e. is both vertically and horizontally truncated).) 

- (vi) Show that if _f ∈ L_[1] ( _X, B, µ_ ), then _∥f ∥L_ 1( _µ_ ) = 0 if and only if _f_ is zero _µ_ -almost everywhere. 

- (vii) If _Y ⊂ X_ is _B_ -measurable and _f ∈ L_[1] ( _X, B, µ_ ), then _f_ ⇂ _Y ∈ L_[1] ( _Y, B_ ⇂ _Y , µ_ ⇂ _Y_ ) and � _Y[f]_[⇂] _[Y] dµ_ ⇂ _Y_ = � _X[f]_[1] _[Y][dµ]_[.] As before, by abuse of notation we write � _Y[f][dµ]_[for] � _Y[f]_[⇂] _[Y] dµ_ ⇂ _Y_ . 

**1.4.5. The convergence theorems.** Let ( _X, B, µ_ ) be a measure space, and let _f_ 1 _, f_ 2 _, . . ._ : _X →_ [0 _,_ + _∞_ ] be a sequence of measurable functions. Suppose that as _n →∞_ , _fn_ ( _x_ ) converges pointwise either everywhere, or _µ_ -almost everywhere, to a measurable limit _f_ . A basic question in the subject is to determine the conditions under which such pointwise convergence would imply convergence of the integral: 

**==> picture [94 x 23] intentionally omitted <==**

To put it another way: when can we ensure that one can interchange integrals and limits, 

**==> picture [144 x 24] intentionally omitted <==**

There are certainly some cases in which one can safely do this: 

**Exercise 1.4.42** (Uniform convergence on a finite measure space) **.** Suppose that ( _X, B, µ_ ) is a _finite_ measure space (so _µ_ ( _X_ ) _< ∞_ ), and _fn_ : _X →_ [0 _,_ + _∞_ ] (resp. _fn_ : _X →_ **C** ) are a sequence of unsigned measurable functions (resp. absolutely integrable functions) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

106 

that converge _uniformly_ to a limit _f_ . Show that � _X[f][n][dµ]_[converges] to � _X[f][dµ]_[.] 

However, there are also cases in which one cannot interchange limits and integrals, even when the _fn_ are unsigned. We give the three classic examples, all of “moving bump” type, though the way in which the bump moves varies from example to example: 

**Example 1.4.40** (Escape to horizontal infinity) **.** Let _X_ be the real line with Lebesgue measure, and let _fn_ := 1[ _n,n_ +1]. Then _fn_ converges pointwise to _f_ := 0, but � **R** _[f][n]_[(] _[x]_[)] _[dx]_[=][1][does][not][converge] to � **R** _[f]_[(] _[x]_[)] _[dx]_[=][0.][Somehow,][all][the][mass][in][the] _[f][n]_[has][escaped][by] moving off to infinity in a horizontal direction, leaving none behind for the pointwise limit _f_ . 

**Example 1.4.41** (Escape to width infinity) **.** Let _X_ be the real line with Lebesgue measure, and let _fn_ := _n_[1][1][[0] _[,n]_[]][.][Then] _[ f][n]_[now converges] _uniformly f_ := 0, but � **R** _[f][n]_[(] _[x]_[)] _[dx]_[=][1][still][does][not][converge][to] � **R** _[f]_[(] _[x]_[)] _[dx]_[=][0.][Exercise][1.4.42][would][prevent][this][from][happening] if all the _fn_ were supported in a single set of finite measure, but the increasingly wide nature of the support of the _fn_ prevents this from happening. **Example 1.4.42** (Escape to vertical infinity) **.** Let _X_ be the unit interval [0 _,_ 1] with Lebesgue measure (restricted from **R** ), and let _fn_ := _n_ 1[ _n_ 1 _[,] n_[2][]][.][Now,][we][have][finite][measure,][and] _[f][n]_[converges][point-] wise to _f_ , but no uniform convergence. And again, �[0 _,_ 1] _[f][n]_[(] _[x]_[)] _[ dx]_[ = 1] is not converging to �[0 _,_ 1] _[f]_[(] _[x]_[)] _[dx]_[=][0.][This][time,][the][mass][has][es-] caped vertically, through the increasingly large values of _fn_ . 

**Remark 1.4.43.** From the perspective of _time-frequency analysis_ (or perhaps more accurately, space-frequency analysis), these three escapes are analogous (though not quite identical) to escape to spatial infinity, escape to zero frequency, and escape to infinite frequency respectively, thus describing the three different ways in which _phase space_ fails to be compact (if one excises the zero frequency as being singular). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

107 

However, once one shuts down these avenues of escape to infinity, it turns out that one can recover convergence of the integral. There are two major ways to accomplish this. One is to enforce _monotonicity_ , which prevents each _fn_ from abandoning the location where the mass of the preceding _f_ 1 _, . . . , fn−_ 1 was concentrated and which thus shuts down the above three escape scenarios. More precisely, we have the _monotone convergence theorem_ : 

**Theorem 1.4.44** (Monotone convergence theorem) **.** _Let_ ( _X, B, µ_ ) _be a measure space, and let_ 0 _≤ f_ 1 _≤ f_ 2 _≤ . . . be a monotone nondecreasing sequence of unsigned measurable functions on X. Then we have_ 

**==> picture [142 x 24] intentionally omitted <==**

Note that in the special case when each _fn_ is an indicator function _fn_ = 1 _En_ , this theorem collapses to the upwards monotone convergence property (Exercise 1.4.23(ii)). Conversely, the upwards monotone convergence property will play a key role in the proof of this theorem. 

**Proof.** Write _f_ := lim _n→∞ fn_ = sup _n fn_ , then _f_ : _X →_ [0 _,_ + _∞_ ] is measurable. Since the _fn_ are non-decreasing to _f_ , we see from monotonicity that � _X[f][n][dµ]_[are][non-decreasing][and][bounded][above] by � _X[f][dµ]_[,][which][gives][the][bound] 

**==> picture [114 x 23] intentionally omitted <==**

It remains to establish the reverse inequality 

**==> picture [114 x 23] intentionally omitted <==**

By definition, it suffices to show that 

**==> picture [114 x 24] intentionally omitted <==**

whenever _g_ is a simple function that is bounded pointwise by _f_ . By vertical truncation we may assume without loss of generality that _g_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

108 

also is finite everywhere, then we can write 

**==> picture [57 x 30] intentionally omitted <==**

for some 0 _≤ ci < ∞_ and some disjoint _B_ -measurable sets _A_ 1 _, . . . , Ak_ , thus 

**==> picture [100 x 30] intentionally omitted <==**

Let 0 _< ε <_ 1 be arbitrary. Then we have 

_f_ ( _x_ ) = sup _n[f][n]_[(] _[x]_[)] _[ >]_[ (1] _[ −][ε]_[)] _[c][i]_ 

for all _x ∈ Ai_ . Thus, if we define the sets 

**==> picture [156 x 11] intentionally omitted <==**

then the _Ai,n_ increase to _Ai_ and are measurable. By upwards monotonicity of measure, we conclude that 

**==> picture [96 x 15] intentionally omitted <==**

On the other hand, observe the pointwise bound 

**==> picture [97 x 31] intentionally omitted <==**

for any _n_ ; integrating this, we obtain 

**==> picture [144 x 30] intentionally omitted <==**

Taking limits as _n →∞_ , we obtain 

**==> picture [300 x 48] intentionally omitted <==**

**Remark 1.4.45.** It is easy to see that the result still holds if the monotonicity _fn ≤ fn_ +1 only holds almost everywhere rather than everywhere. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

109 

This has a number of important corollaries. Firstly, we can generalise (part of) Tonelli’s theorem for exchanging sums (see Theorem 0.0.2): 

**Corollary 1.4.46** (Tonelli’s theorem for sums and integrals) **.** _Let_ ( _X, B, µ_ ) _be a measure space, and let f_ 1 _, f_ 2 _, . . ._ : _X →_ [0 _,_ + _∞_ ] _be a sequence of unsigned measurable functions. Then one has_ 

**==> picture [130 x 28] intentionally omitted <==**

**Proof.** Apply the monotone convergence theorem (Theorem 1.4.44) to the partial sums _FN_ :=[�] _[N] n_ =1 _[f][n]_[.] □ 

**Exercise 1.4.43.** Give an example to show that this corollary can fail if the _fn_ are assumed to be absolutely integrable rather than unsigned measurable, even if the sum[�] _[∞] n_ =1 _[f][n]_[(] _[x]_[)][is][absolutely][convergent][for] each _x_ . ( _Hint:_ think about the three escapes to infinity.) 

**Exercise 1.4.44** (Borel-Cantelli lemma) **.** Let ( _X, B, µ_ ) be a measure space, and let _E_ 1 _, E_ 2 _, E_ 3 _, . . ._ be a sequence of _B_ -measurable sets such that[�] _[∞] n_ =1 _[µ]_[(] _[E][n]_[)] _[<][∞]_[.][Show][that][almost][every] _[x][∈][X]_[is][contained] in at most finitely many of the _En_ (i.e. _{n ∈_ **N** : _x ∈ En}_ is finite for almost every _x ∈ X_ ). ( _Hint:_ Apply Tonelli’s theorem to the indicator functions 1 _En_ .) 

## **Exercise 1.4.45.** 

- (i) Give an alternate proof of the Borel-Cantelli lemma (Exercise 1.4.44) that does not go through any of the convergence theorems, but instead exploits the more basic properties of measure from Exercise 1.4.23. 

- (ii) Give a counterexample that shows that the Borel-Cantelli lemma can fail if the condition[�] _[∞] n_ =1 _[µ]_[(] _[E][n]_[)] _[ <][ ∞]_[is][relaxed] to lim _n→∞ µ_ ( _En_ ) = 0. 

Secondly, when one does not have monotonicity, one can at least obtain an important inequality, known as _Fatou’s lemma_ : 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

110 

**Corollary 1.4.47** (Fatou’s lemma) **.** _Let_ ( _X, B, µ_ ) _be a measure space, and let f_ 1 _, f_ 2 _, . . ._ : _X →_ [0 _,_ + _∞_ ] _be a sequence of unsigned measurable functions. Then_ 

**==> picture [156 x 24] intentionally omitted <==**

**Proof.** Write _FN_ := inf _n≥N fn_ for each _N_ . Then the _FN_ are measurable and non-decreasing, and hence by the monotone convergence theorem (Theorem 1.4.44) 

**==> picture [142 x 24] intentionally omitted <==**

By definition of lim inf, we have sup _N>_ 0 _FN_ = lim inf _n→∞ fn_ . By monotonicity, we have � _X[F][N][dµ][ ≤]_ � _X[f][n][dµ]_[for][all] _[n][ ≥][N]_[,][and][thus] 

**==> picture [120 x 23] intentionally omitted <==**

**==> picture [300 x 65] intentionally omitted <==**

**Remark 1.4.48.** Informally, Fatou’s lemma tells us that when taking the pointwise limit of unsigned functions _fn_ , that mass � _X[f][n][dµ]_ can be destroyed in the limit (as was the case in the three key moving bump examples), but it cannot be created in the limit. Of course the unsigned hypothesis is necessary here (consider for instance multiplying any of the moving bump examples by _−_ 1). While this lemma was stated only for pointwise limits, the same general principle (that mass can be destroyed, but not created, by the process of taking limits) tends to hold for other “weak” notions of convergence. See _§_ 1.9 of _An epsilon of room, Vol. I_ for some examples of this. 

Finally, we give the other major way to shut down loss of mass via escape to infinity, which is to _dominate_ all of the functions involved by an absolutely convergent one. This result is known as the _dominated convergence theorem_ : 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

111 

**Theorem 1.4.49** (Dominated convergence theorem) **.** _Let_ ( _X, B, µ_ ) _be a measure space, and let f_ 1 _, f_ 2 _, . . ._ : _X →_ **C** _be a sequence of measurable functions that converge pointwise µ-almost everywhere to a measurable limit f_ : _X →_ **C** _. Suppose that there is an unsigned absolutely integrable function G_ : _X →_ [0 _,_ + _∞_ ] _such that |fn| are pointwise µ-almost everywhere bounded by G for each n. Then we have_ 

**==> picture [114 x 23] intentionally omitted <==**

From the moving bump examples we see that this statement fails if there is no absolutely integrable dominating function _G_ . The reader is encouraged to see why, in each of the moving bump examples, no such dominating function exists, without appealing to the above theorem. Note also that when each of the _fn_ is an indicator function _fn_ = 1 _En_ , the dominated convergence theorem collapses to Exercise 1.4.24. 

**Proof.** By modifying _fn, f_ on a null set, we may assume without loss of generality that the _fn_ converge to _f_ pointwise everywhere rather than _µ_ -almost everywhere, and similarly we can assume that _|fn_ are bounded by _G_ pointwise everywhere rather than _µ_ -almost everywhere. 

By taking real and imaginary parts we may assume without loss of generality that _fn, f_ are real, thus _−G ≤ fn ≤ G_ pointwise. Of course, this implies that _−G ≤ f ≤ G_ pointwise also. 

If we apply Fatou’s lemma (Corollary1.4.47) to the unsigned functions _fn_ + _G_ , we see that 

**==> picture [162 x 24] intentionally omitted <==**

which on subtracting the _finite_ quantity � _X[G][dµ]_[gives] 

**==> picture [122 x 23] intentionally omitted <==**

Similarly, if we apply that lemma to the unsigned functions _G − fn_ , we obtain 

**==> picture [162 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

112 

negating this inequality and then cancelling � _X[G][dµ]_[again][we][con-] clude that 

**==> picture [300 x 39] intentionally omitted <==**

**Remark 1.4.50.** We deduced the dominated convergence theorem from Fatou’s lemma, and Fatou’s lemma from the monotone convergence theorem. However, one can obtain these theorems in a different order, depending on one’s taste, as they are so closely related. For instance, in [ **StSk2005** ], the logic is somewhat different; one first obtains the slightly simpler _bounded convergence theorem_ , which is the dominated convergence theorem under the assumption that the functions are uniformly bounded and all supported on a single set of finite measure, and then uses that to deduce Fatou’s lemma, which in turn is used to deduce the monotone convergence theorem; and then the horizontal and vertical truncation properties are used to extend the bounded convergence theorem to the dominated convergence theorem. It is instructive to view a couple different derivations of these key theorems to get more of an intuitive understanding as to how they work. 

**Exercise 1.4.46.** Under the hypotheses of the dominated convergence theorem (Theorem 1.4.49), establish also that _∥fn − f ∥L_ 1 _→_ 0 as _n →∞_ . 

**Exercise 1.4.47** (Almost dominated convergence) **.** Let ( _X, B, µ_ ) be a measure space, and let _f_ 1 _, f_ 2 _, . . ._ : _X →_ **C** be a sequence of measurable functions that converge pointwise _µ_ -almost everywhere to a measurable limit _f_ : _X →_ **C** . Suppose that there is an unsigned absolutely integrable functions _G, g_ 1 _, g_ 2 _, . . ._ : _X →_ [0 _,_ + _∞_ ] such that the _|fn|_ are pointwise _µ_ -almost everywhere bounded by _G_ + _gn_ , and that � _X[g][n][dµ][ →]_[0][as] _[n][ →∞]_[.][Show][that] 

**==> picture [114 x 23] intentionally omitted <==**

**Exercise 1.4.48** (Defect version of Fatou’s lemma) **.** Let ( _X, B, µ_ ) be a measure space, and let _f_ 1 _, f_ 2 _, . . ._ : _X →_ [0 _,_ + _∞_ ] be a sequence of 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.4. Abstract measure spaces** 

113 

unsigned absolutely integrable functions that converges pointwise to an absolutely integrable limit _f_ . Show that 

**==> picture [180 x 23] intentionally omitted <==**

as _n →∞_ . ( _Hint:_ Apply the dominated convergence theorem (Theorem 1.4.49) to min( _fn, f_ ).) Informally, this result (first established in [ **BrLi1983** ]) tells us that the gap between the left and right hand sides of Fatou’s lemma can be measured by the quantity _∥f −fn∥L_ 1( _µ_ ). 

**Exercise 1.4.49.** Let ( _X, B, µ_ ) be a measure space, and let _g_ : _X →_ [0 _,_ + _∞_ ] be measurable. Show that the function _µg_ : _B →_ [0 _,_ + _∞_ ] defined by the formula 

**==> picture [136 x 24] intentionally omitted <==**

is a measure. (Such measures are studied in greater detail in _§_ 1.2 of _An epsilon of room, Vol. I_ .) 

The monotone convergence theorem is, in some sense, a defining property of the unsigned integral, as the following exercise illustrates. 

**Exercise 1.4.50** (Characterisation of the unsigned integral) **.** Let ( _X, B_ ) be a measurable space. _I_ : _f �→ I_ ( _f_ ) be a map from the space _U_ ( _X, B_ ) of unsigned measurable functions _f_ : _X →_ [0 _,_ + _∞_ ] to [0 _,_ + _∞_ ] that obeys the following axioms: 

- (i) (Homogeneity) For every _f ∈U_ ( _X, B_ ) and _c ∈_ [0 _,_ + _∞_ ], one has _I_ ( _cf_ ) = _cI_ ( _f_ ). 

- (ii) (Finite additivity) For every _f, g ∈U_ ( _X, B_ ), one has _I_ ( _f_ + _g_ ) = _I_ ( _f_ ) + _I_ ( _g_ ). 

- (iii) (Monotone convergence) If 0 _≤ f_ 1 _≤ f_ 2 _≤ . . ._ are a nondecreasing sequence of unsigned measurable functions, then _I_ (lim _n→∞ fn_ ) = lim _n→∞ I_ ( _fn_ ). 

Then there exists a unique measure _µ_ on ( _X, B_ ) such that _I_ ( _f_ ) = � _X[f][dµ]_[for][all] _[f][∈U]_[(] _[X,][ B]_[).][Furthermore,] _[µ]_[is][given][by][the][formula] _µ_ ( _E_ ) := _I_ (1 _E_ ) for all _B_ -measurable sets _E_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

114 

**Exercise 1.4.51.** Let ( _X, B, µ_ ) be a finite measure space (i.e. _µ_ ( _X_ ) _< ∞_ ), and let _f_ : _X →_ **R** be a bounded function. Suppose that _µ_ is _complete_ (see Definition 1.4.31). Suppose that the upper integral 

**==> picture [146 x 77] intentionally omitted <==**

and lower integral 

agree. Show that _f_ is measurable. (This is a converse to Exercise 1.3.11.) 

We will continue to see the monotone convergence theorem, Fatou’s lemma, and the dominated convergence theorem make an appearance throughout the rest of this text (and in _An epsilon of room, Vol. I_ ). 

## **1.5. Modes of convergence** 

If one has a sequence _x_ 1 _, x_ 2 _, x_ 3 _, . . . ∈_ **R** of real numbers _xn_ , it is unambiguous what it means for that sequence to converge to a limit _x ∈_ **R** : it means that for every _ε >_ 0, there exists an _N_ such that _|xn − x| ≤ ε_ for all _n > N_ . Similarly for a sequence _z_ 1 _, z_ 2 _, z_ 3 _, . . . ∈_ **C** of complex numbers _zn_ converging to a limit _z ∈_ **C** . 

More generally, if one has a sequence _v_ 1 _, v_ 2 _, v_ 3 _, . . ._ of _d_ -dimensional vectors _vn_ in a real vector space **R** _[d]_ or complex vector space **C** _[d]_ , it is also unambiguous what it means for that sequence to converge to a limit _v ∈_ **R** _[d]_ or _v ∈_ **C** _[d]_ ; it means that for every _ε >_ 0, there exists an _N_ such that _∥vn − v∥≤ ε_ for all _n ≥ N_ . Here, the norm _∥v∥_ of a vector _v_ = ( _v_[(1)] _, . . . , v_[(] _[d]_[)] ) can be chosen to be the Euclidean norm _∥v∥_ 2 := ([�] _[d] j_ =1[(] _[v]_[(] _[j]_[)][)][2][)][1] _[/]_[2][,][the][supremum][norm] _∥v∥∞_ := sup1 _≤j≤d |v_[(] _[j]_[)] _|_ , or any other number of norms, but for the purposes of convergence, these norms are all _equivalent_ ; a sequence of vectors converges in the Euclidean norm if and only if it converges in the supremum norm, and similarly for any other two norms on the finite-dimensional space **R** _[d]_ or **C** _[d]_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

115 

If however one has a sequence _f_ 1 _, f_ 2 _, f_ 3 _, . . ._ of functions _fn_ : _X →_ **R** or _fn_ : _X →_ **C** on a common domain _X_ , and a putative limit _f_ : _X →_ **R** or _f_ : _X →_ **C** , there can now be many different ways in which the sequence _fn_ may or may not converge to the limit _f_ . (One could also consider convergence of functions _fn_ : _Xn →_ **C** on different domains _Xn_ , but we will not discuss this issue at all here.) This is contrast with the situation with scalars _xn_ or _zn_ (which corresponds to the case when _X_ is a single point) or vectors _vn_ (which corresponds to the case when _X_ is a finite set such as _{_ 1 _, . . . , d}_ ). Once _X_ becomes infinite, the functions _fn_ acquire an infinite number of degrees of freedom, and this allows them to approach _f_ in any number of inequivalent ways. 

What different types of convergence are there? As an undergraduate, one learns of the following two basic _modes of convergence_ : 

- (i) We say that _fn_ converges to _f pointwise_ if, for every _x ∈ X_ , _fn_ ( _x_ ) converges to _f_ ( _x_ ). In other words, for every _ε >_ 0 and _x ∈ X_ , there exists _N_ (that depends on _both ε_ and _x_ ) such that _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤ ε_ whenever _n ≥ N_ . 

- (ii) We say that _fn_ converges to _f uniformly_ if, for every _ε >_ 0, there exists _N_ such that for every _n ≥ N_ , _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤ ε_ for every _x ∈ X_ . The difference between uniform convergence and pointwise convergence is that with the former, the time _N_ at which _fn_ ( _x_ ) must be permanently _ε_ -close to _f_ ( _x_ ) is not permitted to depend on _x_ , but must instead be chosen uniformly in _x_ . 

Uniform convergence implies pointwise convergence, but not conversely. A typical example: the functions _fn_ : **R** _→_ **R** defined by _fn_ ( _x_ ) := _x/n_ converge pointwise to the zero function _f_ ( _x_ ) := 0, but not uniformly. 

However, pointwise and uniform convergence are only two of dozens of many other modes of convergence that are of importance in analysis. We will not attempt to exhaustively enumerate these modes here (but see _§_ 1.9 of _An epsilon of room, Vol. I_ ). We will, however, discuss some of the modes of convergence that arise from measure theory, when the domain _X_ is equipped with the structure 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

116 

of a measure space ( _X, B, µ_ ), and the functions _fn_ (and their limit _f_ ) are measurable with respect to this space. In this context, we have some additional modes of convergence: 

- (i) We say that _fn_ converges to _f pointwise almost everywhere_ if, for ( _µ_ -)almost everywhere _x ∈ X_ , _fn_ ( _x_ ) converges to _f_ ( _x_ ). 

- (ii) We say that _fn_ converges to _f uniformly almost everywhere_ , _essentially uniformly_ , or _in L[∞] norm_ if, for every _ε >_ 0, there exists _N_ such that for every _n ≥ N_ , _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≤ ε_ for _µ_ -almost every _x ∈ X_ . 

- (iii) We say that _fn_ converges to _f almost uniformly_ if, for every _ε >_ 0, there exists an exceptional set _E ∈B_ of measure _µ_ ( _E_ ) _≤ ε_ such that _fn_ converges uniformly to _f_ on the complement of _E_ . 

- (iv) We say that _fn_ converges to _f in L_[1] _norm_ if the quantity _∥fn − f ∥L_ 1( _µ_ ) = � _X[|][f][n]_[(] _[x]_[)] _[ −][f]_[(] _[x]_[)] _[|][dµ]_[converges][to][0][as] _[n][ →] ∞_ . 

- (v) We say that _fn_ converges to _f in measure_ if, for every _ε >_ 0, the measures _µ_ ( _{x ∈ X_ : _|fn_ ( _x_ ) _− f_ ( _x_ ) _| ≥ ε}_ ) converge to zero as _n →∞_ . 

Observe that each of these five modes of convergence is unaffected if one modifies _fn_ or _f_ on a set of measure zero. In contrast, the pointwise and uniform modes of convergence can be affected if one modifies _fn_ or _f_ even on a single point. The _L_[1] and _L[∞]_ modes of converges are special cases of the _L[p]_ mode of convergence, which is discussed in _§_ 1.3 of _An epsilon of room, Vol. I_ . 

**Remark 1.5.1.** In the context of probability theory (see Section 2.3), in which _fn_ and _f_ are interpreted as random variables, convergence in _L_[1] norm is often referred to as _convergence in mean_ , pointwise convergence almost everywhere is often referred to as _almost sure convergence_ , and convergence in measure is often referred to as _convergence in probability_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

117 

**Exercise 1.5.1** (Linearity of convergence) **.** Let ( _X, B, µ_ ) be a measure space, let _fn, gn_ : _X →_ **C** be sequences of measurable functions, and let _f, g_ : _X →_ **C** be measurable functions. 

- (i) Show that _fn_ converges to _f_ along one of the above seven modes of convergence if and only if _|fn − f |_ converges to 0 along the same mode. 

- (ii) If _fn_ converges to _f_ along one of the above seven modes of convergence, and _gn_ converges to _g_ along the same mode, show that _fn_ + _gn_ converges to _f_ + _g_ along the same mode, and that _cfn_ converges to _cf_ along the same mode for any _c ∈_ **C** . 

- (iii) (Squeeze test) If _fn_ converges to 0 along one of the above seven modes, and _|gn| ≤ fn_ pointwise for each _n_ , show that _gn_ converges to 0 along the same mode. 

We have some easy implications between modes: 

**Exercise 1.5.2** (Easy implications) **.** Let ( _X, B, µ_ ) be a measure space, and let _fn_ : _X →_ **C** and _f_ : _X →_ **C** be measurable functions. 

- (i) If _fn_ converges to _f_ uniformly, then _fn_ converges to _f_ pointwise. 

- (ii) If _fn_ converges to _f_ uniformly, then _fn_ converges to _f_ in _L[∞]_ norm. Conversely, if _fn_ converges to _f_ in _L[∞]_ norm, then _fn_ converges to _f_ uniformly outside of a null set (i.e. there exists a null set _E_ such that the restriction _fn_ ⇂ _X\E_ of _fn_ to the complement of _E_ converges to the restriction _f_ ⇂ _X\E_ of _f_ ). 

- (iii) If _fn_ converges to _f_ in _L[∞]_ norm, then _fn_ converges to _f_ almost uniformly. 

- (iv) If _fn_ converges to _f_ almost uniformly, then _fn_ converges to _f_ pointwise almost everywhere. 

- (v) If _fn_ converges to _f_ pointwise, then _fn_ converges to _f_ pointwise almost everywhere. 

- (vi) If _fn_ converges to _f_ in _L_[1] norm, then _fn_ converges to _f_ in measure. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

118 

- (vii) If _fn_ converges to _f_ almost uniformly, then _fn_ converges to _f_ in measure. 

The reader is encouraged to draw a diagram that summarises the logical implications between the seven modes of convergence that the above exercise describes. 

We give four key examples that distinguish between these modes, in the case when _X_ is the real line **R** with Lebesgue measure. The first three of these examples already were introduced in Section 1.4, but the fourth is new, and also important. 

**Example 1.5.2** (Escape to horizontal infinity) **.** Let _fn_ := 1[ _n,n_ +1]. Then _fn_ converges to zero pointwise (and thus, pointwise almost everywhere), but not uniformly, in _L[∞]_ norm, almost uniformly, in _L_[1] norm, or in measure. 

**Example 1.5.3** (Escape to width infinity) **.** Let _fn_ := _n_[1][1][[0] _[,n]_[]][.][Then] _fn_ converges to zero uniformly (and thus, pointwise, pointwise almost everywhere, in _L[∞]_ norm, almost uniformly, and in measure), but not in _L_[1] norm. 

**Example 1.5.4** (Escape to vertical infinity) **.** Let _fn_ := _n_ 1[ _n_ 1 _[,] n_[2][]][.] Then _fn_ converges to zero pointwise (and thus, pointwise almost everywhere) and almost uniformly (and hence in measure), but not uniformly, in _L[∞]_ norm, or in _L_[1] norm. 

**Example 1.5.5** (Typewriter sequence) **.** Let _fn_ be defined by the formula 

**==> picture [88 x 16] intentionally omitted <==**

whenever _k ≥_ 0 and 2 _[k] ≤ n <_ 2 _[k]_[+1] . This is a sequence of indicator functions of intervals of decreasing length, marching across the unit interval [0 _,_ 1] over and over again. Then _fn_ converges to zero in measure and in _L_[1] norm, but not pointwise almost everywhere (and hence also not pointwise, not almost uniformly, nor in _L[∞]_ norm, nor uniformly). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

119 

**Remark 1.5.6.** The _L[∞] norm ∥f ∥L∞_ ( _µ_ ) of a measurable function _f_ : _X →_ **C** is defined to the infimum of all the quantities _M ∈_ [0 _,_ + _∞_ ] that are _essential upper bounds_ for _f_ in the sense that _|f_ ( _x_ ) _| ≤ M_ for almost every _x_ . Then _fn_ converges to _f_ in _L[∞]_ norm if and only if _∥fn − f ∥L∞_ ( _µ_ ) _→_ 0 as _n →∞_ . The _L[∞]_ and _L_[1] norms are part of the larger family of _L[p] norms_ , studied in _§_ 1.3 of _An epsilon of room, Vol. I_ . 

One particular advantage of _L_[1] convergence is that, in the case when the _fn_ are absolutely integrable, it implies convergence of the integrals, 

**==> picture [94 x 24] intentionally omitted <==**

as one sees from the triangle inequality. Unfortunately, none of the other modes of convergence automatically imply this convergence of the integral, as the above examples show. 

The purpose of these notes is to compare these modes of convergence with each other. Unfortunately, the relationship between these modes is not particularly simple; unlike the situation with pointwise and uniform convergence, one cannot simply rank these modes in a linear order from strongest to weakest. This is ultimately because the different modes react in different ways to the three “escape to infinity” scenarios described above, as well as to the “typewriter” behaviour when a single set is “overwritten” many times. On the other hand, if one imposes some additional assumptions to shut down one or more of these escape to infinity scenarios, such as a finite measure hypothesis _µ_ ( _X_ ) _< ∞_ or a _uniform integrability hypothesis_ , then one can obtain some additional implications between the different modes. 

**1.5.1. Uniqueness.** Throughout these notes, ( _X, B, µ_ ) denotes a measure space. We abbreviate “ _µ_ -almost everywhere” as “almost everywhere” throughout. 

Even though the modes of convergence all differ from each other, they are all _compatible_ in the sense that they never disagree about _which_ function _f_ a sequence of functions _fn_ converges to, outside of a set of measure zero. More precisely: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

120 

**Proposition 1.5.7.** _Let fn_ : _X →_ **C** _be a sequence of measurable functions, and let f, g_ : _X →_ **C** _be two additional measurable functions. Suppose that fn converges to f along one of the seven modes of convergence defined above, and fn converges to g along another of the seven modes of convergence (or perhaps the same mode of convergence as for f ). Then f and g agree almost everywhere._ 

Note that the conclusion is the best one can hope for in the case of the last five modes of convergence, since as remarked earlier, these modes of convergence are unaffected if one modifies _f_ or _g_ on a set of measure zero. 

**Proof.** In view of Exercise 1.5.2, we may assume that _fn_ converges to _f_ either pointwise almost everywhere, or in measure, and similarly that _fn_ converges to _g_ either pointwise almost everywhere, or in measure. 

Suppose first that _fn_ converges to both _f_ and _g_ pointwise almost everywhere. Then by Exercise 1.5.1, 0 converges to _f − g_ pointwise almost everywhere, which clearly implies that _f − g_ is zero almost everywhere, and the claim follows. A similar argument applies if _fn_ converges to both _f_ and _g_ in measure. 

By symmetry, the only remaining case that needs to be considered is when _fn_ converges to _f_ pointwise almost everywhere, and _fn_ converges to _g_ in measure. We need to show that _f_ = _g_ almost everywhere. It suffices to show that for every _ε >_ 0, that _|f_ ( _x_ ) _− g_ ( _x_ ) _| ≤ ε_ for almost every _x_ , as the claim then follows by setting _ε_ = 1 _/m_ for _m_ = 1 _,_ 2 _,_ 3 _, . . ._ and using the fact that the countable union of null sets is again a null set. 

Fix _ε >_ 0, and let _A_ := _{x ∈ X_ : _|f_ ( _x_ ) _− g_ ( _x_ ) _| > ε}_ . This is a measurable set; our task is to show that it has measure zero. Suppose for contradiction that _µ_ ( _A_ ) _>_ 0. We consider the sets 

**==> picture [228 x 11] intentionally omitted <==**

These are measurable sets that are increasing in _N_ . As _fn_ converges to _f_ almost everywhere, we see that almost every _x ∈ A_ belongs to at least one of the _AN_ , thus[�] _[∞] N_ =1 _[A][N]_[is][equal][to] _[A]_[outside][of][a][null] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

121 

set. In particular, 

**==> picture [70 x 28] intentionally omitted <==**

Applying monotone convergence for sets, we conclude that 

**==> picture [48 x 11] intentionally omitted <==**

for some finite _N_ . But by the triangle inequality, we have _|fn_ ( _x_ ) _− g_ ( _x_ ) _| > ε/_ 2 for all _x ∈ AN_ and all _n ≥ N_ . As a consequence, _fn_ cannot converge in measure to _g_ , which gives the desired contradiction. □ 

**1.5.2. The case of a step function.** One way to appreciate the distinctions between the above modes of convergence is to focus on the case when _f_ = 0, and when each of the _fn_ is a _step function_ , by which we mean a constant multiple _fn_ = _An_ 1 _En_ of a measurable set _En_ . For simplicity we will assume that the _An >_ 0 are positive reals, and that the _En_ have a positive measure _µ_ ( _En_ ) _>_ 0. We also assume the _An_ exhibit one of two modes of behaviour: either the _An_ converge to zero, or else they are bounded away from zero (i.e. there exists _c >_ 0 such that _An ≥ c_ for every _n_ . It is easy to see that if a sequence _An_ does not converge to zero, then it has a subsequence that is bounded away from zero, so it does not cause too much loss of generality to restrict to one of these two cases. 

Given such a sequence _fn_ = _An_ 1 _En_ of step functions, we now ask, for each of the seven modes of convergence, what it means for this sequence to converge to zero along that mode. It turns out that the answer to question is controlled more or less completely by the following three quantities: 

- (i) The _height An_ of the _n[th]_ function _fn_ ; 

- (ii) The _width µ_ ( _En_ ) of the _n[th]_ function _fn_ ; and 

**==> picture [280 x 25] intentionally omitted <==**

Indeed, we have: 

**Exercise 1.5.3** (Convergence for step functions) **.** Let the notation and assumptions be as above. Establish the following claims: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

122 

- (i) _fn_ converges uniformly to zero if and only if _An →_ 0 as _n →∞_ . 

- (ii) _fn_ converges in _L[∞]_ norm to zero if and only if _An →_ 0 as _n →∞_ . 

- (iii) _fn_ converges almost uniformly to zero if and only if _An →_ 0 as _n →∞_ , or _µ_ ( _EN[∗]_[)] _[ →]_[0][as] _[N][→∞]_[.] 

- (iv) _fn_ converges pointwise to zero if and only if _An →_ 0 as _n →∞_ , or[�] _[∞] N_ =1 _[E] N[∗]_[=] _[ ∅]_[.] 

- (v) _fn_ converges pointwise almost everywhere to zero if and only if _An →_ 0 as _n →∞_ , or[�] _[∞] N_ =1 _[E] N[∗]_[is][a][null][set.] 

- (vi) _fn_ converges in measure to zero if and only if _An →_ 0 as _n →∞_ , or _µ_ ( _En_ ) _→_ 0 as _n →∞_ . 

- (vii) _fn_ converges in _L_[1] norm if and only if _Anµ_ ( _En_ ) _→_ 0 as _n →∞_ . 

To put it more informally: when the height goes to zero, then one has convergence to zero in all modes except possibly for _L_[1] convergence, which requires that the product of the height and the width goes to zero. If instead the height is bounded away from zero and the width is positive, then we never have uniform or _L[∞]_ convergence, but we have convergence in measure if the width goes to zero, we have almost uniform convergence if the tail support (which has larger measure than the width) has measure that goes to zero, we have pointwise almost everywhere convergence if the tail support shrinks to a null set, and pointwise convergence if the tail support shrinks to the empty set. 

It is instructive to compare this exercise with Exercise 1.5.2, or with the four examples given in the introduction. In particular: 

- (i) In the escape to horizontal infinity scenario, the height and width do not shrink to zero, but the tail set shrinks to the empty set (while remaining of infinite measure throughout). 

- (ii) In the escape to width infinity scenario, the height goes to zero, but the width (and tail support) go to infinity, causing the _L_[1] norm to stay bounded away from zero. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

123 

- (iii) In the escape to vertical infinity, the height goes to infinity, but the width (and tail support) go to zero (or the empty set), causing the _L_[1] norm to stay bounded away from zero. 

- (iv) In the typewriter example, the width goes to zero, but the height and the tail support stay fixed (and thus bounded away from zero). 

**Remark 1.5.8.** The monotone convergence theorem (Theorem 1.4.44) can also be specialised to this case. Observe that the _fn_ = _An_ 1 _En_ are monotone increasing if and only if _An ≤ An_ +1 and _En ⊂ En_ +1 for each _n_ . In such cases, observe that the _fn_ converge pointwise to _f_ := _A_ 1 _E_ , where _A_ := lim _n→∞ An_ and _E_ :=[�] _[∞] n_ =1 _[E][n]_[.][The][mono-] tone convergence theorem then asserts that _Anµ_ ( _En_ ) _→ Aµ_ ( _E_ ) as _n →∞_ , which is a consequence of the monotone convergence theorem _µ_ ( _En_ ) _→ µ_ ( _E_ ) for sets. 

**1.5.3. Finite measure spaces.** The situation simplifies somewhat if the space _X_ has finite measure (and in particular, in the case when ( _X, B, µ_ ) is a _probability space_ , see Section 2.3). This shuts down two of the four examples (namely, escape to horizontal infinity or width infinity) and creates a few more equivalences. Indeed, from Egorov’s theorem (Exercise 1.4.31), we now have 

**Theorem 1.5.9** (Egorov’s theorem, again) **.** _Let X have finite measure, and let fn_ : _X →_ **C** _and f_ : _X →_ **C** _be measurable functions. Then fn converges to f pointwise almost everywhere if and only if fn converges to f almost uniformly._ 

Note that when one specialises to step functions using Exercise 1.5.3, then Egorov’s theorem collapses to the downward monotone convergence property for sets (Exercise 1.4.23(iii)). 

Another nice feature of the finite measure case is that _L[∞]_ convergence implies _L_[1] convergence: 

**Exercise 1.5.4.** Let _X_ have finite measure, and let _fn_ : _X →_ **C** and _f_ : _X →_ **C** be measurable functions. Show that if _fn_ converges to _f_ in _L[∞]_ norm, then _fn_ also converges to _f_ in _L_[1] norm. 

**1.5.4. Fast convergence.** The typewriter example shows that _L_[1] convergence is not strong enough to force almost uniform or pointwise 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

124 

almost everywhere convergence. However, this can be rectified if one assumes that the _L_[1] convergence is sufficiently fast: 

**Exercise 1.5.5** (Fast _L_[1] convergence) **.** Suppose that _fn, f_ : _X →_ **C** are measurable functions such that[�] _[∞] n_ =1 _[∥][f][n][−][f][∥][L]_[1][(] _[µ]_[)] _[<][∞]_[;][thus,] not only do the quantities _∥fn − f ∥L_ 1( _µ_ ) go to zero (which would mean _L_[1] convergence), but they converge in an absolutely summable fashion. 

- (i) Show that _fn_ converges pointwise almost everywhere to _f_ . 

- (ii) Show that _fn_ converges almost uniformly to _f_ . 

( _Hint:_ If you have trouble getting started, try working first in the special case in which _fn_ = _An_ 1 _En_ are step functions and _f_ = 0 and use Exercise 1.5.3 in order to gain some intuition. The second part of the exercise implies the first, but the first is a little easier to prove and may thus serve as a useful warmup. The _ε/_ 2 _[n]_ trick may come in handy for the second part.) 

As a corollary, we see that _L_[1] convergence implies almost uniform or pointwise almost everywhere convergence if we are allowed to pass to a subsequence: 

**Corollary 1.5.10.** _Suppose that fn_ : _X →_ **C** _are a sequence of measurable functions that converge in L_[1] _norm to a limit f . Then there exists a subsequence fnj that converges almost uniformly (and hence, pointwise almost everywhere) to f (while remaining convergent in L_[1] _norm, of course)._ 

**Proof.** Since _∥fn − f ∥L_ 1( _µ_ ) _→_ 0 as _n →∞_ , we can select _n_ 1 _< n_ 2 _< n_ 3 _< . . ._ such that _∥fnj − f ∥L_ 1( _µ_ ) _≤_ 2 _[−][j]_ (say). This is enough for the previous exercise to apply. □ 

Actually, one can strengthen this corollary a bit by relaxing _L_[1] convergence to convergence in measure: 

**Exercise 1.5.6.** Suppose that _fn_ : _X →_ **C** are a sequence of measurable functions that converge in measure to a limit _f_ . Then there exists a subsequence _fnj_ that converges almost uniformly (and hence, pointwise almost everywhere) to _f_ . ( _Hint:_ Choose the _nj_ so that the sets _{x ∈ X_ : _|fnj_ ( _x_ ) _− f_ ( _x_ ) _| >_ 1 _/j}_ have a suitably small measure.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

125 

It is instructive to see how this subsequence is extracted in the case of the typewriter sequence. In general, one can view the operation of passing to a subsequence as being able to eliminate “typewriter” situations in which the tail support is much larger than the width. 

**Exercise 1.5.7.** Let ( _X, B, µ_ ) be a measure space, let _fn_ : _X →_ **C** be a sequence of measurable functions converging pointwise almost everywhere as _n →∞_ to a measurable limit _f_ : _X →_ **C** , and for each _n_ , let _fn,m_ : _X →_ **C** be a sequence of measurable functions converging pointwise almost everywhere as _m →∞_ (keeping _n_ fixed) to _fn_ . 

- (i) If _µ_ ( _X_ ) is finite, show that there exists a sequence _m_ 1 _, m_ 2 _, . . ._ such that _fn,mn_ converges pointwise almost everywhere to _f_ . 

- (ii) Show the same claim is true if, instead of assuming that _µ_ ( _X_ ) is finite, we merely assume that _X_ is _σ-finite_ , i.e. it is the countable union of sets of measure. 

(The claim can fail if _X_ is not _σ_ -finite. A counterexample is if _X_ = **N[N]** with counting measure, _fn_ and _f_ are identically zero for all _n ∈_ **N** , and _fn,m_ is the indicator function the space of all sequences ( _ai_ ) _i∈_ **N** _∈_ **N[N]** with _an ≥ m_ .) 

**Exercise 1.5.8.** Let _fn_ : _X →_ **C** be a sequence of measurable functions, and let _f_ : _X →_ **C** be another measurable function. Show that the following are equivalent: 

- (i) _fn_ converges in measure to _f_ . 

- (ii) Every subsequence _fnj_ of the _fn_ has a further subsequence _fnji_ that converges almost uniformly to _f_ . 

**1.5.5. Domination and uniform integrability.** Now we turn to the reverse question, of whether almost uniform convergence, pointwise almost everywhere convergence, or convergence in measure can imply _L_[1] convergence. The escape to vertical and width infinity examples shows that without any further hypotheses, the answer to this question is no. However, one can do better if one places some _domination_ hypotheses on the _fn_ that shut down both of these escape routes. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

126 

We say that a sequence _fn_ : _X →_ **C** is _dominated_ if there exists an absolutely integrable function _g_ : _X →_ **C** such that _|fn_ ( _x_ ) _| ≤ g_ ( _x_ ) for all _n_ and almost every _x_ . For instance, if _X_ has finite measure and the _fn_ are uniformly bounded, then they are dominated. Observe that the sequences in the vertical and width escape to infinity examples are _not_ dominated (why?). 

The dominated convergence theorem (Theorem 1.4.49) then asserts that if _fn_ converges to _f_ pointwise almost everywhere, then it necessarily converges to _f_ in _L_[1] norm (and hence also in measure). Here is a variant: 

**Exercise 1.5.9.** Suppose that _fn_ : _X →_ **C** are a dominated sequence of measurable functions, and let _f_ : _X →_ **C** be another measurable function. Show that _fn_ converges in _L_[1] norm to _f_ if and only if _fn_ converges in measure to _f_ . ( _Hint:_ one way to establish the “if” direction is first show that every subsequence of the _fn_ has a further subsequence that converges in _L_[1] to _f_ , using Exercise 1.5.6 and the dominated convergence theorem (Theorem 1.4.49). Alternatively, use monotone convergence to find a set _E_ of finite measure such that � _X\E[g][dµ]_[,][and][hence] � _X\E[f][n][dµ]_[and] � _X\E[f][dµ]_[,][are][small.)] 

There is a more general notion than domination, known as _uniform integrability_ , which serves as a substitute for domination in many (but not all) contexts. 

**Definition 1.5.11** (Uniform integrability) **.** A sequence _fn_ : _X →_ **C** of absolutely integrable functions is said to be _uniformly integrable_ if the following three statements hold: 

- (i) (Uniform bound on _L_[1] norm) One has sup _n ∥fn∥L_ 1( _µ_ ) = sup _n_ � _X[|][f][n][|][dµ <]_[ +] _[∞]_[.] 

- (ii) (No escape to vertical infinity) One has sup _n_ � _|fn|≥M[|][f][n][|][ dµ][ →]_ 0 as _M →_ + _∞_ . 

- (iii) (No escape to width infinity) One has sup _n_ � _|fn|≤δ[|][f][n][|][ dµ][ →]_ 0 as _δ →_ 0. 

**Remark 1.5.12.** It is instructive to understand uniform integrability in the step function case _fn_ = _An_ 1 _En_ . The uniform bound on the 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

127 

_L_[1] norm then asserts that _Anµ_ ( _En_ ) stays bounded. The lack of escape to vertical infinity means that along any subsequence for which _An →∞_ , _Anµ_ ( _En_ ) must go to zero. Similarly, the lack of escape to width infinity means that along any subsequence for which _An →_ 0, _Anµ_ ( _En_ ) must go to zero. 

**Exercise 1.5.10.** (i) Show that if _f_ is an absolutely integrable function, then the constant sequence _fn_ = _f_ is uniformly integrable. ( _Hint:_ use the monotone convergence theorem.) 

- (ii) Show that every dominated sequence of measurable functions is uniformly integrable. 

- (iii) Give an example of a sequence that is uniformly integrable but not dominated. 

In the case of a finite measure space, there is no escape to width infinity, and the criterion for uniform integrability simplifies to just that of excluding vertical infinity: 

**Exercise 1.5.11.** Suppose that _X_ has finite measure, and let _fn_ : _X →_ **C** be a sequence of measurable functions. Show that _fn_ is uniformly integrable if and only if sup _n_ � _|fn|≥M[|][f][n][|][dµ][ →]_[0][as] _[M][→]_[+] _[∞]_[.] 

**Exercise 1.5.12** (Uniform _L[p]_ bound on finite measure implies uniform integrability) **.** Suppose that _X_ have finite measure, let 1 _< p < ∞_ , an d suppose that _fn_ : _X →_ **C** is a sequence of measurable functions such that sup _n_ � _X[|][f][n][|][p][dµ][<][∞]_[.][Show][that][the][sequence] _[f][n]_[is] uniformly integrable. 

**Exercise 1.5.13.** Let _fn_ : _X →_ **C** be a uniformly integrable sequence of functions. Show that for every _ε >_ 0 there exists a _δ >_ 0 such that 

**==> picture [64 x 24] intentionally omitted <==**

whenever _n ≥_ 1 and _E_ is a measurable set with _µ_ ( _E_ ) _≤ δ_ . 

**Exercise 1.5.14.** This exercise is a partial converse to Exercise 1.5.13. Let _X_ be a probability space, and let _fn_ : _X →_ **C** be a sequence of absolutely integrable functions with sup _n ∥fn∥L_ 1 _< ∞_ . Suppose that for every _ε >_ 0 there exists a _δ >_ 0 such that 

**==> picture [64 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

128 

whenever _n ≥_ 1 and _E_ is a measurable set with _µ_ ( _E_ ) _≤ δ_ . Show that the sequence _fn_ is uniformly integrable. 

The dominated convergence theorem (Theorem 1.4.49) does not have an analogue in the uniformly integrable setting: 

**Exercise 1.5.15.** Give an example of a sequence _fn_ of uniformly integrable functions that converge pointwise almost everywhere to zero, but do _not_ converge almost uniformly, in measure, or in _L_[1] norm. 

However, one _does_ have an analogue of Exercise 1.5.9: 

**Theorem 1.5.13** (Uniformly integrable convergence in measure) **.** _Let fn_ : _X →_ **C** _be a uniformly integrable sequence of functions, and let f_ : _X →_ **C** _be another function. Then fn converges in L_[1] _norm to f if and only if fn converges to f in measure._ 

**Proof.** The “only if” part follows from Exercise 1.5.2, so we establish the “if” part. 

By uniform integrability, there exists a finite _A >_ 0 such that 

**==> picture [66 x 24] intentionally omitted <==**

for all _n_ . By Exercise 1.5.6, there is a subsequence of the _fn_ that converges pointwise almost everywhere to _f_ . Applying Fatou’s lemma (Corollary1.4.47), we conclude that 

**==> picture [66 x 23] intentionally omitted <==**

thus _f_ is absolutely integrable. 

Now let _ε >_ 0 be arbitrary. By uniform integrability, one can find _δ >_ 0 such that 

**==> picture [190 x 26] intentionally omitted <==**

for all _n_ . By monotone convergence, and decreasing _δ_ if necessary, we may say the same for _f_ , thus 

**==> picture [187 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.5. Modes of convergence** 

129 

Let 0 _< κ < δ/_ 2 be another small quantity (that can depend on _A, ε, δ_ ) that we will choose a bit later. From (1.15), (1.16) and the hypothesis _κ < δ/_ 2 we have 

**==> picture [224 x 107] intentionally omitted <==**

Finally, from Markov’s inequality (Exercise 1.4.36(vi)) we have 

and thus 

**==> picture [180 x 62] intentionally omitted <==**

In particular, by shrinking _κ_ further if necessary we see that 

**==> picture [220 x 85] intentionally omitted <==**

Meanwhile, since _fn_ converges in measure to _f_ , we know that there exists an _N_ (depending on _κ_ ) such that 

**==> picture [114 x 11] intentionally omitted <==**

for all _n ≥ N_ . Applying Exercise 1.5.13, we conclude (making _κ_ smaller if necessary) that 

and 

**==> picture [92 x 64] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

130 

and hence by the triangle inequality 

**==> picture [116 x 26] intentionally omitted <==**

for all _n ≥ N_ . Combining this with (1.18) we conclude that 

**==> picture [300 x 41] intentionally omitted <==**

Finally, we recall two results from the previous notes for unsigned functions. 

**Exercise 1.5.16** (Monotone convergence theorem) **.** Suppose that _fn_ : _X →_ [0 _,_ + _∞_ ) are measurable, monotone non-decreasing in _n_ and are such that sup _n_ � _X[f][n][dµ][<][∞]_[.][Show][that] _[f][n]_[converges][in] _[L]_[1] norm to sup _n fn_ . (Note that sup _n fn_ can be infinite on a null set, but the definition of _L_[1] convergence can be easily modified to accomodate this.) 

**Exercise 1.5.17** (Defect version of Fatou’s lemma) **.** Suppose that _fn_ : _X →_ [0 _,_ + _∞_ ) are measurable, are such that sup _n_ � _X[f][n][dµ <][ ∞]_[,] and converge pointwise almost everywhere to some measurable limit _f_ : _X →_ [0 _,_ + _∞_ ). Show that _fn_ converges in _L_[1] norm to _f_ if and only if � _X[f][n][dµ]_[converges][to] � _X[f][dµ]_[.][Informally,][we][see][that][in][the] unsigned, bounded mass case, pointwise convergence implies _L_[1] norm convergence if and only if there is no loss of mass. 

**Exercise 1.5.18.** Suppose that _fn_ : _X →_ **C** are a dominated sequence of measurable functions, and let _f_ : _X →_ **C** be another measurable function. Show that _fn_ converges pointwise almost everywhere to _f_ if and only if _fn_ converges in almost uniformly to _f_ . 

**Exercise 1.5.19.** Let _X_ be a probability space (see Section 2.3). Given any real-valued measurable function _f_ : _X →_ **R** , we define the _cumulative distribution function F_ : **R** _→_ [0 _,_ 1] of _f_ to be the function _F_ ( _λ_ ) := _µ_ ( _{x ∈ X_ : _f_ ( _x_ ) _≤ λ}_ ). Given another sequence _fn_ : _X →_ **R** of real-valued measurable functions, we say that _fn converges in distribution_ to _f_ if the cumulative distribution function _Fn_ ( _λ_ ) of _fn_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

131 

converges pointwise to the cumulative distribution function _F_ ( _λ_ ) of _f_ at all _λ ∈_ **R** for which _F_ is continuous. 

- (i) Show that if _fn_ converges to _f_ in any of the seven senses discussed above (uniformly, essentially uniformly, almost uniformly pointwise, pointwise almost everywhere, in _L_[1] , or in measure), then it converges in distribution to _f_ . 

- (ii) Give an example in which _fn_ converges to _f_ in distribution, but not in any of the above seven senses. 

- (iii) Show that convergence in distribution is not linear, in the sense that if _fn_ converges to _f_ in distribution, and _gn_ converges to _g_ , then _fn_ + _gn_ need not converge to _f_ + _g_ . 

- (iv) Show that a sequence _fn_ can converge in distribution to two different limits _f, g_ , which are not equal almost everywhere. 

Convergence in distribution (not to be confused with convergence in the sense of _distributions_ , which is studied in S 1.13 of _An epsilon of room, Vol. I_ is commonly used in probability; but, as the above exercise demonstrates, it is quite a weak notion of convergence, lacking many of the properties of the modes of convergence discussed here. 

## **1.6. theorems** 

Let [ _a, b_ ] be a compact interval of positive length (thus _−∞ < a < b <_ + _∞_ ). Recall that a function _F_ : [ _a, b_ ] _→_ **R** is said to be _differentiable_ at a point _x ∈_ [ _a, b_ ] if the limit 

**==> picture [229 x 24] intentionally omitted <==**

exists. In that case, we call _F[′]_ ( _x_ ) the _strong derivative_ , _classical derivative_ , or just _derivative_ for short, of _F_ at _x_ . We say that _F_ is _everywhere differentiable_ , or _differentiable_ for short, if it is differentiable at all points _x ∈_ [ _a, b_ ], and _differentiable almost everywhere_ if it is differentiable at almost every point _x ∈_ [ _a, b_ ]. If _F_ is differentiable everywhere and its derivative _F[′]_ is continuous, then we say that _F_ is _continuously differentiable_ . 

**Remark 1.6.1.** In _§_ 1.13 of _An epsilon of room, Vol. I_ , the notion of a _weak derivative_ or _distributional derivative_ is introduced. This type 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

132 

of derivative can be applied to a much rougher class of functions and is in many ways more suitable than the classical derivative for doing “Lebesgue” type analysis (i.e. analysis centred around the Lebesgue integral, and in particular allowing functions to be uncontrolled, infinite, or even undefined on sets of measure zero). However, for now we will stick with the classical approach to differentiation. 

**Exercise 1.6.1.** If _F_ : [ _a, b_ ] _→_ **R** is everywhere differentiable, show that _F_ is continuous and _F[′]_ is measurable. If _F_ is almost everywhere differentiable, show that the (almost everywhere defined) function _F[′]_ is measurable (i.e. it is equal to an everywhere defined measurable function on [ _a, b_ ] outside of a null set), but give an example to demonstrate that _F_ need not be continuous. 

**Exercise 1.6.2.** Give an example of a function _F_ : [ _a, b_ ] _→_ **R** which is everywhere differentiable, but not continuously differentiable. ( _Hint:_ choose an _F_ that vanishes quickly at some point, say at the origin 0, but which also oscillates rapidly near that point.) 

In single-variable calculus, the operations of integration and differentiation are connected by a number of basic theorems, starting with _Rolle’s theorem_ . 

**Theorem 1.6.2** (Rolle’s theorem) **.** _Let_ [ _a, b_ ] _be a compact interval of positive length, and let F_ : [ _a, b_ ] _→_ **R** _be a differentiable function such that F_ ( _a_ ) = _F_ ( _b_ ) _. Then there exists x ∈_ ( _a, b_ ) _such that F[′]_ ( _x_ ) = 0 _._ 

**Proof.** By subtracting a constant from _F_ (which does not affect differentiability or the derivative) we may assume that _F_ ( _a_ ) = _F_ ( _b_ ) = 0. If _F_ is identically zero then the claim is trivial, so assume that _F_ is non-zero somewhere. By replacing _F_ with _−F_ if necessary, we may assume that _F_ is positive somewhere, thus sup _x∈_ [ _a,b_ ] _F_ ( _x_ ) _>_ 0. On the other hand, as _F_ is continuous and [ _a, b_ ] is compact, _F_ must attain its maximum somewhere, thus there exists _x ∈_ [ _a, b_ ] such that _F_ ( _x_ ) _≥ F_ ( _y_ ) for all _y ∈_ [ _a, b_ ]. Then _F_ ( _x_ ) must be positive and so _x_ cannot equal either _a_ or _b_ , and thus must lie in the interior. From the right limit of (1.19) we see that _F[′]_ ( _x_ ) _≤_ 0, while from the left limit we have _F[′]_ ( _x_ ) _≥_ 0. Thus _F[′]_ ( _x_ ) = 0 and the claim follows. □ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

133 

**Remark 1.6.3.** Observe that the same proof also works if _F_ is only differentiable in the interior ( _a, b_ ) of the interval [ _a, b_ ], so long as it is continuous all the way up to the boundary of [ _a, b_ ]. 

**Exercise 1.6.3.** Give an example to show that Rolle’s theorem can fail if _f_ is merely assumed to be almost everywhere differentiable, even if one adds the additional hypothesis that _f_ is continuous. This example illustrates that everywhere differentiability is a significantly stronger property than almost everywhere differentiability. We will see further evidence of this fact later in these notes; there are many theorems that assert in their conclusion that a function is almost everywhere differentiable, but few that manage to conclude _everywhere_ differentiability. 

**Remark 1.6.4.** It is important to note that Rolle’s theorem only works in the real scalar case when _F_ is real-valued, as it relies heavily on the least upper bound property for the domain **R** . If, for instance, we consider complex-valued scalar functions _F_ : [ _a, b_ ] _→_ **C** , then the theorem can fail; for instance, the function _F_ : [0 _,_ 1] _→_ **C** defined by _F_ ( _x_ ) := _e_[2] _[πix] −_ 1 vanishes at both endpoints and is differentiable, but its derivative _F[′]_ ( _x_ ) = 2 _πie_[2] _[πix]_ is never zero. (Rolle’s theorem does imply that the real and imaginary parts of the derivative _F[′]_ both vanish somewhere, but the problem is that they don’t _simultaneously_ vanish at the same point.) Similar remarks to functions taking values in a finite-dimensional vector space, such as **R** _[n]_ . 

One can easily amplify Rolle’s theorem to the _mean value theorem_ : 

**Corollary 1.6.5** (Mean value theorem) **.** _Let_ [ _a, b_ ] _be a compact interval of positive length, and let F_ : [ _a, b_ ] _→_ **R** _be a differentiable_[(] _[b]_[)] _[−][F]_[(] _[a]_[)] _function. Then there exists x ∈_ ( _a, b_ ) _such that F[′]_ ( _x_ ) = _[F] b−a ._ 

**Proof.** Apply Rolle’s theorem to the function _x �→ F_ ( _x_ ) _−[F]_[(] _[b] b_[)] _[−] −[F] a_[(] _[a]_[)] ( _x− a_ ). □ 

**Remark 1.6.6.** As Rolle’s theorem is only applicable to real scalarvalued functions, the more general mean value theorem is also only applicable to such functions. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

134 

**Exercise 1.6.4** (Uniqueness of antiderivatives up to constants) **.** Let [ _a, b_ ] be a compact interval of positive length, and let _F_ : [ _a, b_ ] _→_ **R** and _G_ : [ _a, b_ ] _→_ **R** be differentiable functions. Show that _F[′]_ ( _x_ ) = _G[′]_ ( _x_ ) for every _x ∈_ [ _a, b_ ] if and only if _F_ ( _x_ ) = _G_ ( _x_ ) + _C_ for some constant _C ∈_ **R** and all _x ∈_ [ _a, b_ ]. 

We can use the mean value theorem to deduce one of the fundamental theorems of calculus: 

**Theorem 1.6.7** (Second fundamental theorem of calculus) **.** _Let F_ : [ _a, b_ ] _→_ **R** _be a differentiable function, such that F[′] is Riemann integrable. b Then the Riemann integral_ � _a[F][ ′]_[(] _[x]_[)] _[dx][of][F][ ′][is][equal][to][F]_[(] _[b]_[)] _[−][F]_[(] _[a]_[)] _[.] b In particular, we have_ � _a[F][ ′]_[(] _[x]_[)] _[dx]_[=] _[F]_[(] _[b]_[)] _[−][F]_[(] _[a]_[)] _[whenever][F][is] continuously differentiable._ 

**Proof.** Let _ε >_ 0. By the definition of Riemann integrability, there exists a finite partition _a_ = _t_ 0 _< t_ 1 _< . . . < tk_ = _b_ such that 

**==> picture [166 x 31] intentionally omitted <==**

for every choice of _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[].] 

Fix this partition. From the mean value theorem, for each 1 _≤ j ≤ k_ one can find _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[]][such][that] 

**==> picture [156 x 13] intentionally omitted <==**

and thus by telescoping series 

**==> picture [300 x 41] intentionally omitted <==**

**Remark 1.6.8.** Even though the mean value theorem only holds for real scalar functions, the fundamental theorem of calculus holds for complex or vector-valued functions, as one can simply apply that theorem to each component of that function separately. 

Of course, we also have the other half of the fundamental theorem of calculus: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

135 

**Theorem 1.6.9** (First fundamental theorem of calculus) **.** _Let_ [ _a, b_ ] _be a compact interval of positive length. Let f_ : [ _a, b_ ] _→_ **C** _be a continuous function, and let F_ : [ _a, b_ ] _→_ **C** _be the indefinite integral F_ ( _x_ ) := � _ax[f]_[(] _[t]_[)] _[dt][.][Then][F][is][differentiable][on]_[[] _[a, b]_[]] _[,][with][deriv-] ative F[′]_ ( _x_ ) = _f_ ( _x_ ) _for all x ∈_ [ _a, b_ ] _. In particular, F is continuously differentiable._ 

**Proof.** It to show that 

**==> picture [132 x 22] intentionally omitted <==**

for all _x ∈_ [ _a, b_ ), and 

**==> picture [132 x 22] intentionally omitted <==**

for all _x ∈_ ( _a, b_ ]. After a change of variables, we can write 

**==> picture [157 x 26] intentionally omitted <==**

for any _x ∈_ [ _a, b_ ) and any sufficiently small _h >_ 0, or any _x ∈_ ( _a, b_ ] and any sufficiently small _h <_ 0. As _f_ is continuous, the function _t �→ f_ ( _x_ + _ht_ ) converges uniformly to _f_ ( _x_ ) on [0 _,_ 1] as _h →_ 0 (keeping _x_ 1 fixed). As the interval [0 _,_ 1] is bounded, �0 _[f]_[(] _[x]_[+] _[ht]_[)] _[ dt]_[ thus converges] 1 to �0 _[f]_[(] _[x]_[)] _[dt]_[ =] _[ f]_[(] _[x]_[),][and][the][claim][follows.] □ 

**Corollary 1.6.10** (Differentiation theorem for continuous functions) **.** _Let f_ : [ _a, b_ ] _→_ **C** _be a continuous function on a compact interval. Then we have_ 

**==> picture [132 x 26] intentionally omitted <==**

_for all x ∈_ [ _a, b_ ) _,_ 

**==> picture [132 x 26] intentionally omitted <==**

_for all x ∈_ ( _a, b_ ] _, and thus_ 

**==> picture [148 x 25] intentionally omitted <==**

_for all x ∈_ ( _a, b_ ) _._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

136 

In these notes we explore the question of the extent to which these theorems continue to hold when the differentiability or integrability conditions on the various functions _F, F[′] , f_ are relaxed. Among the results proven in these notes are 

- (i) The _Lebesgue differentiation theorem_ , which roughly speaking asserts that Corollary 1.6.10 continues to hold for _almost_ every _x_ if _f_ is merely absolutely integrable, rather than continuous; 

- (ii) A number of _differentiation theorems_ , which assert for instance that monotone, Lipschitz, or bounded variation functions in one dimension are almost everywhere differentiable; and 

- (iii) The second fundamental theorem of calculus for _absolutely continuous_ functions. 

## **1.6.1. The Lebesgue differentiation theorem in one dimen-** 

**sion.** The main objective of this section is to show 

**Theorem 1.6.11** (Lebesgue differentiation theorem, one-dimensional case) **.** _Let f_ : **R** _→_ **C** _be an absolutely integrable function, and let F_ : **R** _→_ **C** _be the definite integral F_ ( _x_ ) := �[ _−∞,x_ ] _[f]_[(] _[t]_[)] _[dt][.][Then][F] is continuous and almost everywhere differentiable, and F[′]_ ( _x_ ) = _f_ ( _x_ ) _for almost every x ∈_ **R** _._ 

This can be viewed as a variant of Corollary 1.6.10; the hypotheses are weaker because _f_ is only assumed to be absolutely integrable, rather than continuous (and can live on the entire real line, and not just on a compact interval); but the conclusion is weaker too, because _F_ is only found to be almost everywhere differentiable, rather than everywhere differentiable. (But such a relaxation of the conclusion is necessary at this level of generality; consider for instance the example when _f_ = 1[0 _,_ 1].) 

The continuity is an easy exercise: 

**Exercise 1.6.5.** Let _f_ : **R** _→_ **C** be an absolutely integrable function, and let _F_ : **R** _→_ **C** be the definite integral _F_ ( _x_ ) := �[ _−∞,x_ ] _[f]_[(] _[t]_[)] _[dt]_[.] Show that _F_ is continuous. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

137 

The main difficulty is to show that _F[′]_ ( _x_ ) = _f_ ( _x_ ) for almost every _x ∈_ **R** . This will follow from 

**Theorem 1.6.12** (Lebesgue differentiation theorem, second formulation) **.** _Let f_ : **R** _→_ **C** _be an absolutely integrable function. Then_ 

**==> picture [216 x 26] intentionally omitted <==**

_for almost every x ∈_ **R** _, and_ 

**==> picture [216 x 25] intentionally omitted <==**

_for almost every x ∈_ **R** _._ 

**Exercise 1.6.6.** Show that Theorem 1.6.11 follows from Theorem 1.6.12. 

We will just prove the first fact (1.20); the second fact (1.21) is similar (or can be deduced from (1.20) by replacing _f_ with the reflected function _x �→ f_ ( _−x_ ). 

We are taking _f_ to be complex valued, but it is clear from taking real and imaginary parts that it suffices to prove the claim when _f_ is real-valued, and we shall thus assume this for the rest of the argument. 

The conclusion (1.20) we want to prove is a convergence theorem - an assertion that for all functions _f_ in a given class (in this case, the class of absolutely integrable functions _f_ : **R** _→_ **R** ), a certain sequence of linear expressions _Thf_ (in this case, the right averages _Thf_ ( _x_ ) = _h_ 1 �[ _x,x_ + _h_ ] _[f]_[(] _[t]_[)] _[dt]_[)][converge][in][some][sense][(in][this][case,] pointwise almost everywhere) to a specified limit (in this case, _f_ ). There is a general and very useful argument to prove such convergence theorems, known as the _density argument_ . This argument requires two ingredients, which we state informally as follows: 

- (i) A verification of the convergence result for some “dense subclass” of “nice” functions _f_ , such as continuous functions, smooth functions, simple functions, etc.. By “dense”, we mean that a general function _f_ in the original class can be approximated to arbitrary accuracy in a suitable sense by a function in the nice subclass. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

138 

- (ii) A quantitative estimate that upper bounds the maximal fluctuation of the linear expressions _Thf_ in terms of the “size” of the function _f_ (where the precise definition of “size” depends on the nature of the approximation in the first ingredient). 

Once one has these two ingredients, it is usually not too hard to put them together to obtain the desired convergence theorem for general functions _f_ (not just those in the dense subclass). We illustrate this with a simple example: 

**Proposition 1.6.13** (Translation is continuous in _L_[1] ) **.** _Let f_ : **R** _[d] →_ **C** _be an absolutely integrable function, and for each h ∈_ **R** _[d] , let fh_ : **R** _[d] →_ **C** _be the shifted function_ 

**==> picture [80 x 11] intentionally omitted <==**

_Then fh converges in L_[1] _norm to f as h →_ 0 _, thus_ 

**==> picture [134 x 24] intentionally omitted <==**

**Proof.** We first verify this claim for a dense subclass of _f_ , namely the functions _f_ which are continuous and compactly supported (i.e. they vanish outside of a compact set). Such functions are continuous, and thus _fh_ converges uniformly to _f_ as _h →_ 0. Furthermore, as _f_ is compactly supported, the support of _fh − f_ stays uniformly bounded for _h_ in a bounded set. From this we see that _fh_ also converges to _f_ in _L_[1] norm as required. 

Next, we observe the quantitative estimate 

**==> picture [236 x 24] intentionally omitted <==**

for any _h ∈_ **R** _[d]_ . This follows easily from the triangle inequality 

**==> picture [240 x 24] intentionally omitted <==**

together with the translation invariance of the Lebesgue integral: 

**==> picture [136 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

139 

Now we put the two ingredients together. Let _f_ : **R** _[d] →_ **C** be absolutely integrable, and let _ε >_ 0 be arbitrary. Applying Littlewood’s second principle (Theorem 1.3.20(iii)) to the absolutely integrable function _F[′]_ , we can find a continuous, compactly supported function _g_ : **R** _[d] →_ **C** such that 

**==> picture [110 x 24] intentionally omitted <==**

Applying (1.22), we conclude that 

**==> picture [172 x 24] intentionally omitted <==**

which we rearrange as 

**==> picture [180 x 23] intentionally omitted <==**

By the dense subclass result, we also know that 

**==> picture [112 x 24] intentionally omitted <==**

for all _h_ sufficiently close to zero. From the triangle inequality, we conclude that 

**==> picture [300 x 40] intentionally omitted <==**

**Remark 1.6.14.** In the above application of the density argument, we proved the required quantitative estimate directly for all functions _f_ in the original class of functions. However, it is also possible to use the density argument a second time and initially verify the quantitative estimate just for functions _f_ in a nice subclass (e.g. continuous functions of compact support). In many cases, one can then extend that estimate to the general case by using tools such as _Fatou’s lemma_ (Corollary1.4.47), which are particularly suited for showing that upper bound estimates are preserved with respect to limits. 

**Exercise 1.6.7.** Let _f_ : **R** _[d] →_ **C** , _g_ : **R** _[d] →_ **C** be Lebesgue measurable functions such that _f_ is absolutely integrable and _g_ is essentially 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

140 

bounded (i.e. bounded outside of a null set). Show that the _convolution f ∗ g_ : **R** _[d] →_ **C** defined by the formula 

**==> picture [135 x 24] intentionally omitted <==**

is well-defined (in the sense that the integrand on the right-hand side is absolutely integrable) and that _f ∗ g_ is a bounded, continuous function. 

The above exercise is illustrative of a more general intuition, which is that convolutions tend to be _smoothing_ in nature; the convolution _f ∗ g_ of two functions is usually at least as regular as, and often more regular than, either of the two factors _f, g_ . 

This smoothing phenomenon gives rise to an important fact, namely the _Steinhaus theorem_ : 

**Exercise 1.6.8** (Steinhaus theorem) **.** Let _E ⊂_ **R** _[d]_ be a Lebesgue measurable set of positive measure. Show that the set _E − E_ := _{x − y_ : _x, y ∈ E}_ contains an open neighbourhood of the origin. ( _Hint:_ reduce to the case when _E_ is bounded, and then apply the previous exercise to the convolution 1 _E ∗_ 1 _−E_ , where _−E_ := _{−y_ : _y ∈ E}_ .) 

**Exercise 1.6.9.** A _homomorphism f_ : **R** _[d] →_ **C** is a map with the property that _f_ ( _x_ + _y_ ) = _f_ ( _x_ ) + _f_ ( _y_ ) for all _x, y ∈_ **R** _[d]_ . 

- (i) Show that all measurable homomorphisms are continuous. ( _Hint:_ for any disk _D_ centered at the origin in the complex plane, show that _f[−]_[1] ( _z_ + _D_ ) has positive measure for at least one _z ∈_ **C** , and then use the Steinhaus theorem from the previous exercise.) 

- Show that _f_ is a measurable homomorphism if and only if it takes the form _f_ ( _x_ 1 _, . . . , xd_ ) = _x_ 1 _z_ 1 + _. . ._ + _xdzd_ for all _x_ 1 _, . . . , xd ∈_ **R** and some complex coefficients _z_ 1 _, . . . , zd_ . ( _Hint:_ first establish this for rational _x_ 1 _, . . . , xd_ , and then use the previous part of this exercise.) 

- (ii) (For readers familiar with _Zorn’s lemma_ , see _§_ 2.4 of _An epsilon of room, Vol. I_ ) Show that there exist homomorphisms _f_ : **R** _[d] →_ **C** which are not of the form in the previous exercise. ( _Hint:_ view **R** _[d]_ (or **C** ) as a vector space over the 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

141 

rationals **Q** , and use the fact (from Zorn’s lemma) that every vector space - even an infinite-dimensional one - has at least one basis.) This gives an alternate construction of a non-measurable set to that given in previous notes. 

**Remark 1.6.15.** One drawback with the density argument is it gives convergence results which are _qualitative_ rather than quantitative - there is no explicit bound on the rate of convergence. For instance, in Proposition 1.6.13, we know that for any _ε >_ 0, there exists _δ >_ 0 such that � **R** _[d][ |][f][h]_[(] _[x]_[)] _[ −][f]_[(] _[x]_[)] _[|][dx][ ≤][ε]_[whenever] _[|][h][| ≤][δ]_[,][but][we][do][not] know exactly how _δ_ depends on _ε_ and _f_ . Actually, the proof does eventually give such a bound, but it depends on “how measurable” the function _f_ is, or more precisely how “easy” it is to approximate _f_ by a “nice” function. To illustrate this issue, let’s work in one dimension and consider the function _f_ ( _x_ ) := sin( _Nx_ )1[0 _,_ 2 _π_ ]( _x_ ), where _N ≥_ 1 is a large integer. On the one hand, _f_ is bounded in the _L_[1] norm uniformly in _N_ : � **R** _[|][f]_[(] _[x]_[)] _[|][dx][≤]_[2] _[π]_[(indeed,][the][left-hand] side is equal to 2). On the other hand, it is not hard to see that � **R** _[|][f][π/N]_[(] _[x]_[)] _[ −][f]_[(] _[x]_[)] _[|][dx][≥][c]_[for][some][absolute][constant] _[c][>]_[0.][Thus,] if one force � **R** _[|][f][h]_[(] _[x]_[)] _[ −][f]_[(] _[x]_[)] _[|][dx]_[to][drop][below] _[c]_[,][one][has][to][make] _[h]_ at most _π/N_ from the origin. Making _N_ large, we thus see that the rate of convergence of � **R** _[|][f][h]_[(] _[x]_[)] _[ −][f]_[(] _[x]_[)] _[|][dx]_[to][zero][can][be][arbitrarily] slow, even though _f_ is bounded in _L_[1] . The problem is that as _N_ gets large, it becomes increasingly difficult to approximate _f_ well by a “nice” function, by which we mean a uniformly continuous function with a reasonable _modulus of continuity_ , due to the increasingly oscillatory nature of _f_ . See [ **Ta2008** , _§_ 1.4] for some further discussion of this issue, and what quantitative substitutes are available for such qualitative results. 

Now we return to the Lebesgue differentiation theorem, and apply the density argument. The dense subclass result is already contained in Corollary 1.6.10, which asserts that (1.20) holds for all continuous functions _f_ . The quantitative estimate we will need is the following special case of the _Hardy-Littlewood maximal inequality_ : 

**Lemma 1.6.16** (One-sided Hardy-Littlewood maximal inequality) **.** _Let f_ : **R** _→_ **C** _be an absolutely integrable function, and let λ >_ 0 _._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

142 

_Then_ 

**==> picture [252 x 25] intentionally omitted <==**

We will prove this lemma shortly, but let us first see how this, combined with the dense subclass result, will give the Lebesgue differentiation theorem. Let _f_ : **R** _→_ **C** be absolutely integrable, and let _ε, λ >_ 0 be arbitrary. Then by Littlewood’s second principle, we can find a function _g_ : **R** _→_ **C** which is continuous and compactly supported, with 

**==> picture [106 x 24] intentionally omitted <==**

Applying the one-sided Hardy-Littlewood maximal inequality, we conclude that 

**==> picture [230 x 26] intentionally omitted <==**

In a similar spirit, from Markov’s inequality (Lemma 1.3.15) we have 

**==> picture [162 x 20] intentionally omitted <==**

By subadditivity, we conclude that for all _x ∈_ **R** outside of a set _E_ of measure at most 2 _ε/λ_ , one has both 

**==> picture [214 x 25] intentionally omitted <==**

and 

**==> picture [188 x 11] intentionally omitted <==**

for all _h >_ 0. 

Now let _x ∈_ **R** _\E_ . From the dense subclass result (Corollary 1.6.10) applied to the continuous function _g_ , we have 

**==> picture [130 x 25] intentionally omitted <==**

whenever _h_ is sufficiently close to _x_ . Combining this with (1.23), (1.24), and the triangle inequality, we conclude that 

**==> picture [136 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

143 

for all _h_ sufficiently close to zero. In particular we have 

**==> picture [168 x 26] intentionally omitted <==**

for all _x_ outside of a set of measure 2 _ε/λ_ . Keeping _λ_ fixed and sending _ε_ to zero, we conclude that 

**==> picture [168 x 25] intentionally omitted <==**

for almost every _x ∈_ **R** . If we then let _λ_ go to zero along a countable sequence (e.g. _λ_ := 1 _/n_ for _n_ = 1 _,_ 2 _, . . ._ ), we conclude that 

**==> picture [162 x 25] intentionally omitted <==**

for almost every _x ∈_ **R** , and the claim follows. 

The only remaining task is to establish the one-sided HardyLittlewood maximal inequality. We will do so by using the _rising sun lemma_ : 

**Lemma 1.6.17** (Rising sun lemma) **.** _Let_ [ _a, b_ ] _be a compact interval, and let F_ : [ _a, b_ ] _→_ **R** _be a continuous function. Then one can find an at most countable family of disjoint non-empty open intervals In_ = ( _an, bn_ ) _in_ [ _a, b_ ] _with the following properties:_ 

- (i) _For each n, either F_ ( _an_ ) = _F_ ( _bn_ ) _, or else an_ = _a and F_ ( _bn_ ) _≥ F_ ( _an_ ) _._ 

- (ii) _If x ∈_ [ _a, b_ ] _does not lie in any of the intervals In, then one must have F_ ( _y_ ) _≤ F_ ( _x_ ) _for all x ≤ y ≤ b._ 

**Remark 1.6.18.** To explain the name “rising sun lemma”, imagine the graph _{_ ( _x, F_ ( _x_ )) : _x ∈_ [ _a, b_ ] _}_ of _F_ as depicting a hilly landscape, with the sun shining horizontally from the rightward infinity (+ _∞,_ 0) (or rising from the east, if you will). Those _x_ for which _F_ ( _y_ ) _≤ F_ ( _x_ ) are the locations on the landscape which are illuminated by the sun. The intervals _In_ then represent the portions of the landscape that are in shadow. The reader is encouraged to draw a picture[14] to illustrate this perspective. 

> 14Author’s note: I have deliberately omitted including such pictures in the text, as I feel that it is far more instructive and useful for the reader to directly create a personalised visual aid for these results. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

144 

This lemma is proven using the following basic fact: 

**Exercise 1.6.10.** Show that any open subset _U_ of **R** can be written as the union of at most countably many disjoint non-empty open intervals, whose endpoints lie outside of _U_ . ( _Hint:_ first show that every _x_ in _U_ is contained in a maximal open subinterval ( _a, b_ ) of _U_ , and that these maximal open subintervals are disjoint, with each such interval containing at least one rational number.) 

**Proof.** (Proof of rising sun lemma) Let _U_ be the set of all _x ∈_ ( _a, b_ ) such that _F_ ( _y_ ) _> F_ ( _x_ ) for at least one _x < y < b_ . As _F_ is continuous, _U_ is open, and so _U_ is the union of at most countably many disjoint non-empty open intervals _In_ = ( _an, bn_ ), with the endpoints _an, bn_ lying outside of _U_ . 

The second conclusion of the rising sun lemma is clear from construction, so it suffices to establish the first. Suppose first that _In_ = ( _an, bn_ ) is such that _an_ = _a_ . As the endpoint _an_ does not lie in _U_ , we must have _F_ ( _y_ ) _≤ F_ ( _an_ ) for all _an ≤ y ≤ b_ ; similarly we have _F_ ( _y_ ) _≤ F_ ( _bn_ ) for all _bn ≤ y ≤ b_ . In particular we have _F_ ( _bn_ ) _≤ F_ ( _an_ ). By the continuity of _F_ , it will then suffice to show that _F_ ( _bn_ ) _≥ F_ ( _t_ ) for all _an < t < bn_ . 

Suppose for contradiction that there was _an < t < bn_ with _F_ ( _bn_ ) _< F_ ( _t_ ). Let _A_ := _{s ∈_ [ _t, b_ ] : _F_ ( _s_ ) _≥ F_ ( _t_ ) _}_ , then _A_ is a closed set that contains _t_ but not _b_ . Set _t∗_ := sup( _A_ ), then _t∗ ∈_ [ _t, b_ ) _⊂ In ⊂ U_ , and thus there exists _t∗ < y ≤ b_ such that _F_ ( _y_ ) _> F_ ( _t∗_ ). Since _F_ ( _t∗_ ) _≥ F_ ( _t_ ) _> F_ ( _bn_ ), and _F_ ( _bn_ ) _≥ F_ ( _z_ ) for all _bn ≤ z ≤ b_ , we see that _y_ cannot exceed _bn_ , and thus lies in _A_ , but this contradicts the fact that _t∗_ is the supremum of _A_ . 

The case when _an_ = _a_ is similar and is left to the reader; the only difference is that we can no longer assert that _F_ ( _y_ ) _≤ F_ ( _an_ ) for all _an ≤ y ≤ b_ , and so do not have the upper bound _F_ ( _bn_ ) _≤ F_ ( _an_ ). □ 

Now we can prove the one-sided Hardy-Littlewood maximal inequality. By upwards monotonicity, it will suffice to show that 

**==> picture [308 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

145 

for any compact interval [ _a, b_ ]. By modifying _λ_ by an epsilon, we may replace the non-strict inequality here with strict inequality: (1.25) 

**==> picture [308 x 26] intentionally omitted <==**

Fix [ _a, b_ ]. We apply the rising sun lemma to the function _F_ : [ _a, b_ ] _→_ **R** as 

**==> picture [148 x 25] intentionally omitted <==**

By Lemma 1.6.5, _F_ is continuous, and so we can find an at most countable sequence of intervals _In_ = ( _an, bn_ ) with the properties given by the rising sun lemma. From the second property of that lemma, we observe that 

**==> picture [260 x 26] intentionally omitted <==**

since the property _h_[1] �[ _x,x_ + _h_ ] _[|][f]_[(] _[t]_[)] _[|][ dt > λ]_[ can be rearranged as] _[ F]_[(] _[x]_[+] _h_ ) _> F_ ( _x_ ). By countable additivity, we may thus upper bound the left-hand side of (1.25) by[�] _n_[(] _[b][n][−][a][n]_[).][On][the][other][hand,][since] _F_ ( _bn_ ) _− F_ ( _an_ ) _≥_ 0, we have 

and thus 

**==> picture [148 x 66] intentionally omitted <==**

As the _In_ are disjoint intervals in _I_ , we may apply monotone convergence and monotonicity to conclude that 

**==> picture [142 x 26] intentionally omitted <==**

and the claim follows. 

**Exercise 1.6.11** (Two-sided Hardy-Littlewood maximal inequality) **.** Let _f_ : **R** _→_ **C** be an absolutely integrable function, and let _λ >_ 0. Show that 

**==> picture [234 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

146 

where the supremum ranges over all intervals _I_ of positive length that contain _x_ . 

**Exercise 1.6.12** (Rising sun inequality) **.** Let _f_ : **R** _→_ **R** be an absolutely integrable function, and let _f[∗]_ : **R** _→_ **R** be the one-sided signed Hardy-Littlewood maximal function 

**==> picture [134 x 26] intentionally omitted <==**

Establish the _rising sun inequality_ 

**==> picture [168 x 26] intentionally omitted <==**

for all real _λ_ (note here that we permit _λ_ to be zero or negative), and show that this inequality implies Lemma 1.6.16. ( _Hint:_ First do the _λ_ = 0 case, by invoking the rising sun lemma.) See [ **Ta2009** , _§_ 2.9] for some further discussion of inequalities of this type, and applications to ergodic theory (and in particular the _maximal ergodic theorem_ ). 

**Exercise 1.6.13.** Show that the left and right-hand sides in Lemma 1.6.16 are in fact equal. ( _Hint:_ one may first wish to try this in the case when _f_ has compact support, in which case one can apply the rising sun lemma to a sufficiently large interval containing the support of _f_ .) 

**1.6.2. The Lebesgue differentiation theorem in higher dimensions.** Now we extend the Lebesgue differentiation theorem to higher dimensions. Theorem 1.6.11 does not have an obvious highdimensional analogue, but Theorem 1.6.12 does: 

**Theorem 1.6.19** (Lebesgue differentiation theorem in general dimension) **.** _Let f_ : **R** _[d] →_ **C** _be an absolutely integrable function. Then for almost every x ∈_ **R** _[d] , one has_ 

**==> picture [245 x 26] intentionally omitted <==**

_and_ 

**==> picture [170 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

147 

_where B_ ( _x, r_ ) := _{y ∈_ **R** _[d]_ : _|x − y| < r} is the open ball of radius r centred at x._ 

**==> picture [321 x 68] intentionally omitted <==**

so we see that the first conclusion of Theorem 1.6.19 implies the second. A point _x_ for which (1.26) holds is called a _Lebesgue point_ of _f_ ; thus, for an absolutely integrable function _f_ , almost every point in **R** _[d]_ will be a Lebesgue point for **R** _[d]_ . 

**Exercise 1.6.14.** Call a function _f_ : **R** _[d] →_ **C** _locally integrable_ if, for every _x ∈_ **R** _[d]_ , there exists an open neighbourhood of _x_ on which _f_ is absolutely integrable. 

- (i) Show that _f_ is locally integrable if and only if � _B_ (0 _,r_ ) _[|][f]_[(] _[x]_[)] _[|][ dx <] ∞_ for all _r >_ 0. 

- (ii) Show that Theorem 1.6.19 implies a generalisation of itself in which the condition of absolute integrability of _f_ is weakened to local integrability. 

**Exercise 1.6.15.** For each _h >_ 0, let _Eh_ be a subset of _B_ (0 _, h_ ) with the property that _m_ ( _Eh_ ) _≥ cm_ ( _B_ (0 _, h_ )) for some _c >_ 0 independent of _h_ . Show that if _f_ : **R** _[d] →_ **C** is locally integrable, and _x_ is a Lebesgue point of _f_ , then 

**==> picture [150 x 25] intentionally omitted <==**

Conclude that Theorem 1.6.19 implies Theorem 1.6.12. 

To prove Theorem 1.6.19, we use the density argument. The dense subclass case is easy: 

**Exercise 1.6.16.** Show that Theorem 1.6.19 holds whenever _f_ is continuous. 

The quantitative estimate needed is the following: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

148 

**Theorem 1.6.20** (Hardy-Littlewood maximal inequality) **.** _Let f_ : **R** _[d] →_ **C** _be an absolutely integrable function, and let λ >_ 0 _. Then_ 

**==> picture [300 x 40] intentionally omitted <==**

**Remark 1.6.21.** The expression sup _r>_ 0 _m_ ( _B_ 1( _x,r_ )) � _B_ ( _x,r_ ) _[|][f]_[(] _[y]_[)] _[|][dy][≥] λ}_ is known as the _Hardy-Littlewood maximal function_ of _f_ , and is often denoted _Mf_ ( _x_ ). It is an important function in the field of (real-variable) _harmonic analysis_ . 

**Exercise 1.6.17.** Use the density argument to show that Theorem 1.6.20 implies Theorem 1.6.19. 

In the one-dimensional case, this estimate was established via the rising sun lemma. Unfortunately, that lemma relied heavily on the ordered nature of **R** , and does not have an obvious analogue in higher dimensions. Instead, we will use the following covering lemma. Given an open ball _B_ = _B_ ( _x, r_ ) in **R** _[d]_ and a real number _c >_ 0, we write _cB_ := _B_ ( _x, cr_ ) for the ball with the same centre as _B_ , but _c_ times the radius. (Note that this is slightly different from the set _c · B_ := _{cy_ : _y ∈ B}_ - why?) Note that _|cB|_ = _c[d] |B|_ for any open ball _B ⊂_ **R** _[d]_ and any _c >_ 0. 

**Lemma 1.6.22** (Vitali-type covering lemma) **.** _Let B_ 1 _, . . . , Bn be a finite collection of open balls in_ **R** _[d] (not necessarily disjoint). Then there exists a subcollection B_ 1 _[′][, . . . , B] m[′][of]_[disjoint] _[balls][in][this][collec-] tion, such that_ 

**==> picture [187 x 30] intentionally omitted <==**

_In particular, by finite subadditivity,_ 

**==> picture [114 x 30] intentionally omitted <==**

**Proof.** We use a _greedy algorithm_ argument, selecting the balls _Bi[′]_ to be as large as possible while remaining disjoint. More precisely, we run the following algorithm: 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

149 

- Step 0. Initialise _m_ = 0 (so that, initially, there are no balls _B_ 1 _[′][, . . . , B] m[′]_ in the desired collection). 

- Step 1. Consider all the balls _Bj_ that do not already intersect one of the _B_ 1 _[′][, . . . , B] m[′]_[(so,][initially,][all][of][the][balls] _[B]_[1] _[, . . . , B][n]_[will] be considered). If there are no such balls, STOP. Otherwise, go on to Step 2. 

- Step 2. Locate the largest ball _Bj_ that does not already intersect one of the _B_ 1 _[′][, . . . , B] m[′]_[.][(If][there][are][multiple][largest][balls] with exactly the same radius, break the tie arbitrarily.) Add this ball to the collection _B_ 1 _[′][, . . . , B] m[′]_[by setting] _[ B] m[′]_ +1[:=] _[ B][j]_ and then incrementing _m_ to _m_ + 1. Then return to Step 1. 

Note that at each iteration of this algorithm, the number of available balls amongst the _B_ 1 _, . . . , Bn_ drops by at least one (since each ball selected certainly intersects itself and so cannot be selected again). So this algorithm terminates in finite time. It is also clear from construction that the _B_ 1 _[′][, . . . , B] m[′]_[are][a][subcollection][of][the] _[B]_[1] _[, . . . , B][n]_ consisting of disjoint balls. So the only task remaining is to verify that (1.27) holds at the completion of the algorithm, i.e. to show that each ball _Bi_ in the original collection is covered by the triples 3 _Bj[′]_[of][the][subcollection.] 

For this, we argue as follows. Take any ball _Bi_ in the original collection. Because the algorithm only halts when there are no more balls that are disjoint from the _B_ 1 _[′][, . . . , B] m[′]_[, the ball] _[ B][i]_[must intersect] at least one of the balls _Bj[′]_[in][the][subcollection.][Let] _[B] j[′]_[be][the][first] ball with this property, thus _Bi_ is disjoint from _B_ 1 _[′][, . . . , B] j[′] −_ 1[,][but] intersects _Bj[′]_[.][Because] _[B] j[′]_[was][chosen][to][be][largest][amongst][all][balls] that did not intersect _B_ 1 _[′][, . . . , B] j[′] −_ 1[, we conclude that the radius of] _[ B][i]_ cannot exceed that of _B[′]_[From][the][triangle][inequality,][this][implies] _j_[.] that _Bi ⊂_ 3 _Bj[′]_[,][and][the][claim][follows.] □ 

**Exercise 1.6.18.** Technically speaking, the above algorithmic argument was not phrased in the standard language of formal mathematical deduction, because in that language, any mathematical object (such as the natural number _m_ ) can only be defined once, and not redefined multiple times as is done in most algorithms. Rewrite the above argument in a way that avoids redefining any variable. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

150 

( _Hint:_ introduce a “time” variable _t_ , and recursively construct families _B_ 1 _[′] ,t[, . . . , B] m[′] t,t_[of][balls][that][represent][the][outcome][of][the][above] algorithm after _t_ iterations (or _t∗_ iterations, if the algorithm halted at some previous time _t∗ < t_ ). For this particular algorithm, there are also more _ad hoc_ approaches that exploit the relatively simple nature of the algorithm to allow for a less notationally complicated construction.) More generally, it is possible to use this time parameter trick to convert any construction involving a provably terminating algorithm into a construction that does not redefine any variable. (It is however dangerous to work with any algorithm that has an infinite run time, unless one has a suitably strong convergence result for the algorithm that allows one to take limits, either in the classical sense or in the more general sense of jumping to _limit ordinals_ ; in the latter case, one needs to use _transfinite induction_ in order to ensure that the use of such algorithms is rigorous; see _§_ 2.4 of _An epsilon of room, Vol. I_ .) 

**Remark 1.6.23.** The actual _Vitali covering lemma_ [ **Vi1908** ] is slightly different to this one, but we will not need it here. Actually there is a family of related covering lemmas which are useful for a variety of tasks in harmonic analysis, see for instance [ **deG1981** ] for further discussion. 

Now we can prove the Hardy-Littlewood inequality, which we will do with the constant _Cd_ := 3 _[d]_ . It suffices to verify the claim with strict inequality, 

**==> picture [300 x 55] intentionally omitted <==**

Fix _f_ and _λ_ . By inner regularity, it suffices to show that 

**==> picture [102 x 26] intentionally omitted <==**

whenever _K_ is a compact set that is contained in 

**==> picture [210 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

151 

By construction, for every _x ∈ K_ , there exists an open ball _B_ ( _x, r_ ) such that 

**==> picture [222 x 26] intentionally omitted <==**

By compactness of _K_ , we can cover _K_ by a finite number _B_ 1 _, . . . , Bn_ of such balls. Applying the Vitali-type covering lemma, we can find a subcollection _B_ 1 _[′][, . . . , B] m[′]_[of][disjoint][balls][such][that] 

**==> picture [114 x 30] intentionally omitted <==**

By (1.28), on each ball _Bj[′]_[we][have] 

**==> picture [110 x 27] intentionally omitted <==**

summing in _j_ and using the disjointness of the _Bj[′]_[we][conclude][that] 

**==> picture [130 x 29] intentionally omitted <==**

Since the _B_ 1 _, . . . , Bn_ cover _K_ , we obtain Theorem 1.6.20 as desired. 

**Exercise 1.6.19.** Improve the constant 3 _[d]_ in the Hardy-Littlewood maximal inequality to 2 _[d]_ . ( _Hint:_ observe that with the construction used to prove the Vitali covering lemma, the _centres_ of the balls _Bi_ are contained in[�] _[m] j_ =1[2] _[B] j[′]_[and][not][just][in][�] _[m] j_ =1[3] _[B] j[′]_[.][To][exploit][this] observation one may need to first create an epsilon of room, as the centers are not by themselves sufficient to cover the required set.) 

**Remark 1.6.24.** The optimal value of _Cd_ is not known in general, although a fairly recent result of Melas[ **Me2003** ] gives the surprising conclusion that the optimal value of _C_ 1 is _C_ 1 =[11+] 12 ~~_√_~~ 61 = 1 _._ 56 _. . ._ . It is known that _Cd_ grows at most linearly in _d_ , thanks to a result of Stein and Str¨omberg[ **StSt1983** ], but it is not known if _Cd_ is bounded in _d_ or grows as _d →∞_ . 

**Exercise 1.6.20** (Dyadic maximal inequality) **.** If _f_ : **R** _[d] →_ **C** is an absolutely integrable function, establish the dyadic Hardy-Littlewood maximal inequality 

**==> picture [246 x 25] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

152 

where the supremum ranges over all dyadic cubes _Q_ that contain _x_ . ( _Hint:_ the nesting property of dyadic cubes will be useful when it comes to the covering lemma stage of the argument, much as it was in Exercise 1.1.14.) 

**Exercise 1.6.21** (Besicovich covering lemma in one dimension) **.** Let _I_ 1 _, . . . , In_ be a finite family of open intervals in **R** (not necessarily disjoint). Show that there exist a subfamily _I_ 1 _[′][, . . . , I] m[′]_[of][intervals] such that 

**==> picture [121 x 14] intentionally omitted <==**

(ii) Each point _x ∈_ **R** is contained in at most two of the _Im[′]_[.] 

( _Hint:_ First refine the family of intervals so that no interval _Ii_ is contained in the union of the the other intervals. At that point, show that it is no longer possible for a point to be contained in three of the intervals.) There is a variant of this lemma that holds in higher dimensions, known as the _Besicovitch covering lemma_ . 

**Exercise 1.6.22.** Let _µ_ be a Borel measure (i.e. a countably additive measure on the Borel _σ_ -algebra) on **R** , such that 0 _< µ_ ( _I_ ) _< ∞_ for every interval _I_ of positive length. Assume that _µ_ is _inner regular_ , in the sense that _µ_ ( _E_ ) = sup _K⊂E,_ compact _µ_ ( _K_ ) for every Borel measurable set _E_ . (As it turns out, from the theory of _Radon measures_ , all locally finite Borel measures have this property, but we will not prove this here; see _§_ 1.10 of _An epsilon of room, Vol. I_ .) Establish the Hardy-Littlewood maximal inequality 

**==> picture [272 x 24] intentionally omitted <==**

for any absolutely integrable function _f ∈ L_[1] ( _µ_ ), where the supremum ranges over all open intervals _I_ that contain _x_ . Note that this essentially generalises Exercise 1.6.11, in which _µ_ is replaced by Lebesgue measure. ( _Hint:_ Repeat the proof of the usual Hardy-Littlewood maximal inequality, but use the Besicovich covering lemma in place of the Vitali-type covering lemma. Why do we need the former lemma here instead of the latter?) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

153 

**Exercise 1.6.23** (Cousin’s theorem) **.** Prove _Cousin’s theorem_ : given any function _δ_ : [ _a, b_ ] _→_ (0 _,_ + _∞_ ) on a compact interval [ _a, b_ ] of positive length, there exists a partition _a_ = _t_ 0 _< t_ 1 _< . . . < tk_ = _b_ with _k ≥_ 1, together with real numbers _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[]][for][each][1] _[≤][j][≤][k]_[and] _tj − tj−_ 1 _≤ δ_ ( _t[∗] j_[).][(] _[Hint:]_[use][the][Heine-Borel][theorem,][which][asserts] that any open cover of [ _a, b_ ] has a finite subcover, followed by the Besicovitch covering lemma.) This theorem is useful in a variety of applications related to the second fundamental theorem of calculus, as we shall see below. The positive function _δ_ is known as a _gauge function_ . 

Now we turn to consequences of the Lebesgue differentiation theorem. Given a Lebesgue measurable set _E ⊂_ **R** _[d]_ , call a point _x ∈_ **R** _[d]_ a _point of density_ for _E_ if _[m] m_[(] _[E]_ ( _B[∩][B]_ ( _x,r_[(] _[x][,]_ )) _[r]_[))] _→_ 1 as _r →_ 0. Thus, for instance, if _E_ = [ _−_ 1 _,_ 1] _\{_ 0 _}_ , then every point in ( _−_ 1 _,_ 1) (including the boundary point 0) is a point of density for _E_ , but the endpoints _−_ 1 _,_ 1 (as well as the exterior of _E_ ) are not points of density. One can think of a point of density as being an “almost interior” point of _E_ ; it is not necessarily the case that one can fit an small ball _B_ ( _x, r_ ) centred at _x_ inside of _E_ , but one can fit _most_ of that small ball inside _E_ . 

**Exercise 1.6.24.** If _E ⊂_ **R** _[d]_ is Lebesgue measurable, show that almost every point in _E_ is a point of density for _E_ , and almost every point in the complement of _E_ is not a point of density for _E_ . 

**Exercise 1.6.25.** Let _E ⊂_ **R** _[d]_ be a measurable set of positive measure, and let _ε >_ 0. 

- (i) Using Exercise 1.6.15 and Exercise 1.6.24, show that there exists a cube _Q ⊂_ **R** _[d]_ of positive sidelength such that _m_ ( _E ∩ Q_ ) _>_ (1 _− ε_ ) _m_ ( _Q_ ). 

- (ii) Give an alternate proof of the above claim that avoids the Lebesgue differentiation theorem. ( _Hint:_ reduce to the case when _E_ is bounded, then approximate _E_ by an almost disjoint union of cubes.) 

- (iii) Use the above result to give an alternate proof of the Steinhaus theorem (Exercise 1.6.8). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

154 

Of course, one can replace cubes here by other comparable shapes, such as balls. (Indeed, a good principle to adopt in analysis is that cubes and balls are “equivalent up to constants”, in that a cube of some sidelength can be contained in a ball of comparable radius, and vice versa. This type of mental equivalence is analogous to, though not identical with, the famous dictum that a topologist cannot distinguish a doughnut from a coffee cup.) 

- **Exercise 1.6.26.** (i) Give an example of a compact set _K ⊂_ **R** of positive measure such that _m_ ( _K ∩ I_ ) _< |I|_ for every interval _I_ of positive length. ( _Hint:_ first construct an open dense subset of [0 _,_ 1] of measure strictly less than 1.) 

   - (ii) Give an example of a measurable set _E ⊂_ **R** such that 0 _< m_ ( _E ∩ I_ ) _< |I|_ for every interval _I_ of positive length. ( _Hint:_ first work in a bounded interval, such as ( _−_ 1 _,_ 2). The complement of the set _K_ in the first example is the union of at most countably many open intervals, thanks to Exercise 1.6.10. Now fill in these open intervals and iterate.) 

**Exercise 1.6.27** (Approximations to the identity) **.** Define a _good kernel_[15] to be a measurable function _P_ : **R** _[d] →_ **R**[+] which is nonnegative, radial (which means that there is a function _P_[˜] : [0 _,_ + _∞_ ) _→_ **R**[+] such that _P_ ( _x_ ) = _P_[˜] ( _|x|_ )), radially non-increasing (so that _P_[˜] is a non-increasing function), and has total mass � **R** _[d][ P]_[(] _[x]_[)] _[dx]_[equal][to][1.] The functions _Pt_ ( _x_ ) := _t_ 1 _[d][P]_[(] _[x] t_[)][for] _[t][>]_[0][are][then][said][to][be][a] _[good] family of approximations to the identity_ . 

   - (i) Show that the _heat kernels_[16] _Pt_ ( _x_ ) := (4 _πt_ 1[2] ) _[d/]_[2] _[e][−|][x][|]_[2] _[/]_[4] _[t]_[2][and] _Poisson kernels Pt_ ( _x_ ) := _cd_ ( _t_[2] + _|x|_[2] _t_ )[(] _[d]_[+1)] _[/]_[2][are][good][families] of approximations to the identity, if the constant _cd >_ 0 is chosen correctly (in fact one has _cd_ = Γ(( _d_ +1) _/_ 2) _/π_[(] _[d]_[+1)] _[/]_[2] , but you are not required to establish this). 

- 15Different texts have slightly different notions of what a good kernel is; the 

- “right” class of kernels to consider depends to some extent on what type of convergence results one is interested in (e.g. almost everywhere convergence, convergence in _L_[1] or _L[∞]_ norm, etc.), and on what hypotheses one wishes to place on the original function _f_ . 

16Note that we have modified the usual formulation of the heat kernel by replacing _t_ with _t_[2] in order to make it conform to the notational conventions used in this exercise. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

155 

(ii) Show that if _P_ is a good kernel, then 

**==> picture [115 x 28] intentionally omitted <==**

for some constants 0 _< cd < Cd_ depending only on _d_ . ( _Hint:_ compare _P_ with such “horizontal wedding cake” functions as[�] _[∞] n_ = _−∞_[1][2] _[n][−]_[1] _[<][|][x][|≤]_[2] _[n][P]_[˜][(2] _[n]_[).)] 

(iii) Establish the quantitative upper bound 

**==> picture [253 x 25] intentionally omitted <==**

for any absolutely integrable function _f_ and some constant _Cd[′][>]_[ 0][depending][only][on] _[d]_[.] 

- (iv) Show that if _f_ : **R** _[d] →_ **C** is absolutely integrable and _x_ is a Lebesgue point of _f_ , then the convolution 

**==> picture [148 x 24] intentionally omitted <==**

converges to _f_ ( _x_ ) as _t →_ 0. ( _Hint:_ split _f_ ( _y_ ) as the sum of _f_ ( _x_ ) and _f_ ( _y_ ) _− f_ ( _x_ ).) In particular, _f ∗ Pt_ converges pointwise almost everywhere to _f_ . 

**1.6.3. Almost everywhere differentiability.** As we see in undergraduate real analysis, not every continuous function _f_ : **R** _→_ **R** is differentiable, with the standard example being the absolute value function _f_ ( _x_ ) := _|x|_ , which is continuous not differentiable at the origin _x_ = 0. Of course, this function is still almost everywhere differentiable. With a bit more effort, one can construct continuous functions that are in fact _nowhere differentiable_ : 

**Exercise 1.6.28** (Weierstrass function) **.** Let _F_ : **R** _→_ **R** be the function 

**==> picture [118 x 28] intentionally omitted <==**

- (i) Show that _F_ is well-defined (in the sense that the series is absolutely convergent) and that _F_ is a bounded continuous function. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

156 

- (ii) Show that for every 8-dyadic interval [ 8 _[j][n][,][j]_ 8[+] _[n]_[1][]][with] _[n][≥]_[1,] one has _|F_ ( _[j]_ 8[+] _[n]_[1][)] _[−][F]_[(] 8 _[j][n]_[)] _[| ≥][c]_[4] _[−][n]_[for some absolute constant] _c >_ 0. 

- (iii) Show that _F_ is not differentiable at any point _x ∈_ **R** . ( _Hint:_ argue by contradiction and use the previous part of this exercise.) Note that it is _not_ enough to formally differentiate the series term by term and observe that the resulting series is divergent - why not? 

The difficulty here is that a continuous function can still contain a large amount of _oscillation_ , which can lead to breakdown of differentiability. However, if one can somehow limit the amount of oscillation present, then one can often recover a fair bit of differentiability. For instance, we have 

**Theorem 1.6.25** (Monotone differentiation theorem) **.** _Any function F_ : **R** _→_ **R** _which is monotone (either monotone non-decreasing or monotone non-increasing) is differentiable almost everywhere._ 

**Exercise 1.6.29.** Show that every monotone function is measurable. 

To prove this theorem, we just treat the case when _F_ is monotone non-decreasing, as the non-increasing case is similar (and can be deduced from the non-decreasing case by replacing _F_ with _−F_ ). 

We also first focus on the case when _F_ is continuous, as this allows us to use the rising sun lemma. To understand the differentiability of _F_ , we introduce the four _Dini derivatives_ of _F_ at _x_ : 

> [(] _[x]_[+] _[h]_[)] _[−][F]_[(] _[x]_[)] (i) The upper right derivative _D_[+] _F_ ( _x_ ) := lim sup _h→_ 0+ _[F] h_ ; (ii) The lower right derivative _D_[+] _F_ ( _x_ ) := lim inf _h→_ 0+ _[F]_[(] _[x]_[+] _[h] h_[)] _[−][F]_[(] _[x]_[)] ; 

> [(] _[x]_[+] _[h]_[)] _[−][F]_[(] _[x]_[)] (iii) The upper left derivative _D[−] F_ ( _x_ ) := lim sup _h→_ 0 _−[F] h_ ; 

> [(] _[x]_[+] _[h]_[)] _[−][F]_[(] _[x]_[)] (iv) The lower right derivative _D[−] F_ ( _x_ ) := lim inf _h→_ 0 _−[F] h_ . 

Regardless of whether _F_ is differentiable or not (or even whether _F_ is continuous or not), the four Dini derivatives always exist and take values in the extended real line [ _−∞, ∞_ ]. (If _F_ is only defined on an interval [ _a, b_ ], rather than on the endpoints, then some of the Dini 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

157 

derivatives may not exist at the endpoints, but this is a measure zero set and will not impact our analysis.) 

**Exercise 1.6.30.** If _F_ is monotone, show that the four Dini derivatives of _F_ are measurable. ( _Hint:_ the main difficulty is to reformulate the derivatives so that _h_ ranges over a countable set rather than an uncountable one.) 

A function _F_ is differentiable at _x_ precisely when the four derivatives are equal and finite: 

(1.29) _D_[+] _F_ ( _x_ ) = _D_[+] _F_ ( _x_ ) = _D[−] F_ ( _x_ ) = _D[−] F_ ( _x_ ) _∈_ ( _−∞,_ + _∞_ ) _._ We also have the trivial inequalities 

**==> picture [190 x 12] intentionally omitted <==**

If _F_ is non-decreasing, all these quantities are non-negative, thus 

**==> picture [226 x 12] intentionally omitted <==**

The one-sided Hardy-Littlewood maximal inequality has an analogue in this setting: 

**Lemma 1.6.26** (One-sided Hardy-Littlewood inequality) **.** _Let F_ : [ _a, b_ ] _→_ **R** _be a continuous monotone non-decreasing function, and let λ >_ 0 _. Then we have_ 

**==> picture [200 x 22] intentionally omitted <==**

_Similarly for the other three Dini derivatives of F ._ 

_If F is not assumed to be continuous, then we have the weaker inequality_ 

**==> picture [203 x 22] intentionally omitted <==**

_for some absolute constant C >_ 0 _._ 

**Remark 1.6.27.** Note that if one naively applies the fundamental theorems of calculus, one can _formally_ see that the first part of Lemma 1.6.26 is equivalent to Lemma 1.6.16. We cannot however use this argument rigorously because we have not established the necessary fundamental theorems of calculus to do this. Nevertheless, we can borrow the _proof_ of Lemma 1.6.16 without difficulty to use here, and this is exactly what we will do. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

158 

**Proof.** We just prove the continuous case and leave the discontinuous case as an exercise. 

It suffices to prove the claim for _D_[+] _F_ ; by reflection (replacing _F_ ( _x_ ) with _−F_ ( _−x_ ), and [ _a, b_ ] with [ _−b, −a_ ]), the same argument works for _D[−] F_ , and then this trivially implies the same inequalities for _D_[+] _F_ and _D[−] F_ . By modifying _λ_ by an epsilon, and dropping the endpoints from [ _a, b_ ] as they have measure zero, it suffices to show that 

**==> picture [199 x 22] intentionally omitted <==**

We may apply the rising sun lemma (Lemma 1.6.17) to the continuous function _G_ ( _x_ ) := _F_ ( _x_ ) _− λx_ . This gives us an at most countable family of intervals _In_ = ( _an, bn_ ) in ( _a, b_ ), such that _G_ ( _bn_ ) _≥ G_ ( _an_ ) for each _n_ , and such that _G_ ( _y_ ) _≤ G_ ( _x_ ) whenever _a ≤ x ≤ y ≤ b_ and _x_ lies outside of all of the _In_ . 

Observe that if _x ∈_ ( _a, b_ ), and _G_ ( _y_ ) _≤ G_ ( _x_ ) for all _x ≤ y ≤ b_ , then _D_[+] _F_ ( _x_ ) _≤ λ_ . Thus we see that the set _{x ∈_ ( _a, b_ ) : _D_[+] _F_ ( _x_ ) _> λ}_ is contained in the union of the _In_ , and so by countable additivity 

**==> picture [196 x 22] intentionally omitted <==**

But we can rearrange the inequality _G_ ( _bn_ ) _≤ G_ ( _an_ ) as _bn − an ≤ F_ ( _bn_ ) _−F_ ( _an_ ) _λ_ . From telescoping series and the monotone nature of _F_ we have[�] _n[F]_[(] _[b][n]_[)] _[ −][F]_[(] _[a][n]_[)] _[ ≤][F]_[(] _[b]_[)] _[ −][F]_[(] _[a]_[)][(this][is][easiest][to][prove][by] first working with a finite subcollection of the intervals ( _an, bn_ ), and then taking suprema), and the claim follows. The discontinuous case is left as an exercise. □ **Exercise 1.6.31.** Prove Lemma 1.6.26 in the discontinuous case. ( _Hint:_ the rising sun lemma is no longer available, but one can use either the Vitali-type covering lemma (which will give _C_ = 3) or the Besicovitch lemma (which will give _C_ = 2), by modifying the proof of Theorem 1.6.20. 

Sending _λ →∞_ in the above lemma (cf. Exercise 1.3.18), and then sending [ _a, b_ ] to **R** , we conclude as a corollary that all the four Dini derivatives of a continuous monotone non-decreasing function are finite almost everywhere. So to prove Theorem 1.6.25 for continuous 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

159 

monotone non-decreasing functions, it suffices to show that (1.29) holds for almost every _x_ . In view of the trivial inequalities, it suffices to show that _D_ + _F_ ( _x_ ) _≤ D−F_ ( _x_ ) and _D−F_ ( _x_ ) _≤ D_ + _F_ ( _x_ ) for almost every _x_ . We will just show the first inequality, as the second follows by replacing _F_ with its reflection _x �→−F_ ( _−x_ ). It will suffice to show that for every pair 0 _< r < R_ of real numbers, the set 

**==> picture [228 x 12] intentionally omitted <==**

is a null set, since by letting _R, r_ range over rationals with _R > r >_ 0 and taking countable unions, we would conclude that the set _{x ∈_ **R** : _D_ + _F_ ( _x_ ) _> D−F_ ( _x_ ) _}_ is a null set (recall that the Dini derivatives are all non-negative when _F_ is non-decreasing), and the claim follows. 

Clearly _E_ is a measurable set. To prove that it is null, we will establish the following estimate: 

**Lemma 1.6.28** ( _E_ has density less than one) **.** _For any interval_ [ _a, b_ ] _and any_ 0 _< r < R, one has m_ ( _Er,R ∩_ [ _a, b_ ]) _≤ R[r][|][b][ −][a][|][.]_ 

Indeed, this lemma implies that _E_ has no points of density, which by Exercise 1.6.24 forces _E_ to be a null set. 

**Proof.** We begin by applying the rising sun lemma to the function _G_ ( _x_ ) := _rx_ + _F_ ( _−x_ ) on [ _−b, −a_ ]; the large number of negative signs present here is needed in order to properly deal with the lower left Dini derivative _D−F_ . This gives an at most countable family of disjoint intervals _−In_ = ( _−bn, −an_ ) in ( _−b, −a_ ), such that _G_ ( _−an_ ) _≥ G_ ( _−bn_ ) for all _n_ , and such that _G_ ( _−x_ ) _≤ G_ ( _−y_ ) whenever _−x ≤−y ≤−a_ and _−x ∈_ ( _−b, −a_ ) lies outside of all of the _−In_ . Observe that if _x ∈_ ( _a, b_ ), and _G_ ( _−x_ ) _≤ G_ ( _−y_ ) for all _−x ≤−y ≤−a_ , then _D−F_ ( _x_ ) _≥ r_ . Thus we see that _Er,R_ is contained inside the union of the intervals _In_ = ( _an, bn_ ). On the other hand, from the first part of Lemma 1.6.26 we have 

**==> picture [162 x 23] intentionally omitted <==**

But we can rearrange the inequality _G_ ( _−an_ ) _≤ G_ ( _−bn_ ) as _F_ ( _bn_ ) _− F_ ( _an_ ) _≤ r_ ( _bn − an_ ). From countable additivity, one thus has 

**==> picture [114 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

160 

But the ( _an, bn_ ) are disjoint inside ( _a, b_ ), so from countable additivity again, we have[�] _n[b][n][ −][a][n][≤][b][ −][a]_[,][and][the][claim][follows.] □ 

**Remark 1.6.29.** Note if _F_ was not assumed to be continuous, then one would lose a factor of _C_ here from the second part of Lemma 1.6.26, and one would then be unable to prevent _D_[+] _F_ from being up to _C_ times as large as _D−F_ . So sometimes, even when all one is seeking is a qualitative result such as differentiability, it is still important to keep track of constants. (But this is the exception rather than the rule: for a large portion of arguments in analysis, the constants are not terribly important.) 

This concludes the proof of Theorem 1.6.25 in the continuous monotone non-decreasing case. Now we work on removing the continuity hypothesis (which was needed in order to make the rising sun lemma work properly). If we naively try to run the density argument as we did in previous sections, then (for once) the argument does _not_ work very well, as the space of continuous monotone functions are not sufficiently dense in the space of all monotone functions in the relevant sense (which, in this case, is in the _total variation_ sense, which is what is needed to invoke such tools as Lemma 1.6.26.). To bridge this gap, we have to supplement the continuous monotone functions with another class of monotone functions, known as the _jump functions_ . 

**Definition 1.6.30** (Jump function) **.** A _basic jump function J_ is a function of the form 

**==> picture [124 x 37] intentionally omitted <==**

for some real numbers _x_ 0 _∈_ **R** and 0 _≤ θ ≤_ 1; we call _x_ 0 the _point of discontinuity_ for _J_ and _θ_ the _fraction_ . Observe that such functions are monotone non-decreasing, but have a discontinuity at one point. A _jump function_ is any absolutely convergent combination of basic jump functions, i.e. a function of the form _F_ =[�] _n[c][n][J][n]_[,][where] _[n]_ ranges over an at most countable set, each _Jn_ is a basic jump function, and the _cn_ are positivereals with[�] _n[c][n][<][ ∞]_[.][If there are only finitely] many _n_ involved, we say that _F_ is a _piecewise constant jump function_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

161 

Thus, for instance, if _q_ 1 _, q_ 2 _, q_ 3 _, . . ._ is any enumeration of the rationals, then[�] _[∞] n_ =1[2] _[−][n]_[1][[] _[q] n[,]_[+] _[∞]_[)][is][a][jump][function.] 

Clearly, all jump functions are monotone non-decreasing. From the absolute convergence of the _cn_ we see that every jump function is the uniform limit of piecewise constant jump functions, for instance � _∞n_ =1 _[c][n][J][n]_[is][the][uniform][limit][of][�] _[N] n_ =1 _[c][n][J][n]_[.][One][consequence][of] this is that the points of discontinuity of a jump function[�] _[∞] n_ =1 _[c][n][J][n]_ are precisely those of the individual summands _cnJn_ , i.e. of the points _xn_ where each _Jn_ jumps. 

The key fact is that these functions, together with the continuous monotone functions, essentially generate all monotone functions, at least in the bounded case: 

**Lemma 1.6.31** (Continuous-singular decomposition for monotone functions) **.** _Let F_ : **R** _→_ **R** _be a monotone non-decreasing function._ 

- (i) _The only discontinuities of F are jump discontinuities. More precisely, if x is a point where F is discontinuous, then the limits_ lim _y→x− F_ ( _y_ ) _and_ lim _y→x_ + _F_ ( _y_ ) _both exist, but are unequal, with_ lim _y→x− F_ ( _y_ ) _<_ lim _y→x_ + _F_ ( _y_ ) _._ 

- (ii) _There are at most countably many discontinuities of F ._ 

- (iii) _If F is bounded, then F can be expressed as the sum of a continuous monotone non-decreasing function Fc and a jump function Fpp._ 

**Remark 1.6.32.** This decomposition is part of the more general _Lebesgue decomposition_ , discussed in _§_ 1.2 of _An epsilon of room, Vol. I_ . 

**Proof.** By monotonicity, the limits _F−_ ( _x_ ) := lim _y→x− F_ ( _y_ ) and _F_[+] ( _x_ ) := lim _y→x_ + _F_ ( _y_ ) always exist, with _F−_ ( _x_ ) _≤ F_ ( _x_ ) _≤ F_ +( _x_ ) for all _x_ . This gives (i). 

By (i), whenever there is a discontinuity _x_ of _F_ , there is at least one rational number _qx_ strictly between _F−_ ( _x_ ) and _F_ +( _x_ ), and from monotonicity, each rational number can be assigned to at most one discontinuity. This gives (ii). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

162 

Now we prove (iii). Let _A_ be the set of discontinuities of _F_ , thus _A_ is at most countable. For each _x ∈ A_ , we define the jump _F_ ( _x_ ) _−F−_ ( _x_ ) _cx_ := _F_ +( _x_ ) _− F−_ ( _x_ ) _>_ 0, and the fraction _θx_ := _F_ +( _x_ ) _−F−_ ( _x_ ) _[∈]_[[0] _[,]_[ 1].] Thus 

**==> picture [206 x 11] intentionally omitted <==**

Note that _cx_ is the measure of the interval ( _F−_ ( _x_ ) _, F_ +( _x_ )). By monotonicity, these intervals are disjoint; by the boundedness of _F_ , their union is bounded. By countable additivity, we thus have[�] _x∈A[c][x][<] ∞_ , and so if we let _Jx_ be the basic jump function with point of discontinuity _x_ and fraction _θx_ , then the function 

**==> picture [69 x 23] intentionally omitted <==**

is a jump function. 

As discussed previously, _G_ is discontinuous only at _A_ , and for each _x ∈ A_ one easily checks that 

**==> picture [260 x 11] intentionally omitted <==**

where ( _Fpp_ ) _−_ ( _x_ ) := lim _y→x− Fpp_ ( _y_ ), and ( _Fpp_ )+( _x_ ) := lim _y→x_ + _Fpp_ ( _y_ ). We thus see that the difference _Fc_ := _F − Fpp_ is continuous. The only remaining task is to verify that _Fc_ is monotone non-decreasing, thus we need 

**==> picture [134 x 11] intentionally omitted <==**

for all _a < b_ . But the left-hand side can be rewritten as[�] _x∈A∩_ [ _a,b_ ] _[c][x]_[.] As each _cx_ is the measure of the interval ( _F−_ ( _x_ ) _, F_ +( _x_ )), and these intervals for _x ∈ A ∩_ [ _a, b_ ] are disjoint and lie in ( _F_ ( _a_ ) _, F_ ( _b_ )), the claim follows from countable additivity. □ 

**Exercise 1.6.32.** Show that the decomposition of a bounded monotone non-decreasing function _F_ into continuous _Fc_ and jump components _Fpp_ given by the above lemma is unique. 

**Exercise 1.6.33.** Find a suitable generalisation of the notion of a jump function that allows one to extend the above decomposition to unbounded monotone functions, and then prove this extension. ( _Hint:_ the notion to shoot for here is that of a “locally jump function”.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

163 

Now we can finish the proof of Theorem 1.6.25. As noted previously, it suffices to prove the claim for monotone non-decreasing functions. As differentiability is a local condition, we can easily reduce to the case of _bounded_ monotone non-decreasing functions, since to test differentiability of a monotone non-decreasing function _F_ in any compact interval [ _a, b_ ] we may replace _F_ by the bounded monotone non-decreasing function max(min( _F, F_ ( _b_ )) _, F_ ( _a_ )) with no change in the differentiability in [ _a, b_ ] (except perhaps at the endpoints _a, b_ , but these form a set of measure zero). As we have already proven the claim for continuous functions, it suffices by Lemma 1.6.31 (and linearity of the derivative) to verify the claim for jump functions. 

Now, finally, we are able to use the density argument, using the piecewise constant jump functions as the dense subclass, and using the second part of Lemma 1.6.26 for the quantitative estimate; fortunately for us, the density argument does not particularly care that there is a loss of a constant factor in this estimate. 

For piecewise constant jump functions, the claim is clear (indeed, the derivative exists and is zero outside of finitely many discontinuities). Now we run the density argument. Let _F_ be a bounded jump function, and let _ε >_ 0 and _λ >_ 0 be arbitrary. As every jump function is the uniform limit of piecewise constant jump functions, we can find a piecewise constant jump function _Fε_ such that _|F_ ( _x_ ) _− Fε_ ( _x_ ) _| ≤ ε_ for all _x_ . Indeed, by taking _Fε_ to be a partial sum of the basic jump functions that make up _F_ , we can ensure that _F − Fε_ is also a monotone non-decreasing function. Applying the second part of Lemma 1.6.26, we have 

**==> picture [163 x 22] intentionally omitted <==**

for some absolute constant _C_ , and similarly for the other four Dini derivatives. Thus, outside of a set of measure at most 8 _Cε/λ_ , all of the Dini derivatives of _F − Fε_ are less than _λ_ . Since _Fε[′]_[is][almost] everywhere differentiable, we conclude that outside of a set of measure at most 8 _Cε/λ_ , all the Dini derivatives of _F_ ( _x_ ) lie within _λ_ of _Fε[′]_[(] _[x]_[),] and in particular are finite and lie within 2 _λ_ of each other. Sending _ε_ to zero (holding _λ_ fixed), we conclude that for almost every _x_ , the Dini derivatives of _F_ are and lie within 2 _λ_ of each other. If 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

164 

we then send _λ_ to zero, we see that for almost every _x_ , the Dini derivatives of _F_ agree with each other and are finite, and the claim follows. This concludes the proof of Theorem 1.6.25. 

Just as the integration theory of unsigned functions can be used to develop the integration theory of the absolutely convergent functions (see Section 1.3.4), the differentiation theory of monotone functions can be used to develop a parallel differentiation theory for the class of functions of _bounded variation_ : 

**Definition 1.6.33** (Bounded variation) **.** Let _F_ : **R** _→_ **R** be a function. The _total variation ∥F ∥T V_ ( **R** ) (or _∥F ∥T V_ for short) of _F_ is defined to be the supremum 

**==> picture [192 x 28] intentionally omitted <==**

where the supremum ranges over all finite increasing sequences _x_ 0 _, . . . , xn_ of real numbers with _n ≥_ 0; this is a quantity in [0 _,_ + _∞_ ]. We say that _F_ has _bounded variation_ (on **R** ) if _∥F ∥T V_ ( **R** ) is finite. (In this case, _∥F ∥T V_ ( **R** ) is often written as _∥F ∥BV_ ( **R** ) or just _∥F ∥BV_ .) 

Given any interval [ _a, b_ ], we define the total variation _∥F ∥T V_ ([ _a,b_ ]) of _F_ on [ _a, b_ ] as 

**==> picture [224 x 29] intentionally omitted <==**

thus the definition is the same, but the points _x_ 0 _, . . . , xn_ are restricted to lie in [ _a, b_ ]. Thus for instance _∥F ∥T V_ ( **R** ) = sup _N →∞ ∥F ∥T V_ ([ _−N,N_ ]). We say that a function _F_ has _bounded variation_ on [ _a, b_ ] if _∥F ∥BV_ ([ _a,b_ ]) is 

**Exercise 1.6.34.** If _F_ : **R** _→_ **R** is a monotone function, show that _∥F ∥T V_ ([ _a,b_ ]) = _|F_ ( _b_ ) _− F_ ( _a_ ) _|_ for any interval [ _a, b_ ], and that _F_ has bounded variation on **R** if and only if it is bounded. 

**Exercise 1.6.35.** For any functions _F, G_ : **R** _→_ **R** , establish the triangle property _∥F_ + _G∥T V_ ( **R** ) _≤∥F ∥T V_ ( **R** ) + _∥G∥T V_ ( **R** ) and the homogeneity property _∥cF ∥T V_ ( **R** ) = _|c|∥F ∥T V_ ( **R** ) for any _c ∈_ **R** . Also show that _∥F ∥T V_ = 0 if and only if _F_ is constant. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

165 

**Exercise 1.6.36.** If _F_ : **R** _→_ **R** is a function, show that _∥F ∥T V_ ([ _a,b_ ])+ _∥F ∥T V_ ([ _b,c_ ]) = _∥F ∥T V_ ([ _a,c_ ]) whenever _a ≤ b ≤ c_ . 

- **Exercise 1.6.37.** (i) Show that every function _f_ : **R** _→_ **R** of bounded variation is bounded, and that the limits lim _x→_ + _∞ f_ ( _x_ ) and lim _x→−∞ f_ ( _x_ ), are well-defined. 

   - (ii) Give a counterexample of a bounded, continuous, compactly supported function _f_ that is not of bounded variation. 

**Exercise 1.6.38.** Let _f_ : **R** _→_ **R** be an absolutely integrable function, and let _F_ : **R** _→_ **R** be the indefinite integral _F_ ( _x_ ) := �[ _−∞,x_ ] _[f]_[(] _[x]_[).] Show that _F_ is of bounded variation, and that _∥F ∥T V_ ( **R** ) = _∥f ∥L_ 1( **R** ). ( _Hint:_ the upper bound _∥F ∥T V_ ( **R** ) _≤∥f ∥L_ 1( **R** ) is relatively easy to establish. To obtain the lower bound, use the density argument.) 

Much as an absolutely integrable function can be expressed as the difference of its positive and negative parts, a bounded variation function can be expressed as the difference of two bounded monotone functions: 

**Proposition 1.6.34.** _A function F_ : **R** _→_ **R** _is of bounded variation if and only if it is the difference of two bounded monotone functions._ 

**Proof.** It is clear from Exercises 1.6.34, 1.6.35 that the difference of two bounded monotone functions is bounded. Now define the _positive variation F_[+] : **R** _→_ **R** of _F_ by the formula 

**==> picture [273 x 28] intentionally omitted <==**

It is clear from construction that this is a monotone increasing function, taking values between 0 and _∥F ∥T V_ ( **R** ), and is thus bounded. To conclude the proposition, it suffices to (by writing _F_ = _F_ + _−_ ( _F_ + _−F−_ ) to show that _F_ + _−F_ is non-decreasing, or in other words to show that 

**==> picture [136 x 12] intentionally omitted <==**

If _F_ ( _b_ ) _− F_ ( _a_ ) is negative then this is clear from the monotone nondecreasing nature of _F_[+] , so assume that _F_ ( _b_ ) _− F_ ( _a_ ) _≥_ 0. But then the claim follows because any sequence of real numbers _x_ 0 _< . . . < xn ≤ a_ can be extended by one or two elements by adding _a_ and _b_ , 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

166 

thus increasing the sum sup _x_ 0 _<...<xn_ � _ni_ =1[max(] _[F]_[(] _[x][i]_[)] _[ −][F]_[(] _[x][i]_[+1][)] _[,]_[ 0)] by at least _F_ ( _b_ ) _− F_ ( _a_ ). □ 

**Exercise 1.6.39.** Let _F_ : **R** _→_ **R** be of bounded variation. Define the positive variation _F_[+] by (1.30), and the negative variation _F[−]_ by 

**==> picture [228 x 29] intentionally omitted <==**

Establish the identities 

**==> picture [206 x 34] intentionally omitted <==**

and 

**==> picture [136 x 11] intentionally omitted <==**

for every interval [ _a, b_ ], where _F_ ( _−∞_ ) := lim _x→−∞ F_ ( _x_ ), _F_[+] (+ _∞_ ) := lim _x→_ + _∞ F_[+] ( _x_ ), and _F[−]_ (+ _∞_ ) := lim _x→_ + _∞ F[−]_ ( _x_ ). ( _Hint:_ The main difficulty comes from the fact that a partition _x_ 0 _< . . . < xn ≤ x_ that is good for _F_[+] need not be good for _F[−]_ , and vice versa. However, this can be fixed by taking a good partition for _F_[+] and a good partition for _F[−]_ and combining them together into a common refinement.) 

From Proposition 1.6.34 and Theorem 1.6.25 we immediately obtain 

**Corollary 1.6.35** (BV differentiation theorem) **.** _Every bounded variation function is differentiable almost everywhere._ 

**Exercise 1.6.40.** Call a function _locally of bounded variation_ if it is of bounded variation on every compact interval [ _a, b_ ]. Show that every function that is locally of bounded variation is differentiable almost everywhere. 

**Exercise 1.6.41** (Lipschitz differentiation theorem, one-dimensional case) **.** A function _f_ : **R** _→_ **R** is said to be _Lipschitz continuous_ if there exists a constant _C >_ 0 such that _|f_ ( _x_ ) _− f_ ( _y_ ) _| ≤ C|x − y|_ for all _x, y ∈_ **R** ; the smallest _C_ with this property is known as the _Lipschitz constant_ of _f_ . Show that every Lipschitz continuous function 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

167 

_F_ is locally of bounded variation, and hence differentiable almost everywhere. Furthermore, show that the derivative _F[′]_ , when it exists, is bounded in magnitude by the Lipschitz constant of _F_ . 

**Remark 1.6.36.** The same result is true in higher dimensions, and is known as the _Rademacher differentiation theorem_ , but we will defer the proof of this theorem to Section 2.2, when we have the powerful tool of the Fubini-Tonelli theorem (Corollary 1.7.23) available, that is particularly useful for deducing higher-dimensional results in analysis from lower-dimensional ones. 

**Exercise 1.6.42.** A function _f_ : **R** _→_ **R** is said to be _convex_ if one has _f_ ((1 _− t_ ) _x_ + _ty_ ) _≤_ (1 _− t_ ) _f_ ( _x_ ) + _tf_ ( _y_ ) for all _x < y_ and 0 _< t <_ 1. Show that if _f_ is convex, then it is continuous and almost everywhere differentiable, and its derivative _f[′]_ is equal almost everywhere to a monotone non-decreasing function, and so is itself almost everywhere differentiable. ( _Hint:_ Drawing the graph of _f_ , together with a number of chords and tangent lines, is likely to be very helpful in providing visual intuition.) Thus we see that in some sense, convex functions are “almost everywhere twice differentiable”. Similar claims also hold for concave functions, of course. 

**1.6.4. The second fundamental theorem of calculus.** We are now finally ready to attack the second fundamental theorem of calculus in the cases where _F_ is not assumed to be continuously differentiable. We begin with the case when _F_ : [ _a, b_ ] _→_ **R** is monotone non-decreasing. From Theorem 1.6.25 (extending _F_ to the rest of the real line if needed), this implies that _F_ is differentiable almost everywhere in [ _a, b_ ], so _F[′]_ is defined a.e.; from monotonicity we see that _F[′]_ is non-negative whenever it is defined. Also, an easy modification of Exercise 1.6.1 shows that _F[′]_ is measurable. 

One half of the second fundamental theorem is easy: 

**Proposition 1.6.37** (Upper bound for second fundamental theorem) **.** _Let F_ : [ _a, b_ ] _→_ **R** _be monotone non-decreasing (so that, as discussed above, F[′] is defined almost everywhere, is unsigned, and is measurable). Then_ 

**==> picture [130 x 26] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

168 

_In particular, F[′] is absolutely integrable._ 

**Proof.** It is convenient to extend _F_ to all of **R** by declaring _F_ ( _x_ ) := _F_ ( _b_ ) for _x > b_ and _F_ ( _x_ ) := _F_ ( _a_ ) for _x < a_ , then _F_ is now a bounded monotone function on **R** , and _F[′]_ vanishes outside of [ _a, b_ ]. As _F_ is almost everywhere differentiable, the Newton quotients 

**==> picture [125 x 25] intentionally omitted <==**

converge pointwise almost everywhere to _F[′]_ . Applying Fatou’s lemma (Corollary1.4.47), we conclude that 

**==> picture [228 x 26] intentionally omitted <==**

The right-hand side can be rearranged as 

**==> picture [210 x 26] intentionally omitted <==**

which can be rearranged further as 

**==> picture [212 x 25] intentionally omitted <==**

Since _F_ is equal to _F_ ( _b_ ) for the first integral and is at least _F_ ( _a_ ) for the second integral, this expression is at most 

**==> picture [196 x 14] intentionally omitted <==**

and the claim follows. □ 

**Exercise 1.6.43.** Show that any function of bounded variation has an (almost everywhere defined) derivative that is absolutely integrable. 

In the Lipschitz case, one can do better: 

**Exercise 1.6.44** (Second fundamental theorem for Lipschitz functions) **.** Let _F_ : [ _a, b_ ] _→_ **R** be Lipschitz continuous. Show that �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] _[ dx]_[ =] _F_ ( _b_ ) _− F_ ( _a_ ). ( _Hint:_ Argue as in the proof of Proposition 1.6.37, but use the dominated convergence theorem (Theorem 1.4.49) in place of Fatou’s lemma (Corollary1.4.47).) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

169 

**Exercise 1.6.45** (Integration by parts formula) **.** Let _F, G_ : [ _a, b_ ] _→_ **R** be Lipschitz continuous functions. Show that 

**==> picture [190 x 26] intentionally omitted <==**

**==> picture [96 x 26] intentionally omitted <==**

( _Hint:_ first show that the product of two Lipschitz continuous functions on [ _a, b_ ] is again Lipschitz continuous.) 

Now we return to the monotone case. Inspired by the Lipschitz case, one may hope to recover equality in Proposition 1.6.37 for such functions _F_ . However, there is an important obstruction to this, which is that all the variation of _F_ may be concentrated in a set of measure zero, and thus undetectable by the Lebesgue integral of _F[′]_ . This is most obvious in the case of a discontinuous monotone function, such as the (appropriately named) _Heaviside function F_ := 1[0 _,_ + _∞_ ); it is clear that _F[′]_ vanishes almost everywhere, but _F_ ( _b_ ) _− F_ ( _a_ ) is not equal to �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] _[dx]_[if] _[b]_[and] _[a]_[lie][on][opposite][sides][of][the] discontinuity at 0. In fact, the same problem arises for all jump functions: 

**Exercise 1.6.46.** Show that if _F_ is a jump function, then _F[′]_ vanishes almost everywhere. ( _Hint:_ use the density argument, starting from piecewise constant jump functions and using Proposition 1.6.37 as the quantitative estimate.) 

One may hope that jump functions - in which all the fluctuation is concentrated in a countable set - are the only obstruction to the second fundamental theorem of calculus holding for monotone functions, and that as long as one restricts attention to _continuous_ monotone functions, that one can recover the second fundamental theorem. However, this is still not true, because it is possible for all the fluctuation to now be concentrated, not in a countable collection of jump discontinuities, but instead in an uncountable set of zero measure, such as the middle thirds Cantor set (Exercise 1.2.9). This can be illustrated by the key counterexample of the _Cantor function_ , also known as the _Devil’s staircase function_ . The construction of this function is detailed in the exercise below. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

170 

**Exercise 1.6.47** (Cantor function) **.** Define the functions _F_ 0 _, F_ 1 _, F_ 2 _, . . ._ : [0 _,_ 1] _→_ **R** recursively as follows: 

1. Set _F_ 0( _x_ ) := _x_ for all _x ∈_ [0 _,_ 1]. 

2. For each _n_ = 1 _,_ 2 _, . . ._ in turn, define 

**==> picture [224 x 39] intentionally omitted <==**

- (i) Graph _F_ 0, _F_ 1, _F_ 2, and _F_ 3 (preferably on a single graph). 

- (ii) Show that for each _n_ = 0 _,_ 1 _, . . ._ , _Fn_ is a continuous monotone non-decreasing function with _Fn_ (0) = 0 and _Fn_ (1) = 1. ( _Hint:_ induct on _n_ .) 

- (iii) Show that for each _n_ = 0 _,_ 1 _, . . ._ , one has _|Fn_ +1( _x_ ) _−Fn_ ( _x_ ) _| ≤_ 2 _[−][n]_ for each _x ∈_ [0 _,_ 1]. Conclude that the _Fn_ converge uniformly to a limit _F_ : [0 _,_ 1] _→_ **R** . This limit is known as the _Cantor function_ . 

- (iv) Show that the Cantor function _F_ is continuous and monotone non-decreasing, with _F_ (0) = 0 and _F_ (1) = 1. 

- (v) Show that if _x ∈_ [0 _,_ 1] lies outside the middle thirds Cantor set (Exercise 1.2.9), then _F_ is constant in a neighbourhood of _x_ , and in particular _F[′]_ ( _x_ ) = 0. Conclude that �[0 _,_ 1] _[F][ ′]_[(] _[x]_[)] _[dx]_[=][0][=][1][=] _[F]_[(1)] _[ −][F]_[(0),][so][that][the][second] fundamental theorem of calculus fails for this function. 

- (vi) Show that _F_ ([�] _[∞] n_ =1 _[a][n]_[3] _[−][n]_[)][=][�] _[∞] n_ =1 _a_ 2 _n_[2] _[−][n]_[for][any][digits] _a_ 1 _, a_ 2 _, . . . ∈{_ 0 _,_ 2 _}_ . Thus the Cantor function, in some sense, converts base three expansions to base two expansions. 

- (1) Let _I_ = [[�] _[n] i_ =1 _a_ 3 _[i] i[,]_[ �] _[n] i_ =1 _a_ 3 _[i] i_[+] 3[1] _[n]_[] be one of the intervals used] in the _n[th]_ cover _In_ of _C_ (see Exercise 1.2.9), thus _n ≥_ 0 and _a_ 1 _, . . . , an ∈{_ 0 _,_ 2 _}_ . Show that _I_ is an interval of length 3 _[−][n]_ , but _F_ ( _I_ ) is an interval of length 2 _[−][n]_ . 

- (2) Show that _F_ is not differentiable at any element of the Cantor set _C_ . 

**Remark 1.6.38.** This example shows that the classical derivative _F_ ( _x_ + _h_ ) _−F_ ( _x_ ) _F[′]_ ( _x_ ) := lim _h→_ 0; _h_ =0 _h_ of a function has some defects; it cannot “see” some of the variation of a continuous monotone function 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

171 

such as the Cantor function. In _§_ 1.13 of _An epsilon of room, Vol. I_ , this will be rectified by introducing the concept of the _weak derivative_ of a function, which despite the name, is more able than the strong derivative to detect this type of singular variation behaviour. (We will also encounter in Section 1.7.3 the _Lebesgue-Stieltjes integral_ , which is another (closely related) way to capture all of the variation of a monotone function, and which is related to the classical derivative via the _Lebesgue-Radon-Nikodym theorem_ , see _§_ 1.2 of _An epsilon of room, Vol. I_ .) 

In view of this counterexample, we see that we need to add an additional hypothesis to the continuous monotone non-increasing function _F_ before we can recover the second fundamental theorem. One such hypothesis is _absolute continuity_ . To motivate this definition, let us recall two existing definitions: 

- (i) A function _F_ : **R** _→_ **R** is _continuous_ if, for every _ε >_ 0 and _x_ 0 _∈_ **R** , there exists a _δ >_ 0 such that _|F_ ( _b_ ) _− F_ ( _a_ ) _| ≤ ε_ whenever ( _a, b_ ) is an interval of length at most _δ_ that contains _x_ 0. 

- (ii) A function _F_ : **R** _→_ **R** is _uniformly continuous_ if, for every _ε >_ 0, there exists a _δ >_ 0 such that _|F_ ( _b_ ) _− F_ ( _a_ ) _| ≤ ε_ whenever ( _a, b_ ) is an interval of length at most _δ_ . 

**Definition 1.6.39.** A function _F_ : **R** _→_ **R** is said to be _absolutely continuous_ if, for every _ε >_ 0, there exists a _δ >_ 0 such that[�] _[n] j_ =1 _[|][F]_[(] _[b][j]_[)] _[−] F_ ( _aj_ ) _| ≤ ε_ whenever ( _a_ 1 _, b_ 1) _, . . . ,_ ( _an, bn_ ) is a finite collection of disjoint intervals of total length[�] _[n] j_ =1 _[b][j][−][a][j]_[at][most] _[δ]_[.] 

We define absolute continuity for a function _F_ : [ _a, b_ ] _→_ **R** defined on an interval [ _a, b_ ] similarly, with the only difference being that the intervals [ _aj, bj_ ] are of course now required to lie in the domain [ _a, b_ ] of _F_ . 

The following exercise places absolute continuity in relation to other regularity properties: 

**Exercise 1.6.48.** (i) Show that every absolutely continuous function is uniformly continuous and therefore continuous. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

172 

   - (ii) Show that every absolutely continuous function is of bounded variation on every compact interval [ _a, b_ ]. ( _Hint:_ first show this is true for any sufficiently small interval.) In particular (by Exercise 1.6.40), absolutely continuous functions are differentiable almost everywhere. 

   - (iii) Show that every Lipschitz continuous function is absolutely continuous. 

   - (iv) Show that the function _x �→[√] x_ is absolutely continuous, but not Lipschitz continuous, on the interval [0 _,_ 1]. 

   - (v) Show that the Cantor function from Exercise 1.6.47 is continuous, monotone, and uniformly continuous, but _not_ absolutely continuous, on [0 _,_ 1]. 

   - (vi) If _f_ : **R** _→_ **R** is absolutely integrable, show that the indefinite integral _F_ ( _x_ ) := �[ _−∞,x_ ] _[f]_[(] _[y]_[)] _[dy]_[is][absolutely][contin-] uous, and that _F_ is differentiable almost everywhere with _F[′]_ ( _x_ ) = _f_ ( _x_ ) for almost every _x_ . 

   - (vii) Show that the sum or product of two absolutely continuous functions on an interval [ _a, b_ ] remains absolutely continuous. What happens if we work on **R** instead of on [ _a, b_ ]? 

- **Exercise 1.6.49.** (i) Show that absolutely continuous functions map null sets to null sets, i.e. if _F_ : **R** _→_ **R** is absolutely continuous and _E_ is a null set then _F_ ( _E_ ) := _{F_ ( _x_ ): _x ∈ E}_ is also a null set. 

   - (ii) Show that the Cantor function does _not_ have this property. 

For absolutely continuous functions, we can recover the second fundamental theorem of calculus: 

**Theorem 1.6.40** (Second fundamental theorem for absolutely continuous functions) **.** _Let F_ : [ _a, b_ ] _→_ **R** _be absolutely continuous. Then[dx]_[ =] _[ F]_[(] _[b]_[)] _[ −][F]_[(] _[a]_[)] _[.]_ �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] 

**Proof.** Our main tool here will be _Cousin’s theorem_ (Exercise 1.6.23). 

By Exercise 1.6.43, _F[′]_ is absolutely integrable. By Exercise 1.5.10, _F[′]_ is thus uniformly integrable. Now let _ε >_ 0. By Exercise 1.5.13, we can find _κ >_ 0 such that � _U[|][F][ ′]_[(] _[x]_[)] _[|][ dx][ ≤][ε]_[ whenever] _[ U][⊂]_[[] _[a, b]_[] is a] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

173 

measurable set of measure at most _κ_ . (Here we adopt the convention that _F[′]_ vanishes outside of [ _a, b_ ].) By making _κ_ small enough, we may also assume from absolute continuity that[�] _[n] j_ =1 _[|][F]_[(] _[b][j]_[)] _[ −][F]_[(] _[a][j]_[)] _[|][≤][ε]_ whenever ( _a_ 1 _, b_ 1) _, . . . ,_ ( _an, bn_ ) is a finite collection of disjoint intervals of total length[�] _[n] j_ =1 _[b][j][−][a][j]_[at][most] _[κ]_[.] 

Let _E ⊂_ [ _a, b_ ] be the set of points _x_ where _F_ is not differentiable, together with the endpoints _a, b_ , as well as the points where _x_ is not a Lebesgue point of _F[′]_ . thus _E_ is a null set. By outer regularity (or the definition of outer measure) we can find an open set _U_ containing _E_ of measure _m_ ( _U_ ) _< κ_ . In particular, � _U[|][F][ ′]_[(] _[x]_[)] _[|][dx][ ≤][ε]_[.] 

Now define a gauge function _δ_ : [ _a, b_ ] _→_ (0 _,_ + _∞_ ) as follows. 

- (i) If _x ∈ E_ , we define _δ_ ( _x_ ) _>_ 0 to be small enough that the open interval ( _x − δ_ ( _x_ ) _, x_ + _δ_ ( _x_ )) lies in _U_ . 

- (ii) If _x ̸∈ E_ , then _F_ is differentiable at _x_ and _x_ is a Lebesgue point of _F[′]_ . We let _δ_ ( _x_ ) _>_ 0 be small enough that _|F_ ( _y_ ) _− F_ ( _x_ ) _−_ ( _y−x_ ) _F[′]_ ( _x_ ) _| ≤ ε|y−x|_ holds whenever _|y−x| ≤ δ_ ( _x_ ), and such that _| |I_[1] _|_ � _I[F][ ′]_[(] _[y]_[)] _[dy][ −][F][ ′]_[(] _[x]_[)] _[| ≤][ε]_[whenever] _[I]_[is][an] interval containing _x_ of length at most _δ_ ( _x_ ); such a _δ_ ( _x_ ) exists by the definition of differentiability, and of Lebesgue point. We rewrite these properties using _big-O notation_[17] as _F_ ( _y_ ) _− F_ ( _x_ ) = ( _y − x_ ) _F[′]_ ( _x_ ) + _O_ ( _ε|y − x|_ ) and � _I[F][ ′]_[(] _[y]_[)] _[ dy]_[=] _|I|F[′]_ ( _x_ ) + _O_ ( _ε|I|_ ). 

Applying Cousin’s theorem, we can find a partition _a_ = _t_ 0 _< t_ 1 _< . . . < tk_ = _b_ with _k ≥_ 1, together with real numbers _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[]][for] each 1 _≤ j ≤ k_ and _tj − tj−_ 1 _≤ δ_ ( _t[∗] j_[).] 

We can express _F_ ( _b_ ) _− F_ ( _a_ ) as a telescoping series 

**==> picture [154 x 31] intentionally omitted <==**

To estimate the size of this sum, let us first consider those _j_ for which _t[∗] j[∈][E]_[.][Then,][by][construction,][the][intervals][(] _[t][j][−]_[1] _[, t][j]_[)][are][disjoint][in] 

> 17In this notation, we use _O_ ( _X_ ) to denote a quantity _Y_ whose magnitude _|Y |_ is at most _CX_ for some absolute constant _C_ . This notation is convenient for managing error terms when it is not important to keep track of the exact value of constants such as _C_ , due to such rules as _O_ ( _X_ ) + _O_ ( _X_ ) = _O_ ( _X_ ). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

174 

_U_ . By construction of _κ_ , we thus have 

and thus 

**==> picture [132 x 69] intentionally omitted <==**

Next, we consider those _j_ for which _t[∗] j[̸∈][E]_[.][By][construction,][for] those _j_ we have 

**==> picture [202 x 13] intentionally omitted <==**

and 

**==> picture [232 x 13] intentionally omitted <==**

and thus 

**==> picture [234 x 13] intentionally omitted <==**

On the other hand, from construction again we have 

**==> picture [236 x 70] intentionally omitted <==**

and thus 

Summing in _j_ , we conclude that 

**==> picture [224 x 30] intentionally omitted <==**

where _S_ is the union of all the [ _tj−_ 1 _, tj_ ] with _t[∗] j[̸∈][E]_[.] By construction, this set is contained in [ _a, b_ ] and contains [ _a, b_ ] _\U_ . Since � _U[|][F][ ′]_[(] _[x]_[)] _[|][dx][ ≤][ε]_[,][we][conclude][that] 

**==> picture [160 x 26] intentionally omitted <==**

Putting everything together, we conclude that 

**==> picture [300 x 41] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

175 

Combining this result with Exercise 1.6.48, we obtain a satisfactory classification of the absolutely continuous functions: 

**Exercise 1.6.50.** Show that a function _F_ : [ _a, b_ ] _→_ **R** is absolutely continuous if and only if it takes the form _F_ ( _x_ ) = �[ _a,x_ ] _[f]_[(] _[y]_[)] _[dy]_[ +] _[ C]_ for some absolutely integrable _f_ : [ _a, b_ ] _→_ **R** and a constant _C_ . 

**Exercise 1.6.51** (Compatibility of the strong and weak derivatives in the absolutely continuous case) **.** Let _F_ : [ _a, b_ ] _→_ **R** be an absolutely continuous function, and let _φ_ : [ _a, b_ ] _→_ **R** be a continuously differentiable function supported in a compact subset of ( _a, b_ ). Show that �[ _a,b_ ] _[F][ ′][φ]_[(] _[x]_[)] _[dx]_[ =] _[ −]_ �[ _a,b_ ] _[Fφ][′]_[(] _[x]_[)] _[dx]_[.] 

Inspecting the proof of Theorem 1.6.40, we see that the absolute continuity was used primarily in two ways: firstly, to ensure the almost everywhere existence, and to control an exceptional null set _E_ . It turns out that one can achieve the latter control by making a different hypothesis, namely that the function _F_ is _everywhere_ differentiable rather than merely almost everywhere differentiable. More precisely, we have 

**Proposition 1.6.41** (Second fundamental theorem of calculus, again) **.** _Let_ [ _a, b_ ] _be a compact interval of positive length, let F_ : [ _a, b_ ] _→_ **R** _be a differentiable function, such that F[′] is absolutely integrable. Then the Lebesgue integral_ �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] _[dx][of][F][ ′][is][equal][to][F]_[(] _[b]_[)] _[ −][F]_[(] _[a]_[)] _[.]_ 

**Proof.** This will be similar to the proof of Theorem 1.6.40, the one main new twist being that we need several open sets _U_ instead of just one. Let _E ⊂_ [ _a, b_ ] be the set of points _x_ which are not Lebesgue points of _F[′]_ , together with the endpoints _a, b_ . This is a null set. Let _ε >_ 0, and then let _κ >_ 0 be small enough that � _U[|][F][ ′]_[(] _[x]_[)] _[|][dx][≤][ε]_ whenever _U_ is measurable with _m_ ( _U_ ) _≤ κ_ . We can also ensure that _κ ≤ ε_ . 

For every natural number _m_ = 1 _,_ 2 _, . . ._ we can find an open set _Um_ containing _E_ of measure _m_ ( _Um_ ) _≤ κ/_ 4 _[m]_ . In particular we see that _m_ ([�] _[∞] m_ =1 _[U][m]_[)] _[ ≤][κ]_[and][thus] �� _∞m_ =1 _[U][m][ |][F][ ′]_[(] _[x]_[)] _[|][dx][ ≤][ε]_[.] Now define a gauge function _δ_ : [ _a, b_ ] _→_ (0 _,_ + _∞_ ) as follows. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

176 

- (i) If _x ∈ E_ , we define _δ_ ( _x_ ) _>_ 0 to be small enough that the open interval ( _x − δ_ ( _x_ ) _, x_ + _δ_ ( _x_ )) lies in _Um_ , where _m_ is the first natural number such that _|F[′]_ ( _x_ ) _| ≤_ 2 _[m]_ , and also small enough that _|F_ ( _y_ ) _− F_ ( _x_ ) _−_ ( _y − x_ ) _F[′]_ ( _x_ ) _| ≤ ε|y − x|_ holds whenever _|y − x| ≤ δ_ ( _x_ ). (Here we crucially use the _everywhere_ differentiability to ensure that _f[′]_ ( _x_ ) exists and is finite here.) 

- (ii) If _x ̸∈ E_ , we let _δ_ ( _x_ ) _>_ 0 be small enough that _|F_ ( _y_ ) _−F_ ( _x_ ) _−_ ( _y − x_ ) _F[′]_ ( _x_ ) _| ≤ ε|y − x|_ holds whenever _|y − x| ≤ δ_ ( _x_ ), and such that _| |I_[1] _|_ � _I[F][ ′]_[(] _[y]_[)] _[dy][−][F][ ′]_[(] _[x]_[)] _[|][≤][ε]_[whenever] _[I]_[is][an] interval containing _x_ of length at most _δ_ ( _x_ ), exactly as in the proof of Theorem 1.6.40. 

Applying Cousin’s theorem, we can find a partition _a_ = _t_ 0 _< t_ 1 _< . . . < tk_ = _b_ with _k ≥_ 1, together with real numbers _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[]][for] each 1 _≤ j ≤ k_ and _tj − tj−_ 1 _≤ δ_ ( _t[∗] j_[).] 

As before, we express _F_ ( _b_ ) _− F_ ( _a_ ) as a telescoping series 

**==> picture [154 x 31] intentionally omitted <==**

For the contributions of those _j_ with _t[∗] j[̸∈][E]_[,][we][argue][exactly][as][in] the proof of Theorem 1.6.40 to conclude eventually that 

**==> picture [224 x 30] intentionally omitted <==**

where _S_ is the union of all the [ _tj−_ 1 _, tj_ ] with _t[∗] j[̸∈][E]_[.][Since] 

**==> picture [194 x 77] intentionally omitted <==**

we thus have 

Now we turn to those _j_ with _t[∗] j[∈][E]_[.][By][construction,][we][have] 

**==> picture [232 x 12] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.6. theorems** 

177 

fir these intervals, and so 

**==> picture [280 x 26] intentionally omitted <==**

Next, for each _j_ we have _F[′]_ ( _t[∗] j_[)] _[≤]_[2] _[m]_[and][[] _[t][j][−]_[1] _[, t][j]_[]] _[⊂][U][m]_[for][some] natural number _m_ = 1 _,_ 2 _, . . ._ , by construction. By countable additivity, we conclude that 

**==> picture [284 x 32] intentionally omitted <==**

Putting all this together, we again have 

**==> picture [300 x 40] intentionally omitted <==**

**Remark 1.6.42.** The above proposition is yet another illustration of how the property of everywhere differentiability is significantly better than that of almost everywhere differentiability. In practice, though, the above proposition is not as useful as one might initially think, because there are very few methods that establish the everywhere differentiability of a function that do not also establish continuous differentiability (or at least Riemann integrability of the derivative), at which point one could just use Theorem 1.6.7 instead. 

**Exercise 1.6.52.** Let _F_ : [ _−_ 1 _,_ 1] _→_ **R** be the function defined by setting _F_ ( _x_ ) := _x_[2] sin( _x_[1][3][) when] _[ x]_[ is non-zero, and] _[ F]_[(0) := 0.][Show that] _F_ is everywhere differentiable, but the deriative _F[′]_ is not absolutely integrable, and so the second fundamental theorem of calculus does not apply in this case (at least if we interpret �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] _[dx]_[using] the absolutely convergent Lebesgue integral). See however the next exercise. 

**Exercise 1.6.53** (Henstock-Kurzweil integral) **.** Let [ _a, b_ ] be a compact interval of positive length. We say that a function _f_ : [ _a, b_ ] _→_ **R** is _Henstock-Kurzweil integrable_ with integral _L ∈_ **R** if for every _ε >_ 0 there exists a gauge function _δ_ : [ _a, b_ ] _→_ (0 _,_ + _∞_ ) such that one has 

**==> picture [128 x 32] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

178 

whenever _k ≥_ 1 and _a_ = _t_ 0 _< t_ 1 _< . . . < tk_ = _b_ and _t[∗]_ 1 _[, . . . , t][∗] k_[are] such that _t[∗] j[∈]_[[] _[t][j][−]_[1] _[, t][j]_[]][and] _[|][t][j][−][t][j][−]_[1] _[|][≤][δ]_[(] _[t][∗] j_[)][for][every][1] _[≤][j][≤][k]_[.] When this occurs, we call _L_ the _Henstock-Kurzweil integral_ of _f_ and write it as �[ _a,b_ ] _[f]_[(] _[x]_[)] _[dx]_[.] 

- (i) Show that if a function is Henstock-Kurzweil integrable, it has a unique Henstock-Kurzweil integral. ( _Hint:_ use Cousin’s theorem.) 

- (ii) Show that if a function is Riemann integrable, then it is Henstock-Kurzweil integrable, and the Henstock-Kurzweil _b_ 

- integral �[ _a,b_ ] _[f]_[(] _[x]_[)] _[ dx]_[ is equal to the Riemann integral] � _a[f]_[(] _[x]_[)] _[ dx]_[.] 

- (iii) Show that if a function _f_ : [ _a, b_ ] _→_ **R** is everywhere defined, everywhere finite, and is absolutely integrable, then it is Henstock-Kurzweil integrable, and the Henstock-Kurzweil integral �[ _a,b_ ] _[f]_[(] _[x]_[)] _[ dx]_[ is equal to the Lebesgue integral] �[ _a,b_ ] _[f]_[(] _[x]_[)] _[ dx]_[.] ( _Hint:_ this is a variant of the proof of Theorem 1.6.40 or Proposition 1.6.41.) 

- (iv) Show that if _F_ : [ _a, b_ ] _→_ **R** is everywhere differentiable, then _F[′]_ is Henstock-Kurzweil integrable, and the HenstockKurzweil integral �[ _a,b_ ] _[F][ ′]_[(] _[x]_[)] _[dx]_[is][equal][to] _[F]_[(] _[b]_[)] _[−][F]_[(] _[a]_[).] ( _Hint:_ this is a variant of the proof of Theorem 1.6.40 or Proposition 1.6.41.) 

- (v) Explain why the above results give an alternate proof of Exercise 1.6.4 and of Proposition 1.6.41. 

**Remark 1.6.43.** As the above exercise indicates, the HenstockKurzweil integral (also known as the _Denjoy integral_ or _Perron integral_ ) extends the Riemann integral and the absolutely convergent Lebesgue integral, at least as long as one restricts attention to functions that are defined and are finite everywhere (in contrast to the Lebesgue integral, which is willing to tolerate functions being infinite or undefined so long as this only occurs on a null set). It is the notion of integration that is most naturally associated with the fundamental theorem of calculus for everywhere differentiable functions, as seen in part 4 of the above exercise; it can also be used as a unified framework for all the proofs in this section that invoked Cousin’s theorem. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

179 

The Henstock-Kurzweil integral can also integrate some (highly oscillatory) functions that the Lebesgue integral cannot, such as the derivative _F[′]_ of the function _F_ appearing in Exercise 1.6.52. This is analogous to how conditional summation lim _N →∞_ � _Nn_ =1 _[a][n]_[can][sum] conditionally convergent series[�] _[∞] n_ =1 _[a][n]_[,][even][if][they][are][not][abso-] lutely integrable. However, much as conditional summation is not always well-behaved with respect to rearrangement, the HenstockKurzweil integral does not always react well to changes of variable; also, due to its reliance on the order structure of the real line **R** , it is difficult to extend the Henstock-Kurzweil integral to more general spaces, such as the Euclidean space **R** _[d]_ , or to abstract measure spaces. 

## **1.7. Outer measures, pre-measures, and product measures** 

In this text so far, we have focused primarily on one specific example of a countably additive measure, namely _Lebesgue measure_ . This measure was constructed from a more primitive concept of _Lebesgue outer measure_ , which in turn was constructed from the even more primitive concept of _elementary measure_ . 

It turns out that both of these constructions can be abstracted. In this section, we will give the _Carath´eodory extension theorem_ , which constructs a countably additive measure from any abstract outer measure; this generalises the construction of Lebesgue measure from Lebesgue outer measure. One can in turn construct outer measures from another concept known as a _pre-measure_ , of which elementary measure is a typical example. 

With these tools, one can start constructing many more measures, such as _Lebesgue-Stieltjes measures_ , _product measures_ , and _Hausdorff measures_ . With a little more effort, one can also establish the _Kolmogorov extension theorem_ , which allows one to construct a variety of measures on infinite-dimensional spaces, and is of particular importance in the foundations of probability theory, as it allows one to set up probability spaces associated to both discrete and continuous random processes, even if they have infinite length. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

180 

The most important result about product measure, beyond the fact that it exists, is that one can use it to evaluate iterated integrals, and to interchange their order, provided that the integrand is either unsigned or absolutely integrable. This fact is known as the _Fubini-Tonelli theorem_ , and is an absolutely indispensable tool for computing integrals, and for deducing higher-dimensional results from lower-dimensional ones. 

In this section we will however omit a very important way to construct measures, namely the _Riesz representation theorem_ , which is discussed in _§_ 1.10 of _An epsilon of room, Vol. I_ . 

## **1.7.1. Outer measures and the Carath´eodory extension the-** 

**orem.** We begin with the abstract concept of an outer measure. 

**Definition 1.7.1** (Abstract outer measure) **.** Let _X_ be a set. An _abstract outer measure_ (or _outer measure_ for short) is a map _µ[∗]_ : 2 _[X] →_ [0 _,_ + _∞_ ] that assigns an unsigned extended real number _µ[∗]_ ( _E_ ) _∈_ [0 _,_ + _∞_ ] to _every_ set _E ⊂ X_ which obeys the following axioms: 

- (i) (Empty set) _µ[∗]_ ( _∅_ ) = 0. 

- (ii) (Monotonicity) If _E ⊂ F_ , then _µ[∗]_ ( _E_ ) _≤ µ[∗]_ ( _F_ ). 

- (iii) (Countable subadditivity) If _E_ 1 _, E_ 2 _, . . . ⊂ X_ is a countable sequence of subsets of _X_ , then _µ[∗]_ ([�] _[∞] n_ =1 _[E][n]_[)] _[ ≤]_[�] _[∞] n_ =1 _[µ][∗]_[(] _[E][n]_[).] 

Outer measures are also known as _exterior measures_ . 

Thus, for instance, Lebesgue outer measure _m[∗]_ is an outer measure (see Exercise 1.2.3). On the other hand, Jordan outer measure _m[∗][,]_[(] _[J]_[)] is only finitely subadditive rather than countably subadditive and thus is not, strictly speaking, an outer measure; for this reason this concept is often referred to as _Jordan outer content_ rather than _Jordan outer measure_ . 

Note that outer measures are weaker than measures in that they are merely countably subadditive, rather than countably additive. On the other hand, they are able to measure _all_ subsets of _X_ , whereas measures can only measure a _σ_ -algebra of measurable sets. 

In Definition 1.2.2, we used Lebesgue outer measure together with the notion of an open set to define the concept of Lebesgue measurability. This definition is not available in our more abstract setting, 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

181 

as we do not necessarily have the notion of an open set. An alternative definition of measurability was put forth in Exercise 1.2.17, but this still required the notion of a box or an elementary set, which is still not available in this setting. Nevertheless, we can modify that definition to give an abstract definition of measurability: 

**Definition 1.7.2** (Carath´eodory measurability) **.** Let _µ[∗]_ be an outer measure on a set _X_ . A set _E ⊂ X_ is said to be _Carath´eodory measurable_ with respect to _µ[∗]_ if one has 

**==> picture [136 x 11] intentionally omitted <==**

for _every_ set _A ⊂ X_ . 

**Exercise 1.7.1** (Null sets are Carath´eodory measurable) **.** Suppose that _E_ is a null set for an outer measure _µ[∗]_ (i.e. _µ[∗]_ ( _E_ ) = 0). Show that _E_ is Carath´eodory measurable with respect to _µ[∗]_ . 

**Exercise 1.7.2** (Compatibility with Lebesgue measurability) **.** Show that a set _E ⊂_ **R** _[d]_ is Carath´eodory measurable with respect to Lebesgue outer measurable if and only if it is Lebesgue measurable. ( _Hint:_ one direction follows from Exercise 1.2.17. For the other direction, first verify simple cases, such as when _E_ is a box, or when _E_ or _A_ are bounded.) 

The construction of Lebesgue measure can then be abstracted as follows: 

**Theorem 1.7.3** (Carath´eodory extension theorem) **.** _Let µ[∗]_ : 2 _[X] →_ [0 _,_ + _∞_ ] _be an outer measure on a set X, let B be the collection of all subsets of X that are Carath´eodory measurable with respect to µ[∗] , and let µ_ : _B →_ [0 _,_ + _∞_ ] _be the restriction of µ[∗] to B (thus µ_ ( _E_ ) := _µ[∗]_ ( _E_ ) _whenever E ∈B). Then B is a σ-algebra, and µ is a measure._ 

**Proof.** We begin with the _σ_ -algebra property. It is easy to see that the empty set lies in _B_ , and that the complement of a set in _B_ lies in _B_ also. Next, we verify that _B_ is closed under finite unions (which will make _B_ a Boolean algebra). Let _E, F ∈B_ , and let _A ⊂ X_ be arbitrary. By definition, it suffices to show that 

(1.31) _µ[∗]_ ( _A_ ) = _µ[∗]_ ( _A ∩_ ( _E ∪ F_ )) + _µ[∗]_ ( _A\_ ( _E ∪ F_ )) _._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

182 

To simplify the notation, we partition _A_ into the four disjoint sets 

**==> picture [82 x 58] intentionally omitted <==**

(the reader may wish to draw a Venn diagram here to understand the nature of these sets). Thus (1.31) becomes 

**==> picture [295 x 11] intentionally omitted <==**

On the other hand, from the Carath´eodory measurability of _E_ , one has 

**==> picture [264 x 11] intentionally omitted <==**

and 

**==> picture [210 x 11] intentionally omitted <==**

while from the Carath´eodory measurability of _F_ one has 

**==> picture [158 x 11] intentionally omitted <==**

putting these identities together we obtain (1.32). (Note that no subtraction is employed here, and so the arguments still work when some sets have infinite outer measure.) 

Now we verify that _B_ is a _σ_ -algebra. As it is already a Boolean algebra, it suffices (see Exercise 1.7.3 below) to verify that _B_ is closed with respect to countable disjoint unions. Thus, let _E_ 1 _, E_ 2 _, . . ._ be a disjoint sequence of Carath´eodory-measurable sets, and let _A_ be arbitrary. We wish to show that 

**==> picture [184 x 28] intentionally omitted <==**

In view of subadditivity, it suffices to show that 

**==> picture [184 x 29] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

183 

For any _N ≥_ 1,[�] _[N] n_ =1 _[E][n]_[is][Carath´eodory][measurable][(as] _[B]_[is][a] Boolean algebra), and so 

**==> picture [184 x 30] intentionally omitted <==**

By monotonicity, _µ[∗]_ ( _A\_[�] _[N] n_ =1 _[E][n]_[)] _[≥][µ][∗]_[(] _[A][\]_[ �] _[∞] n_ =1 _[E][n]_[).][Taking][limits] as _N →∞_ , it thus suffices to show that 

**==> picture [174 x 30] intentionally omitted <==**

But by the Carath´eodory measurability of[�] _[N] n_ =1 _[E][n]_[,][we][have] 

**==> picture [260 x 30] intentionally omitted <==**

for any _N ≥_ 0, and thus on iteration 

**==> picture [222 x 30] intentionally omitted <==**

On the other hand, from countable subadditivity one has 

**==> picture [198 x 30] intentionally omitted <==**

and the claim follows. 

Finally, we show that _µ_ is a measure. It is clear that _µ_ ( _∅_ ) = 0, so it suffices to establish countable additivity, thus we need to show that 

**==> picture [110 x 28] intentionally omitted <==**

whenever _E_ 1 _, E_ 2 _, . . ._ are Carath´eodory-measurable and disjoint. By subadditivity it suffices to show that 

**==> picture [112 x 28] intentionally omitted <==**

By monotonicity it suffices to show that 

**==> picture [110 x 30] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

184 

for any finite _N_ . But from the Carath´eodory measurability of[�] _[N] n_ =1 _[E][n]_ one has 

**==> picture [168 x 30] intentionally omitted <==**

for any _N ≥_ 0, and the claim follows from induction. □ 

**Exercise 1.7.3.** Let _B_ be a Boolean algebra on a set _X_ . Show that _B_ is a _σ_ -algebra if and only if it is closed under countable _disjoint_ unions, which means that[�] _[∞] n_ =1 _[E][n][∈B]_[whenever] _[E]_[1] _[, E]_[2] _[, E]_[3] _[, . . .][ ∈B]_ are a countable sequence of _disjoint_ sets in _B_ . 

**Remark 1.7.4.** Note that the above theorem, combined with Exercise 1.7.2 gives a slightly alternate way to construct Lebesgue measure from Lebesgue outer measure than the construction given in Section 1.2. This is arguably a more efficient way to proceed, but is also less geometrically intuitive than the approach taken in Section 1.2. 

**Remark 1.7.5.** From Exercise 1.7.1 we see that the measure _µ_ constructed by the Carath´eodory extension theorem is automatically _complete_ (see Definition 1.4.31). 

**Remark 1.7.6.** In _§_ 1.15 of _An epsilon of room, Vol. I_ , an important example of a measure constructed by Carath´eodory’s theorem is given, namely the _d_ -dimensional _Hausdorff measure H[d]_ on **R** _[n]_ that is good for measuring the size of _d_ -dimensional subsets of **R** _[n]_ . 

**1.7.2. Pre-measures.** In previous notes, we saw that finitely additive measures, such as elementary measure or Jordan measure, could be extended to a countably additive measure, namely Lebesgue measure. It is natural to ask whether this property is true in general. In other words, given a finitely additive measure _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] on a Boolean algebra _B_ 0, is it possible to find a _σ_ -algebra _B_ refining _B_ 0, and a countably additive measure _µ_ : _B →_ [0 _,_ + _∞_ ] that extends _µ_ 0? 

There is an obvious necessary condition in order for _µ_ 0 to have a countably additive extension, namely that _µ_ 0 already has to be countably additive _within B_ 0. More precisely, suppose that _E_ 1 _, E_ 2 _, E_ 3 _, . . . ∈ B_ 0 were disjoint sets such that their union[�] _[∞] n_ =1 _[E][n]_[was][also][in] _[B]_[0][.] (Note that this latter property is not automatic as _B_ 0 is merely a Boolean algebra rather than a _σ_ -algebra.) Then, in order for _µ_ 0 to 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

185 

be extendible to a countably additive measure, it is clearly necessary that 

**==> picture [112 x 28] intentionally omitted <==**

Using the Carath´eodory extension theorem, we can show that this necessary condition is also sufficient. More precisely, we have 

**Definition 1.7.7** (Pre-measure) **.** A _pre-measure_ on a Boolean algebra _B_ 0 is a finitely additive measure _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] with the property that _µ_ 0([�] _[∞] n_ =1 _[E][n]_[) =][ �] _[∞] n_ =1 _[µ]_[0][(] _[E][n]_[) whenever] _[ E]_[1] _[, E]_[2] _[, E]_[3] _[, . . .][ ∈B]_[0] are disjoint sets such that[�] _[∞] n_ =1 _[E][n]_[is][in] _[B]_[0][.] 

## **Exercise 1.7.4.** 

- (i) Show that the requirement that _µ_ 0 is finitely additive can be relaxed to the condition that _µ_ 0( _∅_ ) = 0 without affecting the definition of a pre-measure. 

- (ii) Show that the condition _µ_ 0([�] _[∞] n_ =1 _[E][n]_[)][=][�] _[∞] n_ =1 _[µ]_[0][(] _[E][n]_[)][can] be relaxed to _µ_ 0([�] _[∞] n_ =1 _[E][n]_[)] _[≤]_[�] _[∞] n_ =1 _[µ]_[0][(] _[E][n]_[)][without][affect-] ing the definition of a pre-measure. 

- (iii) On the other hand, give an example to show that if one performs both of the above two relaxations at once, one starts admitting objects _µ_ 0 that are not pre-measures. 

**Exercise 1.7.5.** Without using the theory of Lebesgue measure, show that elementary measure (on the elementary Boolean algebra) is a pre-measure. ( _Hint:_ use Lemma 1.2.6. Note that one has to also deal with co-elementary sets as well as elementary sets in the elementary Boolean algebra.) 

**Exercise 1.7.6.** Construct a finitely additive measure _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] that is not a pre-measure. ( _Hint:_ take _X_ to be the natural numbers, take _B_ 0 = 2 **[N]** to be the discrete algebra, and define _µ_ 0 separately for finite and infinite sets.) 

**Theorem 1.7.8** (Hahn-Kolmogorov theorem) **.** _Every pre-measure µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] _on a Boolean algebra B_ 0 _in X can be extended to a countably additive measure µ_ : _B →_ [0 _,_ + _∞_ ] _._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

186 

**Proof.** We mimic the construction of Lebesgue measure from elementary measure. Namely, for any set _E ⊂ X_ , define the _outer measure µ[∗]_ ( _E_ ) of _E_ to be the quantity 

**==> picture [252 x 28] intentionally omitted <==**

It is easy to verify (cf. Exercise 1.2.3) that _µ[∗]_ is indeed an outer measure. Let _B_ be the collection of all sets _E ⊂ X_ that are Carath´eodory measurable with respect to _µ[∗]_ , and let _µ_ be the restriction of _µ[∗]_ to _B_ . By the Carath´eodory extension theorem, _B_ is a _σ_ -algebra and _µ_ is a countably additive measure. 

It remains to show that _B_ contains _B_ 0 and that _µ_ extends _µ_ 0. Thus, let _E ∈B_ 0; we need to show that _E_ is Carath´eodory measurable with respect to _µ[∗]_ and that _µ[∗]_ ( _E_ ) = _µ_ 0( _E_ ). To prove the first claim, let _A ⊂ X_ be arbitrary. We need to show that 

**==> picture [138 x 11] intentionally omitted <==**

by subadditivity, it suffices to show that 

**==> picture [138 x 11] intentionally omitted <==**

We may assume that _µ[∗]_ ( _A_ ) is finite, since the claim is trivial otherwise. 

Fix _ε >_ 0. By definition of _µ[∗]_ , one can find _E_ 1 _, E_ 2 _, . . . ∈B_ 0 covering _A_ such that 

**==> picture [108 x 28] intentionally omitted <==**

The sets _En ∩ E_ lie in _B_ 0 and cover _A ∩ E_ and thus 

**==> picture [128 x 28] intentionally omitted <==**

Similarly we have 

**==> picture [116 x 28] intentionally omitted <==**

Meanwhile, from finite additivity we have 

**==> picture [154 x 11] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

187 

Combining all of these estimates, we obtain 

**==> picture [156 x 11] intentionally omitted <==**

since _ε >_ 0 was arbitrary, the claim follows. 

Finally, we have to show that _µ[∗]_ ( _E_ ) = _µ_ 0( _E_ ). Since _E_ covers itself, we certainly have _µ[∗]_ ( _E_ ) _≤ µ_ 0( _E_ ). To show the converse inequality, it suffices to show that 

**==> picture [88 x 28] intentionally omitted <==**

whenever _E_ 1 _, E_ 2 _, . . . ∈B_ 0 cover _E_ . By replacing each _En_ with the smaller set _En\_[�] _[n] m[−]_ =1[1] _[E][m]_[(which][still][lies][in] _[B]_[0][,][and][still][covers] _[E]_[),] we may assume without loss of generality (thanks to the monotonicity of _µ_ 0) that the _En_ are disjoint. Similarly, by replacing each _En_ with the smaller set _En ∩ E_ we may assume without loss of generality that the union of the _En_ is exactly equal to _E_ . But then the claim follows from the hypothesis that _µ_ 0 is a pre-measure (and not merely a finitely additive measure). □ 

Let us call the measure _µ_ constructed in the above proof the _Hahn-Kolmogorov extension_ of the pre-measure _µ_ 0. Thus, for instance, from Exercise 1.7.2, the Hahn-Kolmogorov extension of elementary measure (with the convention that co-elementary sets have infinite elementary measure) is Lebesgue measure. This is not quite the unique extension of _µ_ 0 to a countably additive measure, though. For instance, one could restrict Lebesgue measure to the Borel _σ_ - algebra, and this would still be a countably additive extension of elementary measure. However, the extension is unique within its own _σ_ -algebra: 

**Exercise 1.7.7.** Let _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] be a pre-measure, let _µ_ : _B →_ [0 _,_ + _∞_ ] be the Hahn-Kolmogorov extension of _µ_ 0, and let _µ[′]_ : _B[′] →_ [0 _,_ + _∞_ ] be another countably additive extension of _µ_ 0. Suppose also that _µ_ 0 is _σ-finite_ , which means that one can express the whole space _X_ as the countable union of sets _E_ 1 _, E_ 2 _, . . . ∈B_ 0 for which _µ_ 0( _En_ ) _< ∞_ for all _n_ . Show that _µ_ and _µ[′]_ agree on their common domain of definition. In other words, show that _µ_ ( _E_ ) = _µ[′]_ ( _E_ ) for all _E ∈B∩B[′]_ . ( _Hint:_ first show that _µ[′]_ ( _E_ ) _≤ µ[∗]_ ( _E_ ) for all _E ∈B[′]_ .) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

188 

**Exercise 1.7.8.** The purpose of this exercise is to show that the _σ_ - finite hypothesis in Exercise 1.7.7 cannot be removed. Let _A_ be the collection of all subsets in **R** that can be expressed as finite unions of half-open intervals [ _a, b_ ). Let _µ_ 0 : _A →_ [0 _,_ + _∞_ ] be the function such that _µ_ 0( _E_ ) = + _∞_ for non-empty _E_ and _µ_ 0( _∅_ ) = 0. 

- (i) Show that _µ_ 0 is a pre-measure. 

- (ii) Show that _⟨A⟩_ is the Borel _σ_ -algebra _B_ [ **R** ]. 

- (iii) Show that the Hahn-Kolmogorov extension _µ_ : _B_ [ **R** ] _→_ [0 _,_ + _∞_ ] of _µ_ 0 assigns an infinite measure to any non-empty Borel set. 

- (iv) Show that counting measure # (or more generally, _c_ # for any _c ∈_ (0 _,_ + _∞_ ]) is another extension of _µ_ 0 on _B_ [ **R** ]. 

**Exercise 1.7.9.** Let _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] be a pre-measure which is _σ_ - finite (thus _X_ is the countable union of sets in _B_ 0 of finite _µ_ 0-measure), and let _µ_ : _B →_ [0 _,_ + _∞_ ] be the Hahn-Kolmogorov extension of _µ_ 0. 

- (i) Show that if _E ∈B_ , then there exists _F ∈⟨B_ 0 _⟩_ containing _E_ such that _µ_ ( _F \E_ ) = 0 (thus _F_ consists of the union of _E_ and a null set). Furthermore, show that _F_ can be chosen to be a countable intersection _F_ =[�] _[∞] n_ =1 _[F][n]_[of sets] _[ F][n]_[,][each of] which is a countable union _Fn_ =[�] _[∞] m_ =1 _[F][n,m]_[of][sets] _[F][n,m]_[in] _B_ 0. 

- (ii) If _E ∈B_ has finite measure (i.e. _µ_ ( _E_ ) _< ∞_ ), and _ε >_ 0, show that there exists _F ∈B_ 0 such that _µ_ ( _E_ ∆ _F_ ) _≤ ε_ . 

- (iii) Conversely, if _E_ is a set such that for every _ε >_ 0 there exists _F ∈B_ 0 such that _µ[∗]_ ( _E_ ∆ _F_ ) _≤ ε_ , show that _E ∈B_ . 

**1.7.3. Lebesgue-Stieltjes measure.** Now we use the Hahn-Kolmogorov extension theorem to construct a variety of measures. We begin with Lebesgue-Stieltjes measure. 

**Theorem 1.7.9** (Existence of Lebesgue-Stieltjes measure) **.** _Let F_ : **R** _→_ **R** _be a monotone non-decreasing function, and define the left and right limits_ 

**==> picture [178 x 18] intentionally omitted <==**

_thus one has F−_ ( _x_ ) _≤ F_ ( _x_ ) _≤ F_ +( _x_ ) _for all x. Let B_ [ **R** ] _be the Borel σ-algebra on_ **R** _. Then there exists a unique Borel measure_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

189 

_µF_ : _B_ [ **R** ] _→_ [0 _,_ + _∞_ ] _such that_ (1.33) _µF_ ([ _a, b_ ]) = _F_ +( _b_ ) _− F−_ ( _a_ ) _, µF_ ([ _a, b_ )) = _F−_ ( _b_ ) _− F−_ ( _a_ ) _, µF_ (( _a, b_ ]) = _F_ +( _b_ ) _− F_ +( _a_ ) _, µF_ (( _a, b_ )) = _F−_ ( _b_ ) _− F_ +( _a_ ) _for all −∞ < b < a < ∞, and_ (1.34) _µF_ ( _{a}_ ) = _F_ +( _a_ ) _− F−_ ( _a_ ) _for all a ∈_ **R** _._ 

**Proof.** (Sketch) For this proof, we will deviate from our previous notational conventions, and allow intervals to be unbounded, thus in particular including the half-infinite intervals [ _a,_ + _∞_ ), ( _a,_ + _∞_ ), ( _−∞, a_ ], ( _−∞, a_ ) and the doubly infinite interval ( _−∞,_ + _∞_ ) as intervals. 

Define the _F_ -volume _|I|F ∈_ [0 _,_ + _∞_ ] of any interval _I_ , adopting the obvious conventions that _F−_ (+ _∞_ ) = sup _y∈_ **R** _F_ ( _y_ ) and _F_ +( _−∞_ ) = inf _y∈_ **R** _F_ ( _y_ ), and also adopting the convention that the empty interval _∅_ has zero _F_ -volume, _|∅|F_ = 0. Note that _F−_ (+ _∞_ ) could equal + _∞_ and _F_ +( _−∞_ ) could equal _−∞_ , but in all circumstances the _F_ - volume _|I|F_ is well-defined and takes values in [0 _,_ + _∞_ ], after adopting the obvious conventions to evaluate expressions such as + _∞−_ ( _−∞_ ). 

A somewhat tedious case check (Exercise!) gives the additivity property 

**==> picture [96 x 11] intentionally omitted <==**

whenever _I_ , _J_ are disjoint intervals that share a common endpoint. As a corollary, we see that if a interval _I_ is partitioned into finitely many disjoint sub-intervals _I_ 1 _, . . . , Ik_ , we have _|I|_ = _|I_ 1 _|_ + _. . ._ + _|Ik|_ . 

Let _B_ 0 be the Boolean algebra generated by the (possibly infinite) intervals, then _B_ 0 consists of those sets that can be expressed as a finite union of intervals. (This is slightly larger than the elementary algebra, as it allows for half-infinite intervals such as [0 _,_ + _∞_ ), whereas the elementary algebra does not.) We can define a measure _µ_ 0 on this algebra by declaring 

**==> picture [117 x 11] intentionally omitted <==**

whenever _E_ = _I_ 1 _∪ . . . ∪ Ik_ is the disjoint union of finitely many intervals. One can check (Exercise!) that this measure is well-defined 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

190 

(in the sense that it gives a unique value to _µ_ 0( _E_ ) for each _E ∈B_ 0) and is finitely additive. We now claim that _µ_ 0 is a pre-measure: thus we suppose that _E_ = _B_ 0 is the disjoint union of countably many sets _E_ 1 _, E_ 2 _, . . . ∈B_ 0, and wish to show that 

**==> picture [90 x 28] intentionally omitted <==**

By splitting up _E_ into intervals and then intersecting each of the _En_ with these intervals and using finite additivity, we may assume that _E_ is a single interval. By splitting up the _En_ into their component intervals and using finite additivity, we may assume that the _En_ are also individual intervals. By subadditivity, it suffices to show that 

**==> picture [90 x 28] intentionally omitted <==**

By the definition of _µ_ 0( _E_ ), one can check that 

**==> picture [195 x 18] intentionally omitted <==**

where _K_ ranges over all compact intervals contained in _E_ (Exercise!). Thus, it suffices to show that 

**==> picture [90 x 29] intentionally omitted <==**

for each compact sub-interval _K_ of _E_ . In a similar spirit, one can show that 

**==> picture [102 x 16] intentionally omitted <==**

where _U_ ranges over all open intervals containing _En_ (Exercise!). Using the _ε/_ 2 _[n]_ trick, it thus suffices to show that 

**==> picture [88 x 29] intentionally omitted <==**

whenever _Un_ is an open interval containing _En_ . But by the HeineBorel theorem, one can cover _K_ by a finite number[�] _[N] n_ =1 _[U][n]_[of][the] _Un_ , hence by finite subadditivity 

**==> picture [88 x 30] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

191 

and the claim follows. 

As _µ_ 0 is now verified to be a pre-measure, we may use the HahnKolmogorov extension theorem to extend it to a countably additive measure _µ_ on a _σ_ -algebra _B_ that contains _B_ 0. In particular, _B_ contains all the elementary sets and hence (by Exercise 1.4.14) contains the Borel _σ_ -algebra. Restricting _µ_ to the Borel _σ_ -algebra we obtain the existence claim. 

Finally, we establish uniqueness. If _µ[′]_ is another Borel measure with the stated properties, then _µ[′]_ ( _K_ ) = _|K|F_ for every compact interval _K_ , and hence by (1.35) and upward monotone convergence, one has _µ[′]_ ( _I_ ) = _|I|F_ for every interval (including the unbounded ones). This implies that _µ[′]_ agrees with _µ_ 0 on _B_ 0, and thus (by Exercise 1.7.7, noting that _µ_ 0 is _σ_ -finite) agrees with _µ_ on Borel measurable sets. □ 

**Exercise 1.7.10.** Verify the claims marked “Exercise!” in the above proof. 

The measure _µF_ given by the above theorem is known as the _Lebesgue-Stieltjes measure µF_ of _F_ . (In some texts, this measure is only defined when _F_ is right-continuous, or equivalently if _F_ = _F_ +.) 

**Exercise 1.7.11.** Define a _Radon measure_ on **R** to be a Borel measure _µ_ obeying the following additional properties: 

- (i) (Local finiteness) _µ_ ( _K_ ) _< ∞_ for every compact _K_ . 

- (ii) (Inner regularity) One has _µ_ ( _E_ ) = sup _K⊂E,K_ compact _µ_ ( _K_ ) for every Borel set _E_ . 

- (iii) (Outer regularity) One has _µ_ ( _E_ ) = inf _U ⊃E,U_ open _µ_ ( _U_ ) for every Borel set _E_ . 

Show that for every monotone function _F_ : **R** _→_ **R** , the LebesgueStieltjes measure _µF_ is a Radon measure on **R** ; conversely, if _µ_ is a Radon measure on **R** , show that there exists a monotone function _F_ : **R** _→_ **R** such that _µ_ = _µF_ . 

Radon measures are studied in more detail in _§_ 1.10 of _An epsilon of room, Vol. I_ . 

**Exercise 1.7.12** (Near uniqueness) **.** If _F, F[′]_ : **R** _→_ **R** are monotone non-decreasing functions, show that _µF_ = _µF ′_ if and only if there 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

192 

exists a constant _C ∈_ **R** such that _F_ +( _x_ ) = _F_ + _[′]_[(] _[x]_[) +] _[ C]_[and] _[F][−]_[(] _[x]_[) =] _F−[′]_[(] _[x]_[)][+] _[C]_[for][all] _[x][∈]_ **[R]**[.] Note that this implies that the value of _F_ at its points of discontinuity are irrelevant for the purposes of determining the Lebesgue-Stieltjes measure _µF_ ; in particular, _µF_ = _µF_ + = _µF−_ . 

In the special case when _F_ +( _−∞_ ) = 0 and _F−_ (+ _∞_ ) = 1, then _µF_ is a probability measure, and _F_ +( _x_ ) = _µF_ (( _−∞, x_ ]) is known as the _cumulative distribution function_ of _µF_ . 

Now we give some examples of Lebesgue-Stieltjes measure. 

**Exercise 1.7.13** (Lebesgue-Stieltjes measure, absolutely continuous case) **.** 

- (i) If _F_ : **R** _→_ **R** is the identity function _F_ ( _x_ ) = _x_ , show that _µF_ is equal to Lebesgue measure _m_ . 

- (ii) If _F_ : **R** _→_ **R** is monotone non-decreasing and absolutely continuous (which in particular implies that _F[′]_ exists and is absolutely integrable, show that _µF_ = _mF ′_ in the sense of Exercise 1.4.49, thus 

**==> picture [94 x 23] intentionally omitted <==**

for any Borel measurable _E_ , and 

**==> picture [154 x 24] intentionally omitted <==**

for any unsigned Borel measurable _f_ : **R** _→_ [0 _,_ + _∞_ ]. 

In view of the above exercise, the integral � **R** _[f][dµ][F]_[is][often][ab-] breviated � **R** _[f][dF]_[,][and][referred][to][as][the] _[Lebesgue-Stieltjes][integral]_ of _f_ with respect to _F_ . In particular, observe the identity 

**==> picture [116 x 26] intentionally omitted <==**

for any monotone non-decreasing _F_ : **R** _→_ **R** and any _−∞ < b < a <_ + _∞_ , which can be viewed as yet another formulation of the fundamental theorem of calculus. 

**Exercise 1.7.14** (Lebesgue-Stieltjes measure, pure point case) **.** 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

193 

- (i) If _H_ : **R** _→_ **R** is the _Heaviside function H_ := 1[0 _,_ + _∞_ ), show that _µH_ is equal to the Dirac measure _δ_ 0 at the origin (defined in Example 1.4.22). 

- (ii) If _F_ =[�] _n[c][n][J][n]_[is][a][jump][function][(as][defined][in][Definition] 1.6.30), show that _µF_ is equal to the linear combination � _cnδxn_ of delta functions (as defined in Exercise 1.4.22), where _xn_ is the point of discontinuity for the basic jump function _Jn_ . 

**Exercise 1.7.15** (Lebesgue-Stieltjes measure, singular continuous case) **.** 

- (i) If _F_ : **R** _→_ **R** is a monotone non-decreasing function, show that _F_ is continuous if and only if _µF_ ( _{x}_ ) = 0 for all _x ∈_ **R** . 

- (ii) If _F_ is the Cantor function (defined in Exercise 1.6.47), show that _µF_ is a probability measure supported on the middle-thirds Cantor set (see Exercise 1.2.9) in the sense that _µF_ ( **R** _\C_ ) = 0. The measure _µF_ is known as _Cantor measure_ . 

- (iii) If _µF_ is Cantor measure, establish the self-similarity properties _µ_ ( 3[1] _[·][ E]_[) =][1] 2 _[µ]_[(] _[E]_[)][and] _[µ]_[(][1] 3 _[·][ E]_[ +][2] 3[) =][1] 2 _[µ]_[(] _[E]_[)][for][every] Borel-measurable _E ⊂_ [0 _,_ 1], where[1] 3 _[·][ E]_[:=] _[ {]_[1] 3 _[x]_[ :] _[ x][ ∈][E][}]_[.] 

**Exercise 1.7.16** (Connection with Riemann-Stieltjes integral) **.** Let _F_ : **R** _→_ **R** be monotone non-decreasing, let [ _a, b_ ] be a compact interval, and let _f_ : [ _a, b_ ] _→_ **R** be continuous. Suppose that _F_ is continuous at the endpoints _a, b_ of the interval. Show that for every _ε >_ 0 there exists _δ >_ 0 such that 

**==> picture [196 x 28] intentionally omitted <==**

whenever _a_ = _t_ 0 _< t_ 1 _< . . . < tn_ = _b_ and _t[∗] i[∈]_[[] _[t][i][−]_[1] _[, t][i]_[]][for][1] _[≤] i ≤ n_ are such that sup1 _≤i≤n |ti − ti−_ 1 _| ≤ δ_ . In the language of the _Riemann-Stieltjes integral_ , this result asserts that the LebesgueStieltjes integral extends the Riemann-Stieltjes integral. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

194 

**Exercise 1.7.17** (Integration by parts formula) **.** Let _F, G_ : **R** _→_ **R** be monotone non-decreasing and continuous. Show that 

**==> picture [222 x 25] intentionally omitted <==**

for any compact interval [ _a, b_ ]. ( _Hint:_ use Exercise 1.7.16.) This formula can be partially extended to the case when one or both of _F, G_ have discontinuities, but care must be taken when _F_ and _G_ are simultaneously discontinuous at the same location. 

**1.7.4. Product measure.** Given two sets _X_ and _Y_ , one can form their Cartesian product _X × Y_ = _{_ ( _x, y_ ) : _x ∈ X, y ∈ Y }_ . This set is naturally equipped with the coordinate projection maps _πX_ : _X × Y → X_ and _πY_ : _X × Y → Y_ defined by setting _πX_ ( _x, y_ ) := _x_ and _πY_ ( _x, y_ ) := _y_ . One can certainly take Cartesian products _X_ 1 _×. . .×Xd_ of more than two sets, or even take an infinite product[�] _α∈A[X][α]_[, but] for simplicity we will only discuss the theory for products of two sets for now. 

Now suppose that ( _X, BX_ ) and ( _Y, BY_ ) are measurable spaces. Then we can still form the Cartesian product _X×Y_ and the projection maps _πX_ : _X × Y → X_ and _πY_ : _X × Y → Y_ . But now we can also form the _pullback σ_ -algebras 

**==> picture [230 x 13] intentionally omitted <==**

and 

**==> picture [232 x 13] intentionally omitted <==**

We then define the _product σ-algebra BX × BY_ to be the _σ_ -algebra generated by the union of these two _σ_ -algebras: 

**==> picture [148 x 11] intentionally omitted <==**

This definition has several equivalent formulations: 

**Exercise 1.7.18.** Let ( _X, BX_ ) and ( _Y, BY_ ) be measurable spaces. 

- (i) Show that _BX × BY_ is the _σ_ -algebra generated by the sets _E × F_ with _E ∈BX_ , _Y ∈BY_ . In other words, _BX × BY_ is the coarsest _σ_ -algebra on _X × Y_ with the property that the 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

195 

   - product of a _BX_ -measurable set and a _BY_ -measurable set is always _BX × BY_ measurable. 

- (ii) Show that _BX × BY_ is the coarsest _σ_ -algebra on _X × Y_ that makes the projection maps _πX , πY_ both measurable morphisms (see Remark 1.4.33). 

- (iii) If _E ∈BX × BY_ , show that the sets _Ex_ := _{y ∈ Y_ : ( _x, y_ ) _∈ E}_ lie in _BY_ for every _x ∈ X_ , and similarly that the sets _E[y]_ := _{x ∈ X_ : ( _x, y_ ) _∈ E}_ lie in _BX_ for every _y ∈ Y_ . 

- (iv) If _f_ : _X × Y →_ [0 _,_ + _∞_ ] is measurable (with respect to _BX × BY_ ), show that the function _fx_ : _y �→ f_ ( _x, y_ ) is _BY_ - measurable for every _x ∈ X_ , and similarly that the function _f[y]_ : _x �→ f_ ( _x, y_ ) is _BX_ -measurable for every _y ∈ Y_ . 

- (v) If _E ∈BX × BY_ , show that the slices _Ex_ := _{y ∈ Y_ : ( _x, y_ ) _∈ E}_ lie in a countably generated _σ_ -algebra. In other words, show that there exists an at most countable collection _A_ = _AE_ of sets (which can depend on _E_ ) such that _{Ex_ : _x ∈ X} ⊂⟨A⟩_ . Conclude in particular that the number of distinct slices _Ex_ is at most _c_ , the cardinality of the continuum. (The last part of this exercise is only suitable for students who are comfortable with cardinal arithmetic.) 

## **Exercise 1.7.19.** 

- (i) Show that the product of two trivial _σ_ -algebras (on two different spaces _X, Y_ ) is again trivial. 

- (ii) Show that the product of two atomic _σ_ -algebras is again atomic. 

- (iii) Show that the product of two finite _σ_ -algebras is again finite. 

- (iv) Show that the product of two Borel _σ_ -algebras (on two Euclidean spaces **R** _[d] ,_ **R** _[d][′]_ with _d, d[′] ≥_ 1) is again the Borel _σ_ -algebra (on **R** _[d] ×_ **R** _[d][′] ≡_ **R** _[d]_[+] _[d][′]_ ). 

- (v) Show that the product of two Lebesgue _σ_ -algebras (on two Euclidean spaces **R** _[d] ,_ **R** _[d][′]_ with _d, d[′] ≥_ 1) is _not_ the Lebesgue _σ_ -algebra. ( _Hint:_ argue by contradiction and use Exercise 1.7.18(iii).) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

196 

- (vi) However, show that the Lebesgue _σ_ -algebra on **R** _[d]_[+] _[d][′]_ is the _completion_ (see Exercise 1.4.26) of the product of the Lebesgue _σ_ -algebras of **R** _[d]_ and **R** _[d][′]_ with respect to _d_ + _d[′]_ - dimensional Lebesgue measure. 

- (vii) This part of the exercise is only for students who are comfortable with cardinal arithmetic. Give an example to show that the product of two discrete _σ_ -algebras is not necessarily discrete. 

- (viii) On the other hand, show that the product of two discrete _σ_ -algebras 2 _[X] ,_ 2 _[Y]_ is again a discrete _σ_ -algebra if at least one of the domains _X, Y_ is at most countably infinite. 

Now suppose we have two measure spaces ( _X, BX , µX_ ) and ( _Y, BY , µY_ ). Given that we can multiply together the sets _X_ and _Y_ to form a product set _X × Y_ , and can multiply the _σ_ -algebras _BX_ and _BY_ together to form a product _σ_ -algebra _BX × BY_ , it is natural to expect that we can multiply the two measures _µX_ : _BX →_ [0 _,_ + _∞_ ] and _µY_ : _BY →_ [0 _,_ + _∞_ ] to form a product measure _µX × µY_ : _BX ×BY →_ [0 _,_ + _∞_ ]. In view of the “base times height formula” that one learns in elementary school, one expects to have 

(1.36) _µX × µY_ ( _E × F_ ) = _µX_ ( _E_ ) _µY_ ( _F_ ) 

whenever _E ∈BX_ and _F ∈BY_ . 

To construct this measure, it is convenient to make the assumption that both spaces are _σ-finite_ : 

**Definition 1.7.10** ( _σ_ -finite) **.** A measure space ( _X, B, µ_ ) is _σ-finite_ if _X_ can be expressed as the countable union of sets of finite measure. 

Thus, for instance, **R** _[d]_ with Lebesgue measure is _σ_ -finite, as **R** _[d]_ can be expressed as the union of (for instance) the balls _B_ (0 _, n_ ) for _n_ = 1 _,_ 2 _,_ 3 _, . . ._ , each of which has finite measure. On the other hand, **R** _[d]_ with counting measure is not _σ_ -finite (why?). But most measure spaces that one actually encounters in analysis (including, clearly, all probability spaces) are _σ_ -finite. It is possible to partially extend the theory of product spaces to the non- _σ_ -finite setting, but there are a number of very delicate technical issues that arise and so we will not discuss them here. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

197 

As long as we restrict attention to the _σ_ -finite case, product measure always exists and is unique: 

**Proposition 1.7.11** (Existence and uniqueness of product measure) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be σ-finite measure spaces. Then there exists a unique measure µX × µY on BX × BY that obeys µX × µY_ ( _E × F_ ) = _µX_ ( _E_ ) _µY_ ( _F_ ) _whenever E ∈BX and F ∈BY ._ 

**Proof.** We first show existence. Inspired by the fact that Lebesgue measure is the Hahn-Kolmogorov completion of elementary (pre-)measure, we shall first construct an “elementary product pre-measure” that we will then apply Theorem 1.7.8 to. 

Let _B_ 0 be the collection of all finite unions 

**==> picture [144 x 10] intentionally omitted <==**

of Cartesian products of _BX_ -measurable sets _E_ 1 _, . . . , Ek_ and _BY_ - measurable sets _F_ 1 _, . . . , Fk_ . (One can think of such sets as being somewhat analogous to elementary sets in Euclidean space, although the analogy is not perfectly exact.) It is not difficult to verify that this is a Boolean algebra (though it is not, in general, a _σ_ -algebra). Also, any set in _B_ 0 can be easily decomposed into a _disjoint_ union of product sets _E_ 1 _× F_ 1 _, . . . , Ek × Fk_ of _BX_ -measurable sets and _BY_ - measurable sets (cf. Exercise 1.1.2). We then define the quantity _µ_ 0( _S_ ) associated such a disjoint union _S_ by the formula 

**==> picture [122 x 31] intentionally omitted <==**

whenever _S_ is the disjoint union of products _E_ 1 _× F_ 1 _, . . . , Ek × Fk_ of _BX_ -measurable sets and _BY_ -measurable sets. One can show that this definition does not depend on exactly how _S_ is decomposed, and gives a finitely additive measure _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] (cf. Exercise 1.1.2 and Exercise 1.4.33). 

Now we show that _µ_ 0 is a pre-measure. It suffices to show that if _S ∈B_ 0 is the countable disjoint union of sets _S_ 1 _, S_ 2 _, . . . ∈B_ 0, then _µ_ 0( _S_ ) =[�] _[∞] n_ =1 _[µ]_[(] _[S][n]_[).] 

Splitting _S_ up into disjoint product sets, and restricting the _Sn_ to each of these product sets in turn, we may assume without loss 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

198 

of generality (using the finite additivity of _µ_ 0) that _S_ = _E × F_ for some _E ∈BX_ and _F ∈BY_ . In a similar spirit, by breaking each _Sn_ up into component product sets and using finite additivity again, we may assume without loss of generality that each _Sn_ takes the form _Sn_ = _En × Fn_ for some _En ∈BX_ and _Fn ∈BY_ . By definition of _µ_ 0, our objective is now to show that 

**==> picture [158 x 28] intentionally omitted <==**

To do this, first observe from construction that we have the pointwise identity 

**==> picture [138 x 28] intentionally omitted <==**

for all _x ∈ X_ and _y ∈ Y_ . We fix _x ∈ X_ , and integrate this identity in _y_ (noting that both sides are measurable and unsigned) to conclude that 

**==> picture [238 x 28] intentionally omitted <==**

The left-hand side simplifies to 1 _E_ ( _x_ ) _µY_ ( _F_ ). To compute the righthand side, we use the monotone convergence theorem (Theorem 1.4.44) to interchange the summation and integration, and soon see that the right-hand side is[�] _[∞] n_ =1[1] _[E] n_[(] _[x]_[)] _[µ][Y]_[ (] _[F][n]_[),][thus] 

**==> picture [146 x 28] intentionally omitted <==**

for all _x_ . Both sides are measurable and unsigned in _x_ , so we may integrate in _X_ and conclude that 

**==> picture [236 x 28] intentionally omitted <==**

The left-hand side here is _µX_ ( _E_ ) _µY_ ( _F_ ). Using monotone convergence as before, the right-hand side simplifies to[�] _[∞] n_ =1 _[µ][X]_[(] _[E][n]_[)] _[µ][Y]_[ (] _[F][n]_[), and] the claim follows. 

Now that we have established that _µ_ 0 is a pre-measure, we may apply Theorem 1.7.8 to extend this measure to a countably additive measure _µX ×µY_ on a _σ_ -algebra containing _B_ 0. By Exercise 1.7.18(2), 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

199 

_µX ×µY_ is a countably additive measure on _BX ×BY_ , and as it extends _µ_ 0, it will obey (1.36). Finally, to show uniqueness, observe from finite additivity that any measure _µX × µY_ on _BX × BY_ that obeys (1.36) must extend _µ_ 0, and so uniqueness follows from Exercise 1.7.7. □ 

**Remark 1.7.12.** When _X_ , _Y_ are not both _σ_ -finite, then one can still construct at least one product measure, but it will, in general, not be unique. This makes the theory much more subtle, and we will not discuss it in these notes. 

**Example 1.7.13.** From Exercise 1.2.22, we see that the product _m[d] × m[d][′]_ of the Lebesgue measures _m[d] , m[d][′]_ on ( **R** _[d] , L_ [ **R** _[d]_ ]) and ( **R** _[d] , L_ [ **R** _[d][′]_ ]) respectively will agree with Lebesgue measure _m[d]_[+] _[d][′]_ on the product space _L_ [ **R** _[d]_ ] _× L_ [ **R** _[d][′]_ ], which as noted in Exercise 1.7.19 is a subalgebra of _L_ [ **R** _[d]_[+] _[d][′]_ ]. After taking the completion _m[d] × m[d][′]_ of this product measure, one obtains the full Lebesgue measure _m[d]_[+] _[d][′]_ . 

**Exercise 1.7.20.** Let ( _X, BX_ ), ( _Y, BY_ ) be measurable spaces. 

- (i) Show that the product of two Dirac measures on ( _X, BX_ ), ( _Y, BY_ ) is a Dirac measure on ( _X × Y, BX × BY_ ). 

- (ii) If _X, Y_ are at most countable, show that the product of the two counting measures on ( _X, BX_ ), ( _Y, BY_ ) is the counting measure on ( _X × Y, BX × BY_ ). 

**Exercise 1.7.21** (Associativity of product) **.** Let ( _X, BX , µX_ ), ( _Y, BY , µY_ ), ( _Z, BZ, µZ_ ) be _σ_ -finite sets. We may identify the Cartesian products ( _X × Y_ ) _× Z_ and _X ×_ ( _Y × Z_ ) with each other in the obvious manner. If we do so, show that ( _BX × BY_ ) _× BZ_ = _BX ×_ ( _BY × BZ_ ) and ( _µX × µY_ ) _× µZ_ = _µX ×_ ( _µY × µZ_ ). 

Now we integrate using this product measure. We will need the following technical lemma. Define a _monotone class_ in _X_ is a collection _B_ of subsets of _X_ with the following two closure properties: 

- (i) If _E_ 1 _⊂ E_ 2 _⊂ . . ._ are a countable increasing sequence of sets in _B_ , then[�] _[∞] n_ =1 _[E][n][∈B]_[.] 

- (ii) If _E_ 1 _⊃ E_ 2 _⊃ . . ._ are a countable decreasing sequence of sets in _B_ , then[�] _[∞] n_ =1 _[E][n][∈B]_[.] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

200 

**Lemma 1.7.14** (Monotone class lemma) **.** _Let A be a Boolean algebra on X. Then ⟨A⟩ is the smallest monotone class that contains A._ 

**Proof.** Let _B_ be the intersection of all the monotone classes that contain _A_ . Since _⟨A⟩_ is clearly one such class, _B_ is a subset of _⟨A⟩_ . Our task is then to show that _B_ contains _⟨A⟩_ . 

It is also clear that _B_ is a monotone class that contains _A_ . By replacing all the elements of _B_ with their complements, we see that _B_ is necessarily closed under complements. 

For any _E ∈A_ , consider the set _CE_ of all sets _F ∈B_ such that _F \E_ , _E\F_ , _F ∩ E_ , and _X\_ ( _E ∪ F_ ) all lie in _B_ . It is clear that _CE_ contains _A_ ; since _B_ is a monotone class, we see that _CE_ is also. By definition of _B_ , we conclude that _CE_ = _B_ for all _E ∈A_ . 

Next, let _D_ be the set of all _E ∈B_ such that _F \E_ , _E\F_ , _F ∩ E_ , and _X\_ ( _E∪F_ ) all lie in _B_ for all _F ∈B_ . By the previous discussion, we see that _D_ contains _A_ . One also easily verifies that _D_ is a monotone class. By definition of _B_ , we conclude that _D_ = _B_ . Since _B_ is also closed under complements, this implies that _B_ is closed with respect to finite unions. Since this class also contains _A_ , which contains _∅_ , we conclude that _B_ is a Boolean algebra. Since _B_ is also closed under increasing countable unions, we conclude that it is closed under arbitrary countable unions, and is thus a _σ_ -algebra. As it contains _A_ , it must also contain _⟨A⟩_ . □ 

**Theorem 1.7.15** (Tonelli’s theorem, incomplete version) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be σ-finite measure spaces, and let f_ : _X × Y →_ [0 _,_ + _∞_ ] _be measurable with respect to BX × BY . Then:_ 

- (i) _The functions x �→_ � _Y[f]_[(] _[x, y]_[)] _[ dµ][Y]_[ (] _[y]_[)] _[ and][ y][�→]_ � _X[f]_[(] _[x, y]_[)] _[ dµ][X]_[(] _[x]_[)] _(which are well-defined, thanks to Exercise 1.7.18) are measurable with respect to BX and BY respectively._ 

- (ii) _We have_ 

**==> picture [146 x 57] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

201 

**==> picture [148 x 23] intentionally omitted <==**

**Proof.** By writing the _σ_ -finite space _X_ as an increasing union _X_ = � _∞n_ =1 _[X][n]_[of][finite][measure][sets,][we][see][from][several][applications][of] the monotone convergence theorem (Theorem 1.4.44) that it suffices to prove the claims with _X_ replaced by _Xn_ . Thus we may assume without loss of generality that _X_ has finite measure. Similarly we may assume _Y_ has finite measure. Note from (1.36) that this implies that _X × Y_ has measure also. 

Every unsigned measurable function is the increasing limit of unsigned simple functions. By several applications of the monotone convergence theorem (Theorem 1.4.44), we thus see that it suffices to verify the claim when _f_ is a simple function. By linearity, it then suffices to verify the claim when _f_ is an indicator function, thus _f_ = 1 _S_ for some _S ∈BX × BY_ . 

Let _C_ be the set of all _S ∈BX × BY_ for which the claims hold. From the repeated applications of the monotone convergence theorem (Theorem 1.4.44) and the downward monotone convergence theorem (which is available in this finite measure setting) we see that _C_ is a monotone class. 

By direct computation (using (1.36)), we see that _C_ contains as an element any product _S_ = _E × F_ with _E ∈BX_ and _F ∈BY_ . By finite additivity, we conclude that _C_ also contains as an element any a disjoint finite union _S_ = _E_ 1 _×F_ 1 _∪. . .∪Ek ×Fk_ of such products. This implies that _C_ also contains the Boolean algebra _B_ 0 in the proof of Proposition 1.7.11, as such sets can always be expressed as the disjoint finite union of Cartesian products of measurable sets. Applying the monotone class lemma, we conclude that _C_ contains _⟨B_ 0 _⟩_ = _BX ×BY_ , and the claim follows. □ 

**Remark 1.7.16.** Note that Tonelli’s theorem for sums (Theorem 0.0.2) is a special case of the above result when _µX , µY_ are counting measure. In a similar spirit, Corollary 1.4.46 is the special case when just one of _µX , µY_ is counting measure. 

**Corollary 1.7.17.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be σ-finite measure spaces, and let E ∈BX ×BY be a null set with respect to µX ×µY ._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

202 

_Then for µX -almost every x ∈ X, the set Ex_ := _{y ∈ Y_ : ( _x, y_ ) _∈ E} is a µY -null set; and similarly, for µY -almost every y ∈ Y , the set E[y]_ := _{x ∈ X_ : ( _x, y_ ) _∈ E} is a µX -null set._ 

**Proof.** Applying the Tonelli theorem to the indicator function 1 _E_ , we conclude that 

**==> picture [308 x 85] intentionally omitted <==**

With this corollary, we can extend Tonelli’s theorem to the _completion_ ( _X ×Y, BX × BY , µX × µY_ ) of the product space ( _X ×Y, BX × BY , µX × µY_ ), as constructed in Exercise 1.4.26. But we can easily extend the Tonelli theorem to this context: 

**Theorem 1.7.18** (Tonelli’s theorem, complete version) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be complete σ-finite measure spaces, and let f_ : _X ×_ 

_Y →_ [0 _,_ + _∞_ ] _be measurable with respect to BX × BY . Then:_ 

(i) _For µX -almost every x ∈ X, the function y �→ f_ ( _x, y_ ) _is BY -measurable, and in particular_ � _Y[f]_[(] _[x, y]_[)] _[dµ][Y]_[ (] _[y]_[)] _[exists.] Furthermore, the (µX -almost everywhere defined) map x �→_ � _Y[f]_[(] _[x, y]_[)] _[dµ][Y][is][B][X][-measurable.]_ 

(ii) _For µY -almost every y ∈ Y , the function x �→ f_ ( _x, y_ ) _is BX -measurable, and in particular_ � _X[f]_[(] _[x, y]_[)] _[dµ][X]_[(] _[x]_[)] _[exists.] Furthermore, the (µY -almost everywhere defined) map y �→_ � _X[f]_[(] _[x, y]_[)] _[dµ][X][is][B][Y][ -measurable.]_ 

(iii) _We have_ 

**==> picture [289 x 65] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

203 

**Proof.** From Exercise 1.4.28, every measurable set in _BX × BY_ is equal to a measurable set in _BX × BY_ outside of a _µX × µY_ -null set. This implies that the _BX × BY_ -measurable function _f_ agrees with a _BX × BY_ -measurable function _f_[˜] outside of a _µX × µY_ -null set _E_ (as can be seen by expressing _f_ as the limit of simple functions). From Corollary 1.7.17, we see that for _µX_ -almost every _x ∈ X_ , the function _y �→ f_ ( _x, y_ ) agrees with _y �→ f_[˜] ( _x, y_ ) outside of a _µY_ -null set (and is in particular measurable, as ( _Y, BY , µY_ ) is complete); and similarly for _µY_ -almost every _y ∈ Y_ , the function _x �→ f_ ( _x, y_ ) agrees with _x �→ f_[˜] ( _x, y_ ) outside of a _µX_ -null set and is measurable, and the claim follows. □ 

Specialising to the case when _f_ is an indicator function _f_ = 1 _E_ , we conclude 

**Corollary 1.7.19** (Tonelli’s theorem for sets) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be complete σ-finite measure spaces, and let E ∈ BX × BY . Then:_ 

- (i) _For µX -almost every x ∈ X, the set Ex_ := _{y ∈ Y_ : ( _x, y_ ) _∈ E} lies in BY , and the (µX -almost everywhere defined) map x �→ µY_ ( _Ex_ ) _is BX -measurable._ 

(ii) _For µY -almost every y ∈ Y , the set E[y]_ := _{x ∈ X_ : ( _x, y_ ) _∈ E} lies in BX , and the (µY -almost everywhere defined) map y �→ µX_ ( _E[y]_ ) _is BY -measurable._ 

**==> picture [59 x 11] intentionally omitted <==**

**==> picture [226 x 24] intentionally omitted <==**

**==> picture [98 x 24] intentionally omitted <==**

**Exercise 1.7.22.** The purpose of this exercise is to demonstrate that Tonelli’s theorem can fail if the _σ_ -finite hypothesis is removed, and also that product measure need not be unique. Let _X_ is the unit interval [0 _,_ 1] with Lebesgue measure _m_ (and the Lebesgue _σ_ -algebra _L_ ([0 _,_ 1])) and _Y_ is the unit interval [0 _,_ 1] with counting measure (and the discrete _σ_ -algebra 2[[0] _[,]_[1]] ) #. Let _f_ := 1 _E_ be the indicator function of the diagonal _E_ := _{_ ( _x, x_ ) : _x ∈_ [0 _,_ 1] _}_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

204 

- (i) Show that _f_ is measurable in the product _σ_ -algebra. 

- (ii) Show that � _X_[(] � _Y[f]_[(] _[x, y]_[)] _[d]_[#(] _[y]_[))] _[dm]_[(] _[x]_[) = 1.] 

- (iii) Show that � _Y_[(] � _X[f]_[(] _[x, y]_[)] _[dm]_[(] _[x]_[))] _[d]_[#(] _[y]_[) = 0.] 

- (iv) Show that there is more than one measure _µ_ on _L_ ([0 _,_ 1]) _×_ 2[[0] _[,]_[1]] with the property that _µ_ ( _E × F_ ) = _m_ ( _E_ )#( _F_ ) for all _E ∈L_ ([0 _,_ 1]) and _F ∈_ 2[[0] _[,]_[1]] . ( _Hint:_ use the two different ways to perform a double integral to create two different measures.) 

**Remark 1.7.20.** If _f_ is not assumed to be measurable in the product space (or its completion), then of course the expression � _X×Y[f]_[(] _[x, y]_[)] _[d] µX × µY_ ( _x, y_ ) does not make sense. Furthermore, in this case the remaining two expressions in (1.37) may become different as well (in some models of set theory, at least), even when _X_ and _Y_ are finite measure. For instance, let us assume the _continuum hypothesis_ , which implies that the unit interval [0 _,_ 1] can be placed in one-to-one correspondence with the _first uncountable ordinal ω_ 1. Let _≺_ be the ordering of [0 _,_ 1] that is associated to this ordinal, let _E_ := _{_ ( _x, y_ ) _∈_ [0 _,_ 1][2] : _x ≺ y}_ , and let _f_ := 1 _E_ . Then, for any _y ∈_ [0 _,_ 1], there are at most countably many _x_ such that _x ≺ y_ , and so �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[dx]_[exists][and][is][equal] to zero for every _y_ . On the other hand, for every _x ∈_ [0 _,_ 1], one has _x ≺ y_ for all but countably many _y ∈_ [0 _,_ 1], and so �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[ dy]_[ex-] ists and is equal to one for every _y_ , and so the last two expressions in (1.37) exist but are unequal. (In particular, Tonelli’s theorem implies that _E_ cannot be a Lebesgue measurable subset of [0 _,_ 1][2] .) Thus we see that measurability in the product space is an important hypothesis. (There do however exist models of set theory (with the axiom of choice) in which such counterexamples cannot be constructed, at least in the case when _X_ and _Y_ are the unit interval with Lebesgue measure.) 

Tonelli’s theorem is for the unsigned integral, but it leads to an important analogue for the absolutely integral, known as _Fubini’s theorem_ : 

**Theorem 1.7.21** (Fubini’s theorem) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be complete σ-finite measure spaces, and let f_ : _X × Y →_ **C** _be absolutely integrable with respect to BX × BY . Then:_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

205 

- (i) _For µX -almost every x ∈ X, the function y �→ f_ ( _x, y_ ) _is absolutely integrable with respect to µY , and in particular[dµ][Y]_[ (] _[y]_[)] _[exists.][Furthermore,][the][(][µ][X][-almost][ev-]_ 

- � _Y[f]_[(] _[x, y]_[)] _erywhere defined) map x �→_ � _Y[f]_[(] _[x, y]_[)] _[dµ][Y]_[ (] _[y]_[)] _[is][absolutely] integrable with respect to µX ._ 

- (ii) _For µY -almost every y ∈ Y , the function x �→ f_ ( _x, y_ ) _is absolutely integrable with respect to µX , and in particular[dµ][X]_[(] _[x]_[)] _[exists.][Furthermore,][the][(][µ][Y][ -almost][ev-]_ 

- � _X[f]_[(] _[x, y]_[)] _erywhere defined) map y �→_ � _X[f]_[(] _[x, y]_[)] _[dµ][X]_[(] _[x]_[)] _[is][absolutely] integrable with respect to µY ._ 

- (iii) _We have_ 

**==> picture [278 x 51] intentionally omitted <==**

**Proof.** By taking real and imaginary parts we may assume that _f_ is real; by taking positive and negative parts we may assume that _f_ is unsigned. But then the claim follows from Tonelli’s theorem; note from (1.37) that � _X_[(] � _Y[f]_[(] _[x, y]_[)] _[dµ][Y]_[ (] _[y]_[))] _[dµ][X]_[(] _[x]_[)][is][finite,][and][so] � _Y[f]_[(] _[x, y]_[)] _[dµ][Y]_[ (] _[y]_[)] _[<][∞]_[for] _[µ][X]_[-almost][every] _[x][∈][X]_[,][and][similarly] � _X[f]_[(] _[x, y]_[)] _[dµ][X]_[(] _[x]_[)] _[ <][ ∞]_[for] _[µ][Y]_[ -almost][every] _[y][∈][Y]_[ .] □ 

**Exercise 1.7.23.** Give an example of a Borel measurable function _f_ : [0 _,_ 1][2] _→_ **R** such that the integrals �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[ dy]_[ and] �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[ dx]_ exist and are absolutely integrable for all _x ∈_ [0 _,_ 1] and _y ∈_ [0 _,_ 1] respectively, and that �[0 _,_ 1][(] �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[ dy]_[)] _[ dx]_[ and] �[0 _,_ 1][(] �[0 _,_ 1] _[f]_[(] _[x, y]_[)] _[ dy]_[)] _[ dx]_ exist and are absolutely integrable, but such that 

**==> picture [234 x 25] intentionally omitted <==**

are unequal. ( _Hint:_ adapt the example from Remark 0.0.3.) Thus we see that Fubini’s theorem fails when one drops the hypothesis that _f_ is absolutely integrable with respect to the product space. 

**Remark 1.7.22.** Despite the failure of Tonelli’s theorem in the _σ_ - finite setting, it is possible to (carefully) extend Fubini’s theorem to the non- _σ_ -finite setting, as the absolute integrability hypotheses, 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1. Measure theory** 

206 

when combined with Markov’s inequality (Exercise 1.4.36(vi)), can provide a substitute for the _σ_ -finite property. However, we will not do so here, and indeed I would recommend proceeding with extreme caution when performing any sort of interchange of integrals or invoking of product measure when one is not in the _σ_ -finite setting. 

Informally, Fubini’s theorem allows one to always interchange the order of two integrals, as long as the integrand is absolutely integrable in the product space (or its completion). In particular, specialising to Lebesgue measure, we have 

**==> picture [318 x 55] intentionally omitted <==**

By combining Fubini’s theorem with Tonelli’s theorem, we can recast the absolute integrability hypothesis: 

**Corollary 1.7.23** (Fubini-Tonelli theorem) **.** _Let_ ( _X, BX , µX_ ) _and_ ( _Y, BY , µY_ ) _be complete σ-finite measure spaces, and let f_ : _X × Y →_ **C** _be measurable with respect to BX × BY . If_ 

**==> picture [164 x 24] intentionally omitted <==**

_(note the left-hand side always exists, by Tonelli’s theorem) then f is absolutely integrable with respect to BX × BY , and in particular the conclusions of Fubini’s theorem hold. Similarly if we use_ � _Y_[(] � _X[|][f]_[(] _[x, y]_[)] _[|][ dµ][X]_[(] _[x]_[))] _[ dµ][Y]_[ (] _[y]_[)] _instead of_ � _X_[(] � _Y[|][f]_[(] _[x, y]_[)] _[|][dµ][Y]_[ )] _[dµ][X][.]_ 

The Fubini-Tonelli theorem is an indispensable tool for computing integrals. We give some basic examples below: 

**Exercise 1.7.24** (Area interpretation of integral) **.** Let ( _X, B, µ_ ) be a _σ_ -finite measure space, and let **R** be equipped with Lebesgue measure _m_ and the Borel _σ_ -algebra _B_ [ **R** ]. Show that if _f_ : _X →_ [0 _,_ + _∞_ ] is measurable if and only if the set _{_ ( _x, t_ ) _∈ X ×_ **R** : 0 _≤ t ≤ f_ ( _x_ ) _}_ is measurable in _B × B_ [ **R** ], in which case we have 

**==> picture [258 x 24] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**1.7. Outer measure, pre-measure, product measure** 

207 

Similarly if we replace _{_ ( _x, t_ ) _∈ X ×_ **R** : 0 _≤ t ≤ f_ ( _x_ ) _}_ by _{_ ( _x, t_ ) _∈ X ×_ **R** : 0 _≤ t < f_ ( _x_ ) _}_ . 

**Exercise 1.7.25** (Distribution formula) **.** Let ( _X, B, µ_ ) be a _σ_ -finite measure space, and let _f_ : _X →_ [0 _,_ + _∞_ ] be measurable. Show that 

**==> picture [224 x 25] intentionally omitted <==**

(Note that the integrand on the right-hand side is monotone and thus Lebesgue measurable.) Similarly if we replace _{x ∈ X_ : _f_ ( _x_ ) _≥ λ}_ by _{x ∈ X_ : _f_ ( _x_ ) _> λ}_ . 

**Exercise 1.7.26** (Approximations to the identity) **.** Let _P_ : **R** _[d] →_ **R**[+] be a good kernel (see Exercise 1.6.27), and let _Pt_ ( _x_ ) := _t_ 1 _[d][P]_[(] _[x] t_[)] be the associated rescaled functions. Show that if _f_ : **R** _[d] →_ **C** is absolutely integrable, that _f ∗ Pt_ converges in _L_[1] norm to _f_ as _t →_ 0. ( _Hint:_ use the density argument. You will need an upper bound on _∥f ∗ Pt∥L_ 1( **R** _d_ ) which can be obtained using Tonelli’s theorem.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Chapter 2 

## **Related articles** 

**==> picture [16 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
209<br>**----- End of picture text -----**<br>


Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

210 

## **2.1. Problem solving strategies** 

The purpose of this section is to list (in no particular order) a number of common problem solving strategies for attacking real analysis exercises such as that presented in this text. Some of these strategies are specific to real analysis type problems, but others are quite general and would be applicable to other mathematical exercises. 

**2.1.1. Split up equalities into inequalities.** If one has to show that two numerical quantities _X_ and _Y_ are equal, try proving that _X ≤ Y_ and _Y ≤ X_ separately. Often one of these will be very easy, and the other one harder; but the easy direction may still provide some clue as to what needs to be done to establish the other direction. Exercise 1.1.6(iii) is a typical problem in which this strategy can be applied. 

In a similar spirit, to show that two sets _E_ and _F_ are equal, try proving that _E ⊂ F_ and _F ⊂ E_ . See for instance the proof of Lemma 1.2.11 for a simple example of this. 

**2.1.2. Give yourself an epsilon of room.** If one has to show that _X ≤ Y_ , try proving that _X ≤ Y_ + _ε_ for any _ε >_ 0. (This trick combines well with _§_ 2.1.1.) See for instance Lemma 1.2.5 for an example of this. 

In a similar spirit: 

- if one needs to show that a quantity _X_ vanishes, try showing that _|X| ≤ ε_ for every _ε >_ 0. (Exercise 1.2.19 is a simple application of this strategy.) 

- if one wishes to show that two functions _f, g_ agree almost everywhere, try showing first that _|f_ ( _x_ ) _− g_ ( _x_ ) _| ≤ ε_ holds for almost every _x_ , or even just outside of a set of measure at most _ε_ , for any given _ε >_ 0. (See for instance the proof of Lemma 1.5.7 for an example of this.) 

- if one wants to show that a sequence _xn_ of real numbers converges to zero, try showing that lim sup _n→∞ |xn| ≤ ε_ for every _ε >_ 0. (The proof of the Lebesgue differentiation theorem, Theorem 1.6.12, is in this spirit.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

211 

Don’t be too focused on getting all your error terms adding up to exactly _ε_ - usually, as long as the final error bound consists of terms that can all be made as small as one wishes by choosing parameters in a suitable way, that is enough. For instance, an error term such as 10 _ε_ is certainly OK, or even more complicated expressions such as 10 _ε/δ_ + 4 _δ_ if one has the ability to choose _δ_ as small as one wishes, and then after _δ_ is chosen, one can then also set _ε_ as small as one wishes (in a manner that can depend on _δ_ ). 

One caveat: for finite _x_ , and any _ε >_ 0, it is true that _x_ + _ε > x_ and _x − ε < x_ , but this statement is not true when _x_ is equal to + _∞_ (or _−∞_ ). So remember to exercise some care with the epsilon of room trick when some quantities are infinite. 

See also _§_ 2.7 of _An epsilon of room, Vol. I_ . 

**2.1.3. Decompose (or approximate) a rough or general object into (or by) a smoother or simpler one.** If one has to prove something about an unbounded (or infinite measure) set, consider proving it for bounded (or finite measure) sets first if this looks easier. 

In a similar spirit: 

- If one has to prove something about a measurable set, try proving it for open, closed, compact, bounded, or elementary sets 

- If one has to prove something about a measurable function, try proving it for functions that are continuous, bounded, compactly supported, simple, absolutely integrable, etc.. 

- If one has to prove something about an infinite sum or sequence, try proving it first for finite truncations of that sum or sequence (but try to get all the bounds independent of the number of terms in that truncation, so that you can still pass to the limit!). 

- If one has to prove something about a complex-valued function, try it for real-valued functions first. 

- If one has to prove something about a real-valued function, try it for unsigned functions first. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

212 

- If one has to prove something about a simple function, try it for indicator functions 

In order to pass back to the general case from these special cases, one will have to somehow decompose the general object into a combination of special ones, or approximate general objects by special ones (or as a limit of a sequence of special objects). In the latter case, one may need an epsilon of room ( _§_ 2.1.2), and some sort of limiting analysis may be needed to deal with the errors in the approximation (it is not always enough to just “pass to the limit”, as one has to justify that the desirable properties of the approximating object are preserved in the limit). Littlewood’s principles (Section 1.3.5) and their variants are often useful for thus purpose. 

Note: one should not do this blindly, as one might then be loading on a bunch of distracting but ultimately useless hypotheses that end up being a lot less help than one might hope. But they should be kept in mind as something to try if one starts having thoughts such as “Gee, it would be nice at this point if I could assume that _f_ is continuous / real-valued / simple / unsigned / etc.”. 

In the more quantitative areas of analysis and PDE, one sees a common variant of the above technique, namely the method of _a priori estimates_ . Here, one needs to prove an estimate or inequality for all functions in a large, rough class (e.g. all rough solutions to a PDE). One can often then first prove this inequality in a much smaller (but still “dense”) class of “nice” functions, so that there is little difficulty justifying the various manipulations (e.g. exchanging integrals, sums, or limits, or integrating by parts) that one wishes to perform. Once one obtains these a priori estimates, one can then often take some sort of limiting argument to recover the general case. 

**2.1.4. If one needs to flip an upper bound to a lower bound or vice versa, look for a way to take reflections or complements.** Sometimes one needs a lower bound for some quantity, but only has techniques that give upper bounds. In some cases, though, one can “reflect” an upper bound into a lower bound (or vice versa) by replacing a set _E_ contained in some space _X_ with its complement _X\E_ , or a function _f_ with its negation _−f_ (or perhaps subtracting _f_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

213 

from some dominating function _F_ to obtain _F − f_ ). This trick works best when the objects being reflected are contained in some sort of “bounded”, “finite measure”, or “absolutely integrable” container, so that one avoids having the dangerous situation of having to subtract infinite quantities from each other. 

A typical example of this is when one deduces downward monotone convergence for sets from upward monotone convergence for sets (Exercise 1.2.11). 

## **2.1.5. Uncountable unions can sometimes be replaced by** 

**countable or finite unions.** Uncountable unions are not well-behaved in measure theory; for instance, an uncountable union of null sets need not be a null set (or even a measurable set). (On the other hand, the uncountable union of open sets remains open; this can often be important to know.) However, in many cases one can replace an uncountable union by a countable one. For instance, if one needs to prove a statement for all _ε >_ 0, then there are an uncountable number of _ε_ ’s one needs to check, which may threaten measurability; but in many cases it is enough to only work with a countable sequence of _ε_ s, such as the numbers 1 _/m_ for _m_ = 1 _,_ 2 _,_ 3 _, . . ._ . (Exercise 1.6.30 relies heavily on this trick.) 

In a similar spirit, given a real parameter _λ_ , this parameter initially ranges over uncountably many values, but in some cases one can get away with only working with a countable set of such values, such as the rationals. In a similar spirit, rather than work with all boxes (of which there are uncountably many), one might work with the dyadic boxes (of which there are only countably many; also, they obey nicer nesting properties than general boxes and so are often desirable to work with in any event). 

If you are working on a compact set, then one can often replace even uncountable unions with finite ones, so long as one is working with open sets. (The proof of Theorem 1.6.20 is a good example of this strategy.) When this option is available, it is often worth spending an epsilon of measure (or whatever other resource is available to spend) to make one’s sets open, just so that one can take advantage of compactness. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

214 

## **2.1.6. If it is difficult to work globally, work locally instead.** 

A domain such as Euclidean space **R** _[d]_ has infinite measure, and this creates a number of technical difficulties when trying to do measure theory directly on such spaces. Sometimes it is best to work more locally, for instance working on a large ball _B_ (0 _, R_ ) or even a small ball such as _B_ ( _x, ε_ ) first, and then figuring out how to patch things together later. Compactness (or the closely related property of total boundedness) is often useful for patching together small balls to cover a large ball. Patching together large balls into the whole space tends to work well when the properties one are trying to establish are local in nature (such as continuity, or pointwise convergence) or behave well with respect to countable unions. For instance, to prove that a sequence of functions _fn_ converges pointwise almost everywhere to _f_ on **R** _[d]_ , it suffices to verify this pointwise almost everywhere convergence on the ball _B_ (0 _, R_ ) for every _R >_ 0 (which one can take to be an integer to get countability, see _§_ 2.1.5). The application of vertical truncation (as done, for instance, in the proof of Corollary 1.3.14) is an instance of this idea. 

**2.1.7. Be willing to throw away an exceptional set.** The “Lebesgue philosophy” to measure theory is that null sets are often “irrelevant”, and so one should be very willing to cut out a set of measure zero on which bad things are happening (e.g. a function is undefined or infinite, a sequence of functions is not converging, etc.). One should also be only slightly less willing to throw away sets of positive but small measure, e.g. sets of measure at most _ε_ . If such sets can be made arbitrarily small in measure, this is often almost as good as just throwing away a null set. 

Many things in measure theory improve after throwing away a small set. The most notable examples of this are Egorov’s theorem (Theorem 1.3.26) and Lusin’s theorem (Theorem 1.3.28); see also Exercise 1.3.25 for some other examples of this idea. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

215 

It is also common to see a similar trick[1] of throwing away most of a sequence and working with a subsequence instead. See _§_ 2.1.17 below. 

**2.1.8. Draw pictures and try to build counterexamples.** Measure theory, particularly on Euclidean spaces, has a significant geometric aspect to it, and you should be exploiting your geometric intuition. Drawing pictures and graphs of all the objects being studied is a good way to start. These pictures need not be completely realistic; they should be just complicated enough to hint at the complexities of the problem, but not more. For instance, usually one- or twodimensional pictures suffice for understanding problems in **R** _[d]_ ; drawing intricate 3D (or 4D, etc.) pictures does not often make things simpler. To indicate that a function is not continuous, one or two discontinuities or oscillations might suffice; make it too ornate and it becomes less clear what to do about that function. One should view these pictures as providing a “cartoon sketch” of the situation, which exaggerates key features and downplays others, rather than a photorealistic image of the situation; too much detail or accuracy in a picture may be a waste of time, or otherwise counterproductive. 

A common mistake is to try to draw a picture in which _both_ the hypotheses _and_ conclusion of the problem hold. This is actually not all that useful, as it often does not reveal the causal relationship between the former and the latter. One should try instead to draw a picture in which the hypotheses hold but for which the conclusion does not - in other words, a counterexample to the problem. Of course, you should be expected to fail at this task, given that the statement of the problem is presumably true. However, the way in which your picture fails to accomplish this task is often very instructive, and can reveal vital clues as to how the solution to the problem is supposed to proceed. 

I have deliberately avoided drawing pictures in this book. This is not because I feel that pictures are not useful - far from it - but because I have found that it is far more informative for a reader 

> 1This trick can also be interpreted as “throwing away a small set”, but to understand what “small” means in this context, one needs the language of _ultrafilters_ , which will not be discussed here; see [ **Ta2008** , _§_ 1.5] for a discussion. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

216 

to draw his or her own pictures of a given mathematical situation, rather than rely on the author’s images (except in situations where the geometric situation is particularly complicated or subtle), as such pictures will naturally be adapted to the reader’s mindset rather than the author’s. Besides, the process of actually _drawing_ the picture is at least as instructive as the picture itself. 

**2.1.9. Try simpler cases first.** This advice of course extends well beyond measure theory, but if one is completely stuck on a problem, try making the problem simpler (while still capturing at least one of the difficulties of the problem that you cannot currently resolve). For instance, if faced with a problem in **R** _[d]_ , try the one-dimensional case _d_ = 1 first. Faced with a problem about a general measurable function _f_ , try a much simpler case first, such as an indicator function _f_ = 1 _E_ . Faced with a problem about a general measurable set, try an elementary set first. Faced with a problem about a sequence of functions, try a monotone sequence of functions first. And so forth. (Note that this trick overlaps quite a bit with _§_ 2.1.3.) 

The problem should not be made so simple that it becomes trivial, as this doesn’t really gain you any new insight about the original problem; instead, one should try to keep the “essential” difficulties of the problem while throwing away those aspects that you think are less important (but are still serving to add to the overall difficulty level). 

On the other hand, if the simplified problem is unexpectedly easy, but one cannot extend the methods to the general case (or somehow leverage the simplified case to the general case, as in _§_ 2.1.3), this is an indication that the true difficulty lies elsewhere. For instance, if a problem involving general functions could be solved easily for monotone functions, but one cannot then extend that argument to the general case, this suggests that the true enemy is oscillation, and perhaps one should try another simple case in which the function is allowed to be highly oscillatory (but perhaps simple in other ways, e.g. bounded with compact support). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

217 

## **2.1.10. Abstract away any information that you believe or** 

**suspect to be irrelevant.** Sometimes one is faced with an embarrassment of riches when it comes to what choice of technique to use on a problem; there are so many different facts that one knows about the problem, and so many different pieces of theory that one could apply, that one doesn’t quite know where to begin. 

When this happens, abstraction can be a vital tool to clear away some of the conceptual clutter. Here, one wants to “forget” part of the setting that the problem is phrased in, and only keep the part that seems to be most relevant to the hypotheses and conclusions of the problem (and thus, presumably, to the solution as well). 

For instance, if one is working in a problem that is set in Euclidean space **R** _[d]_ , but the hypotheses and conclusions only involve measure-theoretic concepts (e.g. measurability, integrability, measure, etc.) rather than topological structure, metric structure, etc., then it may be worthwhile to try abstracting the problem to the more general setting of an abstract measure space, thus forgetting that one was initially working in **R** _[d]_ . The point of doing this is that it cuts down on the number of possible ways to start attacking the problem. For instance, facts such as outer regularity (every measurable set can be approximated from above by an open set) do not hold in abstract measure spaces (which do not even have a meaningful notion of an open set), and so presumably will not play a role in the solution; similarly for any facts involving boxes. Instead, one should be trying to use general facts about measure, such as countable additivity, which are not specific to **R** _[d]_ . 

**Remark 2.1.1.** It is worth noting that sometimes this abstraction method does not always work; for instance, when viewed as a measure space, **R** _[d]_ is not completely arbitrary, but does have one or two features that distinguish it from a generic measure space, most notably the fact that it is _σ_ -finite. So, even if the hypotheses and conclusion of a problem about **R** _[d]_ is purely measure-theoretic in nature, one may still need to use some measure-theoretic facts specific to **R** _[d]_ . Here, it becomes useful to know a little bit about the classification of measure spaces to have some intuition as to how “generic” a measure space such as **R** _[d]_ really is. This intuition is hard to convey at this level of 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

218 

the subject, but in general, measure spaces form a very “non-rigid” category, with very few invariants, and so it is largely true that one measure space usually behaves much the same as any other. 

Another example of abstraction: suppose that a problem involves a large number of sets (e.g. _En_ and _Fn_ ) and their measures, but that the conclusion of the problem only involves the measures _m_ ( _En_ ) _, m_ ( _Fn_ ) of the sets, rather than the sets themselves. Then one can try to abstract the sets out of the problem, by trying to write down every single relationship between the numerical quantities _m_ ( _En_ ) _, m_ ( _Fn_ ) that one can easily deduce from the given hypotheses (together with basic properties of measure, such as monotonicity or countable additivity). One can then rename these quantities (e.g. _an_ := _m_ ( _En_ ) and _bn_ := _m_ ( _Fn_ )) to ”forget” that these quantities arose from a measure-theoretic context, and then work with a purely numerical problem, in which one is starting with hypotheses on some sequences _an, bn_ of numbers and trying to deduce a conclusion about such sequences. Such a problem is often easier to solve than the original problem due to the simpler context. Sometimes, this simplified problem will end up being false, but the counterexample will often be instructive, either in indicating the need to add an additional hypothesis connecting the _an, bn_ , or to indicate that one cannot work at this level of abstraction but must introduce some additional concrete ingredient. 

Note that this trick is in many ways the antithesis of _§_ 2.1.9, because by passing to a special case, one often makes the problem more concrete, with more things that one is now able to start trying. However, the two tricks can work together. One particularly useful “advanced move” in mathematical problem solving is to first abstract the problem to a more general one, and then consider a special case of that more abstract problem which is not directly related to the original one, but is somehow simpler than the original while still capturing some of the essence of the difficulty. Attacking this alternate problem can then lead to some indirect but important ways to make progress on the original problem. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

219 

**2.1.11. Exploit Zeno’s paradox: a single epsilon can be cut up into countably many sub-epsilons.** A particularly useful fact in measure theory is that one can cut up a single epsilon into countably many pieces, for instance by using the geometric series identity 

## _ε_ = _ε/_ 2 + _ε/_ 4 + _ε/_ 8 + _. . ._ ; 

this observation arguably goes all the way back to Zeno. As such, even if one only has an epsilon of room budgeted for a problem, one can still use this budget to do a countably infinite number of things. This fact underlies many of the countable additivity and subadditivity properties in measure theory, and also makes the ability to approximate rough objects by smoother ones to be useful even when countably many rough objects need to be approximated. (Exercise 1.2.3 is a typical example in which this trick is used.) 

In general, one should be alert to this sort of trick when one has to spend an epsilon or so on an infinite number of objects. If one was forced to spend the same epsilon on each object, one would soon end up with an unacceptable loss; but if one can get away with using a different epsilon each time, then Zeno’s trick comes in very handy. 

**2.1.12. If you expand your way to a double sum, a double integral, a sum of an integral, or an integral of a sum, try interchanging the two operations.** Or, to put it another way: “The Fubini-Tonelli theorem (Corollary 1.7.23) is your friend”. Provided that one is either in the unsigned or absolutely convergent worlds, this theorem allows you to interchange sums and integrals with each other. In many cases, a double sum or integral that is difficult to sum in one direction can become easier to sum (or at least to upper bound, which is often all that one needs in analysis). In fact, if in the course of expanding an expression, you encounter such a double sum or integral, you should reflexively try interchanging the operations to see if the resulting expression looks any simpler. 

Note that in some cases the parameters in the summation may be constrained, and one may have to take a little care to sum it properly. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

220 

For instance, 

**==> picture [183 x 28] intentionally omitted <==**

interchanges (assuming that the _an,m_ are either unsigned or absolutely convergent) to 

**==> picture [77 x 28] intentionally omitted <==**

(why? try plotting the set of pairs ( _m, n_ ) that appear in both). If one is having trouble interchanging constrained sums or integrals, one solution is to re-express the constraint using indicator functions. For instance, one can rewrite the constrained sum (2.1) as the unconstrained sum 

**==> picture [100 x 28] intentionally omitted <==**

(extending the domain of _am,n_ if necessary), at which point interchanging the summations is easily accomplished. 

The following point is obvious, but bears mentioning explicitly: while the interchanging sums/integrals trick can be very powerful, one should _not_ apply it twice in a row to the same double sum or double operation, unless one is doing something genuinely non-trivial in between those two applications. So, after one exchanges a sum or integral, the next move should be something other than another exchange (unless one is dealing with a triple or higher sum or integral). 

A related move (not so commonly used in measure theory, but occurring in other areas of analysis, particularly those involving the geometry of Euclidean spaces) is to merge two sums or integrals into a single sum or integral over the product space, in order to use some additional feature of the product space (e.g. rotation symmetry) that is not readily visible in the factor spaces. The classic example of this trick is the evaluation of the gaussian integral � _−∞∞[e][−][x]_[2] _[dx]_[by] squaring it, rewriting that square as the two-dimensional gaussian integral � **R**[2] _[ e][−][x]_[2] _[−][y]_[2] _[dxdy]_[,][and][then][switching][to][polar][coordinates.] 

**2.1.13. Pointwise control, uniform control, and integrated (average) control are all partially convertible to each other.** 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

221 

There are three main ways to control functions (or sequences of functions, etc.) in analysis. Firstly, there is _pointwise control_ , in which one can control the function at every point (or almost every point), but in a non-uniform way. Then there is _uniform control_ , where one can control the function in the same way at most points (possibly throwing out a set of zero measure, or small measure). Finally, there is _integrated control_ (or control “on the average”), in which one controls the integral of a function, rather than the pointwise values of that function. 

It is important to realise that control of one type can often be partially converted to another type. Simple examples include the deduction of pointwise convergence from uniform convergence, or integrating a pointwise bound _f_ ( _x_ ) _≤ g_ ( _x_ ) to obtain an integrated bound � _f ≤_ � _g_ . Of course, these conversions are not reversible and thus lose some information; not every pointwise convergent sequence is uniformly convergent, and an integral bound does not imply a pointwise bound. However, one can partially reverse such implications if one is willing to throw away an exceptional set ( _§_ 2.1.7). For instance, Egorov’s theorem (Theorem 1.3.26) lets one convert pointwise convergence to (local) uniform convergence after throwing away an exceptional set, and Markov’s inequality (Exercise 1.4.36(vi)) lets one convert integral bounds to pointwise bounds, again after throwing away an exceptional set. 

**2.1.14. If the conclusion and hypotheses look particularly close to each other, just expand out all the definitions and follow your nose.** This trick is particularly useful when building the most basic foundations of a theory. Here, one may not need to experiment too much with generalisations, abstractions, or special cases, or try to marshall a lot of possibly relevant facts about the objects being studied: sometimes, all one has to do is go back to first principles, write out all the definitions with their epsilons and deltas, and start plugging away at the problem. 

Knowing when to just follow one’s nose, and when to instead look for a more high-level approach to a problem, can require some judgement or experience. A direct approach tends to work best when the conclusion and hypothesis already look quite similar to each other 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

222 

(e.g. they both state that a certain set or family of sets is measurable, or they both state that a certain function or family of functions is continuous, etc.). But when the conclusion looks quite different from the hypotheses (e.g. the conclusion is some sort of integral identity, and the hypotheses involve measurability or convergence properties), then one may need to use more sophisticated tools than what one can easily get from using first principles. 

**2.1.15. Don’t worry too much about exactly what** _ε_ **(or** _δ_ **, or** _N_ **, etc.) needs to be. It can usually be chosen or tweaked later if necessary.** Often in the middle of an argument, you will want to use some fact that involves a parameter, such as _ε_ , that you are completely free to choose (subject of course to reasonable constraints, such as requiring _ε_ to be positive). For instance, you may have a measurable set and decide to approximate it from above by an open set of at most _ε_ more measure. But it may not be obvious exactly what value to give this parameter _ε_ ; you have so many choices available that you don’t know which one to pick! 

In many cases, one can postpone thinking about this problem by leaving _ε_ undetermined for now, and continuing on with one’s argument, which will gradually start being decorated with _ε_ ’s all over the place. At some point, one will need _ε_ to do something (and, in the particular case of _ε_ , “doing something” almost always means “being small enough”), e.g. one may need 3 _nε_ to be less than _δ_ , where _n, δ_ are some other positive quantities in one’s problem that do not depend on _ε_ . At this point, one could now set _ε_ to be whatever is needed to get past this step in the argument, e.g. one could set _ε_ to equal _δ/_ 4 _n_ . But perhaps one still wishes to retain the freedom to set _ε_ because it might come in handy later. In that case, one sets aside the requirement “3 _nε < δ_ ” and keeps going. Perhaps a bit later on, one might need _ε_ to do something else; for instance, one might also need 5 _ε ≤_ 2 _[−][n]_ . Once one has compiled the complete “wish list” of everything one wishes one’s parameters to do, then one can finally make the decision of what value to set those parameters equal to. For instance, if the above two inequalities are the only inequalities required of _ε_ , one can choose _ε_ equal to min( _δ/_ 4 _n,_ 2 _[−][n] /_ 5). This may 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

223 

be a choice of _ε_ which was not obvious at the start of the argument, but becomes so as the argument progresses. 

There is however one big caveat when adopting this “choose parameters later” approach, which is that one needs to avoid a circular dependence of constants. For instance, it is perfectly fine to have two arbitrary parameters _ε_ and _δ_ floating around unspecified for most of the argument, until at some point you realise that you need _ε_ to be smaller than _δ_ , and so one chooses _ε_ accordingly (e.g. one sets it to equal _δ/_ 2). Or, perhaps instead one needs _δ_ to be smaller than _ε_ , and so sets _δ_ equal to _ε/_ 2. One can execute either of these two choices separately, but of course one cannot perform them simultaneously; this sets up an inconsistent circular dependency in which _ε_ needs to be defined after _δ_ is chosen, and _δ_ can only be chosen after _ε_ is fixed. So, if one is going to delay choosing a parameter such as _ε_ until later, it becomes important to mentally keep track of what objects in one’s argument depend on _ε_ , and which ones are independent of _ε_ . One can choose _ε_ in terms of the latter quantities, but one usually cannot do so in terms of the former quantities (unless one takes the care to show that the interlinked constraints between the quantities are still consistent, and thus simultaneously satisfiable). 

## **2.1.16. Once one has started to lose some constants, don’t** 

**be hesitant to lose some more.** Many techniques in analysis end up giving inequalities that are inefficient by a constant factor. For instance, any argument involving dyadic decomposition and powers of two tends to involve losses of factors of 2. When arguing using balls in Euclidean space, one sometimes loses factors involving the volume of the unit ball (although this factor often cancels itself out if one tracks it more carefully). And so forth. However, in many cases these constant factors end up being of little importance: an upper bound of 2 _ε_ or 100 _ε_ is often just as good as an upper bound of _ε_ for the purposes of analysis (cf. _§_ 2.1.15). So it is often best not to invest too much energy in carefully computing and optimising these constants; giving these constants a symbol such as _C_ , and not worrying about their exact value, is often the simplest approach. (One can also use asymptotic notation, such as _O_ (), which is very convenient to use once you know how it works.) 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

224 

Now there are some cases in which one really does not want to lose any constants at all. For instance, if one is using _§_ 2.1.1 to prove that _X_ = _Y_ , it is not enough to show that _X ≤_ 2 _Y_ and _Y ≤_ 2 _X_ ; one really needs to show _X ≤ Y_ and _Y ≤ X_ without losing any constants. (But proving _X ≤_ (1 + _ε_ ) _Y_ and _Y ≤_ (1 + _ε_ ) _X_ is OK, by _§_ 2.1.2.) But once one has already performed one step that loses a constant, there is little further to be lost by losing more; there can be a big difference between _X ≤ Y_ and _X ≤_ 2 _Y_ , but there is little difference in practice between _X ≤_ 2 _Y_ and _X ≤_ 100 _Y_ , at least for the purposes of mathematical analysis. At that stage, one should put oneself in the mental mode of thought where “constants don’t matter”, which can lead to some simplifications. For instance, if one has to estimate a sum _X_ + _Y_ of two positive quantities, one can start using such estimates as 

## max( _X, Y_ ) _≤ X_ + _Y ≤_ 2 max( _X, Y_ ) _,_ 

which says that, up to a factor of 2, _X_ + _Y_ is the same thing as max( _X, Y_ ). In some cases the latter is easier to work with (e.g. max( _X, Y_ ) _[n]_ is equal to max( _X[n] , Y[n]_ ), whereas the formula for ( _X_ + _Y_ ) _[n]_ is messier). 

## **2.1.17. One can often pass to a subsequence to improve the** 

**convergence properties.** In real analysis, one often ends up possessing a sequence of objects, such as a sequence of functions _fn_ , which may converge in some rather slow or weak fashion to a limit _f_ . Often, one can improve the convergence of this sequence by passing to a subsequence. For instance: 

- In a metric space, if a sequence _xn_ converges to a limit _x_ , then one can find a subsequence _xnj_ which converges quickly to the same limit _x_ , for instance one can ensure that _d_ ( _xnj , x_ ) _≤_ 2 _[−][j]_ (or one can replace 2 _[−][j]_ with any other positive expression depending on _j_ ). In particular, one can make � _∞j_ =1 _[d]_[(] _[x][n] j[, x]_[)][and][�] _[∞] j_ =1 _[d]_[(] _[x][n] j[, x][n] j_ +1[)][absolutely][conver-] gent, which is sometimes useful. 

- A sequence of functions that converges in _L_[1] norm or in measure can be refined to a subsequence that converges pointwise almost everywhere as well. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.1. Problem solving strategies** 

225 

- A sequence in a (sequentially) compact space may not converge at all, but some subsequence of it will always converge. 

- The pigeonhole principle: A sequence which takes only finitely many values has a subsequence that is constant. More generally, a sequence which lives in the union of finitely many sets has a subsequence that lives in just one of these sets. 

Often, the subsequence is good enough for one’s applications, and there are also a number of ways to get back from a subsequence to the original sequence, such as: 

- In a metric space, if you know that _xn_ is a Cauchy sequence, and some subsequence of _xn_ already converges to _x_ , then this drags the entire sequence with it, i.e. _xn_ converges to _x_ also. 

- The _Urysohn subsequence principle_ : in a topological space, if every subsequence of a sequence _xn_ itself has a subsequence that converges to a limit _x_ , then the entire sequence converges to _x_ . 

## **2.1.18. A real limit can be viewed as a meeting of the limit** 

**superior and limit inferior.** A sequence _xn_ of real numbers does not necessarily have a limit lim _n→∞ xn_ , but the limit superior lim sup _n→∞ xn_ := inf _N_ sup _n>N xn_ and the limit inferior lim inf _n→∞ xn_ = sup _N_ inf _n>N xn_ always exist (though they may be infinite), and can be easily defined in terms of infima and suprema. Because of this, it is often convenient to work with the lim sup and lim inf instead of a limit. For instance, to show that a limit lim _n→∞ xn_ exists, it suffices to show that 

**==> picture [114 x 16] intentionally omitted <==**

for all _ε >_ 0. In a similar spirit, to show that a sequence _xn_ of real numbers converges to zero, it suffices to show that 

**==> picture [68 x 17] intentionally omitted <==**

for all _ε >_ 0. It can be more convenient to work with lim sups and lim infs instead of limits because one does not need to worry about the issue of whether the limit exists or not, and many tools (notably Fatou’s lemma and its relatives) still work in this setting. One should 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

226 

however be cautious that lim sups and lim infs tend to have only one half of the linearity properties that limits do; for instance, lim sups are subadditive but not necessarily additive, while lim infs are superadditive but not necessarily additive. 

The proof of the monotone differentiation theorem (Theorem 1.6.25) given in the text relies quite heavily on this strategy. 

## **2.2. The Rademacher theorem** 

The Fubini-Tonelli theorem (Corollary 1.7.23) is often used in extending lower-dimensional results to higher-dimensional ones. We illustrate this by extending the one-dimensional Lipschitz differentiation theorem (Exercise 1.6.41) to higher dimensions, obtaining the _Rademacher differentiation theorem_ . 

We first recall some higher-dimensional definitions: 

**Definition 2.2.1** (Lipschitz continuity) **.** A function _f_ : _X → Y_ from one metric space ( _X, dX_ ) to another ( _Y, dY_ ) is said to be _Lipschitz continuous_ if there exists a constant _C >_ 0 such that _dY_ ( _f_ ( _x_ ) _, f_ ( _x[′]_ )) _≤ CdX_ ( _x, x[′]_ ) for all _x, x[′] ∈ X_ . (In the applications of this section, _X_ will be **R** _[d]_ and _Y_ will be **R** , with the usual metrics.) 

**Exercise 2.2.1.** Show that Lipschitz continuous functions are uniformly continuous, and hence continuous. Then give an example of a uniformly continuous function _f_ : [0 _,_ 1] _→_ [0 _,_ 1] that is not Lipschitz continuous. 

**Definition 2.2.2** (Differentiability) **.** Let _f_ : **R** _[d] →_ **R** be a function, and let _x_ 0 _∈_ **R** _[d]_ . For any _v ∈_ **R** _[d]_ , we say that _f_ is _directionally differentiable_ at _x_ 0 in the direction _v_ if the limit 

**==> picture [191 x 24] intentionally omitted <==**

exists, in which case we call _Dvf_ ( _x_ 0) the _directional derivative_ of _f_ at _x_ 0 in this direction. If _v_ = _ei_ is one of the standard basis vectors _e_ 1 _, . . . , ed_ of **R** _[d]_ , we write _Dvf_ ( _x_ 0) as _∂x∂fi_[(] _[x]_[0][),][and][refer][to][this][as] the _partial derivative_ of _f_ at _x_ 0 in the _ei_ direction. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.2. The Rademacher theorem** 

227 

We say that _f_ is _totally differentiable_ at _x_ 0 if there exists a vector _∇f_ ( _x_ 0) _∈_ **R** _[d]_ with the property that 

**==> picture [220 x 24] intentionally omitted <==**

where _v · w_ is the usual dot product on **R** _[d]_ . We refer to _∇f_ ( _x_ 0) (if it exists) as the _gradient_ of _f_ at _x_ 0. 

**Remark 2.2.3.** From the viewpoint of differential geometry, it is better to work not with the gradient vector _∇f_ ( _x_ 0) _∈_ **R** _[d]_ , but rather with the derivative covector _df_ ( _x_ 0) : **R** _[d] →_ **R** given by _df_ ( _x_ 0) : _v �→∇f_ ( _x_ 0) _· v_ . This is because one can then define the notion of total differentiability without any mention of the Euclidean dot product, which allows one to extend this notion to other manifolds in which there is no Euclidean (or more generally, Riemannian) structure. However, as we are working exclusively in Euclidean space for this application, this distinction will not be important for us. 

Total differentiability implies directional and partial differentiability, but not conversely, as the following three exercises demonstrate. 

**Exercise 2.2.2** (Total differentiability implies directional and partial differentiability) **.** Show that if _f_ : **R** _[d] →_ **R** is totally differentiable at _x_ 0, then it is directionally differentiable at _x_ 0 in each direction _v ∈_ **R** _[d]_ , and one has the formula 

(2.2) _Dvf_ ( _x_ 0) = _v · ∇f_ ( _x_ 0) _._ 

In particular, the partial derivatives _∂x∂fi[f]_[(] _[x]_[0][)][exist][for] _[i]_[=][1] _[, . . . , d]_ and 

**==> picture [230 x 25] intentionally omitted <==**

**Exercise 2.2.3** (Continuous partial differentiability implies total differentiability) **.** Let _f_ : **R** _[d] →_ **R** be such that the partial derivatives _∂f_ **[R]** _[d][→]_ **[R]**[exist][everywhere][and][are][continuous.] Then show _∂xi_[:] that _f_ is totally differentiable everywhere, which in particular implies that the gradient is given by the formula (2.3) and the directional derivatives are given by (2.2). 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

228 

**Exercise 2.2.4** (Directional differentiability does not imply total differentiability) **.** Let _f_ : **R**[2] _→_ **R** be defined by setting _f_ (0 _,_ 0) := 0 and _f_ ( _x_ 1 _, x_ 2) := _xx_[2] 11[+] _x[x]_[2] 2[2] 2[for][(] _[x]_[1] _[, x]_[2][)] _[∈]_ **[R]**[2] _[\{]_[(0] _[,]_[ 0)] _[}]_[.][Show][that][the][direc-] tional derivatives _Dvf_ ( _x_ ) exist for all _x, v ∈_ **R**[2] (so in particular, the partial derivatives exist), but that _f_ is not totally differentiable at the origin (0 _,_ 0). 

## Now we can state the _Rademacher differentiation theorem_ . 

**Theorem 2.2.4** (Rademacher differentiation theorem) **.** _Let f_ : **R** _[d] →_ **R** _be Lipschitz continuous. Then f is totally differentiable at x_ 0 _for almost every x_ 0 _∈_ **R** _[d] ._ 

Note that the _d_ = 1 case of this theorem is Exercise 1.6.41, and indeed we will use the one-dimensional theorem to imply the higherdimensional one, though there will be some technical issues due to the gap between directional and total differentiability. 

**Proof.** The strategy here is to first aim for the more modest goal of directional differentiability, and then find a way to link the directional derivatives together to get total differentiability. 

Let _v, x_ 0 _∈_ **R** _[d]_ . As _f_ is continuous, we see that in order for the directional derivative 

**==> picture [191 x 23] intentionally omitted <==**

to exist, it suffices to let _h_ range in the dense subset **Q** _\{_ 0 _}_ of **R** _\{_ 0 _}_ for the purposes of determing whether the limit exists. In particular, _Dvf_ ( _x_ 0) exists if and only if 

**==> picture [294 x 26] intentionally omitted <==**

From this we easily conclude that for each direction _v ∈_ **R** _[d]_ , the set 

**==> picture [184 x 12] intentionally omitted <==**

is Lebesgue measurable in **R** _[d]_ (indeed, it is even Borel measurable). A similar argument reveals that _Dvf_ is a measurable function outside of _Ev_ . From the Lipschitz nature of _f_ , we see that _Dvf_ is also a bounded function. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.2. The Rademacher theorem** 

229 

Now we claim that _Ev_ is a null set for each _v_ . For _v_ = 0 _Ev_ is clearly empty, so we may assume _v_ = 0. Applying an invertible linear transformation to map _v_ to _e_ 1 (noting that such transformations will map Lipschitz functions to Lispchitz functions, and null sets to null sets) we may assume without loss of generality that _v_ is the basis _∂f_ vector _e_ 1. Thus our task is now to show that _∂x_ 1[(] _[x]_[) exists for almost] every _x ∈_ **R** _[d]_ . 

We now split **R** _[d]_ as **R** _×_ **R** _[d][−]_[1] . For each _x_ 0 _∈_ **R** and _y_ 0 _∈_ **R** _[d][−]_[1] , we see from the definitions that _∂x∂f_ 1[(] _[x]_[0] _[, y]_[0][)][exists][if][and][only][if][the] one-dimensional function _x �→ f_ ( _x, y_ 0) is differentiable at _x_ 0. But this function is Lipschitz continuous (this is inherited from the Lipschitz continuity of _f_ ), and so we see that for each fixed _y_ 0 _∈_ **R** _[d][−]_[1] , the set _E[y]_[0] := _{x_ 0 _∈_ **R** : ( _x_ 0 _, y_ 0) _∈ E}_ is a null set in **R** . Applying Tonelli’s theorem for sets (Corollary 1.7.19), we conclude that _E_ is a null set as required. 

We would like to now conclude that[�] _v∈_ **R** _[d][ E][v]_[is][a][null][set,][but] there are uncountably many _v_ ’s, so this is not directly possible. However, as **Q** _[d]_ is rational, we can at least assert that _E_ :=[�] _v∈_ **Q** _[d][ E][v]_[is] a null set. In particular, for almost every _x_ 0 _∈_ **R** _[d]_ , _f_ is directionally differentiable in every rational direction _v ∈_ **Q** _[d]_ . 

Now we perform an important trick, in which we interpret the directional derivative _Dvf_ as a _weak derivative_ . We already know that _Dvf_ is almost everywhere defined, bounded and measurable. Now let _g_ : **R** _[d] →_ **R** be any function that is compactly supported and Lipschitz continuous. We investigate the integral 

**==> picture [88 x 24] intentionally omitted <==**

This integral is absolutely convergent since _Dvf_ ( _x_ ) is bounded and measurable, and _g_ ( _x_ ) is continuous and compactly supported, hence bounded. We expand this out as 

**==> picture [185 x 24] intentionally omitted <==**

Note (from the Lipschitz nature of _f_ ) that the expression _[f]_[(] _[x]_[+] _[hv] h_[)] _[−][f]_[(] _[x]_[)] _g_ ( _x_ ) is bounded uniformly in _h_ and _x_ , and is also uniformly compactly 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

230 

supported in _x_ for _h_ in a bounded set. We may thus apply the dominated convergence theorem (Theorem 1.4.49) to pull the limit out of the integral to obtain 

**==> picture [185 x 24] intentionally omitted <==**

Now, from translation invariance of the Lebesgue integral (Exercise 1.3.15) we have 

**==> picture [202 x 24] intentionally omitted <==**

and so (by the lienarity of the Lebesgue integral) we may rearrange the previous expression as 

**==> picture [184 x 24] intentionally omitted <==**

Now, as _g_ is Lipschitz, we know that _[g]_[(] _[x][−][hv] h_[)] _[−][g]_[(] _[x]_[)] is uniformly bounded and converges pointwise almost everywhere to _D−vg_ ( _x_ ) as _h →_ 0. We may thus apply the dominated convergence theorem again and end up with the _integration by parts formula_ 

**==> picture [245 x 24] intentionally omitted <==**

This formula moves the directional derivative operator _Dv_ from _f_ over to _g_ . At present, this does not look like much of an advantage, because _g_ is the same sort of function that _f_ is. However, the key point is that we can choose _g_ to be whatever we please, whereas _f_ is fixed. In particular, we can choose _g_ to be a compactly supported, _continuously differentiable_ function (such functions are Lipschitz from the fundamental theorem of calculus, as their derivatives are bounded). By Exercise 2.2.3, one has _D−vg_ = _−v · ∇g_ for such functions, and so 

**==> picture [210 x 23] intentionally omitted <==**

The right-hand side is linear in _v_ , and so the left-hand side must be linear in _v_ also. In particular, if _v_ = ( _v_ 1 _, . . . , vd_ ), then we have 

**==> picture [214 x 32] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.2. The Rademacher theorem** 

231 

If we define the gradient candidate function 

_∇f_ ( _x_ ) := ( _De_ 1 _f_ ( _x_ ) _, . . . , Dedf_ ( _x_ )) = ( _∂x[∂][f]_ 1 ( _x_ ) _, . . . , ∂x[∂][f] d_ ( _x_ )) (note that this function is well-defined almost everywhere, even though we don’t know yet whether _f_ is totally differentiable almost everywhere), we thus have 

**==> picture [148 x 24] intentionally omitted <==**

for all compactly supported, continuously differentiable _g_ . This implies (see Exercise 2.2.5 below) that _Fv_ := _Dvf − v · ∇f_ vanishes almost everywhere, thus (by countable subadditivity) we have 

**==> picture [198 x 11] intentionally omitted <==**

for almost every _x_ 0 _∈_ **R** _[d]_ and every _v ∈_ **Q** _[d]_ . 

Let _x_ 0 be such that (2.5) holds for all _v ∈_ **Q** _[d]_ . We claim that this forces _f_ to be totally differentiable at _x_ 0, which would give the claim. Let _F_ : **R** _[d] →_ **R** _[d]_ be the function 

**==> picture [176 x 11] intentionally omitted <==**

Our objective is to show that 

**==> picture [122 x 17] intentionally omitted <==**

On the other hand, we have _F_ (0) = 0, _F_ is Lipschitz, and from (2.5) we see that _DvF_ (0) = 0 for every _v ∈_ **Q** _[d]_ . 

Let _ε >_ 0, and suppose that _h ∈_ **R** _[d] \{_ 0 _}_ . Then we can write _h_ = _ru_ where _r_ := _|h|_ and _u_ := _h/|h|_ lies on the unit sphere. This _u_ need not lie in **Q** _[d]_ , but we can approximate it by some vector _v ∈_ **Q** _[d]_ with _|u − v| ≤ ε_ . Furthermore, by the total boundedness of the unit sphere, we can make _v_ lie in a finite subset _Vε_ of **Q** _[d]_ that only depends on _ε_ (and on _d_ ). 

Since _DvF_ (0) = 0 for all _v ∈ Vε_ , we see (by making _|h|_ small enough depending on _Vε_ ) that we have 

**==> picture [86 x 23] intentionally omitted <==**

for all _v ∈ Vε_ , and thus _|F_ ( _rv_ ) _| ≤ εr._ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

232 

On the other hand, from the Lipschitz nature of _F_ , we have 

_|F_ ( _ru_ ) _− F_ ( _rv_ ) _| ≤ Cr|u − v| ≤ Crε_ 

where _C_ is the Lipschitz constant of _F_ . As _h_ = _ru_ , we conclude that 

_|F_ ( _h_ ) _| ≤_ ( _C_ + 1) _rε._ 

In other words, we have shown that 

_|F_ ( _h_ ) _|/|h| ≤_ ( _C_ + 1) _ε_ 

whenever _|h|_ is sufficiently small depending on _ε_ . Letting _ε →_ 0, we obtain the claim. □ 

**Exercise 2.2.5.** Let _F_ : **R** _[d] →_ **R** be a locally integrable function with the property that � **R** _[d][ F]_[(] _[x]_[)] _[g]_[(] _[x]_[)] _[dx]_[=][0][whenever] _[g]_[is][a][com-] pactly supported, continuously differentiable function. Show that _F_ is zero almost everywhere. ( _Hint:_ if not, use the Lebesgue differentiation theorem to find a Lebesgue point _x_ 0 of _F_ for which _F_ ( _x_ 0) _̸_ = 0, then pick a _g_ which is supported in a sufficiently small neighbourhood of _x_ 0.) 

## **2.3. Probability spaces** 

In this section we isolate an important special type of measure space, namely a _probability space_ . As the name suggests, these spaces are of fundamental importance in the foundations of probability, although it should be emphasised that probability theory should _not_ be viewed as the study of probability spaces, as these are merely models for the true objects of study of that theory, namely the behaviour of random events and random variables. (See _§_ ??? of ??? for further discussion of this point. **Crossreference will be added once the remaining sections of the blog are converted to book form - T.** ) This text will however not be focused on applications to probability theory 

**Definition 2.3.1** (Probability space) **.** A _probability space_ is a measure space (Ω _, F,_ **P** ) of total measure 1: **P** (Ω) = 1. The measure **P** is known as a _probability measure_ . 

Note the change of notation: whereas measure spaces are traditionally denoted by symbols such as ( _X, B, µ_ ), probability spaces are traditionally denoted by symbols such as (Ω _, F,_ **P** ). Of course, such 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.3. Probability spaces** 

233 

notational changes have no impact on the underlying mathematical formalism, but they reflect the different cultures of measure theory and probability theory. In particular, the various components Ω, _F_ , **P** carry the following interpretations in probability theory, that are absent in other applications of measure theory: 

- (i) The space Ωis known as the _sample space_ , and is interpreted as the set of all possible _states ω ∈_ Ωthat a random system could be in. 

- (ii) The _σ_ -algebra _F_ is known as the _event space_ , and is interpreted as the set of all possible _events E ∈F_ that one can measure. 

- (iii) The measure **P** ( _E_ ) of an event is known as the _probability_ of that event. 

The various axioms of a probability space then formalise the _foundational axioms of probability_ , as set out by Kolmogorov. 

**Example 2.3.2** (Normalised measure) **.** Given any measure space ( _X, B, µ_ ) with 0 _< µ_ ( _X_ ) _<_ + _∞_ , the space ( _X, B, µ_ (1 _X_ ) _[µ]_[)][is][a][prob-] ability space. For instance, if Ωis a non-empty finite set with the discrete _σ_ -algebra 2[Ω] and the counting measure #, then the _normalised counting measure_ #Ω1[#][is][a][probability][measure][(known][as] the _(discrete) uniform probability measure_ on Ω), and (Ω _,_ 2[Ω] _,_ #Ω1[#)] is a probability space. In probability theory, this probability spaces models the act of drawing an element of the discrete set Ωuniformly at random. 

Similarly, if Ω _⊂_ **R** _[d]_ is a Lebesgue measurable set of positive finite Lebesgue measure, 0 _< m_ (Ω) _< ∞_ , then (Ω _, L_ [ **R** _[d]_ ] ⇂Ω _, m_ (Ω)1 _[m]_[⇂][Ω][)][is] a probability space. The probability measure _m_ (Ω)1 _[m]_[⇂][Ω][is][known][as] the _(continuous) uniform probability measure_ on Ω. In probability theory, this probability spaces models the act of drawing an element of the continuous set Ωuniformly at random. 

**Example 2.3.3** (Discrete and continuous probability measures) **.** If Ωis a (possibly infinite) non-empty set with the discrete _σ_ -algebra 2[Ω] , and if ( _pω_ ) _ω∈_ Ω are a collection of real numbers in [0 _,_ 1] with � _ω∈_ Ω _[p][ω]_[=][1,][then][the][probability][measure] **[P]**[defined][by] **[P]**[:=] 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

234 

� _ω∈_ Ω _[p][ω][δ][ω]_[,][or][in][other][words] 

**==> picture [72 x 23] intentionally omitted <==**

is indeed a probability measure, and (Ω _,_ 2[Ω] _,_ **P** ) is a probability space. The function _ω �→ pω_ is known as the _(discrete) probability distribution_ of the state variable _ω_ . 

Similarly, if Ωis a Lebesgue measurable subset of **R** _[d]_ of positive (and possibly infinite) measure, and _f_ : Ω _→_ [0 _,_ + _∞_ ] is a Lebesgue measurable function on Ω(where of course we restrict the Lebesgue measure space on **R** _[d]_ to Ωin the usual fashion) with �Ω _[f]_[(] _[x]_[)] _[dx]_[ = 1,] then (Ω _, L_ [ **R** _[d]_ ] ⇂Ω _,_ **P** ) is a probability space, where **P** := _mf_ is the measure 

**==> picture [176 x 24] intentionally omitted <==**

The function _f_ is known as the _(continuous) probability density_ of the state variable _ω_ . (This density is not quite unique, since one can modify it on a set of probability zero, but it is well-defined up to this ambiguity. See _§_ 1.2 of _An epsilon of room, Vol. I_ for further discussion.) 

**Exercise 2.3.1** (No translation-invariant random integer) **.** Show that there is no probability measure **P** on the integers **Z** with the discrete _σ_ -algebra 2 **[Z]** with the translation-invariance property **P** ( _E_ + _n_ ) = **P** ( _E_ ) for every event _E ∈_ 2 **[Z]** and every integer _n_ . 

**Exercise 2.3.2** (No translation-invariant random real) **.** Show that there is no probability measure **P** on the reals **R** with the Lebesgue _σ_ -algebra _L_ [ **R** ] with the translation-invariance property **P** ( _E_ + _x_ ) = **P** ( _E_ ) for every event _E ∈L_ [ **R** ] and every real _x_ . 

Many concepts in measure theory are of importance in probability theory, although the terminology is changed to reflect the different perspective on the subject. For instance, the notion of a property holding almost everywhere is now replaced with that of a property holding _almost surely_ . A measurable function is now referred to as a _random variable_ and is often denoted by symbols such as _X_ , and the integral of that function on the probability space (if the random variable is unsigned or absolutely convergent) is known as the _expectation_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.4. The Kolmogorov extension theorem** 

235 

of that random variable, and is denoted **E** ( _X_ ). Thus, for instance, the Borel-Cantelli lemma (Exercise 1.4.44) now reads as follows: given any sequence _E_ 1 _, E_ 2 _, E_ 3 _, . . ._ of events such that[�] _[∞] n_ =1 **[P]**[(] _[E][n]_[)] _[ <][ ∞]_[,][it] is almost surely true that at most finitely many of these events hold. In a similar spirit, Markov’s inequality (Exercise 1.4.36(vi)) becomes the assertion that **P** ( _X ≥ λ_ ) _≤ λ_[1] **[E]** _[X]_[for][any][non-negative][random] variable _X_ and any 0 _< λ < ∞_ . 

## **2.4. Infinite product spaces and the Kolmogorov extension theorem** 

In Section 1.7.4 we considered the product of two sets, measurable spaces, or ( _σ_ -finite) measure spaces. We now consider how to generalise this concept to products of more than two such spaces. The axioms of set theory allow us to form a Cartesian product _XA_ := � _α∈A[X][α]_[of][any][family][(] _[X][α]_[)] _[α][∈][A]_[of][sets][indexed][by][another][set] _[A]_[,] which consists of the space of all tuples _xA_ = ( _xα_ ) _α∈A_ indexed by _A_ , for which _xα ∈ Xα_ for all _α ∈ A_ . This concept allows for a succinct formulation of the _axiom of choice_ (Axiom 0.0.4), namely that an arbitrary Cartesian product of non-empty sets remains non-empty. 

For any _β ∈ A_ , we have the coordinate projection maps _πβ_ : _XA → Xβ_ defined by _πβ_ (( _xα_ ) _α∈A_ ) := _xβ_ . More generally, given any _B ⊂ A_ , we define the partial projections _πB_ : _XA → XB_ to the partial product space _XB_ :=[�] _α∈B[X][α]_[by] _[π][B]_[((] _[x][α]_[)] _[α][∈][A]_[)][:=][(] _[x][α]_[)] _[α][∈][B]_[.][More] generally still, given two subsets _C ⊂ B ⊂ A_ , we have the partial subprojections _πC←B_ : _XB → XC_ defined by _πC←B_ (( _xα_ ) _α∈B_ ) := ( _xα_ ) _α∈C_ . These partial subprojections obey the composition law _πD←C ◦ πC←B_ := _πD←B_ for all _D ⊂ C ⊂ B ⊂ A_ (and thus form a very simple example of a _category_ ). 

As before, given any _σ_ -algebra _Bβ_ on _Xβ_ , we can pull it back by _πβ_ to create a _σ_ -algebra 

**==> picture [140 x 14] intentionally omitted <==**

on _XA_ . One easily verifies that this is indeed a _σ_ -algebra. Informally, _π[∗]_[describes][those][sets][(or][“events”,][if][one][is][thinking][in][prob-] _β_[(] _[B][β]_[)] abilistic terms) that depend only on the _xβ_ coordinate of the state _xA_ = ( _xα_ ) _α∈A_ , and whose dependence on _xβ_ is _Bβ_ -measurable. We 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

236 

can then define the product _σ_ -algebra 

**==> picture [106 x 23] intentionally omitted <==**

We have a generalisation of Exercise 1.7.18: 

**Exercise 2.4.1.** Let (( _Xα, Bα_ )) _α∈A_ be a family of measurable spaces. For any _B ⊂ A_ , write _BB_ :=[�] _β∈B[B][β]_[.] 

- (1) Show that _BA_ is the coarsest _σ_ -algebra on _XA_ that makes the projection maps _πβ_ measurable morphisms for all _β ∈ A_ . 

- (2) Show that for each _B ⊂ A_ , that _πB_ is a measurable morphism from ( _XA, BA_ ) to ( _XB, BB_ ). 

- (3) If _E_ in _BA_ , show that there exists an at most countable set _B ⊂ A_ and a set _EB ∈BB_ such that _EA_ = _πB[−]_[1][(] _[E][B]_[).] Informally, this asserts that a measurable event can only depend on at most countably many of the coefficients. 

- (4) If _f_ : _XA →_ [0 _,_ + _∞_ ] is _BA_ -measurable, show that there exists an at most countable set _B ⊂ A_ and a _BB_ -measurable function _fB_ : _XB →_ [0 _,_ + _∞_ ] such that _f_ = _fB ◦ πB_ . 

- (5) If _A_ is at most countable, show that _BA_ is the _σ_ -algebra generated by the sets[�] _β∈A[E][β]_[with] _[E][β][∈B][β]_[for][all] _[β][∈][A]_[.] 

- (6) On the other hand, show that if _A_ is uncountable and the _Bα_ are all non-trivial, show that _BA_ is _not_ the _σ_ -algebra generated by sets[�] _β∈A[E][β]_[with] _[E][β][∈B][β]_[for][all] _[β][∈][A]_[.] 

- (7) If _B ⊂ A_ , _E ∈BA_ , and _xA\B ∈ XA\B_ , show that the set _ExA\B ,B_ := _{xB ∈ XB_ : ( _xB, xA\B_ ) _∈ E}_ lies in _BB_ , where we identify _XB × XA\B_ with _XA_ in the obvious manner. 

- (8) If _B ⊂ A_ , _f_ : _XA →_ [0 _,_ + _∞_ ] is _BA_ -measurable, and _xA\B ∈ XA\B_ , show that the function _fxA\B ,B_ : _xB → f_ ( _xB, xA\B_ ) is _BB_ -measurable. 

Now we consider the problem of constructing a measure _µA_ on the product space _XA_ . Any such measure _µA_ will induce _pushforward measures µB_ := ( _πB_ ) _∗µA_ on _XB_ (introduced in Exercise 1.4.38), thus 

**==> picture [110 x 12] intentionally omitted <==**

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.4. The Kolmogorov extension theorem** 

237 

for all _EB ∈BB_ . These measures obey the compatibility relation 

(2.6) ( _πC←B_ ) _∗µB_ = _µC_ 

whenever _C ⊂ B ⊂ A_ , as can be easily seen by chasing the definitions. 

One can then ask whether one can reconstruct _µA_ from just from the projections _µB_ to _finite_ subsets _B_ . This is possible in the important special case when the _µB_ (and hence _µA_ ) are probability measures, provided one imposes an additional _inner regularity_ hypothesis on the measures _µB_ . More precisely: 

**Definition 2.4.1** (Inner regularity) **.** A (metrisable) inner regular measure space ( _X, B, µ, d_ ) is a measure space ( _X, B, µ_ ) equipped with a metric _d_ such that 

- (1) Every compact set is measurable; and 

- (2) One has _µ_ ( _E_ ) = sup _K⊂E,K_ compact _µ_ ( _K_ ) for all measurable _E_ . 

We say that _µ_ is _inner regular_ if it is associated to an inner regular measure space. 

Thus for instance Lebesgue measure is inner regular, as are Dirac measures and counting measures. Indeed, most measures that one actually encounters in applications will be inner regular. For instance, any finite Borel measure on **R** _[d]_ (or more generally, on a locally compact, _σ_ -compact space) is inner regular, as is any _Radon measure_ ; see _§_ 1.10 of _An epsilon of room, Vol. I_ . 

**Remark 2.4.2.** One can generalise the concept of an inner regular measure space to one which is given by a topology rather than a metric; Kolmogorov’s extension theorem still holds in this more general setting, but requires _Tychonoff’s theorem_ , which is discussed in _§_ 1.8 of _An epsilon of room, Vol. I_ . However, some minimal regularity hypotheses of a topological nature are needed to make the Kolmogorov extension theorem work, although this is usually not a severe restriction in practice. 

**Theorem 2.4.3** (Kolmogorov extension theorem) **.** _Let_ (( _Xα, Bα_ ) _, Fα_ ) _α∈A be a family of measurable spaces_ ( _Xα, Bα_ ) _, equipped with a topology_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

238 

_Fα. For each finite B ⊂ A, let µB be an inner regular probability measure on BB_ :=[�] _α∈B[B][α][with][the][product][topology][F][B]_[:=][�] _α∈B[F][α][,] obeying the compatibility condition_ (2.6) _whenever C ⊂ B ⊂ A are two nested finite subsets of A. Then there exists a unique probability measure µA on BA with the property that_ ( _πB_ ) _∗µA_ = _µB for all finite B ⊂ A._ 

**Proof.** Our main tool here will be the Hahn-Kolmogorov extension theorem for pre-measures (Theorem 1.7.8), combined with the HeineBorel theorem. 

Let _B_ 0 be the set of all subsets of _XA_ that are of the form _πB[−]_[1][(] _[E][B]_[)] for some finite _B ⊂ A_ and some _EB ∈BB_ . One easily verifies that this is a Boolean algebra that is contained in _BA_ . We define a function _µ_ 0 : _B_ 0 _→_ [0 _,_ + _∞_ ] by setting 

**==> picture [78 x 11] intentionally omitted <==**

whenever _E_ takes the form _πB[−]_[1][(] _[E][B]_[) for some finite] _[ B][⊂][A]_[ and] _[ E][B][∈] BB_ . Note that a set _E ∈B_ 0 may have two different representations _E_ = _πB[−]_[1][(] _[E][B]_[)][=] _[π] B[−][′]_[1][ (] _[E][B][′]_[)][for][some][finite] _[B, B][′][⊂][A]_[,][but][then][one] must have _EB_ = _πB←B∪B′_ ( _EB∪B′_ ) and _EB′_ = _πB′←B∪B′_ ( _EB∪B[′]_ ), where _EB∪B′_ := _πB∪B′_ ( _E_ ). Applying (2.6), we see that 

**==> picture [112 x 11] intentionally omitted <==**

and 

**==> picture [118 x 10] intentionally omitted <==**

and thus _µB_ ( _EB_ ) = _µB′_ ( _EB′_ ). This shows that _µ_ 0( _E_ ) is well defined. As the _µB_ are probability measures, we see that _µ_ 0( _XA_ ) = 1. 

It is not difficult to see that _µ_ 0 is finitely additive. We now claim that _µ_ 0 is a pre-measure. In other words, we claim that if _E ∈B_ 0 is the disjoint countable union _E_ =[�] _[∞] n_ =1 _[E][n]_[of][sets] _[E][n][∈B]_[0][,][then] _µ_ 0( _E_ ) =[�] _[∞] n_ =1 _[µ]_[0][(] _[E][n]_[).] 

For each _N ≥_ 1, let _FN_ := _E\_[�] _[N] n_ =1 _[E][N]_[.][Then][the] _[F][N]_[lie][in] _B_ 0, are decreasing, and are such that[�] _[∞] N_ =1 _[F][N]_[=] _[∅]_[.][By][finite][addi-] tivity (and the finiteness of _µ_ 0), we see that it suffices to show that lim _N →∞ µ_ 0( _FN_ ) = 0. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.4. The Kolmogorov extension theorem** 

239 

Suppose this is not the case, then there exists _ε >_ 0 such that _µ_ 0( _FN_ ) _> ε_ for all _N_ . As each _FN_ lies in _B_ 0, we have _FN_ = _πB[−] N_[1][(] _[G][N]_[)] for some finite sets _BN ⊂ A_ and some _BBN_ -measurable sets _GN_ . By enlarging each _BN_ as necessary we may assume that the _BN_ are increasing in _N_ . The decreasing nature of the _FN_ then gives the inclusions 

_GN_ +1 _⊂ πB[−] N_[1] _←BN_ +1[(] _[G][N]_[)] _[.]_ 

By inner regularity, one can find a compact subset _KN_ of each _GN_ such that 

**==> picture [146 x 12] intentionally omitted <==**

If we then set 

**==> picture [120 x 31] intentionally omitted <==**

then we see that each _KN[′]_[is][compact][and] 

_µBN_ ( _KN[′]_[)] _[ ≥][µ][B] N_[(] _[G][N]_[)] _[ −][ε/]_[2] _[N][≥][ε][ −][ε/]_[2] _[N][.]_ 

In particular, the sets _KN[′]_[are][non-empty.][By][construction,][we][also] have the inclusions 

**==> picture [112 x 15] intentionally omitted <==**

and thus the sets _HN_ := _πB[−] N_[1][(] _[K] N[′]_[) are decreasing in] _[ N]_[.][On the other] hand, since these sets are contained in _FN_ , we have[�] _[∞] N_ =1 _[H][N]_[=] _[ ∅]_[.] 

By the axiom of choice, we can select an element _xN ∈ HN_ from _HN_ for each _N_ . Observe that for any _N_ 0, that _πBN_ 0 ( _xN_ ) will lie in the compact set _KN[′]_ 0[whenever] _[N][≥][N]_[0][.] Applying the HeineBorel theorem repeatedly, we may thus find a subsequence _xN_ 1 _,m_ of the _xN_ for _m_ = 1 _,_ 2 _, . . ._ such that _πB_ 1( _xN_ 1 _,m_ ) converges; then we can find a further subsequence _xN_ 2 _,m_ of that subsequence such that _πB_ 2( _xN_ 2 _,m_ ), and more generally obtain nested subsequences _xNj,m_ for _m_ = 1 _,_ 2 _, . . ._ and _j_ = 1 _,_ 2 _, . . ._ such that for each _j_ = 1 _,_ 2 _, . . ._ , the sequence _m �→ πBj_ ( _xNj,m_ ) converges. 

Now we use the diagonalisation trick. Consier the sequence _xNm,m_ =: ( _ym,α_ ) _α∈A_ for _m_ = 1 _,_ 2 _, . . ._ . By construction, we see that for each _j_ , _πBj_ ( _xNm,m_ ) converges to a limit as _m →∞_ . This implies that for each _α ∈_[�] _[∞] j_ =1 _[B][j]_[,] _[y][m,α]_[converges][to][a][limit] _[y][α]_[as] _[m][ →∞]_[.][As] _[K] j[′]_[is] closed, we see that ( _yα_ ) _α∈Bj ∈ Kj[′]_[for][each] _[j]_[.][If][we][then][extend] _[y][α]_ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2. Related articles** 

240 

arbitrarily from _α ∈_[�] _[∞] j_ =1 _[B][j]_[to] _[α][∈][A]_[,][then][the][point] _[y]_[:=][(] _[y][α]_[)] _[α][∈][A]_ lies in _Hj_ for each _j_ . But this contradicts the fact that[�] _[∞] N_ =1 _[H][N]_[=] _[ ∅]_[.] This contradiction completes the proof that _µ_ 0 is a pre-measure. If we then let _µ_ be the Hahn-Kolmogorov extension of _µ_ 0, one easily verifies that _µ_ obeys all the required properties, and the uniqueness follows from Exercise 1.7.7. □ 

The Kolmogorov extension theorem is a fundamental tool in the foundations of probability theory, as it allows one to construct a probability space to hold a variety of random processes ( _Xt_ ) _t∈T_ , both in the discrete case (when the set of times _T_ is something like the integers **Z** ) and in the continuous case (when the set of times _T_ is something like **R** ). In particular, it can be used to rigorously construct a process for _Brownian motion_ , known as the _Wiener process_ . We will however not focus on this topic, which can be found in many graduate probability texts. But we will give one common special case of the Kolmogorov extension theorem, which is to construct product probability measures: 

**Theorem 2.4.4** (Existence of product measures) **.** _Let A be an arbitrary set. For each α ∈ A, let_ ( _Xα, Bα, µα_ ) _be a probability space in which Xα is a locally compact, σ-compact metric space, with Bα being its Borel σ-algebra (i.e. the σ-algebra generated by the open sets). Then there exists a unique probability measure µA_ =[�] _α∈A[µ][α] on_ ( _XA, BA_ ) := ([�] _α∈A[X][α][,]_[ �] _α∈A[B][α]_[)] _[with][the][property][that]_ 

**==> picture [116 x 23] intentionally omitted <==**

_whenever Eα ∈Bα for each α ∈ A, and one has Eα_ = _Xα for all but finitely many of the α._ 

**Proof.** We apply the Kolmogorov extension theorem to the finite product measures _µB_ :=[�] _α∈B[µ][α]_[for][finite] _[B][⊂][A]_[,][which][can][be] constructed using the machinery in Section 1.7.4. These are Borel probability measures on a locally compact, _σ_ -compact space and are thus inner regular (see _§_ 1.10 of _An epsilon of room, Vol. I_ ). The compatibility condition (2.6) can be verified from the uniqueness properties of finite product measures. □ 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**2.4. The Kolmogorov extension theorem** 

241 

**Remark 2.4.5.** This result can also be obtained from the _Riesz representation theorem_ , which is covered in _§_ 1.10 of _An epsilon of room, Vol. I_ . 

**Example 2.4.6** (Bernoulli cube) **.** Let _A_ := **N** , and for each _α ∈ A_ , let ( _Xα, Bα, µα_ ) be the two-element set _Xα_ = _{_ 0 _,_ 1 _}_ with the discrete metric (and thus discrete _σ_ -algebra) and the uniform probability measure _µα_ . Then Theorem 2.4.4 gives a probability measure _µ_ on the infinite discrete cube _XA_ := _{_ 0 _,_ 1 _}_ **[N]** , known as the (uniform) _Bernoulli measure_ on this cube. The coordinate functions _πα_ : _XA →{_ 0 _,_ 1 _}_ can then be interpreted as a countable sequence of random variables taking values in _{_ 0 _,_ 1 _}_ . From the properties of product measure one can easily check that these random variables are uniformly distributed on _{_ 0 _,_ 1 _}_ and are jointly independent[2] . Informally, Bernoulli measure allows one to model an infinite number of “coin flips”. One can replace the natural numbers here by any other index set, and have a similar construction. 

**Example 2.4.7** (Continuous cube) **.** We repeat the previous example, but replace _{_ 0 _,_ 1 _}_ with the unit interval [0 _,_ 1] (with the usual metric, the Borel _σ_ -algebra, and the uniform probability measure). This gives a probability measure on the infinite continuous cube [0 _,_ 1] **[N]** , and the coordinate functions _πα_ : _XA →_ [0 _,_ 1] can now be interpreted as jointly independent random variables, each having the uniform distribution on [0 _,_ 1]. 

**Example 2.4.8** (Independent gaussians) **.** We repeat the previous example, but now replace [0 _,_ 1] with **R** (with the usual metric, and the Borel _σ_ -algebra), and the normal probability distribution _dµα_ = ~~_√_~~ 12 _π[e][−][x]_[2] _[/]_[2] _[dx]_[ (thus] _[ µ][α]_[(] _[E]_[) =] � _E_ ~~_√_~~ 12 _π[e][−][x]_[2] _[/]_[2] _[dx]_[ for every Borel set] _[ E]_[).] This gives a probability space that supports a countable sequence of jointly independent gaussian random variables _πα_ . 

> 2A family of random variables ( _Yα_ ) _α∈A_ is said to be _jointly independent_ if one has **P** ([�] _α∈B[Y][α][∈][E][α]_[)][=][�] _α∈B_ **[P]**[(] _[Y][α][∈][E][α]_[)][for][every][finite][subset] _[B]_[of] _[A]_[and][every] collection _Eα_ of measurable sets in the range of _Yα_ . 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

## **Bibliography** 

- [BrLi1983] H. Brezis, E. Lieb, _A relation between pointwise convergence of functions and convergence of functional_ , Proc. Amer. Math. Soc. **88** (1983), 486–490. 

- [De1901] M. Dehn, _¨Uber den Rauminhalt_ , Mathematische Annalen **55** (1901), no. 3, pages 465-478. 

- [deG1981] M. de Guzm´an, Real variable methods in Fourier analysis. North-Holland Mathematics Studies, 46. Notas de Matem´atica , 75. North-Holland Publishing Co., Amsterdam-New York, 1981. 

- [Go1938] K. G¨odel, _Consistency of the axiom of choice and of the generalized continuum-hypothesis with the axioms of set theory_ , Proc. Nat. Acad. Sci. **24** (1938), 556–557. 

- [Me2003] A. Melas, _The best constant for the centered Hardy-Littlewood maximal inequality_ , Ann. of Math. **157** (2003), no. 2, 647-688. 

- [So1970] R. Solovay, _A model of set-theory in which every set of reals is Lebesgue measurable_ , Annals of Mathematics **92** (1970), 1-56. 

- [StSk2005] E. Stein, R. Shakarchi, Real analysis. Measure theory, integration, and Hilbert spaces. Princeton Lectures in Analysis, III. Princeton University Press, Princeton, NJ, 2005. 

- [StSt1983] E. Stein, J.-O. Str¨omberg, _Behavior of maximal functions in R[n] for large n_ , Ark. Mat. **21** (1983), no. 2, 259-269. 

- [Ta2008] T. Tao, Structure and Randomness: pages from year one of a mathematical blog, American Mathematical Society, Providence RI, 2008. 

243 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Bibliography** 

244 

- [Ta2009] T. Tao, Poincar´e’s Legacies: pages from year two of a mathematical blog, Vol. I, American Mathematical Society, Providence RI, 2009. 

- [Ta2010] T. Tao, An epsilon of room, Vol. I, American Mathematical Society, Providence RI, 2010. 

- [Vi1908] G. Vitali, _Sui gruppi di punti e sulle funzioni di variabili reali_ , Atti dell’Accademia delle Scienze di Torino **43** (1908), 75-92. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

## **Index** 

_Fσ_ set, 40, 87 _Gδ_ set, 40, 87 _L[p]_ norm, 119, 127 _σ_ -algebra, 85 _σ_ -compact, 85 

_σ_ -finite, 85, 196 

a priori estimate, 212 absolute continuity, 171 absolute integrability, 54, 68, 104 absolutely convergent integral, 104 almost disjoint, 28 almost dominated convergence, 112 almost everywhere, 53 almost everywhere differentiability, 131 

almost sure convergence, 116 almost uniform convergence, 116 approximation by an algebra, 95 approximation to the identity, 155, 207 

area interpretation of integral, 207 area interpretation of Lebesgue integral, 66 

area interpretation of Riemann integral, 17 atomic algebra, 82 axiom of choice, xv axiom of countable choice, xvi 

ball, 11 Banach-Tarski paradox, 3 basic jump function, 160 Bernoulli random variables, 241 Besicovitch covering lemma, 152 Bolyai-Gerwien theorem, 13 Boolean algebra, 10, 80 Borel _σ_ -algebra, 87 Borel hierarchy, 88 Borel measure, 152 Borel-Cantelli lemma, 109 bounded variation, 164 bounded variation differentiation theorem, 166 box, 5 bullet-riddled square, 13 

Cantor function, 169 Cantor set, 35, 61 Cantor’s theorem, 25 Carath´eodory measurability, 40, 181 

category of measure spaces, 96 change of variables (linear), 41, 66 change of variables (measure), 103 change of variables (series), xiii classical derivative, 131 closed dyadic cube, 29 coarsening, 80 compactness, 25 

245 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Index** 

246 

complete measure, 94 completion (measure), 94 continuity of translation, 138 continuous differentiability, 131 continuous probability distribution, 234 continuously differentiable curve, 43 convergence in _L_[1] norm, 116 convergence in _L[∞]_ norm, 116 convergence in distribution, 131 convergence in mean, 116 convergence in measure, 116 convergence in probability, 116 convolution, 140 countable additivity, 36, 92 countable subadditivity, 22, 93 Cousin’s theorem, 153 create an epsilon of room, 23, 25, 210 cumulative distribution function, 131 

Darboux integrability, 16 Darboux integral, 16 de Morgan’s laws, 33 defect version of Fatou’s lemma, 113, 130 density argument, 137 Devil’s staircase, 169 diameter, 24 differentiability, 131 Dini derivative, 156 Dirac measure, 90 directional differentiability, 226 discrete algebra, 81 discrete probability distribution, 234 discretisation, 7 distance ( _L_[1] ), 69 dominated convergence theorem, 111 dominated convergence theorem (sets), 38, 93 domination, 126 dot product, xi downward monotone convergence (sets), 38 

downwards monotone convergence, 93 Dyadic algebra, 83 dyadic cube, 12 dyadic maximal inequality, 152 dyadic mesh, 29 dyadic nesting property, 30 Egorov’s theorem, 75, 97, 123 elementary algebra, 81 elementary measure, 6 elementary set, 5 escape to horizontal infinity, 76, 106, 118 escape to vertical infinity, 106, 118, 126 escape to width infinity, 106, 118, 126 essential upper bound, 119 essentially uniform convergence, 116 Euclidean space, xi event space, 233 existence of non-measurable sets, 44 extended real, xi exterior measure, 180 

fast convergence, 124 Fatou’s lemma, 110 finite additivity, 8, 10, 23, 65, 90, 91, 99, 101 finite subadditivity, 10, 22, 91 first fundamental theorem of calculus, 135 first uncountable ordinal, 88 Fubini’s theorem, 204 Fubini-Tonelli theorem, 206 

gauge function, 153 generation of algebras, 84, 86 good kernel, 155 gradient, 227 graphs, 10 greedy algorithm, 148 

Hahn-Kolmogorov extension, 187 Hahn-Kolmogorov theorem, 185 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Index** 

247 

Hardy-Littlewood maximal inequality, 142, 146, 148, 157 heat kernel, 155 Heaviside function, 193 height (step function), 121 Heine-Borel theorem, 25 Henstock-Kurzweil integral, 177 Hilbert’s third problem, 13 homogeneity, 100 homogeneity (integral), 64, 99 homomorphism, 141 horizontal truncation, 64, 101 

inclusion-exclusion principle, 91, 99 indeterminate forms, xii indicator function, xi infinite series (absolutely summable), 47 infinite series (unsigned), xiii, 47 inner regularity, 39, 237 integration by parts, 169, 194, 230 interval, 5, 189 

Jordan algebra, 81 Jordan inner measure, 9 Jordan measurability, 9 Jordan null set, 12 Jordan outer measure, 9, 18 jump function, 160 

Kolmogorov extension theorem, 238 

Lebesgue algebra, 82 Lebesgue decomposition, 161 Lebesgue differentiation theorem, 136, 137, 146 Lebesgue exterior measure, 20 Lebesgue inner measure, 40 Lebesgue integral (absolutely integrable), 68 Lebesgue integral (unsigned), 65 Lebesgue measurability, 20 Lebesgue measurability (complex functions), 62 Lebesgue measurability (unsigned functions), 57 Lebesgue outer measure, 19 Lebesgue philosophy, 57 

Lebesgue point, 147 Lebesgue-Stieltjes measure, 189 length, xi length (intervals), 5 linearity (integral), 15, 16, 54, 55, 70, 98 Lipschitz continuity, 226 Lipschitz differentiation theorem, 167 Littlewood’s first principle, 20, 34, 40, 72 Littlewood’s second principle, 72, 77 Littlewood’s third principle, 72, 75 Littlewood-like principles, 78 local integrability, 147 locally uniform convergence, 74 lower Darboux integral, 15 lower unsigned Lebesgue integral, 63 Lusin’s theorem, 77 

Markov’s inequality, 67, 100 mean value theorem, 133 measurability (function), 95 measurability (set), 80 measurable map, 96 measurable morphism, 96 measure, 36, 92 measure space, 92 metric completion, 42 metric entropy, 12 monotone class lemma, 200 monotone convergence theorem, 107, 130 monotone convergence theorem (sets), 38, 93 monotone differentiation theorem, 156 monotonicity (integral), 15, 16, 54, 64, 97, 99, 100 monotonicity (measure), 8, 10, 21, 91 moving bump example, 76 moving bump function, 106 

noise tolerance, 56 non-atomic algebra, 83 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Index** 

248 

non-negativity (measure), 10 norm (partition), 14 notation, x null algebra, 82 null set, 32, 94 

sample space, 233 second fundamental theorem of calculus, 134, 168, 172, 175 seminorm, 69 simple function, 50 simple integral, 51, 97, 98 Solovay’s theorem, 43 space-filling curve, 43 Steinhaus theorem, 140, 153 step function, 72 strong derivative, 131 sub-null set, 94 subadditivity (integral), 64 sums of measures, 92 superadditivity, 100 superadditivity (integral), 64 support, 53 symmetric difference, 5 

outer measure, 20, 22, 180, 186 outer regularity, 30 

partial derivative, 226 piecewise constant function, 15 piecewise constant integral, 15 pointwise almost everywhere convergence, 74, 116 pointwise convergence, 73, 115 pointwise convergence (sets), 38 Poisson kernel, 155 polytope, 11 pre-measure, 185 probability, 233 probability density, 234 probability measure, 232 probability space, 232 problem of measure, 2 product _σ_ -algebra, 194, 236 product measure, 197, 240 product space, 235 pullback ( _σ_ -algebra), 194 pushforward, 103, 237 

tagged partition, 14 tail support, 121 Tonelli’s theorem, 200, 202, 203 Tonelli’s theorem (series), xiii, xv Tonelli’s theorem (sums and integrals), 109 total differentiability, 227 total variation, 164 translation (of a set in Euclidean space), 5 translation invariance, 8, 10, 41, 66 triangle inequality, 71 trivial algebra, 81 typewriter sequence, 118 

Rademacher differentiation triangle inequality, 71 theorem, 228 trivial algebra, 81 Radon measure, 191 typewriter sequence, 118 recursive description of a _σ_ -algebra, 88 uniform continuity, 171 recursive description of Boolean uniform convergence, 74, 115 algebra, 84 uniform integrability, 126 refinement, 80 uniformly almost everywhere reflection, 16, 213 convergence, 116 restriction (Boolean algebra), 82 uniqueness of antiderivative, 134 restriction (measure), 101 uniqueness of Jordan measure, 12 Riemann integrability, 14 uniqueness of Lebesgue measure, 42 Riemann integral, 14 uniqueness of the Lebesgue Riemann sum, 14 integral, 66 Riemann-Stieltjes integral, 193 uniqueness of the Riemann rising sun inequality, 146 integral, 17 rising sun lemma, 143 uniqueness of the unsigned integral, Rolle’s theorem, 132 113 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

**Index** 

249 

unsigned integral, 100 upper Darboux integral, 16 upper unsigned Lebesgue integral, 63 upward monotone convergence (sets), 37 upwards monotone convergence, 93 

vertical truncation, 64, 101 Vitali-type covering lemma, 148 volume (box), 5 

weak derivative, 229 Weierstrass function, 156 width (step function), 121 

zero measure, 90 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society 

