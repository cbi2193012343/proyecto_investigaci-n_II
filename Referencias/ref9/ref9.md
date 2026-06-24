Cambridge Series in Statistical and Probabilistic Mathematics 

Markov Chains J.R. Norris 

Markov Chains 

Cambridge Series on Statistical and Probabilistic Mathematics 

Editorial Board: 

R. Gill (Utrecht) 

B.D. Ripley (Oxford) 

S. Ross (Berkeley) 

- M. Stein (Chicago) 

- D. Williams (Bath) 

This series of high quality upper-division textbooks and expository monographs covers all areas of stochastic applicable mathematics. The topics range from pure and applied statistics to probability theory, operations research, mathematical programming, and optimzation. The books contain clear presentations of new developments in the field and also of the state of the art in classical methods. While emphasizing rigorous treatment of theoretical methods, the books contain important applications and discussions of new techniques made possible be advances in computational methods. 

## Markov Chains 

J. R. Norris University of Cambridge 

## CAMBRIDGE UNIVERSITY PRESS 

Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore, São Paulo, Delhi 

## Cambridge University Press 

32 Avenue of the Americas, New York, NY 10013-2473, USA 

www.cambridge.org Information on this title: www.cambridge.org/9780521481816 

© Cambridge University Press 1997 

This publication is in copyright. Subject to statutory exception and to the provisions of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press. 

First published 1997 First paperback edition 1998 15th printing 2009 

Printed in the United States of America 

## _A catalog record for this publication is available from the British Library._ 

_Library of Congress Cataloging in Publication Data_ 

Norris, J. R. (James R.) Markov chains / J. R. Norris. p.   cm. – (Cambridge series on statistical and probabilistic mathematics ; no. 2) Includes bibliographical references and index. ISBN 0-521-48181-3 (pbk.) 1. Markov processes.   I. Title.   II. Series. QA274.7.N67   1997 519.2'33–dc20                                                                                     96-31570 CIP 

ISBN  978-0-521-48181-6 hardback ISBN  978-0-521-63396-3 paperback 

Cambridge University Press has no responsibility for the persistence or accuracy of URLs for external or third-party Internet Web sites referred to in this publication and does not guarantee that any content on such Web sites is, or will remain, accurate or appropriate. Information regarding prices, travel timetables, and other factual information given in this work are correct at the time of first printing, but Cambridge University Press does not guarantee the accuracy of such information thereafter. 

For my parents 

## Contents 

|Preface|ix|
|---|---|
|Introduction|xiii|
|1. Discrete-time Markov chains|1|
|1.1 Defnition and basic properties|1|
|1.2 Class structure|10|
|1.3 Hitting times and absorption probabilities|12|
|1.4 Strong Markov property|19|
|1.5 Recurrence and transience|24|
|1.6 Recurrence and transience of random walks|29|
|1.7 Invariant distributions|33|
|1.8 Convergence to equilibrium|40|
|1.9 Time reversal|47|
|1.10 Ergodic theorem|52|
|1.11 Appendix: recurrence relations|57|
|1.12 Appendix: asymptotics for _n_!|5<br>8|
|2. Continuous-time Markov chains I|60|
|2.1 _Q_-matrices and their exponentials|60|
|2.2 Continuous-time random processes|67|
|2.3 Some properties of the exponential distribution|70|



|Contents|ix|
|---|---|
|2.4 Poisson processes|73|
|2.5 Birth processes|81|
|2.6 Jump chain and holding times|87|
|2.7 Explosion|90|
|2.8 Forward and backward equations|93|
|2.9 Non-minimal chains|103|
|2.10 Appendix: matrix exponentials|105|
|3. Continuous-time Markov chains II|108|
|3.1 Basic properties|108|
|3.2 Class structure|111|
|3.3 Hitting times and absorption probabilities|112|
|3.4 Recurrence and transience|114|
|3.5 Invariant distributions|117|
|3.6 Convergence to equilibrium|121|
|3.7 Time reversal|123|
|3.8 Ergodic theorem|125|
|4. Further theory|128|
|4.1 Martingales|128|
|4.2 Potential theory|134|
|4.3 Electrical networks|151|
|4.4 Brownian motion|159|
|5. Applications|170|
|5.1 Markov chains in biology|170|
|5.2 Queues and queueing networks|179|
|5.3 Markov chains in resource management|192|
|5.4 Markov decision processes|197|
|5.5 Markov chain Monte Carlo|206|
|6. Appendix: probability and measure|217|
|6.1 Countable sets and countable sums|217|
|6.2 Basic facts of measure theory|220|
|6.3 Probability spaces and expectation|222|
|6.4 Monotone convergence and Fubini’s theorem|223|
|6.5 Stopping times and the strong Markov property|224|
|6.6 Uniqueness of probabilities and independence of σ-algebras|228|
|Further reading|232|
|Index|234|



## Preface 

Markov chains are the simplest mathematical models for random phenomena evolving in time. Their simple structure makes it possible to say a great deal about their behaviour. At the same time, the class of Markov chains is rich enough to serve in many applications. This makes Markov chains the first and most important examples of random processes. Indeed, the whole of the mathematical study of random processes can be regarded as a generalization in one way or another of the theory of Markov chains. 

This book is an account of the elementary theory of Markov chains, with applications. It was conceived as a text for advanced undergraduates or master’s level students, and is developed from a course taught to undergraduates for several years. There are no strict prerequisites but it is envisaged that the reader will have taken a course in elementary probability. In particular, measure theory is not a prerequisite. 

The first half of the book is based on lecture notes for the undergraduate course. Illustrative examples introduce many of the key ideas. Careful proofs are given throughout. There is a selection of exercises, which forms the basis of classwork done by the students, and which has been tested over several years. Chapter 1 deals with the theory of discrete-time Markov chains, and is the basis of all that follows. You must begin here. The material is quite straightforward and the ideas introduced permeate the whole book. The basic pattern of Chapter 1 is repeated in Chapter 3 for continuous-time chains, making it easy to follow the development by analogy. In between, Chapter 2 explains how to set up the theory of continuous- 

Preface 

xi 

time chains, beginning with simple examples such as the Poisson process and chains with finite state space. 

The second half of the book comprises three independent chapters intended to complement the first half. In some sections the style is a little more demanding. Chapter 4 introduces, in the context of elementary Markov chains, some of the ideas crucial to the advanced study of Markov processes, such as martingales, potentials, electrical networks and Brownian motion. Chapter 5 is devoted to applications, for example to population growth, mathematical genetics, queues and networks of queues, Markov decision processes and Monte Carlo simulation. Chapter 6 is an appendix to the main text, where we explain some of the basic notions of probability and measure used in the rest of the book and give careful proofs of the few points where measure theory is really needed. 

The following paragraph is directed primarily at an instructor and assumes some familiarity with the subject. Overall, the book is more focused on the Markovian context than most other books dealing with the elementary theory of stochastic processes. I believe that this restriction in scope is desirable for the greater coherence and depth it allows. The treatment of discrete-time chains in Chapter 1 includes the calculation of transition probabilities, hitting probabilities, expected hitting times and invariant distributions. Also treated are recurrence and transience, convergence to equilibrium, reversibility, and the ergodic theorem for long-run averages. All the results are proved, exploiting to the full the probabilistic viewpoint. For example, we use excursions and the strong Markov property to obtain conditions for recurrence and transience, and convergence to equilibrium is proved by the coupling method. In Chapters 2 and 3 we proceed via the jump chain/holding time construction to treat all right-continuous, minimal continuous-time chains, and establish analogues of all the main results obtained for discrete time. No conditions of uniformly bounded rates are needed. The student has the option to take Chapter 3 first, to study the properties of continuous-time chains before the technically more demanding construction. We have left measure theory in the background, but the proofs are intended to be rigorous, or very easily made rigorous, when considered in measure-theoretic terms. Some further details are given in Chapter 6. 

It is a pleasure to acknowledge the work of colleagues from which I have benefitted in preparing this book. The course on which it is based has evolved over many years and under many hands – I inherited parts of it from Martin Barlow and Chris Rogers. In recent years it has been given by Doug Kennedy and Colin Sparrow. Richard Gibbens, Geoffrey Grim- 

xii Preface 

mett, Frank Kelly and Gareth Roberts gave expert advice at various stages. Meena Lakshmanan, Violet Lo and David Rose pointed out many typos and ambiguities. Brian Ripley and David Williams made constructive suggestions for improvement of an early version. 

I am especially grateful to David Tranah at Cambridge University Press for his suggestion to write the book and for his continuing support, and to Sarah Shea-Simonds who typeset the whole book with efficiency, precision and good humour. 

Cambridge, 1996 

James Norris 

## Introduction 

This book is about a certain sort of random process. The characteristic property of this sort of process is that it retains _no memory_ of where it has been in the past. This means that only the current state of the process can influence where it goes next. Such a process is called a _Markov process_ . We shall be concerned exclusively with the case where the process can assume only a finite or countable set of states, when it is usual to refer it as a _Markov chain_ . 

Examples of Markov chains abound, as you will see throughout the book. What makes them important is that not only do Markov chains model many phenomena of interest, but also the lack of memory property makes it possible to predict how a Markov chain may behave, and to compute probabilities and expected values which quantify that behaviour. In this book we shall present general techniques for the analysis of Markov chains, together with many examples and applications. In this introduction we shall discuss a few very simple examples and preview some of the questions which the general theory will answer. 

We shall consider chains both in _discrete time_ 

**==> picture [107 x 13] intentionally omitted <==**

and _continuous time_ 

**==> picture [80 x 14] intentionally omitted <==**

The letters _n, m, k_ will always denote integers, whereas _t_ and _s_ will refer to real numbers. Thus we write ( _Xn_ ) _n≥_ 0 for a discrete-time process and ( _Xt_ ) _t≥_ 0 for a continuous-time process. 

_Introduction_ 

xiv 

Markov chains are often best described by diagrams, of which we now give some simple examples: 

## (i) ( _Discrete time_ ) 

**==> picture [114 x 119] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>1<br>2 1<br>1<br>2<br>3 2<br>1<br>3<br>**----- End of picture text -----**<br>


You move from state 1 to state 2 with probability 1. From state 3 you move either to 1 or to 2 with equal probability 1 _/_ 2, and from 2 you jump to 3 with probability 1 _/_ 3, otherwise stay at 2. We might have drawn a loop from 2 to itself with label 2 _/_ 3. But since the total probability on jumping from 2 must equal 1, this does not convey any more information and we prefer to leave the loops out. 

(ii) ( _Continuous time_ ) 

**==> picture [116 x 18] intentionally omitted <==**

When in state 0 you wait for a random time with exponential distribution of parameter _λ ∈_ (0 _, ∞_ ), then jump to 1. Thus the density function of the waiting time _T_ is given by 

**==> picture [134 x 14] intentionally omitted <==**

We write _T ∼ E_ ( _λ_ ) for short. 

## (iii) ( _Continuous time_ ) 

**==> picture [223 x 26] intentionally omitted <==**

Here, when you get to 1 you do not stop but after another independent exponential time of parameter _λ_ jump to 2, and so on. The resulting process is called the _Poisson process of rate λ_ . 

_Introduction_ 

xv 

**==> picture [114 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 3<br>7<br>3 2<br>4<br>**----- End of picture text -----**<br>


## (iv) ( _Continuous time_ ) 

In state 3 you take two independent exponential times _T_ 1 _∼ E_ (2) and _T_ 2 _∼ E_ (4); if _T_ 1 is the smaller you go to 1 after time _T_ 1, and if _T_ 2 is the smaller you go to 2 after time _T_ 2. The rules for states 1 and 2 are as given in examples (ii) and (iii). It is a simple matter to show that the time spent in 3 is exponential of parameter 2 + 4 = 6, and that the probability of jumping from 3 to 1 is 2 _/_ (2 + 4) = 1 _/_ 3. The details are given later. 

## (v) ( _Discrete time_ ) 

**==> picture [238 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 6<br>2<br>3 1 1 1<br>1<br>3<br>2 1 3 1 4 1 5<br>1 5 5<br>0<br>**----- End of picture text -----**<br>


We use this example to anticipate some of the ideas discussed in detail in Chapter 1. The states may be partitioned into _communicating classes_ , namely _{_ 0 _}_ , _{_ 1 _,_ 2 _,_ 3 _}_ and _{_ 4 _,_ 5 _,_ 6 _}_ . Two of these classes are _closed_ , meaning that you cannot escape. The closed classes here are _recurrent_ , meaning that you return again and again to every state. The class _{_ 0 _}_ is _transient_ . The class _{_ 4 _,_ 5 _,_ 6 _}_ is _periodic_ , but _{_ 1 _,_ 2 _,_ 3 _}_ is not. We shall show how to establish the following facts by solving some simple linear equations. You might like to try from first principles. 

- (a) Starting from 0, the probability of hitting 6 is 1 _/_ 4. 

- (b) Starting from 1, the probability of hitting 3 is 1. 

- (c) Starting from 1, it takes on average three steps to hit 3. 

- (d) Starting from 1, the long-run proportion of time spent in 2 is 3 _/_ 8. 

xvi _Introduction_ 

Let us write _pij_[(] _[n]_[)] for the probability starting from _i_ of being in state _j_ after _n_ steps. Then we have: 

- (e) lim 01[= 9] _[/]_[32;] _n→∞[p]_[(] _[n]_[)] 

- (f) _p_ 04[(] _[n]_[)][does][not][converge][as] _[n][ →∞]_[;] 

- (g) lim 04 = 1 _/_ 124. ( _n_ ) _→∞[p]_[(3] _[n]_[)] 

**1** 

## Discrete-time Markov chains 

This chapter is the foundation for all that follows. Discrete-time Markov chains are defined and their behaviour is investigated. For better orientation we now list the key theorems: these are Theorems 1.3.2 and 1.3.5 on hitting times, Theorem 1.4.2 on the strong Markov property, Theorem 1.5.3 characterizing recurrence and transience, Theorem 1.7.7 on invariant distributions and positive recurrence. Theorem 1.8.3 on convergence to equilibrium, Theorem 1.9.3 on reversibility, and Theorem 1.10.2 on longrun averages. Once you understand these you will understand the basic theory. Part of that understanding will come from familiarity with examples, so a large number are worked out in the text. Exercises at the end of each section are an important part of the exposition. 

## **1.1 Definition and basic properties** 

Let _I_ be a countable set. Each _i ∈ I_ is called a _state_ and _I_ is called the _state-space_ . We say that _λ_ = ( _λi_ : _i ∈ I_ ) is a _measure_ on _I_ if 0 _≤ λi < ∞_ for all _i ∈ I_ . If in addition the _total mass_[�] _i∈I[λ][i]_[equals][1,][then][we][call] _λ_ a _distribution_ . We work throughout with a probability space (Ω _, F ,_ P). Recall that a _random variable X_ with values in _I_ is a function _X_ : Ω _→ I_ . Suppose we set 

**==> picture [174 x 12] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

2 

Then _λ_ defines a distribution, the _distribution of X_ . We think of _X_ as modelling a random state which takes the value _i_ with probability _λi_ . There is a brief review of some basic facts about countable sets and probability spaces in Chapter 6. 

We say that a matrix _P_ = ( _pij_ : _i, j ∈ I_ ) is _stochastic_ if every row ( _pij_ : _j ∈ I_ ) is a distribution. There is a one-to-one correspondence between stochastic matrices _P_ and the sort of diagrams described in the Introduction. Here are two examples: 

**==> picture [242 x 129] intentionally omitted <==**

We shall now formalize the rules for a Markov chain by a definition in terms of the corresponding matrix _P_ . We say that ( _Xn_ ) _n≥_ 0 is a _Markov chain_ with _initial distribution λ_ and _transition matrix P_ if 

- (i) _X_ 0 has distribution _λ_ ; 

- (ii) for _n ≥_ 0, conditional on _Xn_ = _i, Xn_ +1 has distribution ( _pij_ : _j ∈ I_ ) and is independent of _X_ 0 _, . . . , Xn−_ 1. 

More explicitly, these conditions state that, for _n ≥_ 0 and _i_ 1 _, . . . , in_ +1 _∈ I_ , 

**==> picture [103 x 12] intentionally omitted <==**

(ii) P( _Xn_ +1 = _in_ +1 _| X_ 0 = _i_ 1 _, . . . , Xn_ = _in_ ) = _pin in_ +1. 

We say that ( _Xn_ ) _n≥_ 0 is _Markov_ ( _λ, P_ ) for short. If ( _Xn_ )0 _≤n≤N_ is a finite sequence of random variables satisfying (i) and (ii) for _n_ = 0 _, . . . , N −_ 1, then we again say ( _Xn_ )0 _≤n≤N_ is _Markov_ ( _λ, P_ ). 

It is in terms of properties (i) and (ii) that most real-world examples are seen to be Markov chains. But mathematically the following result appears to give a more comprehensive description, and it is the key to some later calculations. 

**Theorem 1.1.1.** _A discrete-time random process_ ( _Xn_ )0 _≤n≤N is Markov_ ( _λ, P_ ) _if and only if for all i_ 1 _, . . . , iN ∈ I_ 

**==> picture [336 x 12] intentionally omitted <==**

_1.1 Definition and basic properties_ 

3 

_Proof._ Suppose ( _Xn_ )0 _≤n≤N_ is Markov( _λ, P_ ), then 

**==> picture [238 x 63] intentionally omitted <==**

On the other hand, if (1.1) holds for _N_ , then by summing both sides over _iN ∈ I_ and using[�] _j∈I[p][ij]_[=][1][we][see][that][(1.1)][holds][for] _[N][−]_[1][and,][by] induction 

**==> picture [258 x 12] intentionally omitted <==**

for all _n_ = 0 _,_ 1 _, . . . , N_ . In particular, P( _X_ 0 = _i_ 1) = _λi_ 1 and, for _n_ = 0 _,_ 1 _, . . . , N −_ 1 _,_ 

**==> picture [334 x 47] intentionally omitted <==**

**==> picture [154 x 12] intentionally omitted <==**

The next result reinforces the idea that Markov chains have no memory. We write _δi_ = ( _δij_ : _j ∈ I_ ) for the _unit mass_ at _i_ , where 

**==> picture [105 x 27] intentionally omitted <==**

**Theorem 1.1.2 (Markov property).** _Let_ ( _Xn_ ) _n≥_ 0 _be Markov_ ( _λ, P_ ) _. Then, conditional on Xm_ = _i,_ ( _Xm_ + _n_ ) _n≥_ 0 _is Markov_ ( _δi, P_ ) _and is independent of the random variables X_ 0 _, . . . , Xm._ 

_Proof._ We have to show that for any event _A_ determined by _X_ 0 _, . . . , Xm_ we have 

**==> picture [302 x 30] intentionally omitted <==**

then the result follows by Theorem 1.1.1. First consider the case of elementary events 

**==> picture [145 x 12] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

4 

In that case we have to show 

**==> picture [271 x 46] intentionally omitted <==**

which is true by Theorem 1.1.1. In general, any event _A_ determined by _X_ 0 _, . . . , Xm_ may be written as a countable disjoint union of elementary events 

**==> picture [58 x 31] intentionally omitted <==**

Then the desired identity (1.2) for _A_ follows by summing up the corresponding identities for _Ak_ . 

The remainder of this section addresses the following problem: _what is the probability that after n steps our Markov chain is in a given state?_ First we shall see how the problem reduces to calculating entries in the _n_ th power of the transition matrix. Then we shall look at some examples where this may be done explicitly. 

We regard distributions and measures _λ_ as row vectors whose components are indexed by _I_ , just as _P_ is a matrix whose entries are indexed by _I × I_ . When _I_ is finite we will often label the states 1 _,_ 2 _, . . . , N_ ; then _λ_ will be an _N_ -vector and _P_ an _N × N_ -matrix. For these objects, matrix multiplication is a familiar operation. We extend matrix multiplication to the general case in the obvious way, defining a new measure _λP_ and a new matrix _P_[2] by 

**==> picture [194 x 26] intentionally omitted <==**

We define _P[n]_ similarly for any _n_ . We agree that _P_[0] is the identity matrix _I_ , where ( _I_ ) _ij_ = _δij_ . The context will make it clear when _I_ refers to the state-space and when to the identity matrix. We write _p_[(] _ij[n]_[)] = ( _P[n]_ ) _ij_ for the ( _i, j_ ) entry in _P[n]_ . 

In the case where _λi >_ 0 we shall write P _i_ ( _A_ ) for the conditional probability P( _A | X_ 0 = _i_ ). By the Markov property at time _m_ = 0, under P _i_ , ( _Xn_ ) _n≥_ 0 is Markov( _δi, P_ ). So the behaviour of ( _Xn_ ) _n≥_ 0 under P _i_ does not depend on _λ_ . 

**==> picture [350 x 47] intentionally omitted <==**

_1.1 Definition and basic properties_ 

5 

_Proof._ (i) By Theorem 1.1.1 

**==> picture [310 x 58] intentionally omitted <==**

(ii) By the Markov property, conditional on _Xm_ = _i_ , ( _Xm_ + _n_ ) _n≥_ 0 is Markov ( _δi, P_ ), so we just take _λ_ = _δi_ in (i). 

In light of this theorem we call _p_[(] _ij[n]_[)] the _n_ - _step transition probability from i to j_ . The following examples give some methods for calculating _p_[(] _ij[n]_[)][.] 

## **Example 1.1.4** 

The most general two-state chain has transition matrix of the form 

**==> picture [106 x 27] intentionally omitted <==**

and is represented by the following diagram: 

**==> picture [148 x 42] intentionally omitted <==**

We exploit the relation _P[n]_[+1] = _P[n] P_ to write 

**==> picture [139 x 15] intentionally omitted <==**

We also know that _p_[(] 11 _[n]_[)][+] _[ p]_[(] 12 _[n]_[)][=][P][1][(] _[X][n]_[= 1][or][2)][=][1,][so][by][eliminating] _p_[(] 12 _[n]_[)][we][get][a][recurrence relation][for] _[p]_[(] 11 _[n]_[)][:] 

**==> picture [194 x 15] intentionally omitted <==**

This has a unique solution (see Section 1.11): 

**==> picture [259 x 41] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

6 

## **Example 1.1.5 (Virus mutation)** 

Suppose a virus can exist in _N_ different strains and in each generation either stays the same, or with probability _α_ mutates to another strain, which is chosen at random. What is the probability that the strain in the _n_ th generation is the same as that in the 0th? 

We could model this process as an _N_ -state chain, with _N × N_ transition matrix _P_ given by 

**==> picture [202 x 12] intentionally omitted <==**

Then the answer we want would be found by computing _p_ 11[(] _[n]_[)][.][In][fact,][in] this example there is a much simpler approach, which relies on exploiting the symmetry present in the mutation rules. 

At any time a transition is made from the initial state to another with probability _α_ , and a transition from another state to the initial state with probability _α/_ ( _N −_ 1). Thus we have a two-state chain with diagram 

**==> picture [189 x 42] intentionally omitted <==**

and by putting _β_ = _α/_ ( _N −_ 1) in Example 1.1.4 we find that the desired probability is 

**==> picture [152 x 28] intentionally omitted <==**

Beware that in examples having less symmetry, this sort of lumping together of states may not produce a Markov chain. 

## **Example 1.1.6** 

Consider the three-state chain with diagram 

**==> picture [114 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>1<br>2 1<br>3 1 2<br>2<br>**----- End of picture text -----**<br>


_1.1 Definition and basic properties_ 

7 

and transition matrix 

**==> picture [95 x 41] intentionally omitted <==**

The problem is to find a general formula for _p_ 11[(] _[n]_[)][.] 

First we compute the eigenvalues of _P_ by writing down its characteristic equation 

**==> picture [259 x 14] intentionally omitted <==**

The eigenvalues are 1 _, i/_ 2 _, −i/_ 2 and from this we deduce that _p_ 11[(] _[n]_[)][has][the] form 

**==> picture [148 x 28] intentionally omitted <==**

for some constants _a_ , _b_ and _c_ . (The justification comes from linear algebra: having distinct eigenvalues, _P_ is diagonalizable, that is, for some invertible matrix _U_ we have 

and hence 

**==> picture [180 x 99] intentionally omitted <==**

which forces _p_ 11[(] _[n]_[)][to][have][the][form][claimed.)][The][answer][we][want][is][real] and 

**==> picture [264 x 28] intentionally omitted <==**

so it makes sense to rewrite _p_ 11[(] _[n]_[)][in][the][form] 

**==> picture [194 x 28] intentionally omitted <==**

for constants _α_ , _β_ and _γ_ . The first few values of _p_ 11[(] _[n]_[)] are easy to write down, so we get equations to solve for _α_ , _β_ and _γ_ : 

**==> picture [86 x 57] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

8 

so _α_ = 1 _/_ 5, _β_ = 4 _/_ 5, _γ_ = _−_ 2 _/_ 5 and 

**==> picture [206 x 28] intentionally omitted <==**

More generally, the following method may in principle be used to find a formula for _pij_[(] _[n]_[)] for any _M_ -state chain and any states _i_ and _j_ . 

- (i) Compute the eigenvalues _λ_ 1 _, . . . , λM_ of _P_ by solving the characteristic equation. 

- (ii) If the eigenvalues are distinct then _pij_[(] _[n]_[)] has the form 

**==> picture [127 x 17] intentionally omitted <==**

for some constants _a_ 1 _, . . . , aM_ (depending on _i_ and _j_ ). If an eigenvalue _λ_ is repeated (once, say) then the general form includes the term ( _an_ + _b_ ) _λ[n]_ . 

- (iii) As roots of a polynomial with real coefficients, complex eigenvalues will come in conjugate pairs and these are best written using sine and cosine, as in the example. 

## **Exercises** 

**1.1.1** Let _B_ 1 _, B_ 2 _, . . ._ be disjoint events with[�] _[∞] n_ =1 _[B][n]_[= Ω.][Show][that][if] _[A]_ is another event and P( _A|Bn_ ) = _p_ for all _n_ then P( _A_ ) = _p_ . 

Deduce that if _X_ and _Y_ are discrete random variables then the following are equivalent: 

- (a) _X_ and _Y_ are independent; 

- (b) the conditional distribution of _X_ given _Y_ = _y_ is independent of _y_ . 

**1.1.2** Suppose that ( _Xn_ ) _n≥_ 0 is Markov ( _λ, P_ ). If _Yn_ = _Xkn_ , show that ( _Yn_ ) _n≥_ 0 is Markov ( _λ, P[k]_ ). 

**1.1.3** Let _X_ 0 be a random variable with values in a countable set _I_ . Let _Y_ 1 _, Y_ 2 _, . . ._ be a sequence of independent random variables, uniformly distributed on [0 _,_ 1]. Suppose we are given a function 

**==> picture [82 x 12] intentionally omitted <==**

and define inductively 

**==> picture [105 x 12] intentionally omitted <==**

Show that ( _Xn_ ) _n≥_ 0 is a Markov chain and express its transition matrix _P_ in terms of _G_ . Can all Markov chains be realized in this way? How would you simulate a Markov chain using a computer? 

_1.1 Definition and basic properties_ 

9 

Suppose now that _Z_ 0 _, Z_ 1 _, . . ._ are independent, identically distributed random variables such that _Zi_ = 1 with probability _p_ and _Zi_ = 0 with probability 1 _− p_ . Set _S_ 0 = 0, _Sn_ = _Z_ 1 + _. . ._ + _Zn_ . In each of the following cases determine whether ( _Xn_ ) _n≥_ 0 is a Markov chain: 

- (a) _Xn_ = _Zn_ , (b) _Xn_ = _Sn_ , 

(c) _Xn_ = _S_ 0 + _. . ._ + _Sn_ , (d) _Xn_ = ( _Sn, S_ 0 + _. . ._ + _Sn_ ). 

In the cases where ( _Xn_ ) _n≥_ 0 is a Markov chain find its state-space and transition matrix, and in the cases where it is not a Markov chain give an example where _P_ ( _Xn_ +1 = _i|Xn_ = _j, Xn−_ 1 = _k_ ) is not independent of _k_ . 

**1.1.4** A flea hops about at random on the vertices of a triangle, with all jumps equally likely. Find the probability that after _n_ hops the flea is back where it started. 

A second flea also hops about on the vertices of a triangle, but this flea is twice as likely to jump clockwise as anticlockwise. What is the probability that after _n_ hops this second flea is back where it started? [ _Recall that e[±][iπ/]_[6] = _√_ 3 _/_ 2 _± i/_ 2.] 

**1.1.5** A die is ‘fixed’ so that each time it is rolled the score cannot be the same as the preceding score, all other scores having probability 1/5. If the first score is 6, what is the probability _p_ that the _n_ th score is 6? What is the probability that the _n_ th score is 1? 

Suppose now that a new die is produced which cannot score one greater (mod 6) than the preceding score, all other scores having equal probability. By considering the relationship between the two dice find the value of _p_ for the new die. 

**1.1.6** An octopus is trained to choose object _A_ from a pair of objects _A, B_ by being given repeated trials in which it is shown both and is rewarded with food if it chooses _A_ . The octopus may be in one of three states of mind: in state 1 it cannot remember which object is rewarded and is equally likely to choose either; in state 2 it remembers and chooses _A_ but may forget again; in state 3 it remembers and chooses _A_ and never forgets. After each trial it may change its state of mind according to the transition matrix 

**==> picture [99 x 52] intentionally omitted <==**

It is in state 1 before the first trial. What is the probablity that it is in state 1 just before the ( _n_ +1)th trial ? What is the probability _Pn_ +1( _A_ ) that it chooses _A_ on the ( _n_ + 1)th trial ? 

_1. Discrete-time Markov chains_ 

10 

Someone suggests that the record of successive choices (a sequence of _A_ s and _B_ s) might arise from a two-state Markov chain with constant transition probabilities. Discuss, with reference to the value of _Pn_ +1( _A_ ) that you have found, whether this is possible. 

**1.1.7** Let ( _Xn_ ) _n≥_ 0 be a Markov chain on _{_ 1 _,_ 2 _,_ 3 _}_ with transition matrix 

**==> picture [123 x 41] intentionally omitted <==**

Calculate P( _Xn_ = 1 _|X_ 0 = 1) in each of the following cases: (a) _p_ = 1 _/_ 16, (b) _p_ = 1 _/_ 6, (c) _p_ = 1 _/_ 12. 

## **1.2 Class structure** 

It is sometimes possible to break a Markov chain into smaller pieces, each of which is relatively easy to understand, and which together give an understanding of the whole. This is done by identifying the communicating classes of the chain. 

We say that _i leads to j_ and write _i → j_ if 

**==> picture [152 x 12] intentionally omitted <==**

We say _i communicates with j_ and write _i ↔ j_ if both _i → j_ and _j → i_ . 

**Theorem 1.2.1.** _For distinct states i and j the following are equivalent:_ 

(i) _i → j;_ (ii) _pi_ 1 _i_ 2 _pi_ 2 _i_ 2 _. . . pin −_ 1 _in >_ 0 _for some states i_ 1 _, i_ 2 _, . . . , in with i_ 1 = _i and in_ = _j;_ 

(iii) _pij_[(] _[n]_[)] _>_ 0 _for some n ≥_ 0 _._ 

_Proof._ Observe that 

**==> picture [213 x 31] intentionally omitted <==**

which proves the equivalence of (i) and (iii). Also 

**==> picture [157 x 27] intentionally omitted <==**

so that (ii) and (iii) are equivalent. 

_1.3 Hitting times and absorption probabilities_ 

11 

It is clear from (ii) that _i → j_ and _j → k_ imply _i → k_ . Also _i → i_ for any state _i_ . So _↔_ satisfies the conditions for an equivalence relation on _I_ , and thus partitions _I_ into _communicating classes_ . We say that a class _C_ is _closed_ if 

**==> picture [133 x 11] intentionally omitted <==**

Thus a closed class is one from which there is no escape. A state _i_ is _absorbing_ if _{i}_ is a closed class. The smaller pieces referred to above are these communicating classes. A chain or transition matrix _P_ where _I_ is a single class is called _irreducible_ . 

As the following example makes clear, when one can draw the diagram, the class structure of a chain is very easy to find. 

## **Example 1.2.2** 

Find the communicating classes associated to the stochastic matrix 

**==> picture [146 x 77] intentionally omitted <==**

The solution is obvious from the diagram 

**==> picture [190 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 4<br>3<br>2 5 6<br>**----- End of picture text -----**<br>


the classes being _{_ 1 _,_ 2 _,_ 3 _}_ , _{_ 4 _}_ and _{_ 5 _,_ 6 _}_ , with only _{_ 5 _,_ 6 _}_ being closed. **Exercises** 

**1.2.1** Identify the communicating classes of the following transition matrix: 

**==> picture [142 x 69] intentionally omitted <==**

Which classes are closed? 

_1. Discrete-time Markov chains_ 

12 

**1.2.2** Show that every transition matrix on a finite state-space has at least one closed communicating class. Find an example of a transition matrix with no closed communicating class. 

## **1.3 Hitting times and absorption probabilities** 

Let ( _Xn_ ) _n≥_ 0 be a Markov chain with transition matrix _P_ . The _hitting time_ of a subset _A_ of _I_ is the random variable _H[A]_ : Ω _→{_ 0 _,_ 1 _,_ 2 _, . . . } ∪{∞}_ given by 

**==> picture [161 x 14] intentionally omitted <==**

where we agree that the infimum of the empty set _∅_ is _∞_ . The probability starting from _i_ that ( _Xn_ ) _n≥_ 0 ever hits _A_ is then 

**==> picture [94 x 14] intentionally omitted <==**

When _A_ is a closed class, _h[A] i_[is called the] _[ absorption][probability]_[.][The mean] time taken for ( _Xn_ ) _n≥_ 0 to reach _A_ is given by 

**==> picture [248 x 25] intentionally omitted <==**

We shall often write less formally 

**==> picture [201 x 14] intentionally omitted <==**

Remarkably, these quantities can be calculated explicitly by means of certain linear equations associated with the transition matrix _P_ . Before we give the general theory, here is a simple example. 

## **Example 1.3.1** 

Consider the chain with the following diagram: 

**==> picture [194 x 46] intentionally omitted <==**

Starting from 2, what is the probability of absorption in 4? How long does it take until the chain is absorbed in 1 or 4? 

Introduce 

**==> picture [212 x 12] intentionally omitted <==**

_1.3 Hitting times and absorption probabilities_ 

13 

Clearly, _h_ 1 = 0, _h_ 4 = 1 and _k_ 1 = _k_ 4 = 0. Suppose now that we start at 2, and consider the situation after making one step. With probability 1 _/_ 2 we jump to 1 and with probability 1 _/_ 2 we jump to 3. So 

**==> picture [188 x 14] intentionally omitted <==**

The 1 appears in the second formula because we count the time for the first step. Similarly, 

**==> picture [188 x 14] intentionally omitted <==**

Hence 

**==> picture [152 x 32] intentionally omitted <==**

So, starting from 2, the probability of hitting 4 is 1 _/_ 3 and the mean time to absorption is 2. Note that in writing down the first equations for _h_ 2 and _k_ 2 we made implicit use of the Markov property, in assuming that the chain begins afresh from its new position after the first jump. Here is a general result for hitting probabilities. 

**Theorem 1.3.2.** _The vector of hitting probabilities h[A]_ = ( _h[A] i_[:] _[i][∈][I]_[)] _[is] the minimal non-negative solution to the system of linear equations_ 

**==> picture [256 x 32] intentionally omitted <==**

( _Minimality means that if x_ = ( _xi_ : _i ∈ I_ ) _is another solution with xi ≥_ 0 _for all i, then xi ≥ hi for all i._ ) 

_Proof._ First we show that _h[A]_ satisfies (1.3). If _X_ 0 = _i ∈ A_ , then _H[A]_ = 0, so _h[A] i_[= 1.][If] _[X]_[0][=] _[ i][ ̸∈][A]_[,][then] _[H][A][≥]_[1,][so][by][the][Markov][property] 

**==> picture [210 x 15] intentionally omitted <==**

and 

**==> picture [266 x 57] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

14 

Suppose now that _x_ = ( _xi_ : _i ∈ I_ ) is any solution to (1.3). Then _h[A] i_[=] _[ x][i]_[= 1] for _i ∈ A_ . Suppose _i ̸∈ A_ , then 

**==> picture [172 x 26] intentionally omitted <==**

Substitute for _x_ to obtain _j_ 

**==> picture [282 x 64] intentionally omitted <==**

By repeated substitution for _x_ in the final term we obtain after _n_ steps 

**==> picture [290 x 45] intentionally omitted <==**

Now if _x_ is non-negative, so is the last term on the right, and the remaining terms sum to P _i_ ( _H[A] ≤ n_ ). So _xi ≥_ P _i_ ( _H[A] ≤ n_ ) for all _n_ and then 

**==> picture [211 x 18] intentionally omitted <==**

## **Example 1.3.1 (continued)** 

The system of linear equations (1.3) for _h_ = _h[{]_[4] _[}]_ are given here by 

**==> picture [160 x 31] intentionally omitted <==**

so that 

**==> picture [113 x 14] intentionally omitted <==**

and 

**==> picture [141 x 14] intentionally omitted <==**

The value of _h_ 1 is not determined by the system (1.3), but the minimality condition now makes us take _h_ 1 = 0, so we recover _h_ 2 = 1 _/_ 3 as before. Of course, the extra boundary condition _h_ 1 = 0 was obvious from the beginning 

_1.3 Hitting times and absorption probabilities_ 

15 

so we built it into our system of equations and did not have to worry about minimal non-negative solutions. 

In cases where the state-space is infinite it may not be possible to write down a corresponding extra boundary condition. Then, as we shall see in the next examples, the minimality condition is essential. 

## **Example 1.3.3 (Gamblers’ ruin)** 

Consider the Markov chain with diagram 

**==> picture [215 x 28] intentionally omitted <==**

where 0 _< p_ = 1 _− q <_ 1. The transition probabilities are 

**==> picture [39 x 11] intentionally omitted <==**

**==> picture [186 x 11] intentionally omitted <==**

Imagine that you enter a casino with a fortune of _£i_ and gamble, _£_ 1 at a time, with probability _p_ of doubling your stake and probability _q_ of losing it. The resources of the casino are regarded as infinite, so there is no upper limit to your fortune. But what is the probability that you leave broke? 

Set _hi_ = P _i_ (hit 0), then _h_ is the minimal non-negative solution to 

**==> picture [182 x 29] intentionally omitted <==**

If _p ̸_ = _q_ this recurrence relation has a general solution 

**==> picture [91 x 30] intentionally omitted <==**

(See Section 1.11.) If _p < q_ , which is the case in most successful casinos, then the restriction 0 _≤ hi ≤_ 1 forces _B_ = 0, so _hi_ = 1 for all _i_ . If _p > q_ , then since _h_ 0 = 1 we get a family of solutions 

**==> picture [148 x 34] intentionally omitted <==**

for a non-negative solution we must have _A ≥_ 0, so the minimal nonnegative solution is _hi_ = ( _q/p_ ) _[i]_ . Finally, if _p_ = _q_ the recurrence relation has a general solution 

**==> picture [60 x 11] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

16 

and again the restriction 0 _≤ hi ≤_ 1 forces _B_ = 0, so _hi_ = 1 for all _i_ . Thus, even if you find a fair casino, you are certain to end up broke. This apparent paradox is called gamblers’ ruin. 

## **Example 1.3.4 (Birth-and-death chain)** 

Consider the Markov chain with diagram 

**==> picture [341 x 27] intentionally omitted <==**

where, for _i_ = 1 _,_ 2 _, . . ._ , we have 0 _< pi_ = 1 _− qi <_ 1. As in the preceding example, 0 is an absorbing state and we wish to calculate the absorption probability starting from _i_ . But here we allow _pi_ and _qi_ to depend on _i_ . 

Such a chain may serve as a model for the size of a population, recorded each time it changes, _pi_ being the probability that we get a birth before a death in a population of size _i_ . Then _hi_ = P _i_ (hit 0) is the extinction probability starting from _i_ . 

We write down the usual system of equations 

**==> picture [188 x 29] intentionally omitted <==**

This recurrence relation has variable coefficients so the usual technique fails. But consider _ui_ = _hi−_ 1 _− hi_ , then _piui_ +1 = _qiui_ , so 

**==> picture [214 x 27] intentionally omitted <==**

where the final equality defines _γi_ . Then 

**==> picture [110 x 10] intentionally omitted <==**

so 

**==> picture [132 x 12] intentionally omitted <==**

where _A_ = _u_ 1 and _γ_ 0 = 1. At this point _A_ remains to be determined. In the case[�] _[∞] i_ =0 _[γ][i]_[=] _[ ∞]_[,][the][restriction][0] _[≤][h][i][≤]_[1][forces] _[A]_[=][0][and] _[h][i]_[=][1] for all _i_ . But if[�] _[∞] i_ =0 _[γ][i][<][ ∞]_[then][we][can][take] _[A >]_[ 0][so][long][as] 

**==> picture [177 x 12] intentionally omitted <==**

_1.3 Hitting times and absorption probabilities_ 

17 

Thus the minimal non-negative solution occurs when _A_ = �� _∞i_ =0 _[γ][i]_ � _−_ 1 and then 

**==> picture [98 x 33] intentionally omitted <==**

In this case, for _i_ = 1 _,_ 2 _, . . ._ , we have _hi <_ 1, so the population survives with positive probability. 

Here is the general result on mean hitting times. Recall that _ki[A]_ = E _i_ ( _H[A]_ ), where _H[A]_ is the first time ( _Xn_ ) _n≥_ 0 hits _A_ . We use the notation 1 _B_ for the indicator function of _B_ , so, for example, 1 _X_ 1= _j_ is the random variable equal to 1 if _X_ 1 = _j_ and equal to 0 otherwise. 

**Theorem 1.3.5.** _The vector of mean hitting times k[A]_ = ( _k[A]_ : _i ∈ I_ ) _is the minimal non-negative solution to the system of linear equations_ 

**==> picture [267 x 32] intentionally omitted <==**

_Proof._ First we show that _k[A]_ satisfies (1.4). If _X_ 0 = _i ∈ A_ , then _H[A]_ = 0, so _ki[A]_[= 0.][If] _[X]_[0][=] _[ i][ ̸∈][A]_[,][then] _[H][A][≥]_[1,][so,][by][the][Markov][property,] 

**==> picture [152 x 14] intentionally omitted <==**

and 

**==> picture [260 x 58] intentionally omitted <==**

Suppose now that _y_ = ( _yi_ : _i ∈ I_ ) is any solution to (1.4). Then _ki[A]_[=] _[ y][i]_[= 0] for _i ∈ A_ . If _i ̸∈ A_ , then 

**==> picture [247 x 94] intentionally omitted <==**

By repeated substitution for _y_ in the final term we obtain after _n_ steps 

**==> picture [358 x 27] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

18 

So, if _y_ is non-negative, 

**==> picture [178 x 14] intentionally omitted <==**

and, letting _n →∞_ , 

**==> picture [182 x 31] intentionally omitted <==**

## **Exercises** 

**1.3.1** Prove the claims (a), (b) and (c) made in example (v) of the Introduction. 

**1.3.2** A gambler has _£_ 2 and needs to increase it to _£_ 10 in a hurry. He can play a game with the following rules: a fair coin is tossed; if a player bets on the right side, he wins a sum equal to his stake, and his stake is returned; otherwise he loses his stake. The gambler decides to use a bold strategy in which he stakes all his money if he has _£_ 5 or less, and otherwise stakes just enough to increase his capital, if he wins, to _£_ 10. 

Let _X_ 0 = 2 and let _Xn_ be his capital after _n_ throws. Prove that the gambler will achieve his aim with probability 1/5. 

What is the expected number of tosses until the gambler either achieves his aim or loses his capital? 

**1.3.3** A simple game of ‘snakes and ladders’ is played on a board of nine squares. 

**==> picture [188 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
7 8 FINISH 9<br>6 5 4<br>1 2 3<br>START<br>**----- End of picture text -----**<br>


_1.4 Strong Markov property_ 

19 

At each turn a player tosses a fair coin and advances one or two places according to whether the coin lands heads or tails. If you land at the foot of a ladder you climb to the top, but if you land at the head of a snake you slide down to the tail. How many turns on average does it take to complete the game? 

What is the probability that a player who has reached the middle square will complete the game without slipping back to square 1? 

**1.3.4** Let ( _Xn_ ) _n≥_ 0 be a Markov chain on _{_ 0 _,_ 1 _, . . . }_ with transition probabilities given by 

**==> picture [312 x 29] intentionally omitted <==**

Show that if _X_ 0 = 0 then the probability that _Xn ≥_ 1 for all _n ≥_ 1 is 6 _/π_[2] . 

## **1.4 Strong Markov property** 

In Section 1.1 we proved the Markov property. This says that for each time _m_ , conditional on _Xm_ = _i_ , the process after time _m_ begins afresh from _i_ . Suppose, instead of conditioning on _Xm_ = _i_ , we simply waited for the process to hit state _i_ , at some random time _H_ . What can one say about the process after time _H_ ? What if we replaced _H_ by a more general random time, for example _H −_ 1? In this section we shall identify a class of random times at which a version of the Markov property does hold. This class will include _H_ but not _H −_ 1; after all, the process after time _H −_ 1 jumps straight to _i_ , so it does not simply begin afresh. 

A random variable _T_ : Ω _→{_ 0 _,_ 1 _,_ 2 _, . . . } ∪{∞}_ is called a _stopping time_ if the event _{T_ = _n}_ depends only on _X_ 0 _, X_ 1 _, . . . , Xn_ for _n_ = 0 _,_ 1 _,_ 2 _, . . ._ . Intuitively, by watching the process, you know at the time when _T_ occurs. If asked to stop at _T_ , you know when to stop. 

## **Examples 1.4.1** 

(a) The _first passage time_ 

**==> picture [122 x 12] intentionally omitted <==**

is a stopping time because 

**==> picture [217 x 13] intentionally omitted <==**

**==> picture [341 x 13] intentionally omitted <==**

**==> picture [230 x 14] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

20 

(c) The _last exit time_ 

**==> picture [130 x 13] intentionally omitted <==**

is not in general a stopping time because the event _{L[A]_ = _n}_ depends on whether ( _Xn_ + _m_ ) _m≥_ 1 visits _A_ or not. 

We shall show that the Markov property holds at stopping times. The crucial point is that, if _T_ is a stopping time and _B ⊆_ Ωis determined by _X_ 0 _, X_ 1 _, . . . , XT_ , then _B ∩{T_ = _m}_ is determined by _X_ 0 _, X_ 1 _, . . . , Xm_ , for all _m_ = 0 _,_ 1 _,_ 2 _, . . ._ . 

**Theorem 1.4.2 (Strong Markov property).** _Let_ ( _Xn_ ) _n≥_ 0 _be Markov_ ( _λ, P_ ) _and let T be a stopping time of_ ( _Xn_ ) _n≥_ 0 _. Then, conditional on T < ∞ and XT_ = _i,_ ( _XT_ + _n_ ) _n≥_ 0 _is Markov_ ( _δi, P_ ) _and independent of X_ 0 _, X_ 1 _, . . . , XT ._ 

_Proof._ If _B_ is an event determined by _X_ 0 _, X_ 1 _, . . . , XT_ , then _B ∩{T_ = _m}_ is determined by _X_ 0 _, X_ 1 _, . . . , Xm_ , so, by the Markov property at time _m_ 

**==> picture [336 x 29] intentionally omitted <==**

where we have used the condition _T_ = _m_ to replace _m_ by _T_ . Now sum over _m_ = 0 _,_ 1 _,_ 2 _, . . ._ and divide by P( _T < ∞, XT_ = _i_ ) to obtain 

**==> picture [306 x 29] intentionally omitted <==**

The following example uses the strong Markov property to get more information on the hitting times of the chain considered in Example 1.3.3. 

## **Example 1.4.3** 

Consider the Markov chain ( _Xn_ ) _n≥_ 0 with diagram 

**==> picture [215 x 27] intentionally omitted <==**

_1.4 Strong Markov property_ 

21 

where 0 _< p_ = 1 _− q <_ 1. We know from Example 1.3.3 the probability of hitting 0 starting from 1. Here we obtain the complete distribution of the time to hit 0 starting from 1 in terms of its probability generating function. Set 

**==> picture [124 x 12] intentionally omitted <==**

and, for 0 _≤ s <_ 1 

**==> picture [181 x 24] intentionally omitted <==**

Suppose we start at 2. Apply the strong Markov property at _H_ 1 to see that� under P2, conditional on _H_ 1 _< ∞_ , we have _H_ 0 = _H_ 1 + _H_[�] 0, where _H_ 0, the time taken after _H_ 1 to get to 0, is independent of _H_ 1 and has the (unconditioned) distribution of _H_ 1. So 

**==> picture [286 x 57] intentionally omitted <==**

Then, by the Markov property at time 1, conditional on _X_ 1 = 2, we have _H_ 0 = 1 + _H_ 0, where _H_ 0, the time taken after time 1 to get to 0, has the same distribution as _H_ 0 does under P2. So 

**==> picture [275 x 71] intentionally omitted <==**

Thus _φ_ = _φ_ ( _s_ ) satisfies 

**==> picture [222 x 14] intentionally omitted <==**

and 

**==> picture [131 x 14] intentionally omitted <==**

Since _φ_ (0) _≤_ 1 and _φ_ is continuous we are forced to take the negative root at _s_ = 0 and stick with it for all 0 _≤ s <_ 1. 

To recover the distribution of _H_ 0 we expand the square-root as a power series: 

**==> picture [310 x 62] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

22 

The first few probabilities P1( _H_ 0 = 1) _,_ P1( _H_ 0 = 2) _, . . ._ are readily checked from first principles. 

On letting _s ↑_ 1 we have _φ_ ( _s_ ) _→_ P1( _H_ 0 _< ∞_ ), so 

**==> picture [233 x 28] intentionally omitted <==**

(Remember that _q_ = 1 _− p_ , so 

**==> picture [240 x 15] intentionally omitted <==**

We can also find the mean hitting time using 

**==> picture [94 x 18] intentionally omitted <==**

It is only worth considering the case _p ≤ q_ , where the mean hitting time has a chance of being finite. Differentiate (1.5) to obtain 

**==> picture [126 x 13] intentionally omitted <==**

so 

_φ[′]_ ( _s_ ) = ( _pφ_ ( _s_ )[2] + _q_ ) _/_ (1 _−_ 2 _psφ_ ( _s_ )) _→_ 1 _/_ (1 _−_ 2 _p_ ) = 1 _/_ ( _q − p_ ) as _s ↑_ 1 _._ 

See Example 5.1.1 for a connection with branching processes. 

## **Example 1.4.4** 

We now consider an application of the strong Markov property to a Markov chain ( _Xn_ ) _n≥_ 0 observed only at certain times. In the first instance suppose that _J_ is some subset of the state-space _I_ and that we observe the chain only when it takes values in _J_ . The resulting process ( _Ym_ ) _m≥_ 0 may be obtained formally by setting _Ym_ = _XTm_ , where 

**==> picture [123 x 12] intentionally omitted <==**

and, for _m_ = 0 _,_ 1 _,_ 2 _, . . ._ 

**==> picture [150 x 11] intentionally omitted <==**

Let us assume that P( _Tm < ∞_ ) = 1 for all _m_ . For each _m_ we can check easily that _Tm_ , the time of the _m_ th visit to _J_ , is a stopping time. So the strong Markov property applies to show, for _i_ 1 _, . . . , im_ +1 _∈ J_ , that 

**==> picture [233 x 48] intentionally omitted <==**

_1.4 Strong Markov property_ 

23 

where, for _i, j ∈ J_ 

**==> picture [39 x 16] intentionally omitted <==**

and where, for _j ∈ J_ , the vector ( _h[j] i_[:] _[i][∈][I]_[)][is][the][minimal][non-negative] solution to 

**==> picture [229 x 27] intentionally omitted <==**

Thus ( _Ym_ ) _m≥_ 0 is a Markov chain on _J_ with transition matrix _P_ . 

A second example of a similar type arises if we observe the original chain ( _Xn_ ) _n≥_ 0 only when it moves. The resulting process ( _Zm_ ) _m≥_ 0 is given by _Zm_ = _XSm_ where _S_ 0 = 0 and for _m_ = 0 _,_ 1 _,_ 2 _, . . ._ 

**==> picture [166 x 12] intentionally omitted <==**

Let us assume there are no absorbing states. Again the random times _Sm_ for _m ≥_ 0 are stopping times and, by the strong Markov property 

**==> picture [234 x 47] intentionally omitted <==**

� where _pii_ = 0 and, for _i ̸_ = _j_ 

**==> picture [84 x 26] intentionally omitted <==**

Thus ( _Zm_ ) _m≥_ 0 is a Markov chain on _I_ with transition matrix _P_[�] . 

## **Exercises** 

**1.4.1** Let _Y_ 1 _, Y_ 2 _, . . ._ be independent identically distributed random variables with 

P( _Y_ 1 = 1) = P( _Y_ 1 = _−_ 1) = 1 _/_ 2 and set _X_ 0 = 1, _Xn_ = _X_ 0 + _Y_ 1 + _. . ._ + _Yn_ for _n ≥_ 1. Define 

**==> picture [130 x 11] intentionally omitted <==**

Find the probability generating function _φ_ ( _s_ ) = E( _s[H]_[0] ). Suppose the distribution of _Y_ 1 _, Y_ 2 _, . . ._ is changed to P( _Y_ 1 = 2) = 1 _/_ 2 _,_ P( _Y_ 1 = _−_ 1) = 1 _/_ 2. Show that _φ_ now satisfies 

**==> picture [86 x 13] intentionally omitted <==**

**1.4.2** Deduce carefully from Theorem 1.3.2 the claim made at (1.6). 

_1. Discrete-time Markov chains_ 

24 

## **1.5 Recurrence and transience** 

Let ( _Xn_ ) _n≥_ 0 be a Markov chain with transition matrix _P_ . We say that a state _i_ is _recurrent_ if 

**==> picture [179 x 12] intentionally omitted <==**

We say that _i_ is _transient_ if 

**==> picture [179 x 12] intentionally omitted <==**

Thus a recurrent state is one to which you keep coming back and a transient state is one which you eventually leave for ever. We shall show that every state is either recurrent or transient. 

Recall that the _first passage time_ to state _i_ is the random variable _Ti_ defined by 

**==> picture [150 x 12] intentionally omitted <==**

where inf _∅_ = _∞_ . We now define inductively the _rth passage time Ti_[(] _[r]_[)] to state _i_ by 

**==> picture [148 x 16] intentionally omitted <==**

and, for _r_ = 0 _,_ 1 _,_ 2 _, . . ._ , 

**==> picture [223 x 15] intentionally omitted <==**

The length of the _r_ th excursion to _i_ is then 

**==> picture [189 x 34] intentionally omitted <==**

The following diagram illustrates these definitions: 

**==> picture [15 x 10] intentionally omitted <==**

**==> picture [248 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
i<br>T [(0)] T [(1)] T [(2)] T [(3)] n<br>i i i i<br>Si [(1)] Si [(2)] Si [(3)] Si [(4)]<br>**----- End of picture text -----**<br>


_1.5 Recurrence and transience_ 

25 

Our analysis of recurrence and transience will rest on finding the joint distribution of these excursion lengths. 

**Lemma 1.5.1.** _For r_ = 2 _,_ 3 _, . . . , conditional on Ti_[(] _[r][−]_[1)] _< ∞, Si_[(] _[r]_[)] _is independent of {Xm_ : _m ≤ Ti_[(] _[r][−]_[1)] _} and_ 

**==> picture [190 x 16] intentionally omitted <==**

_Proof._ Apply the strong Markov property at the stopping time _T_ = _Ti_[(] _[r][−]_[1)] . It is automatic that _XT_ = _i_ on _T < ∞_ . So, conditional on _T < ∞_ , ( _XT_ + _n_ ) _n≥_ 0 is Markov( _δi, P_ ) and independent of _X_ 0 _, X_ 1 _, . . . , XT_ . But 

**==> picture [144 x 16] intentionally omitted <==**

so _Si_[(] _[r]_[)] is the first passage time of ( _XT_ + _n_ ) _n≥_ 0 to state _i_ . 

Recall that the indicator function 1 _{X_ 1= _j}_ is the random variable equal to 1 if _X_ 1 = _j_ and 0 otherwise. Let us introduce the _number of visits Vi_ to _i_ , which may be written in terms of indicator functions as 

**==> picture [80 x 31] intentionally omitted <==**

and note that 

**==> picture [343 x 31] intentionally omitted <==**

Also, we can compute the distribution of _Vi_ under P _i_ in terms of the _return probability_ 

**==> picture [82 x 11] intentionally omitted <==**

**==> picture [293 x 12] intentionally omitted <==**

_Proof._ Observe that if _X_ 0 = _i_ then _{Vi > r}_ = _{Ti_[(] _[r]_[)] _< ∞}_ . When _r_ = 0 the result is true. Suppose inductively that it is true for _r_ , then 

**==> picture [223 x 74] intentionally omitted <==**

by Lemma 1.5.1, so by induction the result is true for all _r_ . 

_1. Discrete-time Markov chains_ 

26 

Recall that one can compute the expectation of a non-negative integervalued random variable as follows: 

**==> picture [282 x 70] intentionally omitted <==**

The next theorem is the means by which we establish recurrence or transience for a given state. Note that it provides two criteria for this, one in terms of the return probability, the other in terms of the _n_ -step transition probabilities. Both are useful. 

**Theorem 1.5.3.** _The following dichotomy holds:_ 

(i) _if_ P _i_ ( _Ti < ∞_ ) = 1 _, then i is recurrent and_[�] _[∞] n_ =0 _[p] ii_[(] _[n]_[)] = _∞;_ (ii) _if_ P _i_ ( _Ti < ∞_ ) _<_ 1 _, then i is transient and_[�] _[∞] n_ =0 _[p] ii_[(] _[n]_[)] _< ∞. In particular, every state is either transient or recurrent._ 

_Proof._ If P _i_ ( _Ti < ∞_ ) = 1, then, by Lemma 1.5.2, 

**==> picture [162 x 15] intentionally omitted <==**

so _i_ is recurrent and 

**==> picture [110 x 31] intentionally omitted <==**

On the other hand, if _fi_ = P _i_ ( _Ti < ∞_ ) _<_ 1, then by Lemma 1.5.2 

**==> picture [277 x 31] intentionally omitted <==**

so P _i_ ( _Vi_ = _∞_ ) = 0 and _i_ is transient. 

From this theorem we can go on to solve completely the problem of recurrence or transience for Markov chains with finite state-space. Some cases of infinite state-space are dealt with in the following chapter. First we show that recurrence and transience are _class properties_ . 

**Theorem 1.5.4.** _Let C be a communicating class. Then either all states in C are transient or all are recurrent._ 

_Proof._ Take any pair of states _i, j ∈ C_ and suppose that _i_ is transient. There exist _n, m ≥_ 0 with _pij_[(] _[n]_[)] _>_ 0 and _p_[(] _ji[m]_[)] _>_ 0, and, for all _r ≥_ 0 

**==> picture [116 x 17] intentionally omitted <==**

_1.5 Recurrence and transience_ 

27 

so 

**==> picture [181 x 33] intentionally omitted <==**

by Theorem 1.5.3. Hence _j_ is also transient by Theorem 1.5.3. 

In the light of this theorem it is natural to speak of a recurrent or transient class. 

**Theorem 1.5.5.** _Every recurrent class is closed._ 

_Proof._ Let _C_ be a class which is not closed. Then there exist _i ∈ C_ , _j ̸∈ C_ and _m ≥_ 1 with 

**==> picture [80 x 12] intentionally omitted <==**

Since we have 

**==> picture [247 x 12] intentionally omitted <==**

this implies that 

**==> picture [176 x 12] intentionally omitted <==**

so _i_ is not recurrent, and so neither is _C_ . 

**Theorem 1.5.6.** _Every finite closed class is recurrent._ 

_Proof._ Suppose _C_ is closed and finite and that ( _Xn_ ) _n≥_ 0 starts in _C_ . Then for some _i ∈ C_ we have 

**==> picture [279 x 29] intentionally omitted <==**

by the strong Markov property. This shows that _i_ is not transient, so _C_ is recurrent by Theorems 1.5.3 and 1.5.4. 

It is easy to spot closed classes, so the transience or recurrence of finite classes is easy to determine. For example, the only recurrent class in Example 1.2.2 is _{_ 5 _,_ 6 _}_ , the others being transient. On the other hand, infinite closed classes may be transient: see Examples 1.3.3 and 1.6.3. 

We shall need the following result in Section 1.8. Remember that irreducibility means that the chain can get from any state to any other, with positive probability. 

_1. Discrete-time Markov chains_ 

28 

**Theorem 1.5.7.** _Suppose P is irreducible and recurrent. Then for all j ∈ I we have_ P( _Tj < ∞_ ) = 1 _._ 

_Proof._ By the Markov property we have 

**==> picture [188 x 25] intentionally omitted <==**

so it suffices to show P _i_ ( _Tj < ∞_ ) = 1 for all _i ∈ I_ . Choose _m_ with _p_[(] _ji[m]_[)] _>_ 0. By Theorem 1.5.3, we have 

**==> picture [296 x 91] intentionally omitted <==**

where the final equality uses the Markov property. But[�] _k∈I[p]_[(] _jk[m]_[)] = 1 so we must have P _i_ ( _Tj < ∞_ ) = 1. 

## **Exercises** 

**1.5.1** In Exercise 1.2.1, which states are recurrent and which are transient? 

**1.5.2** Show that, for the Markov chain ( _Xn_ ) _n≥_ 0 in Exercise 1.3.4 we have 

**==> picture [136 x 12] intentionally omitted <==**

Suppose, instead, the transition probabilities satisfy 

**==> picture [120 x 28] intentionally omitted <==**

For each _α ∈_ (0 _, ∞_ ) find the value of P( _Xn →∞_ as _n →∞_ ). 

**1.5.3 (First passage decomposition).** Denote by _Tj_ the first passage time to state _j_ and set 

**==> picture [89 x 17] intentionally omitted <==**

Justify the identity 

**==> picture [166 x 32] intentionally omitted <==**

_1.6 Recurrence and transience of random walks_ 

29 

and deduce that 

**==> picture [128 x 13] intentionally omitted <==**

where 

**==> picture [202 x 31] intentionally omitted <==**

Hence show that P _i_ ( _Ti < ∞_ ) = 1 if and only if 

**==> picture [63 x 31] intentionally omitted <==**

without using Theorem 1.5.3. 

**1.5.4** A random sequence of non-negative integers ( _Fn_ ) _n≥_ 0 is obtained by setting _F_ 0 = 0 and _F_ 1 = 1 and, once _F_ 0 _, . . . , Fn_ are known, taking _Fn_ +1 to be either the sum or the difference of _Fn−_ 1 and _Fn_ , each with probability 1 _/_ 2. Is ( _Fn_ ) _n≥_ 0 a Markov chain? 

By considering the Markov chain _Xn_ = ( _Fn−_ 1 _, Fn_ ), find the probability that ( _Fn_ ) _n≥_ 0 reaches 3 before first returning to 0. 

Draw enough of the flow diagram for ( _Xn_ ) _n≥_ 0 to establish a general pattern. Hence, using the strong Markov property, show that the hitting probability for (1 _,_ 1), starting from (1 _,_ 2), is (3 _− √_ 5) _/_ 2. 

Deduce that ( _Xn_ ) _n≥_ 0 is transient. Show that, moreover, with probability 1, _Fn →∞_ as _n →∞_ . 

## **1.6 Recurrence and transience of random walks** 

In the last section we showed that recurrence was a class property, that all recurrent classes were closed and that all finite closed classes were recurrent. So the only chains for which the question of recurrence remains interesting are irreducible with infinite state-space. Here we shall study some simple and fundamental examples of this type, making use of the following criterion for recurrence from Theorem 1.5.3: a state _i_ is recurrent if and only if _∞_ � _n_ =0 _[p] ii_[(] _[n]_[)] = _∞_ . 

## **Example 1.6.1 (Simple random walk on** Z **)** 

The simple random walk on Z has diagram 

**==> picture [220 x 27] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

30 

where 0 _< p_ = 1 _− q <_ 1. Suppose we start at 0. It is clear that we cannot return to 0 after an odd number of steps, so _p_[(2] 00 _[n]_[+1)] = 0 for all _n_ . Any given sequence of steps of length 2 _n_ from 0 to 0 occurs with probability _p[n] q[n]_ , there being _n_ steps up and _n_ steps down, and the number of such sequences is the number of ways of choosing the _n_ steps up from 2 _n_ . Thus 

**==> picture [92 x 27] intentionally omitted <==**

Stirling’s formula provides a good approximation to _n_ ! for large _n_ : it is known that 

**==> picture [155 x 14] intentionally omitted <==**

where _an ∼ bn_ means _an/bn →_ 1. For a proof see W. Feller, _An Introduction to Probability Theory and its Applications, Vol I_ (Wiley, New York, 3rd edition, 1968). At the end of this chapter we reproduce the argument used by Feller to show that 

**==> picture [151 x 13] intentionally omitted <==**

for some _A ∈_ [1 _, ∞_ ). The additional work needed to show _A_ = _√_ 2 _π_ is omitted, as this fact is unnecessary to our applications. 

For the _n_ -step transition probabilities we obtain 

**==> picture [219 x 29] intentionally omitted <==**

In the symmetric case _p_ = _q_ = 1 _/_ 2, so 4 _pq_ = 1; then for some _N_ and all _n ≥ N_ we have 

**==> picture [69 x 26] intentionally omitted <==**

so 

**==> picture [146 x 31] intentionally omitted <==**

which shows that the random walk is recurrent. On the other hand, if _p ̸_ = _q_ then 4 _pq_ = _r <_ 1, so by a similar argument, for some _N_ 

**==> picture [128 x 31] intentionally omitted <==**

showing that the random walk is transient. 

_1.6 Recurrence and transience of random walks_ 

31 

**Example 1.6.2 (Simple symmetric random walk on** Z[2] **)** The simple symmetric random walk on Z[2] has diagram 

**==> picture [170 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>4<br>1<br>4<br>1<br>4<br>1<br>4<br>**----- End of picture text -----**<br>


and transition probabilities 

**==> picture [127 x 28] intentionally omitted <==**

Suppose we start at 0. Let us call the walk _Xn_ and write _Xn_[+][and] _[X] n[−]_[for] the orthogonal projections of _Xn_ on the diagonal lines _y_ = _±x_ : 

**==> picture [162 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xn [+]<br>Xn<br>Xn [−]<br>**----- End of picture text -----**<br>


Then _Xn_[+][and] _[X] n[−]_[are][independent][simple][symmetric][random][walks][on] 2 _[−]_[1] _[/]_[2] Z and _Xn_ = 0 if and only if _Xn_[+][= 0 =] _[ X] n[−]_[.][This][makes][it][clear][that] for _Xn_ we have 

**==> picture [232 x 37] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

32 

by Stirling’s formula. Then[�] _[∞] n_ =1 _[p]_ 00[(] _[n]_[)][=] _[ ∞]_[by][comparison with][�] _[∞] n_ =1[1] _[/n]_ and the walk is recurrent. 

## **Example 1.6.3 (Simple symmetric random walk on** Z[3] **)** 

The transition probabilities of the simple symmetric random walk on Z[3] are given by 

**==> picture [127 x 27] intentionally omitted <==**

Thus the chain jumps to each of its nearest neighbours with equal probability. Suppose we start at 0. We can only return to 0 after an even number 2 _n_ of steps. Of these 2 _n_ steps there must be _i_ up, _i_ down, _j_ north, _j_ south, _k_ east and _k_ west for some _i, j, k ≥_ 0, with _i_ + _j_ + _k_ = _n_ . By counting the ways in which this can be done, we obtain 

**==> picture [357 x 103] intentionally omitted <==**

Now 

the left-hand side being the total probability of all the ways of placing _n_ balls randomly into three boxes. For the case where _n_ = 3 _m_ , we have 

**==> picture [140 x 27] intentionally omitted <==**

for all _i, j, k_ , so 

**==> picture [325 x 30] intentionally omitted <==**

by Stirling’s formula. Hence,[�] _[∞] m_ =0 _[p]_ 00[(6] _[m]_[)] _< ∞_ by comparison with � _∞n_ =0 _[n][−]_[3] _[/]_[2][.][But] _[p]_[(6] 00 _[m]_[)] _≥_ (1 _/_ 6)[2] _p_[(6] 00 _[m][−]_[2)] and _p_[(6] 00 _[m]_[)] _≥_ (1 _/_ 6)[4] _p_[(6] 00 _[m][−]_[4)] for all _m_ so we must have 

**==> picture [63 x 31] intentionally omitted <==**

and the walk is transient. 

_1.7 Invariant distributions_ 

33 

## **Exercises** 

**1.6.1** The rooted binary tree is an infinite graph _T_ with one distinguished vertex _R_ from which comes a single edge; at every other vertex there are three edges and there are no closed loops. The random walk on _T_ jumps from a vertex along each available edge with equal probability. Show that the random walk is transient. 

**1.6.2** Show that the simple symmetric random walk in Z[4] is transient. 

## **1.7 Invariant distributions** 

Many of the long-time properties of Markov chains are connected with the notion of an invariant distribution or measure. Remember that a measure _λ_ is any row vector ( _λi_ : _i ∈ I_ ) with non-negative entries. We say _λ_ is _invariant_ if 

**==> picture [40 x 8] intentionally omitted <==**

The terms _equilibrium_ and _stationary_ are also used to mean the same. The first result explains the term stationary. 

**Theorem 1.7.1.** _Let_ ( _Xn_ ) _n≥_ 0 _be Markov_ ( _λ, P_ ) _and suppose that λ is invariant for P . Then_ ( _Xm_ + _n_ ) _n≥_ 0 _is also Markov_ ( _λ, P_ ) _._ 

_Proof._ By Theorem 1.1.3, P( _Xm_ = _i_ ) = ( _λP[m]_ ) _i_ = _λi_ for all _i_ and, clearly, conditional on _Xm_ + _n_ = _i_ , _Xm_ + _n_ +1 is independent of _Xm, Xm_ +1 _, . . . , Xm_ + _n_ and has distribution ( _pij_ : _j ∈ I_ ). 

The next result explains the term equilibrium. 

**Theorem 1.7.2.** _Let I be finite. Suppose for some i ∈ I that_ 

**==> picture [184 x 17] intentionally omitted <==**

_Then π_ = ( _πj_ : _j ∈ I_ ) _is an invariant distribution._ 

_Proof._ We have 

**==> picture [200 x 27] intentionally omitted <==**

and 

**==> picture [308 x 26] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

34 

where we have used finiteness of _I_ to justify interchange of summation and limit operations. Hence _π_ is an invariant distribution. 

Notice that for any of the random walks discussed in Section 1.6 we have _p_[(] _ij[n]_[)] _→_ 0 as _n →∞_ for all _i, j ∈ I_ . The limit is certainly invariant, but it is not a distribution! 

Theorem 1.7.2 is not a very useful result but it serves to indicate a relationship between invariant distributions and _n_ -step transition probabilities. In Theorem 1.8.3 we shall prove a sort of converse, which is much more useful. 

## **Example 1.7.3** 

Consider the two-state Markov chain with transition matrix 

**==> picture [111 x 28] intentionally omitted <==**

Ignore the trivial cases _α_ = _β_ = 0 and _α_ = _β_ = 1. Then, by Example 1.1.4 

**==> picture [223 x 27] intentionally omitted <==**

so, by Theorem 1.7.2, the distribution ( _β/_ ( _α_ + _β_ ) _, α/_ ( _α_ + _β_ )) must be invariant. There are of course easier ways to discover this. 

## **Example 1.7.4** 

Consider the Markov chain ( _Xn_ ) _n≥_ 0 with diagram 

**==> picture [114 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>1<br>2 1<br>3 1 2<br>2<br>**----- End of picture text -----**<br>


To find an invariant distribution we write down the components of the vector equation _πP_ = _π_ 

**==> picture [80 x 50] intentionally omitted <==**

_1.7 Invariant distributions_ 

35 

In terms of the chain, the right-hand sides give the probabilities for _X_ 1, when _X_ 0 has distribution _π_ , and the equations require _X_ 1 also to have distribution _π_ . The equations are homogeneous so one of them is redundant, and another equation is required to fix _π_ uniquely. That equation is 

**==> picture [81 x 10] intentionally omitted <==**

and we find that _π_ = �1 _/_ 5 _,_ 2 _/_ 5 _,_ 2 _/_ 5�. 

According to Example 1.1.6 

**==> picture [112 x 16] intentionally omitted <==**

so this confirms Theorem 1.7.2. Alternatively, knowing that _p_ 11[(] _[n]_[)][had][the] form 

**==> picture [188 x 28] intentionally omitted <==**

we could have used Theorem 1.7.2 and knowledge of _π_ 1 to identify _a_ = 1 _/_ 5, instead of working out _p_[(2)] 11[in][Example][1.1.6.] 

In the next two results we shall show that every irreducible and recurrent stochastic matrix _P_ has an essentially unique positive invariant measure. The proofs rely heavily on the probabilistic interpretation so it is worth noting at the outset that, for a finite state-space _I_ , the existence of an invariant row vector is a simple piece of linear algebra: the row sums of _P_ are all 1, so the column vector of ones is an eigenvector with eigenvalue 1, so _P_ must have a row eigenvector with eigenvalue 1. 

For a fixed state _k_ , consider for each _i_ the _expected time spent in i between visits to k_ : 

**==> picture [105 x 33] intentionally omitted <==**

Here the sum of indicator functions serves to count the number of times _n_ at which _Xn_ = _i_ before the first passage time _Tk_ . 

**Theorem 1.7.5.** _Let P be irreducible and recurrent. Then_ 

(i) _γk[k]_[= 1] _[;]_ 

**==> picture [196 x 29] intentionally omitted <==**

_Proof._ (i) This is obvious. (ii) For _n_ = 1 _,_ 2 _, . . ._ the event _{n ≤ Tk}_ depends only on _X_ 0 _, X_ 1 _, . . . , Xn−_ 1, so, by the Markov property at _n −_ 1 

**==> picture [318 x 12] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

36 

Since _P_ is recurrent, under P _k_ we have _Tk < ∞_ and _X_ 0 = _XTk_ = _k_ with probability one. Therefore 

**==> picture [226 x 220] intentionally omitted <==**

(iii) Since _P_ is irreducible, for each state _i_ there exist _n, m ≥_ 0 with _pik_[(] _[n]_[)] _[, p]_[(] _ki[m]_[)] _>_ 0. Then _γi[k][≥][γ] k[k][p]_[(] _ki[m]_[)] _>_ 0 and _γi[k][p] ik_[(] _[n]_[)] _≤ γk[k]_[=][1][by][(i)][and] (ii). 

**Theorem 1.7.6.** _Let P be irreducible and let λ be an invariant measure for P with λk_ = 1 _. Then λ ≥ γ[k] . If in addition P is recurrent, then λ_ = _γ[k] ._ 

_Proof._ For each _j ∈ I_ we have 

**==> picture [336 x 227] intentionally omitted <==**

_1.7 Invariant distributions_ 

37 

So _λ ≥ γ[k]_ . If _P_ is recurrent, then _γ[k]_ is invariant by Theorem 1.7.5, so _µ_ = _λ − γ[k]_ is also invariant and _µ ≥_ 0. Since _P_ is irreducible, given _i ∈ I_ , we have _pik_[(] _[n]_[)] _>_ 0 for some _n_ , and 0 = _µk_ =[�] _j∈I[µ][j][p] jk_[(] _[n]_[)] _≥ µipik_[(] _[n]_[)][,][so] _µi_ = 0. 

Recall that a state _i_ is recurrent if 

**==> picture [176 x 12] intentionally omitted <==**

and we showed in Theorem 1.5.3 that this is equivalent to 

**==> picture [79 x 12] intentionally omitted <==**

If in addition the _expected return time_ 

**==> picture [58 x 12] intentionally omitted <==**

is finite, then we say _i_ is _positive recurrent_ . A recurrent state which fails to have this stronger property is called _null recurrent_ . 

**Theorem 1.7.7.** _Let P be irreducible. Then the following are equivalent:_ 

(i) _every state is positive recurrent;_ 

(ii) _some state i is positive recurrent;_ 

(iii) _P has an invariant distribution, π say. Moreover, when_ (iii) _holds we have mi_ = 1 _/πi for all i._ 

_Proof._ (i) _⇒_ (ii) This is obvious. 

(ii) _⇒_ (iii) If _i_ is positive recurrent, it is certainly recurrent, so _P_ is recurrent. By Theorem 1.7.5, _γ[i]_ is then invariant. But 

**==> picture [82 x 26] intentionally omitted <==**

so _πj_ = _γj[i][/m][i]_[defines][an][invariant][distribution.] (iii) _⇒_ (i) Take any state _k_ . Since _P_ is irreducible and[�] _i∈I[π][i]_[= 1 we have] _πk_ =[�] _i∈I[π][i][p] ik_[(] _[n]_[)] _[>]_[0][for][some] _[n]_[.][Set] _[λ][i]_[=] _[π][i][/π][k]_[.][Then] _[λ]_[is][an][invariant] measure with _λk_ = 1. So by Theorem 1.7.6, _λ ≥ γ[k]_ . Hence 

**==> picture [259 x 30] intentionally omitted <==**

and _k_ is positive recurrent. 

_1. Discrete-time Markov chains_ 

38 

To complete the proof we return to the argument for (iii) _⇒_ (i) armed with the knowledge that _P_ is recurrent, so _λ_ = _γ[k]_ and the inequality (1.7) is in fact an equality. 

## **Example 1.7.8 (Simple symmetric random walk on** Z **)** 

The simple symmetric random walk on Z is clearly irreducible and, by Example 1.6.1, it is also recurrent. Consider the measure 

**==> picture [81 x 10] intentionally omitted <==**

Then 

**==> picture [94 x 14] intentionally omitted <==**

so _π_ is invariant. Now Theorem 1.7.6 forces any invariant measure to be a scalar multiple of _π_ . Since[�] _i∈_ Z _[π][i]_[=] _[∞]_[,][there][can][be][no][invariant] distribution and the walk is therefore null recurrent, by Theorem 1.7.7. 

## **Example 1.7.9** 

The existence of an invariant measure does not guarantee recurrence: consider, for example, the simple symmetric random walk on Z[3] , which is transient by Example 1.6.3, but has invariant measure _π_ given by _πi_ = 1 for all _i_ . 

## **Example 1.7.10** 

Consider the asymmetric random walk on Z with transition probabilities _pi,i−_ 1 = _q < p_ = _pi,i_ +1. In components the invariant measure equation _πP_ = _π_ reads 

**==> picture [95 x 10] intentionally omitted <==**

This is a recurrence relation for _π_ with general solution 

**==> picture [88 x 13] intentionally omitted <==**

So, in this case, there is a two-parameter family of invariant measures – uniqueness up to scalar multiples does not hold. 

## **Example 1.7.11** 

Consider a _success-run chain_ on Z[+] , whose transition probabilities are given by 

**==> picture [149 x 11] intentionally omitted <==**

_1.7 Invariant distributions_ 

39 

Then the components of the invariant measure equation _πP_ = _π_ read 

**==> picture [128 x 47] intentionally omitted <==**

Suppose we choose _pi_ converging sufficiently rapidly to 1 so that 

**==> picture [70 x 32] intentionally omitted <==**

Then for any invariant measure _π_ we have 

**==> picture [199 x 31] intentionally omitted <==**

This equation forces either _π_ 0 = 0 or _π_ 0 = _∞_ , so there is no non-zero invariant measure. 

## **Exercises** 

**1.7.1** Find all invariant distributions of the transition matrix in Exercise 1.2.1. 

**1.7.2** Gas molecules move about randomly in a box which is divided into two halves symmetrically by a partition. A hole is made in the partition. Suppose there are _N_ molecules in the box. Show that the number of molecules on one side of the partition just after a molecule has passed through the hole evolves as a Markov chain. What are the transition probabilities? What is the invariant distribution of this chain? 

**1.7.3** A particle moves on the eight vertices of a cube in the following way: at each step the particle is equally likely to move to each of the three adjacent vertices, independently of its past motion. Let _i_ be the initial vertex occupied by the particle, _o_ the vertex opposite _i_ . Calculate each of the following quantities: 

_1. Discrete-time Markov chains_ 

40 

(i) the expected number of steps until the particle returns to _i_ ; 

(ii) the expected number of visits to _o_ until the first return to _i_ ; 

(iii) the expected number of steps until the first visit to _o_ . 

**1.7.4** Let ( _Xn_ ) _n≥_ 0 be a simple random walk on Z with _pi,i−_ 1 = _q < p_ = _pi,i_ +1. Find 

**==> picture [118 x 34] intentionally omitted <==**

and verify that 

**==> picture [99 x 18] intentionally omitted <==**

where the infimum is taken over all invariant measures _λ_ with _λ_ 0 = 1. (Compare with Theorem 1.7.6 and Example 1.7.10.) 

**1.7.5** Let _P_ be a stochastic matrix on a finite set _I_ . Show that a distribution _π_ is invariant for _P_ if and only if _π_ ( _I −P_ + _A_ ) = _a_ , where _A_ = ( _aij_ : _i, j ∈ I_ ) with _aij_ = 1 for all _i_ and _j_ , and _a_ = ( _ai_ : _i ∈ I_ ) with _ai_ = 1 for all _i_ . Deduce that if _P_ is irreducible then _I −P_ + _A_ is invertible. _Note that this enables one to compute the invariant distribution by any standard method of inverting a matrix_ . 

## **1.8 Convergence to equilibrium** 

We shall investigate the limiting behaviour of the _n_ -step transition probabilities _pij_[(] _[n]_[)] as _n →∞_ . As we saw in Theorem 1.7.2, if the state-space is finite and if for some _i_ the limit exists for all _j_ , then it must be an invariant distribution. But, as the following example shows, the limit does not always exist. 

## **Example 1.8.1** 

Consider the two-state chain with transition matrix 

**==> picture [71 x 27] intentionally omitted <==**

Then _P_[2] = _I_ , so _P_[2] _[n]_ = _I_ and _P_[2] _[n]_[+1] = _P_ for all _n_ . Thus _pij_[(] _[n]_[)] fails to converge for all _i, j_ . 

Let us call a state _i aperiodic_ if _pii_[(] _[n]_[)] _>_ 0 for all sufficiently large _n_ . We leave it as an exercise to show that _i_ is aperiodic if and only if the set _{n ≥_ 0 : _pii_[(] _[n]_[)] _>_ 0 _}_ has no common divisor other than 1. This is also a consequence of Theorem 1.8.4. The behaviour of the chain in Example 1.8.1 is connected with its periodicity. 

_1.8 Convergence to equilibrium_ 

41 

**Lemma 1.8.2.** _Suppose P is irreducible and has an aperiodic state i. Then, for all states j and k, pjk_[(] _[n]_[)] _[>]_[ 0] _[ for all sufficiently large][ n][.][In particular,] all states are aperiodic._ 

**==> picture [249 x 17] intentionally omitted <==**

**==> picture [128 x 17] intentionally omitted <==**

for all sufficiently large _n_ . 

Here is the main result of this section. The method of proof, by coupling two Markov chains, is ingenious. 

**Theorem 1.8.3 (Convergence to equilibrium).** _Let P be irreducible and aperiodic, and suppose that P has an invariant distribution π. Let λ be any distribution. Suppose that_ ( _Xn_ ) _n≥_ 0 _is Markov_ ( _λ, P_ ) _. Then_ 

**==> picture [182 x 13] intentionally omitted <==**

_In particular,_ 

**==> picture [159 x 17] intentionally omitted <==**

_Proof._ We use a coupling argument. Let ( _Yn_ ) _n≥_ 0 be Markov( _π, P_ ) and independent of ( _Xn_ ) _n≥_ 0. Fix a reference state _b_ and set 

**==> picture [148 x 12] intentionally omitted <==**

**Step 1** . We show P( _T < ∞_ ) = 1. The process _Wn_ = ( _Xn, Yn_ ) is a Markov chain on _I × I_ with transition probabilities 

**==> picture [82 x 13] intentionally omitted <==**

and initial distribution 

**==> picture [65 x 13] intentionally omitted <==**

Since _P_ is aperiodic, for all states _i, j, k, l_ we have 

**==> picture [112 x 18] intentionally omitted <==**

for all sufficiently large _n_ ; so _P_[�] is irreducible. Also, _P_[�] has an invariant distribution given by 

**==> picture [61 x 13] intentionally omitted <==**

so, by Theorem 1.7.7, _P_[�] is positive recurrent. But _T_ is the first passage time of _Wn_ to ( _b, b_ ) so P( _T < ∞_ ) = 1, by Theorem 1.5.7. 

_1. Discrete-time Markov chains_ 

42 

**Step 2** . Set 

**==> picture [109 x 28] intentionally omitted <==**

The diagram below illustrates the idea. We show that ( _Zn_ ) _n≥_ 0 is Markov( _λ, P_ ). 

**==> picture [324 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
I<br>Zn<br>Xn * [***] * * *<br>******** ****<br>* [***] * [*******]<br>********<br>* [*******]<br>b<br>T n<br>Yn<br>**----- End of picture text -----**<br>


The strong Markov property applies to ( _Wn_ ) _n≥_ 0 at time _T_ , so ( _XT_ + _n, YT_ + _n_ ) _n≥_ 0 is Markov( _δ_ ( _b,b_ ) _, P_[�] ) and independent of ( _X_ 0 _, Y_ 0) _,_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _XT , YT_ ). By symmetry, we can replace the process ( _XT_ + _n, YT_ + _n_ ) _n≥_ 0 by ( _YT_ + _n, XT_ + _n_ ) _n≥_ 0 which is also Markov( _δ_ ( _b,b_ ) _, P_[�] ) and remains independent of ( _X_ 0 _, Y_ 0) _,_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _XT , YT_ ). Hence _Wn[′]_[=] ( _Zn, Zn[′]_[)][is][Markov(] _[µ,][P]_[�][)][where] 

**==> picture [109 x 28] intentionally omitted <==**

In particular, ( _Zn_ ) _n≥_ 0 is Markov( _λ, P_ ). 

**Step 3** . We have 

**==> picture [283 x 12] intentionally omitted <==**

so 

**==> picture [250 x 46] intentionally omitted <==**

and P( _n < T_ ) _→_ 0 as _n →∞_ . 

_1.8 Convergence to equilibrium_ 

43 

To understand this proof one should see what goes wrong when _P_ is not aperiodic. Consider the two-state chain of Example 1.8.1 which has (1 _/_ 2 _,_ 1 _/_ 2) as its unique invariant distribution. We start ( _Xn_ ) _n≥_ 0 from 0 and ( _Yn_ ) _n≥_ 0 with equal probability from 0 or 1. However, if _Y_ 0 = 1, then, because of periodicity, ( _Xn_ ) _n≥_ 0 and ( _Yn_ ) _n≥_ 0 will never meet, and the proof fails. We move on now to the cases that were excluded in the last theorem, where ( _Xn_ ) _n≥_ 0 is periodic or transient or null recurrent. The remainder of this section might be omitted on a first reading. 

**Theorem 1.8.4.** _Let P be irreducible. There is an integer d ≥_ 1 _and a partition_ 

**==> picture [120 x 11] intentionally omitted <==**

_such that (setting Cnd_ + _r_ = _Cr)_ 

**==> picture [314 x 37] intentionally omitted <==**

_Proof._ Fix a state _k_ and consider _S_ = _{n ≥_ 0 : _pkk_[(] _[n]_[)] _[>]_[ 0] _[}]_[.][Choose] _[ n]_[1] _[, n]_[2] _[∈][S]_ with _n_ 1 _< n_ 2 and such that _d_ := _n_ 2 _− n_ 1 is as small as possible. (Here and throughout we use the symbol := to mean ‘defined to equal’.) Define for _r_ = 0 _, . . . , d −_ 1 

**==> picture [203 x 16] intentionally omitted <==**

Then _C_ 0 _∪ . . . ∪ Cd−_ 1 = _I_ , by irreducibility. Moreover, if _p_[(] _ki[nd]_[+] _[r]_[)] _>_ 0 and _p_[(] _ki[nd]_[+] _[s]_[)] _>_ 0 for some _r, s ∈{_ 0 _,_ 1 _, . . . , d −_ 1 _}_ , then, choosing _m ≥_ 0 so that _p_[(] _ik[m]_[)] _>_ 0, we have _p_[(] _kk[nd]_[+] _[r]_[+] _[m]_[)] _>_ 0 and _p_[(] _kk[nd]_[+] _[s]_[+] _[m]_[)] _>_ 0 so _r_ = _s_ by minimality of _d_ . Hence we have a partition. 

To prove (i) suppose _pij_[(] _[n]_[)] _>_ 0 and _i ∈ Cr_ . Choose _m_ so that _pki_[(] _[md]_[+] _[r]_[)] _>_ 0, then _pkj_[(] _[md]_[+] _[r]_[+] _[n]_[)] _>_ 0 so _j ∈ Cr_ + _n_ as required. By taking _i_ = _j_ = _k_ we now see that _d_ must divide every element of _S_ , in particular _n_ 1. 

Now for _nd ≥ n_[2] 1[,][we][can][write] _[nd]_[=] _[qn]_[1][+] _[ r]_[for][integers] _[q][≥][n]_[1][and] 0 _≤ r ≤ n_ 1 _−_ 1. Since _d_ divides _n_ 1 we then have _r_ = _md_ for some integer _m_ and then _nd_ = ( _q − m_ ) _n_ 1 + _mn_ 2. Hence 

**==> picture [148 x 16] intentionally omitted <==**

and hence _nd ∈ S_ . To prove (ii) for _i, j ∈ Cr_ choose _m_ 1 and _m_ 2 so that _p_[(] _ik[m]_[1][)] _>_ 0 and _p_[(] _kj[m]_[2][)] _>_ 0, then 

**==> picture [169 x 18] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

44 

whenever _nd ≥ n_[2] 1[.][Since] _[m]_[1][+] _[ m]_[2][is][then][necessarily][a][multiple][of] _[d]_[,][we] are done. 

We call _d_ the _period_ of _P_ . The theorem just proved shows in particular for all _i ∈ I_ that _d_ is the greatest common divisor of the set _{n ≥_ 0 : _pii_[(] _[n]_[)] _>_ 0 _}_ . This is sometimes useful in identifying _d_ . 

Finally, here is a complete description of limiting behaviour for irreducible chains. This generalizes Theorem 1.8.3 in two respects since we require neither aperiodicity nor the existence of an invariant distribution. The argument we use for the null recurrent case was discovered recently by B. Fristedt and L. Gray. 

**Theorem 1.8.5.** _Let P be irreducible of period d and let C_ 0 _, C_ 1 _, . . . , Cd−_ 1 _be the partition obtained in Theorem 1.8.4. Let λ be a distribution with_ � _i∈C_ 0 _[λ][i]_[=][1] _[.] Suppose that_ ( _Xn_ ) _n≥_ 0 _is Markov_ ( _λ, P_ ) _. Then for r_ = 0 _,_ 1 _, . . . , d −_ 1 _and j ∈ Cr we have_ 

**==> picture [168 x 12] intentionally omitted <==**

_where mj is the expected return time to j. In particular, for i ∈ C_ 0 _and j ∈ Cr we have_ 

**==> picture [139 x 17] intentionally omitted <==**

_Proof_ 

**Step 1** . We reduce to the aperiodic case. Set _ν_ = _λP[r]_ , then by Theorem 1.8.4 we have 

**==> picture [55 x 25] intentionally omitted <==**

Set _Yn_ = _Xnd_ + _r_ , then ( _Yn_ ) _n≥_ 0 is Markov( _ν, P[d]_ ) and, by Theorem 1.8.4, _P[d]_ is irreducible and aperiodic on _Cr_ . For _j ∈ Cr_ the expected return time of ( _Yn_ ) _n≥_ 0 to _j_ is _mj/d_ . So if the theorem holds in the aperiodic case, then 

**==> picture [230 x 12] intentionally omitted <==**

so the theorem holds in general. 

**Step 2** . Assume that _P_ is aperiodic. If _P_ is positive recurrent then 1 _/mj_ = _πj_ , where _π_ is the unique invariant distribution, so the result follows from Theorem 1.8.3. Otherwise _m_ = _∞_ and we have to show that _j_ 

**==> picture [136 x 12] intentionally omitted <==**

_1.8 Convergence to equilibrium_ 

45 

If _P_ is transient this is easy and we are left with the null recurrent case. 

**Step 3** . Assume that _P_ is aperiodic and null recurrent. Then 

**==> picture [145 x 32] intentionally omitted <==**

Given _ε >_ 0 choose _K_ so that 

**==> picture [101 x 33] intentionally omitted <==**

Then, for _n ≥ K −_ 1 

**==> picture [280 x 109] intentionally omitted <==**

so we must have P( _Xn−k_ = _j_ ) _≤ ε/_ 2 for some _k ∈{_ 0 _,_ 1 _, . . . , K −_ 1 _}_ . 

Return now to the coupling argument used in Theorem 1.8.3, only now let ( _Yn_ ) _n≥_ 0 be Markov( _µ, P_ ), where _µ_ is to be chosen later. Set _Wn_ = ( _Xn, Yn_ ). As before, aperiodicity of ( _Xn_ ) _n≥_ 0 ensures irreducibility of ( _Wn_ ) _n≥_ 0. If ( _Wn_ ) _n≥_ 0 is transient then, on taking _µ_ = _λ_ , we obtain 

**==> picture [164 x 14] intentionally omitted <==**

as required. Assume then that ( _Wn_ ) _n≥_ 0 is recurrent. Then, in the notation of Theorem 1.8.3, we have P( _T < ∞_ ) = 1 and the coupling argument shows that 

**==> picture [213 x 12] intentionally omitted <==**

We exploit this convergence by taking _µ_ = _λP[k]_ for _k_ = 1 _, . . . , K −_ 1, so that P( _Yn_ = _j_ ) = P( _Xn_ + _k_ = _j_ ). We can find _N_ such that for _n ≥ N_ and _k_ = 1 _, . . . , K −_ 1, 

**==> picture [160 x 21] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

46 

But for any _n_ we can find _k ∈{_ 0 _,_ 1 _, . . . , K −_ 1 _}_ such that P( _Xn_ + _k_ = _j_ ) _≤ ε/_ 2. Hence, for _n ≥ N_ 

**==> picture [74 x 12] intentionally omitted <==**

Since _ε >_ 0 was arbitrary, this shows that P( _Xn_ = _j_ ) _→_ 0 as _n →∞_ , as required. 

## **Exercises** 

**1.8.1** Prove the claims (e), (f) and (g) made in example (v) of the Introduction. 

**1.8.2** Find the invariant distributions of the transition matrices in Exercise 

1.1.7, parts (a), (b) and (c), and compare them with your answers there. 

**1.8.3** A fair die is thrown repeatedly. Let _Xn_ denote the sum of the first _n_ throws. Find 

**==> picture [146 x 16] intentionally omitted <==**

quoting carefully any general theorems that you use. 

**1.8.4** Each morning a student takes one of the three books he owns from his shelf. The probability that he chooses book _i_ is _αi_ , where 0 _< αi <_ 1 for _i_ = 1 _,_ 2 _,_ 3, and choices on successive days are independent. In the evening he replaces the book at the left-hand end of the shelf. If _pn_ denotes the probability that on day _n_ the student finds the books in the order 1,2,3, from left to right, show that, irrespective of the initial arrangement of the books, _pn_ converges as _n →∞_ , and determine the limit. 

**1.8.5 (Renewal theorem).** Let _Y_ 1 _, Y_ 2 _, . . ._ be independent, identically distributed random variables with values in _{_ 1 _,_ 2 _, . . . }_ . Suppose that the set of integers 

**==> picture [96 x 12] intentionally omitted <==**

has greatest common divisor 1. Set _µ_ = E( _Y_ 1). Show that the following process is a Markov chain: 

**==> picture [279 x 12] intentionally omitted <==**

Determine 

**==> picture [76 x 16] intentionally omitted <==**

and hence show that as _n →∞_ 

**==> picture [212 x 12] intentionally omitted <==**

_1.9 Time reversal_ 

47 

( _Think of Y_ 1 _, Y_ 2 _, . . . as light-bulb lifetimes. A bulb is replaced when it fails. Thus the limiting probability that a bulb is replaced at time n is_ 1 _/µ. Although this appears to be a very special case of convergence to equilibrium, one can actually recover the full result by applying the renewal theorem to the excursion lengths Si_[(1)] _, Si_[(2)] _, . . . from state i._ ) 

## **1.9 Time reversal** 

For Markov chains, the past and future are independent given the present. This property is symmetrical in time and suggests looking at Markov chains with time running backwards. On the other hand, convergence to equilibrium shows behaviour which is asymmetrical in time: a highly organised state such as a point mass decays to a disorganised one, the invariant distribution. This is an example of entropy increasing. It suggests that if we want complete time-symmetry we must begin in equilibrium. The next result shows that a Markov chain in equilibrium, run backwards, is again a Markov chain. The transition matrix may however be different. 

**Theorem 1.9.1.** _Let P be irreducible and have an invariant distribution π. Suppose that_ ( _Xn_ )0 _≤n≤N is Markov_ ( _π, P_ ) _and set Yn_ = _XN −n. Then_ ( _Yn_ )0 _≤n≤N is Markov_ ( _π, P_[�] ) _, where P_[�] = ( _p_ � _ij_ ) _is given by_ 

**==> picture [119 x 12] intentionally omitted <==**

_and P_[�] _is also irreducible with invariant distribution π._ 

_Proof._ First we check that _P_[�] is a stochastic matrix: 

**==> picture [123 x 29] intentionally omitted <==**

since _π_ is invariant for _P_ . Next we check that _π_ is invariant for _P_[�] : 

**==> picture [122 x 26] intentionally omitted <==**

since _P_ is a stochastic matrix. 

We have 

**==> picture [216 x 46] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

48 

so, by Theorem 1.1.1, ( _Yn_ )0 _≤n≤N_ is Markov( _π, P_[�] ). Finally, since _P_ is irreducible, for each pair of states _i, j_ there is a chain of states _i_ 1 = _i, i_ 2 _, . . . , in−_ 1 _, in_ = _j_ with _pi_ 1 _i_ 2 _. . . pin −_ 1 _in >_ 0. Then 

**==> picture [210 x 12] intentionally omitted <==**

so _P_[�] is also irreducible. 

The chain ( _Yn_ )0 _≤n≤N_ is called the _time-reversal_ of ( _Xn_ )0 _≤n≤N_ . 

A stochastic matrix _P_ and a measure _λ_ are said to be in _detailed balance_ if 

**==> picture [123 x 12] intentionally omitted <==**

Though obvious, the following result is worth remembering because, when a solution _λ_ to the detailed balance equations exists, it is often easier to find by the detailed balance equations than by the equation _λ_ = _λP_ . 

**Lemma 1.9.2.** _If P and λ are in detailed balance, then λ is invariant for P ._ 

_Proof._ We have ( _λP_ ) _i_ =[�] _j∈I[λ][j][p][ji]_[=][ �] _j∈I[λ][i][p][ij]_[=] _[ λ][i]_[.] 

Let ( _Xn_ ) _n≥_ 0 be Markov( _λ, P_ ), with _P_ irreducible. We say that ( _Xn_ ) _n≥_ 0 is _reversible_ if, for all _N ≥_ 1, ( _XN −n_ )0 _≤n≤N_ is also Markov( _λ, P_ ). 

**Theorem 1.9.3.** _Let P be an irreducible stochastic matrix and let λ be a distribution. Suppose that_ ( _Xn_ ) _n≥_ 0 _is Markov_ ( _λ, P_ ) _. Then the following are equivalent:_ 

- (a) ( _Xn_ ) _n≥_ 0 _is reversible;_ 

- (b) _P and λ are in detailed balance._ 

_Proof._ Both (a) and (b) imply that _λ_ is invariant for _P_ . Then both (a) and (b) are equivalent to the statement that _P_[�] = _P_ in Theorem 1.9.1. 

We begin a collection of examples with a chain which is not reversible. 

## **Example 1.9.4** 

Consider the Markov chain with diagram: 

**==> picture [116 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 2<br>3 3<br>1 1<br>3 3<br>1<br>3<br>3 2<br>2<br>3<br>**----- End of picture text -----**<br>


_1.9 Time reversal_ 

49 

The transition matrix is 

**==> picture [118 x 40] intentionally omitted <==**

and _π_ = (1 _/_ 3 _,_ 1 _/_ 3 _,_ 1 _/_ 3) is invariant. Hence _P_[�] = _P[T]_ , the transpose of _P_ . But _P_ is not symmetric, so _P_ = _P_[�] and this chain is not reversible. A patient observer would see the chain move clockwise in the long run: under time-reversal the clock would run backwards! 

## **Example 1.9.5** 

Consider the Markov chain with diagram: 

**==> picture [258 x 27] intentionally omitted <==**

where 0 _< p_ = 1 _− q <_ 1. The non-zero detailed balance equations read 

**==> picture [220 x 12] intentionally omitted <==**

So a solution is given by 

**==> picture [142 x 14] intentionally omitted <==**

and this may be normalised to give a distribution in detailed balance with _P_ . Hence this chain is reversible. 

If _p_ were much larger than _q_ , one might argue that the chain would tend to move to the right and its time-reversal to the left. However, this ignores the fact that we reverse the chain _in equilibrium_ , which in this case would be heavily concentrated near _M_ . An observer would see the chain spending most of its time near _M_ and making occasional brief forays to the left, which behaviour is symmetrical in time. 

## **Example 1.9.6 (Random walk on a graph)** 

A _graph G_ is a countable collection of states, usually called _vertices_ , some of which are joined by _edges_ , for example: 

_1. Discrete-time Markov chains_ 

50 

**==> picture [114 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>4 3<br>**----- End of picture text -----**<br>


Thus a graph is a partially drawn Markov chain diagram. There is a natural way to complete the diagram which gives rise to the random walk on _G_ . The _valency vi_ of vertex _i_ is the number of edges at _i_ . We have to assume that every vertex has finite valency. The random walk on _G_ picks edges with equal probability: 

**==> picture [117 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 1<br>1 2 3 2<br>1<br>3<br>1 1<br>2 3<br>1<br>1 1<br>3<br>3 2<br>4 1 1 3<br>3 2<br>**----- End of picture text -----**<br>


Thus the transition probabilities are given by 

**==> picture [155 x 27] intentionally omitted <==**

We assume _G_ is connected, so that _P_ is irreducible. It is easy to see that _P_ is in detailed balance with _v_ = ( _vi_ : _i ∈ G_ ). So, if the total valency _σ_ =[�] _i∈G[v][i]_[is][finite,][then] _[π]_[=] _[ v/σ]_[is][invariant][and] _[P]_[is][reversible.] 

## **Example 1.9.7 (Random chessboard knight)** 

A random knight makes each permissible move with equal probability. If it starts in a corner, how long on average will it take to return? 

This is an example of a random walk on a graph: the vertices are the squares of the chessboard and the edges are the moves that the knight can take: 

_1.9 Time reversal_ 

51 

The diagram shows a part of the graph. We know by Theorem 1.7.7 and the preceding example that 

**==> picture [132 x 23] intentionally omitted <==**

so all we have to do is identify valencies. The four corner squares have valency 2, and the eight squares adjacent to the corners have valency 3. There are 20 squares of valency 4, 16 of valency 6, and the 16 central squares have valency 8. Hence 

**==> picture [192 x 24] intentionally omitted <==**

Alternatively, if you enjoy solving sets of 64 simultaneous linear equations, you might try finding _π_ from _πP_ = _π_ , or calculating E _c_ ( _Tc_ ) using Theorem 1.3.5! 

## **Exercises** 

**1.9.1** In each of the following cases determine whether the stochastic matrix _P_ , which you may assume is irreducible, is reversible: 

**==> picture [304 x 41] intentionally omitted <==**

(c) _I_ = _{_ 0 _,_ 1 _, . . . , N }_ and _pij_ = 0 if _|j − i| ≥_ 2 ; 

_1. Discrete-time Markov chains_ 

52 

(d) _I_ = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ and _p_ 01 = 1, _pi,i_ +1 = _p_ , _pi,i−_ 1 = 1 _− p_ for _i ≥_ 1; (e) _pij_ = _pji_ for all _i, j ∈ S_ . 

**1.9.2** Two particles _X_ and _Y_ perform independent random walks on the graph shown in the diagram. So, for example, a particle at _A_ jumps to _B_ , _C_ or _D_ with equal probability 1 _/_ 3. 

**==> picture [204 x 200] intentionally omitted <==**

**----- Start of picture text -----**<br>
D<br>A B<br>C<br>E<br>**----- End of picture text -----**<br>


Find the probability that _X_ and _Y_ ever meet at a vertex in the following cases: 

- (a) _X_ starts at _A_ and _Y_ starts at _B_ ; 

- (b) _X_ starts at _A_ and _Y_ starts at _E_ . 

For _I_ = _B, D_ let _MI_ denote the expected time, when both _X_ and _Y_ start at _I_ , until they are once again both at _I_ . Show that 9 _MD_ = 16 _MB_ . 

## **1.10 Ergodic theorem** 

Ergodic theorems concern the limiting behaviour of averages over time. We shall prove a theorem which identifies for Markov chains the long-run proportion of time spent in each state. An essential tool is the following ergodic theorem for independent random variables which is a version of the strong law of large numbers. 

**Theorem 1.10.1 (Strong law of large numbers).** _Let Y_ 1 _, Y_ 2 _, . . . be a sequence of independent, identically distributed, non-negative random_ 

_1.10 Ergodic theorem_ 

53 

_variables with_ E( _Y_ 1) = _µ. Then_ 

**==> picture [189 x 28] intentionally omitted <==**

_Proof._ A proof for the case _µ < ∞_ may be found, for example, in _Probability with Martingales_ by David Williams (Cambridge University Press, 1991). The case where _µ_ = _∞_ is a simple deduction. Fix _N < ∞_ and set _Yn_[(] _[N]_[)] = _Yn ∧ N_ . Then 

**==> picture [306 x 27] intentionally omitted <==**

with probability one. As _N ↑∞_ we have E( _Y_ 1 _∧ N_ ) _↑ µ_ by monotone convergence (see Section 6.4). So we must have, with probability 1 

**==> picture [166 x 23] intentionally omitted <==**

We denote by _Vi_ ( _n_ ) the _number of visits to i before n_ : 

**==> picture [99 x 33] intentionally omitted <==**

Then _Vi_ ( _n_ ) _/n_ is the proportion of time before _n_ spent in state _i_ . The following result gives the long-run proportion of time spent by a Markov chain in each state. 

**Theorem 1.10.2 (Ergodic theorem).** _Let P be irreducible and let λ be any distribution. If_ ( _Xn_ ) _n≥_ 0 _is Markov_ ( _λ, P_ ) _then_ 

**==> picture [158 x 27] intentionally omitted <==**

_where mi_ = E _i_ ( _Ti_ ) _is the expected return time to state i. Moreover, in the positive recurrent case, for any bounded function f_ : _I →_ R _we have_ 

**==> picture [182 x 33] intentionally omitted <==**

_where_ 

**==> picture [58 x 25] intentionally omitted <==**

_and where_ ( _πi_ : _i ∈ I_ ) _is the unique invariant distribution._ 

_1. Discrete-time Markov chains_ 

54 

_Proof._ If _P_ is transient, then, with probability 1, the total number _Vi_ of visits to _i_ is finite, so 

**==> picture [111 x 26] intentionally omitted <==**

Suppose then that _P_ is recurrent and fix a state _i_ . For _T_ = _Ti_ we have P( _T < ∞_ ) = 1 by Theorem 1.5.7 and ( _XT_ + _n_ ) _n≥_ 0 is Markov( _δi, P_ ) and independent of _X_ 0 _, X_ 1 _, . . . , XT_ by the strong Markov property. The longrun proportion of time spent in _i_ is the same for ( _XT_ + _n_ ) _n≥_ 0 and ( _Xn_ ) _n≥_ 0, so it suffices to consider the case _λ_ = _δi_ . 

Write _Si_[(] _[r]_[)] for the length of the _r_ th excursion to _i_ , as in Section 1.5. By Lemma 1.5.1, the non-negative random variables _Si_[(1)] _, Si_[(2)] _, . . ._ are independent and identically distributed with E _i_ ( _Si_[(] _[r]_[)] ) = _mi_ . Now 

**==> picture [150 x 15] intentionally omitted <==**

the left-hand side being the time of the last visit to _i_ before _n_ . Also 

**==> picture [120 x 16] intentionally omitted <==**

the left-hand side being the time of the first visit to _i_ after _n −_ 1. Hence 

**==> picture [311 x 30] intentionally omitted <==**

By the strong law of large numbers 

**==> picture [210 x 33] intentionally omitted <==**

and, since _P_ is recurrent 

**==> picture [144 x 12] intentionally omitted <==**

So, letting _n →∞_ in (1.8), we get 

which implies 

**==> picture [161 x 78] intentionally omitted <==**

_1.10 Ergodic theorem_ 

55 

Assume now that ( _Xn_ ) _n≥_ 0 has an invariant distribution ( _πi_ : _i ∈ I_ ). Let _f_ : _I →_ R be a bounded function and assume without loss of generality that _|f | ≤_ 1. For any _J ⊆ I_ we have 

**==> picture [199 x 266] intentionally omitted <==**

We proved above that 

Given _ε >_ 0, choose _J_ finite so that 

and then _N_ = _N_ ( _ω_ ) so that, for _n ≥ N_ ( _ω_ ) 

**==> picture [111 x 31] intentionally omitted <==**

Then, for _n ≥ N_ ( _ω_ ), we have 

**==> picture [108 x 34] intentionally omitted <==**

which establishes the desired convergence. 

We consider now the statistical problem of estimating an unknown transition matrix _P_ on the basis of observations of the corresponding Markov chain. Consider, to begin, the case where we have _N_ + 1 observations ( _Xn_ )0 _≤n≤N_ . The log-likelihood function is given by 

**==> picture [250 x 23] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

56 

up to a constant independent of _P_ , where _Nij_ is the number of transitions from _i_ to _j_ . A standard statistical procedure is to find the _maximum likelihood estimate P_[�] , which is the choice of _P_ maximizing _l_ ( _P_ ). Since _P_ must satisfy the linear constraint[�] _j[p][ij]_[= 1][for][each] _[i]_[,][we][first][try][to][maximize] 

**==> picture [79 x 26] intentionally omitted <==**

and then choose ( _µi_ : _i ∈ I_ ) to fit the constraints. This is the method of Lagrange multipliers. Thus we find 

**==> picture [188 x 33] intentionally omitted <==**

which is the proportion of jumps from _i_ which go to _j_ . 

We now turn to consider the _consistency_ of this sort of estimate, that is � to say whether _pij → pij_ with probability 1 as _N →∞_ . Since this is clearly false when _i_ is transient, we shall slightly modify our approach. Note that to find _p_ � _ij_ we simply have to maximize 

**==> picture [65 x 26] intentionally omitted <==**

subject to[�] _j[p][ij]_[= 1:][the][other terms and][constraints are][irrelevant.][Sup-] pose then that instead of _N_ + 1 observations we make enough observations to ensure the chain leaves state _i_ a total of _N_ times. In the transient case this may involve restarting the chain several times. Denote again by _Nij_ the number of transitions from _i_ to _j_ . 

To maximize the likelihood for ( _pij_ : _j ∈ I_ ) we still maximize 

**==> picture [65 x 26] intentionally omitted <==**

subject to[�] _j[p][ij]_[= 1,][which][leads][to][the][maximum][likelihood][estimate] 

**==> picture [63 x 13] intentionally omitted <==**

But _Nij_ = _Y_ 1 + _. . ._ + _YN_ , where _Yn_ = 1 if the _n_ th transition from _i_ is to _j_ , and _Yn_ = 0 otherwise. By the strong Markov property _Y_ 1 _, . . . , YN_ are independent and identically distributed random variables with mean _pij_ . So, by the strong law of large numbers 

**==> picture [138 x 13] intentionally omitted <==**

which shows that _p_ � _ij_ is consistent. 

_1.11 Appendix: recurrence relations_ 

57 

## **Exercises** 

**1.10.1** Prove the claim (d) made in example (v) of the Introduction. 

**1.10.2** A professor has _N_ umbrellas. He walks to the office in the morning and walks home in the evening. If it is raining he likes to carry an umbrella and if it is fine he does not. Suppose that it rains on each journey with probability _p_ , independently of past weather. What is the long-run proportion of journeys on which the professor gets wet? 

**1.10.3** Let ( _Xn_ ) _n≥_ 0 be an irreducible Markov chain on _I_ having an invariant distribution _π_ . For _J ⊆ I_ let ( _Ym_ ) _m≥_ 0 be the Markov chain on _J_ obtained by observing ( _Xn_ ) _n≥_ 0 whilst in _J_ . (See Example 1.4.4.) Show that ( _Ym_ ) _m≥_ 0 is positive recurrent and find its invariant distribution. 

**1.10.4** An opera singer is due to perform a long series of concerts. Having a fine artistic temperament, she is liable to pull out each night with probability 1 _/_ 2. Once this has happened she will not sing again until the promoter convinces her of his high regard. This he does by sending flowers every day until she returns. Flowers costing _x_ thousand pounds, 0 _≤ x ≤_ 1, bring about a reconciliation with probability _[√] x_ . The promoter stands to make _£_ 750 from each successful concert. How much should he spend on 

## **1.11 Appendix: recurrence relations** 

Recurrence relations often arise in the linear equations associated to Markov chains. Here is an account of the simplest cases. A more specialized case was dealt with in Example 1.3.4. In Example 1.1.4 we found a recurrence relation of the form 

**==> picture [78 x 12] intentionally omitted <==**

We look first for a constant solution _xn_ = _x_ ; then _x_ = _ax_ + _b_ , so provided _a_ = 1 we must have _x_ = _b/_ (1 _− a_ ). Now _yn_ = _xn − b/_ (1 _− a_ ) satisfies _yn_ +1 = _ayn_ , so _yn_ = _a[n] y_ 0. Thus the general solution when _a_ = 1 is given by 

**==> picture [104 x 11] intentionally omitted <==**

where _A_ is a constant. When _a_ = 1 the general solution is obviously 

**==> picture [67 x 11] intentionally omitted <==**

In Example 1.3.3 we found a recurrence relation of the form 

**==> picture [122 x 12] intentionally omitted <==**

_1. Discrete-time Markov chains_ 

58 

where _a_ and _c_ were both non-zero. Let us try a solution of the form _xn_ = _λ[n]_ ; then _aλ_[2] + _bλ_ + _c_ = 0. Denote by _α_ and _β_ the roots of this quadratic. Then 

**==> picture [82 x 11] intentionally omitted <==**

is a solution. If _α ̸_ = _β_ then we can solve the equations 

**==> picture [142 x 11] intentionally omitted <==**

so that _y_ 0 = _x_ 0 and _y_ 1 = _x_ 1; but 

**==> picture [244 x 12] intentionally omitted <==**

for all _n_ , so by induction _yn_ = _xn_ for all _n_ . If _α_ = _β_ = 0, then 

**==> picture [85 x 12] intentionally omitted <==**

is a solution and we can solve 

**==> picture [141 x 12] intentionally omitted <==**

so that _y_ 0 = _x_ 0 and _y_ 1 = _x_ 1; then, by the same argument, _yn_ = _xn_ for all _n_ . The case _α_ = _β_ = 0 does not arise. Hence the general solution is given by 

**==> picture [151 x 29] intentionally omitted <==**

## **1.12 Appendix: asymptotics for** _n_ ! 

Our analysis of recurrence and transience for random walks in Section 1.6 rested heavily on the use of the asymptotic relation 

**==> picture [140 x 13] intentionally omitted <==**

for some _A ∈_ [1 _, ∞_ ). Here is a derivation. 

We make use of the power series expansions for _|t| <_ 1 

**==> picture [165 x 33] intentionally omitted <==**

By subtraction we obtain 

**==> picture [176 x 27] intentionally omitted <==**

_1.12 Appendix: asymptotics for n_ ! 

59 

Set _An_ = _n_ ! _/_ ( _n[n]_[+1] _[/]_[2] _e[−][n]_ ) and _an_ = log _An_ . Then, by a straightforward calculation 

**==> picture [240 x 28] intentionally omitted <==**

By the series expansion written above we have 

**==> picture [349 x 117] intentionally omitted <==**

It follows that _an_ decreases and _an −_ 1 _/_ (12 _n_ ) increases as _n →∞_ . Hence _an → a_ for some _a ∈_ [0 _, ∞_ ) and hence _An → A_ , as _n →∞_ , where _A_ = _e[a]_ . 

**2** 

## Continuous-time Markov chains I 

The material on continuous-time Markov chains is divided between this chapter and the next. The theory takes some time to set up, but once up and running it follows a very similar pattern to the discrete-time case. To emphasise this we have put the setting-up in this chapter and the rest in the next. If you wish, you can begin with Chapter 3, provided you take certain basic properties on trust, which are reviewed in Section 3.1. The first three sections of Chapter 2 fill in some necessary background information and are independent of each other. Section 2.4 on the Poisson process and Section 2.5 on birth processes provide a gentle warm-up for general continuoustime Markov chains. These processes are simple and particularly important examples of continuous-time chains. Sections 2.6–2.8, especially 2.8, deal with the heart of the continuous-time theory. There is an irreducible level of difficulty at this point, so we advise that Sections 2.7 and 2.8 are read selectively at first. Some examples of more general processes are given in Section 2.9. As in Chapter 1 the exercises form an important part of the text. 

## **2.1** _Q_ **-matrices and their exponentials** 

In this section we shall discuss some of the basic properties of _Q_ -matrices and explain their connection with continuous-time Markov chains. 

Let _I_ be a countable set. A _Q_ - _matrix_ on _I_ is a matrix _Q_ = ( _qij_ : _i, j ∈ I_ ) satisfying the following conditions: 

_2.1 Q-matrices and their exponentials_ 

61 

**==> picture [141 x 12] intentionally omitted <==**

**==> picture [134 x 42] intentionally omitted <==**

Thus in each row of _Q_ we can choose the off-diagonal entries to be any nonnegative real numbers, subject only to the constraint that the off-diagonal row sum is 

**==> picture [83 x 26] intentionally omitted <==**

The diagonal entry _qii_ is then _−qi_ , making the total row sum zero. 

A convenient way to present the data for a continuous-time Markov chain is by means of a diagram, for example: 

**==> picture [116 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 1<br>1 1<br>3 2<br>1<br>**----- End of picture text -----**<br>


Each diagram then corresponds to a unique _Q_ -matrix, in this case 

**==> picture [119 x 41] intentionally omitted <==**

Thus each off-diagonal entry _qij_ gives the value we attach to the ( _i, j_ ) arrow on the diagram, which we shall interpret later as the _rate of going from i to j_ . The numbers _qi_ are not shown on the diagram, but you can work them out from the other information given. We shall later interpret _qi_ as the _rate of leaving i_ . 

We may think of the discrete parameter space _{_ 0 _,_ 1 _,_ 2 _, . . . }_ as embedded in the continuous parameter space [0 _, ∞_ ). For _p ∈_ (0 _, ∞_ ) a natural way to interpolate the discrete sequence ( _p[n]_ : _n_ = 0 _,_ 1 _,_ 2 _, . . ._ ) is by the function ( _e[tq]_ : _t ≥_ 0), where _q_ = log _p_ . Consider now a _finite_ set _I_ and a matrix 

_2. Continuous-time Markov chains I_ 

62 

_P_ = ( _pij_ : _i, j ∈ I_ ). Is there a natural way to fill in the gaps in the discrete sequence ( _P[n]_ : _n_ = 0 _,_ 1 _,_ 2 _, . . ._ )? 

For any matrix _Q_ = ( _qij_ : _i, j ∈ I_ ), the series 

**==> picture [35 x 31] intentionally omitted <==**

converges componentwise and we denote its limit by _e[Q]_ . Moreover, if two matrices _Q_ 1 and _Q_ 2 commute, then 

**==> picture [87 x 11] intentionally omitted <==**

The proofs of these assertions follow the scalar case closely and are given in Section 2.10. Suppose then that we can find a matrix _Q_ with _e[Q]_ = _P_ . Then 

**==> picture [90 x 14] intentionally omitted <==**

so ( _e[tQ]_ : _t ≥_ 0) fills in the gaps in the discrete sequence. 

**Theorem 2.1.1.** _Let Q be a matrix on a finite set I. Set P_ ( _t_ ) = _e[tQ] . Then_ ( _P_ ( _t_ ) : _t ≥_ 0) _has the following properties:_ 

- (i) _P_ ( _s_ + _t_ ) = _P_ ( _s_ ) _P_ ( _t_ ) _for all s, t (semigroup property);_ 

(ii) ( _P_ ( _t_ ) : _t ≥_ 0) _is the unique solution to the forward equation_ 

**==> picture [154 x 24] intentionally omitted <==**

(iii) ( _P_ ( _t_ ) : _t ≥_ 0) _is the unique solution to the backward equation_ 

**==> picture [154 x 23] intentionally omitted <==**

(iv) _for k_ = 0 _,_ 1 _,_ 2 _, . . . , we have_ 

**==> picture [108 x 30] intentionally omitted <==**

_Proof._ For any _s, t ∈_ R, _sQ_ and _tQ_ commute, so 

**==> picture [82 x 11] intentionally omitted <==**

proving the semigroup property. The matrix-valued power series 

**==> picture [83 x 32] intentionally omitted <==**

_2.1 Q-matrices and their exponentials_ 

63 

has infinite radius of convergence (see Section 2.10). So each component is differentiable with derivative given by term-by-term differentiation: 

**==> picture [188 x 31] intentionally omitted <==**

Hence _P_ ( _t_ ) satisfies the forward and backward equations. Moreover by repeated term-by-term differentiation we obtain (iv). It remains to show that _P_ ( _t_ ) is the only solution of the forward and backward equations. But if _M_ ( _t_ ) satisfies the forward equation, then 

**==> picture [250 x 44] intentionally omitted <==**

so _M_ ( _t_ ) _e[−][tQ]_ is constant, and so _M_ ( _t_ ) = _P_ ( _t_ ). A similar argument proves uniqueness for the backward equation. 

The last result was about matrix exponentials in general. Now let us see what happens to _Q_ -matrices. Recall that a matrix _P_ = ( _pij_ : _i, j ∈ I_ ) is stochastic if it 

**==> picture [147 x 42] intentionally omitted <==**

We recall the convention that in the limit _t →_ 0 the statement _f_ ( _t_ ) = _O_ ( _t_ ) means that _f_ ( _t_ ) _/t ≤ C_ for all sufficiently small _t_ , for some _C < ∞_ . Later we shall also use the convention that _f_ ( _t_ ) = _o_ ( _t_ ) means _f_ ( _t_ ) _/t →_ 0 as _t →_ 0. 

**Theorem 2.1.2.** _A matrix Q on a finite set I is a Q-matrix if and only if P_ ( _t_ ) = _e[tQ] is a stochastic matrix for all t ≥_ 0 _._ 

_Proof._ As _t ↓_ 0 we have 

**==> picture [108 x 14] intentionally omitted <==**

so _qij ≥_ 0 for _i ̸_ = _j_ if and only if _pij_ ( _t_ ) _≥_ 0 for all _i, j_ and _t ≥_ 0 sufficiently small. Since _P_ ( _t_ ) = _P_ ( _t/n_ ) _[n]_ for all _n_ , it follows that _qij ≥_ 0 for _i_ = _j_ if and only if _pij_ ( _t_ ) _≥_ 0 for all _i, j_ and _all t ≥_ 0. 

If _Q_ has zero row sums then so does _Q[n]_ for every _n_ : 

**==> picture [249 x 27] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

64 

So 

**==> picture [169 x 32] intentionally omitted <==**

On the other hand, if[�] _j∈I[p][ij]_[(] _[t]_[) = 1][for][all] _[t][ ≥]_[0,][then] 

**==> picture [146 x 32] intentionally omitted <==**

Now, if _P_ is a stochastic matrix of the form _e[Q]_ for some _Q_ -matrix, we can do some sort of filling-in of gaps at the level of processes. Fix some large integer _m_ and let ( _Xn[m]_[)] _[n][≥]_[0][be][discrete-time][Markov(] _[λ, e][Q/m]_[).][We] define a process indexed by _{n/m_ : _n_ = 0 _,_ 1 _,_ 2 _, . . . }_ by 

**==> picture [64 x 13] intentionally omitted <==**

Then ( _Xn_ : _n_ = 0 _,_ 1 _,_ 2 _, . . ._ ) is discrete-time Markov( _λ,_ ( _e[Q/m]_ ) _[m]_ ) (see Exercise 1.1.2) and 

**==> picture [95 x 14] intentionally omitted <==**

Thus we can find discrete-time Markov chains with arbitrarily fine grids _{n/m_ : _n_ = 0 _,_ 1 _,_ 2 _, . . . }_ as time-parameter sets which give rise to Markov( _λ, P_ ) when sampled at integer times. It should not then be too surprising that there is, as we shall see in Section 2.8, a continuous-time process ( _Xt_ ) _t≥_ 0 which also has this property. 

To anticipate a little, we shall see in Section 2.8 that a continuous-time Markov chain ( _Xt_ ) _t≥_ 0 with _Q_ -matrix _Q_ satisfies 

**==> picture [298 x 13] intentionally omitted <==**

for all _n_ = 0 _,_ 1 _,_ 2 _, . . ._ , all times 0 _≤ t_ 0 _≤ . . . ≤ tn_ +1 and all states _i_ 0 _, . . . , in_ +1, where _pij_ ( _t_ ) is the ( _i, j_ ) entry in _e[tQ]_ . In particular, the _transition probability_ from _i_ to _j_ in time _t_ is given by 

**==> picture [203 x 13] intentionally omitted <==**

(Recall that := means ‘defined to equal’.) You should compare this with the defining property of a discrete-time Markov chain given in Section 1.1. We shall now give some examples where the transition probabilities _pij_ ( _t_ ) may be calculated explicitly. 

_2.1 Q-matrices and their exponentials_ 

65 

## **Example 2.1.3** 

We calculate _p_ 11( _t_ ) for the continuous-time Markov chain with _Q_ -matrix 

**==> picture [119 x 40] intentionally omitted <==**

The method is similar to that of Example 1.1.6. We begin by writing down the characteristic equation for _Q_ : 

**==> picture [166 x 12] intentionally omitted <==**

This shows that _Q_ has distinct eigenvalues 0 _, −_ 2 _, −_ 4. Then _p_ 11( _t_ ) has the form 

**==> picture [124 x 14] intentionally omitted <==**

for some constants _a_ , _b_ and _c_ . (This is because we could diagonalize _Q_ by an invertible matrix _U_ : 

**==> picture [143 x 40] intentionally omitted <==**

Then 

**==> picture [220 x 120] intentionally omitted <==**

so _p_ 11( _t_ ) must have the form claimed.) To determine the constants we use 

**==> picture [147 x 50] intentionally omitted <==**

so 

**==> picture [134 x 15] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

66 

**==> picture [251 x 28] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ λ λ<br>0 1 2 N − 1 N<br>**----- End of picture text -----**<br>


## **Example 2.1.4** 

We calculate _pij_ ( _t_ ) for the continuous-time Markov chain with diagram given above. The _Q_ -matrix is 

**==> picture [179 x 81] intentionally omitted <==**

where entries off the diagonal and super-diagonal are all zero. The exponential of an upper-triangular matrix is upper-triangular, so _pij_ ( _t_ ) = 0 for _i > j_ . In components the forward equation _P[′]_ ( _t_ ) = _P_ ( _t_ ) _Q_ reads 

**==> picture [310 x 47] intentionally omitted <==**

We can solve these equations. First, _pii_ ( _t_ ) = _e[−][λt]_ for _i < N_ . Then, for _i < j < N_ 

**==> picture [121 x 14] intentionally omitted <==**

so, by induction 

**==> picture [102 x 28] intentionally omitted <==**

If _i_ = 0, these are the Poisson probabilities of parameter _λt_ . So, starting from 0, the distribution of the Markov chain at time _t_ is the same as the distribution of min _{Yt, N }_ , where _Yt_ is a Poisson random variable of parameter _λt_ . 

## **Exercises** 

**2.1.1** Compute _p_ 11( _t_ ) for _P_ ( _t_ ) = _e[tQ]_ , where 

**==> picture [116 x 41] intentionally omitted <==**

_2.2 Continuous-time random processes_ 

67 

**2.1.2** Which of the following matrices is the exponential of a _Q_ -matrix? 

**==> picture [259 x 27] intentionally omitted <==**

What consequences do your answers have for the discrete-time Markov chains with these transition matrices? 

## **2.2 Continuous-time random processes** 

Let _I_ be a countable set. A _continuous-time random process_ 

**==> picture [132 x 13] intentionally omitted <==**

with values in _I_ is a family of random variables _Xt_ : Ω _→ I_ . We are going to consider ways in which we might specify the probabilistic behaviour (or _law_ ) of ( _Xt_ ) _t≥_ 0. These should enable us to find, at least in principle, any probability connected with the process, such as P( _Xt_ = _i_ ) or P( _Xt_ 0 = _i_ 0 _, . . . , Xtn_ = _in_ ), or P( _Xt_ = _i_ for some _t_ ). There are subtleties in this problem not present in the discrete-time case. They arise because, for a countable disjoint union 

**==> picture [120 x 33] intentionally omitted <==**

whereas for an uncountable union[�] _t≥_ 0 _[A][t]_[there][is][no][such][rule.][To][avoid] these subtleties as far as possible we shall restrict our attention to processes ( _Xt_ ) _t≥_ 0 which are _right-continuous_ . This means in this context that for all _ω ∈_ Ωand _t ≥_ 0 there exists _ε >_ 0 such that 

**==> picture [176 x 12] intentionally omitted <==**

By a standard result of measure theory, which is proved in Section 6.6, the probability of any event depending on a right-continuous process can be determined from its _finite-dimensional distributions_ , that is, from the probabilities 

**==> picture [171 x 13] intentionally omitted <==**

**==> picture [311 x 11] intentionally omitted <==**

**==> picture [358 x 26] intentionally omitted <==**

where _q_ 1 _, q_ 2 _, . . ._ is an enumeration of the rationals. 

_2. Continuous-time Markov chains I_ 

68 

Every path _t �→ Xt_ ( _ω_ ) of a right-continuous process must remain constant for a while in each new state, so there are three possibilities for the sorts of path we get. In the first case the path makes infinitely many jumps, but only finitely many in any interval [0 _, t_ ]: 

**==> picture [353 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xt ( ω )<br>J 0 = 0 J 1 J 2 J 3 J 4 J 5 t<br>S 1 S 2 S 3 S 4 S 5 S 6<br>**----- End of picture text -----**<br>


The second case is where the path makes finitely many jumps and then becomes stuck in some state forever: 

**==> picture [353 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xt ( ω )<br>J 0 = 0 J 1 J 2 t<br>S 1 S 2 S 3 =  ∞<br>**----- End of picture text -----**<br>


In the third case the process makes infinitely many jumps in a finite interval; this is illustrated below. In this case, after the explosion time _ζ_ the process starts up again; it may explode again, maybe infinitely often, or it may not. 

_2.2 Continuous-time random processes_ 

69 

**==> picture [353 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xt ( ω )<br>J 0 = 0 J 1 J 2 J 3 J 4 J 5 ζ t<br>S 1 S 2 S 3 S 4  S 5<br>**----- End of picture text -----**<br>


We call _J_ 0 _, J_ 1 _, . . ._ the _jump times_ of ( _Xt_ ) _t≥_ 0 and _S_ 1 _, S_ 2 _, . . ._ the _holding times_ . They are obtained from ( _Xt_ ) _t≥_ 0 by 

**==> picture [197 x 12] intentionally omitted <==**

for _n_ = 0 _,_ 1 _, . . ._ , where inf _∅_ = _∞_ , and, for _n_ = 1 _,_ 2 _, . . ._ , 

**==> picture [159 x 27] intentionally omitted <==**

Note that right-continuity forces _Sn >_ 0 for all _n_ . If _Jn_ +1 = _∞_ for some _n_ , we define _X∞_ = _XJn_ , the final value, otherwise _X∞_ is undefined. The ( _first_ ) _explosion time ζ_ is defined by 

**==> picture [100 x 31] intentionally omitted <==**

The discrete-time process ( _Yn_ ) _n≥_ 0 given by _Yn_ = _XJn_ is called the _jump process_ of ( _Xt_ ) _t≥_ 0, or the _jump chain_ if it is a discrete-time Markov chain. This is simply the sequence of values taken by ( _Xt_ ) _t≥_ 0 up to explosion. 

We shall not consider what happens to a process after explosion. So it is convenient to adjoin to _I_ a new state, _∞_ say, and require that _Xt_ = _∞_ if _t ≥ ζ_ . Any process satisfying this requirement is called _minimal_ . The terminology ‘minimal’ does not refer to the state of the process but to the 

_2. Continuous-time Markov chains I_ 

70 

interval of time over which the process is active. Note that a minimal process may be reconstructed from its holding times and jump process. Thus by specifying the joint distribution of _S_ 1 _, S_ 2 _, . . ._ and ( _Yn_ ) _n≥_ 0 we have another ‘countable’ specification of the probabilistic behaviour of ( _Xt_ ) _t≥_ 0. For example, the probability that _Xt_ = _i_ is given by 

**==> picture [220 x 31] intentionally omitted <==**

and 

P( _Xt_ = _i_ for some _t ∈_ [0 _, ∞_ )) = P( _Yn_ = _i_ for some _n ≥_ 0) _._ 

## **2.3 Some properties of the exponential distribution** 

A random variable _T_ : Ω _→_ [0 _, ∞_ ] has _exponential distribution of parameter λ_ (0 _≤ λ < ∞_ ) if 

**==> picture [148 x 13] intentionally omitted <==**

We write _T ∼ E_ ( _λ_ ) for short. If _λ >_ 0, then _T_ has density function 

**==> picture [92 x 14] intentionally omitted <==**

The mean of _T_ is given by 

**==> picture [148 x 26] intentionally omitted <==**

The exponential distribution plays a fundamental role in continuous-time Markov chains because of the following results. 

**Theorem 2.3.1 (Memoryless property).** _A random variable T_ : Ω _→_ (0 _, ∞_ ] _has an exponential distribution if and only if it has the following memoryless property:_ 

**==> picture [234 x 12] intentionally omitted <==**

_Proof._ Suppose _T ∼ E_ ( _λ_ ), then 

**==> picture [327 x 29] intentionally omitted <==**

_2.3 Some properties of the exponential distribution_ 

71 

On the other hand, suppose _T_ has the memoryless property whenever P( _T > s_ ) _>_ 0. Then _g_ ( _t_ ) = P( _T > t_ ) satisfies 

**==> picture [170 x 12] intentionally omitted <==**

We assumed _T >_ 0 so that _g_ (1 _/n_ ) _>_ 0 for some _n_ . Then, by induction 

**==> picture [190 x 28] intentionally omitted <==**

so _g_ (1) = _e[−][λ]_ for some 0 _≤ λ < ∞_ . By the same argument, for integers _p, q ≥_ 1 

**==> picture [129 x 14] intentionally omitted <==**

so _g_ ( _r_ ) = _e[−][λr]_ for all rationals _r >_ 0. For real _t >_ 0, choose rationals _r, s >_ 0 with _r ≤ t ≤ s_ . Since _g_ is decreasing, 

**==> picture [160 x 14] intentionally omitted <==**

and, since we can choose _r_ and _s_ arbitrarily close to _t_ , this forces _g_ ( _t_ ) = _e[−][λt]_ , so _T ∼ E_ ( _λ_ ). 

The next result shows that a sum of independent exponential random variables is either certain to be finite or certain to be infinite, and gives a criterion for deciding which is true. This will be used to determine whether or not certain continuous-time Markov chains can take infinitely many jumps in a time. 

**Theorem 2.3.2.** _Let S_ 1 _, S_ 2 _, . . . be a sequence of independent random variables with Sn ∼ E_ ( _λn_ ) _and_ 0 _< λn < ∞ for all n._ 

**==> picture [229 x 70] intentionally omitted <==**

_Proof._ (i) Suppose[�] _[∞] n_ =1[1] _[/λ][n][<][ ∞]_[.][Then,][by][monotone][convergence] 

**==> picture [132 x 34] intentionally omitted <==**

so 

**==> picture [107 x 34] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

72 

(ii) Suppose instead that[�] _[∞] n_ =1[1] _[/λ][n]_[=] _[∞]_[.][Then][�] _[∞] n_ =1[(1 + 1] _[/λ][n]_[)][=] _[∞]_[.] By monotone convergence and independence 

**==> picture [325 x 34] intentionally omitted <==**

so 

**==> picture [107 x 34] intentionally omitted <==**

The following result is fundamental to continuous-time Markov chains. 

**Theorem 2.3.3.** _Let I be a countable set and let Tk, k ∈ I, be independent random variables with Tk ∼ E_ ( _qk_ ) _and_ 0 _< q_ :=[�] _k∈I[q][k][<][∞][.] Set T_ = inf _k Tk. Then this infimum is attained at a unique random value K of k, with probability_ 1 _. Moreover, T and K are independent, with T ∼ E_ ( _q_ ) _and_ P( _K_ = _k_ ) = _qk/q._ 

_Proof._ Set _K_ = _k_ if _Tk < Tj_ for all _j_ = _k_ , otherwise let _K_ be undefined. Then 

**==> picture [203 x 126] intentionally omitted <==**

Hence P( _K_ = _k_ for some _k_ ) = 1 and _T_ and _K_ have the claimed joint distribution. 

The following identity is the simplest case of an identity used in Section 2.8 in proving the forward equations for a continuous-time Markov chain. 

**Theorem 2.3.4.** _For independent random variables S ∼ E_ ( _λ_ ) _and R ∼ E_ ( _µ_ ) _and for t ≥_ 0 _, we have_ 

**==> picture [202 x 12] intentionally omitted <==**

_2.4 Poisson processes_ 

73 

_Proof._ We have 

**==> picture [352 x 28] intentionally omitted <==**

from which the identity follows by symmetry. 

## **Exercises** 

**2.3.1** Suppose _S_ and _T_ are independent exponential random variables of parameters _α_ and _β_ respectively. What is the distribution of min _{S, T }_ ? What is the probability that _S ≤ T_ ? Show that the two events _{S < T }_ and _{_ min _{S, T } ≥ t}_ are independent. 

**2.3.2** Let _T_ 1 _, T_ 2 _, . . ._ be independent exponential random variables of parameter _λ_ and let _N_ be an independent geometric random variable with 

**==> picture [210 x 13] intentionally omitted <==**

Show that _T_ =[�] _[N] i_ =1 _[T][i]_[has][exponential][distribution][of][parameter] _[λβ]_[.] 

**2.3.3** Let _S_ 1 _, S_ 2 _, . . ._ be independent exponential random variables with parameters _λ_ 1 _, λ_ 2 _, . . ._ respectively. Show that _λ_ 1 _S_ 1 is exponential of parameter 1. 

Use the strong law of large numbers to show, first in the special case _λn_ = 1 for all _n_ , and then subject only to the condition sup _n λn < ∞_ , that 

**==> picture [108 x 33] intentionally omitted <==**

Is the condition sup _n λn < ∞_ absolutely necessary? 

## **2.4 Poisson processes** 

Poisson processes are some of the simplest examples of continuous-time Markov chains. We shall also see that they may serve as building blocks for the most general continuous-time Markov chain. Moreover, a Poisson process is the natural probabilistic model for any uncoordinated stream of discrete events in continuous time. So we shall study Poisson processes first, both as a gentle warm-up for the general theory and because they are useful in themselves. The key result is Theorem 2.4.3, which provides three different descriptions of a Poisson process. The reader might well begin with the statement of this result and then see how it is used in the 

_2. Continuous-time Markov chains I_ 

74 

theorems and examples that follow. We shall begin with a definition in terms of jump chain and holding times (see Section 2.2). A right-continuous process ( _Xt_ ) _t≥_ 0 with values in _{_ 0 _,_ 1 _,_ 2 _, . . . }_ is a _Poisson process of rate λ_ (0 _< λ < ∞_ ) if its holding times _S_ 1 _, S_ 2 _, . . ._ are independent exponential random variables of parameter _λ_ and its jump chain is given by _Yn_ = _n_ . Here is the diagram: 

**==> picture [223 x 27] intentionally omitted <==**

The associated _Q_ -matrix is given by 

**==> picture [162 x 68] intentionally omitted <==**

By Theorem 2.3.2 (or the strong law of large numbers) we have P( _Jn →∞_ ) = 1 so there is no explosion and the law of ( _Xt_ ) _t≥_ 0 is uniquely determined. A simple way to construct a Poisson process of rate _λ_ is to take a sequence _S_ 1 _, S_ 2 _, . . ._ of independent exponential random variables of parameter _λ_ , to set _J_ 0 = 0, _Jn_ = _S_ 1 + _. . ._ + _Sn_ and then set 

**==> picture [135 x 12] intentionally omitted <==**

**==> picture [341 x 203] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xt<br>5<br>4<br>3<br>2<br>1<br>0<br>J 0 = 0 J 1 J 2 J 3 J 4 J 5 t<br>S 1 S 2 S 3 S 4 S 5 S 6<br>**----- End of picture text -----**<br>


_2.4 Poisson processes_ 

75 

The diagram illustrates a typical path. We now show how the memoryless property of the exponential holding times, Theorem 2.3.1, leads to a memoryless property of the Poisson process. 

**Theorem 2.4.1 (Markov property).** _Let_ ( _Xt_ ) _t≥_ 0 _be a Poisson process of rate λ. Then, for any s ≥_ 0 _,_ ( _Xs_ + _t − Xs_ ) _t≥_ 0 _is also a Poisson process of rate λ, independent of_ ( _Xr_ : _r ≤ s_ ) _._ 

_Proof._ It suffices to prove the claim conditional on the event _Xs_ = _i_ , for each _i ≥_ 0. Set _X_[�] _t_ = _Xs_ + _t − Xs_ . We have 

**==> picture [280 x 12] intentionally omitted <==**

On this event 

**==> picture [139 x 34] intentionally omitted <==**

and the holding times _S_[�] 1 _, S_[�] 2 _, . . ._ of ( _X_[�] _t_ ) _t≥_ 0 are given by 

**==> picture [219 x 14] intentionally omitted <==**

as shown in the diagram. 

**==> picture [312 x 111] intentionally omitted <==**

Recall that the holding times _S_ 1 _, S_ 2 _, . . ._ are independent _E_ ( _λ_ ). Condition on _S_ 1 _, . . . , Si_ and _{Xs_ = _i}_ , then by the memoryless property of _Si_ +1 and independence, _S_[�] 1 _, S_[�] 2 _, . . ._ are themselves independent _E_ ( _λ_ ). Hence, conditional on _{Xs_ = _i}_ , _S_[�] 1 _, S_[�] 2 _, . . ._ are independent _E_ ( _λ_ ), and independent of _S_ 1 _, . . . , Si_ . Hence, conditional on _{Xs_ = _i}_ , ( _X_[�] _t_ ) _t≥_ 0 is a Poisson process of rate _λ_ and independent of ( _Xr_ : _r ≤ s_ ). 

In fact, we shall see in Section 6.5, by an argument in essentially the same spirit that the result also holds with _s_ replaced by any stopping time _T_ of ( _Xt_ ) _t≥_ 0. 

_2. Continuous-time Markov chains I_ 

76 

**Theorem 2.4.2 (Strong Markov property).** _Let_ ( _Xt_ ) _t≥_ 0 _be a Poisson process of rate λ and let T be a stopping time of_ ( _Xt_ ) _t≥_ 0 _. Then, conditional on T < ∞,_ ( _XT_ + _t − XT_ ) _t≥_ 0 _is also a Poisson process of rate λ, independent of_ ( _Xs_ : _s ≤ T_ ) _._ 

Here is some standard terminology. If ( _Xt_ ) _t≥_ 0 is a real-valued process, we can consider its _increment Xt − Xs_ over any interval ( _s, t_ ]. We say that ( _Xt_ ) _t≥_ 0 has _stationary_ increments if the distribution of _Xs_ + _t − Xs_ depends only on _t ≥_ 0. We say that ( _Xt_ ) _t≥_ 0 has _independent_ increments if its increments over any finite collection of disjoint intervals are independent. 

We come to the key result for the Poisson process, which gives two conditions equivalent to the jump chain/holding time characterization which we took as our original definition. Thus we have three alternative definitions of the same process. 

**Theorem 2.4.3.** _Let_ ( _Xt_ ) _t≥_ 0 _be an increasing, right-continuous integervalued process starting from_ 0 _. Let_ 0 _< λ < ∞. Then the following three conditions are equivalent:_ 

- (a) (jump chain/holding time definition) _the holding times S_ 1 _, S_ 2 _, . . . of_ ( _Xt_ ) _t≥_ 0 _are independent exponential random variables of parameter λ and the jump chain is given by Yn_ = _n for all n;_ 

- (b) (infinitesimal definition) ( _Xt_ ) _t≥_ 0 _has independent increments and, as h ↓_ 0 _, uniformly in t,_ 

P( _Xt_ + _h − Xt_ = 0) = 1 _− λh_ + _o_ ( _h_ ) _,_ P( _Xt_ + _h − Xt_ = 1) = _λh_ + _o_ ( _h_ ); 

- (c) (transition probability definition) ( _Xt_ ) _t≥_ 0 _has stationary independent increments and, for each t, Xt has Poisson distribution of parameter λt._ 

- If ( _Xt_ ) _t≥_ 0 satisfies any of these conditions then it is called a _Poisson process of rate λ_ . 

_Proof._ (a) _⇒_ (b) If (a) holds, then, by the Markov property, for any _t, h ≥_ 0, the increment _Xt_ + _h−Xt_ has the same distribution as _Xh_ and is independent of ( _Xs_ : _s ≤ t_ ). So ( _Xt_ ) _t≥_ 0 has independent increments and as _h ↓_ 0 

**==> picture [334 x 49] intentionally omitted <==**

which implies (b). 

_2.4 Poisson processes_ 

77 

(b) _⇒_ (c) If (b) holds, then, for _i_ = 2 _,_ 3 _, . . ._ , we have P( _Xt_ + _h − Xt_ = _i_ ) = _o_ ( _h_ ) as _h ↓_ 0, uniformly in _t_ . Set _pj_ ( _t_ ) = P( _Xt_ = _j_ ). Then, for _j_ = 1 _,_ 2 _, . . ._ , 

**==> picture [357 x 51] intentionally omitted <==**

so 

**==> picture [226 x 24] intentionally omitted <==**

Since this estimate is uniform in _t_ we can put _t_ = _s − h_ to obtain for all _s ≥ h_ 

**==> picture [270 x 24] intentionally omitted <==**

Now let _h ↓_ 0 to see that _pj_ ( _t_ ) is first continuous and then differentiable and satisfies the differential equation 

**==> picture [133 x 14] intentionally omitted <==**

By a simpler argument we also find 

**==> picture [79 x 12] intentionally omitted <==**

Since _X_ 0 = 0 we have initial conditions 

**==> picture [193 x 12] intentionally omitted <==**

As we saw in Example 2.1.4, this system of equations has a unique solution given by 

**==> picture [182 x 27] intentionally omitted <==**

Hence _Xt ∼ P_ ( _λt_ ). If ( _Xt_ ) _t≥_ 0 satisfies (b), then certainly ( _Xt_ ) _t≥_ 0 has independent increments, but also ( _Xs_ + _t − Xs_ ) _t≥_ 0 satisfies (b), so the above argument shows _Xs_ + _t − Xs ∼ P_ ( _λt_ ), for any _s_ , which implies (c). (c) _⇒_ (a) There is a process satisfying (a) and we have shown that it must then satisfy (c). But condition (c) determines the finite-dimensional distributions of ( _Xt_ ) _t≥_ 0 and hence the distribution of jump chain and holding times. So if one process satisfying (c) also satisfies (a), so must every process satisfying (c). 

The differential equations which appeared in the proof are really the forward equations for the Poisson process. To make this clear, consider the 

_2. Continuous-time Markov chains I_ 

78 

possibility of starting the process from _i_ at time 0, writing P _i_ as a reminder, and set 

**==> picture [96 x 13] intentionally omitted <==**

Then, by spatial homogeneity _pij_ ( _t_ ) = _pj−i_ ( _t_ ), and we could rewrite the differential equations as 

**==> picture [216 x 31] intentionally omitted <==**

or, in matrix form, for _Q_ as above, 

**==> picture [142 x 13] intentionally omitted <==**

Theorem 2.4.3 contains a great deal of information about the Poisson process of rate _λ_ . It can be useful when trying to decide whether a given process is a Poisson process as it gives you three alternative conditions to check, and it is likely that one will be easier to check than another. On the other hand it can also be useful when answering a question about a given Poisson process as this question may be more closely connected to one definition than another. For example, you might like to consider the difficulties in approaching the next result using the jump chain/holding time definition. 

**Theorem 2.4.4.** _If_ ( _Xt_ ) _t≥_ 0 _and_ ( _Yt_ ) _t≥_ 0 _are independent Poisson processes of rates λ and µ, respectively, then_ ( _Xt_ + _Yt_ ) _t≥_ 0 _is a Poisson process of rate λ_ + _µ._ 

_Proof._ We shall use the infinitesimal definition, according to which ( _Xt_ ) _t≥_ 0 and ( _Yt_ ) _t≥_ 0 have independent increments and, as _h ↓_ 0, uniformly in _t_ , 

**==> picture [332 x 29] intentionally omitted <==**

Set _Zt_ = _Xt_ + _Yt_ . Then, since ( _Xt_ ) _t≥_ 0 and ( _Yt_ ) _t≥_ 0 are independent, ( _Zt_ ) _t≥_ 0 has independent increments and, as _h ↓_ 0, uniformly in _t_ , 

**==> picture [360 x 97] intentionally omitted <==**

Hence ( _Zt_ ) _t≥_ 0 is a Poisson process of rate _λ_ + _µ_ . 

_2.4 Poisson processes_ 

79 

Next we establish some relations between Poisson processes and the uniform distribution. Notice that the conclusions are independent of the rate of the process considered. The results say in effect that the jumps of a Poisson process are as randomly distributed as possible. 

**Theorem 2.4.5.** _Let_ ( _Xt_ ) _t≥_ 0 _be a Poisson process. Then, conditional on_ ( _Xt_ ) _t≥_ 0 _having exactly one jump in the interval_ [ _s, s_ + _t_ ] _, the time at which that jump occurs is uniformly distributed on_ [ _s, s_ + _t_ ] _._ 

_Proof._ We shall use the finite-dimensional distribution definition. By stationarity of increments, it suffices to consider the case _s_ = 0. Then, for 0 _≤ u ≤ t_ , 

**==> picture [264 x 48] intentionally omitted <==**

**Theorem 2.4.6.** _Let_ ( _Xt_ ) _t≥_ 0 _be a Poisson process. Then, conditional on the event {Xt_ = _n}, the jump times J_ 1 _, . . . , Jn have joint density function_ 

**==> picture [181 x 13] intentionally omitted <==**

_Thus, conditional on {Xt_ = _n}, the jump times J_ 1 _, . . . , Jn have the same distribution as an ordered sample of size n from the uniform distribution on_ [0 _, t_ ] _._ 

_Proof._ The holding times _S_ 1 _, . . . , Sn_ +1 have joint density function 

**==> picture [165 x 15] intentionally omitted <==**

so the jump times _J_ 1 _, . . . , Jn_ +1 have joint density function 

**==> picture [136 x 15] intentionally omitted <==**

So for _A ⊆_ R _[n]_ we have 

**==> picture [358 x 46] intentionally omitted <==**

and since P( _Xt_ = _n_ ) = _e[−][λt]_ ( _λt_ ) _[n] /n_ ! we obtain 

**==> picture [276 x 26] intentionally omitted <==**

as required. 

_2. Continuous-time Markov chains I_ 

80 

We finish with a simple example typical of many problems making use of a range of properties of the Poisson process. 

## **Example 2.4.7** 

Robins and blackbirds make brief visits to my birdtable. The probability that in any small interval of duration _h_ a robin will arrive is found to be _ρh_ + _o_ ( _h_ ), whereas the corresponding probability for blackbirds is _βh_ + _o_ ( _h_ ). What is the probability that the first two birds I see are both robins? What is the distribution of the total number of birds seen in time _t_ ? Given that this number is _n_ , what is the distribution of the number of blackbirds seen in time _t_ ? 

By the infinitesimal characterization, the number of robins seen by time _t_ is a Poisson process ( _Rt_ ) _t≥_ 0 of rate _ρ_ , and the number of blackbirds is a Poisson process ( _Bt_ ) _t≥_ 0 of rate _β_ . The times spent waiting for the first robin or blackbird are independent exponential random variables _S_ 1 and _T_ 1 of parameters _ρ_ and _β_ respectively. So a robin arrives first with probability _ρ/_ ( _ρ_ + _β_ ) and, by the memoryless property of _T_ 1, the probability that the first two birds are robins is _ρ_[2] _/_ ( _ρ_ + _β_ )[2] . By Theorem 2.4.4 the total number of birds seen in an interval of duration _t_ has Poisson distribution of parameter ( _ρ_ + _β_ ) _t_ . Finally 

**==> picture [352 x 79] intentionally omitted <==**

so if _n_ birds are seen in time _t_ , then the distribution of the number of blackbirds is binomial of parameters _n_ and _β/_ ( _ρ_ + _β_ ). 

## **Exercises** 

**2.4.1** State the transition probability definition of a Poisson process. Show directly from this definition that the first jump time _J_ 1 of a Poisson process of rate _λ_ is exponential of parameter _λ_ . 

Show also (from the same definition and without assuming the strong Markov property) that 

**==> picture [232 x 14] intentionally omitted <==**

and hence that _J_ 2 _− J_ 1 is also exponential of parameter _λ_ and independent of _J_ 1. 

_2.5 Birth processes_ 

81 

**2.4.2** Show directly from the infinitesimal definition that the first jump time _J_ 1 of a Poisson process of rate _λ_ has exponential distribution of parameter _λ_ . 

**2.4.3** Arrivals of the Number 1 bus form a Poisson process of rate one bus per hour, and arrivals of the Number 7 bus form an independent Poisson process of rate seven buses per hour. 

- (a) What is the probability that exactly three buses pass by in one hour? 

- (b) What is the probability that exactly three Number 7 buses pass by while I am waiting for a Number 1? 

- (c) When the maintenance depot goes on strike half the buses break down before they reach my stop. What, then, is the probability that I wait for 30 minutes without seeing a single bus? 

**2.4.4** A radioactive source emits particles in a Poisson process of rate _λ_ . The particles are each emitted in an independent random direction. A Geiger counter placed near the source records a fraction _p_ of the particles emitted. What is the distribution of the number of particles recorded in time _t_ ? 

**2.4.5** A pedestrian wishes to cross a single lane of fast-moving traffic. Suppose the number of vehicles that have passed by time _t_ is a Poisson process of rate _λ_ , and suppose it takes time _a_ to walk across the lane. Assuming that the pedestrian can foresee correctly the times at which vehicles will pass by, how long on average does it take to cross over safely? [ _Consider the time at which the first car passes._ ] 

How long on average does it take to cross two similar lanes (a) when one must walk straight across (assuming that the pedestrian will not cross if, at any time whilst crossing, a car would pass in either direction), (b) when an island in the middle of the road makes it safe to stop half-way? 

## **2.5 Birth processes** 

A birth process is a generalization of a Poisson process in which the parameter _λ_ is allowed to depend on the current state of the process. The data for a birth process consist of _birth rates_ 0 _≤ qj < ∞_ , where _j_ = 0 _,_ 1 _,_ 2 _, . . ._ . We begin with a definition in terms of jump chain and holding times. A minimal right-continuous process ( _Xt_ ) _t≥_ 0 with values in _{_ 0 _,_ 1 _,_ 2 _, . . . }∪{∞}_ is a _birth process of rates_ ( _qj_ : _j ≥_ 0) if, conditional on _X_ 0 = _i_ , its holding times _S_ 1 _, S_ 2 _, . . ._ are independent exponential random variables of parameters _qi, qi_ +1 _, . . . ,_ respectively, and its jump chain is given by _Yn_ = _i_ + _n_ . 

_2. Continuous-time Markov chains I_ 

82 

**==> picture [223 x 26] intentionally omitted <==**

The flow diagram is shown above and the _Q_ -matrix is given by: 

**==> picture [198 x 93] intentionally omitted <==**

## **Example 2.5.1 (Simple birth process)** 

Consider a population in which each individual gives birth after an exponential time of parameter _λ_ , all independently. If _i_ individuals are present then the first birth will occur after an exponential time of parameter _iλ_ . Then we have _i_ + 1 individuals and, by the memoryless property, the process begins afresh. Thus the size of the population performs a birth process with rates _qi_ = _iλ_ . Let _Xt_ denote the number of individuals at time _t_ and suppose _X_ 0 = 1. Write _T_ for the time of the first birth. Then 

**==> picture [203 x 45] intentionally omitted <==**

Put _µ_ ( _t_ ) = E( _Xt_ ), then E( _Xt | T_ = _s_ ) = 2 _µ_ ( _t − s_ ), so 

**==> picture [168 x 29] intentionally omitted <==**

and setting _r_ = _t − s_ 

**==> picture [148 x 29] intentionally omitted <==**

By differentiating we obtain 

**==> picture [63 x 12] intentionally omitted <==**

so the mean population size grows exponentially: 

**==> picture [62 x 14] intentionally omitted <==**

_2.5 Birth processes_ 

83 

Much of the theory associated with the Poisson process goes through for birth processes with little change, except that some calculations can no longer be made so explicitly. The most interesting new phenomenon present in birth processes is the possibility of explosion. For certain choices of birth rates, a typical path will make infinitely many jumps in a finite time, as shown in the diagram. The convention of setting the process to equal _∞_ after explosion is particularly appropriate for birth processes! 

**==> picture [341 x 268] intentionally omitted <==**

**----- Start of picture text -----**<br>
Xt<br>8<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>J 0 = 0 J 1 J 2 J 3 J 4 ζ t<br>S 1 S 2 S 3 S 4<br>**----- End of picture text -----**<br>


In fact, Theorem 2.3.2 tells us exactly when explosion will occur. 

**Theorem 2.5.2.** _Let_ ( _Xt_ ) _t≥_ 0 _be a birth process of rates_ ( _qj_ : _j ≥_ 0) _, starting from_ 0 _._ 

**==> picture [189 x 67] intentionally omitted <==**

_Proof._ Apply Theorem 2.3.2 to the sequence of holding times _S_ 1 _, S_ 2 _, . . ._ . 

The proof of the Markov property for the Poisson process is easily adapted to give the following generalization. 

_2. Continuous-time Markov chains I_ 

84 

**Theorem 2.5.3 (Markov property).** _Let_ ( _Xt_ ) _t≥_ 0 _be a birth process of rates_ ( _qj_ : _j ≥_ 0) _. Then, conditional on Xs_ = _i,_ ( _Xs_ + _t_ ) _t≥_ 0 _is a birth process of rates_ ( _qj_ : _j ≥_ 0) _starting from i and independent of_ ( _Xr_ : _r ≤ s_ ) _._ 

We shall shortly prove a theorem on birth processes which generalizes the key theorem on Poisson processes. First we must see what will replace the Poisson probabilities. In Theorem 2.4.3 these arose as the unique solution of a system of differential equations, which we showed were essentially the forward equations. Now we can still write down the forward equation 

**==> picture [131 x 13] intentionally omitted <==**

or, in components 

**==> picture [156 x 13] intentionally omitted <==**

and, for _j_ = 1 _,_ 2 _, . . ._ 

**==> picture [224 x 15] intentionally omitted <==**

Moreover, these equations still have a unique solution; it is just not as explicit as before. For we must have 

**==> picture [78 x 13] intentionally omitted <==**

which can be substituted in the equation 

**==> picture [197 x 12] intentionally omitted <==**

and this equation solved to give 

**==> picture [214 x 28] intentionally omitted <==**

Now we can substitute for _pi_ 1( _t_ ) in the next equation up the hierarchy and find an explicit expression for _pi_ 2( _t_ ), and so on. 

**Theorem 2.5.4.** _Let_ ( _Xt_ ) _t≥_ 0 _be an increasing, right-continuous process with values in {_ 0 _,_ 1 _,_ 2 _, . . . } ∪{∞}. Let_ 0 _≤ qj < ∞ for all j ≥_ 0 _. Then the following three conditions are equivalent:_ 

- (a) (jump chain/holding time definition) _conditional on X_ 0 = _i, the holding times S_ 1 _, S_ 2 _, . . . are independent exponential random variables of parameters qi, qi_ +1 _, . . . respectively and the jump chain is given by Yn_ = _i_ + _n for all n;_ 

_2.5 Birth processes_ 

85 

- (b) (infinitesimal definition) _for all t, h ≥_ 0 _, conditional on Xt_ = _i, Xt_ + _h is independent of_ ( _Xs_ : _s ≤ t_ ) _and, as h ↓_ 0 _, uniformly in t,_ 

**==> picture [185 x 29] intentionally omitted <==**

- (c) (transition probability definition) _for all n_ = 0 _,_ 1 _,_ 2 _, . . . , all times_ 0 _≤ t_ 0 _≤ . . . ≤ tn_ +1 _and all states i_ 0 _, . . . , in_ +1 

**==> picture [297 x 13] intentionally omitted <==**

_where_ ( _pij_ ( _t_ ) : _i, j_ = 0 _,_ 1 _,_ 2 _, . . ._ ) _is the unique solution of the forward equations._ 

If ( _Xt_ ) _t≥_ 0 satisfies any of these conditions then it is called a _birth process of rates_ ( _qj_ : _j ≥_ 0). 

_Proof._ (a) _⇒_ (b) If (a) holds, then, by the Markov property for any _t, h ≥_ 0, conditional on _Xt_ = _i_ , _Xt_ + _h_ is independent of ( _Xs_ : _s ≤ t_ ) and, as _h ↓_ 0, uniformly in _t_ , 

**==> picture [265 x 31] intentionally omitted <==**

and 

**==> picture [300 x 48] intentionally omitted <==**

which implies (b). 

- (b) _⇒_ (c) If (b) holds, then certainly for _k_ = _i_ + 2 _, i_ + 3 _, . . ._ 

**==> picture [261 x 12] intentionally omitted <==**

**==> picture [259 x 13] intentionally omitted <==**

**==> picture [162 x 12] intentionally omitted <==**

**==> picture [271 x 50] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

86 

so 

**==> picture [250 x 24] intentionally omitted <==**

As in the proof of Theorem 2.4.3, we can deduce that _pij_ ( _t_ ) is differentiable and satisfies the differential equation 

**==> picture [153 x 14] intentionally omitted <==**

By a simpler argument we also find 

**==> picture [89 x 12] intentionally omitted <==**

Thus ( _pij_ ( _t_ ) : _i, j_ = 0 _,_ 1 _,_ 2 _, . . ._ ) must be the unique solution to the forward equations. If ( _Xt_ ) _t≥_ 0 satisfies (b), then certainly 

**==> picture [339 x 13] intentionally omitted <==**

but also ( _Xtn_ + _t_ ) _t≥_ 0 satisfies (b), so 

**==> picture [231 x 13] intentionally omitted <==**

by uniqueness for the forward equations. Hence ( _Xt_ ) _t≥_ 0 satisfies (c). 

**==> picture [202 x 12] intentionally omitted <==**

## **Exercise** 

**2.5.1** Each bacterium in a colony splits into two identical bacteria after an exponential time of parameter _λ_ , which then split in the same way but independently. Let _Xt_ denote the size of the colony at time _t_ , and suppose _X_ 0 = 1. Show that the probability generating function _φ_ ( _t_ ) = E( _z[X][t]_ ) 

**==> picture [178 x 28] intentionally omitted <==**

Make a change of variables _u_ = _t − s_ in the integral and deduce that _dφ/dt_ = _λφ_ ( _φ −_ 1). Hence deduce that, for _q_ = 1 _− e[−][λt]_ and _n_ = 1 _,_ 2 _, . . ._ 

**==> picture [125 x 13] intentionally omitted <==**

_2.6 Jump chain and holding times_ 

87 

## **2.6 Jump chain and holding times** 

This section begins the theory of continuous-time Markov chains proper, which will occupy the remainder of this chapter and the whole of the next. The approach we have chosen is to introduce continuous-time chains in terms of the joint distribution of their jump chain and holding times. This provides the most direct mathematical description. It also makes possible a number of constructive realizations of a given Markov chain, which we shall describe, and which underlie many applications. 

Let _I_ be a countable set. The basic data for a continuous-time Markov chain on _I_ are given in the form of a _Q_ -matrix. Recall that a _Q_ -matrix on _I_ is any matrix _Q_ = ( _qij_ : _i, j ∈ I_ ) which satisfies the following conditions: 

**==> picture [147 x 54] intentionally omitted <==**

We will sometimes find it convenient to write _qi_ or _q_ ( _i_ ) as an alternative notation for _−qii_ . 

We are going to describe a simple procedure for obtaining from a _Q_ - matrix _Q_ a stochastic matrix Π. The _jump matrix_ Π = ( _πij_ : _i, j ∈ I_ ) of _Q_ is defined by 

**==> picture [169 x 59] intentionally omitted <==**

This procedure is best thought of row by row. For each _i ∈ I_ we take, where possible, the off-diagonal entries in the _i_ th row of _Q_ and scale them so they add up to 1, putting a 0 on the diagonal. This is only impossible when the off-diagonal entries are all 0, then we leave them alone and put a 1 on the diagonal. As you will see in the following example, the associated diagram transforms into a discrete-time Markov chain diagram simply by rescaling all the numbers on any arrows leaving a state so they add up to 1. 

## **Example 2.6.1** 

The _Q_ -matrix 

**==> picture [111 x 41] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

88 

has diagram: 

**==> picture [116 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 1<br>1 1<br>3 2<br>1<br>**----- End of picture text -----**<br>


The jump matrix Π of _Q_ is given by 

**==> picture [118 x 41] intentionally omitted <==**

and has diagram: 

**==> picture [116 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 1<br>3 2<br>1 1<br>2<br>3 1 2<br>3<br>**----- End of picture text -----**<br>


Here is the definition of a continuous-time Markov chain in terms of its jump chain and holding times. Recall that a minimal process is one which is set equal to _∞_ after any explosion – see Section 2.2. A minimal rightcontinuous process ( _Xt_ ) _t≥_ 0 on _I_ is a _Markov chain with initial distribution λ and generator matrix Q_ if its jump chain ( _Yn_ ) _n≥_ 0 is discrete-time Markov( _λ,_ Π) and if for each _n ≥_ 1, conditional on _Y_ 0 _, . . . , Yn−_ 1, its holding times _S_ 1 _, . . . , Sn_ are independent exponential random variables of parameters _q_ ( _Y_ 0) _, . . . , q_ ( _Yn−_ 1) respectively. We say ( _Xt_ ) _t≥_ 0 is _Markov_ ( _λ, Q_ ) for short. We can construct such a process as follows: let ( _Yn_ ) _n≥_ 0 be discretetime Markov( _λ,_ Π) and let _T_ 1 _, T_ 2 _, . . ._ be independent exponential random 

_2.6 Jump chain and holding times_ 

89 

variables of parameter 1, independent of ( _Yn_ ) _n≥_ 0. Set _Sn_ = _Tn/q_ ( _Yn−_ 1), _Jn_ = _S_ 1 + _. . ._ + _Sn_ and 

**==> picture [197 x 27] intentionally omitted <==**

Then ( _Xt_ ) _t≥_ 0 has the required properties. 

We shall now describe two further constructions. You will need to understand these constructions in order to identify processes in applications which can be modelled as Markov chains. Both constructions make direct use of the entries in the _Q_ -matrix, rather than proceeding first via the jump matrix. Here is the second construction. 

We begin with an initial state _X_ 0 = _Y_ 0 with distribution _λ_ , and with an array ( _Tn[j]_[:] _[n][≥]_[1] _[, j][∈][I]_[)][of][independent][exponential][random][variables][of] parameter 1. Then, inductively for _n_ = 0 _,_ 1 _,_ 2 _, . . ._ , if _Yn_ = _i_ we set 

**==> picture [173 x 73] intentionally omitted <==**

Then, conditional on _Yn_ = _i_ , the random variables _Sn[j]_ +1[are][independent] exponentials of parameter _qij_ for all _j_ = _i_ . So, conditional on _Yn_ = _i_ , by Theorem 2.3.3, _Sn_ +1 is exponential of parameter _qi_ =[�] _j_ = _i[q][ij]_[,] _[Y][n]_[+1] has distribution ( _πij_ : _j ∈ I_ ), and _Sn_ +1 and _Yn_ +1 are independent, and independent of _Y_ 0 _, . . . , Yn_ and _S_ 1 _, . . . , Sn_ , as required. This construction shows why we call _qi_ the _rate of leaving i_ and _qij_ the _rate of going from i to j_ . 

Our third and final construction of a Markov chain with generator matrix _Q_ and initial distribution _λ_ is based on the Poisson process. Imagine the state-space _I_ as a labyrinth of chambers and passages, each passage shut off by a single door which opens briefly from time to time to allow you through in one direction only. Suppose the door giving access to chamber _j_ from chamber _i_ opens at the jump times of a Poisson process of rate _qij_ and you take every chance to move that you can, then you will perform a Markov chain with _Q_ -matrix _Q_ . In more mathematical terms, we begin with an initial state _X_ 0 = _Y_ 0 with distribution _λ_ , and with a family of independent Poisson processes _{_ ( _Nt[ij]_[)] _[t][≥]_[0][:] _[i, j][∈][I, i]_[=] _[ j][}]_[,][(] _[N] t[ ij]_[)] _[t][≥]_[0][having] rate _qij_ . Then set _J_ 0 = 0 and define inductively for _n_ = 0 _,_ 1 _,_ 2 _, . . ._ 

**==> picture [255 x 54] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

90 

The first jump time of ( _Nt[ij]_[)] _[t][≥]_[0][is][exponential][of][parameter] _[q][ij]_[.][So,][by] Theorem 2.3.3, conditional on _Y_ 0 = _i_ , _J_ 1 is exponential of parameter _qi_ = � _j_ = _i[q][ij]_[,] _[Y]_[1][has][distribution][(] _[π][ij]_[:] _[ j][∈][I]_[),][and] _[J]_[1][and] _[Y]_[1][are][independent.] Now suppose _T_ is a stopping time of ( _Xt_ ) _t≥_ 0. If we condition on _X_ 0 and on the processes ( _Nt[kl]_[)] _[t][≥]_[0][for][(] _[k, l]_[)] _[ ̸]_[=][(] _[i, j]_[),][which][are][independent][of] _[N] t[ ij]_[,] then _{T ≤ t}_ depends only on ( _Ns[ij]_ : _s ≤ t_ ). So, by the strong Markov property of the Poisson process _N_[�] _t[ij]_[:=] _[ N] T[ ij]_ + _t[−][N] T[ ij]_[is][a][Poisson][process][of] rate _qij_ independent of ( _Ns[ij]_[:] _[ s][ ≤][T]_[),][and independent of] _[X]_[0][and (] _[N] t[ kl]_[)] _[t][≥]_[0] for ( _k, l_ ) = ( _i, j_ ). Hence, conditional on _T < ∞_ and _XT_ = _i_ , ( _XT_ + _t_ ) _t≥_ 0 has the same distribution as ( _Xt_ ) _t≥_ 0 and is independent of ( _Xs_ : _s ≤ T_ ). In particular, we can take _T_ = _Jn_ to see that, conditional on _Jn < ∞_ and _Yn_ = _i_ , _Sn_ +1 is exponential of parameter _qi_ , _Yn_ +1 has distribution ( _πij_ : _j ∈ I_ ), and _Sn_ +1 and _Yn_ +1 are independent, and independent of _Y_ 0 _, . . . , Yn_ and _S_ 1 _, . . . , Sn_ . Hence ( _Xt_ ) _t≥_ 0 is Markov( _λ, Q_ ) and, moreover, ( _Xt_ ) _t≥_ 0 has the strong Markov property. The conditioning on which this argument relies requires some further justification, especially when the state-space is infinite, so we shall not rely on this third construction in the development of the theory. 

## **2.7 Explosion** 

We saw in the special case of birth processes that, although each holding time is strictly positive, one can run through a sequence of states with shorter and shorter holding times and end up taking infinitely many jumps in a finite time. This phenomenon is called explosion. Recall the notation of Section 2.2: for a process with jump times _J_ 0 _, J_ 1 _, J_ 2 _, . . ._ and holding times _S_ 1 _, S_ 2 _, . . ._ , the explosion time _ζ_ is given by 

**==> picture [100 x 31] intentionally omitted <==**

**Theorem 2.7.1.** _Let_ ( _Xt_ ) _t≥_ 0 _be Markov_ ( _λ, Q_ ) _. Then_ ( _Xt_ ) _t≥_ 0 _does not explode if any one of the following conditions holds:_ 

**==> picture [243 x 47] intentionally omitted <==**

_Proof._ Set _Tn_ = _q_ ( _Yn−_ 1) _Sn_ , then _T_ 1 _, T_ 2 _, . . ._ are independent _E_ (1) and independent of ( _Yn_ ) _n≥_ 0. In cases (i) and (ii), _q_ = sup _i qi < ∞_ and 

**==> picture [83 x 31] intentionally omitted <==**

_2.7 Explosion_ 

91 

with probability 1. In case (iii), we know that ( _Yn_ ) _n≥_ 0 visits _i_ infinitely often, at times _N_ 1 _, N_ 2 _, . . ._ , say. Then 

**==> picture [108 x 31] intentionally omitted <==**

with probability 1. 

We say that a _Q_ -matrix _Q_ is _explosive_ if, for the associated Markov chain 

**==> picture [152 x 12] intentionally omitted <==**

Otherwise _Q_ is _non-explosive_ . Here as in Chapter 1 we denote by P _i_ the conditional probability P _i_ ( _A_ ) = P( _A|X_ 0 = _i_ ). It is a simple consequence of the Markov property for ( _Yn_ ) _n≥_ 0 that under P _i_ the process ( _Xt_ ) _t≥_ 0 is Markov( _δi, Q_ ). The result just proved gives simple conditions for nonexplosion and covers many cases of interest. As a corollary to the next result we shall obtain necessary and sufficient conditions for _Q_ to be explosive, but these are not as easy to apply as Theorem 2.7.1. 

**Theorem 2.7.2.** _Let_ ( _Xt_ ) _t≥_ 0 _be a continuous-time Markov chain with generator matrix Q and write ζ for the explosion time of_ ( _Xt_ ) _t≥_ 0 _. Fix θ >_ 0 _and set zi_ = E _i_ ( _e[−][θζ]_ ) _. Then z_ = ( _zi_ : _i ∈ I_ ) _satisfies:_ 

(i) _|zi| ≤_ 1 _for all i;_ (ii) _Qz_ = _θz._ 

� � _Moreover, if z also satisfies_ (i) _and_ (ii) _, then zi ≤ zi for all i._ 

_Proof._ Condition on _X_ 0 = _i_ . The time and place of the first jump are independent, _J_ 1 is _E_ ( _qi_ ) and 

**==> picture [92 x 12] intentionally omitted <==**

Moreover, by the Markov property of the jump chain at time _n_ = 1, conditional on _XJ_ 1 = _k_ , ( _XJ_ 1+ _t_ ) _t≥_ 0 is Markov( _δk, Q_ ) and independent of _J_ 1. So 

**==> picture [277 x 48] intentionally omitted <==**

and 

**==> picture [264 x 28] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

92 

Recall that _qi_ = _−qii_ and _qiπik_ = _qik_ . Then 

**==> picture [104 x 26] intentionally omitted <==**

so 

**==> picture [71 x 26] intentionally omitted <==**

and so _z_ satisfies (i) and (ii). Note that the same argument also shows that 

**==> picture [172 x 28] intentionally omitted <==**

Suppose that _z_ � also satisfies (i) and (ii), then, in particular 

**==> picture [90 x 14] intentionally omitted <==**

for all _i_ . Suppose inductively that 

**==> picture [71 x 13] intentionally omitted <==**

then, since _z_ � satisfies (ii) 

**==> picture [269 x 28] intentionally omitted <==**

Hence _z_ � _i ≤_ E _i_ ( _e[−][θJ][n]_ ) for all _n_ . By monotone convergence 

**==> picture [106 x 14] intentionally omitted <==**

� as _n →∞_ , so _zi ≤ zi_ for all _i_ . 

**Corollary 2.7.3.** _For each θ >_ 0 _the following are equivalent:_ 

- (a) _Q is non-explosive;_ 

- (b) _Qz_ = _θz and |zi| ≤_ 1 _for all i imply z_ = 0 _._ 

_Proof._ If (a) holds then P _i_ ( _ζ_ = _∞_ ) = 1 so E _i_ ( _e[−][θζ]_ ) = 0. By the theorem, _Qz_ = _θz_ and _|z| ≤_ 1 imply _zi ≤_ E _i_ ( _e[−][θζ]_ ), hence _z ≤_ 0, by symmetry _z ≥_ 0, and hence (b) holds. On the other hand, if (b) holds, then by the theorem E _i_ ( _e[−][θζ]_ ) = 0 for all _i_ , so P _i_ ( _ζ_ = _∞_ ) = 1 and (a) holds. 

_2.8 Forward and backward equations_ 

93 

## **Exercise** 

**2.7.1** Let ( _Xt_ ) _t≥_ 0 be a Markov chain on the integers with transition rates 

_qi,i_ +1 = _λqi, qi,i−_ 1 = _µqi_ 

and _qij_ = 0 if _|j − i| ≥_ 2, where _λ_ + _µ_ = 1 and _qi >_ 0 for all _i_ . Find for all integers _i_ : 

(a) the probability, starting from 0, that _Xt_ hits _i_ ; 

(b) the expected total time spent in state _i_ , starting from 0. 

In the case where _µ_ = 0, write down a necessary and sufficient condition for ( _Xt_ ) _t≥_ 0 to be explosive. Why is this condition necessary for ( _Xt_ ) _t≥_ 0 to be explosive for all _µ ∈_ [0 _,_ 1 _/_ 2)? 

Show that, in general, ( _Xt_ ) _t≥_ 0 is non-explosive if and only if one of the following conditions holds: 

**==> picture [171 x 43] intentionally omitted <==**

## **2.8 Forward and backward equations** 

Although the definition of a continuous-time Markov chain in terms of its jump chain and holding times provides a clear picture of the process, it does not answer some basic questions. For example, we might wish to calculate P _i_ ( _Xt_ = _j_ ). In this section we shall obtain two more ways of characterizing a continuous-time Markov chain, which will in particular give us a means to find P _i_ ( _Xt_ = _j_ ). As for Poisson processes and birth processes, the first step is to deduce the _Markov property_ from the jump chain/holding time definition. In fact, we shall give the _strong_ Markov property as this is a fundamental result and the proof is not much harder. However, the proof of both results really requires the precision of measure theory, so we have deferred it to Section 6.5. If you want to understand what happens, Theorem 2.4.1 on the Poisson process gives the main idea in a simpler context. 

Recall that a random variable _T_ with values in [0 _, ∞_ ] is a stopping time of ( _Xt_ ) _t≥_ 0 if for each _t ∈_ [0 _, ∞_ ) the event _{T ≤ t}_ depends only on ( _Xs_ : _s ≤ t_ ). 

**Theorem 2.8.1 (Strong Markov property).** _Let_ ( _Xt_ ) _t≥_ 0 _be Markov_ ( _λ, Q_ ) _and let T be a stopping time of_ ( _Xt_ ) _t≥_ 0 _. Then, conditional on T < ∞ and XT_ = _i,_ ( _XT_ + _t_ ) _t≥_ 0 _is Markov_ ( _δi, Q_ ) _and independent of_ ( _Xs_ : _s ≤ T_ ) _._ 

We come to the key result for continuous-time Markov chains. We shall present first a version for the case of finite state-space, where there is a 

_2. Continuous-time Markov chains I_ 

94 

simpler proof. In this case there are three alternative definitions, just as for the Poisson process. 

**Theorem 2.8.2.** _Let_ ( _Xt_ ) _t≥_ 0 _be a right-continuous process with values in a finite set I. Let Q be a Q-matrix on I with jump matrix_ Π _. Then the following three conditions are equivalent:_ 

- (a) (jump chain/holding time definition) _conditional on X_ 0 = _i, the jump chain_ ( _Yn_ ) _n≥_ 0 _of_ ( _Xt_ ) _t≥_ 0 _is discrete-time Markov_ ( _δi,_ Π) _and for each n ≥_ 1 _, conditional on Y_ 0 _, . . . , Yn−_ 1 _, the holding times S_ 1 _, . . . , Sn are independent exponential random variables of parameters q_ ( _Y_ 0) _, . . . , q_ ( _Yn−_ 1) _respectively;_ 

- (b) (infinitesimal definition) _for all t, h ≥_ 0 _, conditional on Xt_ = _i, Xt_ + _h is independent of_ ( _Xs_ : _s ≤ t_ ) _and, as h ↓_ 0 _, uniformly in t, for all j_ 

**==> picture [197 x 13] intentionally omitted <==**

- (c) (transition probability definition) _for all n_ = 0 _,_ 1 _,_ 2 _, . . . , all times_ 0 _≤ t_ 0 _≤ t_ 1 _≤ . . . ≤ tn_ +1 _and all states i_ 0 _, . . . , in_ +1 

**==> picture [297 x 13] intentionally omitted <==**

**==> picture [326 x 12] intentionally omitted <==**

**==> picture [131 x 13] intentionally omitted <==**

If ( _Xt_ ) _t≥_ 0 satisfies any of these conditions then it is called a _Markov chain with generator matrix Q_ . We say that ( _Xt_ ) _t≥_ 0 is _Markov_ ( _λ, Q_ ) for short, where _λ_ is the distribution of _X_ 0. 

_Proof._ (a) _⇒_ (b) Suppose (a) holds, then, as _h ↓_ 0, 

**==> picture [243 x 14] intentionally omitted <==**

and for _j_ = _i_ we have 

**==> picture [231 x 31] intentionally omitted <==**

Thus for every state _j_ there is an inequality 

**==> picture [148 x 12] intentionally omitted <==**

_2.8 Forward and backward equations_ 

95 

and by taking the finite sum over _j_ we see that these must in fact be equalities. Then by the Markov property, for any _t, h ≥_ 0, conditional on _Xt_ = _i_ , _Xt_ + _h_ is independent of ( _Xs_ : _s ≤ t_ ) and, as _h ↓_ 0, uniformly in _t_ 

**==> picture [266 x 13] intentionally omitted <==**

(b) _⇒_ (c) Set _pij_ ( _t_ ) = P _i_ ( _Xt_ = _j_ ) = P( _Xt_ = _j | X_ 0 = _i_ ). If (b) holds, then for all _t, h ≥_ 0, as _h ↓_ 0, uniformly in _t_ 

**==> picture [234 x 56] intentionally omitted <==**

Since _I_ is we have 

**==> picture [197 x 31] intentionally omitted <==**

so, letting _h ↓_ 0, we see that _pij_ ( _t_ ) is differentiable on the right. Then by uniformity we can replace _t_ by _t − h_ in the above and let _h ↓_ 0 to see first that _pij_ ( _t_ ) is continuous on the left, then differentiable on the left, hence differentiable, and satisfies the forward equations 

**==> picture [173 x 25] intentionally omitted <==**

Since _I_ is finite, _pij_ ( _t_ ) is then the unique solution by Theorem 2.1.1. Also, if (b) holds, then 

**==> picture [342 x 13] intentionally omitted <==**

and, moreover, (b) holds for ( _Xtn_ + _t_ ) _t≥_ 0 so, by the above argument, 

**==> picture [234 x 13] intentionally omitted <==**

proving (c). 

(c) _⇒_ (a) See the proof of Theorem 2.4.3. 

We know from Theorem 2.1.1 that for _I_ finite the forward and backward equations have the same solution. So in condition (c) of the result just proved we could replace the forward equation with the backward equation. Indeed, there is a slight variation of the argument from (b) to (c) which leads directly to the backward equation. 

_2. Continuous-time Markov chains I_ 

96 

The deduction of (c) from (b) above can be seen as the matrix version of the following result: for _q ∈_ R we have 

**==> picture [195 x 28] intentionally omitted <==**

Suppose (b) holds and set 

**==> picture [173 x 12] intentionally omitted <==**

**==> picture [236 x 13] intentionally omitted <==**

**==> picture [133 x 12] intentionally omitted <==**

and 

**==> picture [359 x 28] intentionally omitted <==**

Some care is needed in making this precise, since the _o_ ( _h_ ) terms, though uniform in _t_ , are not _a priori_ identical. On the other hand, in (c) we see that 

**==> picture [66 x 13] intentionally omitted <==**

We turn now to the case of infinite state-space. The backward equation may still be written in the form 

**==> picture [127 x 12] intentionally omitted <==**

only now we have an infinite system of differential equations 

**==> picture [169 x 25] intentionally omitted <==**

and the results on matrix exponentials given in Section 2.1 no longer apply. A solution to the backward equation is any matrix ( _pij_ ( _t_ ) : _i, j ∈ I_ ) of differentiable functions satisfying this system of differential equations. 

**Theorem 2.8.3.** _Let Q be a Q-matrix. Then the backward equation_ 

_P[′]_ ( _t_ ) = _QP_ ( _t_ ) _, P_ (0) = _I_ 

_has a minimal non-negative solution_ ( _P_ ( _t_ ) : _t ≥_ 0) _. This solution forms a matrix semigroup_ 

**==> picture [190 x 12] intentionally omitted <==**

We shall prove this result by a probabilistic method in combination with Theorem 2.8.4. Note that if _I_ is finite we must have _P_ ( _t_ ) = _e[tQ]_ by Theorem 2.1.1. We call ( _P_ ( _t_ ) : _t ≥_ 0) the _minimal non-negative semigroup_ associated to _Q_ , or simply the _semigroup_ of _Q_ , the qualifications _minimal_ and _nonnegative_ being understood. 

Here is the key result for Markov chains with infinite state-space. There are just two alternative definitions now as the infinitesimal characterization becomes problematic for infinite state-space. 

_2.8 Forward and backward equations_ 

97 

**Theorem 2.8.4.** _Let_ ( _Xt_ ) _t≥_ 0 _be a minimal right-continuous process with values in I. Let Q be a Q-matrix on I with jump matrix_ Π _and semigroup_ ( _P_ ( _t_ ) : _t ≥_ 0) _. Then the following conditions are equivalent:_ 

- (a) (jump chain/holding time definition) _conditional on X_ 0 = _i, the jump chain_ ( _Yn_ ) _n≥_ 0 _of_ ( _Xt_ ) _t≥_ 0 _is discrete-time Markov_ ( _δi,_ Π) _and for each n ≥_ 1 _, conditional on Y_ 0 _, . . . , Yn−_ 1 _, the holding times S_ 1 _, . . . , Sn are independent exponential random variables of parameters q_ ( _Y_ 0) _, . . . , q_ ( _Yn−_ 1) _respectively;_ 

- (b) (transition probability definition) _for all n_ = 0 _,_ 1 _,_ 2 _, . . . , all times_ 0 _≤ t_ 0 _≤ t_ 1 _≤ . . . ≤ tn_ +1 _and all states i_ 0 _, i_ 1 _, . . . , in_ +1 

**==> picture [301 x 13] intentionally omitted <==**

If ( _Xt_ ) _t≥_ 0 satisfies any of these conditions then it is called a _Markov chain with generator matrix Q_ . We say that ( _Xt_ ) _t≥_ 0 is _Markov_ ( _λ, Q_ ) for short, where _λ_ is the distribution of _X_ 0. 

_Proof of Theorems 2.8.3 and 2.8.4._ We know that there exists a process ( _Xt_ ) _t≥_ 0 satisfying (a). So let us _define P_ ( _t_ ) by 

**==> picture [96 x 12] intentionally omitted <==**

**Step 1** . _We show that P_ ( _t_ ) _satisfies the backward equation_ . 

Conditional on _X_ 0 = _i_ we have _J_ 1 _∼ E_ ( _qi_ ) and _XJ_ 1 _∼_ ( _πik_ : _k ∈ I_ ). Then conditional on _J_ 1 = _s_ and _XJ_ 1 = _k_ we have ( _Xs_ + _t_ ) _t≥_ 0 _∼_ Markov( _δk, Q_ ). So P _i_ ( _Xt_ = _j, t < J_ 1) = _e[−][q][i][ t] δij_ 

and 

**==> picture [270 x 28] intentionally omitted <==**

Therefore 

**==> picture [323 x 63] intentionally omitted <==**

Make a change of variable _u_ = _t − s_ in each of the integrals, interchange sum and integral by monotone convergence and multiply by _e[q][i][t]_ to obtain 

**==> picture [281 x 33] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

98 

This equation shows, firstly, that _pij_ ( _t_ ) is continuous in _t_ for all _i, j_ . Secondly, the integrand is then a uniformly converging sum of continuous functions, hence continuous, and hence _pij_ ( _t_ ) is differentiable in _t_ and sat- 

**==> picture [202 x 26] intentionally omitted <==**

Recall that _qi_ = _−qii_ and _qik_ = _qiπik_ for _k_ = _i_ . Then, on rearranging, we obtain 

**==> picture [229 x 25] intentionally omitted <==**

so _P_ ( _t_ ) satisfies the backward equation. 

The integral equation (2.1) is called the _integral form of the backward equation_ . 

**Step 2** . _We show that if P_[�] ( _t_ ) _is another non-negative solution of the backward equation, then P_ ( _t_ ) _≤ P_[�] ( _t_ ) _, hence P_ ( _t_ ) _is the minimal non-negative solution._ 

The argument used to prove (2.1) also shows that 

**==> picture [323 x 51] intentionally omitted <==**

On the other hand, if _P_[�] ( _t_ ) satisfies the backward equation, then, by reversing the steps from (2.1) to (2.3), it also satisfies the integral form: 

**==> picture [295 x 32] intentionally omitted <==**

If _P_[�] ( _t_ ) _≥_ 0, then 

� P _i_ ( _Xt_ = _j, t < J_ 0) = 0 _≤ pij_ ( _t_ ) for all _i, j_ and _t_ . 

Let us suppose inductively that 

**==> picture [228 x 12] intentionally omitted <==**

then by comparing (2.4) and (2.5) we have 

**==> picture [238 x 12] intentionally omitted <==**

_2.8 Forward and backward equations_ 

99 

and the induction proceeds. Hence 

**==> picture [292 x 16] intentionally omitted <==**

**Step 3** . Since ( _Xt_ ) _t≥_ 0 does not return from _∞_ we have 

**==> picture [314 x 56] intentionally omitted <==**

by the Markov property. Hence ( _P_ ( _t_ ) : _t ≥_ 0) is a matrix semigroup. This completes the proof of Theorem 2.8.3. 

**Step 4** . Suppose, as we have throughout, that ( _Xt_ ) _t≥_ 0 satisfies (a). Then, by the Markov property 

**==> picture [298 x 30] intentionally omitted <==**

so ( _Xt_ ) _t≥_ 0 satisfies (b). We complete the proof of Theorem 2.8.4 by the usual argument that (b) must now imply (a) (see the proof of Theorem 2.4.3, (c) _⇒_ (a)). 

So far we have said nothing about the forward equation in the case of infinite state-space. Remember that the finite state-space results of Section 2.1 are no longer valid. The forward equation may still be written 

**==> picture [131 x 13] intentionally omitted <==**

now understood as an infinite system of differential equations 

**==> picture [173 x 25] intentionally omitted <==**

A solution is then any matrix � _pij_ ( _t_ ) : _i, j ∈ I_ � of differentiable functions satisfying this system of equations. We shall show that the semigroup � _P_ ( _t_ ) : _t ≥_ 0� of _Q_ does satisfy the forward equations, by a probabilistic argument resembling Step 1 of the proof of Theorems 2.8.3 and 2.8.4. This time, instead of conditioning on the first event, we condition on the last event before time _t_ . The argument is a little longer because there is no reverse-time Markov property to give the conditional distribution. We need the following time-reversal identity, a simple version of which was given in Theorem 2.3.4. 

_2. Continuous-time Markov chains I_ 

100 

**Lemma 2.8.5.** _We have_ 

**==> picture [287 x 29] intentionally omitted <==**

_Proof._ Conditional on _Y_ 0 = _i_ 0 _, . . . , Yn_ = _in_ , the holding times _S_ 1 _, . . . , Sn_ +1 are independent with _Sk ∼ E_ ( _qik −_ 1). So the left-hand side is given by 

**==> picture [309 x 32] intentionally omitted <==**

where ∆( _t_ ) = _{_ ( _s_ 1 _, . . . , sn_ ) : _s_ 1 + _. . ._ + _sn ≤ t_ and _s_ 1 _, . . . , sn ≥_ 0 _}_ . On making the substitutions _u_ 1 = _t − s_ 1 _− . . . − sn_ and _uk_ = _sn−k_ +2, for _k_ = 2 _, . . . , n_ , we obtain 

**==> picture [353 x 66] intentionally omitted <==**

**Theorem 2.8.6.** _The minimal non-negative solution_ � _P_ ( _t_ ) : _t ≥_ 0� _of the backward equation is also the minimal non-negative solution of the forward equation_ 

**==> picture [131 x 13] intentionally omitted <==**

_Proof._ Let ( _Xt_ ) _t≥_ 0 denote the minimal Markov chain with generator matrix _Q_ . By Theorem 2.8.4 

**==> picture [254 x 50] intentionally omitted <==**

Now by Lemma 2.8.5, for _n ≥_ 1, we have 

**==> picture [279 x 94] intentionally omitted <==**

_2.8 Forward and backward equations_ 

101 

where we have used the Markov property of ( _Yn_ ) _n≥_ 0 for the second equality. Hence 

**==> picture [360 x 127] intentionally omitted <==**

where we have used monotone convergence to interchange the sum and integral at the last step. This is the _integral form of the forward equation_ . Now make a change of variable _u_ = _t − s_ in the integral and multiply by _e[q][j][ t]_ to obtain 

**==> picture [277 x 33] intentionally omitted <==**

We know by equation (2.2) that _e[q][i][ t] pik_ ( _t_ ) is _increasing_ for all _i, k_ . Hence either 

**==> picture [236 x 26] intentionally omitted <==**

or 

**==> picture [158 x 26] intentionally omitted <==**

The latter would contradict (2.7) since the left-hand side is finite for all _t_ , so it is the former which holds. We know from the backward equation that _pij_ ( _t_ ) is continuous for all _i, j_ ; hence by uniform convergence the integrand in (2.7) is continuous and we may differentiate to obtain 

**==> picture [151 x 27] intentionally omitted <==**

Hence _P_ ( _t_ ) solves the forward equation. 

To establish minimality let us suppose that _p_ � _ij_ ( _t_ ) is another solution of the forward equation; then we also have 

**==> picture [223 x 33] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

102 

A small variation of the argument leading to (2.6) shows that, for _n ≥_ 0 

**==> picture [303 x 50] intentionally omitted <==**

If _P_[�] ( _t_ ) _≥_ 0, then 

� P( _Xt_ = _j, t < J_ 0) = 0 _≤ pij_ ( _t_ ) for all _i, j_ and _t._ 

Let us suppose inductively that 

**==> picture [216 x 12] intentionally omitted <==**

then by comparing (2.7) and (2.8) we obtain 

**==> picture [224 x 12] intentionally omitted <==**

and the induction proceeds. Hence 

**==> picture [282 x 16] intentionally omitted <==**

## **Exercises** 

**2.8.1** Two fleas are bound together to take part in a nine-legged race on the vertices _A, B, C_ of a triangle. Flea 1 hops at random times in the clockwise direction; each hop takes the pair from one vertex to the next and the times between successive hops of Flea 1 are independent random variables, each with with exponential distribution, mean 1 _/λ_ . Flea 2 behaves similarly, but hops in the anticlockwise direction, the times between his hops having mean 1 _/µ_ . Show that the probability that they are at _A_ at a given time _t >_ 0 (starting from _A_ at time _t_ = 0) is 

**==> picture [224 x 34] intentionally omitted <==**

**2.8.2** Let ( _Xt_ ) _t≥_ 0 be a birth-and-death process with rates _λn_ = _nλ_ and _µn_ = _nµ_ , and assume that _X_ 0 = 1. Show that _h_ ( _t_ ) = P( _Xt_ = 0) satisfies 

**==> picture [182 x 28] intentionally omitted <==**

_2.9 Non-minimal chains_ 

103 

and deduce that if _λ ̸_ = _µ_ then 

**==> picture [172 x 14] intentionally omitted <==**

## **2.9 Non-minimal chains** 

This book concentrates entirely on processes which are right-continuous and minimal. These are the simplest sorts of process and, overwhelmingly, the ones of greatest practical application. We have seen in this chapter that we can associate to each distribution _λ_ and _Q_ -matrix _Q_ a unique such process, the Markov chain with initial distribution _λ_ and generator matrix _Q_ . Indeed we have taken the liberty of defining Markov chains to be those processes which arise in this way. However, these processes do not by any means exhaust the class of memoryless continuous-time processes with values in a countable set _I_ . There are many more exotic possibilities, the general theory of which goes very much deeper than the account given in this book. It is in the nature of things that these exotic cases have received the greater attention among mathematicians. Here are some examples to help you imagine the possibilities. 

## **Example 2.9.1** 

Consider a birth process ( _Xt_ ) _t≥_ 0 starting from 0 with rates _qi_ = 2 _[i]_ for _i ≥_ 0. We have chosen these rates so that 

**==> picture [110 x 31] intentionally omitted <==**

which shows that the process explodes (see Theorems 2.3.2 and 2.5.2). We have until now insisted that _Xt_ = _∞_ for all _t ≥ ζ_ , where _ζ_ is the explosion time. But another obvious possibility is to start the process off again from 0 at time _ζ_ , and do the same for all subsequent explosions. An argument based on the memoryless property of the exponential distribution shows that for 0 _≤ t_ 0 _≤ . . . ≤ tn_ +1 this process satisfies 

**==> picture [299 x 14] intentionally omitted <==**

for a semigroup of stochastic matrices ( _P_ ( _t_ ) : _t ≥_ 0) on _I_ . This is the defining property for a more general class of Markov chains. Note that the chain is no longer determined by _λ_ and _Q_ alone; the rule for bringing ( _Xt_ ) _t≥_ 0 back into _I_ after explosion also has to be given. 

_2. Continuous-time Markov chains I_ 

104 

## **Example 2.9.2** 

We make a variation on the preceding example. Suppose now that the jump chain ( _Yn_ ) _n≥_ 0 of ( _Xt_ ) _t≥_ 0 is the Markov chain on Z which moves one step away from 0 with probability 2 _/_ 3 and one step towards 0 with probability 1 _/_ 3, with _π_ 01 = _π_ 0 _,−_ 1 = 1 _/_ 2, and that _Y_ 0 = 0. Let the transition rates for ( _Xt_ ) _t≥_ 0 be _qi_ = 2 _[|][i][|]_ for _i ∈_ Z. Then ( _Xt_ ) _t≥_ 0 is again explosive. (A simple way to see this using some results of Chapter 3 is to check that ( _Yn_ ) _n≥_ 0 is transient but ( _Xt_ ) _t≥_ 0 has an invariant distribution – by solution of the detailed balance equations. Then Theorem 3.5.3 makes explosion inevitable.) Now there are two ways in which ( _Xt_ ) _t≥_ 0 can explode, either _Xt →−∞_ or _Xt →∞_ . 

The process may again be restarted at 0 after explosion. Alternatively, we may choose the restart randomly, and according to the way that explosion occurred. For example 

**==> picture [172 x 27] intentionally omitted <==**

where _Z_ takes values _±_ 1 with probability 1 _/_ 2. 

## **Example 2.9.3** 

The processes in the preceding two examples, though no longer minimal, were at least right-continuous. Here is an altogether more exotic example, due to P. L´evy, which is not even right-continuous. Consider 

**==> picture [174 x 13] intentionally omitted <==**

and set _I_ = _∪nDn_ . With each _i ∈ Dn\Dn−_ 1 we associate an independent exponential random variable _Si_ of parameter (2 _[n]_ )[2] . There are 2 _[n][−]_[1] states in ( _D[n] \D[n][−]_[1] ) _∩_ [0 _,_ 1), so, for all _i ∈ I_ 

and 

**==> picture [204 x 99] intentionally omitted <==**

Now 

**==> picture [235 x 41] intentionally omitted <==**

_2.10 Appendix: matrix exponentials_ 

105 

This process runs through all the dyadic rationals _i ∈ I_ in the usual order. It remains in _i ∈ Dn\Dn−_ 1 for an exponential time of parameter 1. Between any two distinct states _i_ and _j_ it makes infinitely many visits to _∞_ . The Lebesgue measure of the set of times _t_ when _Xt_ = _∞_ is zero. There is a semigroup of stochastic matrices ( _P_ ( _t_ ) : _t ≥_ 0) on _I_ such that, for 0 _≤ t_ 0 _≤ . . . ≤ tn_ +1 

**==> picture [302 x 14] intentionally omitted <==**

In particular, P( _Xt_ = _∞_ ) = 0 for all _t ≥_ 0. The details may be found in _Markov Chains_ by D. Freedman (Holden-Day, San Francisco, 1971). 

We hope these three examples will serve to suggest some of the possibilities for more general continuous-time Markov chains. For further reading, see Freedman’s book, or else _Markov Chains with Stationary Transition Probabilities_ by K.-L. Chung (Springer, Berlin, 2nd edition, 1967), or _Diffusions, Markov Processes and Martingales, Vol 1: Foundations_ by L. C. G. Rogers and D. Williams (Wiley, Chichester, 2nd edition, 1994). 

## **2.10 Appendix: matrix exponentials** 

Define two norms on the space of real-valued _N × N_ -matrices 

**==> picture [186 x 20] intentionally omitted <==**

Obviously, _∥Q∥∞_ is finite for all _Q_ and controls the size of the entries in _Q_ . We shall show that the two norms are equivalent and that _|Q|_ is well adapted to sums and products of matrices, which _∥Q∥∞_ is not. 

**Lemma 2.10.1.** _We have_ 

**==> picture [135 x 12] intentionally omitted <==**

**==> picture [251 x 12] intentionally omitted <==**

_Proof._ (a) For any vector _v_ we have _|Qv| ≤|Q||v|_ . In particular, for the vector _εj_ = (0 _, . . . ,_ 1 _, . . . ,_ 0), with 1 in the _j_ th place, we have _|Qεj| ≤|Q|_ . The supremum defining _∥Q∥∞_ is achieved, at _j_ say, so 

**==> picture [168 x 25] intentionally omitted <==**

_2. Continuous-time Markov chains I_ 

106 

On the other hand 

**==> picture [144 x 135] intentionally omitted <==**

and, by the Cauchy–Schwarz inequality 

**==> picture [113 x 43] intentionally omitted <==**

so _|Qv|_[2] _≤ N_[2] _∥Q∥∞_[2] _[|][v][|]_[2][.][This][implies][that] _[|][Q][| ≤][N][∥][Q][∥][∞]_[.] 

(b) For any vector _v_ we have 

**==> picture [231 x 29] intentionally omitted <==**

Now for _n_ = 0 _,_ 1 _,_ 2 _, . . ._ , consider the finite sum 

**==> picture [77 x 31] intentionally omitted <==**

For each _i_ and _j_ , and _m ≤ n_ , we have 

**==> picture [271 x 89] intentionally omitted <==**

Since _|Q| ≤ N ∥Q∥∞ < ∞_ ,[�] _[∞] k_ =0 _[|][Q][|][k][/k]_[!][converges][by][the][ratio][test,][so] 

**==> picture [173 x 32] intentionally omitted <==**

_2.10 Appendix: matrix exponentials_ 

107 

Hence each component of _E_ ( _n_ ) forms a Cauchy sequence, which therefore converges, proving that 

**==> picture [61 x 32] intentionally omitted <==**

is well defined and, indeed, that the power series 

**==> picture [95 x 32] intentionally omitted <==**

has infinite radius of convergence for all _i, j_ . Finally, for two commuting matrices _Q_ 1 and _Q_ 2 we have 

**==> picture [193 x 120] intentionally omitted <==**

**3** 

## Continuous-time Markov chains II 

This chapter brings together the discrete-time and continuous-time theories, allowing us to deduce analogues, for continuous-time chains, of all the results given in Chapter 1. All the facts from Chapter 2 that are necessary to understand this synthesis are reviewed in Section 3.1. You will require a reasonable understanding of Chapter 1 here, but, given such an understanding, this chapter should look reassuringly familiar. Exercises remain an important part of the text. 

## **3.1 Basic properties** 

Let _I_ be a countable set. Recall that a _Q_ - _matrix_ on _I_ is a matrix _Q_ = ( _qij_ : _i, j ∈ I_ ) satisfying the following conditions: 

**==> picture [141 x 12] intentionally omitted <==**

**==> picture [131 x 12] intentionally omitted <==**

**==> picture [132 x 26] intentionally omitted <==**

We set _qi_ = _q_ ( _i_ ) = _−qii_ . Associated to any _Q_ -matrix is a _jump matrix_ Π = ( _πij_ : _i, j ∈ I_ ) given by 

**==> picture [169 x 59] intentionally omitted <==**

Note that Π is a stochastic matrix. 

_3.1 Basic properties_ 

109 

A _sub-stochastic matrix_ on _I_ is a matrix _P_ = ( _pij_ : _i, j ∈ I_ ) with nonnegative entries and such that 

**==> picture [116 x 26] intentionally omitted <==**

Associated to any _Q_ -matrix is a _semigroup_ ( _P_ ( _t_ ) : _t ≥_ 0) of sub-stochastic matrices _P_ ( _t_ ) = ( _pij_ ( _t_ ) : _i, j ∈ I_ ). As the name implies we have 

**==> picture [193 x 12] intentionally omitted <==**

You will need to be familiar with the following terms introduced in Section 2.2: _minimal right-continuous random process, jump times, holding times, jump chain_ and _explosion_ . Briefly, a right-continuous process ( _Xt_ ) _t≥_ 0 runs through a sequence of states _Y_ 0 _, Y_ 1 _, Y_ 2 _, . . ._ , being held in these states for times _S_ 1 _, S_ 2 _, S_ 3 _, . . ._ respectively and jumping to the next state at times _J_ 1 _, J_ 2 _, J_ 3 _, . . ._ . Thus _Jn_ = _S_ 1 + _. . ._ + _Sn_ . The discrete-time process ( _Yn_ ) _n≥_ 0 is the jump chain, ( _Sn_ ) _n≥_ 1 are the holding times and ( _Jn_ ) _n≥_ 1 are the jump times. The explosion time _ζ_ is given by 

**==> picture [106 x 31] intentionally omitted <==**

For a minimal process we take a new state _∞_ and insist that _Xt_ = _∞_ for all _t ≥ ζ_ . An important point is that a minimal right-continuous process is determined by its jump chain and holding times. 

The data for a continuous-time Markov chain ( _Xt_ ) _t≥_ 0 are a distribution _λ_ and a _Q_ -matrix _Q_ . The distribution _λ_ gives the _initial distribution_ , the distribution of _X_ 0. The _Q_ -matrix is known as the _generator matrix_ of ( _Xt_ ) _t≥_ 0 and determines how the process evolves from its initial state. We established in Section 2.8 that there are two different, but equivalent, ways to describe how the process evolves. 

The first, in terms of jump chain and holding times, states that (a) ( _Yn_ ) _n≥_ 0 is Markov( _λ,_ Π); 

(b) conditional on _Y_ 0 = _i_ 0 _, . . . , Yn−_ 1 = _in−_ 1, the holding times _S_ 1 _, . . . , Sn_ are independent exponential random variables of parameters _qi_ 0 _, . . . , qin −_ 1 . 

Put more simply, given that the chain starts at _i_ , it waits there for an exponential time of parameter _qi_ and then jumps to a new state, choosing state _j_ with probability _πij_ . It then starts afresh, forgetting what has gone before. 

_3. Continuous-time Markov chains II_ 

110 

The second description, in terms of the semigroup, states that the finitedimensional distributions of the process are given by 

**==> picture [350 x 26] intentionally omitted <==**

**==> picture [301 x 13] intentionally omitted <==**

Again, put more simply, given that the chain starts at _i_ , by time _t_ it is found in state _j_ with probability _pij_ ( _t_ ). It then starts afresh, forgetting what has gone before. In the case where 

**==> picture [132 x 26] intentionally omitted <==**

the chain is found at _∞_ with probability _p_ � _i∞_ ( _t_ ). The semigroup _P_ ( _t_ ) is referred to as the _transition matrix_ of the chain and its entries _pij_ ( _t_ ) are the _transition probabilities_ . This description implies that for all _h >_ 0 the discrete skeleton ( _Xnh_ ) _n≥_ 0 is Markov( _λ, P_ ( _h_ )). Strictly, in the explosive case, that is, when _P_ ( _t_ ) is strictly sub-stochastic, we should say Markov( _λ,_[�] _P_[�] ( _h_ )), where _λ_[�] and _P_[�] ( _h_ ) are defined on _I ∪{∞}_ , extending _λ_ and _P_ ( _h_ ) by _λ_[�] _∞_ = 0 � and _p∞j_ ( _h_ ) = 0. But there is no danger of confusion in using the simpler notation. 

The information coming from these two descriptions is sufficient for most of the analysis of continuous-time chains done in this chapter. Note that we have not yet said how the semigroup _P_ ( _t_ ) is associated to the _Q_ -matrix _Q_ , except via the process! This extra information will be required when we discuss reversibility in Section 3.7. So we recall from Section 2.8 that the semigroup is characterized as the minimal non-negative solution of the _backward equation_ 

**==> picture [127 x 12] intentionally omitted <==**

which reads in components 

**==> picture [173 x 25] intentionally omitted <==**

The semigroup is also the minimal non-negative solution of the _forward equation_ 

**==> picture [131 x 12] intentionally omitted <==**

In the case where _I_ is finite, _P_ ( _t_ ) is simply the matrix exponential _e[tQ]_ , and is the _unique_ solution of the backward and forward equations. 

_3.2 Class structure_ 

111 

## **3.2 Class structure** 

A first step in the analysis of a continuous-time Markov chain ( _Xt_ ) _t≥_ 0 is to identify its class structure. We emphasise that we deal only with minimal chains, those that die after explosion. Then the class structure is simply the discrete-time class structure of the jump chain ( _Yn_ ) _n≥_ 0, as discussed in Section 1.2. 

We say that _i leads to j_ and write _i → j_ if 

**==> picture [148 x 12] intentionally omitted <==**

We say _i communicates with j_ and write _i ↔ j_ if both _i → j_ and _j → i_ . The notions of _communicating class, closed class, absorbing state_ and _irreducibility_ are inherited from the jump chain. 

**Theorem 3.2.1.** _For distinct states i and j the following are equivalent:_ 

**==> picture [47 x 12] intentionally omitted <==**

- (ii) _i → j for the jump chain;_ 

**==> picture [345 x 25] intentionally omitted <==**

- (iv) _pij_ ( _t_ ) _>_ 0 _for all t >_ 0 _;_ 

**==> picture [142 x 13] intentionally omitted <==**

_Proof._ Implications (iv) _⇒_ (v) _⇒_ (i) _⇒_ (ii) are clear. If (ii) holds, then by Theorem 1.2.1, there are states _i_ 0 _, i_ 1 _, . . . , in_ with _i_ 0 = _i_ , _in_ = _j_ and _πi_ 0 _i_ 1 _πi_ 1 _i_ 2 _. . . πin −_ 1 _in >_ 0, which implies (iii). If _qij >_ 0, then 

**==> picture [284 x 13] intentionally omitted <==**

for all _t >_ 0, so if (iii) holds, then 

**==> picture [180 x 12] intentionally omitted <==**

for all _t >_ 0, and (iv) holds. 

Condition (iv) of Theorem 3.2.1 shows that the situation is simpler than in discrete-time, where it may be possible to reach a state, but only after a certain length of time, and then only periodically. 

## **3.3 Hitting times and absorption probabilities** 

Let ( _Xt_ ) _t≥_ 0 be a Markov chain with generator matrix _Q_ . The _hitting time_ of a subset _A_ of _I_ is the random variable _D[A]_ defined by 

**==> picture [156 x 14] intentionally omitted <==**

_3. Continuous-time Markov chains II_ 

112 

with the usual convention that inf _∅_ = _∞_ . We emphasise that ( _Xt_ ) _t≥_ 0 is minimal. So if _H[A]_ is the hitting time of _A_ for the jump chain, then 

**==> picture [122 x 13] intentionally omitted <==**

and on this set we have 

**==> picture [56 x 13] intentionally omitted <==**

The probability, starting from _i_ , that ( _Xt_ ) _t≥_ 0 ever hits _A_ is then 

**==> picture [170 x 14] intentionally omitted <==**

When _A_ is a closed class, _h[A] i_[is][called][the] _[absorption][probability]_[.][Since][the] hitting probabilities are those of the jump chain we can calculate them as in Section 1.3. 

**Theorem 3.3.1.** _The vector of hitting probabilities h[A]_ = ( _h[A] i_[:] _[i][∈][I]_[)] _[is] the minimal non-negative solution to the system of linear equations_ 

**==> picture [143 x 32] intentionally omitted <==**

_Proof._ Apply Theorem 1.3.2 to the jump chain and rewrite (1.3) in terms of _Q_ . 

The average time taken, starting from _i_ , for ( _Xt_ ) _t≥_ 0 to reach _A_ is given by 

**==> picture [68 x 13] intentionally omitted <==**

In calculating _ki[A]_[we][have][to][take][account][of][the][holding][times][so][the][rela-] tionship to the discrete-time case is not quite as simple. 

**==> picture [116 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 1 2 2<br>2<br>1 2<br>3 3<br>3 3 4<br>**----- End of picture text -----**<br>


_3.3 Hitting times and absorption probabilities_ 

113 

## **Example 3.3.2** 

Consider the Markov chain ( _Xt_ ) _t≥_ 0 with the diagram given on the preceding page. How long on average does it take to get from 1 to 4? 

Set _ki_ = E _i_ (time to get to 4). On starting in 1 we spend an average time _q_ 1 _[−]_[1] = 1 _/_ 2 in 1, then jump with equal probability to 2 or 3. Thus 

**==> picture [94 x 15] intentionally omitted <==**

and similarly 

**==> picture [208 x 15] intentionally omitted <==**

On solving these linear equations we find _k_ 1 = 17 _/_ 12. 

Here is the general result. The proof follows the same lines as Theorem 1.3.5. 

**Theorem 3.3.3.** _Assume that qi >_ 0 _for all i ̸∈ A. The vector of expected hitting times k[A]_ = ( _ki[A]_[:] _[ i][ ∈][I]_[)] _[is][the][minimal][non-negative][solution][to][the] system of linear equations_ 

**==> picture [257 x 32] intentionally omitted <==**

_Proof._ First we show that _k[A]_ satisfies (3.1). If _X_ 0 = _i ∈ A_ , then _D[A]_ = 0, so _ki[A]_[= 0.][If] _[X]_[0][=] _[ i][ ̸∈][A]_[,][then] _[ D][A][≥][J]_[1][,][so][by][the Markov][property of][the] jump chain 

**==> picture [156 x 14] intentionally omitted <==**

so 

**==> picture [358 x 26] intentionally omitted <==**

and so 

**==> picture [78 x 26] intentionally omitted <==**

Suppose now that _y_ = ( _yi_ : _i ∈ I_ ) is another solution to (3.1). Then _ki[A]_[=] _[ y][i]_[= 0][for] _[i][ ∈][A]_[.][Suppose] _[i][ ̸∈][A]_[,][then] 

**==> picture [272 x 72] intentionally omitted <==**

_3. Continuous-time Markov chains II_ 

114 

By repeated substitution for _y_ in the final term we obtain after _n_ steps 

**==> picture [330 x 26] intentionally omitted <==**

So, if _y_ is non-negative 

**==> picture [200 x 35] intentionally omitted <==**

where we use the notation _H[A] ∧ n_ for the minimum of _H[A]_ and _n_ . Now 

**==> picture [67 x 35] intentionally omitted <==**

so, by monotone convergence, _yi ≥_ E _i_ ( _DA_ ) = _ki[A]_[,][as][required.] 

## **Exercise** 

**3.3.1** Consider the Markov chain on _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ with generator matrix 

**==> picture [163 x 49] intentionally omitted <==**

Calculate (a) the probability of hitting 3 starting from 1, (b) the expected time to hit 4 starting from 1. 

## **3.4 Recurrence and transience** 

Let ( _Xt_ ) _t≥_ 0 be Markov chain with generator matrix _Q_ . Recall that we insist ( _Xt_ ) _t≥_ 0 be minimal. We say a state _i_ is _recurrent_ if 

**==> picture [189 x 12] intentionally omitted <==**

We say that _i_ is _transient_ if 

**==> picture [189 x 12] intentionally omitted <==**

Note that if ( _Xt_ ) _t≥_ 0 can explode starting from _i_ then _i_ is certainly not recurrent. The next result shows that, like class structure, recurrence and transience are determined by the jump chain. 

_3.4 Recurrence and transience_ 

115 

**Theorem 3.4.1.** _We have:_ 

- (i) _if i is recurrent for the jump chain_ ( _Yn_ ) _n≥_ 0 _, then i is recurrent for_ ( _Xt_ ) _t≥_ 0 _;_ 

- (ii) _if i is transient for the jump chain, then i is transient for_ ( _Xt_ ) _t≥_ 0 _;_ 

- (iii) _every state is either recurrent or transient;_ 

- (iv) _recurrence and transience are class properties._ 

_Proof._ (i) Suppose _i_ is recurrent for ( _Yn_ ) _n≥_ 0. If _X_ 0 = _i_ then ( _Xt_ ) _t≥_ 0 does not explode and _Jn →∞_ by Theorem 2.7.1. Also _X_ ( _Jn_ ) = _Yn_ = _i_ infinitely often, so _{t ≥_ 0 : _Xt_ = _i}_ is unbounded, with probability 1. 

(ii) Suppose _i_ is transient for ( _Yn_ ) _n≥_ 0. If _X_ 0 = _i_ then 

**==> picture [148 x 12] intentionally omitted <==**

so _{t ≥_ 0 : _Xt_ = _i}_ is bounded by _J_ ( _N_ +1), which is finite, with probability 1, because ( _Yn_ : _n ≤ N_ ) cannot include an absorbing state. 

(iii) Apply Theorem 1.5.3 to the jump chain. 

- (iv) Apply Theorem 1.5.4 to the jump chain. 

The next result gives continuous-time analogues of the conditions for recurrence and transience found in Theorem 1.5.3. We denote by _Ti_ the _first passage time_ of ( _Xt_ ) _t≥_ 0 to state _i_ , defined by 

**==> picture [170 x 12] intentionally omitted <==**

**Theorem 3.4.2.** _The following dichotomy holds:_ 

(i) _if qi_ = 0 _or_ P _i_ ( _Ti < ∞_ ) = 1 _, then i is recurrent and_[�] 0 _[∞] pii_ ( _t_ ) _dt_ = _∞;_ (ii) _if qi >_ 0 _and_ P _i_ ( _Ti < ∞_ ) _<_ 1 _, then i is transient and_ �0 _∞ pii_ ( _t_ ) _dt < ∞._ 

_Proof._ If _qi_ = 0, then ( _Xt_ ) _t≥_ 0 cannot leave _i_ , so _i_ is recurrent, _pii_ ( _t_ ) = 1 _∞_ for all _t_ , and �0 _pii_ ( _t_ ) _dt_ = _∞_ . Suppose then that _qi >_ 0. Let _Ni_ denote the first passage time of the jump chain ( _Yn_ ) _n≥_ 0 to state _i_ . Then 

**==> picture [127 x 12] intentionally omitted <==**

so _i_ is recurrent if and only if P _i_ ( _Ti < ∞_ ) = 1, by Theorem 3.4.1 and the corresponding result for the jump chain. 

Write _πij_[(] _[n]_[)] for the ( _i, j_ ) entry in Π _[n]_ . We shall show that 

**==> picture [241 x 31] intentionally omitted <==**

so that _i_ is recurrent if and only if �0 _∞ pii_ ( _t_ ) _dt_ = _∞_ , by Theorem 3.4.1 and the corresponding result for the jump chain. 

_3. Continuous-time Markov chains II_ 

116 

To establish (3.2) we use Fubini’s theorem (see Section 6.4): 

**==> picture [257 x 98] intentionally omitted <==**

Finally, we show that recurrence and transience are determined by any discrete-time sampling of ( _Xt_ ) _t≥_ 0. 

**Theorem 3.4.3.** _Let h >_ 0 _be given and set Zn_ = _Xnh._ 

(i) _If i is recurrent for_ ( _Xt_ ) _t≥_ 0 _then i is recurrent for_ ( _Zn_ ) _n≥_ 0 _._ 

(ii) _If i is transient for_ ( _Xt_ ) _t≥_ 0 _then i is transient for_ ( _Zn_ ) _n≥_ 0 _._ 

_Proof._ Claim (ii) is obvious. To prove (i) we use for _nh ≤ t <_ ( _n_ + 1) _h_ the estimate 

**==> picture [128 x 15] intentionally omitted <==**

which follows from the Markov property. Then, by monotone convergence 

**==> picture [151 x 31] intentionally omitted <==**

and the result follows by Theorems 1.5.3 and 3.4.2. 

## **Exercise** 

**3.4.1** Customers arrive at a certain queue in a Poisson process of rate _λ_ . The single ‘server’ has two states _A_ and _B_ , state _A_ signifying that he is ‘in attendance’ and state _B_ that he is having a tea-break. Independently of how many customers are in the queue, he fluctuates between these states as a Markov chain _Y_ on _{A, B}_ with _Q_ -matrix 

**==> picture [68 x 27] intentionally omitted <==**

The total service time for any customer is exponentially distributed with parameter _µ_ and is independent of the chain _Y_ and of the service times of other customers. 

_3.5 Invariant distributions_ 

117 

Describe the system as a Markov chain _X_ with state-space 

**==> picture [178 x 12] intentionally omitted <==**

_An_ signifying that the server is in state _A_ and there are _n_ people in the queue (including anyone being served) and _Bn_ signifying that the server is in state _B_ and there are _n_ people in the queue. 

Explain why, for some _θ_ in (0 _,_ 1], and _k_ = 0 _,_ 1 _,_ 2 _, . . ._ , 

**==> picture [142 x 14] intentionally omitted <==**

Show that ( _θ −_ 1) _f_ ( _θ_ ) = 0, where 

**==> picture [218 x 14] intentionally omitted <==**

By considering _f_ (1) or otherwise, prove that _X_ is transient if _µβ < λ_ ( _α_ + _β_ ), and explain why this is intuitively obvious. 

## **3.5 Invariant distributions** 

Just as in the discrete-time theory, the notions of invariant distribution and measure play an important role in the study of continuous-time Markov chains. We say that _λ_ is _invariant_ if 

**==> picture [39 x 11] intentionally omitted <==**

**Theorem 3.5.1.** _Let Q be a Q-matrix with jump matrix_ Π _and let λ be a measure. The following are equivalent:_ 

**==> picture [85 x 12] intentionally omitted <==**

**==> picture [139 x 12] intentionally omitted <==**

_Proof._ We have _qi_ ( _πij − δij_ ) = _qij_ for all _i, j_ , so 

**==> picture [248 x 25] intentionally omitted <==**

This tie-up with measures invariant for the jump matrix means that we can use the existence and uniqueness results of Section 1.7 to obtain the following result. 

_3. Continuous-time Markov chains II_ 

118 

**Theorem 3.5.2.** _Suppose that Q is irreducible and recurrent. Then Q has an invariant measure λ which is unique up to scalar multiples._ 

_Proof._ Let us exclude the trivial case _I_ = _{i}_ ; then irreducibility forces _qi >_ 0 for all _i_ . By Theorems 3.2.1 and 3.4.1, Π is irreducible and recurrent. Then, by Theorems 1.7.5 and 1.7.6, Π has an invariant measure _µ_ , which is unique up to scalar multiples. So, by Theorem 3.5.1, we can take _λi_ = _µi/qi_ to obtain an invariant measure unique up to scalar multiples. 

Recall that a state _i_ is recurrent if _qi_ = 0 or P _i_ ( _Ti < ∞_ ) = 1. If _qi_ = 0 or the _expected return time mi_ = E _i_ ( _Ti_ ) is finite then we say _i_ is _positive recurrent_ . Otherwise a recurrent state _i_ is called _null recurrent_ . As in the discrete-time case positive recurrence is tied up with the existence of an invariant distribution. 

**Theorem 3.5.3.** _Let Q be an irreducible Q-matrix. Then the following are equivalent:_ 

- (i) _every state is positive recurrent;_ 

- (ii) _some state i is positive recurrent;_ 

- (iii) _Q is non-explosive and has an invariant distribution λ._ 

Moreover, when (iii) holds we have _mi_ = 1 _/_ ( _λiqi_ ) for all _i_ . 

**==> picture [358 x 68] intentionally omitted <==**

where _Ti ∧ ζ_ denotes the minimum of _Ti_ and _ζ_ . By monotone convergence, 

**==> picture [95 x 26] intentionally omitted <==**

Denote by _Ni_ the first passage time of the jump chain to state _i_ . By Fubini’s theorem 

**==> picture [213 x 143] intentionally omitted <==**

_3.5 Invariant distributions_ 

119 

where, in the notation of Section 1.7, _γj[i]_[is][the][expected][time][in] _[j]_[between] visits to _i_ for the jump chain. 

Suppose (ii) holds, then _i_ is certainly recurrent, so the jump chain is recurrent, and _Q_ is non-explosive, by Theorem 2.7.1. We know that _γ[i]_ Π = _γ[i]_ by Theorem 1.7.5, so _µ[i] Q_ = 0 by Theorem 3.5.1. But _µ[i]_ has finite total mass 

**==> picture [102 x 26] intentionally omitted <==**

so we obtain an invariant distribution _λ_ by setting _λj_ = _µ[i] j[/m][i]_[.] 

On the other hand, suppose (iii) holds. Fix _i ∈ I_ and set _νj_ = _λjqj/_ ( _λiqi_ ); then _νi_ = 1 and _ν_ Π = _ν_ by Theorem 3.5.1, so _νj ≥ γj[i]_[for] all _j_ by Theorem 1.7.6. So 

**==> picture [172 x 57] intentionally omitted <==**

showing that _i_ is positive recurrent. 

To complete the proof we return to the preceding calculation armed with the knowledge that _Q_ is recurrent, hence Π is recurrent, _νj_ = _γj[i]_[and] _mi_ = 1 _/_ ( _λiqi_ ) for all _i_ . 

The following example is a caution that the existence of an invariant distribution for a continuous-time Markov chain is not enough to guarantee positive recurrence, or even recurrence. 

## **Example 3.5.4** 

Consider the Markov chain ( _Xt_ ) _t≥_ 0 on Z[+] with the following diagram, where _qi >_ 0 for all _i_ and where 0 _< λ_ = 1 _− µ <_ 1: 

**==> picture [285 x 30] intentionally omitted <==**

The jump chain behaves as a simple random walk away from 0, so ( _Xt_ ) _t≥_ 0 is recurrent if _λ ≤ µ_ and transient if _λ > µ_ . To compute an invariant measure _ν_ it is convenient to use the _detailed balance equations_ 

**==> picture [130 x 12] intentionally omitted <==**

_3. Continuous-time Markov chains II_ 

120 

Look ahead to Lemma 3.7.2 to see that any solution is invariant. In this case the non-zero equations read 

**==> picture [147 x 11] intentionally omitted <==**

So a solution is given by _νi_ = _qi[−]_[1] ( _λ/µ_ ) _[i]_ . If the jump rates _qi_ are constant then _ν_ can be normalized to produce an invariant distribution precisely when _λ < µ_ . 

Consider, on the other hand, the case where _qi_ = 2 _[i]_ for all _i_ and 1 _< λ/µ <_ 2. Then _ν_ has finite total mass so ( _Xt_ ) _t≥_ 0 has an invariant distribution, but ( _Xt_ ) _t≥_ 0 is also transient. Given Theorem 3.5.3, the only possibility is that ( _Xt_ ) _t≥_ 0 is explosive. 

The next result justifies calling measures _λ_ with _λQ_ = 0 invariant. 

**Theorem 3.5.5.** _Let Q be irreducible and recurrent, and let λ be a measure. Let s >_ 0 _be given. The following are equivalent:_ 

**==> picture [57 x 12] intentionally omitted <==**

- (ii) _λP_ ( _s_ ) = _λ._ 

_Proof._ There is a very simple proof in the case of finite state-space: by the backward equation 

**==> picture [140 x 24] intentionally omitted <==**

so _λQ_ = 0 implies _λP_ ( _s_ ) = _λP_ (0) = _λ_ for all _s_ ; _P_ ( _s_ ) is also recurrent, so _µP_ ( _s_ ) = _µ_ implies that _µ_ is proportional to _λ_ , so _µQ_ = 0. 

For infinite state-space, the interchange of differentiation with the summation involved in multiplication by _λ_ is not justified and an entirely different proof is needed. 

Since _Q_ is recurrent, it is non-explosive by Theorem 2.7.1, and _P_ ( _s_ ) is recurrent by Theorem 3.4.3. Hence any _λ_ satisfying (i) or (ii) is unique up to scalar multiples; and from the proof of Theorem 3.5.3, if we fix _i_ and set 

**==> picture [111 x 29] intentionally omitted <==**

then _µQ_ = 0. Thus it suffices to show _µP_ ( _s_ ) = _µ_ . By the strong Markov property at _Ti_ (which is a simple consequence of the strong Markov property of the jump chain) 

**==> picture [187 x 30] intentionally omitted <==**

_3.6 Convergence to equilibrium_ 

121 

Hence, using Fubini’s theorem, 

**==> picture [180 x 159] intentionally omitted <==**

as required. 

**Theorem 3.5.6.** _Let Q be an irreducible non-explosive Q-matrix having an invariant distribution λ. If_ ( _Xt_ ) _t≥_ 0 _is Markov_ ( _λ, Q_ ) _then so is_ ( _Xs_ + _t_ ) _t≥_ 0 _for any s ≥_ 0 _._ 

_Proof._ By Theorem 3.5.5, for all _i_ , 

**==> picture [128 x 12] intentionally omitted <==**

so, by the Markov property, conditional on _Xs_ = _i_ , ( _Xs_ + _t_ ) _t≥_ 0 is Markov( _δi, Q_ ). 

## **3.6 Convergence to equilibrium** 

We now investigate the limiting behaviour of _pij_ ( _t_ ) as _t →∞_ and its relation to invariant distributions. You will see that the situation is analogous to the case of discrete-time, only there is no longer any possibility of periodicity. 

We shall need the following estimate of uniform continuity for the transition probabilities. 

**Lemma 3.6.1.** _Let Q be a Q-matrix with semigroup P_ ( _t_ ) _. Then, for all t, h ≥_ 0 

**==> picture [153 x 14] intentionally omitted <==**

_Proof._ We have 

**==> picture [247 x 85] intentionally omitted <==**

_3. Continuous-time Markov chains II_ 

122 

**Theorem 3.6.2 (Convergence to equilibrium).** _Let Q be an irreducible non-explosive Q-matrix with semigroup P_ ( _t_ ) _, and having an invariant distribution λ. Then for all states i, j we have_ 

**==> picture [122 x 12] intentionally omitted <==**

_Proof._ Let ( _Xt_ ) _t≥_ 0 be Markov( _δi, Q_ ). Fix _h >_ 0 and consider the _h_ - _skeleton Zn_ = _Xnh_ . By Theorem 2.8.4 

**==> picture [247 x 14] intentionally omitted <==**

so ( _Zn_ ) _n≥_ 0 is discrete-time Markov( _δi, P_ ( _h_ )). By Theorem 3.2.1 irreducibility implies _pij_ ( _h_ ) _>_ 0 for all _i, j_ so _P_ ( _h_ ) is irreducible and aperiodic. By Theorem 3.5.5, _λ_ is invariant for _P_ ( _h_ ). So, by discrete-time convergence to equilibrium, for all _i, j_ 

**==> picture [133 x 12] intentionally omitted <==**

Thus we have a lattice of points along which the desired limit holds; we fill in the gaps using uniform continuity. Fix a state _i_ . Given _ε >_ 0 we can find _h >_ 0 so that 

**==> picture [160 x 12] intentionally omitted <==**

and then find _N_ , so that 

**==> picture [170 x 13] intentionally omitted <==**

For _t ≥ Nh_ we have _nh ≤ t <_ ( _n_ + 1) _h_ for some _n ≥ N_ and 

**==> picture [250 x 12] intentionally omitted <==**

by Lemma 3.6.1. Hence 

**==> picture [124 x 13] intentionally omitted <==**

The complete description of limiting behaviour for irreducible chains in continuous time is provided by the following result. It follows from Theorem 1.8.5 by the same argument we used in the preceding result. We do not give the details. 

_3.7 Time reversal_ 

123 

**Theorem 3.6.3.** _Let Q be an irreducible Q-matrix and let ν be any distribution. Suppose that_ ( _Xt_ ) _t≥_ 0 _is Markov_ ( _ν, Q_ ) _. Then_ 

**==> picture [243 x 12] intentionally omitted <==**

_where mj is the expected return time to state j._ 

## **Exercises** 

**3.6.1** Find an invariant distribution _λ_ for the _Q_ -matrix 

**==> picture [111 x 41] intentionally omitted <==**

and verify that lim _t→∞ p_ 11( _t_ ) = _λ_ 1 using your answer to Exercise 2.1.1. 

**3.6.2** In each of the following cases, compute lim _t→∞_ P( _Xt_ = 2 _|X_ 0 = 1) for the Markov chain ( _Xt_ ) _t≥_ 0 with the given _Q_ -matrix on _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ : 

**==> picture [292 x 103] intentionally omitted <==**

**3.6.3** Customers arrive at a single-server queue in a Poisson stream of rate _λ_ . Each customer has a service requirement distributed as the sum of two independent exponential random variables of parameter _µ_ . Service requirements are independent of one another and of the arrival process. Write down the generator matrix _Q_ of a continuous-time Markov chain which models this, explaining what the states of the chain represent. Calculate the essentially unique invariant measure for _Q_ , and deduce that the chain is positive recurrent if and only if _λ/µ <_ 1 _/_ 2. 

## **3.7 Time reversal** 

Time reversal of continuous-time chains has the same features found in the discrete-time case. Reversibility provides a powerful tool in the analysis of Markov chains, as we shall see in Section 5.2. Note in the following 

_3. Continuous-time Markov chains II_ 

124 

result how time reversal interchanges the roles of backward and forward equations. This echoes our proof of the forward equation, which rested on the time reversal identity of Lemma 2.8.5. 

A small technical point arises in time reversal: right-continuous processes become left-continuous processes. For the processes we consider, this is unimportant. We could if we wished redefine the time-reversed process to equal its right limit at the jump times, thus obtaining again a rightcontinuous process. We shall suppose implicitly that this is done, and forget about the problem. 

**Theorem 3.7.1.** _Let Q be irreducible and non-explosive and suppose that Q has an invariant distribution λ. Let T ∈_ (0 _, ∞_ ) _be given and let_ ( _Xt_ )0 _≤t≤T be Markov_ ( _λ, Q_ ) _. Set X_[�] _t_ = _XT −t. Then the process_ ( _X_[�] _t_ )0 _≤t≤T_ � � _is Markov_ ( _λ, Q_[�] ) _, where Q_[�] = ( _qij_ : _i, j ∈ I_ ) _is given by λjqji_ = _λiqij. Moreover, Q_[�] _is also irreducible and non-explosive with invariant distribution λ. Proof._ By Theorem 2.8.6, the semigroup � _P_ ( _t_ ) : _t ≥_ 0� of _Q_ is the minimal non-negative solution of the forward equation 

**==> picture [131 x 13] intentionally omitted <==**

Also, for all _t >_ 0, _P_ ( _t_ ) is an irreducible stochastic matrix with invariant distribution _λ_ . Define _P_[�] ( _t_ ) by 

**==> picture [91 x 13] intentionally omitted <==**

then _P_[�] ( _t_ ) is an irreducible stochastic matrix with invariant distribution _λ_ , and we can rewrite the forward equation transposed as 

**==> picture [73 x 15] intentionally omitted <==**

But� this is the backward equation for _Q_[�] , which is itself� a _Q_ -matrix, and _P_ ( _t_ ) is then its minimal non-negative solution. Hence _Q_ is irreducible and non-explosive and has invariant distribution _λ_ . 

Finally, for 0 = _t_ 0 _< . . . < tn_ = _T_ and _sk_ = _tk − tk−_ 1, by Theorem 2.8.4 we have 

**==> picture [291 x 49] intentionally omitted <==**

so, by Theorem 2.8.4 again, ( _X_[�] _t_ )0 _≤t≤T_ is Markov( _λ, Q_[�] ). 

The chain ( _X_[�] _t_ )0 _≤t≤T_ is called the _time-reversal_ of ( _Xt_ )0 _≤t≤T_ . 

**==> picture [323 x 11] intentionally omitted <==**

**==> picture [133 x 12] intentionally omitted <==**

_3.8 Ergodic theorem_ 

125 

**Lemma 3.7.2.** _If Q and λ are in detailed balance then λ is invariant for Q._ 

_Proof._ We have ( _λQ_ ) _i_ =[�] _j∈I[λ][j][q][ji]_[=][ �] _j∈I[λ][i][q][ij]_[= 0.] 

Let ( _Xt_ ) _t≥_ 0 be Markov( _λ, Q_ ), with _Q_ irreducible and non-explosive. We say that ( _Xt_ ) _t≥_ 0 is _reversible_ if, for all _T >_ 0, ( _XT −t_ )0 _≤t≤T_ is also Markov( _λ, Q_ ). 

**Theorem 3.7.3.** _Let Q be an irreducible and non-explosive Q-matrix and let λ be a distribution. Suppose that_ ( _Xt_ ) _t≥_ 0 _is Markov_ ( _λ, Q_ ) _. Then the following are equivalent:_ 

- (a) ( _Xt_ ) _t≥_ 0 _is reversible;_ 

- (b) _Q and λ are in detailed balance._ 

_Proof._ Both (a) and (b) imply that _λ_ is invariant for _Q_ . Then both (a) and (b) are equivalent to the statement that _Q_[�] = _Q_ in Theorem 3.7.1. 

## **Exercise** 

**3.7.1** Consider a fleet of _N_ buses. Each bus breaks down independently at rate _µ_ , when it is sent to the depot for repair. The repair shop can only repair one bus at a time and each bus takes an exponential time of parameter _λ_ to repair. Find the equilibrium distribution of the number of buses in service. 

**3.7.2** Calls arrive at a telephone exchange as a Poisson process of rate _λ_ , and the lengths of calls are independent exponential random variables of parameter _µ_ . Assuming that infinitely many telephone lines are available, set up a Markov chain model for this process. 

Show that for large _t_ the distribution of the number of lines in use at time _t_ is approximately Poisson with mean _λ/µ_ . 

Find the mean length of the busy periods during which at least one line is in use. 

Show that the expected number of lines in use at time _t_ , given that _n_ are in use at time 0, is _ne[−][µt]_ + _λ_ (1 _− e[−][µt]_ ) _/µ_ . 

Show that, in equilibrium, the number _Nt_ of calls finishing in the time interval [0 _, t_ ] has Poisson distribution of mean _λt_ . 

Is ( _Nt_ ) _t≥_ 0 a Poisson process? 

## **3.8 Ergodic theorem** 

Long-run averages for continuous-time chains display the same sort of behaviour as in the discrete-time case, and for similar reasons. Here is the result. 

_3. Continuous-time Markov chains II_ 

126 

**Theorem 3.8.1 (Ergodic theorem).** _Let Q be irreducible and let ν be any distribution. If_ ( _Xt_ ) _t≥_ 0 _is Markov_ ( _ν, Q_ ) _, then_ 

**==> picture [212 x 28] intentionally omitted <==**

_where mi_ = E _i_ ( _Ti_ ) _is the expected return time to state i. Moreover, in the positive recurrent case, for any bounded function f_ : _I →_ R _we have_ 

**==> picture [185 x 29] intentionally omitted <==**

_where_ 

**==> picture [58 x 25] intentionally omitted <==**

_and where_ ( _λi_ : _i ∈ I_ ) _is the unique invariant distribution._ 

_Proof._ If _Q_ is transient then the total time spent in any state _i_ is finite, so 

**==> picture [223 x 28] intentionally omitted <==**

Suppose then that _Q_ is recurrent and fix a state _i_ . Then ( _Xt_ ) _t≥_ 0 hits _i_ with probability 1 and the long-run proportion of time in _i_ equals the longrun proportion of time in _i_ after first hitting _i_ . So, by the strong Markov property (of the jump chain), it suffices to consider the case _ν_ = _δi_ . 

Denote by _Mi[n]_[the][length][of][the] _[n]_[th][visit][to] _[i]_[,][by] _[T] i[ n]_ the time of the _n_ th return to _i_ and by _L[n] i_[the][length][of][the] _[n]_[th][excursion][to] _[i]_[.][Thus][for] _n_ = 0 _,_ 1 _,_ 2 _, . . ._ , setting _Ti_[0][= 0,][we][have] 

**==> picture [184 x 51] intentionally omitted <==**

By the strong Markov property (of the jump chain) at the stopping times _Ti[n]_[for] _[n][≥]_[0][we][find][that] _[L]_[1] _i[, L]_[2] _i[, . . .]_[are][independent][and][identically][dis-] tributed with mean _mi_ , and that _Mi_[1] _[, M]_[ 2] _i[, . . .]_[are][independent][and][identi-] cally distributed with mean 1 _/qi_ . Hence, by the strong law of large numbers (see Theorem 1.10.1) 

**==> picture [163 x 56] intentionally omitted <==**

_3.8 Ergodic theorem_ 

127 

and hence 

**==> picture [177 x 29] intentionally omitted <==**

with probability 1. In particular, we note that _Ti[n][/T] i[ n]_[+1] _→_ 1 as _n →∞_ with probability 1. Now, for _Ti[n][≤][t < T] i[ n]_[+1] we have 

**==> picture [329 x 30] intentionally omitted <==**

so on letting _t →∞_ we have, with probability 1 

**==> picture [120 x 28] intentionally omitted <==**

In the positive recurrent case we can write 

**==> picture [246 x 32] intentionally omitted <==**

where _λi_ = 1 _/_ ( _miqi_ ). We conclude that 

**==> picture [148 x 28] intentionally omitted <==**

with probability 1, by the same argument as was used in the proof of Theorem 1.10.2. 

**4** 

## Further theory 

In the first three chapters we have given an account of the elementary theory of Markov chains. This already covers a great many applications, but is just the beginning of the theory of Markov processes. The further theory inevitably involves more sophisticated techniques which, although having their own interest, can obscure the overall structure. On the other hand, the overall structure is, to a large extent, already present in the elementary theory. We therefore thought it worth while to discuss some features of the further theory in the context of simple Markov chains, namely, martingales, potential theory, electrical networks and Brownian motion. The idea is that the Markov chain case serves as a guiding metaphor for more complicated processes. So the reader familiar with Markov chains may find this chapter helpful alongside more general higher-level texts. At the same time, further insight is gained into Markov chains themselves. 

## **4.1 Martingales** 

A martingale is a process whose average value remains constant in a particular strong sense, which we shall make precise shortly. This is a sort of balancing property. Often, the identification of martingales is a crucial step in understanding the evolution of a stochastic process. 

We begin with a simple example. Consider the simple symmetric random walk ( _Xn_ ) _n≥_ 0 on Z, which is a Markov chain with the following diagram 

_4.1 Martingales_ 

129 

**==> picture [220 x 34] intentionally omitted <==**

The average value of the walk is constant; indeed it has the stronger property that the average value of the walk at some future time is always simply the current value. In precise terms we have 

**==> picture [62 x 10] intentionally omitted <==**

and the stronger property says that, for _n ≥ m_ , 

**==> picture [202 x 12] intentionally omitted <==**

This stronger property says that ( _Xn_ ) _n≥_ 0 is in fact a martingale. 

Here is the general definition. Let us fix for definiteness a Markov chain ( _Xn_ ) _n≥_ 0 and write _Fn_ for the collection of all sets depending only on _X_ 0 _, . . . , Xn_ . The sequence ( _Fn_ ) _n≥_ 0 is called the _filtration_ of ( _Xn_ ) _n≥_ 0 and we think of _Fn_ as representing the state of knowledge, or history, of the chain up to time _n_ . A process ( _Mn_ ) _n≥_ 0 is called _adapted_ if _Mn_ depends only on _X_ 0 _, . . . , Xn_ . A process ( _Mn_ ) _n≥_ 0 is called _integrable_ if E _|Mn| < ∞_ for all _n_ . An adapted integrable process ( _Mn_ ) _n≥_ 0 is called a _martingale_ if 

**==> picture [113 x 12] intentionally omitted <==**

for all _A ∈Fn_ and all _n_ . Since the collection _Fn_ consists of countable unions of elementary events such as 

**==> picture [160 x 12] intentionally omitted <==**

this martingale property is equivalent to saying that 

**==> picture [207 x 12] intentionally omitted <==**

for all _i_ 0 _, . . . , in_ and all _n_ . 

A third formulation of the martingale property involves another notion of conditional expectation. Given an integrable random variable _Y_ , we define 

**==> picture [318 x 25] intentionally omitted <==**

_4. Further theory_ 

130 

The random variable E( _Y | Fn_ ) is called the _conditional expectation_ of _Y_ given _Fn_ . In passing from _Y_ to E( _Y | Fn_ ), what we do is to replace on each elementary event _A ∈Fn_ , the random variable _Y_ by its average value E( _Y | A_ ). It is easy to check that an adapted integrable process ( _Mn_ ) _n≥_ 0 is a martingale if and only if 

**==> picture [151 x 12] intentionally omitted <==**

Conditional expectation is a partial averaging, so if we complete the process and average the conditional expectation we should get the full expectation 

**==> picture [108 x 14] intentionally omitted <==**

It is easy to check that this formula holds. 

In particular, for a martingale 

**==> picture [190 x 14] intentionally omitted <==**

so, by induction 

**==> picture [82 x 12] intentionally omitted <==**

This was already clear on taking _A_ = Ωin our original definition of a martingale. 

We shall prove one general result about martingales, then see how it explains some things we know about the simple symmetric random walk. Recall that a random variable 

**==> picture [134 x 12] intentionally omitted <==**

is a _stopping time_ if _{T_ = _n} ∈Fn_ for all _n < ∞_ . An equivalent condition is that _{T ≤ n} ∈Fn_ for all _n < ∞_ . Recall from Section 1.4 that all sorts of hitting times are stopping times. 

**Theorem 4.1.1 (Optional stopping theorem).** _Let_ ( _Mn_ ) _n≥_ 0 _be a martingale and let T be a stopping time. Suppose that at least one of the following conditions holds:_ 

(i) _T ≤ n for some n;_ 

(ii) _T < ∞ and |Mn| ≤ C whenever n ≤ T . Then_ E _MT_ = E _M_ 0 _._ 

_Proof._ Assume that (i) holds. Then 

**==> picture [223 x 52] intentionally omitted <==**

_4.1 Martingales_ 

131 

Now _{k < T }_ = _{T ≤ k}[c] ∈Fk_ since _T_ is a stopping time, and so 

**==> picture [124 x 12] intentionally omitted <==**

since ( _Mk_ ) _k≥_ 0 is a martingale. Hence 

**==> picture [221 x 33] intentionally omitted <==**

If we do not assume (i) but (ii), then the preceding argument applies to the stopping time _T ∧ n_ , so that E _MT ∧n_ = E _M_ 0. Then 

**==> picture [324 x 12] intentionally omitted <==**

for all _n_ . But P( _T > n_ ) _→_ 0 as _n →∞_ , so E _MT_ = E _M_ 0. 

Returning to the simple symmetric random walk ( _Xn_ ) _n≥_ 0, suppose that _X_ 0 = 0 and we take 

**==> picture [194 x 11] intentionally omitted <==**

where _a, b ∈_ N are given. Then _T_ is a stopping time and _T < ∞_ by recurrence of finite closed classes. Thus condition (ii) of the optional stopping theorem applies with _Mn_ = _Xn_ and _C_ = _a ∨ b_ . We deduce that E _XT_ = E _X_ 0 = 0. So what? Well, now we can compute 

**==> picture [135 x 12] intentionally omitted <==**

We have _XT_ = _−a_ with probability _p_ and _XT_ = _b_ with probability 1 _− p_ , so 

**==> picture [138 x 12] intentionally omitted <==**

giving 

**==> picture [67 x 12] intentionally omitted <==**

There is an entirely different, Markovian, way to compute _p_ , using the methods of Section 1.4. But the intuition behind the result E _XT_ = 0 is very clear: a gambler, playing a fair game, leaves the casino once losses reach _a_ or winnings reach _b_ , whichever is sooner; since the game is fair, the average gain should be zero. 

We discussed in Section 1.3 the counter-intuitive case of a gambler who keeps on playing a fair game against an infinitely rich casino, with the certain outcome of ruin. This game ends at the finite stopping time 

**==> picture [128 x 12] intentionally omitted <==**

_4. Further theory_ 

132 

where _a_ is the gambler’s initial fortune. Since _XT_ = _−a_ we have 

**==> picture [108 x 11] intentionally omitted <==**

but this does not contradict the optional stopping theorem because neither condition (i) nor condition (ii) is satisfied. Thus, while intuition might suggest that E _XT_ = E _X_ 0 is rather obvious, some care is needed as it is not always true. 

The example just discussed was rather special in that the chain ( _Xn_ ) _n≥_ 0 itself was a martingale. Obviously, this is not true in general; indeed a martingale is necessarily real-valued and we do not in general insist that the state-space _I_ is contained in R. Nevertheless, to every Markov chain is associated a whole collection of martingales, and these martingales characterize the chain. This is the basis of a deep connection between martingales and Markov chains. 

We recall that, given a function _f_ : _I →_ R and a Markov chain ( _Xn_ ) _n≥_ 0 with transition matrix _P_ , we have 

**==> picture [172 x 27] intentionally omitted <==**

**Theorem 4.1.2.** _Let_ ( _Xn_ ) _n≥_ 0 _be a random process with values in I and let P be a stochastic matrix. Write_ ( _Fn_ ) _n≥_ 0 _for the filtration of_ ( _Xn_ ) _n≥_ 0 _. Then the following are equivalent:_ 

- (i) ( _Xn_ ) _n≥_ 0 _is a Markov chain with transition matrix P ;_ 

- (ii) _for all bounded functions f_ : _I →_ R _, the following process is a martingale:_ 

**==> picture [209 x 33] intentionally omitted <==**

_Proof._ Suppose (i) holds. Let _f_ be a bounded function. Then 

**==> picture [156 x 26] intentionally omitted <==**

so 

**==> picture [140 x 21] intentionally omitted <==**

showing that _Mn[f]_[is][integrable][for][all] _[n]_[.] 

**==> picture [283 x 12] intentionally omitted <==**

**==> picture [202 x 14] intentionally omitted <==**

_4.1 Martingales_ 

133 

so 

E( _Mn[f]_ +1 _[−][M][ f] n[|][ A]_[) =][ E][[] _[f]_[(] _[X][n]_[+1][)] _[ −]_[(] _[Pf]_[)(] _[X][n]_[)] _[ |][ A]_[] = 0] and so ( _Mn[f]_[)] _[n][≥]_[0][is][a][martingale.] On the other hand, if (ii) holds, then 

**==> picture [248 x 12] intentionally omitted <==**

for all bounded functions _f_ . On taking _f_ = 1 _{in_ +1 _}_ we obtain 

**==> picture [236 x 13] intentionally omitted <==**

so ( _Xn_ ) _n≥_ 0 is Markov with transition matrix _P_ . 

Some more martingales associated to a Markov chain are described in the next result. Notice that we drop the requirement that _f_ be bounded. 

**Theorem 4.1.3.** _Let_ ( _Xn_ ) _n≥_ 0 _be a Markov chain with transition matrix P . Suppose that a function f_ : Z[+] _× I →_ R _satisfies, for all n ≥_ 0 _, both_ 

**==> picture [82 x 12] intentionally omitted <==**

_and_ 

**==> picture [211 x 26] intentionally omitted <==**

_Then Mn_ = _f_ ( _n, Xn_ ) _is a martingale._ 

_Proof._ We have assumed that _Mn_ is integrable for all _n_ . Then, by the Markov property 

**==> picture [346 x 29] intentionally omitted <==**

**==> picture [137 x 12] intentionally omitted <==**

Let us see how this theorem works in the case where ( _Xn_ ) _n≥_ 0 is a simple random walk on Z, starting from 0. We consider _f_ ( _i_ ) = _i_ and _g_ ( _n, i_ ) = _i_[2] _− n_ . Since _|Xn| ≤ n_ for all _n_ , we have 

**==> picture [168 x 12] intentionally omitted <==**

Also 

**==> picture [326 x 31] intentionally omitted <==**

Hence both _Xn_ = _f_ ( _Xn_ ) and _Yn_ = _g_ ( _n, Xn_ ) are martingales. 

_4. Further theory_ 

134 

In order to put this to some use, consider again the stopping time 

**==> picture [194 x 11] intentionally omitted <==**

where _a, b ∈_ N. By the optional stopping theorem 

**==> picture [220 x 14] intentionally omitted <==**

Hence 

**==> picture [104 x 14] intentionally omitted <==**

On letting _n →∞_ , the left side converges to E( _T_ ), by monotone convergence, and the right side to E( _XT_[2][)][by][bounded][convergence.][So][we][obtain] 

**==> picture [186 x 13] intentionally omitted <==**

We have given only the simplest examples of the use of martingales in studying Markov chains. Some more will appear in later sections. For an excellent introduction to martingales and their applications we recommend _Probability with Martingales_ by David Williams (Cambridge University Press, 1991). 

## **Exercise** 

**4.1.1** Let ( _Xn_ ) _n≥_ 0 be a Markov chain on _I_ and let _A_ be an absorbing set in _I_ . Set 

**==> picture [120 x 12] intentionally omitted <==**

and 

**==> picture [226 x 12] intentionally omitted <==**

Show that _Mn_ = _h_ ( _Xn_ ) is a martingale. 

## **4.2 Potential theory** 

Several physical theories share a common mathematical framework, which is known as potential theory. One example is Newton’s theory of gravity, but potential theory is also relevant to electrostatics, fluid flow and the diffusion of heat. In gravity, a distribution of mass, of density _ρ_ say, gives rise to a gravitational potential _φ_ , which in suitable units satisfies the equation 

**==> picture [48 x 11] intentionally omitted <==**

where ∆= _∂_[2] _/∂x_[2] + _∂_[2] _/∂y_[2] + _∂_[2] _/∂z_[2] . The potential _φ_ is felt physically through its gradient 

**==> picture [104 x 27] intentionally omitted <==**

_4.2 Potential theory_ 

135 

which gives the force of gravity acting on a particle of unit mass. Markov chains, where space is discrete, obviously have no direct link with this theory, in which space is a continuum. An indirect link is provided by Brownian motion, which we shall discuss in Section 4.4. 

In this section we are going to consider _potential theory for a countable state-space_ , which has much of the structure of the continuum version. This discrete theory amounts to doing Markov chains without the probability, which has the disadvantage that one loses the intuitive picture of the process, but the advantage of wider applicability. We shall begin by introducing the idea of potentials associated to a Markov chain, and by showing how to calculate these potentials. This is a unifying idea, containing within it other notions previously considered such as hitting probabilities and expected hitting times. It also finds application when one associates costs to Markov chains in modelling economic activity: see Section 5.4. 

Once we have established the basic link between a Markov chain and its associated potentials, we shall briefly run through some of the main features of potential theory, explaining their significance in terms of Markov chains. This is the easiest way to appreciate the general structure of potential theory, unobscured by technical difficulties. The basic ideas of boundary theory for Markov chains will also be introduced. 

Before we embark on a general discussion of potentials associated to a Markov chain, here are two simple examples. In these examples the potential _φ_ has the interpretation of expected total cost. 

**==> picture [128 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 4<br>3<br>2 5<br>**----- End of picture text -----**<br>


**Example 4.2.1** 

Consider the discrete-time random walk on the directed graph shown above, which at each step choses among the allowable transitions with equal probability. Suppose that on each visit to states _i_ = 1 _,_ 2 _,_ 3 _,_ 4 a cost _ci_ is incurred, where _ci_ = _i_ . What is the fair price to move from state 3 to state 4? 

The fair price is always the difference in the expected total cost. We denote by _φi_ the expected total cost starting from _i_ . Obviously, _φ_ 5 = 0 and 

_4. Further theory_ 

136 

by considering the effect of a single step we see that 

**==> picture [99 x 64] intentionally omitted <==**

Hence _φ_ 3 = 8 and the fair price to move from 3 to 4 is 4. 

We shall now consider two variations on this problem. First suppose our process is, instead, the continuous-time random walk ( _Xt_ ) _t≥_ 0 on the same directed graph which makes each allowable transition at rate 1, and suppose cost is incurred at rate _ci_ = _i_ in state _i_ for _i_ = 1 _,_ 2 _,_ 3 _,_ 4. Thus the total cost is now 

**==> picture [64 x 26] intentionally omitted <==**

What now is the fair price to move from 3 to 4? The expected cost incurred on each visit to _i_ is given by _ci/qi_ and _q_ 1 = 1 _, q_ 2 = 1 _, q_ 3 = 3 _, q_ 4 = 1. So we see, as before 

**==> picture [101 x 64] intentionally omitted <==**

Hence _φ_ 3 = 5 and the fair price to move from 3 to 4 is 1. 

**==> picture [128 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 4<br>3<br>2 5<br>**----- End of picture text -----**<br>


In the second variation we consider the discrete-time random walk ( _Xn_ ) _n≥_ 0 on the modified graph shown above. Where there is no arrow, transitions are allowed in both directions. Obviously, states 1 and 5 are absorbing. We impose a cost _ci_ = _i_ on each visit to _i_ for _i_ = 2 _,_ 3 _,_ 4, and a final cost _fi_ on arrival at _i_ = 1 or 5, where _fi_ = _i_ . Thus the total cost is now 

**==> picture [93 x 33] intentionally omitted <==**

_4.2 Potential theory_ 

137 

where _T_ is the hitting time of _{_ 1 _,_ 5 _}_ . Write, as before, _φi_ for the expected total cost starting from _i_ . Then _φ_ 1 = 1, _φ_ 5 = 5 and 

**==> picture [150 x 50] intentionally omitted <==**

On solving these equations we obtain _φ_ 2 = 7, _φ_ 3 = 9 and _φ_ 4 = 11. So in this case the fair price to move from 3 to 4 is _−_ 2. 

## **Example 4.2.2** 

Consider the simple discrete-time random walk on Z with transition probabilities _pi,i−_ 1 = _q < p_ = _pi,i_ +1. Let _c >_ 0 and suppose that a cost _c[i]_ is incurred every time the walk visits state _i_ . What is the expected total cost _φ_ 0 incurred by the walk starting from 0? 

We must be prepared to find that _φ_ 0 = _∞_ for some values of _c_ , as the total cost is a sum over infinitely many times. Indeed, we know that the walk _Xn →∞_ with probability 1, so for _c ≥_ 1 we shall certainly have _φ_ 0 = _∞_ . 

Let _φi_ denote the expected total cost starting from _i_ . On moving one step to the right, all costs are multiplied by _c_ , so we must have 

**==> picture [55 x 11] intentionally omitted <==**

By considering what happens on the first step, we see 

**==> picture [196 x 12] intentionally omitted <==**

Note that _φ_ 0 = _∞_ always satisfies this equation. We shall see in the general theory that _φ_ 0 is the minimal non-negative solution. Let us look for a finite solution: then 

**==> picture [101 x 13] intentionally omitted <==**

so 

**==> picture [87 x 23] intentionally omitted <==**

The quadratic _c_[2] _p − c_ + _q_ has roots at _q/p_ and 1, and takes negative values in between. Hence the expected total cost is given by 

**==> picture [184 x 29] intentionally omitted <==**

_4. Further theory_ 

138 

It was clear at the outset that _φ_ 0 = _∞_ when _c ≥_ 1. It is interesting that _φ_ 0 = _∞_ also when _c_ is too small: in this case the costs rapidly become large to the left of 0, and although the walk eventually drifts away to the right, the expected cost incurred to the left of 0 is infinite. 

In the examples just discussed we were able to calculate potentials by writing down and solving a system of linear equations. This situation is familiar from hitting probabilities and expected hitting times. Indeed, these are simple examples of potentials for Markov chains. As the examples show, one does not really need a general theory to write down the linear equations. Nevertheless, we are now going to give some general results on potentials. These will help to reveal the scope of the ideas used in the examples, and will reveal also what happens when the linear equations do not have a unique solution. We shall discuss the cases of discrete and continuous time side-by-side. Throughout, we shall write ( _Xn_ ) _n≥_ 0 for a discrete-time chain with transition matrix _P_ , and ( _Xt_ ) _t≥_ 0 for a continuous-time chain with generator matrix _Q_ . As usual, we insist that ( _Xt_ ) _t≥_ 0 be minimal. 

Let us partition the state-space _I_ into two disjoint sets _D_ and _∂D_ ; we call _∂D_ the _boundary_ . We suppose that functions ( _ci_ : _i ∈ D_ ) and ( _fi_ : _i ∈ ∂D_ ) are given. We shall consider the associated _potential_ , defined by 

**==> picture [177 x 33] intentionally omitted <==**

in discrete time, and in continuous time 

**==> picture [189 x 33] intentionally omitted <==**

where _T_ denotes the hitting time of _∂D_ . To be sure that the sums and integrals here are well defined, we shall assume for the most part that _c_ and _f_ are _non-negative_ , that is, _ci ≥_ 0 for all _i ∈ D_ and _fi ≥_ 0 for all _i ∈ ∂D_ . More generally, _φ_ is the difference of the potentials associated with the positive and negative parts of _c_ and _f_ , so this assumption is not too restrictive. In the explosive case we always set _c_ ( _∞_ ) = 0, so no further costs are incurred after explosion. 

The most obvious interpretation of these potentials is in terms of cost: the chain wanders around in _D_ until it hits the boundary: whilst in _D_ , at state _i_ say, it incurs a _cost ci_ per unit time; when and if it hits the boundary, at _j_ say, a _final cost fj_ is incurred. Note that we do not assume the chain will hit the boundary, or even that the boundary is non-empty. 

_4.2 Potential theory_ 

139 

**Theorem 4.2.3.** _Suppose that_ ( _ci_ : _i ∈ D_ ) _and_ ( _fi_ : _i ∈ ∂D_ ) _are nonnegative. Set_ 

**==> picture [177 x 34] intentionally omitted <==**

_where T denotes the hitting time of ∂D. Then_ 

- (i) _the potential φ_ = ( _φi_ : _i ∈ I_ ) _satisfies_ 

**==> picture [222 x 27] intentionally omitted <==**

- (ii) _if ψ_ = ( _ψi_ : _i ∈ I_ ) _satisfies_ 

**==> picture [222 x 28] intentionally omitted <==**

_and ψi ≥_ 0 _for all i, then ψi ≥ φi for all i;_ 

- (iii) _if_ P _i_ ( _T < ∞_ ) = 1 _for all i, then_ (4.1) _has at most one bounded solution._ 

_Proof._ (i) Obviously, _φ_ = _f_ on _∂D_ . For _i ∈ D_ by the Markov property 

**==> picture [203 x 78] intentionally omitted <==**

so we have 

**==> picture [276 x 72] intentionally omitted <==**

as required. 

- (ii) Consider the expected cost up to time _n_ : 

**==> picture [214 x 34] intentionally omitted <==**

_4. Further theory_ 

140 

By monotone convergence, _φi_ ( _n_ ) _↑ φi_ as _n →∞_ . Also, by the argument used in part (i), we find 

**==> picture [159 x 28] intentionally omitted <==**

Suppose that _ψ_ satisfies (4.2) and _ψ ≥_ 0 = _φ_ (0). Then _ψ ≥ Pψ_ + _c ≥ Pφ_ (0) + _c_ = _φ_ (1) in _D_ and _ψ ≥ f_ = _φ_ (1) in _∂D_ , so _ψ ≥ φ_ (1). Similarly and by induction, _ψ ≥ φ_ ( _n_ ) for all _n_ , and hence _ψ ≥ φ_ . (iii) We shall show that if _ψ_ satisfies (4.2) then 

**==> picture [164 x 14] intentionally omitted <==**

with equality if equality holds in (4.2). This is another proof of (ii). But also, in the case of equality, if _|ψi| ≤ M_ and P _i_ ( _T < ∞_ ) = 1 for all _i_ , then as _n →∞_ 

**==> picture [181 x 14] intentionally omitted <==**

so _ψ_ = lim _n→∞ φ_ ( _n_ ) = _φ_ , proving (iii). 

For _i ∈ D_ we have 

**==> picture [152 x 26] intentionally omitted <==**

and, by repeated substitution for _ψ_ on the right 

**==> picture [282 x 188] intentionally omitted <==**

as required, with equality when equality holds in (4.2). 

_4.2 Potential theory_ 

141 

It is illuminating to think of the calculation we have just done in terms of martingales. Consider 

**==> picture [244 x 33] intentionally omitted <==**

Then 

**==> picture [250 x 66] intentionally omitted <==**

with equality if equality holds in (4.2). We note that _Mn_ is not necessarily integrable. Nevertheless, it still follows that 

**==> picture [261 x 14] intentionally omitted <==**

with equality if equality holds in (4.2). 

For continuous-time chains there is a result analogous to Theorem 4.2.3. We have to state it slightly differently because when _φ_ takes infinite values the equations (4.3) may involve subtraction of infinities, and therefore not make sense. Although the conclusion then appears to depend on the finiteness of _φ_ , which is _a priori_ unknown, we can still use the result to determine _φi_ in all cases. To do this we restrict our attention to the set of states _J_ accessible from _i_ . If the linear equations have a finite non-negative solution on _J_ , then ( _φj_ : _j ∈ J_ ) is the minimal such solution. If not, then _φj_ = _∞_ for some _j ∈ J_ , which forces _φi_ = _∞_ , since _i_ leads to _j_ . 

**Theorem 4.2.4.** _Assume that_ ( _Xt_ ) _t≥_ 0 _is minimal, and that_ ( _ci_ : _i ∈ D_ ) _and_ ( _fi_ : _i ∈ ∂D_ ) _are non-negative. Set_ 

**==> picture [184 x 34] intentionally omitted <==**

_where T is the hitting time of ∂D. Then φ_ = ( _φi_ : _i ∈ I_ ) _, if finite, is the minimal non-negative solution to_ 

**==> picture [230 x 27] intentionally omitted <==**

142 _4. Further theory_ 

_If φi_ = _∞ for some i, then_ (4.3) _has no finite non-negative solution. Moreover, if_ P _i_ ( _T < ∞_ ) = 1 _for all i, then_ (4.3) _has at most one bounded solution._ 

_Proof._ Denote by ( _Yn_ ) _n≥_ 0 and _S_ 1 _, S_ 2 _, . . ._ the jump chain and holding times of ( _Xt_ ) _t≥_ 0, and by Π the jump matrix. Then 

**==> picture [286 x 32] intentionally omitted <==**

where _N_ is the first time ( _Yn_ ) _n≥_ 0 hits _∂D_ , and where we use the convention 0 _× ∞_ = 0 on the right. We have 

**==> picture [237 x 29] intentionally omitted <==**

so, by Fubini’s theorem 

**==> picture [173 x 27] intentionally omitted <==**

By Theorem 4.2.3, _φ_ is therefore the minimal non-negative solution to 

**==> picture [235 x 27] intentionally omitted <==**

which equations have at most one bounded solution if P _i_ ( _N < ∞_ ) = 1 for all _i_ . Since the finite solutions of (4.4) are exactly the finite solutions of (4.3), and since _N_ is finite whenever _T_ is finite, this proves the result. 

It is natural in some economic applications to apply to future costs a discount factor _α ∈_ (0 _,_ 1) or rate _λ ∈_ (0 _, ∞_ ), corresponding to an interest rate. _Potentials with discounted costs_ may also be calculated by linear equations; indeed the discounting actually makes the analysis easier. 

**Theorem 4.2.5.** _Suppose that_ ( _ci_ : _i ∈ I_ ) _is bounded. Set_ 

**==> picture [98 x 31] intentionally omitted <==**

_then φ_ = ( _φi_ : _i ∈ I_ ) _is the unique bounded solution to_ 

**==> picture [66 x 10] intentionally omitted <==**

_4.2 Potential theory_ 

143 

_Proof._ Suppose that _|ci| ≤ C_ for all _i_ , then 

**==> picture [136 x 31] intentionally omitted <==**

so _φ_ is bounded. By the Markov property 

**==> picture [253 x 34] intentionally omitted <==**

Then 

**==> picture [222 x 101] intentionally omitted <==**

so 

**==> picture [66 x 11] intentionally omitted <==**

On the other hand, suppose that _ψ_ is bounded and also that _ψ_ = _c_ + _αPψ_ . Set _M_ = sup _i |ψi − φi|_ , then _M < ∞_ . But 

**==> picture [94 x 12] intentionally omitted <==**

so 

**==> picture [174 x 26] intentionally omitted <==**

Hence _M ≤ αM_ , which forces _M_ = 0 and _ψ_ = _φ_ . 

We have a similar looking result for continuous time, which however lies a little deeper, because it really corresponds to a version of the discrete-time result where the discount factor may depend on the current state. 

**Theorem 4.2.6.** _Assume that_ ( _Xt_ ) _t≥_ 0 _is non-explosive. Suppose that_ ( _ci_ : _i ∈ I_ ) _is bounded. Set_ 

**==> picture [121 x 27] intentionally omitted <==**

_then φ_ = ( _φi_ : _i ∈ I_ ) _is the unique bounded solution to_ 

**==> picture [212 x 12] intentionally omitted <==**

_4. Further theory_ 

144 

_Proof._ Assume for now that _c_ is non-negative. Introduce a new state _∂_ with _c∂_ = 0. Let _T_ be an independent _E_ ( _λ_ ) random variable and define 

**==> picture [111 x 27] intentionally omitted <==**

Then ( _X_[�] _t_ ) _t≥_ 0 is a Markov chain on _I ∪{∂}_ with modified transition rates 

**==> picture [153 x 11] intentionally omitted <==**

Also _T_ is the hitting time of _∂_ , and is finite with probability 1. By Fubini’s theorem 

**==> picture [97 x 28] intentionally omitted <==**

Suppose _ci ≤ C_ for all _i_ , then 

**==> picture [129 x 27] intentionally omitted <==**

so _φ_ is bounded. Hence, by Theorem 4.2.4, _φ_ is the unique bounded solution to 

**==> picture [47 x 14] intentionally omitted <==**

which is the same as (4.5). 

When _c_ takes negative values we can apply the preceding argument to the potentials 

**==> picture [129 x 27] intentionally omitted <==**

where _c[±] i_[= (] _[±][c]_[)] _[ ∨]_[0.][Then] _[φ]_[ =] _[ φ]_[+] _[ −][φ][−]_[so] _[φ]_[is][bounded.][We][have] 

**==> picture [78 x 14] intentionally omitted <==**

so, subtracting 

**==> picture [67 x 12] intentionally omitted <==**

Finally, if _ψ_ is bounded and ( _λ−Q_ ) _ψ_ = _c_ , then ( _λ−Q_ )( _ψ −φ_ ) = 0, so _ψ −φ_ is the unique bounded solution for the case when _c_ = 0, which is 0. 

The point of view underlying the last four theorems was that we were interested in a given potential associated to a Markov chain, and wished to calculate it. We shall now take a brief look at some structural aspects of the set of all potentials of a given Markov chain. What we describe is just the simplest case of a structure of great generality. First we shall look at the Green matrix, and then at the role of the boundary. 

_4.2 Potential theory_ 

145 

Let us consider potentials with non-negative costs _c_ , and without boundary. The potential is defined by 

**==> picture [85 x 31] intentionally omitted <==**

in discrete time, and in continuous time 

**==> picture [100 x 26] intentionally omitted <==**

By Fubini’s theorem we have 

**==> picture [186 x 31] intentionally omitted <==**

where _G_ = ( _gij_ : _i, j ∈ I_ ) is the _Green_ matrix 

**==> picture [60 x 31] intentionally omitted <==**

Similarly, in continuous time _φ_ = _Gc_ , with 

**==> picture [80 x 27] intentionally omitted <==**

Thus, once we know the Green matrix, we have explicit expressions for all potentials of the Markov chain. The Green matrix is also called the _fundamental solution_ of the linear equations (4.1) and (4.3). The _j_ th column ( _gij_ : _i ∈ I_ ) is itself a potential. We have 

**==> picture [88 x 31] intentionally omitted <==**

in discrete time, and in continuous time 

**==> picture [104 x 27] intentionally omitted <==**

Thus _gij_ is the expected total time in _j_ starting from _i_ . These quantities have already appeared in our discussions of transience and recurrence in Sections 1.5 and 2.11: we know that _gij_ = _∞_ if and only if _i_ leads to _j_ and _j_ is recurrent. Indeed, in discrete time 

**==> picture [82 x 14] intentionally omitted <==**

146 

**==> picture [84 x 11] intentionally omitted <==**

where _h[j] i_[is][the][probability][of][hitting] _[j]_[from] _[i]_[,][and] _[f][j]_[is][the][return][proba-] bility for _j_ . The formula for continuous time is 

**==> picture [95 x 14] intentionally omitted <==**

For potentials with discounted costs the situation is similar: in discrete time 

**==> picture [229 x 31] intentionally omitted <==**

where 

**==> picture [79 x 31] intentionally omitted <==**

and in continuous time 

**==> picture [268 x 26] intentionally omitted <==**

where 

**==> picture [107 x 27] intentionally omitted <==**

We call � _Rα_ : _α ∈_ (0 _,_ 1)� and � _Rλ_ : _λ ∈_ (0 _, ∞_ )� the _resolvent_ of the Markov chain. Unlike the Green matrix the resolvent is always finite. Indeed, for finite state-space we have 

**==> picture [84 x 13] intentionally omitted <==**

and 

**==> picture [87 x 13] intentionally omitted <==**

We return to the general case, with boundary _∂D_ . Any bounded function ( _φi_ : _i ∈ I_ ) for which 

**==> picture [81 x 11] intentionally omitted <==**

is called _harmonic_ in _D_ . Our object now is to examine the relation between non-negative functions, harmonic in _D_ , and the boundary _∂D_ . Here are two examples. 

_4.2 Potential theory_ 

147 

**==> picture [144 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>**----- End of picture text -----**<br>


## **Example 4.2.7** 

Consider the random walk ( _Xn_ ) _n≥_ 0 on the above graph, where each allowable transition is made with equal probability. States _a_ and _b_ are absorbing. We set _∂D_ = _{a, b}_ . Let _h[a] i_[denote the absorption probability for] _[ a]_[, starting] from _i_ . By the method of Section 1.3 we find 

**==> picture [132 x 40] intentionally omitted <==**

where we have written the vector _h[a]_ as a matrix, corresponding in an obvious way to the state-space. The linear equations for the vector _h[a]_ read 

**==> picture [121 x 28] intentionally omitted <==**

Thus we can find two non-negative functions _h[a]_ and _h[b]_ , harmonic in _D_ , but with different boundary values. In fact, the most general non-negative harmonic function _φ_ in _D_ satisfies 

**==> picture [89 x 27] intentionally omitted <==**

where _fa, fb ≥_ 0, and this implies 

**==> picture [81 x 13] intentionally omitted <==**

Thus the boundary points _a_ and _b_ give us extremal generators _h[a]_ and _h[b]_ of the set of all non-negative harmonic functions. 

_4. Further theory_ 

148 

## **Example 4.2.8** 

Consider the random walk ( _Xn_ ) _n≥_ 0 on Z which jumps towards 0 with probability _q_ and jumps away from 0 with probability _p_ = 1 _− q_ , except that at 0 it jumps to _−_ 1 or 1 with probability 1 _/_ 2. We choose _p > q_ so that the walk is transient. In fact, starting from 0, we can show that ( _Xn_ ) _n≥_ 0 is equally likely to end up drifting to the left or to the right, at speed _p − q_ . Let us consider the problem of determining for ( _Xn_ ) _n≥_ 0 the set _C_ of all non-negative harmonic functions _φ_ . We must have 

**==> picture [210 x 47] intentionally omitted <==**

The first equation has general solution 

**==> picture [210 x 14] intentionally omitted <==**

which is non-negative provided _A_ + _B ≥_ 0. Similarly, the third equation has general solution 

**==> picture [240 x 15] intentionally omitted <==**

non-negative provided _A[′]_ + _B[′] ≥_ 0. To obtain a general harmonic function we must match the values _φ_ 0 and satisfy _φ_ 0 = ( _φ_ 1 + _φ−_ 1) _/_ 2. This forces _A_ = _A[′]_ and _B_ + _B[′]_ = 0. It follows that all non-negative harmonic functions have the form 

**==> picture [90 x 13] intentionally omitted <==**

**==> picture [209 x 14] intentionally omitted <==**

**==> picture [236 x 32] intentionally omitted <==**

In the preceding example the generators of _C_ were in one-to-one correspondence with the points of the boundary – the possible places for the chain to end up. In this example there is no boundary, _but the generators of C still correspond to the two possibilities for the long-time behaviour of the chain_ . For we have 

**==> picture [146 x 13] intentionally omitted <==**

The suggestion of this example, which is fully developed in other works, is that the set of non-negative harmonic functions may be used to identify a 

_4.2 Potential theory_ 

149 

generalized notion of boundary for Markov chains, which sometimes just consists of points in the state-space, but more generally corresponds to the varieties of possible limiting behaviour for _Xn_ as _n →∞_ . See, for example, _Markov Chains_ by D. Revuz (North-Holland, Amsterdam, 1984). 

We cannot begin to give the general theory corresponding to Example 4.2.8, but we can draw some general conclusions from Theorem 4.2.3 when the situation is more like Example 4.2.7. Suppose we have a Markov chain ( _Xn_ ) _n≥_ 0 with absorbing boundary _∂D_ . Set 

**==> picture [80 x 14] intentionally omitted <==**

where _T_ is the hitting time of _∂D_ . Then by the methods of Section 1.3 we have 

**==> picture [232 x 29] intentionally omitted <==**

Note that _h[∂] i_[= 1 for all] _[ i]_[ always gives a possible solution.][Hence if][ (4.6)][ has] a unique bounded solution then _h[∂] i_[=][ P] _[i]_[(] _[T][<][ ∞]_[) = 1][for][all] _[i]_[.][Conversely,] if P _i_ ( _T < ∞_ ) = 1 for all _i_ , then, as we showed in Theorem 4.2.3, (4.6) has a unique bounded solution. Indeed, we showed more generally that this condition implies that 

**==> picture [107 x 28] intentionally omitted <==**

has at most one bounded solution, and since 

**==> picture [267 x 34] intentionally omitted <==**

is the minimal solution, any bounded solution is given by (4.7). Suppose from now on that P _i_ ( _T < ∞_ ) = 1 for all _i_ . Let _φ_ be a bounded non-negative function, harmonic in _D_ , with boundary values _φi_ = _fi_ for _i ∈ ∂D_ . Then, by monotone convergence 

**==> picture [184 x 26] intentionally omitted <==**

Hence every bounded harmonic function is determined by its boundary values and, indeed 

**==> picture [70 x 26] intentionally omitted <==**

where 

**==> picture [84 x 14] intentionally omitted <==**

_4. Further theory_ 

150 

Just as in Example 4.2.7, the hitting probabilities for boundary states form a set of extremal generators for the set of all bounded non-negative harmonic functions. 

## **Exercises** 

**4.2.1** Consider a discrete-time Markov chain ( _Xn_ ) _n≥_ 0 and the potential _φ_ with costs ( _ci_ : _i ∈ D_ ) and boundary values ( _fi_ : _i ∈ ∂D_ ). Set 

**==> picture [111 x 27] intentionally omitted <==**

where _T_ is the hitting time of _∂D_ and _∂_ is a new state. Show that ( _X_[�] _n_ ) _n≥_ 0 is a Markov chain and determine its transition matrix. 

Check that 

**==> picture [162 x 35] intentionally omitted <==**

where _T_[�] = _T_ + 1 and where we set _ci_ = _fi_ on _∂D_ and _c∂_ = 0. This shows that a general potential may always be considered as a potential with boundary value zero or, indeed, without boundary at all. 

Can you find a similar reduction for continuous-time chains? 

**4.2.2** Prove the fact claimed in Example 4.2.8 that 

**==> picture [146 x 14] intentionally omitted <==**

**4.2.3** Let ( _ci_ : _i ∈ I_ ) be a non-negative function. Partition I as _D ∪ ∂D_ and suppose that the linear equations 

**==> picture [107 x 27] intentionally omitted <==**

have a unique bounded solution. Show that the Markov chain ( _Xn_ ) _n≥_ 0 with transition matrix _P_ is certain to hit _∂D_ . 

Consider now a new partition _D_[�] _∪ ∂D_[�] , where _D_[�] _⊆ D_ . Show that the linear equations 

**==> picture [109 x 34] intentionally omitted <==**

also have a unique bounded solution, and that 

**==> picture [116 x 11] intentionally omitted <==**

_4.3 Electrical networks_ 

151 

## **4.3 Electrical networks** 

An electrical network has a countable set _I_ of _nodes_ , each node _i_ having a _capacity πi >_ 0. Some nodes are joined by _wires_ , the wire between _i_ and _j_ having _conductivity aij_ = _aji ≥_ 0. Where no wire joins _i_ to _j_ we take _aij_ = 0. In practice, each ‘wire’ contains a resistor, which determines the conductivity as the reciprocal of its resistance. Each node _i_ holds a certain _charge χi_ , which determines its _potential φi_ by 

**==> picture [49 x 11] intentionally omitted <==**

A _current_ or _flow of charge_ is any matrix ( _γij_ : _i, j ∈ I_ ) with _γij_ = _−γji_ . Physically it is found that the current _γij_ from _i_ to _j_ obeys _Ohm’s law:_ 

**==> picture [89 x 13] intentionally omitted <==**

Thus charge flows from nodes of high potential to nodes of low potential. 

The first problem in electrical networks is to determine equilibrium flows and potentials, subject to given external conditions. The nodes are partitioned into two sets _D_ and _∂D_ . External connections are made at the nodes in _∂D_ and possibly at some of the nodes in _D_ . These have the effect that each node _i ∈ ∂D_ is held at a given potential _fi_ , and that a given current _gi_ enters the network at each node _i ∈ D_ . The case where _gi_ = 0 corresponds to a node with no external connection. In equilibrium, current may also enter or leave the network through _∂D_ , but here it is not the current but the potential which is determined externally. 

Given a flow ( _γij_ : _i, j ∈ I_ ) we shall write _γi_ for the _total flow from i to the network_ : 

**==> picture [59 x 26] intentionally omitted <==**

In equilibrium the charge at each node is constant, so 

**==> picture [102 x 11] intentionally omitted <==**

Therefore, by Ohm’s law, any equilibrium potential _φ_ = ( _φi_ : _i ∈ I_ ) must satisfy 

**==> picture [275 x 28] intentionally omitted <==**

There is a simple correspondence between electrical networks and reversible Markov chains in continuous-time, given by 

**==> picture [117 x 12] intentionally omitted <==**

_4. Further theory_ 

152 

_We shall assume that the total conductivity at each node is finite_ : 

**==> picture [85 x 26] intentionally omitted <==**

Then _ai_ = _πiqi_ = _−πiqii_ . The capacities _πi_ are the components of an invariant measure, and the symmetry of _aij_ corresponds to the detailed balance equations. The equations for an equilibrium potential may now be written in a form familiar from the preceding section: 

**==> picture [230 x 27] intentionally omitted <==**

where _ci_ = _gi/πi_ . It is natural that _c_ appears here and not _g_ , because _ct_ and _f_ have the same physical dimensions. We know that these equations may fail to have a unique solution, indicating the interesting possibility that there may be more than one equilibrium potential. However, to keep matters simple here, _we shall assume that I is finite, that the network is connected, and that ∂D is non-empty_ . This is enough to ensure uniqueness of potentials. Then, by Theorem 4.2.4, the equilibrium potential is given by 

**==> picture [257 x 34] intentionally omitted <==**

where _T_ is the hitting time of _∂D_ . 

In fact, the case where _∂D_ is empty may be dealt with as follows: we must have 

**==> picture [48 x 25] intentionally omitted <==**

or there is no possibility of equilibrium; pick one node _k_ , set _∂D_ = _{k}_ , and replace the condition _γk_ = _gk_ by _φi_ = 0. The new problem is equivalent to the old, but now _∂D_ is non-empty. 

**==> picture [151 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>1 2<br>2 1 2<br>2 1<br>D E F<br>**----- End of picture text -----**<br>


_4.3 Electrical networks_ 

153 

## **Example 4.3.1** 

Determine the equilibrium current in the network shown on the preceding page when unit current enters at _A_ and leaves at _F_ . The conductivities are shown on the diagram. Let us set _φA_ = 1 and _φF_ = 0. This will result in some flow from _A_ to _F_ , which we can scale to get a unit flow. By symmetry, _φE_ = 1 _− φB_ and _φD_ = 1 _− φC_ . Then, by Ohm’s law, since the total current leaving _B_ and _C_ must vanish 

**==> picture [206 x 28] intentionally omitted <==**

Hence, _φB_ = 1 _/_ 2 and _φC_ = 1 _/_ 4, and the associated flow is given by _γAB_ = 1 _/_ 2 _, γBC_ = 1 _/_ 2 _, γCF_ = 1 _/_ 2 _, γBE_ = 0. In fact, we were lucky – no scaling was necessary. 

Note that the node capacities do not affect the problem we considered. Let us arbitrarily assign to each node a capacity 1. Then there is an associated Markov chain and, according to (4.10), the equilibrium potential is given by 

**==> picture [150 x 12] intentionally omitted <==**

where _T_ is the hitting time of _{A, F }_ . Different node capacities result in different Markov chains, but the same jump chain and hence the same hitting probabilities. 

Here is a general result expressing equilibrium potentials, flows and charges in terms of the associated Markov chain. 

**Theorem 4.3.2.** _Consider a finite network with external connections at two nodes A and B, and the associated Markov chain_ ( _Xt_ ) _t≥_ 0 _._ (a) _The unique equilibrium potential φ with φA_ = 1 _and φB_ = 0 _is given by_ 

**==> picture [87 x 12] intentionally omitted <==**

_where TA and TB are the hitting times of A and B._ 

(b) _The unique equilibrium flow γ with γA_ = 1 _and γB_ = _−_ 1 _is given by_ 

**==> picture [94 x 13] intentionally omitted <==**

_where_ Γ _ij is the number of times that_ ( _Xt_ ) _t≥_ 0 _jumps from i to j before hitting B._ 

- (c) _The charge χ associated with γ, subject to χB_ = 0 _, is given by_ 

**==> picture [116 x 29] intentionally omitted <==**

154 

**==> picture [84 x 11] intentionally omitted <==**

_Proof._ The formula for _φ_ is a special case of (4.10), where _c_ = 0 and _f_ = 1 _{A}_ . We shall prove (b) and (c) together. Observe that if _X_ 0 = _A_ then 

**==> picture [185 x 47] intentionally omitted <==**

so if _γij_ = E _A_ (Γ _ij −_ Γ _ji_ ) then _γ_ is a unit flow from _A_ to _B_ . We have 

**==> picture [144 x 31] intentionally omitted <==**

where _NB_ is the hitting time of _B_ for the jump chain ( _Yn_ ) _n≥_ 0. So, by the Markov property of the jump chain 

**==> picture [214 x 68] intentionally omitted <==**

Set 

**==> picture [113 x 28] intentionally omitted <==**

and consider the associated potential _ψi_ = _χi/πi_ . Then 

**==> picture [266 x 31] intentionally omitted <==**

so 

**==> picture [165 x 13] intentionally omitted <==**

Hence _ψ_ = _φ_ , _γ_ is the equilibrium unit flow and _χ_ the associated charge, as required. 

The interpretation of potential theory in terms of electrical networks makes it natural to consider notions of _energy_ . We define for a potential _φ_ = ( _φi_ : _i ∈ I_ ) and a flow _γ_ = ( _γij_ : _i, j ∈ I_ ) 

**==> picture [133 x 57] intentionally omitted <==**

_4.3 Electrical networks_ 

155 

The 1 _/_ 2 means that each wire is counted once. When _φ_ and _γ_ are related by Ohm’s law we have 

**==> picture [160 x 26] intentionally omitted <==**

and _E_ ( _φ_ ) is found physically to give the rate of dissipation of energy, as heat, by the network. Moreover, we shall see that certain equilibrium potentials and flows determined by Ohm’s law minimize these energy functions. This characteristic of energy minimization can indeed replace Ohm’s law as the fundamental physical principle. 

**Theorem 4.3.3.** _The equilibrium potential and flow may be determined as follows._ 

- (a) _The equilibrium potential φ_ = ( _φi_ : _i ∈ I_ ) _with boundary values φi_ = _fi for i ∈ ∂D and no current sources in D is the unique solution to_ 

**==> picture [159 x 29] intentionally omitted <==**

- (b) _The equilibrium flow γ_ = ( _γij_ : _i, j ∈ I_ ) _with current sources γi_ = _gi for i ∈ D and boundary potential zero is the unique solution to_ 

**==> picture [152 x 29] intentionally omitted <==**

_Proof._ For any potential _φ_ = ( _φi_ : _i ∈ I_ ) and any flow _γ_ = ( _γij_ : _i, j ∈ I_ ) we have 

**==> picture [140 x 26] intentionally omitted <==**

(a) Denote by _φ_ = ( _φi_ : _i ∈ I_ ) and by _γ_ = ( _γij_ : _i, j ∈ I_ ) the equilibrium potential and flow. We have _γi_ = 0 for _i ∈ D_ . We can write any potential in the minimization problem in the form _φ_ + _ε_ , where _ε_ = ( _εi_ : _i ∈ I_ ) with _εi_ = 0 for _i ∈ ∂D_ . Then 

**==> picture [285 x 26] intentionally omitted <==**

so 

**==> picture [156 x 12] intentionally omitted <==**

with equality only if _ε_ = 0. 

156 

**==> picture [84 x 11] intentionally omitted <==**

(b) Denote by _φ_ = ( _φi_ : _i ∈ I_ ) and by _γ_ = ( _γij_ : _i, j ∈ I_ ) the equilibrium potential and flow. We have _φi_ = 0 for _i ∈ ∂D_ . We can write any flow in the minimization problem in the form _γ_ + _δ_ , where _δ_ = ( _δij_ : _i, j ∈ I_ ) is a flow with _δi_ = 0 for _i ∈ D_ . Then 

**==> picture [238 x 26] intentionally omitted <==**

so 

**==> picture [142 x 12] intentionally omitted <==**

with equality only if _δ_ = 0. 

The following reformulation of part (a) of the preceding result states that harmonic functions minimize energy. 

**Corollary 4.3.4.** _Suppose that φ_ = ( _φi_ : _i ∈ I_ ) _satisfies_ 

**==> picture [91 x 27] intentionally omitted <==**

_Then φ is the unique solution to_ 

**==> picture [132 x 29] intentionally omitted <==**

An important feature of electrical networks is that networks with a small number of external connections look like networks with a small number of nodes altogether. In fact, given any network, there is always another network of wires joining the externally connected nodes alone, equivalent in its response to external flows and potentials. 

Let _J ⊆ I_ . We say that _a_ = ( _aij_ : _i, j ∈ J_ ) is an _effective conductivity_ on _J_ if, for all potentials _f_ = ( _fi_ : _i ∈ J_ ), the external currents into _J_ when _J_ is held at potential _f_ are the same for ( _J, a_ ) as for ( _I, a_ ). We know that _f_ determines an equilibrium potential _φ_ = ( _φi_ : _i ∈ I_ ) by 

**==> picture [175 x 28] intentionally omitted <==**

Then _a_ is an effective conductivity if, for all _f_ , for _i ∈ J_ we have 

**==> picture [165 x 26] intentionally omitted <==**

For a conductivity matrix _a_ on _J_ , for a potential _f_ = ( _fi_ : _i ∈ J_ ) and a flow _δ_ = ( _δij_ : _i, j ∈ J_ ) we set 

**==> picture [132 x 58] intentionally omitted <==**

_4.3 Electrical networks_ 

157 

**Theorem 4.3.5.** _There is a unique effective conductivity a given by_ 

**==> picture [100 x 26] intentionally omitted <==**

_where for each j ∈ J , φ[j]_ = ( _φ[j] i_[:] _[ i][ ∈][I]_[)] _[is][the][potential][defined][by]_ 

**==> picture [271 x 34] intentionally omitted <==**

_Moreover, a is characterized by the Dirichlet variational principle_ 

**==> picture [112 x 19] intentionally omitted <==**

_and also by the Thompson variational principle_ 

**==> picture [161 x 37] intentionally omitted <==**

_Proof._ Given _f_ = ( _fi_ : _i ∈ J_ ), define _φ_ = ( _φi_ : _i ∈ I_ ) by 

**==> picture [63 x 26] intentionally omitted <==**

then _φ_ is the equilibrium potential given by 

**==> picture [177 x 28] intentionally omitted <==**

and, by Corollary 4.3.4, _φ_ solves 

**==> picture [150 x 29] intentionally omitted <==**

We have, for _i ∈ J_ 

**==> picture [243 x 27] intentionally omitted <==**

In particular, taking _f ≡_ 1 we obtain 

**==> picture [81 x 26] intentionally omitted <==**

158 _4. Further theory_ 

Hence we have equality of external currents: 

**==> picture [162 x 26] intentionally omitted <==**

Moreover, we also have equality of energies: 

**==> picture [302 x 58] intentionally omitted <==**

Finally, if _gij_ = ( _fi − fj_ ) _aij_ and _γij_ = ( _φi − φj_ ) _aij_ , then 

**==> picture [220 x 58] intentionally omitted <==**

so, by Theorem 4.3.3, for any flow _δ_ = ( _δij_ : _i, j ∈ I_ ) with _δi_ = _gi_ for _i ∈ J_ and _δi_ = 0 for _i ∈/ J_ , we have 

**==> picture [124 x 26] intentionally omitted <==**

Effective conductivity is also related to the associated Markov chain ( _Xt_ ) _t≥_ 0 in an interesting way. Define the _time spent in J_ 

**==> picture [93 x 28] intentionally omitted <==**

and a time-changed process ( _Xt_ ) _t≥_ 0 by 

**==> picture [54 x 13] intentionally omitted <==**

where 

**==> picture [128 x 12] intentionally omitted <==**

We obtain ( _Xt_ ) _t≥_ 0 by observing ( _Xt_ ) _t≥_ 0 whilst in _J_ , and stopping the clock whilst ( _Xt_ ) _t≥_ 0 makes excursions outside _J_ . This is really a transformation of the jump chain. By applying the strong Markov property to the jump chain we find that ( _Xt_ ) _t≥_ 0 is itself a Markov chain, with jump matrix Π given by 

**==> picture [178 x 27] intentionally omitted <==**

_4.4 Brownian motion_ 

159 

where 

**==> picture [84 x 15] intentionally omitted <==**

and _T_ denotes the hitting time of _J_ . See Example 1.4.4. Hence ( _Xt_ ) _t≥_ 0 has _Q_ -matrix given by 

**==> picture [101 x 26] intentionally omitted <==**

Since _φ[j]_ = ( _φ[j] k_[:] _[ k][∈][I]_[)][is][the][unique][solution][to][(4.11),][this][shows][that] 

**==> picture [51 x 10] intentionally omitted <==**

so ( _X t_ ) _t≥_ 0 is the Markov chain on _J_ associated with the effective conductivity _a_ . 

There is much more that one can say, for example in tying up the nonequilibrium behaviour of Markov chains and electrical networks. Moreover, methods coming from one theory one provide insights into the other. For an entertaining and illuminating account of the subject, you should see _Random Walks and Electrical Networks_ by P. G. Doyle and J. L. Snell (Carus Mathematical Monographs 22, Mathematical Association of America, 1984). 

## **4.4 Brownian motion** 

Imagine a symmetric random walk in Euclidean space which takes infinitesimal jumps with infinite frequency and you will have some idea of Brownian motion. It is named after a botanist who observed such a motion when looking at pollen grains under a microscope. The mathematical object now called Brownian motion was actually discovered by Wiener, and is also called the Wiener process. 

A discrete approximation to Euclidean space R _[d]_ is provided by 

**==> picture [136 x 14] intentionally omitted <==**

where _c_ is a large positive number. The simple symmetric random walk ( _Xn_ ) _n≥_ 0 on Z _[d]_ is a Markov chain which is by now quite familiar. We shall show that the scaled-down and speeded-up process 

**==> picture [78 x 15] intentionally omitted <==**

is a good approximation to Brownian motion. This provides an elementary way of thinking about Brownian motion. Also, it makes it reasonable to 

_4. Further theory_ 

160 

suppose that some properties of the random walk carry over to Brownian motion. At the end of this section we state some results which confirm that this is true to a remarkable extent. 

Why is space rescaled by the square-root of the time-scaling? Well, if we hope that _Xt_[(] _[c]_[)] converges in some sense as _c →∞_ to a non-degenerate limit, we will at least want E[ _|Xt_[(] _[c]_[)] _|_[2] ] to converge to a non-degenerate limit. For _ct ∈_ Z[+] we have 

**==> picture [104 x 13] intentionally omitted <==**

so the square-root scaling gives 

**==> picture [104 x 15] intentionally omitted <==**

which is independent of _c_ . 

We begin by defining Brownian motion, and then show that this is not an empty definition; that is to say, Brownian motions exist. 

A real-valued random variable is said to have _Gaussian distribution with mean_ 0 _and variance t_ if it has density function 

**==> picture [153 x 14] intentionally omitted <==**

The fundamental role of Gaussian distributions in probability derives from the following result. 

**Theorem 4.4.1 (Central limit theorem).** _Let X_ 1 _, X_ 2 _, . . . be a sequence of independent and identically distributed real-valued random variables with mean_ 0 _and variance t ∈_ (0 _, ∞_ ) _. Then, for all bounded continuous functions f , as n →∞ we have_ 

**==> picture [225 x 26] intentionally omitted <==**

We shall take this result and a few other standard properties of the Gaussian distribution for granted in this section. There are many introductory texts on probability which give the full details. 

A real-valued process ( _Xt_ ) _t≥_ 0 is said to be continuous if 

**==> picture [184 x 14] intentionally omitted <==**

A continuous real-valued process ( _Bt_ ) _t≥_ 0 is called a _Brownian motion_ if _B_ 0 = 0 and for all 0 = _t_ 0 _< t_ 1 _< . . . < tn_ the increments 

**==> picture [131 x 11] intentionally omitted <==**

_4.4 Brownian motion_ 

161 

are independent Gaussian random variables of mean 0 and variance 

**==> picture [106 x 10] intentionally omitted <==**

The conditions made on ( _Bt_ ) _t≥_ 0 are enough to determine all the probabilities associated with the process. To put it properly, the law of Brownian motion, which is a measure on the set of continuous paths, is uniquely determined. However, it is not obvious that there is any such process. We need the following result. 

**Theorem 4.4.2 (Wiener’s theorem).** _Brownian motion exists._ 

_Proof._ For _N_ = 0 _,_ 1 _,_ 2 _, . . ._ , denote by _DN_ the set of integer multiples of 2 _[−][N]_ in [0 _, ∞_ ), and denote by _D_ the union of these sets. Let us say that ( _Bt_ : _t ∈ DN_ ) is a _Brownian motion indexed by DN_ if _B_ 0 = 0 and for all 0 = _t_ 0 _< t_ 1 _< . . . < tn_ in _DN_ the increments 

**==> picture [131 x 11] intentionally omitted <==**

are independent Gaussian random variables of mean 0 and variance 

**==> picture [106 x 10] intentionally omitted <==**

We suppose given, for each _t ∈ D_ , an independent Gaussian random variable _Yt_ of mean 0 and variance 1. For _t ∈ D_ 0 = Z[+] set 

**==> picture [113 x 10] intentionally omitted <==**

then ( _Bt_ : _t ∈ D_ 0) is a Brownian motion indexed by _D_ 0. We shall show how to extend this process successively to Brownian motions ( _Bt_ : _t ∈ DN_ ) indexed by _DN_ . Then ( _Bt_ : _t ∈ D_ ) is a Brownian motion indexed by _D_ . Next we shall show that ( _Bt_ : _t ∈ D_ ) extends continuously to _t ∈_ [0 _, ∞_ ), and finally check that the extension is a Brownian motion. 

Suppose we have constructed ( _Bt_ : _t ∈ DN −_ 1), a Brownian motion indexed by _DN −_ 1. For _t ∈ DN \DN −_ 1 set _r_ = _t −_ 2 _[−][N]_ and _s_ = _t_ + 2 _[−][N]_ so that _r, s ∈ DN −_ 1 and define 

**==> picture [111 x 33] intentionally omitted <==**

We obtain two new increments: 

**==> picture [137 x 32] intentionally omitted <==**

_4. Further theory_ 

162 

We compute 

**==> picture [297 x 34] intentionally omitted <==**

The two new increments, being Gaussian, are therefore independent and of the required variance. Moreover, being constructed from _Bs − Br_ and _Yt_ , they are certainly independent of increments over intervals disjoint from ( _r, s_ ). Hence ( _Bt_ : _t ∈ DN_ ) is a Brownian motion indexed by _DN_ , as required. Hence, by induction, we obtain a Brownian motion ( _Bt_ : _t ∈ D_ ). 

For each _N_ denote by ( _Bt_[(] _[N]_[)] ) _t≥_ 0 the continuous process obtained by linear interpolation from ( _Bt_ : _t ∈ DN_ ). Also, set _Zt_[(] _[N]_[)] = _Bt_[(] _[N]_[)] _− Bt_[(] _[N][−]_[1)] . For _t ∈ DN −_ 1 we have _Zt_[(] _[N]_[)] = 0. For _t ∈ DN \DN −_ 1, by our construction we have 

**==> picture [264 x 16] intentionally omitted <==**

with _Yt_ Gaussian of mean 0 and variance 1. Set 

**==> picture [94 x 24] intentionally omitted <==**

Then, since ( _Zt_[(] _[N]_[)] ) _t≥_ 0 interpolates linearly between its values on _DN_ , we obtain 

**==> picture [184 x 23] intentionally omitted <==**

There are 2 _[N][−]_[1] points in ( _DN \DN −_ 1) _∩_ [0 _,_ 1]. So for _λ >_ 0 we have 

**==> picture [200 x 14] intentionally omitted <==**

For a random variable _X ≥_ 0 and _p >_ 0 we have the formula 

**==> picture [279 x 27] intentionally omitted <==**

Hence 

**==> picture [316 x 57] intentionally omitted <==**

_4.4 Brownian motion_ 

163 

and hence, for any _p >_ 2 

**==> picture [313 x 109] intentionally omitted <==**

It follows that, with probability 1, as _N →∞_ 

converges uniformly in _t ∈_ [0 _,_ 1], and by a similar argument uniformly for _t_ in any bounded interval. Now _Bt_[(] _[N]_[)] eventually equals _Bt_ for any _t ∈ D_ and the uniform limit of continuous functions is continuous. Therefore, ( _Bt_ : _t ∈ D_ ) has a continuous extension ( _Bt_ ) _t≥_ 0, as claimed. 

It remains to show that the increments of ( _Bt_ ) _t≥_ 0 have the required joint distribution. But given 0 _< t_ 1 _< . . . < tn_ we can find sequences ( _t[m] k_[)] _[m][∈]_[N] in _D_ such that 0 _< t[m]_ 1 _[<][. . .][<][t][m] n_[for][all] _[m]_[and] _[t][m] k[→][t][k]_[for][all] _[k]_[.][Set] _t_ 0 = _t[m]_ 0[= 0.][We][know][that][the][increments] 

**==> picture [139 x 13] intentionally omitted <==**

are Gaussian of mean 0 and variance 

**==> picture [115 x 12] intentionally omitted <==**

Hence, using continuity of ( _Bt_ ) _t≥_ 0 we can let _m →∞_ to obtain the desired distribution for the increments 

**==> picture [135 x 11] intentionally omitted <==**

Having shown that Brownian motion exists, we now want to show how it appears as a universal scaling limit of random walks, very much as the Gaussian distribution does for sums of independent random variables. 

**Theorem 4.4.3.** _Let_ ( _Xn_ ) _n≥_ 0 _be a discrete-time real-valued random walk with steps of mean 0 and variance σ_[2] _∈_ (0 _, ∞_ ) _. For c >_ 0 _consider the rescaled process_ 

**==> picture [78 x 15] intentionally omitted <==**

_where the value of Xct when ct is not an integer is found by linear interpolation. Then, for all m, for all bounded continuous functions f_ : R _[m] →_ R _and all_ 0 _≤ t_ 1 _< . . . < tm, we have_ 

**==> picture [219 x 17] intentionally omitted <==**

_as c →∞, where_ ( _Bt_ ) _t≥_ 0 _is a Brownian motion._ 

_4. Further theory_ 

164 

_Proof._ The claim is that ( _Xt_[(] 1 _[c]_[)] _[, . . .][, X] t_[(] _m[c]_[)][)] converges weakly to ( _σBt_ 1 _, . . . , σBtm_ ) as _c →∞_ . In the proof we shall take for granted some basic properties of weak convergence. First define 

**==> picture [84 x 16] intentionally omitted <==**

where [ _ct_ ] denotes the integer part of _ct_ . Then 

**==> picture [326 x 16] intentionally omitted <==**

where _Yn_ denotes the _n_ th step of ( _Xn_ ) _n≥_ 0. The right side converges weakly to 0, so it suffices to prove the claim with _X_[�] _t_[(] _[c]_[)] replacing _Xt_[(] _[c]_[)] . Consider now the increments 

**==> picture [213 x 17] intentionally omitted <==**

� for _k_ = 1 _, . . . , m_ . Since _X_ 0[(] _[c]_[)] = _B_ 0 = 0 it suffices to show that ( _U_ 1[(] _[c]_[)] _[, . . .][, U] m_[(] _[c]_[)][)][converges weakly][to][(] _[Z]_ 1 _[, . . .][, Z] m_[).][Then since][both sets of] increments are independent, it suffices to show that _Uk_[(] _[c]_[)] converges weakly to _Zk_ for each _k_ . But 

**==> picture [351 x 36] intentionally omitted <==**

where _∼_ denotes identity of distribution and _Nk_ ( _c_ ) = [ _ctk_ ] _−_ [ _ctk−_ 1]. By the central limit theorem _Nk_ ( _c_ ) _[−]_[1] _[/]_[2] ( _Y_ 1 + _. . ._ + _YN_ ( _c_ )) converges weakly to ( _tk − tk−_ 1) _[−]_[1] _[/]_[2] _Zk_ , and � _c[−]_[1] _[/]_[2] _Nk_ ( _c_ )[1] _[/]_[2][�] _→_ ( _tk − tk−_ 1)[1] _[/]_[2] . Hence _Uk_[(] _[c]_[)] converges weakly to _Zk_ , as required. 

To summarize the last two results, we have shown, using special properties of the Gaussian distribution, that there is a continuous process ( _Bt_ ) _t≥_ 0 with stationary independent increments and such that _Bt_ is Gaussian of mean 0 and variance _t_ , for each _t ≥_ 0. That was Wiener’s theorem. Then, using the central limit theorem applied to the increments of a rescaled random walk, we established a sort of convergence to Brownian motion. There now follows a series of related remarks. 

Note the similarity to the definition of a _Poisson process_ as a rightcontinuous integer-valued process ( _Xt_ ) _t≥_ 0 starting from 0, having stationary independent increments and such that _Xt_ is Poisson of parameter _λt_ for each _t ≥_ 0. 

Given _d_ independent Brownian motions ( _Bt_[1][)] _[t][≥]_[0] _[, . . .][,]_[ (] _[B] t[d]_[)] _[t][≥]_[0][, let us con-] sider the R _[d]_ -valued process _Bt_ = ( _Bt_[1] _[, . . .][, B] t[d]_[).][We call (] _[B][t]_[)] _[t][≥]_[0][a] _[ Brownian]_ 

_4.4 Brownian motion_ 

165 

_motion in_ R _[d]_ . There is a multidimensional version of the central limit theorem which leads to a multidimensional version of Theorem 4.4.3, with no essential change in the proof. Thus if ( _Xn_ ) _n≥_ 0 is a random walk in R _[d]_ with steps of mean 0 and covariance matrix 

**==> picture [71 x 13] intentionally omitted <==**

and if _V_ is finite, then for all bounded continuous functions _f_ : (R _[d]_ ) _[m] →_ R, as _c →∞_ we have 

**==> picture [245 x 16] intentionally omitted <==**

Here are two examples. We might take ( _Xn_ ) _n≥_ 0 to be the simple symmetric random walk in Z[3] , then _V_ =[1] 3 _[I]_[.][Alternatively,][we][might][take][the][compo-] nents of ( _Xn_ ) _n≥_ 0 to be three independent simple symmetric random walks in Z, in which case _V_ = _I_ . Although these are different random walks, once the difference in variance is taken out, the result shows that in the scaling limit they behave asymptotically the same. More generally, given a random walk with a complicated step distribution, it is useful to know that on large scales all one needs to calculate is the variance (or covariance matrix). All other aspects of the step distribution become irrelevant as _c →∞_ . 

The scaling used in Theorem 4.4.3 suggests the following _scaling invariance property_ of Brownian motion ( _Bt_ ) _t≥_ 0, which is also easy to check from the definition. For any _c >_ 0 the process ( _Bt_[(] _[c]_[)][)] _[t][≥]_[0][defined][by] 

**==> picture [76 x 15] intentionally omitted <==**

is a Brownian motion. Thus Brownian motion appears as a fixed point of the scaling transformation, which attracts all other finite variance symmetric random walks as _c →∞_ . 

The sense in which we have shown that ( _Xt_[(] _[c]_[)] ) _t≥_ 0 converges to Brownian motion is very weak, and one can with effort prove stronger forms of convergence. However, what we have proved is strong enough to ensure that ( _Xt_[(] _[c]_[)] ) _t≥_ 0 does not converge, in the same sense, to anything else. 

The discussion to this point has not really been about the Markov property, but rather about processes with independent increments. To remedy this we must first define _Brownian motion starting from x_ : this is simply any process ( _Bt_ ) _t≥_ 0 such that _B_ 0 = _x_ and ( _Bt − B_ 0) _t≥_ 0 is a Brownian motion (starting from 0). As a limit of Markov chains it is natural to look in Brownian motion for the structure of a Markov process. By analogy with continuous-time Markov chains we look for a _transition semigroup_ ( _Pt_ ) _t≥_ 0 

_4. Further theory_ 

166 

and a _generator G_ . For any bounded measurable function _f_ : R _[d] →_ R we have 

**==> picture [324 x 55] intentionally omitted <==**

where 

**==> picture [193 x 14] intentionally omitted <==**

This is the _transition density_ for Brownian motion and the _transition semigroup_ is given by 

**==> picture [211 x 26] intentionally omitted <==**

To check the semigroup property _PsPt_ = _Ps_ + _t_ we note that 

**==> picture [201 x 32] intentionally omitted <==**

where we first took the expectation over the independent increment _Bs_ + _t − Bs_ . For _t >_ 0 it is easy to check that 

**==> picture [130 x 24] intentionally omitted <==**

where 

**==> picture [114 x 28] intentionally omitted <==**

Hence, if _f_ has two bounded derivatives, we have 

**==> picture [195 x 102] intentionally omitted <==**

as _t ↓_ 0. This suggests, by analogy with continuous-time chains, that the generator, a term we have not defined precisely, should be given by 

**==> picture [44 x 14] intentionally omitted <==**

_4.4 Brownian motion_ 

167 

Where formerly we considered vectors ( _fi_ : _i ∈ I_ ), now there are functions _f_ : R _[d] →_ R, required to have various degrees of local regularity, such as measurability and differentiability. Where formerly we considered matrices _Pt_ and _Q_ , now we have linear operators on functions: _Pt_ is an integral operator, _G_ is a differential operator. 

We would like to explain the appearance of the Laplacian ∆by reference to the random walk approximation. Denote by ( _Xn_ ) _n≥_ 0 the simple symmetric random walk in Z _[d]_ and consider for _N_ = 1 _,_ 2 _, . . ._ the rescaled process 

**==> picture [206 x 15] intentionally omitted <==**

For a bounded continuous function _f_ : R _[d] →_ R, set 

**==> picture [210 x 15] intentionally omitted <==**

The closest thing we have to a derivative in _t_ at 0 for ( _Pt_[(] _[N]_[)] ) _t_ =0 _,_ 1 _/N,_ 2 _/N,..._ is 

**==> picture [326 x 54] intentionally omitted <==**

If we assume that _f_ has two bounded derivatives then, by Taylor’s theorem, as _N →∞_ , 

**==> picture [302 x 15] intentionally omitted <==**

so 

**==> picture [142 x 18] intentionally omitted <==**

We finish by stating some results about Brownian motion which emphasise how much of the structure of Markov chains carries over. You will notice some weasel words creeping in, such as measurable, continuous and differentiable. These are various sorts of local regularity for functions defined on the state-space R _[d]_ . They did not appear for Markov chains because a discrete state-space has no local structure. You might correctly guess that the proofs would require additional real analysis, relative to the corresponding results for chains, and a proper measure-theoretic basis for the probability. But, this aside, the main ideas are very similar. For further details see, for example, _Probability Theory – an analytic view_ by D. W. Stroock (Cambridge University Press, 1993), or _Diffusions, Markov Processes and Martingales, Volume 1: Foundations_ by L. C. G. Rogers and David Williams (Wiley, Chichester, 2nd edition 1994). 

First, here is a result on recurrence and transience. 

_4. Further theory_ 

168 

**Theorem 4.4.4.** _Let_ ( _Bt_ ) _t≥_ 0 _be a Brownian motion in_ R _[d] ._ 

**==> picture [83 x 12] intentionally omitted <==**

**==> picture [183 x 12] intentionally omitted <==**

**==> picture [86 x 12] intentionally omitted <==**

**==> picture [141 x 12] intentionally omitted <==**

**==> picture [261 x 31] intentionally omitted <==**

**==> picture [89 x 12] intentionally omitted <==**

**==> picture [153 x 12] intentionally omitted <==**

It is natural to compare this result with the facts proved in Section 1.6, that in Z and Z[2] the simple symmetric random walk is recurrent, whereas in Z[3] it is transient. The results correspond exactly in dimensions one and three. In dimension two we see the fact that for continuous state-space it makes a difference to demand returns to a point or to arbitrarily small neighbourhoods of a point. If we accept this latter notion of recurrence the correspondence extends to dimension two. 

The invariant measure for Brownian motion is Lebesgue measure _dx_ . This has infinite total mass so in dimensions one and two Brownian motion is only null recurrent. So that we can state some results for the positive recurrent case, we shall consider Brownian motion in R _[d]_ projected onto the torus _T[d]_ = R _[d] /_ Z _[d]_ . In dimension one this just means wrapping the line round a circle of circumference 1. The invariant measure remains Lebesgue measure but this now has total mass 1. So the projected process is positive recurrent and we can expect convergence to equilibrium and ergodic results corresponding to Theorems 1.8.3 and 1.10.2. 

**Theorem 4.4.5.** _Let_ ( _Bt_ ) _t≥_ 0 _be a Brownian motion in_ R _[d] and let f_ : R _[d] →_ R _be a continuous periodic function, so that_ 

**==> picture [154 x 14] intentionally omitted <==**

_Then for all x ∈_ R _[d] , as t →∞, we have_ 

**==> picture [146 x 27] intentionally omitted <==**

_and, moreover_ 

**==> picture [191 x 29] intentionally omitted <==**

The generator[1] 2[∆of][Brownian][motion][in][R] _[d]_[reappears][as][it][should][in] the following martingale characterization of Brownian motion. 

_4.4 Brownian motion_ 

169 

**Theorem 4.4.6.** _Let_ ( _Xt_ ) _t≥_ 0 _be a continuous_ R _[d] -valued random process. Write_ ( _Ft_ ) _t≥_ 0 _for the filtration of_ ( _Xt_ ) _t≥_ 0 _. Then the following are equivalent:_ 

- (i) ( _Xt_ ) _t≥_ 0 _is a Brownian motion;_ 

- (ii) _for all bounded functions f which are twice differentiable with bounded second derivative, the following process is a martingale:_ 

**==> picture [195 x 28] intentionally omitted <==**

This result obviously corresponds to Theorem 4.1.2. In case you are unsure, a continuous time process ( _Mt_ ) _t≥_ 0 is a martingale if it is adapted to the given filtration ( _Ft_ ) _t≥_ 0, if E _|Mt| < ∞_ for all _t_ , and 

**==> picture [99 x 12] intentionally omitted <==**

whenever _s ≤ t_ and _A ∈Fs_ . 

We end with a result on the potentials associated with Brownian motion, corresponding very closely to Theorem 4.2.3 for Markov chains. These potentials are identical to those appearing in Newton’s theory of gravity, as we remarked in Section 4.2. 

**Theorem 4.4.7.** _Let D be an open set in_ R _[d] with smooth boundary ∂D. Let c_ : _D →_ [0 _, ∞_ ) _be measurable and let f_ : _∂D →_ [0 _, ∞_ ) _be continuous. Set_ 

**==> picture [188 x 29] intentionally omitted <==**

_where T is the hitting time of ∂D. Then_ 

- (i) _φ if finite belongs to C_[2] ( _D_ ) _∩ C_ ( _D_ ) _and satisfies_ 

**==> picture [221 x 30] intentionally omitted <==**

- (ii) _if ψ ∈ C_[2] ( _D_ ) _∩ C_ ( _D_ ) _and satisfies_ 

**==> picture [105 x 30] intentionally omitted <==**

_and ψ ≥_ 0 _, then ψ ≥ φ;_ 

- (iii) _if φ_ ( _x_ ) = _∞ for some x, then_ (4.12) _has no finite solution;_ 

- (iv) _if_ P _x_ ( _T < ∞_ ) = 1 _for all x, then_ (4.12) _has at most one bounded solution in C_[2] ( _D_ ) _∩ C_ ( _D_ ) _._ 

**5** 

## Applications 

Applications of Markov chains arise in many different areas. Some have already appeared to illustrate the theory, from games of chance to the evolution of populations, from calculating the fair price for a random reward to calculating the probability that an absent-minded professor is caught without an umbrella. In a real-world problem involving random processes you should always look for Markov chains. They are often easy to spot. Once a Markov chain is identified, there is a qualitative theory which limits the sorts of behaviour that can occur – we know, for example, that every state is either recurrent or transient. There are also good computational methods – for hitting probabilities and expected rewards, and for long-run behaviour via invariant distributions. 

In this chapter we shall look at five areas of application in detail: biological models, queueing models, resource management models, Markov decision processes and Markov chain Monte Carlo. In each case our aim is to provide an introduction rather than a systematic account or survey of the field. References to books for further reading are given in each section. 

## **5.1 Markov chains in biology** 

Randomness is often an appropriate model for systems of high complexity, such as are often found in biology. We have already illustrated some aspects of the theory by simple models with a biological interpretation. See Example 1.1.5 (virus), Exercise 1.1.6 (octopus), Example 1.3.4 (birthand-death chain) and Exercise 2.5.1 (bacteria). We are now going to give 

_5.1 Markov chains in biology_ 

171 

some more examples where Markov chains have been used to model biological processes, in the study of population growth, epidemics and genetic inheritance. It should be recognised from the start that these models are simplified and somewhat stylized in order to make them mathematically tractable. Nevertheless, by providing quantitative understanding of various phenomena they can provide a useful contribution to science. 

## **Example 5.1.1 (Branching processes)** 

The original branching process was considered by Galton and Watson in the 1870s while seeking a quantitative explanation for the phenomenon of the disappearance of family names, even in a growing population. Under the assumption that each male in a given family had a probability _pk_ of having _k_ sons, they wished to determine the probability that after _n_ generations an individual had no male descendents. The solution to this problem is explained below. 

The basic branching process model has many applications to problems of population growth, and also to the study of chain reactions in chemistry and nuclear fission. Suppose at time _n_ = 0 there is one individual, who dies and is replaced at time _n_ = 1 by a random number of offspring _N_ . Suppose, next, that these offspring also die and are themselves replaced at time _n_ = 2, each independently, by a random number of further offspring, having the same distribution as _N_ , and so on. We can construct the process by taking for each _n ∈_ N a sequence of independent random variables ( _Nk[n]_[)] _[k][∈]_[N][,][each] with the same distribution as _N_ , by setting _X_ 0 = 1 and defining inductively, for _n ≥_ 1 

**==> picture [121 x 13] intentionally omitted <==**

Then _Xn_ gives the size of the population in the _n_ th generation. The process ( _Xn_ ) _n≥_ 0 is a Markov chain on _I_ = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ with absorbing state 0. The case where P( _N_ = 1) = 1 is trivial so we exclude it. We have 

**==> picture [168 x 13] intentionally omitted <==**

so if P( _N_ = 0) _>_ 0 then _i_ leads to 0, and every state _i ≥_ 1 is transient. If P( _N_ = 0) = 0 then P( _N ≥_ 2) _>_ 0, so for _i ≥_ 1, _i_ leads to _j_ for some _j > i_ , and _j_ does not lead to _i_ , hence _i_ is transient in any case. We deduce that with probability 1 either _Xn_ = 0 for some _n_ or _Xn →∞_ as _n →∞_ . 

Further information on ( _Xn_ ) _n≥_ 0 is obtained by exploiting the branching structure. Consider the probability generating function 

**==> picture [153 x 32] intentionally omitted <==**

_5. Applications_ 

172 

defined for 0 _≤ t ≤_ 1. Conditional on _Xn−_ 1 = _k_ we have 

**==> picture [102 x 12] intentionally omitted <==**

so 

**==> picture [211 x 14] intentionally omitted <==**

and so 

**==> picture [294 x 31] intentionally omitted <==**

Hence, by induction, we find that E( _t[X][n]_ ) = _φ_[(] _[n]_[)] ( _t_ ), where _φ_[(] _[n]_[)] is the _n_ -fold composition _φ ◦ . . . ◦ φ_ . In principle, this gives the entire distribution of _Xn_ , though _φ_[(] _[n]_[)] may be a rather complicated function. Some quantities are easily deduced: we have 

**==> picture [286 x 24] intentionally omitted <==**

where _µ_ = E( _N_ ); also 

**==> picture [99 x 14] intentionally omitted <==**

so, since 0 is absorbing, we have 

**==> picture [202 x 18] intentionally omitted <==**

Now _φ_ ( _t_ ) is a convex function with _φ_ (1) = 1. Let us set _r_ = inf _{t ∈_ [0 _,_ 1] : _φ_ ( _t_ ) = _t}_ , then _φ_ ( _r_ ) = _r_ by continuity. Since _φ_ is increasing and 0 _≤ r_ , we have _φ_ (0) _≤ r_ and, by induction, _φ_[(] _[n]_[)] (0) _≤ r_ for all _n_ , hence _q ≤ r_ . On the other hand 

**==> picture [213 x 18] intentionally omitted <==**

so also _q ≥ r_ . Hence _q_ = _r_ . If _φ[′]_ (1) _>_ 1 then we must have _q <_ 1, and if _φ[′]_ (1) _≤_ 1 then since either _φ[′′]_ = 0 or _φ[′′] >_ 0 everywhere in [0 _,_ 1) we must have _q_ = 1. We have shown that the population survives with positive probability if and only if _µ >_ 1, where _µ_ is the mean of the offspring distribution. 

There is a nice connection between branching processes and random walks. Suppose that in each generation we replace individuals by their offspring one at a time, so if _Xn_ = _k_ then it takes _k_ steps to obtain _Xn_ +1. 

_5.1 Markov chains in biology_ 

173 

The population size then performs a random walk ( _Ym_ ) _m≥_ 0 with step distribution _N −_ 1. Define stopping times _T_ 0 = 0 and, for _n ≥_ 0 

**==> picture [86 x 11] intentionally omitted <==**

Observe that _Xn_ = _YTn_ for all _n_ , and since ( _Ym_ ) _m≥_ 0 jumps down by at most 1 each time, ( _Xn_ ) _n≥_ 0 hits 0 if and only if ( _Ym_ ) _m≥_ 0 hits 0. Moreover we can use the strong Markov property and a variation of the argument of Example 1.4.3 to see that, if 

**==> picture [170 x 12] intentionally omitted <==**

then _qi_ = _q_ 1 _[i]_[for][all] _[i]_[and][so] 

**==> picture [198 x 31] intentionally omitted <==**

Now each non-negative solution of this equation provides a non-negative solution of the hitting probability equations, so we deduce that _q_ 1 is the smallest non-negative root of the equation _q_ = _φ_ ( _q_ ), in agreement with the generating function approach. 

The classic work in this area is _The Theory of Branching Processes_ by T. E. Harris (Dover, New York, 1989). 

## **Example 5.1.2 (Epidemics)** 

Many infectious diseases persist at a low intensity in a population for long periods. Occasionally a large number of cases arise together and form an epidemic. This behaviour is to some extent explained by the observation that the presence of a large number of infected individuals increases the risk to the rest of the population. The decline of an epidemic can also be explained by the eventual decline in the number of individuals susceptible to infection, as infectives either die or recover and are then resistant to further infection. However, these naive explanations leave unanswered many quantitative questions that are important in predicting the behaviour of epidemics. 

In an idealized population we might suppose that all pairs of individuals make contact randomly and independently at a common rate, whether infected or not. For an idealized disease we might suppose that on contact with an infective, individuals themselves become infective and remain so for an exponential random time, after which they either die or recover. These two possibilities have identical consequences for the progress of the epidemic. This idealized model is obviously unrealistic, but it is the simplest mathematical model to incorporate the basic features of an epidemic. 

_5. Applications_ 

174 

We denote the number of susceptibles by _St_ and the number of infectives by _It_ . In the idealized model, _Xt_ = ( _St, It_ ) performs a Markov chain on (Z[+] )[2] with transition rates 

**==> picture [182 x 12] intentionally omitted <==**

for some _λ, µ ∈_ (0 _, ∞_ ). Since _St_ + _It_ does not increase, we effectively have a finite state-space. The states ( _s,_ 0) for _s ∈_ Z[+] are all absorbing and all the other states are transient; indeed all the communicating classes are singletons. The epidemic must therefore eventually die out, and the absorption probabilities give the distribution of the number of susceptibles who escape infection. We can calculate these probabilities explicitly when _S_ 0 + _I_ 0 is small. 

Of greater concern is the behaviour of an epidemic in a large population, of size _N_ , say. Let us consider the proportions _s[N] t_[=] _[ S][t][/N]_[and] _[i][N] t_[=] _[ I][t][/N]_ and suppose that _λ_ = _ν/N_ , where _ν_ is independent of _N_ . Consider now a sequence of models as _N →∞_ and choose _s[N]_ 0 _[→][s]_[0][and] _[i][N]_ 0 _[→][i]_[0][.][It][can] be shown that as _N →∞_ the process ( _s[N] t[, i][N] t_[)][converges][to][the][solution] ( _st, it_ ) of the differential equations 

**==> picture [104 x 29] intentionally omitted <==**

starting from ( _s_ 0 _, i_ 0). Here convergence means that E[ _|_ ( _s[N] t[, i][N] t_[)] _[−]_[(] _[s][t][, i][t]_[)] _[|]_[]] _[ →]_ 0 for all _t ≥_ 0. We will not prove this result, but will give an example of another easier asymptotic calculation. 

Consider the case where _S_ 0 = _N −_ 1, _I_ 0 = 1, _λ_ = 1 _/N_ and _µ_ = 0. This has the following interpretation: a rumour is begun by a single individual who tells it to everyone she meets; they in turn pass the rumour on to everyone they meet. We assume that each individual meets another randomly at the jump times of a Poisson process of rate 1. How long does it take until everyone knows the rumour? If _i_ people know the rumour, then _N − i_ do not, and the rate at which the rumour is passed on is 

**==> picture [81 x 12] intentionally omitted <==**

The expected time until everyone knows the rumour is then 

**==> picture [317 x 32] intentionally omitted <==**

as _N →∞_ . This is not a limit as above but, rather, an asymptotic equivalence. The fact that the expected time grows with _N_ is related to the fact 

_5.1 Markov chains in biology_ 

175 

that we do not scale _I_ 0 with _N_ : when the rumour is known by very few or by almost all, the proportion of ‘infectives’ changes very slowly. 

The final two examples come from population genetics. They represent an attempt to understand quantitatively the consequences of randomness in genetic inheritance. The randomness here might derive from the choice of reproducing individual, in sexual reproduction the choice of partner, or the choice of parents’ alleles retained by their offspring. (The word _gene_ refers to a particular chromosomal locus; the varieties of genetic material that can be present at such a locus are known as _alleles_ .) This sort of study was motivated in the first place by a desire to find mathematical models of natural selection, and thereby to discriminate between various competing accounts of the process of evolution. More recently, as scientists have gained access to the genetic material itself, many more questions of a statistical nature have arisen. We emphasise that we present only the very simplest examples in a rich theory, for which we refer the interested reader to _Mathematical Population Genetics_ by W. J. Ewens (Springer, Berlin, 1979). 

## **Example 5.1.3 (Wright–Fisher model)** 

This is the discrete-time Markov chain on _{_ 0 _,_ 1 _, . . . , m}_ with transition probabilities 

**==> picture [161 x 30] intentionally omitted <==**

In each generation there are _m_ alleles, some of type _A_ and some of type _a_ . The types of alleles in generation _n_ +1 are found by choosing randomly (with replacement) from the types in generation _n_ . If _Xn_ denotes the number of alleles of type _A_ in generation _n_ , then ( _Xn_ ) _n≥_ 0 is a Markov chain with the above transition probabilities. 

This can be viewed as a model of inheritance for a particular gene with two alleles _A_ and _a_ . We suppose that each individual has two genes, so the possibilities are _AA_ , _Aa_ and _aa_ . Let us take _m_ to be even with _m_ = 2 _k_ . Suppose that individuals in the next generation are obtained by mating randomly chosen individuals from the current generation and that offspring inherit one allele from each parent. We have to allow that both parents may be the same, and in particular make no requirement that parents be of opposite sexes. Then if the generation _n_ is, for example 

**==> picture [123 x 11] intentionally omitted <==**

then each gene in generation _n_ + 1 is _A_ with probability 7 _/_ 10 and _a_ with probability 3 _/_ 10, all independent. We might, for example, get 

**==> picture [120 x 9] intentionally omitted <==**

_5. Applications_ 

176 

The structure of pairs of genes is irrelevant to the Markov chain ( _Xn_ ) _n≥_ 0, which simply counts the number of alleles of type _A_ . 

The communicating classes of ( _Xn_ ) _n≥_ 0 are _{_ 0 _}, {_ 1 _, . . . , m −_ 1 _}, {m}_ . States 0 and _m_ are absorbing and _{_ 1 _, . . . , m −_ 1 _}_ is transient. The hitting probabilities for state _m_ (pure _AA_ ) are given by 

**==> picture [175 x 12] intentionally omitted <==**

This is obvious when one notes that ( _Xn_ ) _n≥_ 0 is a martingale; alternatively one can check that 

**==> picture [70 x 33] intentionally omitted <==**

According to this model, genetic diversity eventually disappears. It is known, however, that, for _p ∈_ (0 _,_ 1), as _m →∞_ 

**==> picture [211 x 13] intentionally omitted <==**

where _T_ is the hitting time of _{_ 0 _, m}_ , so in a large population diversity does not disappear quickly. 

Some modifications are possible which model other aspects of genetic theory. Firstly, it may be that the three genetic types _AA_ , _Aa_ , _aa_ have a relative selective advantage given by _α, β, γ >_ 0 respectively. This means that the probability of choosing allele _A_ when _Xn_ = _i_ is given by 

**==> picture [231 x 32] intentionally omitted <==**

and the transition probabilities are 

**==> picture [127 x 27] intentionally omitted <==**

Secondly, we may allow genes to mutate. Suppose _A_ mutates to _a_ with probability _u_ and _a_ mutates to _A_ with probability _v_ . Then the probability of choosing _A_ when _Xn_ = _i_ is given by 

**==> picture [144 x 12] intentionally omitted <==**

and 

**==> picture [126 x 27] intentionally omitted <==**

_5.1 Markov chains in biology_ 

177 

With _u, v >_ 0, the states 0 and _m_ are no longer absorbing, in fact the chain is irreducible, so attention shifts from hitting probabilities to the invariant distribution _π_ . There is an exact calculation for the mean of _π_ : we have 

**==> picture [322 x 68] intentionally omitted <==**

so that 

**==> picture [80 x 12] intentionally omitted <==**

## **Example 5.1.4 (Moran model)** 

The Moran model is the birth-and-death chain on _{_ 0 _,_ 1 _, . . . , m}_ with transition probabilities 

**==> picture [354 x 14] intentionally omitted <==**

Here is the genetic interpretation: a population consists of individuals of two types, _a_ and _A_ ; we choose randomly one individual from the population at time _n_ , and add a new individual of the same type; then we choose, again randomly, one individual from the population at time _n_ and remove it; so we obtain the population at time _n_ +1. The same individual may be chosen each time, both to give birth and to die, in which case there is no change in the make-up of the population. Now, if _Xn_ denotes the number of type _A_ individuals in the population at time _n_ , then ( _Xn_ ) _n≥_ 0 is a Markov chain with transition matrix _P_ . 

There are some obvious differences from the Wright–Fisher model: firstly, the Moran model cannot be interpreted in terms of a species where genes come in pairs, or where individuals have more than one parent; secondly in the Moran model we only change one individual at a time, not the whole population. However, the basic Markov chain structure is the same, with communicating classes _{_ 0 _}, {_ 1 _, . . . , m −_ 1 _}, {m}_ , absorbing states 0 and _m_ and transient class _{_ 1 _, . . . , m −_ 1 _}_ . The Moran model is reversible, and, like the Wright–Fisher model, is a martingale. The hitting probabilities are given by 

**==> picture [150 x 12] intentionally omitted <==**

We can also calculate explicitly the mean time to absorption 

**==> picture [52 x 12] intentionally omitted <==**

178 _5. Applications_ 

where _T_ is the hitting time of _{_ 0 _, m}_ . The simplest method is first to fix _j_ and write down equations for the mean time _ki[j]_[spent][in] _[j]_[,][starting from] _[i]_[,] before absorption: 

**==> picture [310 x 33] intentionally omitted <==**

Then, for _i_ = 1 _, . . . , m −_ 1 

**==> picture [183 x 15] intentionally omitted <==**

so that 

**==> picture [188 x 35] intentionally omitted <==**

where _kj[j]_[is][determined][by] 

**==> picture [205 x 28] intentionally omitted <==**

which gives _kj[j]_[=] _[ m]_[.][Hence] 

**==> picture [220 x 40] intentionally omitted <==**

As in the Wright–Fisher model, one is really interested in the case where _m_ is large, and _i_ = _pm_ for some _p ∈_ (0 _,_ 1). Then 

**==> picture [353 x 34] intentionally omitted <==**

as _m →∞_ . So, as _m →∞_ 

**==> picture [213 x 14] intentionally omitted <==**

For the Wright–Fisher model we claimed that 

**==> picture [211 x 13] intentionally omitted <==**

which has the same functional form in _p_ and differs by a factor of _m/_ 2. This factor is partially explained by the fact that the Moran model deals 

_5.2 Queues and queueing networks_ 

179 

with one individual at a time, whereas the Wright–Fisher model changes all _m_ at once. 

## **Exercises** 

**5.1.1** Consider a branching process with immigration. This is defined, in the notation of Example 5.1.1, by 

**==> picture [142 x 13] intentionally omitted <==**

where ( _In_ ) _n≥_ 0 is a sequence of independent Z[+] -valued random variables with common generating function _ψ_ ( _t_ ) = E( _t[I][n]_ ). Show that, if _X_ 0 = 1, then 

**==> picture [152 x 33] intentionally omitted <==**

In the case where the number of immigrants in each generation is Poisson of parameter _λ_ , and where P( _N_ = 0) = 1 _− p_ and P( _N_ = 1) = _p_ , find the long-run proportion of time during which the population is zero. 

**5.1.2** A species of plant comes in three genotypes _AA_ , _Aa_ and _aa_ . A single plant of genotype _Aa_ is crossed with itself, so that the offspring has genotype _AA_ , _Aa_ or _aa_ with probabilities 1 _/_ 4, 1 _/_ 2 and 1 _/_ 4. How long on average does it take to achieve a pure strain, that is, _AA_ or _aa_ ? Suppose it is desired to breed an _AA_ plant. What should you do? How many crosses would your procedure require, on average? 

**5.1.3** In the Moran model we may introduce a selective bias by making it twice as likely that a type _a_ individual is chosen to die, as compared to a type _A_ individual. Thus in a population of size _m_ containing _i_ type _A_ individuals, the probability that some type _A_ is chosen to die is now _i/_ ( _i_ + 2( _m − i_ )). Suppose we begin with just one type _A_ . What is the probability that eventually the whole population is of type _A_ ? 

## **5.2 Queues and queueing networks** 

Queues form in many circumstances and it is important to be able to predict their behaviour. The basic mathematical model for queues runs as follows: there is a succession of customers wanting service; on arrival each customer must wait until a server is free, giving priority to earlier arrivals; it is assumed that the times between arrivals are independent random variables of the same distribution, and the times taken to serve customers are also independent random variables, of some other distribution. The main 

_5. Applications_ 

180 

quantity of interest is the random process ( _Xt_ ) _t≥_ 0 recording the number of customers in the queue at time _t_ . This is always taken to include both those being served and those waiting to be served. 

In cases where inter-arrival times and service times have exponential distributions, ( _Xt_ ) _t≥_ 0 turns out to be a _continuous-time Markov chain_ , so we can answer many questions about the queue. This is the context of our first six examples. Some further variations on queues of this type have already appeared in Exercises 3.4.1, 3.6.3, 3.7.1 and 3.7.2. 

If the inter-arrival times only are exponential, an analysis is still possible, by exploiting the memorylessness of the _Poisson process_ of arrivals, and a certain _discrete-time Markov chain_ embedded in the queue. This is explained in the final two examples. 

In each example we shall aim to describe some salient features of the queue in terms of the given data of arrival-time and service-time distributions. We shall find conditions for the stability of the queue, and in the stable case find means to compute the equilibrium distribution of queue length. We shall also look at the random times that customers spend waiting and the length of time that servers are continuously busy. 

## **Example 5.2.1 (M/M/1 queue)** 

This is the simplest queue of all. The code means: _memoryless inter-arrival times/memoryless service times/one server_ . Let us suppose that the interarrival times are exponential of parameter _λ_ , and the service times are exponential of parameter _µ_ . Then the number of customers in the queue ( _Xt_ ) _t≥_ 0 evolves as a Markov chain with the following diagram: 

**==> picture [215 x 28] intentionally omitted <==**

To see this, suppose at time 0 there are _i_ customers in the queue, where _i >_ 0. Denote by _T_ the time taken to serve the first customer and by _A_ the time of the next arrival. Then the first jump time _J_ 1 is _A ∧ T_ , which is exponential of parameter _λ_ + _µ_ , and _XJ_ 1 = _i −_ 1 if _T < A_ , _XJ_ 1 = _i_ + 1 if _T > A_ , which events are independent of _J_ 1, with probabilities _µ/_ ( _λ_ + _µ_ ) and _λ/_ ( _λ_ + _µ_ ) respectively. If we condition on _J_ 1 = _T_ , then _A−J_ 1 is exponential of parameter _λ_ and independent of _J_ 1: the time already spent waiting for an arrival is forgotten. Similarly, conditional on _J_ 1 = _A_ , _T − J_ 1 is exponential of parameter _µ_ and independent of _J_ 1. The case where _i_ = 0 is simpler as there is no serving going on. Hence, conditional on _XJ_ 1 = _j_ , ( _Xt_ ) _t≥_ 0 

_5.2 Queues and queueing networks_ 

181 

begins afresh from _j_ at time _J_ 1. It follows that ( _Xt_ ) _t≥_ 0 is the claimed Markov chain. This sort of argument should by now be very familiar and we shall not spell out the details like this in later examples. 

The M/M/1 queue thus evolves like a random walk, except that it does not take jumps below 0. We deduce that if _λ > µ_ then ( _Xt_ ) _t≥_ 0 is transient, that is _Xt →∞_ as _t →∞_ . Thus if _λ > µ_ the _queue grows without limit_ in the long term. When _λ < µ_ , ( _Xt_ ) _t≥_ 0 is positive recurrent with invariant distribution 

**==> picture [105 x 13] intentionally omitted <==**

So when _λ < µ_ the _average number of customers in the queue in equilibrium_ is given by 

**==> picture [246 x 31] intentionally omitted <==**

Also, the mean time to return to 0 is given by 

**==> picture [138 x 12] intentionally omitted <==**

so the _mean length of time that the server is continuously busy_ is given by 

**==> picture [122 x 12] intentionally omitted <==**

Another quantity of interest is the _mean waiting time for a typical customer_ , when _λ < µ_ and the queue is in equilibrium. Conditional on finding a queue of length _i_ on arrival, this is ( _i_ + 1) _/µ_ , so the overall mean waiting time is 

**==> picture [130 x 12] intentionally omitted <==**

A rough check is available here as we can calculate in two ways the expected total time spent in the queue over an interval of length _t_ : either we multiply the average queue length by _t_ , or we multiply the mean waiting time by the expected number of customers _λt_ . Either way we get _λt/µ − λ_ . The first calculation is exact but we have not fully justified the second. 

Thus, once the queue size is identified as a Markov chain, its behaviour is largely understood. Even in more complicated examples where exact calculation is limited, once the Markovian character of the queue is noted we know what sort of features to look for – transience and recurrence, convergence to equilibrium, long-run averages, and so on. 

_5. Applications_ 

182 

## **Example 5.2.2 (M/M/s queue)** 

This is a variation on the last example where there is one queue but there are _s_ servers. Let us assume that the arrival rate is _λ_ and the service rate by each server is _µ_ . Then if _i_ servers are occupied, the first service is completed at the minimum of _i_ independent exponential times of parameter _µ_ . The first service time is therefore exponential of parameter _iµ_ . The total service rate increases to a maximum _sµ_ when all servers are working. We emphasise that the queue size includes those customers who are currently being served. By an argument similar to the preceding example, the queue size ( _Xt_ ) _t≥_ 0 performs a Markov chain with the following diagram: 

**==> picture [283 x 30] intentionally omitted <==**

So this time we obtain a birth-and-death chain. It is transient in the case _λ > sµ_ and otherwise recurrent. To find an invariant measure we look at the detailed balance equations 

**==> picture [100 x 9] intentionally omitted <==**

Hence 

**==> picture [248 x 29] intentionally omitted <==**

The queue is therefore positive recurrent when _λ < sµ_ . There are two cases when the invariant distribution has a particularly nice form: when _s_ = 1 we are back to Example 5.2.1 and the invariant distribution is geometric of parameter _λ/µ_ : 

**==> picture [105 x 13] intentionally omitted <==**

When _s_ = _∞_ we normalize _π_ by taking _π_ 0 = _e[−][λ/µ]_ so that 

**==> picture [96 x 14] intentionally omitted <==**

and the invariant distribution is Poisson of parameter _λ/µ_ . 

The number of arrivals by time _t_ is a Poisson process of rate _λ_ . Each arrival corresponds to an increase in _Xt_ , and each departure to a decrease. Let us suppose that _λ < sµ_ , so there is an invariant distribution, and consider the queue in equilibrium. The detailed balance equations hold and ( _Xt_ ) _t≥_ 0 is non-explosive, so by Theorem 3.7.3 for any _T >_ 0, ( _Xt_ )0 _≤t≤T_ 

_5.2 Queues and queueing networks_ 

183 

and ( _XT −t_ )0 _≤t≤T_ have the same law. It follows that, in equilibrium, the number of departures by time _t_ is also a Poisson process of rate _λ_ . This is slightly counter-intuitive, as one might imagine that the departure process runs in fits and starts depending on the number of servers working. Instead, it turns out that the process of departures, in equilibrium, is just as regular as the process of arrivals. 

## **Example 5.2.3 (Telephone exchange)** 

A variation on the M/M/s queue is to turn away customers who cannot be served immediately. This might serve as a simple model for a telephone exchange, where the maximum number of calls that can be connected at once is _s_ : when the exchange is full, additional calls are lost. The maximum queue size or _buffer size_ is _s_ and we get the following modified Markov chain diagram: 

**==> picture [279 x 30] intentionally omitted <==**

We can find the invariant distribution of this finite Markov chain by solving the detailed balance equations, as in the last example. This time we get a _truncated Poisson distribution_ 

**==> picture [127 x 33] intentionally omitted <==**

By the ergodic theorem, the long-run proportion of time that the exchange is full, and hence the long-run proportion of calls that are lost, is given by 

**==> picture [129 x 33] intentionally omitted <==**

This is known as _Erlang’s formula_ . Compare this example with the bus maintenance problem in Exercise 3.7.1. 

## **Example 5.2.4 (Queues in series)** 

Suppose that customers have two service requirements: they arrive as a Poisson process of rate _λ_ to be seen first by server _A_ , and then by server 

_5. Applications_ 

184 

_B_ . For simplicity we shall assume that the service times are independent exponentials of parameters _α_ and _β_ respectively. What is the average queue length at _B_ ? 

Let us denote the queue length at _A_ by ( _Xt_ ) _t≥_ 0 and that by _B_ by ( _Yt_ ) _t≥_ 0. Then ( _Xt_ ) _t≥_ 0 is simply an M/M/1 queue. If _λ > α_ , then ( _Xt_ ) _t≥_ 0 is transient so there is eventually always a queue at _A_ and departures form a Poisson process of rate _α_ . If _λ < α_ , then, by the reversibility argument of Example 5.2.2, the process of departures from _A_ is Poisson of rate _λ_ , _provided queue A is in equilibrium_ . The question about queue length at _B_ is not precisely formulated: it does not specify that the queues should be in equilibrium; indeed if _λ ≥ α_ there is no equilibrium. Nevertheless, we hope you will agree to treat arrivals at _B_ as a Poisson process of rate _α ∧ λ_ . Then, by Example 5.2.1, the average queue length at _B_ when _α ∧ λ < β_ , in equilibrium, is given by ( _α ∧ λ_ ) _/_ � _β −_ ( _α ∧ λ_ )�. If, on the other hand, _α ∧ λ > β_ , then ( _Yt_ ) _t≥_ 0 is transient so the queue at _B_ grows without limit. 

There is an equilibrium for both queues if _λ < α_ and _λ < β_ . The fact that in equilibrium the output from _A_ is Poisson greatly simplifies the analysis of the two queues in series. For example, the average time taken by one customer to obtain both services is given by 

**==> picture [110 x 12] intentionally omitted <==**

## **Example 5.2.5 (Closed migration process)** 

Consider, first, a single particle in a finite state-space _I_ which performs a Markov chain with irreducible _Q_ -matrix _Q_ . We know there is a unique invariant distribution _π_ . We may think of the holding times of this chain as service times, by a single server at each node _i ∈ I_ . 

Let us suppose now that there are _N_ particles in the state-space, which move as before except that they must queue for service at every node. If we do not care to distinguish between the particles, we can regard this as a new process ( _Xt_ ) _t≥_ 0 with state-space _I_[�] = N _[I]_ , where _Xt_ = ( _ni_ : _i ∈ I_ ) if at time _t_ there are _ni_ particles at state _i_ . In fact, this new process is also a Markov chain. To describe its _Q_ -matrix _Q_[�] we define a function _δi_ : _I_[�] _→ I_[�] by 

**==> picture [84 x 12] intentionally omitted <==**

Thus _δi_ adds a particle at _i_ . Then for _i_ = _j_ the non-zero transition rates are given by 

**==> picture [182 x 15] intentionally omitted <==**

_5.2 Queues and queueing networks_ 

185 

Observe that we can write the invariant measure equation _πQ_ = 0 in the form 

**==> picture [230 x 26] intentionally omitted <==**

For _n_ = ( _ni_ : _i ∈ I_ ) we set 

**==> picture [72 x 25] intentionally omitted <==**

Then 

**==> picture [217 x 115] intentionally omitted <==**

Given _m ∈ I_[�] we can put _m_ = _δin_ in the last identity whenever _mi ≥_ 1. On summing the resulting equations we obtain 

**==> picture [177 x 26] intentionally omitted <==**

so _π_ � is an invariant measure for _Q_[�] . The total number of particles is conserved so _Q_[�] has communicating classes 

**==> picture [136 x 34] intentionally omitted <==**

and the unique invariant distribution for the _N_ -particle system is given by � normalizing _π_ restricted to _CN_ . 

## **Example 5.2.6 (Open migration process)** 

We consider a modification of the last example where new customers, or particles, arrive at each node _i ∈ I_ at rate _λi_ . We suppose also that customers receiving service at node _i_ leave the network at rate _µi_ . Thus customers enter the network, move from queue to queue according to a Markov chain and eventually leave, rather like a shopping centre. This model includes the closed system of the last example and also the queues 

186 

**==> picture [74 x 11] intentionally omitted <==**

in series of Example 5.2.4. Let _Xt_ = ( _Xt[i]_[:] _[i][∈][I]_[),][where] _[X] t[i]_[denotes][the] number of customers at node _i_ at time _t_ . Then ( _Xt_ ) _t≥_ 0 is a Markov chain in _I_[�] = N _[I]_ and the non-zero transition rates are given by 

� � � _q_ ( _n, δin_ ) = _λi, q_ ( _δin, δjn_ ) = _qij, q_ ( _δjn, n_ ) = _µj_ for _n ∈ I_[�] and distinct states _i, j ∈ I_ . We shall assume that _λi >_ 0 for some _i_ and _µj >_ 0 for some _j_ ; then _Q_[�] is irreducible on _I_[�] . 

The system of equations (5.1) for an invariant measure is replaced here by 

**==> picture [168 x 41] intentionally omitted <==**

This system has a unique solution, with _πi >_ 0 for all _i_ . This may be seen by considering the invariant distribution for the extended _Q_ -matrix _Q_ on _I ∪{∂}_ with off-diagonal entries 

**==> picture [156 x 13] intentionally omitted <==**

On summing the system over _i ∈ I_ we find 

**==> picture [84 x 25] intentionally omitted <==**

As in the last example, for _n_ = ( _ni_ : _i ∈ I_ ) we set 

**==> picture [72 x 25] intentionally omitted <==**

Transitions from _m ∈ I_[�] may be divided into those where a new particle is added and, for each _i ∈ I_ with _mi ≥_ 1, those where a particle is moved from _i_ to somewhere else. We have, for the first sort of transition 

**==> picture [220 x 58] intentionally omitted <==**

and for the second sort 

**==> picture [223 x 126] intentionally omitted <==**

_5.2 Queues and queueing networks_ 

187 

On summing these equations we obtain 

**==> picture [177 x 26] intentionally omitted <==**

� � so _π_ is an invariant measure for _Q_ . If _πi <_ 1 for all _i_ then _π_ has finite total mass[�] _i∈I_[(1] _[−][π][i]_[), otherwise the total mass if infinite.][Hence,] _[Q]_[�][ is positive] recurrent if and only if _πi <_ 1 for all _i_ , and in that case, in equilibrium, the individual queue lengths ( _Xt[i]_[:] _[i][∈][I]_[)][are] _[independent]_[geometric][random] variables with 

**==> picture [126 x 14] intentionally omitted <==**

## **Example 5.2.7 (M/G/1 queue)** 

As we argued in Section 2.4, the Poisson process is the natural probabilistic model for any uncoordinated stream of discrete events. So we are often justified in assuming that arrivals to a queue form a Poisson process. In the preceding examples we also assumed an exponential service-time distribution. This is desirable because it makes the queue size into a continuous-time Markov chain, but it is obviously inappropriate in many real-world examples. The service requirements of customers and the duration of telephone calls have observable distributions which are generally not exponential. A better model in this case is the M/G/1 queue, where G indicates that the service-time distribution is general. 

We can characterize the distribution of a service time _T_ by its distribution function 

**==> picture [82 x 12] intentionally omitted <==**

or by its Laplace transform 

**==> picture [170 x 26] intentionally omitted <==**

(The integral written here is the Lebesgue–Stieltjes integral: when T has a density function _f_ ( _t_ ) we can replace _dF_ ( _t_ ) by _f_ ( _t_ ) _dt_ .) Then the mean service time _µ_ is given by 

**==> picture [105 x 13] intentionally omitted <==**

To analyse the M/G/1 queue, we consider the queue size _Xn_ immediately following the _n_ th departure. Then 

**==> picture [247 x 12] intentionally omitted <==**

_5. Applications_ 

188 

where _Yn_ denotes the number of arrivals during the _n_ th service time. The case where _Xn_ = 0 is different because then we get an extra arrival before the ( _n_ + 1)th service time begins. By the Markov property of the Poisson process, _Y_ 1 _, Y_ 2 _, . . ._ are independent and identically distributed, _so_ ( _Xn_ ) _n≥_ 0 _is a discrete-time Markov chain_ . Indeed, except for visits to 0, ( _Xn_ ) _n≥_ 0 behaves as a random walk with jumps _Yn −_ 1. 

Let _Tn_ denote the _n_ th service time. Then, conditional on _Tn_ = _t_ , _Yn_ is Poisson of parameter _λt_ . So 

**==> picture [130 x 27] intentionally omitted <==**

and, indeed, we can compute the probability generating function 

**==> picture [207 x 56] intentionally omitted <==**

Set _ρ_ = E( _Yn_ ) = _λµ_ . We call _ρ_ the _service intensity_ . Let us suppose that _ρ <_ 1. We have 

**==> picture [176 x 12] intentionally omitted <==**

where _Zn_ denotes the number of visits of _Xn_ to 0 before time _n_ . So 

**==> picture [175 x 12] intentionally omitted <==**

Take _X_ 0 = 0, then, since _Xn ≥_ 0, we have for all _n_ 

**==> picture [105 x 12] intentionally omitted <==**

By the ergodic theorem we know that, as _n →∞_ 

**==> picture [84 x 12] intentionally omitted <==**

where _m_ 0 is the mean return time to 0. Hence 

**==> picture [100 x 12] intentionally omitted <==**

showing that ( _Xn_ ) _n≥_ 0 is positive recurrent. 

Suppose now that we start ( _Xn_ ) _n≥_ 0 with its equilibrium distribution _π_ . Set 

**==> picture [124 x 32] intentionally omitted <==**

_5.2 Queues and queueing networks_ 

189 

then 

**==> picture [207 x 69] intentionally omitted <==**

so 

**==> picture [258 x 14] intentionally omitted <==**

By l’Hˆopital’s rule, as _z ↑_ 1 

**==> picture [203 x 14] intentionally omitted <==**

Since _G_ (1) = 1 = _A_ (1), we must therefore have _π_ 0 = 1 _− ρ, m_ 0 = 1 _/_ (1 _− ρ_ ) and 

**==> picture [186 x 14] intentionally omitted <==**

Since _A_ is given explicitly in terms of the service-time distribution, we can now obtain, in principle, the full equilibrium distribution. The fact that generating functions work well here is due to the additive structure of (5.2). 

To obtain the _mean queue length_ we differentiate (5.3) 

**==> picture [327 x 14] intentionally omitted <==**

then substitute for _G_ ( _z_ ) to obtain 

**==> picture [358 x 33] intentionally omitted <==**

By l’Hˆopital’s rule: 

**==> picture [358 x 33] intentionally omitted <==**

Hence 

**==> picture [277 x 30] intentionally omitted <==**

In the case of the M/M/1 queue _ρ_ = _λ/µ_ , E( _T_[2] ) = 2 _/µ_[2] and E( _Xn_ ) = _ρ/_ (1 _− ρ_ ) = _λ/_ ( _µ − λ_ ), as we found in Example 5.2.1. 

_5. Applications_ 

190 

We shall use generating functions to study two more quantities of interest – the queueing time of a typical customer and the busy periods of the server. 

Consider the queue ( _Xn_ ) _n∈_ Z in equilibrium. Suppose that the customer who leaves at time 0 has spent time _Q_ queueing to be served, and time _T_ being served. Then, conditional on _Q_ + _T_ = _t_ , _X_ 0 is Poisson of parameter _λt_ , since the customers in the queue at time 0 are precisely those who arrived during the queueing and service times of the departing customer. Hence 

**==> picture [256 x 15] intentionally omitted <==**

where _M_ is the Laplace transform 

**==> picture [89 x 14] intentionally omitted <==**

On substituting for _G_ ( _z_ ) we obtain the formula 

**==> picture [188 x 20] intentionally omitted <==**

Differentiation and l’Hˆopital’s rule, as above, lead to a formula for the _mean queueing time_ 

**==> picture [243 x 32] intentionally omitted <==**

We now turn to the busy period _S_ . Consider the Laplace transform 

**==> picture [85 x 13] intentionally omitted <==**

Let _T_ denote the service time of the first customer in the busy period. Then conditional on _T_ = _t_ , we have 

**==> picture [110 x 11] intentionally omitted <==**

where _N_ is the number of customers arriving while the first customer is served, which is Poisson of parameter _λt_ , and where _S_ 1 _, S_ 2 _, . . ._ are independent, with the same distribution as _S_ . Hence 

**==> picture [292 x 57] intentionally omitted <==**

_5.2 Queues and queueing networks_ 

191 

Although this is an implicit relation for _B_ ( _w_ ), we can obtain moments by 

**==> picture [288 x 14] intentionally omitted <==**

so the _mean length of the busy period_ is given by 

**==> picture [87 x 12] intentionally omitted <==**

## **Example 5.2.8 (M/G/** _∞_ **queue)** 

Arrivals at this queue form a Poisson process, of rate _λ_ , say. Service times are independent, with a common distribution function _F_ ( _t_ ) = P( _T ≤ t_ ). There are infinitely many servers, so all customers in fact receive service at once. The analysis here is simpler than in the last example because customers do not interact. Suppose there are no customers at time 0. What, then, is the distribution of the number _Xt_ being served at time _t_ ? 

The number _Nt_ of arrivals by time _t_ is a Poisson random variable of parameter _λt_ . We condition on _Nt_ = _n_ and label the times of the _n_ arrivals randomly by _A_ 1 _, . . . , An_ . Then, by Theorem 2.4.6, _A_ 1 _, . . . , An_ are independent and uniformly distributed on the interval [0 _, t_ ]. For each of these customers, service is incomplete at time _t_ with probability 

**==> picture [210 x 28] intentionally omitted <==**

Hence, conditional on _Nt_ = _n_ , _Xt_ is binomial of parameters _n_ and _p_ . Then 

**==> picture [263 x 122] intentionally omitted <==**

So we have shown that _Xt_ is Poisson of parameter 

**==> picture [89 x 28] intentionally omitted <==**

_5. Applications_ 

192 

Recall that 

**==> picture [288 x 26] intentionally omitted <==**

Hence if E( _T_ ) _< ∞_ , the queue size has a limiting distribution, which is Poisson of parameter _λ_ E( _T_ ). 

For further reading see _Reversibility and Stochastic Networks_ by F. P. Kelly (Wiley, Chichester, 1978). 

## **5.3 Markov chains in resource management** 

Management decisions are always subject to risk because of the uncertainty of future events. If one can quantify that risk, perhaps on the basis of past experience, then the determination of the best action will rest on the calculation of probabilities, often involving a Markov chain. Here we present some examples involving the management of a resource: either the stock in a warehouse, or the water in a reservoir, or the reserves of an insurance company. See also Exercise 3.7.1 on the maintenance of unreliable equipment. The statistical problem of estimating transition rates for Markov chains has already been discussed in Section 1.10. 

## **Example 5.3.1 (Restocking a warehouse)** 

A warehouse has a capacity of _c_ units of stock. In each time period _n_ , there is a demand for _Dn_ units of stock, which is met if possible. We denote the residual stock at the end of period _n_ by _Xn_ . The warehouse manager restocks to capacity for the beginning of period _n_ + 1 whenever _Xn ≤ m_ , for some threshold _m_ . Thus ( _Xn_ ) _n≥_ 0 satisfies 

**==> picture [207 x 29] intentionally omitted <==**

Let us assume that _D_ 1 _, D_ 2 _, . . ._ are independent and identically distributed; then ( _Xn_ ) _n≥_ 0 is a Markov chain, and, excepting some peculiar demand structures, is irreducible on _{_ 0 _,_ 1 _, . . . , c}_ . Hence ( _Xn_ ) _n≥_ 0 has a unique invariant distribution _π_ which determines the long-run proportion of time in each state. Given that _Xn_ = _i_ , the expected unmet demand in period _n_ + 1 is given by 

**==> picture [169 x 32] intentionally omitted <==**

_5.3 Markov chains in resource management_ 

193 

Hence the long-run proportion of demand that is unmet is 

**==> picture [81 x 31] intentionally omitted <==**

The long-run frequency of restocking is given by 

**==> picture [70 x 31] intentionally omitted <==**

Now as _m_ increases, _u_ ( _m_ ) decreases and _r_ ( _m_ ) increases. The warehouse manager may want to compute these quantities in order to optimize the long-run cost 

**==> picture [73 x 12] intentionally omitted <==**

where _a_ is the cost of restocking and _b_ is the profit per unit. 

There is no general formula for _π_ , but once the distribution of the demand is known, it is a relatively simple matter to write down the ( _c_ + 1) _×_ ( _c_ + 1) transition matrix _P_ for ( _Xn_ ) _n≥_ 0 and solve _πP_ = _π_ subject to[�] _[c] i_ =0 _[π][i]_[= 1.] We shall discuss in detail a special case where the calculations work out nicely. 

Suppose that the capacity _c_ = 3, so possible threshold values are _m_ = 0 _,_ 1 _,_ 2. Suppose that the profit per unit _b_ = 1, and that the demand satisfies 

**==> picture [172 x 13] intentionally omitted <==**

Then 

**==> picture [302 x 31] intentionally omitted <==**

The transition matrices for _m_ = 0 _,_ 1 _,_ 2 are given, respectively, by 

**==> picture [365 x 51] intentionally omitted <==**

with invariant distributions 

**==> picture [303 x 12] intentionally omitted <==**

Hence 

**==> picture [187 x 12] intentionally omitted <==**

_5. Applications_ 

194 

and 

**==> picture [187 x 12] intentionally omitted <==**

Therefore, to minimize the long-run cost _ar_ ( _m_ ) + _u_ ( _m_ ) we should take 

**==> picture [122 x 47] intentionally omitted <==**

## **Example 5.3.2 (Reservoir model – discrete time)** 

We are concerned here with a storage facility, for example a reservoir, of finite capacity _c_ . In each time period _n_ , _An_ units of resource are available to enter the facility and _Bn_ units are drawn off. When the reservoir is full, surplus water is lost. When the reservoir is empty, no water can be supplied. We assume that newly available resources cannot be used in the current time period. Then the quantity of water _Xn_ in the reservoir at the end of period _n_ satisfies 

**==> picture [180 x 14] intentionally omitted <==**

If we assume that _An_ , _Bn_ and _c_ are integer-valued and that _A_ 1 _, A_ 2 _, . . ._ are independent and identically distributed, likewise _B_ 1 _, B_ 2 _, . . ._ , then ( _Xn_ ) _n≥_ 0 is a Markov chain on _{_ 0 _,_ 1 _, . . . , c}_ , whose transition probabilities may be deduced from the distributions of _An_ and _Bn_ . Hence we know that the longrun behaviour of ( _Xn_ ) _n≥_ 0 is controlled by its unique invariant distribution _π_ , assuming irreducibility. For example, the long-run proportion of time that the reservoir is empty is simply _π_ 0. So we would like to calculate _π_ . 

A simplifying assumption which makes some calculations possible is to assume that consumption in each period is constant, and that our units are chosen to make this constant 1. Then the infinite capacity model satisfies a recursion similar to the M/G/1 queue: 

**==> picture [133 x 13] intentionally omitted <==**

Hence, by the argument used in Example 5.2.7, if E( _An_ ) _<_ 1, then ( _Xn_ ) _n≥_ 0 is positive recurrent and the invariant distribution _π_ satisfies 

**==> picture [213 x 31] intentionally omitted <==**

where _A_ ( _z_ ) = E( _z[A][n]_ ). In fact, whether or not E( _An_ ) _<_ 1, the equation 

**==> picture [164 x 32] intentionally omitted <==**

_5.3 Markov chains in resource management_ 

195 

serves to define a solution to the infinite system of linear equations 

**==> picture [186 x 52] intentionally omitted <==**

where _ai_ = P( _An_ = _i_ ). 

Note that ( _Xn_ ) _n≥_ 0 can only enter _{_ 0 _,_ 1 _, . . . , c}_ through _c_ . Hence, by the strong Markov property, ( _Xn_ ) _n≥_ 0 observed whilst in _{_ 0 _,_ 1 _, . . . , c}_ is simply the finite-capacity model. In the case where E( _An_ ) _<_ 1, we can deduce for the finite-capacity model that the long-run proportion of time in state _i_ is given by _νi/_ ( _ν_ 0 + _. . ._ + _νc_ ). In fact, this is true in general as the equilibrium equations for the finite-capacity model coincide with those for _ν_ up to level _c −_ 1, and the level _c_ equation is redundant. 

In reality, it is to be hoped that, in the long run, supply will exceed demand, which is true if E( _An_ ) _>_ 1. Then ( _Xn_ ) _n≥_ 0 is transient, so _ν_ must have infinite total mass. The problem faced by the water company is to keep the long-run proportion of time _π_ 0( _c_ ) that the reservoir is empty below a certain acceptable fraction, _ε >_ 0 say. Hence _c_ should be chosen large enough to make 

**==> picture [105 x 11] intentionally omitted <==**

which is always possible in the transient case. 

## **Example 5.3.3 (Reservoir model – continuous time)** 

Consider a reservoir model where fresh water arrives at the times of a Poisson process of rate _λ_ . The quantities of water _S_ 1 _, S_ 2 _, . . ._ arriving each time are assumed independent and identically distributed. We assume that there is a continuous demand for water of rate 1. For a reservoir of infinite capacity, the quantity of water held ( _Wt_ ) _t≥_ 0 is just the stored work in an M/G/1 queue with the same arrival times and service times _S_ 1 _, S_ 2 _, . . ._ . The periods when the reservoir is empty correspond to idle periods of the queue. Hence in the positive recurrent case where _λ_ E( _Sn_ ) _<_ 1, the long-run proportion of time that the reservoir is empty is given by E( _Sn_ ) _/_ (1 _− λ_ E( _Sn_ )). Note that ( _Wt_ ) _t≥_ 0 can enter [0 _, c_ ] only through _c_ . As in the preceding example we can obtain the finite capacity model by observing ( _Wt_ ) _t≥_ 0 whilst in [0 _, c_ ], but we shall not pursue this here. 

The next example is included, in part, because it illustrates a surprising and powerful connection between _reflected random walks_ and the _maxima_ 

_5. Applications_ 

196 

_of random walks_ , which we now explain. Let _X_ 1 _, X_ 2 _, . . ._ denote a sequence of independent, identically distributed random variables. Set _Sn_ = _X_ 1 + _. . ._ + _Xn_ and define ( _Zn_ ) _n≥_ 0 by _Z_ 0 = 0 and 

**==> picture [112 x 13] intentionally omitted <==**

Then, by induction, we have 

**==> picture [240 x 12] intentionally omitted <==**

so _Zn has the same distribution as Mn_ where 

**==> picture [284 x 18] intentionally omitted <==**

## **Example 5.3.4 (Ruin of an insurance company)** 

An insurance company receives premiums continuously at a constant rate. We choose units making this rate 1. The company pays claims at the times of a Poisson process of rate _λ_ , the claims _Y_ 1 _, Y_ 2 _, . . ._ being independent and identically distributed. Set _ρ_ = _λ_ E( _Y_ 1) and assume that _ρ <_ 1. Then in the long run the company can expect to make a profit of 1 _− ρ_ per unit time. However, there is a danger that large claims early on will ruin the company even though the long-term trend is good. 

Denote by _Sn_ the cumulative net loss following the _n_ th claim. Thus _Sn_ = _X_ 1 + _. . ._ + _Xn_ , where _Xn_ = _Yn − Tn_ and _Tn_ is the _n_ th inter-arrival time. By the strong law of large numbers 

**==> picture [122 x 12] intentionally omitted <==**

as _n →∞_ . The maximum loss that the company will have to sustain is 

**==> picture [68 x 15] intentionally omitted <==**

where 

**==> picture [72 x 17] intentionally omitted <==**

By the argument given above, _Mn_ has the same distribution as _Zn_ , where _Z_ 0 = 0 and 

**==> picture [124 x 13] intentionally omitted <==**

But _Zn_ is the queueing time of the _n_ th customer in the M/G/1 queue with inter-arrival times _Tn_ and service times _Yn_ . We know by Example 5.2.7 that the queue-length distribution converges to equilibrium. Hence, so does the 

_5.4 Markov decision processes_ 

197 

queueing-time distribution. Also by Example 5.2.7, we know the Laplace transform of the equilibrium queueing-time distribution. Hence 

**==> picture [224 x 21] intentionally omitted <==**

The probability of eventual bankruptcy is P( _M > a_ ), where _a_ denotes the initial value of the company’s assets. In principle, this may now be obtained by inverting the Laplace transform. 

## **5.4 Markov decision processes** 

In many contexts costs are incurred at a rate determined by some process which may best be modelled as a Markov chain. We have seen in Section 1.10 and Section 4.2 how to calculate in these circumstances the long-run average cost or the expected total cost. Suppose now that we are able to choose the transition probabilities for each state from a given class and that our choice determines the cost incurred. The question arises as to how best to do this to minimize our expected costs. 

## **Example 5.4.1** 

A random walker on _{_ 0 _,_ 1 _,_ 2 _, . . . }_ jumps one step to the right with probability _p_ and one step to the left with probability _q_ = 1 _− p_ . Any value of _p ∈_ (0 _,_ 1] may be chosen, but incurs a cost 

**==> picture [54 x 12] intentionally omitted <==**

The walker on reaching 0 stays there, incurring no further costs. 

If we are only concerned with minimizing costs over the first few time steps, then the choice _p_ = 1 may be best. However, in the long run the only way to avoid an infinite total cost is to get to 0. Starting from _i_ we must first hit _i −_ 1, then _i −_ 2, and so on. Given the lack of memory in the model, this makes it reasonable to pick the same value of _p_ throughout, and seek to minimize _φ_ ( _p_ ), the expected total cost starting from 1. The expected total cost starting from 2 is 2 _φ_ ( _p_ ) since we must first hit 1. Hence 

**==> picture [100 x 12] intentionally omitted <==**

so that 

**==> picture [178 x 28] intentionally omitted <==**

Thus for _c_ ( _p_ ) = 1 _/p_ the choice _p_ = 1 _/_ 4 is optimal, with expected cost 8. The general discussion which follows will make rigorous what we claimed was reasonable. 

_5. Applications_ 

198 

Generally, let us suppose given some distribution _λ_ = ( _λi_ : _i ∈ I_ ) and, for each _action a ∈ A_ , a transition matrix _P_ ( _a_ ) = � _pij_ ( _a_ ) : _i, j ∈ I_ � and a cost function _c_ ( _a_ ) = � _ci_ ( _a_ ) : _i ∈ I_ �. These are the data for a _Markov decision process_ , though so far we have no process and when we do it will not in general be Markov. To get a process we must choose a policy, that is, a way of determining actions by our current knowledge of the process. Formally, a _policy u_ is a sequence of functions 

**==> picture [170 x 13] intentionally omitted <==**

Each policy _u_ determines a probability law P _[u]_ for a process ( _Xn_ ) _n≥_ 0 with values in _I_ by 

**==> picture [109 x 12] intentionally omitted <==**

(ii) P _[u]_ ( _Xn_ +1 = _in_ +1 _| X_ 0 = _i_ 0 _, . . . , Xn_ = _in_ ) = _pin in_ +1� _un_ ( _i_ 0 _, . . . , in_ )�. A _stationary policy u_ is a function _u_ : _I → A_ . We abuse notation and write _u_ also for the associated policy given by 

**==> picture [109 x 12] intentionally omitted <==**

Under a stationary policy _u_ , the probability law P _[u]_ makes ( _Xn_ ) _n≥_ 0 Markov, with transition probabilities _p[u] ij_[=] _[ p][ij]_ � _u_ ( _i_ )�. 

We suppose that a cost _c_ ( _i, a_ ) = _ci_ ( _a_ ) is incurred when action _a_ is chosen in state _i_ . Then we associate to a policy _u_ an _expected total cost_ starting from _i_ , given by 

**==> picture [189 x 30] intentionally omitted <==**

So that this sum is well defined, we assume that _c_ ( _i, a_ ) _≥_ 0 for all _i_ and _a_ . Define also the _value function_ 

**==> picture [84 x 16] intentionally omitted <==**

which is the minimal expected total cost starting from _i_ . 

The basic problem of Markov decision theory is how to minimize expected costs by our choice of policy. The minimum expected cost incurred before time _n_ = 1 is given by 

**==> picture [85 x 16] intentionally omitted <==**

Then the minimum expected cost incurred before time _n_ = 2 is 

**==> picture [180 x 26] intentionally omitted <==**

_5.4 Markov decision processes_ 

199 

Define inductively 

**==> picture [275 x 26] intentionally omitted <==**

It is easy to see by induction that _Vn_ ( _i_ ) _≤ Vn_ +1( _i_ ) for all _i_ , so _Vn_ ( _i_ ) increases to a limit _V∞_ ( _i_ ), possibly infinite. We have 

**==> picture [224 x 26] intentionally omitted <==**

so, letting _n →∞_ and then minimizing over _a_ , 

**==> picture [273 x 26] intentionally omitted <==**

It is a reasonable guess that _V∞_ ( _i_ ), being the limit of minimal expected costs over finite time intervals, is in fact the value function _V[∗]_ ( _i_ ). This is not always true, unless we can show that the inequality (5.5) is actually an equality. We make three technical assumptions to ensure this. _We assume that_ 

- (i) _for all i, j the functions ci_ : _A →_ [0 _, ∞_ ) _and pij_ : _A →_ [0 _, ∞_ ) _are continuous;_ 

- (ii) _for all i and all B < ∞ the set {a_ : _ci_ ( _a_ ) _≤ B} is compact;_ 

(iii) _for each i, for all but finitely many j, for all a ∈ A we have pij_ ( _a_ ) = 0 _._ A simple case where (i) and (ii) hold is when _A_ is a finite set. It is easy to check that the assumptions are valid in Example 5.4.1, with _A_ = (0 _,_ 1], _ci_ ( _a_ ) = 1 _/a_ and 

**==> picture [145 x 48] intentionally omitted <==**

with obvious exceptions at _i_ = 0. 

**Lemma 5.4.2.** _There is a stationary policy u such that_ 

**==> picture [274 x 26] intentionally omitted <==**

_Proof._ If _V∞_ ( _i_ ) = _∞_ there is nothing to prove, so let us assume that _V∞_ ( _i_ ) _≤ B < ∞_ . Then 

**==> picture [204 x 41] intentionally omitted <==**

_5. Applications_ 

200 

where _K_ is the compact set _{a_ : _c_ ( _i, a_ ) _≤ B}_ and where _J_ is the finite set _{j_ : _pij ̸≡_ 0 _}_ . Hence, by continuity, the infimum is attained and 

**==> picture [281 x 26] intentionally omitted <==**

for some _un_ ( _i_ ) _∈ K_ . By compactness there is a convergent subsequence _unk_ ( _i_ ) _→ u_ ( _i_ ), say, and, on passing to the limit _nk →∞_ in (5.7), we obtain (5.6). 

**Theorem 5.4.3.** _We have_ 

(i) _Vn_ ( _i_ ) _↑ V[∗]_ ( _i_ ) _as n →∞ for all i;_ 

(ii) _if u[∗] is any stationary policy such that a_ = _u[∗]_ ( _i_ ) _minimizes_ 

**==> picture [115 x 26] intentionally omitted <==**

_for all i, then u[∗] is optimal, in the sense that_ 

**==> picture [134 x 14] intentionally omitted <==**

_Proof._ For any policy _u_ we have 

**==> picture [204 x 62] intentionally omitted <==**

where _u_ [ _i_ ] is the policy given by 

**==> picture [179 x 12] intentionally omitted <==**

Hence we obtain 

**==> picture [182 x 26] intentionally omitted <==**

and, on taking the infimum over _u_ 

**==> picture [271 x 26] intentionally omitted <==**

Certainly, _V_ 0( _i_ ) = 0 _≤ V[∗]_ ( _i_ ). Let us suppose inductively that _Vn_ ( _i_ ) _≤ V[∗]_ ( _i_ ) for all _i_ . Then by substitution in the right sides of (5.4) and (5.8) we find _Vn_ +1( _i_ ) _≤ V[∗]_ ( _i_ ) and the induction proceeds. Hence _V∞_ ( _i_ ) _≤ V[∗]_ ( _i_ ) for all _i_ . 

_5.4 Markov decision processes_ 

201 

Let _u[∗]_ be any stationary policy for which 

**==> picture [201 x 26] intentionally omitted <==**

We know such a policy exists by Lemma 5.4.2. Then by Theorem 4.2.3 we have _V[u][∗]_ ( _i_ ) _≤ V∞_ ( _i_ ) for all _i_ . But _V[∗]_ ( _i_ ) _≤ V[u][∗]_ ( _i_ ) for all _i_ , so 

**==> picture [174 x 14] intentionally omitted <==**

and we are done. 

The theorem just proved shows that the problem of finding a good policy is much simpler than we might have supposed. For it was not clear at the outset that there would be a single policy which was optimal for all _i_ , even less that this policy would be stationary. Moreover, part (i) gives an explicit way of obtaining the value function _V[∗]_ and, once this is known, part (ii) identifies an optimal stationary policy. 

In practice we may know only an approximation to _V[∗]_ , for example _Vn_ for _n_ large. We may then hope that, by choosing _a_ = _u_ ( _i_ ) to minimize 

**==> picture [113 x 26] intentionally omitted <==**

we get a nearly optimal policy. An alternative means of constructing nearly optimal policies is sometimes provided by the method of _policy improvement_ . Given one stationary policy _u_ we may define another _θu_ by the requirement that _a_ = ( _θu_ )( _i_ ) minimizes 

**==> picture [119 x 27] intentionally omitted <==**

**Theorem 5.4.4 (Policy improvement).** _We have_ 

(i) _V[θu]_ ( _i_ ) _≤ V[u]_ ( _i_ ) _for all i;_ (ii) _V[θ][n][ u]_ ( _i_ ) _↓ V[∗]_ ( _i_ ) _as n →∞ for all i, provided that_ 

**==> picture [274 x 15] intentionally omitted <==**

_Proof._ (i) We have, by Theorem 4.2.3 

**==> picture [196 x 58] intentionally omitted <==**

so _V[u]_ ( _i_ ) _≥ V[θu]_ ( _i_ ) for all _i_ , by Theorem 4.2.3. 

_5. Applications_ 

202 

(ii) We note from part (i) that 

**==> picture [319 x 26] intentionally omitted <==**

Fix _N ≥_ 0 and consider for _n_ = 0 _,_ 1 _, . . . , N_ the process 

**==> picture [196 x 33] intentionally omitted <==**

Recall the notation for conditional expectation introduced in Section 4.1. We have 

**==> picture [321 x 80] intentionally omitted <==**

where we used (5.10) with _u_ replaced by _θ[N][−][n][−]_[1] _u_ , _i_ = _Xn_ and _a_ = _u[∗]_ ( _Xn_ ). It follows that E _[u][∗]_ ( _Mn_ +1) _≥_ E _[u][∗]_ ( _Mn_ ) for all _n_ . Hence if we assume (5.9), then 

**==> picture [262 x 71] intentionally omitted <==**

We have been discussing the minimization of expected total cost, which is only relevant to the transient case. This is because we will have _V[∗]_ ( _i_ ) = _∞_ unless for some stationary policy _u_ , the only states _j_ with positive cost _c_ ( _j, u_ ( _j_ )) _>_ 0, accessible from _i_ , are transient. The recurrent case is also of practical importance and one way to deal with this is to discount costs at future times by a fixed factor _α ∈_ (0 _,_ 1). We now seek to minimize the _expected total discounted cost_ 

**==> picture [202 x 31] intentionally omitted <==**

Define the _discounted value function_ 

**==> picture [87 x 16] intentionally omitted <==**

_5.4 Markov decision processes_ 

203 

In fact, the discounted case reduces to the undiscounted case by introducing a new absorbing state _∂_ and defining a new Markov decision process by 

**==> picture [166 x 29] intentionally omitted <==**

Thus the new process follows the old until, at some geometric time of parameter _α_ , it jumps to _∂_ and stays there, incurring no further costs. Introduce _V_ 0 _,α_ ( _i_ ) = 0 and, inductively 

**==> picture [214 x 26] intentionally omitted <==**

and, given a stationary policy _u_ , define another _θαu_ by the requirement that _a_ = ( _θαu_ )( _i_ ) minimizes 

**==> picture [128 x 26] intentionally omitted <==**

**Theorem 5.4.5.** _Suppose that the cost function c_ ( _i, a_ ) _is uniformly bounded._ 

- (i) _We have Vn,α_ ( _i_ ) _↑ Vα[∗]_[(] _[i]_[)] _[as][n][ →∞][for][all][i][.]_ 

- (ii) _The value function Vα[∗][is][the][unique][bounded][solution][to]_ 

**==> picture [263 x 26] intentionally omitted <==**

(iii) _Let u[∗] be a stationary policy such that a_ = _u[∗]_ ( _i_ ) _minimizes_ 

**==> picture [123 x 26] intentionally omitted <==**

_for all i. Then u[∗] is optimal in the sense that_ 

**==> picture [134 x 14] intentionally omitted <==**

(iv) _For all stationary policies u we have_ 

**==> picture [188 x 15] intentionally omitted <==**

_Proof._ With obvious notation we have 

**==> picture [224 x 15] intentionally omitted <==**

_5. Applications_ 

204 

so parts (i), (ii) and (iii) follow directly from Theorems 5.4.3 and 5.4.4, except for the uniqueness claim in (ii). But given any bounded solution _V_ to (5.11), there is a stationary policy _u_ such that 

**==> picture [186 x 27] intentionally omitted <==**

Then _V_ = _Vα[u]_[,][by][Theorem 4.2.5.][Then] _[θ][α][u]_[ =] _[ u]_[so][(iv)][will][show][that] _[u]_[is] optimal and _V_ = _Vα[∗]_[.] 

We have _c_ ( _i, a_ ) _≤ B_ for some _B < ∞_ . So for any stationary policy _u_ we have 

**==> picture [216 x 31] intentionally omitted <==**

and so 

**==> picture [259 x 16] intentionally omitted <==**

as _n →∞_ . Hence (iv) also follows from Theorem 5.4.4. 

We finish with a discussion of long-run average costs. Here we are concerned with the limiting behaviour, as _n →∞_ , of 

**==> picture [220 x 34] intentionally omitted <==**

We assume that 

**==> picture [175 x 12] intentionally omitted <==**

_u u_ This forces _|V n_[(] _[i]_[)] _[|][≤][B]_[for][all] _[n]_[,][but][in][general][the][sequence] _V n_[(] _[i]_[)][may] fail to converge as _n →∞_ . In the case of a stationary strategy _u_ for which ( _Xn_ ) _n≥_ 0 has a unique invariant distribution _π[u]_ , we know by the ergodic theorem that 

**==> picture [186 x 34] intentionally omitted <==**

as _n →∞_ , P _[u] i_[-almost][surely,][for][all] _[i]_[.] So _V un_[(] _[i]_[)][does][converge][in][this] case by bounded convergence, with the same limit. This suggests that one approach to minimizing long-run costs might be to minimize 

**==> picture [78 x 26] intentionally omitted <==**

But, although this is sometimes valid, we do not know in general that the optimal policy is positive recurrent, or even stationary. Instead, we use a martingale approach, which is more general. 

_5.4 Markov decision processes_ 

205 

**Theorem 5.4.6.** _Suppose we can find a constant V ∗ and a bounded function W_ ( _i_ ) _such that_ 

**==> picture [326 x 26] intentionally omitted <==**

_Let u[∗] be any stationary strategy such that a_ = _u[∗]_ ( _i_ ) _achieves the infimum in_ (5.12) _for each i. Then_ 

**==> picture [220 x 33] intentionally omitted <==**

_Proof._ Fix a strategy _u_ and set _Un_ = _un_ ( _X_ 0 _, . . . , Xn_ ). Consider 

**==> picture [182 x 33] intentionally omitted <==**

Then 

**==> picture [292 x 59] intentionally omitted <==**

with equality if _u_ = _u[∗]_ . Therefore 

**==> picture [277 x 15] intentionally omitted <==**

So we obtain 

**==> picture [141 x 21] intentionally omitted <==**

This implies (ii) on letting _n →∞_ . When _u_ = _u[∗]_ we also have 

**==> picture [142 x 23] intentionally omitted <==**

and hence (i). 

The most obvious point of this theorem is that it identifies an optimal stationary policy when the hypothesis is met. Two further aspects also deserve comment. Firstly, if _u_ is a stationary policy for which ( _Xn_ ) _n≥_ 0 has an invariant distribution _π[u]_ , then 

**==> picture [299 x 70] intentionally omitted <==**

_5. Applications_ 

206 

so 

**==> picture [102 x 25] intentionally omitted <==**

with equality if we can take _u_ = _u[∗]_ . 

Secondly, there is a connection with the case of discounted costs. Assume that _I_ is finite and that _P_ ( _a_ ) is irreducible for all _a_ . Then we can show that as _α ↑_ 1 we have 

**==> picture [189 x 14] intentionally omitted <==**

On substituting this into (5.11) we find 

so 

**==> picture [302 x 122] intentionally omitted <==**

which brings us back to (5.12) on letting _α ↑_ 1. 

The interested reader is referred to S. M. Ross, _Applied Probability Models with Optimization Applications_ (Holden-Day, San Francisco, 1970) and to H. C. Tijms, _Stochastic Models – an algorithmic approach_ (Wiley, Chichester, 1994) for more examples, results and references. 

## **5.5 Markov chain Monte Carlo** 

Most computers may be instructed to provide a sequence of numbers 

**==> picture [116 x 45] intentionally omitted <==**

written as decimal expansions of a certain length, which for many purposes may be regarded as sample values of a sequence of independent random variables, uniformly distributed on [0 _,_ 1]: 

**==> picture [120 x 12] intentionally omitted <==**

_5.5 Markov chain Monte Carlo_ 

207 

We are cautious in our language because, of course, _u_ 1 _, u_ 2 _, u_ 3 _, . . ._ are actually all integer multiples of 10 _[−][m]_ and, more seriously, they are usually derived sequentially by some entirely deterministic algorithm in the computer. Nevertheless, the generators of such _pseudo-random numbers_ are in general as reliable an imitation as one could wish of _U_ 1( _ω_ ) _, U_ 2( _ω_ ) _, U_ 3( _ω_ ) _, . . ._ . This makes it worth while considering how one might construct Markov chains from a given sequence of independent uniform random variables, and then might exploit the observed properties of such processes. 

We shall now describe one procedure to simulate a Markov chain ( _Xn_ ) _n≥_ 0 with initial distribution _λ_ and transition matrix _P_ . Since[�] _i∈I[λ][i]_[=][1][we] can partition [0 _,_ 1] into disjoint subintervals ( _Ai_ : _i ∈ I_ ) with lengths 

**==> picture [46 x 12] intentionally omitted <==**

Similarly for each _i ∈ I_ , we can partition [0 _,_ 1] into disjoint subintervals ( _Aij_ : _j ∈ I_ ) such that 

**==> picture [54 x 13] intentionally omitted <==**

Now functions 

**==> picture [86 x 28] intentionally omitted <==**

by 

**==> picture [114 x 30] intentionally omitted <==**

Suppose that _U_ 0 _, U_ 1 _, U_ 2 _, . . ._ is a sequence of independent random variables, uniformly distributed on [0 _,_ 1], and set 

**==> picture [161 x 29] intentionally omitted <==**

Then 

**==> picture [144 x 12] intentionally omitted <==**

**==> picture [339 x 13] intentionally omitted <==**

so ( _Xn_ ) _n≥_ 0 is Markov( _λ, P_ ). 

This simple procedure may be used to investigate empirically those aspects of the behaviour of a Markov chain where theoretical calculations become infeasible. 

_5. Applications_ 

208 

The remainder of this section is devoted to one application of the simulation of Markov chains. It is the application which finds greatest practical use, especially in statistics, statistical physics and computer science, known as _Markov chain Monte Carlo_ . Monte Carlo is another name for computer simulation so this sounds no different from the procedure just discussed. But what is really meant is simulation _by means of_ Markov chains, the object of primary interest being the invariant distribution of the Markov chain and not the chain itself. After a general discussion we shall give two examples. 

The context for Markov chain Monte Carlo is a state-space in product form 

**==> picture [58 x 25] intentionally omitted <==**

where Λ is a finite set. For the purposes of this discussion we shall also assume that each component _Sm_ is a finite set. A random variable _X_ with values in _I_ is then a family of component random variables � _X_ ( _m_ ) : _m ∈_ Λ�, where, for each site _m ∈_ Λ, _X_ ( _m_ ) takes values in _Sm_ . 

We are given a distribution _π_ = ( _πi_ : _i ∈ I_ ), perhaps up to an unknown constant multiple, and it is desired to compute the number 

**==> picture [198 x 25] intentionally omitted <==**

for some given function _f_ = ( _fi_ : _i ∈ I_ ). The essential point to understand is that Λ is typically a large set, making the state-space _I_ very large indeed. Then certain operations are computationally infeasible – performing the sum (5.13) state by state for a start. 

An alternative approach would be to simulate a large number of independent random variables _X_ 1 _, . . . , Xn_ in _I_ , each with distribution _π_ , and to approximate (5.13) by 

**==> picture [63 x 31] intentionally omitted <==**

The strong law of large numbers guarantees that this is a good approximation as _n →∞_ and, moreover, one can obtain error estimates which indicate how large to make _n_ in practice. However, simulation from the distribution _π_ is also difficult, unless _π_ has product form 

**==> picture [110 x 26] intentionally omitted <==**

For recall that a computer just simulates sequences of independent _U_ [0 _,_ 1] random variables. When _π_ does not have product form, Markov chain Monte Carlo is sometimes the only way to simulate samples from _π_ . 

_5.5 Markov chain Monte Carlo_ 

209 

The basic idea is to simulate a Markov chain ( _Xn_ ) _n≥_ 0, which is constructed to have invariant distribution _π_ . Then, assuming aperiodicity and irreducibility, we know, by Theorem 1.8.3, that as _n →∞_ the distribution of _Xn_ converges to _π_ . Indeed, assuming only irreducibility, Theorem 1.10.2 shows that 

**==> picture [113 x 34] intentionally omitted <==**

with probability 1. But why should simulating an entire Markov chain be easier than simulating a simple distribution _π_ ? The answer lies in the fact that the state-space is a product. 

Each component _X_ 0( _m_ ) of the initial state _X_ 0 is a random variable in _Sm_ . It does not matter crucially what distribution _X_ 0 is given, but we might, for example, make all components independent. The process ( _Xn_ ) _n≥_ 0 is made to evolve by changing components one site at a time. When the chosen site is _m_ , we simulate a new random variable _Xn_ +1( _m_ ) with values in _Sm_ according to a distribution determined by _Xn_ , and for _k_ = _m_ we set _Xn_ +1( _k_ ) = _Xn_ ( _k_ ). Thus at each step we have only to simulate a random variable in _Sm_ , not one in the much larger space _I_ . 

_m_ Let us write _i ∼ j_ if _i_ and _j_ agree, except possibly at site _m_ . The law for simulating a new value at site _m_ is described by a transition matrix _P_ ( _m_ ), where 

**==> picture [122 x 14] intentionally omitted <==**

We would like _π_ to be invariant for _P_ ( _m_ ). A sufficient condition is that the detailed balance equations hold: thus for all _i, j_ we want 

**==> picture [102 x 12] intentionally omitted <==**

There are many possible choices for _P_ ( _m_ ) satisfying these equations. Indeed, given any stochastic matrix _R_ ( _m_ ) with 

**==> picture [118 x 13] intentionally omitted <==**

we can determine such a _P_ ( _m_ ) by 

**==> picture [172 x 14] intentionally omitted <==**

for _i ̸_ = _j_ , and then 

**==> picture [137 x 27] intentionally omitted <==**

_5. Applications_ 

210 

This has the following interpretation: if _Xn_ = _i_ we simulate a new random variable _Yn_ so that _Yn_ = _j_ with probability _rij_ ( _m_ ), then if _Yn_ = _j_ we set 

**==> picture [276 x 29] intentionally omitted <==**

This is called a _Hastings algorithm_ . 

There are two commonly used special cases. On taking 

**==> picture [173 x 32] intentionally omitted <==**

we also 

**==> picture [177 x 33] intentionally omitted <==**

So we simply resample _Xn_ ( _m_ ) according to the conditional distribution under _π_ , given the other components. This is called the _Gibbs sampler_ . It is particularly useful in Bayesian statistics. 

On taking _rij_ ( _m_ ) = _rji_ ( _m_ ) for all _i_ and _j_ we find 

**==> picture [233 x 15] intentionally omitted <==**

This is called a _Metropolis algorithm_ . A particularly simple case would be to take 

**==> picture [192 x 14] intentionally omitted <==**

where _Nm_ = _|Sm|_ . This amounts to choosing another value _jm_ at site _m_ uniformly at random; if _πj > πi_ , then we adopt the new value, whereas if _πj ≤ πi_ we adopt the new value with probability _πj/πi_ . 

We have not yet specified a rule for deciding which site to visit when. In practice this may not matter much, provided we keep returning to every site. For definiteness we mention two possibilities. We might choose to visit every site once and then repeat, generating a sequence of sites ( _mn_ ) _n≥_ 0. Then ( _mn, Xn_ ) _n≥_ 0 is a Markov chain in Λ _× I_ . Alternatively, we might choose a site randomly at each step. Then ( _Xn_ ) _n≥_ 0 is itself a Markov chain with transition matrix 

**==> picture [103 x 25] intentionally omitted <==**

We shall stick with this second choice, where the analysis is simpler to present. Let us assume that _P_ is irreducible, which is easy to ensure in the examples. We know that 

**==> picture [99 x 12] intentionally omitted <==**

_5.5 Markov chain Monte Carlo_ 

211 

for all _m_ and all _i, j_ , so also 

**==> picture [62 x 9] intentionally omitted <==**

and so _π_ is the unique invariant measure for _P_ . Hence, by Theorem 1.10.2, we have 

**==> picture [113 x 33] intentionally omitted <==**

as _n →∞_ with probability 1. Thus the algorithm works eventually. In practice one is concerned with how fast it works, but useful information of this type cannot be gained in the present general context. Given more information on the structure of _Sm_ and the distribution _π_ to be simulated, much more can be said. We shall not pursue the matter here. It should also be emphasised that there is an empirical side to simulation: with due caution informed by the theory, the computer output gives a good idea of how well we are doing. For further reading we recommend _Stochastic Simulation_ by B. D. Ripley (Wiley, Chichester, 1987), and _Markov Chain Monte Carlo in practice_ by W. R. Gilks, S. Richardson and D. J. Spiegelhalter (Chapman and Hall, London, 1996). The recent survey article _Bayesian computation and stochastic systems_ by J. Besag, P. Green, D. Higdon and K. Mengersen ( _Statistical Science_ , 10 (1), pp. 3–40, 1995) contains many interesting references. We finish with two examples. 

## **Example 5.5.1 (Bayesian statistics)** 

In a statistical problem one may be presented with a set of independent observations _Y_ 1 _, . . . , Yn_ , which it is reasonable to assume are normally distributed, but with unknown mean _µ_ and variance _τ[−]_[1] . One then seeks to draw conclusions about _µ_ and _τ_ on the basis of the observations. The Bayesian approach to this problem is to assume that _µ_ and _τ_ are themselves random variables, with a given prior distribution. For example, we might assume that 

**==> picture [157 x 14] intentionally omitted <==**

that is to say, _µ_ is normal of mean _θ_ 0 and variance _φ[−]_ 0[1][,][and] _[τ]_[has][gamma] distribution of parameters _α_ 0 and _β_ 0. The parameters _θ_ 0, _φ_ 0, _α_ 0 and _β_ 0 are known. Then the prior density for ( _µ, τ_ ) is given by 

**==> picture [236 x 13] intentionally omitted <==**

The posterior density for ( _µ, τ_ ), which is the conditional density given the observations, is then given by Bayes’ formula 

**==> picture [143 x 12] intentionally omitted <==**

**==> picture [348 x 34] intentionally omitted <==**

_5. Applications_ 

212 

Note that the posterior density is no longer in product form: the conditioning has introduced a dependence between _µ_ and _τ_ . Nevertheless, the _full conditional distributions_ still have a simple form 

**==> picture [358 x 72] intentionally omitted <==**

where 

**==> picture [250 x 33] intentionally omitted <==**

**==> picture [211 x 31] intentionally omitted <==**

Our final belief about _µ_ and _τ_ is regarded as measured by the posterior density. We may wish to compute probabilities and expectations. Here the _Gibbs sampler_ provides a particularly simple approach. Of course, numerical integration would also be feasible as the dimension is only two. To make the connection with our general discussion we set 

**==> picture [126 x 12] intentionally omitted <==**

We wish to simulate _X_ = ( _µ, τ_ ) with density _π_ ( _µ, τ | y_ ). The fact that R and [0 _, ∞_ ) are not finite sets does not affect the basic idea. In any case the computer will work with finite approximations to R and [0 _, ∞_ ). First we simulate _X_ 0, say from the product form density _π_ ( _µ, τ_ ). At the _k_ th stage, given _Xk_ = ( _µk, τk_ ), we first simulate _µk_ +1 from _π_ ( _µ | y, τk_ ) and then _τk_ +1 from _π_ ( _τ | y, µk_ +1), then set _Xk_ +1 = ( _µk_ +1 _, τk_ +1). Then ( _Xk_ ) _k≥_ 0 is a Markov chain in _I_ with invariant measure _π_ ( _µ, τ | y_ ), and one can show that 

**==> picture [217 x 34] intentionally omitted <==**

with probability 1, for all bounded continuous functions _f_ : _I →_ R. This is not an immediate consequence of the ergodic theorem for discrete statespace, but you may find it reasonable at an intuitive level, with a rate of convergence depending on the smoothness of _π_ and _f_ . 

We now turn to an elaboration of this example where the Gibbs sampler is indispensible. The model consists of _m_ copies of the preceding one, with 

_5.5 Markov chain Monte Carlo_ 

213 

different means but a common variance. Thus there are _mn_ independent observations _Yij_ , where _i_ = 1 _, . . . n_ , and _j_ = 1 _, . . . , m_ , normally distributed, with means _µj_ and common variance _τ[−]_[1] . We take these parameters to be independent random variables as before, with 

**==> picture [162 x 14] intentionally omitted <==**

Let us write _µ_ = ( _µ_ 1 _, . . . , µn_ ). The prior density is given by 

**==> picture [268 x 41] intentionally omitted <==**

and the posterior density is given by 

**==> picture [347 x 84] intentionally omitted <==**

Hence the full conditional distributions are 

**==> picture [248 x 14] intentionally omitted <==**

where 

**==> picture [258 x 72] intentionally omitted <==**

We can construct approximate samples from _π_ ( _µ, τ | y_ ), just as in the case _m_ = 1 discussed above, by a Gibbs sampler method. Note that, conditional on _τ_ , the means _µj_ , for _j_ = 1 _, . . . , m_ , remain independent. Thus one can update all the means simultaneously in the Gibbs sampler. This has the effect of speeding convergence to the equilibrium distribution. In cases where _m_ is large, numerical integration of _π_ ( _µ, τ | y_ ) is infeasible, as is direct simulation from the distribution, so the Markov chain approach is the only one available. 

_5. Applications_ 

214 

## **Example 5.5.2 (Ising model and image analysis)** 

Consider a large box Λ = Λ _N_ in Z[2] 

**==> picture [154 x 14] intentionally omitted <==**

with boundary _∂_ Λ = Λ _N \_ Λ _N −_ 1, and the _configuration space_ 

**==> picture [66 x 14] intentionally omitted <==**

For _x ∈_ Λ define 

**==> picture [144 x 17] intentionally omitted <==**

where the sum is taken over all pairs _{m, m[′] } ⊆_ Λ with _|m − m[′] |_ = 1. Note that _H_ ( _x_ ) is small when the values taken by _x_ at neighbouring sites are predominantly the same. We write 

**==> picture [198 x 13] intentionally omitted <==**

and for each _β >_ 0 define a probability distribution � _π_ ( _x_ ) : _x ∈ I_[+][�] by 

**==> picture [78 x 14] intentionally omitted <==**

As _β ↓_ 0 the weighting becomes uniform, whereas, as _β ↑∞_ the mass concentrates on configurations _x_ where _H_ ( _x_ ) is small. This is one of the fundamental models of statistical physics, called the _Ising model_ . A famous and deep result of Onsager says that if _X_ has distribution _π_ , then 

**==> picture [200 x 20] intentionally omitted <==**

In particular, if sinh 2 _β ≤_ 1, the fact that _X_ is forced to take boundary values 1 does not significantly affect the distribution of _X_ (0) when _N_ is large, whereas if sinh 2 _β >_ 1 there is a residual effect of the boundary values on _X_ (0), uniformly in _N_ . 

Here we consider the problem of simulating the Ising model. Simulations may sometimes be used to guide further developments in the theory, or even to detect phenomena quite out of reach of the current theory. In fact, the Ising model is rather well understood theoretically; but there are many related models which are not, where simulation is still possible by simple modifications of the methods presented here. 

First we describe a Gibbs sampler. Consider the sets of even and odd sites 

**==> picture [196 x 31] intentionally omitted <==**

_5.5 Markov chain Monte Carlo_ 

215 

and for _x ∈ I_ set 

**==> picture [114 x 15] intentionally omitted <==**

We can exploit the fact that the conditional distribution _π_ ( _x_[+] _| x[−]_ ) has product form 

**==> picture [160 x 27] intentionally omitted <==**

where, for _m ∈_ Λ[+] _\∂_ Λ 

**==> picture [120 x 27] intentionally omitted <==**

Therefore, it is easy to simulate from _π_ ( _x_[+] _| x[−]_ ) and likewise from _π_ ( _x[−] | x_[+] ). Choose now some simple initial configuration _X_ 0 in _I_[+] . Then inductively, given _Xn[−]_ = _x[−]_ , simulate firstly _Xn_[+] +1[with][distribution] _π_ ( _· | x[−]_ ) and then given _Xn_[+] +1[=] _[x]_[+][,][simulate] _[X] n[−]_ +1[with][distribution] _π_ ( _· | x_[+] ). Then according to our general discussion, for large _n_ , the distribution of _Xn_ is approximately _π_ . Note that we did not use the value of the normalizing constant 

**==> picture [84 x 26] intentionally omitted <==**

which is hard to compute by elementary means when _N_ is large. 

An alternative approach is to use a Metropolis algorithm. We can again exploit the even/odd partition. Given that _Xn_ = _x_ , independently for each _m ∈_ Λ[+] _\∂_ Λ, we change the sign of _Xn_[+][(] _[m]_[)][with][probability] 

**==> picture [212 x 15] intentionally omitted <==**

ˆ ˆ where _x ∼[m] x_ with _x_ ( _m_ ) = _−x_ ( _m_ ). Let us call the resulting configuration _Yn_ . Next we apply the corresponding transformation to _Yn[−]_[(] _[m]_[) for the odd] sites _m ∈_ Λ _[−] \∂_ Λ, to obtain _Xn_ +1. The process ( _Xn_ ) _n≥_ 0 is then a Markov chain in _I_[+] with invariant distribution _π_ . 

Both methods we have described serve to simulate samples from _π_ ; there is little to choose between them. Convergence is fast in the subcritical case sinh 2 _β <_ 1, where _π_ has an approximate product structure on large scales. 

In a Bayesian analysis of two-dimensional images, the Ising model is sometimes used as a prior. We may encode a digitized image on a twodimensional grid as a particular configuration � _x_ ( _m_ ) : _m ∈_ Λ� _∈ I_ , where _x_ ( _m_ ) = 1 for a white pixel and _x_ ( _m_ ) = _−_ 1 for a black pixel. By varying the parameter _β_ in the Ising model, we vary the tendency of black pixels 

_5. Applications_ 

216 

to clump together; the same for white pixels. Thus _β_ is a sort of texture parameter, which we choose according to the sort of image we expect, thus obtaining a prior _π_ ( _x_ ). Observations are now made at each site which record the true pixel, black or white, with probability _p ∈_ (0 _,_ 1). The posterior distribution for _X_ given observations _Y_ is then given by 

**==> picture [248 x 14] intentionally omitted <==**

where _a_ ( _x, y_ ) and _d_ ( _x, y_ ) are the numbers of sites at which _x_ and _y_ agree and disagree respectively. ‘Cleaned-up’ versions of the observed image _Y_ may now be obtained by simulating from the posterior distribution. Although this is not exactly the Ising model, the same methods work. We describe the appropriate Metropolis algorithm: given that _Xn_ = _x_ , independently for each _m ∈_ Λ[+] _\∂_ Λ, change the sign of _Xn_[+][(] _[m]_[)][with][probability] 

**==> picture [214 x 35] intentionally omitted <==**

ˆ _m_ ˆ where _x ∼ x_ with _x_ ( _m_ ) = _−x_ ( _m_ ). Call the resulting configuration _Xn_ +1 _/_ 2. Next apply the corresponding transformation to _Xn[−]_ +1 _/_ 2[for][the][odd][sites] to obtain _Xn_ +1. Then ( _Xn_ ) _n≥_ 0 is a Markov chain in _I_[+] with invariant distribution _π_ ( _· | y_ ). 

**6** 

## and measure Appendix: probability 

Section 6.1 contains some reminders about countable sets and the discrete version of measure theory. For much of the book we can do without explicit mention of more general aspects of measure theory, except an elementary understanding of Riemann integration or Lebesgue measure. This is because the state-space is at worst countable. The proofs we have given may be read on two levels, with or without a measure-theoretic background. When interpreted in terms of measure theory, the proofs are intended to be rigorous. The basic framework of measure and probability is reviewed in Sections 6.2 and 6.3. Two important results of measure theory, the monotone convergence theorem and Fubini’s theorem, are needed a number of times: these are discussed in Section 6.4. One crucial result which we found impossible to discuss convincingly without measure theory is the strong Markov property for continuous-time chains. This is proved in Section 6.5. Finally, in Section 6.6, we discuss a general technique for determining probability measures and independence in terms of _π_ -systems, which are often more convenient than _σ_ -algebras. 

## **6.1 Countable sets and countable sums** 

A set _I_ is _countable_ if there is a bijection _f_ : _{_ 1 _, . . . , n} → I_ for some _n ∈_ N, or a bijection _f_ : N _→ I_ . In either case we can _enumerate_ all the elements of _I_ 

**==> picture [59 x 11] intentionally omitted <==**

_6. Appendix: probability and measure_ 

218 

where in one case the sequence terminates and in the other it does not. There would have been no loss in generality had we insisted that all our Markov chains had state-space N or _{_ 1 _, . . . , n}_ for some _n ∈_ N: this just corresponds to a particular choice of the bijection _f_ . 

Any subset of a countable set is countable. Any finite cartesian product of countable sets is countable, for example Z _[n]_ for any _n_ . Any countable union of countable sets is countable. The set of all subsets of N is uncountable and so is the set of real numbers R. 

We need the following basic fact. 

**Lemma 6.1.1.** _Let I be a countably infinite set and let λi ≥_ 0 _for all i ∈ I. Then, for any two enumerations of I_ 

**==> picture [61 x 28] intentionally omitted <==**

_we have_ 

**==> picture [87 x 31] intentionally omitted <==**

_Proof._ Given any _N ∈_ N we can find _M ≥ N_ and _N[′] ≥ M_ such that 

**==> picture [213 x 12] intentionally omitted <==**

Then 

**==> picture [130 x 34] intentionally omitted <==**

and the result follows on letting _N →∞_ . 

Since the value of the sum does not depend on the enumeration we are justified in using a notation which does not specify an enumeration and write simply 

**==> picture [32 x 25] intentionally omitted <==**

More generally, if we allow _λi_ to take negative values, then we can set 

**==> picture [170 x 35] intentionally omitted <==**

where 

**==> picture [113 x 14] intentionally omitted <==**

_6.1 Countable sets and countable sums_ 

219 

allowing that the sum over _I_ is undefined when the sums over _I_[+] and _I[−]_ are both infinite. There is no difficulty in showing for _λi, µi ≥_ 0 that 

**==> picture [146 x 25] intentionally omitted <==**

By induction, for any finite set _J_ and for _λij ≥_ 0, we have 

**==> picture [156 x 40] intentionally omitted <==**

The following two results on sums are simple versions of fundamental results for integrals. We take the opportunity to prove these simple versions in order to convey some intuition relevant to the general case. 

**Lemma 6.1.2 (Fubini’s theorem – discrete case).** _Let I and J be countable sets and let λij ≥_ 0 _for all i ∈ I and j ∈ J . Then_ 

**==> picture [156 x 40] intentionally omitted <==**

_Proof._ Let _j_ 1 _, j_ 2 _, j_ 3 _, . . ._ be an enumeration of _J_ . Then 

**==> picture [320 x 40] intentionally omitted <==**

as _n →∞_ . Hence 

**==> picture [151 x 40] intentionally omitted <==**

and the result follows by symmetry. 

**Lemma 6.1.3 (Monotone convergence – discrete case).** _Suppose for each i ∈ I we are given an increasing sequence_ ( _λi_ ( _n_ )) _n≥_ 0 _with limit λi, and that λi_ ( _n_ ) _≥_ 0 _for all i and n. Then_ 

**==> picture [145 x 25] intentionally omitted <==**

_6. Appendix: probability and measure_ 

220 

_Proof._ Set _δi_ (1) = _λi_ (1) and for _n ≥_ 2 set 

**==> picture [125 x 12] intentionally omitted <==**

Then _δi_ ( _n_ ) _≥_ 0 for all _i_ and _n_ , so as _n →∞_ , by Fubini’s theorem 

**==> picture [222 x 111] intentionally omitted <==**

## **6.2 Basic facts of measure theory** 

We state here for easy reference the basic definitions and results of measure theory. Let _E_ be a set. A _σ_ - _algebra E_ on _E_ is a set of subsets of _E_ satisfying (i) _∅∈E_ ; 

(ii) _A ∈E ⇒ A[c] ∈E_ ; 

(iii) ( _An ∈E, n ∈_ N) _⇒_[�] _n[A][n][∈E]_[.] 

Here _A[c]_ denotes the complement _E\A_ of _A_ in _E_ . Thus _E_ is closed under countable set operations. The pair ( _E, E_ ) is called a _measurable space_ . A _measure µ_ on ( _E, E_ ) is a function _µ_ : _E →_ [0 _, ∞_ ] which has the following _countable additivity_ property: 

**==> picture [270 x 34] intentionally omitted <==**

The triple ( _E, E, µ_ ) is called a _measure space_ . If there exist sets _En ∈E_ , _n ∈_ N with[�] _n[E][n]_[=] _[ E]_[and] _[µ]_[(] _[E][n]_[)] _[ <][ ∞]_[for][all] _[n]_[,][then][we][say] _[µ]_[is] _[σ]_[-] _[finite]_[.] 

## **Example 6.2.1** 

Let _I_ be a countable set and denote by _I_ the set of all subsets of _I_ . Recall that _λ_ = ( _λi_ : _i ∈ I_ ) is a measure in the sense of Section 1.1 if _λi ∈_ [0 _, ∞_ ) for all _i_ . For such _λ_ we obtain a measure on the measurable space ( _I, I_ ) by setting 

**==> picture [70 x 25] intentionally omitted <==**

In fact, we obtain in this way all _σ_ -finite measures _µ_ on ( _I, I_ ). 

_6.2 Basic facts of measure theory_ 

221 

## **Example 6.2.2** 

Let _A_ be any set of subsets of _E_ . The set of all subsets of _E_ is a _σ_ - algebra containing _A_ . The intersection of any collection of _σ_ -algebras is again a _σ_ -algebra. The collection of _σ_ -algebras containing _A_ is therefore non-empty and its intersection is a _σ_ -algebra _σ_ ( _A_ ), which is called the _σ_ -algebra _generated by A_ . 

## **Example 6.2.3** 

In the preceding example take _E_ = R and 

**==> picture [138 x 12] intentionally omitted <==**

The _σ_ -algebra _B_ generated by _A_ is called the _Borel σ-algebra_ of R. It can be shown that there is a unique measure _µ_ on (R _, B_ ) such that 

**==> picture [142 x 12] intentionally omitted <==**

This measure _µ_ is called _Lebesgue measure_ . 

Let ( _E_ 1 _, E_ 1) and ( _E_ 2 _, E_ 2) be measurable spaces. A function _f_ : _E_ 1 _→ E_ 2 is _measurable_ if _f[−]_[1] ( _A_ ) _∈E_ 1 whenever _A ∈E_ 2. When the range _E_ 2 = R we take _E_ 2 = _B_ by default. When the range _E_ 2 is a countable set _I_ we take _E_ 2 to be the set of all subsets _I_ by default. 

Let ( _E, E_ ) be a measurable space. We denote by _mE_ the set of measurable functions _f_ : _E →_ R. Then _mE_ is a vector space. We denote by _mE_[+] the set of measurable functions _f_ : _E →_ [0 _, ∞_ ], where we take on [0 _, ∞_ ] the _σ_ -algebra generated by the open intervals ( _a, b_ ). Then _mE_[+] is a cone 

**==> picture [203 x 13] intentionally omitted <==**

Also, _mE_[+] is closed under countable suprema: 

**==> picture [168 x 19] intentionally omitted <==**

It follows that, for a sequence of functions _fn ∈ mE_[+] , both lim sup _n fn_ and lim inf _n fn_ are in _mE_[+] , and so is lim _n fn_ when this exists. It can be shown � that there is a unique map _µ_ : _mE_[+] _→_ [0 _, ∞_ ] such that 

(i) _µ_ �(1 _A_ ) = _µ_ ( _A_ ) for all _A ∈E_ ; 

**==> picture [296 x 12] intentionally omitted <==**

**==> picture [241 x 14] intentionally omitted <==**

_6. Appendix: probability and measure_ 

222 

For _f ∈ mE_ , set _f[±]_ = ( _±f_ ) _∨_ 0, then _f_[+] _, f[−] ∈ mE_[+] , _f_ = _f_[+] _− f[−]_ and _|f |_ = _f_[+] + _f[−]_ . If _µ_ �( _|f |_ ) _< ∞_ then _f_ is said to be _integrable_ and we set 

**==> picture [112 x 13] intentionally omitted <==**

� We call _µ_ ( _f_ ) the _integral_ of _f_ . It is conventional to drop the tilde and denote the integral by one of the following alternative notations: 

**==> picture [164 x 27] intentionally omitted <==**

In the case of Lebesgue measure _µ_ , one usually writes simply 

**==> picture [63 x 27] intentionally omitted <==**

## **6.3 Probability spaces and expectation** 

The basic apparatus for modelling randomness is a _probability space_ (Ω _, F ,_ P). This is simply a measure space with total mass P(Ω) = 1. Thus _F_ is a _σ_ -algebra of subsets of Ωand P : _F →_ [0 _,_ 1] satisfies 

- (i) P(Ω) = 1; 

- (ii) P( _A_ 1 _∩ A_ 2) = P( _A_ 1) + P( _A_ 2) for _A_ 1 _, A_ 2 disjoint; 

- (iii) P( _An_ ) _↑_ P( _A_ ) whenever _An ↑ A_ . 

In (iii) we write _An ↑ A_ to mean _A_ 1 _⊆ An ⊆ . . ._ with[�] _n[A][n]_[=] _[A]_[.][A] measurable function _X_ defined on (Ω _, F_ ) is called a _random variable_ . We use random variables _Y_ : Ω _→_ R to model random quantities, where for a Borel set _B ⊆_ R the probability that _Y ∈ B_ is given by 

**==> picture [156 x 14] intentionally omitted <==**

Similarly, given a countable state-space _I_ , a random variable _X_ : Ω _→ I_ models a random state, with _distribution_ 

**==> picture [175 x 14] intentionally omitted <==**

To every non-negative or integrable real-valued random variable _Y_ is associated an average value or _expectation_ E( _Y_ ), which is the integral of _Y_ with respect to P. Thus we have 

- (i) E(1 _A_ ) = P( _A_ ) for _A ∈F_ ; 

- (ii) E( _αX_ + _βY_ ) = _α_ E( _X_ ) + _β_ E( _Y_ ) for _X, Y ∈ mF_[+] , _α, β ≥_ 0; 

_6.4 Monotone convergence and Fubini’s theorem_ 

223 

(iii) ( _Yn ∈ mF_[+] _, n ∈_ N _, Yn ↑ Y_ ) _⇒_ E( _Yn_ ) _↑_ E( _Y_ ). When _X_ is a random variable with values in _I_ and _f_ : _I →_ [0 _, ∞_ ] the expectation of _Y_ = _f_ ( _X_ ) = _f ◦ X_ is given explicitly by 

**==> picture [94 x 25] intentionally omitted <==**

where _λ_ is the distribution of _X_ . For a real-valued random variable _Y_ the probabilities are sometimes given by a measurable _density_ function _ρ_ in terms of Lebesgue measure: 

**==> picture [112 x 26] intentionally omitted <==**

Then for any measurable function _f_ : R _→_ [0 _, ∞_ ] there is an explicit formula 

**==> picture [127 x 26] intentionally omitted <==**

## **6.4 Monotone convergence and Fubini’s theorem** 

Here are the two theorems from measure theory that come into play in the main text. First we shall state the theorems, then we shall discuss some places where they are used. Proofs may be found, for example, in _Probability with Martingales_ by D. Williams (Cambridge University Press, 1991). 

**Theorem 6.4.1 (Monotone convergence).** _Let_ ( _E, E, µ_ ) _be a measure space and let_ ( _fn_ ) _n≥_ 1 _be a sequence of non-negative measurable functions. Then, as n →∞_ 

**==> picture [214 x 14] intentionally omitted <==**

**Theorem 6.4.2 (Fubini’s theorem).** _Let_ ( _E_ 1 _, E_ 1 _, µ_ 1) _and_ ( _E_ 2 _, E_ 2 _, µ_ 2) _be two σ-finite measure spaces. Suppose that f_ : _E_ 1 _× E_ 2 _→_ [0 _, ∞_ ] _satisfies_ 

- (i) _x �→ f_ ( _x, y_ ) : _E_ 1 _→_ [0 _, ∞_ ] _is E_ 1 _measurable for all y ∈ E_ 2 _;_ 

- (ii) _y �→_[�] _x∈E_ 1 _[f]_[(] _[x, y]_[)] _[µ]_[1][(] _[dx]_[) :] _[ E]_[2] _[→]_[[0] _[,][ ∞]_[]] _[is][E]_[2] _[measurable.]_ 

- _Then_ 

**==> picture [353 x 61] intentionally omitted <==**

_6. Appendix: probability and measure_ 

224 

The measurability conditions in the above theorems rarely need much consideration. They are powerful results and very easy to use. There is an equivalent formulation of monotone convergence in terms of sums: for non-negative measurable functions _gn_ we have 

**==> picture [116 x 31] intentionally omitted <==**

To see this just take _fn_ = _g_ 1 + _· · ·_ + _gn_ . This form of monotone convergence has already appeared in Section 6.2 as a defining property of the integral. This is also a special case of Fubini’s theorem, provided that ( _E, E, µ_ ) is _σ_ -finite: just take _E_ 2 = _{_ 1 _,_ 2 _,_ 3 _, . . . }_ and _µ_ 2( _{n}_ ) = 1 for all _n_ . 

We used monotone convergence in Theorem 1.10.1 to see that for a nonnegative random variable _Y_ we have 

**==> picture [117 x 17] intentionally omitted <==**

We used monotone convergence in Theorem 2.3.2 to see that for random variables _Sn ≥_ 0 we have 

**==> picture [112 x 26] intentionally omitted <==**

and 

**==> picture [232 x 60] intentionally omitted <==**

In the last application convergence is not monotone increasing but monotone decreasing. But if 0 _≤ Xn ≤ Y_ and _Xn ↓ X_ then _Y − Xn ↑ Y − X_ . So E( _Y − Xn_ ) _↑_ E( _Y − X_ ) and if E( _Y_ ) _< ∞_ we can deduce E( _Xn_ ) _↓_ E( _X_ ). Fubini’s theorem is used in Theorem 3.4.2 to see that 

**==> picture [261 x 27] intentionally omitted <==**

Thus we have taken ( _E_ 1 _, E_ 1 _, µ_ 1) to be [0 _, ∞_ ) with Lebesgue measure and ( _E_ 2 _, E_ 2 _, µ_ 2) to be the probability space with the measure P _i_ . 

## **6.5 Stopping times and the strong Markov property** 

The strong Markov property for continuous-time Markov chains cannot properly be understood without measure theory. The problem lies with 

_6.5 Stopping times and the strong Markov property_ 

225 

the notion of ‘depending only on’, which in measure theory is made precise as measurability with respect to some _σ_ -algebra. Without measure theory the statement that a set _A_ depends only on ( _Xs_ : _s ≤ t_ ) does not have a precise meaning. Of course, if the dependence is reasonably explicit we can exhibit it, but then, in general, in what terms would you require the dependence to be exhibited? So in this section we shall give a precise measure-theoretic account of the strong Markov property. 

Let ( _Xt_ ) _t≥_ 0 be a right-continuous process with values in a countable set _I_ . Denote by _Ft_ the _σ_ -algebra generated by _{Xs_ : _s ≤ t}_ , that is to say, by all sets _{Xs_ = _i}_ for _s ≤ t_ and _i ∈ I_ . We say that a random variable _T_ with values in [0 _, ∞_ ] is a _stopping time_ of ( _Xt_ ) _t≥_ 0 if _{T ≤ t} ∈Ft_ for all _t ≥_ 0. Note that this certainly implies 

**==> picture [244 x 24] intentionally omitted <==**

We define for stopping times _T_ 

**==> picture [228 x 14] intentionally omitted <==**

This turns out to be the correct way to make precise the notion of sets which ‘depend only on _{Xt_ : _t ≤ T }_ ’. 

**Lemma 6.5.1.** _Let S and T be stopping times of_ ( _Xt_ ) _t≥_ 0 _. Then both XT and {S ≤ T } are FT -measurable._ 

_Proof._ Since ( _Xt_ ) _t≥_ 0 is right-continuous, on _{T < t}_ there exists an _n ≥_ 0 such that for all _m ≥ n_ , for some _k ≥_ 1, ( _k −_ 1)2 _[−][m] ≤ T < k_ 2 _[−][m] ≤ t_ and _Xk_ 2 _−m_ = _XT_ . Hence 

**==> picture [348 x 71] intentionally omitted <==**

so _XT_ is _FT_ -measurable. 

We have 

**==> picture [262 x 26] intentionally omitted <==**

so _{S > T } ∈FT_ , and so _{S ≤ T } ∈FT_ . 

_6. Appendix: probability and measure_ 

226 

**Lemma 6.5.2.** _For all m ≥_ 0 _, the jump time Jm is a stopping time of_ ( _Xt_ ) _t≥_ 0 _._ 

_Proof._ Obviously, _J_ 0 = 0 is a stopping time. Assume inductively that _Jm_ is a stopping time. Then 

**==> picture [246 x 26] intentionally omitted <==**

for all _t ≥_ 0, so _Jm_ +1 is a stopping time and the induction proceeds. 

We denote by _Gm_ the _σ_ -algebra generated by _Y_ 0 _, . . . , Ym_ and _S_ 1 _, . . . , Sm_ , that is, by events of the form _{Yk_ = _i}_ for _k ≤ m_ and _i ∈ I_ or of the form _{Sk > s}_ for _k ≤ m_ and _s >_ 0. 

**Lemma 6.5.3.** _Let T be a stopping time of_ ( _Xt_ ) _t≥_ 0 _and let A ∈FT . Then for all m ≥_ 0 _there exist a random variable Tm and a set Am, both measurable with respect to Gm, such that T_ = _Tm and_ 1 _A_ = 1 _Am on {T < Jm_ +1 _}._ 

_Proof._ Fix _t ≥_ 0 and consider 

_At_ = _{A ∈Ft_ : _A ∩{t < Jm_ +1 _}_ = _Am ∩{t < Jm_ +1 _}_ for some _Am ∈Gm}._ 

Since _Gm_ is a _σ_ -algebra, so is _At_ . For _s ≤ t_ we have 

**==> picture [328 x 51] intentionally omitted <==**

so _{Xs_ = _i} ∈At_ . Since these sets generate _Ft_ , this implies that _At_ = _Ft_ . For _T_ a stopping time and _A ∈FT_ we have _B_ ( _t_ ) := _{T ≤ t} ∈Ft_ and _A_ ( _t_ ) := _A ∩{T ≤ t} ∈Ft_ for all _t ≥_ 0. So we can find _Bm_ ( _t_ ), _Am_ ( _t_ ) _∈Gm_ such that 

**==> picture [212 x 29] intentionally omitted <==**

Set 

**==> picture [176 x 25] intentionally omitted <==**

then _Tm_ and _Am_ are _Gm_ -measurable and 

**==> picture [220 x 51] intentionally omitted <==**

_6.5 Stopping times and the strong Markov property_ 

227 

and 

**==> picture [275 x 57] intentionally omitted <==**

as required. 

**Theorem 6.5.4 (Strong Markov property).** _Let_ ( _Xt_ ) _t≥_ 0 _be Markov_ ( _λ, Q_ ) _and let T be a stopping time of_ ( _Xt_ ) _t≥_ 0 _. Then, conditional on T < ζ and XT_ = _i,_ ( _XT_ + _t_ ) _t≥_ 0 _is Markov_ ( _δi, Q_ ) _and independent of FT ._ 

_Proof._ On _{T < ζ}_ set _X_[�] _t_ = _XT_ + _t_ and denote by ( _Y_[�] _n_ ) _n≥_ 0 the jump chain and by ( _S_[�] _n_ ) _n≥_ 1 the holding times of ( _X_[�] _t_ ) _t≥_ 0. We have to show that, for all _A ∈FT_ , all _i_ 0 _, . . . , in ∈ I_ and all _s_ 1 _, . . . , sn ≥_ 0 

**==> picture [351 x 51] intentionally omitted <==**

It suffices to prove this with _{T < ζ}_ replaced by _{Jm ≤ T < Jm_ +1 _}_ for all _m ≥_ 0 and then sum over _m_ . By Lemmas 6.5.1 and 6.5.2, _{Jm ≤ T } ∩{XT_ = _i} ∈FT_ so we may assume without loss of generality that _A ⊆{Jm ≤ T } ∩{XT_ = _i}_ . By Lemma 6.5.3 we can write _T_ = _Tm_ and 1 _A_ = 1 _Am_ on _{T < Jm_ +1 _}_ , where _Tm_ and _Am_ are _Gm_ -measurable. 

**==> picture [312 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
S ˜1 S ˜2<br>Sm +1 Sm +2<br>0 Jm T Jm +1 Jm +2<br>**----- End of picture text -----**<br>


On _{Jm ≤ T < Jm_ +1 _}_ we have, as shown in the diagram 

**==> picture [301 x 15] intentionally omitted <==**

_6. Appendix: probability and measure_ 

228 

Now, conditional on _Ym_ = _i_ , _Sm_ +1 is independent of _Gm_ and hence of _Tm − Jm_ and _Am_ and, by the memoryless property of the exponential 

**==> picture [358 x 14] intentionally omitted <==**

Hence, by the Markov property of the jump chain 

**==> picture [312 x 106] intentionally omitted <==**

as required. 

## **6.6 Uniqueness of probabilities and independence of** _σ_ **-algebras** 

For both discrete-time and continuous-time Markov chains we have given definitions which specify the probabilities of certain events determined by the process. From these specified probabilities we have often deduced explicitly the values of other probabilities, for example hitting probabilities. In this section we shall show, in measure-theoretic terms, that our definitions determine the probabilities of _all_ events depending on the process. The constructive approach we have taken should make this seem obvious, but it is illuminating to see what has to be done. 

Let Ωbe a set. A _π_ - _system A_ on Ωis a collection of subsets of Ωwhich is closed under finite intersections; thus 

**==> picture [135 x 11] intentionally omitted <==**

We denote as usual by _σ_ ( _A_ ) the _σ_ -algebra generated by _A_ . If _σ_ ( _A_ ) = _F_ we say that _A generates F_ . 

**Theorem 6.6.1.** _Let_ (Ω _, F_ ) _be a measurable space. Let_ P1 _and_ P2 _be probability measures on_ (Ω _, F_ ) _which agree on a π-system A generating F . Then_ P1 = P2 _._ 

_Proof._ Consider 

**==> picture [150 x 12] intentionally omitted <==**

_6.6 Uniqueness of probabilities and independence of σ-algebras_ 229 

We have assumed that _A ⊆D_ . Moreover, since P1 and P2 are probability measures, _D_ has the following properties: 

- (i) Ω _∈D_ ; 

(ii) ( _A, B ∈D_ and _A ⊆ B_ ) _⇒ B\A ∈D_ ; 

(iii) ( _An ∈D, An ↑ A_ ) _⇒ A ∈D_ . 

Any collection of subsets having these properties is called a _d_ - _system_ . Since _A_ generates _F_ , the result now follows from the following lemma. 

**Lemma 6.6.2 (Dynkin’s** _π_ **-system lemma).** _Let A be a π-system and let D be a d-system. Suppose A ⊆D. Then σ_ ( _A_ ) _⊆D._ 

_Proof._ Any intersection of _d_ -systems is again a _d_ -system, so we may without loss assume that _D_ is the smallest _d_ -system containing _A_ . You may easily check that any _d_ -system which is also a _π_ -system is necessarily a _σ_ -algebra, so it suffices to show _D_ is a _π_ -system. This we do in two stages. 

Consider 

**==> picture [201 x 12] intentionally omitted <==**

Since _A_ is a _π_ -system, _A ⊆D_ 1. You may easily check that _D_ 1 is a _d_ -system – because _D_ is a _d_ -system. Since _D_ is the smallest _d_ -system containing _A_ , this shows _D_ 1 = _D_ . 

Next consider 

**==> picture [201 x 12] intentionally omitted <==**

Since _D_ 1 = _D_ , _A ⊆D_ 2. You can easily check that _D_ 2 is also a _d_ -system. Hence also _D_ 2 = _D_ . But this shows _D_ is a _π_ -system. 

The notion of independence used in advanced probability is the independence of _σ_ -algebras. Suppose that (Ω _, F ,_ P) is a probability space and _F_ 1 and _F_ 2 are sub- _σ_ -algebras of _F_ . We say that _F_ 1 and _F_ 2 are _independent_ if 

**==> picture [266 x 12] intentionally omitted <==**

The usual means of establishing such independence is the following corollary of Theorem 6.6.1. 

**Theorem 6.6.3.** _Let A_ 1 _be a π-system generating F_ 1 _and let A_ 2 _be a π-system generating F_ 2 _. Suppose that_ 

**==> picture [268 x 12] intentionally omitted <==**

_Then F_ 1 _and F_ 2 _are independent._ 

_6. Appendix: probability and measure_ 

230 

_Proof._ There are two steps. First fix _A_ 2 _∈A_ 2 with P( _A_ 2) _>_ 0 and consider the probability measure 

**==> picture [88 x 14] intentionally omitted <==**

We� have assumed that P[�] ( _A_ ) = P( _A_ ) for all _A ∈A_ 1, so, by Theorem 6.6.1, P = P on _F_ 1. Next fix _A_ 1 _∈F_ 1 with P( _A_ 1) _>_ 0 and consider the probability measure 

**==> picture [88 x 18] intentionally omitted <==**

We showed in the first step that P[��] ( _A_ ) = P( _A_ ) for all _A ∈A_ 2, so, by Theorem 6.6.1, P[��] = P on _F_ 2. Hence _F_ 1 and _F_ 2 are independent. 

We now review some points in the main text where Theorems 6.6.1 and 6.6.3 are relevant. 

In Theorem 1.1.1 we showed that our definition of a discrete-time Markov chain ( _Xn_ ) _n≥_ 0 with initial distribution _λ_ and transition matrix _P_ determines the probabilities of all events of the form 

**==> picture [118 x 12] intentionally omitted <==**

But subsequently we made explicit calculations for probabilities of events which were not of this form – such as the event that ( _Xn_ ) _n≥_ 0 visits a set of states _A_ . We note now that the events _{X_ 0 = _i_ 0 _, . . . , Xn_ = _in}_ form a _π_ -system which generates the _σ_ -algebra _σ_ ( _Xn_ : _n ≥_ 0). Hence, by Theorem 6.6.1, our definition determines (in principle) the probabilities of all events in this _σ_ -algebra. 

In our general discussion of continuous-time random processes in Section 2.2 we claimed that for a right-continuous process ( _Xt_ ) _t≥_ 0 the probabilities of events of the form 

**==> picture [123 x 14] intentionally omitted <==**

for all _n ≥_ 0 determined the probabilities of all events depending on ( _Xt_ ) _t≥_ 0. Now events of the form _{Xt_ 0 = _i_ 0 _, . . . , Xtn_ = _in}_ form a _π_ -system which generates the _σ_ -algebra _σ_ ( _Xt_ : _t ≥_ 0). So Theorem 6.6.1 justifies (a precise version) of this claim. The point about right-continuity is that without such an assumption an event such as 

**==> picture [115 x 12] intentionally omitted <==**

which might reasonably be considered to depend on ( _Xt_ ) _t≥_ 0, is _not necessarily measurable_ with respect to _σ_ ( _Xt_ : _t ≥_ 0). An argument given in 

_6.6 Uniqueness of probabilities and independence of σ-algebras_ 231 

Section 2.2 shows that this event _is_ measurable in the right-continuous case. We conclude that, without some assumption like right-continuity, general continuous-time processes are unreasonable. 

Consider now the method of describing a minimal right-continuous process ( _Xt_ ) _t≥_ 0 via its jump process ( _Yn_ ) _n≥_ 0 and holding times ( _Sn_ ) _n≥_ 1. Let us take _F_ = _σ_ ( _Xt_ : _t ≥_ 0). Then Lemmas 6.5.1 and 6.5.2 show that ( _Yn_ ) _n≥_ 0 and ( _Sn_ ) _n≥_ 1 are _F_ -measurable. Thus _G ⊆F_ where 

**==> picture [124 x 14] intentionally omitted <==**

On the other hand, for all _i ∈ I_ 

**==> picture [231 x 26] intentionally omitted <==**

so also _F ⊂G_ . 

A useful _π_ -system generating _G_ is given by sets of the form 

**==> picture [242 x 12] intentionally omitted <==**

Our jump chain/holding time definition of the continuous-time chain ( _Xt_ ) _t≥_ 0 with initial distribution _λ_ and generator matrix _Q_ may be read as stating that, for such events 

**==> picture [222 x 12] intentionally omitted <==**

Then, by Theorem 6.6.1, this definition determines P on _G_ and hence on _F_ . 

Finally, we consider the strong Markov property, Theorem 6.5.4. Assume that ( _Xt_ ) _t≥_ 0 is Markov( _λ, Q_ ) and that _T_ is a stopping time of ( _Xt_ ) _t≥_ 0. On the set Ω=[�] _{T < ζ}_ define _X_[�] _t_ = _XT_ + _t_ and let _F_[�] = _σ_ ( _X_[�] _t_ : _t ≥_ 0); write ( _Y_[�] _n_ ) _n≥_ 0 and ( _S_[�] _n_ ) _n≥_ 0 for the jump chain and holding times of ( _X_[�] _t_ ) _t≥_ 0 and set 

**==> picture [124 x 16] intentionally omitted <==**

Thus _F_[�] and _G_[�] are _σ_ -algebras on Ω,[�] and coincide by the same argument as for _F_ = _G_ . Set 

**==> picture [242 x 15] intentionally omitted <==**

Then the conclusion of the strong Markov property states that 

**==> picture [144 x 14] intentionally omitted <==**

with _B_ as above, and that 

**==> picture [334 x 14] intentionally omitted <==**

for all _C_[�] _∈ F_[�] and _A ∈FT_ . By Theorem 6.6.3 it suffices to prove the independence assertion for the case _C_[�] = _B_[�] , which is what we did in the proof of Theorem 6.5.4. 

## Further reading 

We gather here the references for further reading which have appeared in the text. This may provide a number of starting points for your exploration of the vast literature on Markov processes and their applications. 

- J. Besag, P. Green, D. Higdon and K. Mengersen, Bayesian computation and stochastic systems, _Statistical Science_ **10 (1)** (1995), 3–40. 

- K.L. Chung, _Markov Chains with Stationary Transition Probabilities,_ Springer, Berlin, 2nd edition, 1967. 

- P.G. Doyle and J.L. Snell, _Random Walks and Electrical Networks_ , Carus Mathematical Monographs 22, Mathematical Association of America, 1984. 

- W.J. Ewens, _Mathematical Population Genetics_ , Springer, Berlin, 1979. 

- D. Freedman, _Markov Chains_ , Holden–Day, San Francisco, 1971. 

- W.R. Gilks, S. Richardson and D.J. Spiegelhalter, _Markov Chain Monte Carlo in Practice_ , Chapman and Hall, London, 1996. 

- T.E. Harris, _The Theory of Branching Processes_ , Dover, New York, 1989. 

- F.P. Kelly, _Reversibility and Stochastic Networks_ , Wiley, Chichester, 1978. 

- D. Revuz, _Markov Chains_ , North-Holland, Amsterdam, 1984. 

- B.D. Ripley, _Stochastic Simulation_ , Wiley, Chichester, 1987. 

- L.C.G. Rogers and D. Williams, _Diffusions, Markov Processes and Martingales, Vol 1: Foundations_ , Wiley, Chichester, 2nd edition, 1994. 

- S.M. Ross, _Applied Probability Models with Optimization Applications_ , Holden–Day, San Francisco, 1970. 

_Further reading_ 

233 

- D.W. Stroock, _Probability Theory – An Analytic View_ , Cambridge University Press, 1993. 

- H.C. Tijms, _Stochastic Models – an Algorithmic Approach_ , Wiley, Chichester, 1994. 

- D. Williams, _Probability with Martingales_ , Cambridge University Press, 1991. 

## Index 

absorbing state 11, 111 absorption probability 12, 112 action 198 adapted 129 alleles 175 aperiodicity 40 average number of customers 181 

backward equation 62, 96 Bayesian statistics 211 biological models 6, 9, 16, 82, 170 birth process 81 infinitesimal definition 85 jump chain/holding time definition 85 transition probability definition 85 birth-and-death chain 16 boundary 138 boundary theory for Markov chains 147 branching process 171 with immigration 179 Brownian motion 159 as limit of random walks 164 existence 161 in R _[d]_ 165 

scaling invariance 165 starting from _x_ 165 transition density 166 busy period 181 

capacity 151 central limit theorem 160 charge 151 closed class 11, 111 closed migration process 184 communicating class 11, 111 conditional expectation 129 conductivity 151 continuous-time Markov chains 87 construction 89 infinitesimal definition 94 jump chain/holding time definition 94, 97 transition probability definition 94, 97 continuous-time random process 67 convergence to equilibrium 41, 121, 168 countable set 217 coupling method 41 current 151 

_Index_ 

235 

detailed balance 48, 124 discounted value function 202 distribution 1 

E, expectation 222 _E_ ( _λ_ ), exponential distribution of parameter _λ_ 70 _e[Q]_ , exponential of _Q_ 62 effective conductivity 156 electrical network 151 energy 154 epidemic model 173 equilibrium distribution 33, 117 ergodic theorem 53, 126, 168 Erlang’s formula 183 excursions 24 expectation 222 expected hitting time 12, 113 expected return time 37, 118 explosion for birth processes 83 for continuous-time chains 90 explosion time 69 explosive _Q_ -matrix 91 exponential distribution 70 

_Fn_ , filtration 129 fair price 135 filtration 129 finite-dimensional distributions 67 first passage decomposition 28 first passage time 19, 115 flow 151 forward equation 62, 100 for birth processes 84 for Poisson process 78 Fubini’s theorem 223 discrete case 219 full conditional distributions 212 fundamental solution 145 

_γi[j]_[,][expected][time][in] _[i]_[between][visits] to _j_ 35 Galton–Watson process 171 gambling 131 Gaussian distribution 160 generator 166 generator matrix 94, 97 

Gibbs sampler 210 gravity 134, 169 Green matrix 144, 145 harmonic function 146 Hastings algorithm 210 hitting probability 12 hitting time 12, 111 holding times 69 

_I_ , state-space 2 infective 173 integrable 129, 222 integral form of the backward equation 98 integral form of the forward equation 101 inter-arrival times 180 invariant distribution 33, 117 computation of 40 irreducibility 11, 111 Ising model 214 jump chain 69 jump matrix 87 jump times 69 last exit time 20 long-run proportion of time 53, 126 _mi_ , expected return time 37, 118 _µ[j] i_[,][expected][time][in] _[i]_[between][visits] to _j_ 118 Markov( _λ, P_ ) 2 Markov( _λ, Q_ ) 94, 97 Markov chain continuous-time 88 discrete-time 2 Markov chain Monte Carlo 206, 208 Markov decision process 197 expected total cost 198 expected total discounted cost 202 long-run average costs 204 Markov property 3 for birth processes 84 for continuous-time chains 93 for Poisson process 75 martingale 129, 141, 176, 204 

_Index_ 

236 

associated to a Markov chain 132 associated to Brownian motion 169 matrix exponentials 105 maximum likelihood estimate 56 measure 1 memoryless property 70 Metropolis algorithm 210 minimal non-negative solution 13 minimal process 69 monotone convergence 223 discrete case 219 Moran model 177 mutation 6, 176 

non-minimal chains 103 null recurrence 37, 118 

_o_ ( _t_ ) _, O_ ( _t_ ), order notation 63 Ohm’s law 151 open migration process 185 optional stopping theorem 130 

P, probability 222 _P_ �, transition matrix 2 _P_ , transition matrix of reversed chain 47 _P_ �( _t_ ), transition semigroup 96 _P_ ( _t_ ), semigroup of reversed chain 124 _p_[(] _ij[n]_[)][,] _[n]_[-step][transition][probability][5] Π, jump matrix 87 _π_ -system 228 Poisson process 74 infinitesimal definition 76 jump chain/holding time definition 76 transition probability definition 76 policy 198 policy improvement 201 population genetics 175 population growth 171 positive recurrence 37, 118 potential 138 associated to a Markov chain 138 associated to Brownian motion 169 

gravitational 134 in electrical networks 151 with discounted costs 142 potential theory 134 probability generating function 171 probability measure 222 probability space 222 _Q_ �-matrix 60 _Q_ , generator matrix of reversed chain 124 _qi_ , rate of leaving _i_ 61 _qij_ , rate of going from _i_ to _j_ 61 queue 179 M/G/1 187 M/G/ _∞_ 191 M/M/1 180 M/M/s 182 queueing network 183–185 queues in series 183 random chessboard knight 50 random walk on Z _[d]_ 29 on a graph 49 recurrence 24, 114, 167 recurrence relations 57 reflected random walks 195 reservoir model 194, 195 resolvent 146 resource management 192 restocking a warehouse 192 return probability 25 reversibility 48, 125 right-continuous process 67 ruin gambler 15 insurance company 196 selective advantage 176 semigroup 96 semigroup property 62 service times 180 shopping centre 185 simple birth process 82 simulation 206 skeleton 122 state-space 1 

_Index_ 

237 

stationary distribution 33, 117 stationary increments 76 stationary policy 198 statistics 55, 211, 215 stochastic matrix 2 stopping time 19 strong law of large numbers 52 strong Markov property 19, 93, 227 success-run chain 38 susceptible 173 

telephone exchange 183 texture parameter 216 time reversal 47, 123 transience 24, 114, 167 transition matrix 2 irreducible 11 

maximum likelihood estimate 56 transition semigroup 165 truncated Poisson distribution 183 

unit mass 3 

_Vi_ ( _n_ ), number of visits to _i_ before _n_ 53 valency 50 value function 198 

weak convergence 164 Wiener process 159 Wiener’s theorem 161 Wright–Fisher model 175 

_ζ_ , explosion time 69 

