## **Applied Mathematical Sciences** 

# Information Geometry and Its Applications 

## Applied Mathematical Sciences 

## Volume 194 

## Editors 

S.S. Antman, Institute for Physical Science and Technology, University of Maryland, College Park, MD, USA 

ssa@math.umd.edu 

Leslie Greengard, Courant Institute of Mathematical Sciences, New York University, New York, NY, USA 

Greengard@cims.nyu.edu 

P.J. Holmes, Department of Mechanical and Aerospace Engineering, Princeton University, Princeton, NJ, USA pholmes@math.princeton.edu 

## Advisors 

J. Bell, Lawrence Berkeley National Lab, Center for Computational Sciences and Engineering, Berkeley, CA, USA 

- P. Constantin, Department of Mathematics, Princeton University, Princeton, NJ, USA 

- J. Keller, Department of Mathematics, Stanford University, Stanford, CA, USA 

- R. Kohn, Courant Institute of Mathematical Sciences, New York University, New York, USA 

- R. Pego, Department of Mathematical Sciences, Carnegie Mellon University, Pittsburgh, PA, USA 

- L. Ryzhik, Department of Mathematics, Stanford University, Stanford, CA, USA 

- A. Singer, Department of Mathematics, Princeton University, Princeton, NJ, USA 

- A. Stevens, Department of Applied Mathematics, University of Münster, Münster, Germany 

- A. Stuart, Mathematics Institute, University of Warwick, Coventry, United Kingdom 

- S. Wright, Computer Sciences Department, University of Wisconsin, Madison, WI, USA 

## Founding Editors 

Fritz John, Joseph P. LaSalle and Lawrence Sirovich 

More information about this series at http://www.springer.com/series/34 

## Shun-ichi Amari 

## Information Geometry and Its Applications 

123 

Shun-ichi Amari Brain Science Institute RIKEN Wako, Saitama Japan 

ISSN 0066-5452 ISSN 2196-968X (electronic) Applied Mathematical Sciences ISBN 978-4-431-55977-1 ISBN 978-4-431-55978-8 (eBook) DOI 10.1007/978-4-431-55978-8 

© Springer Japan 2016, corrected publication 2020 

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. 

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use. 

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, express or implied, with respect to the material contained herein or for any errors or omissions that may have been made. 

This Springer imprint is published by the registered company Springer Japan KK part of Springer Nature. The registered company address is: Shiroyama Trust Tower, 4-3-1 Toranomon, Minato-ku, Tokyo 105-6005, Japan 

## Preface 

Information geometry is a method of exploring the world of information by means of modern geometry. Theories of information have so far been studied mostly by using algebraic, logical, analytical, and probabilistic methods. Since geometry studies mutual relations between elements such as distance and curvature, it should provide the information sciences with powerful tools. 

Information geometry has emerged from studies of invariant geometrical structure involved in statistical inference. It defines a Riemannian metric together with dually coupled affine connections in a manifold of probability distributions. These structures play important roles not only in statistical inference but also in wider areas of information sciences, such as machine learning, signal processing, optimization, and even neuroscience, not to mention mathematics and physics. 

It is intended that the present monograph will give an introduction to information geometry and an overview of wide areas of application. For this purpose, Part I begins with a divergence function in a manifold. We then show that this provides the manifold with a dually flat structure equipped with a Riemannian metric. A highlight is a generalized Pythagorean theorem in a dually flat information manifold. The results are understandable without knowledge of differential geometry. 

Part II gives an introduction to modern differential geometry without tears. We try to present concepts in a way which is intuitively understandable, not sticking to rigorous mathematics. Throughout the monograph, we do not pursue a rigorous mathematical basis but rather develop a framework which gives practically useful and understandable descriptions. 

Part III is devoted to statistical inference, where various topics will be found, including the Neyman–Scott problem, semiparametric models, and the EM algorithm. Part IV overviews various applications of information geometry in the fields of machine learning, signal processing, and others. 

Allow me to review my own personal history in information geometry. It was in 1958, when I was a graduate student on a master’s course, that I followed a seminar on statistics. The text was “Information Theory and Statistics” by S. Kullback, and 

v 

vi 

Preface 

a professor suggested to me that the Fisher information might be regarded as a Riemannian metric. I calculated the Riemannian metric and curvature of the manifold of Gaussian distributions and found that it is a manifold of constant curvature, which is no different from the famous Poincaré half-plane in non-Euclidean geometry. I was enchanted by its beauty. I believed that a beautiful structure must have important practical significance, but I was not able to pursue its consequences further. 

Fifteen years later, I was stimulated by a paper by Prof. B. Efron and accompanying discussions by Prof. A.P. Dawid, and restarted my investigation into information geometry. Later, I found that Prof. N.N. Chentsov had developed a theory along similar lines. I was lucky that Sir D. Cox noticed my approach and organized an international workshop on information geometry in 1984, in which many active statisticians participated. This was a good start for information geometry. 

Now information geometry has been developed worldwide and many symposia and workshops have been organized around the world. Its areas of application have been enlarged from statistical inference to wider fields of information sciences. 

To my regret, I have not been able to introduce many excellent works by other researchers around the world. For example, I have not been able to touch upon quantum information geometry. Also I have not been able to refer to many important works, because of my limited capability. 

Last but not least, I would like to thank Dr. M. Kumon and Prof. H. Nagaoka, who collaborated in the early period of the infancy of information geometry. I also thank the many researchers who have supported me in the process of construction of information geometry, Profs. D. Cox, C.R. Rao, O. Barndorff-Nielsen, S. Lauritzen, B. Efron, A.P. Dawid, K. Takeuchi, and the late N.N. Chentsov, among many many others. Finally, I would like to thank Ms. Emi Namioka who arranged my handwritten manuscripts in the beautiful TEX form. Without her devotion, the monograph would not have appeared. 

April 2015 

Shun-ichi Amari 

The original version of the book was revised: Author-provided belated corrections have been incorporated. The correction to the book is available at https://doi.org/10.1007/978-4-431-55978-8_14 

## Contents 

## Part I Geometry of Divergence Functions: Dually Flat Riemannian Structure 

||Structure|Structure||
|---|---|---|---|
|1|Manifold, Divergence and Dually Flat Structure . . . . . . . . . . . . . .||3|
||1.1|Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
|||1.1.1<br>Manifold and Coordinate Systems . . . . . . . . . . . . . . .|3|
|||1.1.2<br>Examples of Manifolds . . . . . . . . . . . . . . . . . . . . . . .|5|
||1.2|Divergence Between Two Points . . . . . . . . . . . . . . . . . . . . . .|9|
|||1.2.1<br>Divergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
|||1.2.2<br>Examples of Divergence . . . . . . . . . . . . . . . . . . . . . .|11|
||1.3|Convex Function and Bregman Divergence . . . . . . . . . . . . . . .|12|
|||1.3.1<br>Convex Function . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|||1.3.2<br>Bregman Divergence . . . . . . . . . . . . . . . . . . . . . . . .|13|
||1.4|Legendre Transformation. . . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
||1.5|Dually Flat Riemannian Structure Derived from Convex||
|||Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|||1.5.1<br>Affne and Dual Affne Coordinate Systems . . . . . . . . .|19|
|||1.5.2<br>Tangent Space, Basis Vectors||
|||and Riemannian Metric . . . . . . . . . . . . . . . . . . . . . . .|20|
|||1.5.3<br>Parallel Transport of Vector. . . . . . . . . . . . . . . . . . . .|23|
||1.6|Generalized Pythagorean Theorem and Projection Theorem . . . .|24|
|||1.6.1<br>Generalized Pythagorean Theorem . . . . . . . . . . . . . . .|24|
|||1.6.2<br>Projection Theorem . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|||1.6.3<br>Divergence Between Submanifolds: Alternating||
|||Minimization Algorithm . . . . . . . . . . . . . . . . . . . . . .|27|
|2|Exponential Families and Mixture Families of Probability|||
||Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||31|
||2.1|Exponential Family of Probability Distributions . . . . . . . . . . . .|31|



vii 

viii 

Contents 

||2.2|Examples of Exponential Family: Gaussian and Discrete||
|---|---|---|---|
|||Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|34|
|||2.2.1<br>Gaussian Distribution . . . . . . . . . . . . . . . . . . . . . . . .|34|
|||2.2.2<br>Discrete Distribution. . . . . . . . . . . . . . . . . . . . . . . . .|35|
||2.3|Mixture Family of Probability Distributions. . . . . . . . . . . . . . .|36|
||2.4|Flat Structure: e-fat and m-fat. . . . . . . . . . . . . . . . . . . . . . . .|37|
||2.5|On Infnite-Dimensional Manifold||
|||of Probability Distributions . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
||2.6|Kernel Exponential Family . . . . . . . . . . . . . . . . . . . . . . . . . .|42|
||2.7|Bregman Divergence and Exponential Family . . . . . . . . . . . . .|43|
||2.8|Applications of Pythagorean Theorem. . . . . . . . . . . . . . . . . . .|44|
|||2.8.1<br>Maximum Entropy Principle . . . . . . . . . . . . . . . . . . .|44|
|||2.8.2<br>Mutual Information. . . . . . . . . . . . . . . . . . . . . . . . . .|46|
|||2.8.3<br>Repeated Observations and Maximum Likelihood||
|||Estimator. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|47|
|3|Invariant Geometry of Manifold of Probability Distributions. . . . .||51|
||3.1|Invariance Criterion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
||3.2|Information Monotonicity Under Coarse Graining . . . . . . . . . .|53|
|||3.2.1<br>Coarse Graining and Suffcient Statistics in Sn . . . . . . .|53|
|||3.2.2<br>Invariant Divergence. . . . . . . . . . . . . . . . . . . . . . . . .|54|
||3.3|Examples of f-Divergence in Sn. . . . . . . . . . . . . . . . . . . . . . .|57|
|||3.3.1<br>KL-Divergence . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|||3.3.2<br>χ2-Divergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|||3.3.3<br>α-Divergence. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
||3.4|General Properties of f-Divergence and KL-Divergence . . . . . .|59|
|||3.4.1<br>Properties of f-Divergence. . . . . . . . . . . . . . . . . . . . .|59|
|||3.4.2<br>Properties of KL-Divergence . . . . . . . . . . . . . . . . . . .|60|
||3.5|Fisher Information: The Unique Invariant Metric . . . . . . . . . . .|62|
||3.6|f-Divergence in Manifold of Positive Measures . . . . . . . . . . . .|65|
|4|α-Geometry, Tsallis q-Entropy and Positive-Defnite Matrices. . . . .||71|
||4.1|Invariant and Flat Divergence . . . . . . . . . . . . . . . . . . . . . . . .|71|
|||4.1.1<br>KL-Divergence Is Unique . . . . . . . . . . . . . . . . . . . . .|71|
|||4.1.2<br>α-Divergence Is Unique in Rn<br>þ . . . . . . . . . . . . . . . . .|72|
||4.2|α-Geometry in Sn and Rn<br>þ . . . . . . . . . . . . . . . . . . . . . . . . . . .|75|
|||4.2.1<br>α-Geodesic and α-Pythagorean Theorem in Rn<br>þ . . . . . .|75|
|||4.2.2<br>α-Geodesic in Sn . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||4.2.3<br>α-Pythagorean Theorem and α-Projection Theorem||
|||in Sn. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||4.2.4<br>Apportionment Due to α-Divergence . . . . . . . . . . . . .|77|
|||4.2.5<br>α-Mean. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|77|
|||4.2.6<br>α-Families of Probability Distributions . . . . . . . . . . . .|80|
|||4.2.7<br>Optimality of α-Integration . . . . . . . . . . . . . . . . . . . .|82|
|||4.2.8<br>Application to α-Integration of Experts . . . . . . . . . . . .|83|



ix 

Contents 

||4.3|Geometry of Tsallis q-Entropy. . . . . . . . . . . . . . . . . . . . . . . .|84|
|---|---|---|---|
|||4.3.1<br>q-Logarithm and q-Exponential Function. . . . . . . . . . .|85|
|||4.3.2<br>q-Exponential Family (α-Family) of Probability||
|||Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|86|
|||4.3.3<br>q-Escort Geometry . . . . . . . . . . . . . . . . . . . . . . . . . .|87|
|||4.3.4<br>Deformed Exponential Family: χ-Escort Geometry . . . .|89|
|||4.3.5<br>Conformal Character of q-Escort Geometry . . . . . . . . .|91|
||4.4|ðu;vÞ-Divergence: Dually Flat Divergence in Manifold||
|||of Positive Measures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|92|
|||4.4.1<br>Decomposable ðu;vÞ-Divergence . . . . . . . . . . . . . . . .|92|
|||4.4.2<br>General ðu;vÞ Flat Structure in Rn<br>þ . . . . . . . . . . . . . . .|95|
||4.5|Invariant Flat Divergence in Manifold of Positive-Defnite||
|||Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|96|
|||4.5.1<br>Bregman Divergence and Invariance Under GlðnÞ . . . .|96|
|||4.5.2<br>Invariant Flat Decomposable Divergences||
|||Under OðnÞ. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|98|
|||4.5.3<br>Non-fat Invariant Divergences. . . . . . . . . . . . . . . . . .|101|
||4.6|Miscellaneous Divergences . . . . . . . . . . . . . . . . . . . . . . . . . .|102|
|||4.6.1<br>γ-Divergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|102|
|||4.6.2<br>Other Types of ðα;βÞ-Divergences . . . . . . . . . . . . . . .|102|
|||4.6.3<br>Burbea–Rao Divergence and Jensen–Shannon||
|||Divergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
|||4.6.4<br>ðρ;τÞ-Structure and ðF;G;HÞ-Structure. . . . . . . . . . . .|104|
|Part|II|Introduction to Dual Differential Geometry||
|5|Elements of Differential Geometry . . . . . . . . . . . . . . . . . . . . . . . .||109|
||5.1|Manifold and Tangent Space . . . . . . . . . . . . . . . . . . . . . . . . .|109|
||5.2|Riemannian Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|111|
||5.3|Affne Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|112|
||5.4|Tensors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|114|
||5.5|Covariant Derivative. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|
||5.6|Geodesic. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|117|
||5.7|Parallel Transport of Vector. . . . . . . . . . . . . . . . . . . . . . . . . .|118|
||5.8|Riemann–Christoffel Curvature . . . . . . . . . . . . . . . . . . . . . . .|119|
|||5.8.1<br>Round-the-World Transport of Vector. . . . . . . . . . . . .|120|
|||5.8.2<br>Covariant Derivative and RC Curvature . . . . . . . . . . .|122|
|||5.8.3<br>Flat Manifold. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|123|
||5.9|Levi–Civita (Riemannian) Connection. . . . . . . . . . . . . . . . . . .|124|
||5.10|Submanifold and Embedding Curvature . . . . . . . . . . . . . . . . .|126|
|||5.10.1<br>Submanifold . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|126|
|||5.10.2<br>Embedding Curvature . . . . . . . . . . . . . . . . . . . . . . . .|127|



Contents 

x 

|6|Dual|Affne Connections and Dually Flat Manifold . . . . . . . . . . . . 131|
|---|---|---|
||6.1|Dual Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|
||6.2|Metric and Cubic Tensor Derived from Divergence . . . . . . . . . 134|
||6.3|Invariant Metric and Cubic Tensor . . . . . . . . . . . . . . . . . . . . . 136|
||6.4|α-Geometry. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136|
||6.5|Dually Flat Manifold . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
||6.6|Canonical Divergence in Dually Flat Manifold. . . . . . . . . . . . . 138|
||6.7|Canonical Divergence in General Manifold of Dual|
|||Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141|
||6.8|Dual Foliations of Flat Manifold and Mixed Coordinates . . . . . 143|
|||6.8.1<br>k-cut of Dual Coordinate Systems: Mixed|
|||Coordinates and Foliation . . . . . . . . . . . . . . . . . . . . . 144|
|||6.8.2<br>Decomposition of Canonical Divergence . . . . . . . . . . . 145|
|||6.8.3<br>A Simple Illustrative Example: Neural Firing. . . . . . . . 146|
|||6.8.4<br>Higher-Order Interactions of Neuronal Spikes . . . . . . . 148|
||6.9|System Complexity and Integrated Information . . . . . . . . . . . . 150|
||6.10|Input–Output Analysis in Economics . . . . . . . . . . . . . . . . . . . 157|
|Part|III|Information Geometry of Statistical Inference|
|7|Asymptotic Theory of Statistical Inference . . . . . . . . . . . . . . . . . . 165||
||7.1|Estimation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165|
||7.2|Estimation in Exponential Family. . . . . . . . . . . . . . . . . . . . . . 166|
||7.3|Estimation in Curved Exponential Family . . . . . . . . . . . . . . . . 168|
||7.4|First-Order Asymptotic Theory of Estimation. . . . . . . . . . . . . . 171|
||7.5|Higher-Order Asymptotic Theory of Estimation . . . . . . . . . . . . 173|
||7.6|Asymptotic Theory of Hypothesis Testing. . . . . . . . . . . . . . . . 175|
|8|Estimation in the Presence of Hidden Variables. . . . . . . . . . . . . . . 179||
||8.1|EM Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179|
|||8.1.1<br>Statistical Model with Hidden Variables . . . . . . . . . . . 179|
|||8.1.2<br>Minimizing Divergence Between Model Manifold|
|||and Data Manifold . . . . . . . . . . . . . . . . . . . . . . . . . . 182|
|||8.1.3<br>EM Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184|
|||8.1.4<br>Example: Gaussian Mixture . . . . . . . . . . . . . . . . . . . . 184|
||8.2|Loss of Information by Data Reduction. . . . . . . . . . . . . . . . . . 185|
||8.3|Estimation Based on Misspecifed Statistical Model . . . . . . . . . 186|
|9|Neyman-Scott Problem: Estimating Function||
||and Semiparametric Statistical Model. . . . . . . . . . . . . . . . . . . . . . 191||
||9.1|Statistical Model Including Nuisance Parameters . . . . . . . . . . . 191|
||9.2|Neyman–Scott Problem and Semiparametrics. . . . . . . . . . . . . . 194|
||9.3|Estimating Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197|
||9.4|Information Geometry of Estimating Function . . . . . . . . . . . . . 199|



xi 

Contents 

||9.5|Solutions to Neyman–Scott Problems . . . . . . . . . . . . . . . . . . . 206|Solutions to Neyman–Scott Problems . . . . . . . . . . . . . . . . . . . 206|
|---|---|---|---|
|||9.5.1|Estimating Function in the Exponential Case . . . . . . . . 206|
|||9.5.2|Coeffcient of Linear Dependence. . . . . . . . . . . . . . . . 208|
|||9.5.3|Scale Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209|
|||9.5.4|Temporal Firing Pattern of Single Neuron . . . . . . . . . . 211|
|10|Linear Systems and Time Series. . . . . . . . . . . . . . . . . . . . . . . . . . 215|||
||10.1|Stationary Time Series and Linear System. . . . . . . . . . . . . . . . 215||
||10.2|Typical|Finite-Dimensional Manifolds of Time Series. . . . . . . . 217|
||10.3|Dual Geometry of System Manifold . . . . . . . . . . . . . . . . . . . . 219||
||10.4|Geometry of AR, MA and ARMA Models . . . . . . . . . . . . . . . 223||
|Part|IV|Applications of Information Geometry||
|11|Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231|||
||11.1|Clustering Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231||
|||11.1.1|Pattern Space and Divergence . . . . . . . . . . . . . . . . . . 231|
|||11.1.2|Center of Cluster . . . . . . . . . . . . . . . . . . . . . . . . . . . 232|
|||11.1.3|k-Means: Clustering Algorithm . . . . . . . . . . . . . . . . . 233|
|||11.1.4|Voronoi Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . 234|
|||11.1.5|Stochastic Version of Classifcation and Clustering. . . . 236|
|||11.1.6|Robust Cluster Center. . . . . . . . . . . . . . . . . . . . . . . . 238|
|||11.1.7|Asymptotic Evaluation of Error Probability in Pattern|
||||Recognition: Chernoff Information . . . . . . . . . . . . . . . 240|
||11.2|Geometry of Support Vector Machine. . . . . . . . . . . . . . . . . . . 242||
|||11.2.1|Linear Classifer. . . . . . . . . . . . . . . . . . . . . . . . . . . . 242|
|||11.2.2|Embedding into High-Dimensional Space . . . . . . . . . . 245|
|||11.2.3|Kernel Method. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246|
|||11.2.4|Riemannian Metric Induced by Kernel . . . . . . . . . . . . 247|
||11.3|Stochastic Reasoning: Belief Propagation and CCCP||
|||Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249||
|||11.3.1|Graphical Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 250|
|||11.3.2|Mean Field Approximation and m-Projection . . . . . . . . 252|
|||11.3.3|Belief Propagation . . . . . . . . . . . . . . . . . . . . . . . . . . 255|
|||11.3.4|Solution of BP Algorithm . . . . . . . . . . . . . . . . . . . . . 257|
|||11.3.5|CCCP (Convex–Concave Computational|
||||Procedure). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259|
||11.4|Information Geometry of Boosting . . . . . . . . . . . . . . . . . . . . . 260||
|||11.4.1|Boosting: Integration of Weak Machines . . . . . . . . . . . 261|
|||11.4.2|Stochastic Interpretation of Machine . . . . . . . . . . . . . . 262|
|||11.4.3|Construction of New Weak Machines . . . . . . . . . . . . . 263|
|||11.4.4|Determination of the Weights of Weak Machines. . . . . 263|



xii 

Contents 

||11.5|Bayesian Inference and Deep Learning . . . . . . . . . . . . . . . . . . 265|Bayesian Inference and Deep Learning . . . . . . . . . . . . . . . . . . 265|
|---|---|---|---|
|||11.5.1|Bayesian Duality in Exponential Family . . . . . . . . . . . 266|
|||11.5.2|Restricted Boltzmann Machine. . . . . . . . . . . . . . . . . . 268|
|||11.5.3|Unsupervised Learning of RBM. . . . . . . . . . . . . . . . . 269|
|||11.5.4|Geometry of Contrastive Divergence. . . . . . . . . . . . . . 273|
|||11.5.5|Gaussian RBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275|
|12|Natural Gradient Learning and Its Dynamics|||
||in Singular Regions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279|||
||12.1|Natural|Gradient Stochastic Descent Learning . . . . . . . . . . . . . 279|
|||12.1.1|On-Line Learning and Batch Learning . . . . . . . . . . . . 279|
|||12.1.2|Natural Gradient: Steepest Descent Direction|
||||in Riemannian Manifold . . . . . . . . . . . . . . . . . . . . . . 282|
|||12.1.3|Riemannian Metric, Hessian and Absolute Hessian. . . . 284|
|||12.1.4|Stochastic Relaxation of Optimization Problem . . . . . . 286|
|||12.1.5|Natural Policy Gradient in Reinforcement Learning . . . 287|
|||12.1.6|Mirror Descent and Natural Gradient . . . . . . . . . . . . . 289|
|||12.1.7|Properties of Natural Gradient Learning . . . . . . . . . . . 290|
||12.2|Singularity in Learning: Multilayer Perceptron . . . . . . . . . . . . . 296||
|||12.2.1|Multilayer Perceptron . . . . . . . . . . . . . . . . . . . . . . . . 296|
|||12.2.2|Singularities in M. . . . . . . . . . . . . . . . . . . . . . . . . . . 298|
|||12.2.3|Dynamics of Learning in M. . . . . . . . . . . . . . . . . . . . 302|
|||12.2.4|Critical Slowdown of Dynamics. . . . . . . . . . . . . . . . . 305|
|||12.2.5|Natural Gradient Learning Is Free of Plateaus . . . . . . . 309|
|||12.2.6|Singular Statistical Models . . . . . . . . . . . . . . . . . . . . 310|
|||12.2.7|Bayesian Inference and Singular Model. . . . . . . . . . . . 312|
|13|Signal|Processing and Optimization . . . . . . . . . . . . . . . . . . . . . . . 315||
||13.1|Principal Component Analysis . . . . . . . . . . . . . . . . . . . . . . . . 315||
|||13.1.1|Eigenvalue Analysis . . . . . . . . . . . . . . . . . . . . . . . . . 315|
|||13.1.2|Principal Components, Minor Components|
||||and Whitening . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316|
|||13.1.3|Dynamics of Learning of Principal and Minor|
||||Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319|
||13.2|Independent Component Analysis. . . . . . . . . . . . . . . . . . . . . . 322||
|||13.2.3|Estimating Function of ICA: Semiparametric|
||||Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330|
||13.3|Non-negative Matrix Factorization . . . . . . . . . . . . . . . . . . . . . 333||
||13.4|Sparse|Signal Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . 336|
|||13.4.1|Linear Regression and Sparse Solution . . . . . . . . . . . . 337|
|||13.4.2|Minimization of Convex Function Under L1|
||||Constraint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338|
|||13.4.3|Analysis of Solution Path . . . . . . . . . . . . . . . . . . . . . 341|
|||13.4.4|Minkovskian Gradient Flow. . . . . . . . . . . . . . . . . . . . 343|
|||13.4.5|Underdetermined Case . . . . . . . . . . . . . . . . . . . . . . . 344|



|Contents||xiii|
|---|---|---|
|13.5|Optimization in Convex Programming . . . . . . . . . . . . . . . . . .|345|
||13.5.1<br>Convex Programming . . . . . . . . . . . . . . . . . . . . . . . .|345|
||13.5.2<br>Dually Flat Structure Derived||
||from Barrier Function . . . . . . . . . . . . . . . . . . . . . . . .|347|
||13.5.3<br>Computational Complexity and m-curvature. . . . . . . . .|348|
|13.6|Dual Geometry Derived from Game Theory . . . . . . . . . . . . . .|349|
||13.6.1<br>Minimization of Game-Score . . . . . . . . . . . . . . . . . . .|349|
||13.6.2<br>Hyvärinen Score . . . . . . . . . . . . . . . . . . . . . . . . . . .|353|
|Correction to: Information Geometry and Its Applications. . . . . . . . . .||C1|
|References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||359|
|Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||371|



**Part I Geometry of Divergence Functions: Dually Flat Riemannian Structure** 

## **Chapter 1 Manifold, Divergence and Dually Flat Structure** 

The present chapter begins with a manifold and a coordinate system within it. Then, a divergence between two points is defined. We use an intuitive style of explanation for manifolds, followed by typical examples. A divergence represents a degree of separation of two points, but it is not a distance since it is not symmetric with respect to the two points. Here is the origin of dually coupled asymmetry, leading us to a dual world. When a divergence is derived from a convex function in the form of the Bregman divergence, two affine structures are induced in the manifold. They are dually coupled via the Legendre transformation. Thus, a convex function provides a manifold with a dually flat affine structure in addition to a Riemannian metric derived from it. The dually flat structure plays a pivotal role in information geometry, as is shown in the generalized Pythagorean theorem. The dually flat structure is a special case of Riemannian geometry equipped with non-flat dual affine connections, which will be studied in Part II. 

## **1.1 Manifolds** 

## _**1.1.1 Manifold and Coordinate Systems**_ 

An _n_ -dimensional manifold _M_ is a set of points such that each point has _n_ - dimensional extensions in its neighborhood. That is, such a neighborhood is topologically equivalent to an _n_ -dimensional Euclidean space. Intuitively speaking, a manifold is a deformed Euclidean space, like a curved surface in the two-dimensional case. But it may have a different global topology. A sphere is an example which is locally equivalent to a two-dimensional Euclidean space, but is curved and has a different global topology because it is compact (bounded and closed). 

The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_1 

3 

1 Manifold, Divergence and Dually Flat Structure 

4 

**==> picture [388 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
ξ2<br>ξ2<br>ξ1<br>ξ1<br>E 2<br>M<br>**----- End of picture text -----**<br>


**Fig. 1.1** Manifold _M_ and coordinate system _ξ_ . _E_ 2 is a two-dimensional Euclidean space 

Since a manifold _M_ is locally equivalent to an _n_ -dimensional Euclidean space _En_ , we can introduce a local coordinate system 

**==> picture [200 x 10] intentionally omitted <==**

composed of _n_ components _ξ_ 1 _, . . . , ξn_ such that each point is uniquely specified by its coordinates _**ξ**_ in a neighborhood. See Fig. 1.1 for the two-dimensional case. Since a manifold may have a topology different from a Euclidean space, in general we need more than one coordinate neighborhood and coordinate system to cover all the points of a manifold. 

The coordinate system is not unique even in a coordinate neighborhood, and there are many coordinate systems. Let _**ζ**_ = _(ζ_ 1 _, . . . , ζn)_ be another coordinate system. When a point _P_ ∈ _M_ is represented in two coordinate systems _**ξ**_ and _**ζ**_ , there is a one-to-one correspondence between them and we have relations 

**==> picture [212 x 25] intentionally omitted <==**

where _**f**_ and _**f**_[−][1] are mutually inverse vector-valued functions. They are a coordinate transformation and its inverse transformation. We usually assume that (1.2) and (1.3) are differentiable functions of _n_ coordinate variables.[1] 

> 1Mathematically trained readers may know the rigorous definition of a manifold: A manifold _M_ is a Hausdorff space which is covered by a number of open sets called coordinate neighborhoods, such that there exists an isomorphism between a coordinate neighborhood and a Euclidean space. The isomorphism defines a local coordinate system in the neighborhood. _M_ is called a differentiable manifold when the coordinate transformations are differentiable. See textbooks on modern differential geometry. Our definition is intuitive, not mathematically rigorous, but is sufficient for understanding information geometry and its applications. 

5 

1.1 Manifolds 

## _**1.1.2 Examples of Manifolds**_ 

## **A. Euclidean Space** 

Consider a two-dimensional Euclidean space, which is a flat plane. It is convenient to use an orthonormal Cartesian coordinate system _**ξ**_ = _(ξ_ 1 _, ξ_ 2 _)_ . A polar coordinate system _**ζ**_ = _(r, θ)_ is sometimes used, where _r_ is the radius and _θ_ is the angle of a point from one axis (see Fig. 1.2). The coordinate transformation between them is given by 

**==> picture [235 x 38] intentionally omitted <==**

The transformation is analytic except for the origin. 

## **B. Sphere** 

A sphere is the surface of a three-dimensional ball. The surface of the earth is regarded as a sphere, where each point has a two-dimensional neighborhood, so that we can draw a local geographic map on a flat sheet. The pair of latitude and longitude gives a local coordinate system. However, a sphere is topologically different from a Euclidean space and it cannot be covered by one coordinate system. At least two 

**Fig. 1.2** Cartesian coordinate system _**ξ**_ = _(ξ_ 1 _, ξ_ 2 _)_ and polar coordinate system _(r, θ)_ in _E_ 2 

**==> picture [202 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
ξ2<br>E 2<br>r<br>θ<br>ξ1<br>**----- End of picture text -----**<br>


6 

1 Manifold, Divergence and Dually Flat Structure 

coordinate systems are required to cover it. If we delete one point, say the north pole of the earth, it is topologically equivalent to a Euclidean space. Hence, at least two overlapping coordinate neighborhoods, one including the north pole and the other including the south pole, for example, are necessary and they are sufficient to cover the entire sphere. 

## **C. Manifold of Probability Distributions** 

C1. Gaussian Distributions 

The probability density function of Gaussian random variable _x_ is given by 

**==> picture [251 x 26] intentionally omitted <==**

where _μ_ is the mean and _σ_[2] is the variance. Hence, the set of all the Gaussian distributions is a two-dimensional manifold, where a point denotes a probability density function and 

**==> picture [207 x 10] intentionally omitted <==**

is a coordinate system. This is topologically equivalent to the upper half of a twodimensional Euclidean space. The manifold of Gaussian distributions is covered by one coordinate system _**ξ**_ = _(μ, σ)_ . 

There are other coordinate systems. For example, let _m_ 1 and _m_ 2 be the first and second moments of _x_ , given by 

**==> picture [254 x 13] intentionally omitted <==**

where E denotes the expectation of a random variable. Then, 

**==> picture [195 x 10] intentionally omitted <==**

is a coordinate system (the moment coordinate system). 

It will be shown later that the coordinate system defined by _**θ**_ , 

**==> picture [216 x 22] intentionally omitted <==**

is referred to as the natural parameters, and is convenient for studying properties of Gaussian distributions. 

1.1 Manifolds 

7 

C2. Discrete Distributions 

Let _x_ be a discrete random variable taking values on _X_ = {0 _,_ 1 _, . . . , n_ }. A probability distribution _p(x)_ is specified by _n_ + 1 probabilities 

**==> picture [240 x 10] intentionally omitted <==**

so that _p(x)_ is represented by a probability vector 

**==> picture [211 x 10] intentionally omitted <==**

Because of the restriction 

**==> picture [208 x 29] intentionally omitted <==**

the set of all probability distributions _**p**_ forms an _n_ -dimensional manifold. Its coordinate system is given, for example, by 

**==> picture [202 x 10] intentionally omitted <==**

and _p_ 0 is not free but is a function of the coordinates, 

**==> picture [199 x 10] intentionally omitted <==**

The manifold is an _n_ -dimensional simplex, called the probability simplex, and is denoted by _Sn_ . When _n_ = 2, _S_ 2 is the interior of a triangle and when _n_ = 3, it is the interior of a 3-simplex, as is shown in Fig. 1.3. 

**==> picture [283 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
p 2 p 3<br>S 3<br>S 2<br>p 0 p 2<br>p 0 p 1 p 1<br>**----- End of picture text -----**<br>


**Fig. 1.3** Probability simplex: _S_ 2 and _S_ 3 

1 Manifold, Divergence and Dually Flat Structure 

8 

Let us introduce _n_ + 1 random variables _δi (x), i_ = 0 _,_ 1 _, . . . , n_ , such that 

**==> picture [207 x 25] intentionally omitted <==**

Then, a probability distribution of _x_ is denoted by 

**==> picture [238 x 28] intentionally omitted <==**

in terms of coordinates _**ξ**_ . We shall use another coordinate system _**θ**_ later, given by 

**==> picture [224 x 21] intentionally omitted <==**

which is also very useful. 

C3. Regular Statistical Model 

Let _x_ be a random variable which may take discrete, scalar or vector continuous values. A statistical model is a family of probability distributions _M_ = { _p(x,_ _**ξ** )_ } specified by a vector parameter _**ξ**_ . When it satisfies certain regularity conditions, it is called a regular statistical model. Such an _M_ is a manifold, where _**ξ**_ plays the role of a coordinate system. The family of Gaussian distributions and the family of discrete probability distributions are examples of the regular statistical model. Information geometry has emerged from a study of invariant geometrical structures of regular statistical models. 

## **D. Manifold of Positive Measures** 

Let _x_ be a variable taking values in set _N_ = {1 _,_ 2 _, . . . , n_ }. We assign a positive measure (or a weight) _mi_ to element _i, i_ = 1 _, . . . , n_ . Then 

**==> picture [225 x 10] intentionally omitted <==**

defines a distribution of measures over _N_ . The set of all such measures sits in the first quadrant _**R**[n]_ +[of an] _[ n]_[-dimensional Euclidean space. The sum] 

**==> picture [191 x 29] intentionally omitted <==**

is called the total mass of _**m**_ = _(m_ 1 _, . . . , mn)_ . 

1.1 Manifolds 

9 

When _**m**_ satisfies the constraint that the total mass is equal to 1, 

**==> picture [190 x 15] intentionally omitted <==**

it is a probability distribution belonging to _Sn_ −1. Hence, _Sn_ −1 is included in _**R**[n]_ +[as] its submanifold. 

A positive measure (unnormalized probability distribution) appears in many engineering problems. For example, image _s(x, y)_ drawn on the _x_ – _y_ plane is a positive measure when the brightness is positive, 

**==> picture [192 x 10] intentionally omitted <==**

When we discretize the _x_ – _y_ plane into _n_[2] pixels _(i, j)_ , the discretized pictures { _s(i, j)_ } form a positive measure belonging to _**R**[n]_ +[2][.][Similarly,][when][we][consider] a discretized power spectrum of a sound, it is a positive measure. The histogram of observed data defines a positive measure, too. 

## 

Let **A** be an _n_ × _n_ matrix. All such matrices form an _n_[2] -dimensional manifold. When **A** is symmetric and positive-definite, they form a _[n][(][n]_ 2[+][1] _[)]_ -dimensional manifold. This is a submanifold embedded in the manifold of all the matrices. We may use the upper right elements of **A** as a coordinate system. Positive-definite matrices appear in statistics, physics, operations research, control theory, etc. 

## **F. Neural Manifold** 

A neural network is composed of a large number of neurons connected with each other, where the dynamics of information processing takes place. A network is specified by connection weights _w ji_ connecting neuron _i_ with neuron _j_ . The set of all such networks forms a manifold, where matrix **W** = � _w ji_ � is a coordinate system. We will later analyze behaviors of such networks from the information geometry point of view. 

## **1.2 Divergence Between Two Points** 

## _**1.2.1 Divergence**_ 

Let us consider two points _P_ and _Q_ in a manifold _M_ , of which coordinates are _**ξ** P_ and _**ξ** Q_ . A divergence _D_ [ _P_ : _Q_ ] is a function of _**ξ** p_ and _**ξ** Q_ which satisfies certain 

1 Manifold, Divergence and Dually Flat Structure 

10 

criteria. See Basseville (2013) for a detailed bibliography. We may write it as 

**==> picture [220 x 13] intentionally omitted <==**

We assume that it is a differentiable function of _**ξ** P_ and _**ξ** Q_ . 

**Definition 1.1** _D_ [ _P_ : _Q_ ] is called a divergence when it satisfies the following criteria: 

- (1) _D_ [ _P_ : _Q_ ] ≥ 0. 

- (2) _D_ [ _P_ : _Q_ ] = 0, when and only when _P_ = _Q_ . 

- (3) When _P_ and _Q_ are sufficiently close, by denoting their coordinates by _**ξ** P_ and _**ξ** Q_ = _**ξ** P_ + _d_ _**ξ**_ , the Taylor expansion of _D_ is written as 

**==> picture [266 x 22] intentionally omitted <==**

and matrix **G** = � _gi j_ � is positive-definite, depending on _**ξ** P_ . 

A divergence represents a degree of separation of two points _P_ and _Q_ , but it or its square root is not a distance. It does not necessarily satisfy the symmetry condition, so that in general 

**==> picture [214 x 10] intentionally omitted <==**

We may call _D_ [ _P_ : _Q_ ] divergence from _P_ to _Q_ . Moreover, the triangular inequality does not hold. It has the dimension of the square of distance, as is suggested by (1.24). It is possible to symmetrize a divergence by 

**==> picture [251 x 22] intentionally omitted <==**

However, the asymmetry of divergence plays an important role in information geometry, as will be seen later. 

When _P_ and _Q_ are sufficiently close, we define the square of an infinitesimal distance _ds_ between them by using (1.24) as 

**==> picture [248 x 15] intentionally omitted <==**

A manifold _M_ is said to be Riemannian when a positive-definite matrix **G** _(_ _**ξ** )_ is defined on _M_ and the square of the local distance between two nearby points _**ξ**_ and _**ξ**_ + _d_ _**ξ**_ is given by (1.27). A divergence _D_ provides _M_ with a Riemannian structure. 

1.2 Divergence Between Two Points 

11 

## _**1.2.2 Examples of Divergence**_ 

## **A. Euclidean Divergence** 

When we use an orthonormal Cartesian coordinate system in a Euclidean space, we define a divergence by a half of the square of the Euclidean distance, 

**==> picture [233 x 22] intentionally omitted <==**

The matrix **G** is the identity matrix in this case, so that 

**==> picture [203 x 15] intentionally omitted <==**

## **B. Kullback–Leibler Divergence** 

Let _p(x)_ and _q(x)_ be two probability distributions of random variable _x_ in a manifold of probability distributions. The following is called the Kullback–Leibler (KL) divergence: 

**==> picture [251 x 24] intentionally omitted <==**

When _x_ is discrete, integration is replaced by summation. We can easily check that it satisfies the criteria of divergence. It is asymmetric in general and is useful in statistics, information theory, physics, etc. Many other divergences will be introduced later in a manifold of probability distributions. 

## **C. KL-Divergence for Positive Measures** 

A manifold of positive measures _**R**[n]_ +[is][a][subset][of][a][Euclidean][space.][Hence,][we] can introduce the Euclidean divergence (1.28) in it. However, we can extend the KL-divergence to give 

**==> picture [278 x 21] intentionally omitted <==**

When the total masses of two measures _**m**_ 1 and _**m**_ 2 are 1, they are probability distributions and _DK L_ [ _**m**_ 1 : _**m**_ 2] reduces to the KL-divergence _DK L_ in (1.30). 

1 Manifold, Divergence and Dually Flat Structure 

12 

## **D. Divergences for Positive-Definite Matrices** 

There is a family of useful divergences introduced in the manifold of positive-definite matrices. Let **P** and **Q** be two positive-definite matrices. The following are typical examples of divergence: 

**==> picture [256 x 10] intentionally omitted <==**

which is related to the Von Neumann entropy of quantum mechanics, 

**==> picture [250 x 13] intentionally omitted <==**

which is due to the KL-divergence of multivariate Gaussian distribution, and 

**==> picture [300 x 25] intentionally omitted <==**

which is called the _α_ -divergence, where _α_ is a real parameter. Here, tr **P** denotes the trace of matrix **P** and | **P** | is the determinant of **P** . 

## **1.3 Convex Function and Bregman Divergence** 

## _**1.3.1 Convex Function**_ 

A nonlinear function _ψ(_ _**ξ** )_ of coordinates _**ξ**_ is said to be convex when the inequality 

**==> picture [266 x 13] intentionally omitted <==**

is satisfied for any _**ξ**_ 1, _**ξ**_ 2 and scalar 0 ≤ _λ_ ≤ 1. We consider a differentiable convex function. Then, a function is convex if and only if its Hessian 

**==> picture [216 x 26] intentionally omitted <==**

is positive-definite. 

There are many convex functions appearing in physics, optimization and engineering problems. One simple example is 

**==> picture [200 x 21] intentionally omitted <==**

1.3 Convex Function and Bregman Divergence 

13 

which is a half of the square of the Euclidean distance from the origin to point _**ξ**_ . Let _**p**_ be a probability distribution belonging to _Sn_ . Then, its entropy 

**==> picture [214 x 15] intentionally omitted <==**

is a concave function, so that its negative, _ϕ(_ _**p** )_ = − _H (_ _**p** )_ , is a convex function. 

We give one more example from a probability model. An exponential family of probability distributions is written as 

**==> picture [251 x 19] intentionally omitted <==**

where _p(_ _**x** ,_ _**θ** )_ is the probability density function of vector random variable _**x**_ specified by vector parameter _**θ**_ and _k(_ _**x** )_ is a function of _**x**_ . The term exp {− _ψ(_ _**θ** )_ } is the normalization factor with which 

**==> picture [202 x 23] intentionally omitted <==**

is satisfied. Therefore, _ψ(_ _**θ** )_ is given by 

**==> picture [249 x 23] intentionally omitted <==**

_M_ = { _p(_ _**x** ,_ _**θ** )_ } is regarded as a manifold, where _**θ**_ is a coordinate system. By differentiating (1.41), we can prove that its Hessian is positive-definite (see the next subsection). Hence, _ψ(_ _**θ** )_ is a convex function. It is known as the cumulant generating function in statistics and free energy in statistical physics. The exponential family plays a fundamental role in information geometry. 

## _**1.3.2 Bregman Divergence**_ 

A graph of a convex function is shown in Fig. 1.4. We draw a tangent hyperplane touching it at point _**ξ**_ 0 (Fig. 1.4). It is given by the equation 

**==> picture [235 x 13] intentionally omitted <==**

where _z_ is the vertical axis of the graph. Here, ∇ is the gradient operator such that ∇ _ψ_ is the gradient vector defined by 

**==> picture [238 x 25] intentionally omitted <==**

1 Manifold, Divergence and Dually Flat Structure 

14 

**Fig. 1.4** Convex function _z_ = _ψ(ξ)_ , its supporting hyperplane with normal vector _**n**_ = ∇ _ψ (ξ_ 0 _)_ and divergence _D_ [ _ξ_ : _ξ_ 0] 

**==> picture [170 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
z<br>D [ : 0]<br>0<br>**----- End of picture text -----**<br>


in the component form. Since _ψ_ is convex, the graph of _ψ_ is always above the hyperplane, touching it at _**ξ**_ 0. Hence, it is a supporting hyperplane of _ψ_ at _**ξ**_ 0 (Fig. 1.4). We evaluate how high the function _ψ(_ _**ξ** )_ is at _**ξ**_ from the hyperplane (1.42). This depends on the point _**ξ**_ 0 at which the supporting hyperplane is defined. The difference from (1.42) is written as 

**==> picture [271 x 13] intentionally omitted <==**

Considering it as a function of two points _**ξ**_ and _**ξ**_ 0, we can easily prove that it satisfies the criteria of divergence. This is called the Bregman divergence [Bregman (1967)] derived from a convex function _ψ_ . 

We show examples of Bregman divergence. 

_Example 1.1_ ( _Euclidean divergence_ ) For _ψ_ defined by (1.37) in a Euclidean space, we easily see that the divergence is 

**==> picture [219 x 21] intentionally omitted <==**

that is, the same as a half of the square of the Euclidean distance. It is symmetric. 

_Example 1.2_ ( _Logarithmic divergence_ ) We consider a convex function 

**==> picture [207 x 29] intentionally omitted <==**

in the manifold _**R**[n]_ +[of positive measures. Its gradient is] 

**==> picture [205 x 25] intentionally omitted <==**

15 

1.3 Convex Function and Bregman Divergence 

Hence, the Bregman divergence is 

**==> picture [244 x 28] intentionally omitted <==**

For another convex function 

**==> picture [208 x 15] intentionally omitted <==**

the Bregman divergence is the same as the KL-divergence (1.31), given by 

**==> picture [248 x 25] intentionally omitted <==**

When[�] _ξi_ =[�] _ξi_[′][=][1,][this][is][the][KL-divergence][from][probability][vector] _**[ξ]**_[to] another _**ξ**_[′] . 

_Example 1.3_ ( _Free energy of exponential family_ ) We calculate the divergence given by the normalization factor _ψ(_ _**θ** )_ (1.41) of an exponential family. To this end, we differentiate the identity 

**==> picture [283 x 23] intentionally omitted <==**

with respect to _θi_ . We then have 

**==> picture [238 x 25] intentionally omitted <==**

or 

**==> picture [253 x 37] intentionally omitted <==**

where E denotes the expectation with respect to _p(_ _**x** ,_ _**θ** )_ and _x_ ¯ _i_ is the expectation of _xi_ . We then differentiate (1.52) again with respect to _θ j_ and, after some calculations, obtain 

**==> picture [248 x 27] intentionally omitted <==**

or 

**==> picture [256 x 14] intentionally omitted <==**

16 

1 Manifold, Divergence and Dually Flat Structure 

where _**x**[T]_ is the transpose of column vector _**x**_ and Var[ _**x**_ ] is the covariance matrix of _**x**_ , which is positive-definite. This shows that _ψ(_ _**θ** )_ is a convex function. It is useful to see that the expectation and covariance of _**x**_ are derived from _ψ(_ _**θ** )_ by differentiation. 

The Bregman divergence from _**θ**_ to _**θ**_[′] derived from _ψ_ of an exponential family is calculated from 

**==> picture [268 x 12] intentionally omitted <==**

proving that it is equal to the KL-divergence from _**θ**_[′] to _**θ**_ after careful calculations, 

**==> picture [282 x 26] intentionally omitted <==**

## **1.4 Legendre Transformation** 

The gradient of _ψ(_ _**ξ** )_ 

**==> picture [192 x 11] intentionally omitted <==**

is equal to the normal vector _**n**_ of the supporting tangent hyperplane at _**ξ**_ , as is easily seenfromFig. 1.4.Differentpointshavedifferentnormalvectors.Hence,itispossible to specify a point of _M_ by its normal vector. In other words, the transformation between _**ξ**_ and _**ξ**_[∗] is one-to-one and differentiable. This shows that _**ξ**_[∗] is used as another coordinate system of _M_ , which is connected with _**ξ**_ by (1.59). 

The transformation (1.59) is known as the Legendre transformation. The Legendre transformation has a dualistic structure concerning the two coupled coordinate systems _**ξ**_ and _**ξ**_[∗] . To show this, we define a new function of _**ξ**_[∗] by 

**==> picture [217 x 13] intentionally omitted <==**

where 

**==> picture [201 x 22] intentionally omitted <==**

and _**ξ**_ is not free but is a function of _**ξ**_[∗] , 

**==> picture [192 x 13] intentionally omitted <==**

which is the inverse function of _**ξ**_[∗] = ∇ _ψ(_ _**ξ** )_ . By differentiating (1.60) with respect to _**ξ**_[∗] , we have 

**==> picture [245 x 25] intentionally omitted <==**

1.4 Legendre Transformation 

17 

Since the last two terms of (1.63) cancel out because of (1.59), we have a dualistic structure 

**==> picture [229 x 13] intentionally omitted <==**

_ψ_[∗] is called the Legendre dual of _ψ_ . The dual function _ψ_[∗] satisfies 

**==> picture [235 x 18] intentionally omitted <==**

which is usually used as the definition of _ψ_[∗] . Our definition (1.60) is direct. We need to show _ψ_[∗] is a convex function. The Hessian of _ψ_[∗][�] _**ξ**_[∗][�] is written as 

**==> picture [229 x 24] intentionally omitted <==**

which is the Jacobian matrix of the inverse transformation from _**ξ**_[∗] to _**ξ**_ . This is the inverse of the Hessian **G** = ∇∇ _ψ(_ _**ξ** )_ , since it is the Jacobian matrix of the transformation from _**ξ**_ to _**ξ**_[∗] . Hence, it is a positive-definite matrix. This shows that _ψ_[∗][�] _**ξ**_[∗][�] is a convex function of _**ξ**_[∗] . A new Bregman divergence is derived from the dual convex function _ψ_[∗][�] _**ξ**_[∗][�] , 

**==> picture [302 x 13] intentionally omitted <==**

which we call the dual divergence. However, by calculating carefully, one can easily derive 

**==> picture [225 x 12] intentionally omitted <==**

Hence, the dual divergence is equal to the primal one if the order of two points is exchanged. Therefore, the divergences derived from the two convex functions are substantially the same, except for the order. 

It is convenient to use a self-dual expression of divergence by using the two coordinate systems. 

**Theorem 1.1** _The divergence from P to Q derived from a convex ψ(_ _**ξ** ) is written as_ 

**==> picture [254 x 13] intentionally omitted <==**

_where_ _**ξ** P is the coordinates of P in_ _**ξ** coordinate system and_ _**ξ**_[∗] _Q[is the coordinates] of Q in_ _**ξ**_[∗] _coordinate system._ 

_Proof_ From (1.60), we have 

**==> picture [226 x 13] intentionally omitted <==**

Substituting (1.70) in (1.69) and using ∇ _ψ_ � _**ξ** Q_ � = _**ξ**_[∗] _Q_[, we have the theorem.] 

1 Manifold, Divergence and Dually Flat Structure 

18 

We give examples of dual convex functions. For convex function (1.37) in Example 1.1, we easily have 

**==> picture [203 x 22] intentionally omitted <==**

and 

**==> picture [183 x 11] intentionally omitted <==**

Hence, the dual convex function is the same as the primal one, implying that the structure is self-dual. □ 

In the case of Example 1.2, the duals of _ψ_ and _ϕ_ in (1.46) and (1.49) are 

**==> picture [238 x 35] intentionally omitted <==**

by which 

**==> picture [230 x 13] intentionally omitted <==**

hold, respectively. 

In the case of the free energy _ψ(_ _**θ** )_ in Example 1.3, its Legendre transformation is 

**==> picture [213 x 11] intentionally omitted <==**

where E _**θ**_ is the expectation with respect to _p(_ _**x** ,_ _**θ** )_ . Because of this, _**θ**_[∗] is called the expectation parameter in statistics. The dual convex function _ψ_[∗][�] _**θ**_[∗][�] derived from (1.65) is calculated from 

**==> picture [219 x 13] intentionally omitted <==**

where _**θ**_ is a function of _**θ**_[∗] given by _**θ**_[∗] = ∇ _ψ(_ _**θ** )_ . This proves that _ψ_[∗] is the negative entropy, 

**==> picture [241 x 24] intentionally omitted <==**

The dual divergence derived from _ψ_[∗][�] _**θ**_[∗][�] is the KL-divergence 

**==> picture [255 x 13] intentionally omitted <==**

where _**θ**_ = ∇ _ψ_[∗] _(_ _**θ**_[∗] _)_ and _**θ**_[′] = ∇ _ψ_[∗][�] _**θ**_[∗′][�] . 

1.5 Dually Flat Riemannian Structure Derived from Convex Function 

19 

## **1.5 Dually Flat Riemannian Structure Derived from Convex Function** 

## _**1.5.1 Affine and Dual Affine Coordinate Systems**_ 

Whenafunction _ψ(_ _**θ** )_ isconvexinacoordinatesystem _**θ**_ ,thesamefunctionexpressed in another coordinate system _**ξ**_ , 

**==> picture [203 x 12] intentionally omitted <==**

is not necessarily convex as a function of _**ξ**_ . Hence, the convexity of a function depends on the coordinate system of _M_ . But a convex function remains convex 

**==> picture [195 x 10] intentionally omitted <==**

where **A** is a non-singular constant matrix and _**b**_ is a constant vector. 

We fix a coordinate system _**θ**_ in which _ψ(_ _**θ** )_ is convex and introduce geometric structures to _M_ based on it. We consider _**θ**_ as an affine coordinate system, which provides _M_ with an affine flat structure: _M_ is a flat manifold and each coordinate axis of _**θ**_ is a straight line. Any curve _**θ** (t)_ of _M_ written in the linear form of parameter _t_ , 

**==> picture [197 x 10] intentionally omitted <==**

is a straight line, where and _**a**_ and _**b**_ are constant vectors. We call it a geodesic of an affine manifold. Here, the term “geodesic” is used to represent a straight line and does not mean the shortest path connecting two points. A geodesic is invariant under affine transformations (1.81), but this is not true under nonlinear coordinate transformations. 

Dually, we can define another coordinate system _**θ**_[∗] by the Legendre transformation, 

**==> picture [194 x 11] intentionally omitted <==**

and consider it as another type of affine coordinates. This defines another affine structure. Each coordinate axis of _**θ**_[∗] is a dual straight line or dual geodesic. A dual straight line is written as 

**==> picture [199 x 10] intentionally omitted <==**

This is the dual affine structure derived from the convex function _ψ_[∗][�] _**θ**_[∗][�] . Since the coordinate transformation between the two affine coordinate systems _**θ**_ and _**θ**_[∗] is not linear in general, a geodesic is not a dual geodesic and vice versa. This implies that we have introduced two different criteria of straightness or flatness in _M_ , namely primal and dual flatness. _M_ is dually flat and the two flat coordinates are connected by the Legendre transformation. 

1 Manifold, Divergence and Dually Flat Structure 

20 

## _**1.5.2 Tangent Space, Basis Vectors and Riemannian Metric**_ 

When _d_ _**θ**_ is an (infinitesimally) small line element, the square of its length _ds_ is given by 

**==> picture [252 x 15] intentionally omitted <==**

Here, we use the upper indices _i, j_ to represent components of _**θ**_ . It is easy to see that the Riemannian metric _gi j_ is given by the Hessian of _ψ_ 

**==> picture [213 x 23] intentionally omitted <==**

Let { _**e** i , i_ = 1 _, . . . , n_ } be the set of tangent vectors along the coordinate curves of _**θ**_ (Fig. 1.5). The vector space spanned by { _**e** i_ } is the tangent space of _M_ at each point. Since _**θ**_ is an affine coordinate system, { _**e** i_ } looks the same at any point. A tangent vector _**A**_ is represented as 

**==> picture [195 x 15] intentionally omitted <==**

where _A[i]_ are the components of _**A**_ with respect to the basis vectors { _**e** i_ } _, i_ = 1 _, . . . , n_ . The small line element _d_ _**θ**_ is a tangent vector expressed as 

**==> picture [200 x 15] intentionally omitted <==**

Dually, we introduce a set of basis vectors � _**e**_[∗] _[i]_[�] which are tangent vectors of the dual affine coordinate curves of _**θ**_[∗] (Fig. 1.6). The small line element _d_ _**θ**_[∗] is expressed as 

**==> picture [203 x 15] intentionally omitted <==**

in this basis. A vector _**A**_ is represented in this basis as 

**==> picture [197 x 15] intentionally omitted <==**

**Fig. 1.5** Basis vectors _**e** i_ and small line element _d_ _**θ**_ 

**==> picture [218 x 104] intentionally omitted <==**

**----- Start of picture text -----**<br>
θ [j]<br>d<br>e j<br>θ [i]<br>e i<br>**----- End of picture text -----**<br>


1.5 Dually Flat Riemannian Structure Derived from Convex Function 

21 

**Fig. 1.6** Two dual bases { _**e** i_ } and � _**e**_[∗] _[i]_[�] 

**==> picture [305 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
θ [j]<br>θ [*] i<br>e j<br>e [*] [i] e i<br>θ [i]<br>e [*] [j]<br>θ *<br> j<br>**----- End of picture text -----**<br>


In order to distinguish affine and dual affine bases, we use the lower index as in _**e** i_ for the affine basis and the upper index as in _**e**_[∗] _[i]_ for the dual affine basis. Then, by using the lower and upper indices as in _A[i]_ and _Ai_ in the two bases, the components of a vector are naturally expressed without changing the letter _A_ but by changing the position of the index to upper or lower. Since they are the same vector expressed in different bases, 

**==> picture [220 x 15] intentionally omitted <==**

and _Ai_ ̸= _A[i]_ in general. 

It is cumbersome to use the summation symbol in Eqs.(1.87)–(1.91) and others. Even if the summation symbol is discarded, the reader may consider from the context that it has been omitted by mistake. In most cases, index _i_ appearing twice in one term, once as an upper index and the other time as a lower index, is summed over from 1 to _n_ . A. Einstein introduced the following summation convention: 

**Einstein Summation Convention** : When the same index appears twice in one term, once as an upper index and the other time as a lower index, summation is automatically taken over this index even without the summation symbol. 

We use this convention throughout the monograph, unless specified otherwise. Then, (1.91) is rewritten as 

**==> picture [204 x 12] intentionally omitted <==**

Since the square of the length _ds_ of a small line element _d_ _**θ**_ is given by the inner product of _d_ _**θ**_ , we have 

**==> picture [227 x 13] intentionally omitted <==**

which is rewritten as 

**==> picture [247 x 13] intentionally omitted <==**

1 Manifold, Divergence and Dually Flat Structure 

22 

Therefore, we have 

**==> picture [202 x 11] intentionally omitted <==**

This is the inner product of basis vectors _**e** i_ and _**e** j_ , which depends on position _**θ**_ . A manifold equipped with **G** = � _gi j_ �, by which the length of a small line element _d_ _**θ**_ is given by (1.93), is a Riemannian manifold. In the case of a Euclidean space with an orthonormal coordinate system, _gi j_ is given by 

**==> picture [186 x 11] intentionally omitted <==**

where _δi j_ is the Kronecker delta, which is equal to 1 for _i_ = _j_ and 0 otherwise. This is derived from convex function (1.37). A Euclidean space is a special case of the Riemannian manifold in which there is a coordinate system such that _gi j_ does not depend on position, in particular, written as (1.96). A manifold induced from a convex function is not Euclidean in general. 

The Riemannian metric can also be represented in the dual affine coordinate system _**θ**_[∗] . From the representation of a small line element _d_ _**θ**_[∗] as 

**==> picture [196 x 12] intentionally omitted <==**

we have 

**==> picture [234 x 14] intentionally omitted <==**

where _g_[∗] _[i j]_ is given by 

**==> picture [201 x 12] intentionally omitted <==**

From (1.66), we see that the components of the small line elements _d_ _**θ**_ and _d_ _**θ**_[∗] are related as 

**==> picture [228 x 27] intentionally omitted <==**

where **G** = **G**[∗−][1] . So the two Riemannian metric tensors are mutually inverse. This also implies that the two bases are related as 

**==> picture [219 x 13] intentionally omitted <==**

Hence, the inner product of two basis vectors _**e** i_ and _**e**_[∗] _j_[satisfies] 

**==> picture [195 x 14] intentionally omitted <==**

because **G** = **G**[∗−][1] . So the two bases { _**e** i_ } and � _**e**_[∗] _[i]_[�] are mutually dual or reciprocal (Fig. 1.6). Neither of the bases is orthonormal by itself in general, but the two together are complementarily orthogonal. Such a set of bases is useful, because the 

1.5 Dually Flat Riemannian Structure Derived from Convex Function 

23 

components of a vector _**A**_ are given by the inner product, 

**==> picture [227 x 11] intentionally omitted <==**

The two components are connected by 

**==> picture [222 x 13] intentionally omitted <==**

## _**1.5.3 Parallel Transport of Vector**_ 

A tangent vector _**A**_ = _A[i]_ _**e** i_ defined at a point _**θ**_ is transported to another point _**θ**_[′] without changing the components _A[i]_ , because _**e** i_ are the same everywhere in a dually flat manifold. This is a special case of parallel transport of a vector in a general nonflat manifold. As will be seen in Part II, the parallel transport of a vector needs to use an affine connection in the general case. But in our case of a dually flat manifold derived from a convex function _ψ(_ _**θ** )_ , the parallel transport is very simple. 

The dual parallel transport of _**A**_ is different from the parallel transport of _**A**_ . When _**A**_ is represented in the dual basis as 

**==> picture [189 x 11] intentionally omitted <==**

the dual transport does not change the components _Ai_ . However, it changes the components _A[i]_ , because the relation between _Ai_ and _A[i]_ depends on position _**θ**_ or _**θ**_[∗] , as is seen from (1.105), where _gi j_ and _g_[∗] _[i j]_ depend on _**θ**_ and _**θ**_[∗] . 

Since _M_ is Riemannian and is not Euclidean in general, even though the parallel transport is defined easily, the length of a vector changes by the parallel transport and the dual parallel transport. The square of the magnitude of _**A**_ is written as 

**==> picture [244 x 13] intentionally omitted <==**

Therefore, it depends on the position _**θ**_ , even though the components of _A[i]_ do not change by parallel transport. The inner product of vectors _**A**_ and _**B**_ is represented by various forms, 

**==> picture [247 x 13] intentionally omitted <==**

Two vectors _**A**_ and _**B**_ are orthogonal when ⟨ _**A** ,_ _**B**_ ⟩= 0. However, when both _**A**_ and _**B**_ are parallelly transported from _**θ**_ to _**θ**_[′] , the orthogonality does not hold in general at _**θ**_[′] even when it holds at _**θ**_ . However, when _**A**_ is transported in parallel and _**B**_ is transported in dual parallel, the orthogonality is kept invariant, because _A[i] Bi_ is invariant. This is an important property of two dually coupled parallel transports. 

1 Manifold, Divergence and Dually Flat Structure 

24 

## **1.6 Generalized Pythagorean Theorem and Projection Theorem** 

## _**1.6.1 Generalized Pythagorean Theorem**_ 

Two curves _**θ**_ 1 _(t)_ and _**θ**_ 2 _(t)_ intersect orthogonally when their tangent vectors 

**==> picture [203 x 47] intentionally omitted <==**

are orthogonal, that is, 

**==> picture [236 x 13] intentionally omitted <==**

˙ at the intersection point _t_ = 0, _**θ**_ 1 _(_ 0 _)_ = _**θ**_ 2 _(_ 0 _)_ and denotes _d/dt_ . 

Even though a manifold is flat from the point of view of affine structures, it is different from a Euclidean space. A dually flat manifold is a generalization of the Euclidean space. A generalized Pythagorean theorem holds in a dually flat manifold _M_ . 

Let us consider three points _P, Q, R_ in a dually flat manifold _M_ , which form a triangle. We call it an orthogonal triangle when the dual geodesic connecting _P_ and _Q_ is orthogonal to the geodesic connecting _Q_ and _R_ (Fig. 1.7). 

**Theorem 1.2** (Generalized Pythagorean Theorem) _When triangle P QR is orthogonal such that the dual geodesic connecting P and Q is orthogonal to the geodesic connecting Q and R, the following generalized Pythagorean relation holds:_ 

**==> picture [248 x 11] intentionally omitted <==**

**Fig. 1.7** Generalized orthogonal triangle _ΔPQR_ and Pythagorean theorem 

**==> picture [227 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
dual geodesic<br>P<br>R<br>Q geodesic<br>**----- End of picture text -----**<br>


25 

1.6 Generalized Pythagorean Theorem and Projection Theorem 

_Proof_ By using the relation 

**==> picture [255 x 13] intentionally omitted <==**

we have 

**==> picture [312 x 13] intentionally omitted <==**

after some calculations. The dual geodesic connecting _P_ and _Q_ is written as 

**==> picture [224 x 13] intentionally omitted <==**

in the parametric form. Its tangent vector is given by 

**==> picture [208 x 15] intentionally omitted <==**

Dually, the geodesic connecting _Q_ and _R_ is 

**==> picture [222 x 11] intentionally omitted <==**

and its tangent vector is 

**==> picture [207 x 13] intentionally omitted <==**

Since the two tangent vectors are orthogonal, we have 

**==> picture [225 x 13] intentionally omitted <==**

The Pythagorean relation is proved from (1.114). 

**==> picture [9 x 8] intentionally omitted <==**

Since the divergence is asymmetric, we have the dual statement. 

**Theorem 1.3** (Dual Pythagorean Theorem) _When triangle P QR is orthogonal such that the geodesic connecting P and Q is orthogonal to the dual geodesic connecting Q and R, the dual of the generalized Pythagorean relation holds,_ 

**==> picture [252 x 11] intentionally omitted <==**

In the special case of convex function (1.37), the divergence is exactly a half of the square of the Euclidean distance. Moreover, the affine coordinate system is exactly the same as the dual affine coordinate system, because the affine structure is self-dual. Hence, a geodesic is a dual geodesic at the same time. In this case, the generalized Pythagorean relation reduces to the Pythagorean relation in a Euclidean space. The theorems are indeed a generalization of the Pythagorean theorem of a Euclidean space to a dually flat manifold. 

26 

1 Manifold, Divergence and Dually Flat Structure 

## _**1.6.2 Projection Theorem**_ 

Consider a point _P_ and a smooth submanifold _S_ in a dually flat manifold _M_ . Then, the divergence from a point _P_ to submanifold _S_ is defined by 

**==> picture [226 x 15] intentionally omitted <==**

We study the problem of finding the point in _S_ that is closest to _P_ in the sense of divergence. This gives an approximation of _P_ by using a point inside _S_ . The Pythagorean theorem is useful for solving various approximation problems. 

We define the geodesic projection and the dual geodesic projection of _P_ to _S_ ⊂ _M_ . A curve _**θ** (t)_ is said to be orthogonal to _S_ when its tangent vector _**θ**_[˙] _(t)_ is orthogonal to any tangent vectors of _S_ at the intersection (Fig. 1.8). 

**Definition 1.2** _P_ ˆ _S_ is the geodesic projection of _P_ to _S_ when the geodesic connecting _P_ and _P_[ˆ] _S_ ∈ _S_ is orthogonal to _S_ . Dually, _P_[ˆ] _S_[∗][is the dual geodesic projection of] _[P]_[to] _S_ , when the dual geodesic connecting _P_ and _P_[ˆ] _S_[∗][∈] _[S]_[ is orthogonal to] _[ S]_[. See Fig.][1.8][.] 

We then have the projection theorem: 

**Theorem 1.4** (Projection Theorem) _Given P_ ∈ _M and a smooth submanifold S_ ⊂ _M, the point P_[ˆ] _S_[∗] _[that][minimizes][the][divergence][D][ψ]_[[] _[P]_[:] _[R]_[]] _[,][ R]_[∈] _[S,][is][the] dual geodesic projection of P to S. The point P_[ˆ] _S that minimizes the dual divergence Dψ_[∗] [ _P_ : _R_ ] _, R_ ∈ _S, is the geodesic projection of P to S._ 

_Proof_ Let _P_[ˆ] _S_[∗][bethedualgeodesicprojectionof] _[ P]_[ to] _[ S]_[.Considerapoint] _[ Q]_[∈] _[S]_[ which] is (infinitesimally) close to _P_[ˆ] _S_[∗][. Then, three points] _[P]_[,] _[P]_[ˆ] _S_[∗][and] _[Q]_[ form an orthogonal] triangle, because the small line element connecting _P_[ˆ] _S_[∗][and] _[Q]_[is orthogonal][to the] the dual geodesic connecting _P_ and _P_[ˆ] _S_[∗][. Hence, the Pythagorean theorem shows] 

**==> picture [254 x 27] intentionally omitted <==**

**Fig. 1.8** Geodesic projection of _P_ to _S_ 

**==> picture [76 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>P<br>geodesic S<br>. [.] Q<br>Ps<br>**----- End of picture text -----**<br>


1.6 Generalized Pythagorean Theorem and Projection Theorem 

27 

for any neighboring _Q_ . This shows that _P_[ˆ] _S_[∗][is a critical point of] _[D][ψ]_[[] _[P]_[:] _[Q]_[]][,] _[Q]_[∈] _[S]_[,] proving the theorem. The dual part is proved similarly. □ 

It should be noted that the projection theorem gives a necessary condition for the point _P_[ˆ] _S_[∗][to][minimize][the][divergence,][but][is][not][sufficient.][The][projection][or][dual] projection can give the maximum or saddle point of the divergence. The following theorem gives a sufficient condition for the minimality of the projection and its uniqueness. 

**Theorem 1.5** _When S is a flat submanifold of a dually flat manifold M, the dual projection of P to S is unique and minimizes the divergence. Dually, when S is a dual flat submanifold of a dually flat manifold M, the projection of P to S is unique and minimizes the dual divergence._ 

_Proof_ The Pythagorean relations (1.112), (1.120) hold for any _Q_ ∈ _S_ . Hence the projection (dual projection) is unique and minimizes the dual divergence (divergence). □ 

## _**1.6.3 Divergence Between Submanifolds: Alternating Minimization Algorithm**_ 

When there are two submanifolds _K_ and _S_ in a dually flat _M_ , we define a divergence between _K_ and _S_ by 

**==> picture [258 x 18] intentionally omitted <==**

The two points _P_[¯] ∈ _K_ and _Q_[¯] ∈ _S_ are the closest pair between _K_ and _S_ . In order to obtain the closest pair, the following iterative algorithm, the alternating minimization algorithm, is proposed. See Fig. 1.9. 

**Fig. 1.9** Iterated dual geodesic projections ( _em_ algorithm) 

**==> picture [199 x 112] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pt K<br>Pt +1<br>P*<br>.<br>...<br>.<br>Q*<br>Q t Q t +1 S<br>**----- End of picture text -----**<br>


1 Manifold, Divergence and Dually Flat Structure 

28 

Beginwithanarbitrary _Qt_ ∈ _S_ , _t_ = 0 _,_ 1 _, . . ._ ,andsearchfor _P_ ∈ _K_ thatminimizes _D_ [ _P_ : _Qt_ ]. This is given by the geodesic projection of _Qt_ to _K_ . Let it be _Pt_ ∈ _K_ . Then search for the point in _S_ that minimizes _D_ [ _Pt_ : _Q_ ]. Let it be _Qt_ +1. This is given by the dual geodesic projection of _Pt_ to _S_ . Since we have 

**==> picture [261 x 13] intentionally omitted <==**

the procedure converges. It is unique when _S_ is flat and _K_ is dual flat. Otherwise, the converging point is not necessarily unique. 

In later sections, the geodesic projection is called the _e_ -projection, signifying the exponential projection, and the dual geodesic projection is called the _m_ -projection, signifying the mixture projection. By this reason, this alternating primal and dual geodesic projection algorithm is called the _em_ algorithm. 

## **Remarks** 

A dually flat Riemannian structure is derived from the Bregman divergence by using a convexfunction.Ithasadualisticstructure.However,notalldivergencesareBregman divergences, that is, not necessarily derived from convex functions. An interesting question is what type of geometry is induced from such a general divergence. This question will be studied in Part II. Briefly speaking, it gives a Riemannian manifold with a dual pair of affine connections which are not flat. There are no affine coordinate systems in such cases. 

A dually flat manifold is a generalization of a Euclidean space, inheriting useful properties from it. A general non-flat manifold is regarded as a curved submanifold of a dually flat manifold, as a Riemannian manifold is a curved submanifold of a Euclidean space with higher dimensions. Therefore, it is important to study the properties of a dually flat manifold. 

The Pythagorean theorem and related projection theorem are highlights of a dually flat manifold, proposed in Nagaoka and Amari (1982). However, this work was not published in a journal, because, unfortunately, it was rejected by major journals. These theorems play important roles in most applications of information geometry. The Pythagorean theorem has been known for many years in the case of the KLdivergence. It is information geometry that has generalized the Pythagorean relation applicable to any Bregman divergence. Conversely, when a manifold is dually flat from the geometrical point of view, we can prove that there is a convex function from which the dually flat structure is derived. This will be explained later. 

We add a comment on the notation. There are many coordinate systems in a coordinate neighborhood of a manifold, because when _**ξ**_ is a coordinate system, its transform _**ζ**_ = _(ζ_ 1 _, . . . , ζn)_ , 

**==> picture [266 x 11] intentionally omitted <==**

1.6 Generalized Pythagorean Theorem and Projection Theorem 

29 

is another coordinate system, provided _**f**_ is differentiable and invertible. The Jacobian matrix **J** = _(Jκi )_ of the coordinate transformation 

**==> picture [220 x 24] intentionally omitted <==**

is non-degenerate, that is, matrix **J** is invertible. 

Here we use indices _i, j, . . ._ to represent components in the coordinate system _**ξ**_ = _(ξi ) , i_ = 1 _, . . . , n_ and Greek indices _κ, λ, ν, . . ._ for the coordinate system _**ζ**_ = _(ζκ) , κ_ = 1 _, . . . , n_ . This is a convenient way of distinguishing coordinate systems. For example, a small line element connecting _P_ and _P_ + _d P_ is _d_ _**ξ**_ = _(dξi )_ in coordinate system _**ξ**_ and _d_ _**ζ**_ = _(dζκ)_ in coordinate system _**ζ**_ , and they are linearly connected by 

**==> picture [203 x 23] intentionally omitted <==**

When _ds_ is a local distance written as 

**==> picture [208 x 15] intentionally omitted <==**

in the coordinate system _**ξ**_ , it can be written as 

**==> picture [210 x 15] intentionally omitted <==**

in coordinate system _**ζ**_ . Here, � _gi j_ � and _(gκλ)_ are different matrices connected by 

**==> picture [208 x 23] intentionally omitted <==**

Such a quantity is called a tensor. We use the same letter _g_ for the Riemannian metric tensor, but indices _i_ , _j_ or _κ_ , _λ_ distinguish the coordinate system in which it is represented. In general, we may use the same letter for a quantity even if it is represented in different coordinate systems, distinguishing them by the letter types of indices. This is convenient for the index notation, introduced by Schouten (1954). We mainly follow this idea. 

We may choose any coordinate system. The geometry should be the same whichever coordinate system we use. Mathematicians often do not like to use a coordinate system, because geometry should not depend on it. They say that the index notation is an ugly classic method of differential geometry, where tensors are represented by quantities having indices. So they use the coordinate-free method of abstract description. This is sometimes elegant. However, it is wiser to choose an adequate coordinate system, because the geometry is the same in whichever coordinate system it is analyzed. For Euclidean geometry, an orthonormal coordinate system is usually preferable. However, when we analyze a boundary value problem of the 

1 Manifold, Divergence and Dually Flat Structure 

30 

heat equation in a Euclidean space, if the boundary is a circle, the polar coordinate system makes the boundary condition very simple. So in such a case, we use this. Any coordinate system is permissible, but it is advisable to use a convenient one, instead of rejecting the usage of a coordinate system. This is the way in which engineers and physicists work. 

## **Chapter 2 Exponential Families and Mixture Families of Probability Distributions** 

The present chapter studies the geometry of the exponential family of probability distributions. It is not only a typical statistical model, including many well-known families of probability distributions such as discrete probability distributions _Sn_ , Gaussian distributions, multinomial distributions, gamma distributions, etc., but is associated with a convex function known as the cumulant generating function or free energy. The induced Bregman divergence is the KL-divergence. It defines a dually flat Riemannian structure. The derived Riemannian metric is the Fisher information matrix and the two affine coordinate systems are the natural (canonical) parameters and expectation parameters, well-known in statistics. An exponential family is a universal model of dually flat manifolds, because any Bregman divergence has a corresponding exponential family of probability distributions (Banerjee et al. 2005). 

We also study the mixture family of probability distributions, which is the dual of the exponential family. Applications of the generalized Pythagorean theorem demonstrate how useful this is. 

## **2.1 Exponential Family of Probability Distributions** 

The standard form of an exponential family is given by the probability density function 

**==> picture [249 x 12] intentionally omitted <==**

where _x_ is a random variable, _**θ**_ = _θ_[1] _, . . . , θ[n]_ is an _n_ -dimensional vector parameter to specify a distribution, _hi (x)_ are _n_ functions of _x_ which are linearly independent, _k(x)_ is a function of _x_ , _ψ_ corresponds to the normalization factor and the Einstein summation convention is working. We introduce a new vector random variable _**x**_ = _(x_ 1 _, . . . , xn)_ by 

**==> picture [190 x 10] intentionally omitted <==**

The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_2 

31 

2 Exponential Families and Mixture Families of Probability _. . ._ 

32 

We further introduce a measure in the sample space _X_ = { _**x**_ } by 

**==> picture [215 x 10] intentionally omitted <==**

Then, (2.1) is rewritten as 

**==> picture [246 x 10] intentionally omitted <==**

Hence, we may put 

**==> picture [228 x 10] intentionally omitted <==**

which is a probability density function of _**x**_ with respect to measure _dμ(_ _**x** )_ . The family of distributions 

**==> picture [197 x 10] intentionally omitted <==**

forms an _n_ -dimensional manifold, where _**θ**_ is a coordinate system. From the normalization condition 

**==> picture [211 x 23] intentionally omitted <==**

_ψ_ is written as 

**==> picture [231 x 23] intentionally omitted <==**

We proved in Chap. 1 that _ψ(_ _**θ** )_ is a convex function of _**θ**_ , known as the cumulant generating function in statistics and free energy in physics. A dually flat Riemannian structure is introduced in _M_ by using _ψ(_ _**θ** )_ . The affine coordinate system is _**θ**_ , which is called the natural or canonical parameter of an exponential family. The dual affine parameter is given by the Legendre transformation, 

**==> picture [194 x 10] intentionally omitted <==**

which is the expectation of _**x**_ denoted by _**η**_ = _(η_ 1 _, . . . , ηn)_ , 

**==> picture [231 x 23] intentionally omitted <==**

This _**η**_ is called the expectation parameter in statistics. Since the dual affine parameter _**θ**_[∗] is nothing other than _**η**_ , we hereafter use _**η**_ , instead of _**θ**_[∗] , to represent the dual affine parameter in an exponential family. This is a conventional notation used in Amari and Nagaoka (2000), avoiding the cumbersome ∗ notation. So we have 

**==> picture [192 x 10] intentionally omitted <==**

Hence, _**θ**_ and _**η**_ are two affine coordinate systems connected by the Legendre transformation. 

2.1 Exponential Family of Probability Distributions 

33 

We use _ϕ(_ _**η** )_ to denote the dual convex function _ψ_[∗][�] _**θ**_[∗][�] , the Legendre dual of _ψ_ , which is defined by 

**==> picture [225 x 15] intentionally omitted <==**

In order to obtain _ϕ(_ _**η** )_ , we calculate the negative entropy of _p(_ _**x** ,_ _**θ** )_ , obtaining 

**==> picture [307 x 23] intentionally omitted <==**

Given _**η**_ , the _**θ**_ that maximizes the right-hand side of (2.12) is given by the solution of _**η**_ = ∇ _ψ(_ _**θ** )_ . Hence, the dual convex function _ψ_[∗] of _ψ_ , which we hereafter denote as _ϕ_ , is given by the negative entropy, 

**==> picture [236 x 23] intentionally omitted <==**

where _**θ**_ is regarded as a function of _**η**_ through _**η**_ = ∇ _ψ(_ _**θ** )_ . The inverse transformation is given by 

**==> picture [192 x 10] intentionally omitted <==**

The divergence from _p(_ _**x** ,_ _**θ**_[′] _)_ to _p(_ _**x** ,_ _**θ** )_ is written as 

**==> picture [291 x 42] intentionally omitted <==**

This implies that the KL-divergence is the dual of the canonical divergence derived from _ψ_ . 

The Riemannian metric is given by 

**==> picture [207 x 11] intentionally omitted <==**

**==> picture [208 x 12] intentionally omitted <==**

for which we hereafter use the abbreviation 

**==> picture [213 x 24] intentionally omitted <==**

Here, the position of the index _i_ is important. If it is lower, as in _∂i_ , the differentiation is with respect to _θ[i]_ , whereas, if it is upper as in _∂[i]_ , the differentiation is with respect to _ηi_ . 

The Fisher information matrix plays a fundamental role in statistics. We prove the following theorem which connects geometry and statistics. 

**Theorem 2.1** _The Riemannian metric in an exponential family is the Fisher information matrix defined by_ 

2 Exponential Families and Mixture Families of Probability _. . ._ 

34 

**==> picture [245 x 13] intentionally omitted <==**

_Proof_ From 

**==> picture [248 x 10] intentionally omitted <==**

we have 

**==> picture [298 x 13] intentionally omitted <==**

which is equal to ∇∇ _ψ(_ _**θ** )_ . This is the Riemannian metric derived from _ψ(_ _**θ** )_ , as is shown in (1.56). □ 

□ 

## **2.2 Examples of Exponential Family: Gaussian and Discrete Distributions** 

There are many statistical models belonging to the exponential family. Here, we show only two well-known, important distributions. 

## _**2.2.1 Gaussian Distribution**_ 

The Gaussian distribution with mean _μ_ and variance _σ_[2] has the probability density function 

**==> picture [247 x 26] intentionally omitted <==**

We introduce a new vector random variable _**x**_ = _(x_ 1 _, x_ 2 _)_ , 

**==> picture [202 x 24] intentionally omitted <==**

Note that _x_ and _x_[2] are dependent, but are linearly independent. We further introduce new parameters 

**==> picture [192 x 20] intentionally omitted <==**

**==> picture [192 x 22] intentionally omitted <==**

Then, (2.23) is written in the standard form, 

**==> picture [227 x 10] intentionally omitted <==**

The convex function _ψ(_ _**θ** )_ is given by 

35 

2.2 Examples of Exponential Family: Gaussian and Discrete Distributions 

**==> picture [252 x 53] intentionally omitted <==**

Since _x_ 1 and _x_ 2 are not independent but satisfy the relation 

**==> picture [191 x 12] intentionally omitted <==**

we use the dominating measure of 

**==> picture [217 x 13] intentionally omitted <==**

where _δ_ is the delta function. 

The dual affine coordinates _**η**_ are given from (2.10) as 

**==> picture [216 x 12] intentionally omitted <==**

## _**2.2.2 Discrete Distribution**_ 

Distributions of discrete random variable _x_ over _X_ = {0 _,_ 1 _, . . . , n_ } form a probability simplex _Sn_ . A distribution _**p**_ = _( p_ 0 _, p_ 1 _, . . . , pn)_ is represented by 

**==> picture [206 x 28] intentionally omitted <==**

We show that _Sn_ is an exponential family. We have 

**==> picture [299 x 63] intentionally omitted <==**

36 

2 Exponential Families and Mixture Families of Probability _. . ._ 

because of 

**==> picture [213 x 29] intentionally omitted <==**

We introduce new random variables _xi_ , 

**==> picture [237 x 9] intentionally omitted <==**

and new parameters 

**==> picture [256 x 151] intentionally omitted <==**

Then, a discrete distribution _**p**_ is written from (2.34) as 

where the cumulant generating function is 

The dual affine coordinates _**η**_ are 

**==> picture [276 x 65] intentionally omitted <==**

The dual convex function is the negative entropy, 

By differentiating it, we have _**θ**_ = ∇ _ϕ(_ _**η** )_ . 

**==> picture [206 x 22] intentionally omitted <==**

## **2.3 Mixture Family of Probability Distributions** 

A mixture family is in general different from an exponential family, but family _Sn_ of discrete distributions is an exponential family and a mixture family at the same time. We show that the two families play a dual role. 

Given _n_ + 1 probability distributions _q_ 0 _(x), q_ 1 _(x), . . . , qn(x)_ which are linearly independent, we compose a family of probability distributions given by 

2.3 Mixture Family of Probability Distributions 

37 

**==> picture [212 x 28] intentionally omitted <==**

where 

**==> picture [208 x 29] intentionally omitted <==**

This is a statistical model called a mixture family, where _**η**_ = _(η_ 1 _, . . . , ηn)_ is a coordinate system and _η_ 0 = 1 −[�] _ηi_ . (We sometimes consider the closure of the above family, where _ηi_ ≥ 0.) 

As is easily seen from (2.33), a discrete distribution _p(x)_ ∈ _Sn_ is a mixture family, where 

**==> picture [254 x 10] intentionally omitted <==**

Hence, _**η**_ is a dual affine coordinate system of the exponential family _Sn_ . We consider a general mixture family (2.43) which is not an exponential family. Even in this case, the negative entropy 

**==> picture [234 x 23] intentionally omitted <==**

is a convex function of _**η**_ . Therefore, we regard it as a dual convex function and introduce the dually flat structure to _M_ = { _p(x,_ _**η** )_ }, having _**η**_ as the dual affine coordinate system. Then, the primary affine coordinates are given by the gradient, 

**==> picture [192 x 10] intentionally omitted <==**

It defines the primal affine structure dually coupled with _**η**_ , although _**θ**_ is not the natural parameter of an exponential family, except for the case of _Sn_ where _**θ**_ is the natural parameter. 

The divergence given by _ϕ(_ _**η** )_ is the KL-divergence 

**==> picture [251 x 24] intentionally omitted <==**

## **2.4 Flat Structure:** _**e m**_ 

The manifold _M_ of exponential family is dually flat. The primal affine coordinates which define straightness or flatness are the natural parameter _**θ**_ in an exponential family. Let us consider the straight line, that is a geodesic, connecting two distributions _p(_ _**x** ,_ _**θ**_ 1 _)_ and _p(_ _**x** ,_ _**θ**_ 2 _)_ . This is written in the _**θ**_ coordinate system as 

**==> picture [216 x 10] intentionally omitted <==**

2 Exponential Families and Mixture Families of Probability _. . ._ 

38 

where _t_ is the parameter. The probability distributions on the geodesic are 

**==> picture [299 x 10] intentionally omitted <==**

Hence, a geodesic itself is a one-dimensional exponential family, where _t_ is the natural parameter. 

By taking the logarithm, we have 

**==> picture [297 x 10] intentionally omitted <==**

Therefore, a geodesic consists of a linear interpolation of the two distributions in the logarithmic scale. Since (2.51) is an exponential family, we call it an _e_ -geodesic, _e_ standing for “exponential”. More generally, a submanifold which is defined by linear constraints in _**θ**_ is said to be _e_ -flat. The affine parameter _**θ**_ is called the _e_ -affine parameter. 

The dual affine coordinates are _**η**_ , and define the dual flat structure. The dual geodesic connecting two distributions specified by _**η**_ 1 and _**η**_ 2 is given by 

**==> picture [215 x 10] intentionally omitted <==**

in terms of the dual coordinate system. Along the dual geodesic, the expectation of _**x**_ is linearly interpolated, 

**==> picture [240 x 11] intentionally omitted <==**

In the case of discrete probability distributions _Sn_ , the dual geodesic connecting _**p**_ 1 and _**p**_ 2 is 

**==> picture [215 x 10] intentionally omitted <==**

which is a mixture of two distributions _**p**_ 1 and _**p**_ 2. Hence, a dual geodesic is a mixture of two probability distributions. We call a dual geodesic an _m_ -geodesic and, by this reasoning, _**η**_ is called the _m_ -affine parameter, where _m_ stands for “mixture”. A submanifold which is defined by linear constraints in _**η**_ is said to be _m_ -flat. The linear mixture 

**==> picture [226 x 13] intentionally omitted <==**

is not included in _M_ in general, but _p_ � _**x** , (_ 1 − _t)_ _**η**_ 1 + _t_ _**η**_ 2� is in _M_ , where we used the abuse of notation _p(_ _**x** ,_ _**η** )_ to specify the distribution of _M_ of which dual coordinates are _**η**_ . 

_Remark_ An _m_ -geodesic (2.52) is not a linear mixture of two distributions specified by _**η**_ 1 and _**η**_ 2 in the case of a general exponential family. However, we use the term _m_ -geodesic even in this case. 

2.5 On Infinite-Dimensional Manifold of Probability Distributions 

39 

## **2.5 On Infinite-Dimensional Manifold of Probability Distributions** 

We have shown that _Sn_ of discrete probability distributions is an exponential family and a mixture family at the same time. It is a super-manifold, in which any statistical model of a discrete random variable is embedded as a submanifold. When _x_ is a continuous random variable, we are apt to consider the geometry of the manifold _F_ of all probability density functions _p(x)_ in a similar way. It is a super-manifold including all statistical models of a continuous random variable. It is considered to be an exponential family and a mixture family at the same time. However, the problem is not mathematically easy, since it is a function space of infinite dimensions. We show a naive idea of studying the geometry of _F_ . This is not mathematically justified, although it works well in most cases, except for “pathological” situations. 

Let _p(x)_ be a probability density function of real random variable _x_ ∈ _**R**_ , which is mutually absolutely continuous with respect to the Lebesgue measure.[1] We put 

**==> picture [251 x 25] intentionally omitted <==**

Then, _F_ is a function space consisting of _L_ 1 functions. For two distributions _p_ 1 _(x)_ and _p_ 2 _(x)_ , the exponential family connecting them is written as 

**==> picture [282 x 11] intentionally omitted <==**

provided it exists in _F_ . Also the mixture family connecting them 

**==> picture [237 x 10] intentionally omitted <==**

is assumed to belong to _F_ . Then, _F_ is regarded as an exponential and a mixture family at the same time as _Sn_ is. Mathematically, there is a delicate problem concerning the topology of _F_ . The _L_ 1-topology and _L_ 2-topology of the function space _F_ are different. Also the topology induced by _p(x)_ is different from that induced by log _p(x)_ . 

Disregarding such mathematical problems, we discretize the real line _**R**_ into _n_ + 1 intervals, _I_ 0 _, I_ 1 _, . . . , In_ . Then, the discretized version of _p(x)_ is given by the discrete probability distribution _**p**_ = _( p_ 0 _, p_ 1 _, . . . , pn)_ , 

**==> picture [237 x 24] intentionally omitted <==**

1 It would be better to use density function _p(x)_ with respect to the Gaussian measure 

**==> picture [109 x 23] intentionally omitted <==**

rather than the Lebsesque measure _dx_ . 

2 Exponential Families and Mixture Families of Probability _. . ._ 

40 

This gives a mapping from _F_ to _Sn_ , which approximates _p(x)_ by _**p**_ ∈ _Sn_ . When the discretization is done in such a way that _pi_ in each interval converges to 0 as _n_ tends to infinity, the approximation looks fine. Then, the geometry of _F_ would be defined by the limit of _Sn_ consisting of discretized _**p**_ . However, we have difficulty in this approach. The limit _n_ →∞ of the geometry of _Sn_ might not be unique, depending on the method of discretization. Moreover, an admissible discretization would be different for different _p(_ _**x** )_ . 

Forgetting about the difficulty, by using the delta function _δ(x)_ , let us introduce a family of random variables _δ(s_ − _x)_ indexed by a real parameter _s_ , which plays the role of index _i_ in _δi (x)_ of _Sn_ . Then, we have 

**==> picture [221 x 23] intentionally omitted <==**

which shows that _F_ is a mixture family generated by the delta distributions _δ(s_ − _x)_ , _s_ ∈ _**R**_ . Here, _p(s)_ are mixing coefficients. Similarly, we have 

**==> picture [246 x 25] intentionally omitted <==**

where 

**==> picture [208 x 10] intentionally omitted <==**

and _ψ_ is a functional of _θ(s)_ formally given by 

**==> picture [236 x 25] intentionally omitted <==**

Hence, _F_ is an exponential family where _θ(s)_ = log _p(s)_ + _ψ_ is the _**θ**_ affine coordinates and _η(s)_ = _p(s)_ is the dual affine coordinates _**η**_ . The dual convex function is 

**==> picture [227 x 23] intentionally omitted <==**

Indeed the dual coordinates are given by 

**==> picture [225 x 11] intentionally omitted <==**

and we have 

**==> picture [203 x 10] intentionally omitted <==**

where ∇ is the Fréchet-derivative with respect to function _θ(s)_ . The _e_ -geodesic connecting _p(x)_ and _q(x)_ is (2.57) and the _m_ -geodesic (2.58). The tangent vector of an _e_ -geodesic is 

2.5 On Infinite-Dimensional Manifold of Probability Distributions 

41 

**==> picture [259 x 22] intentionally omitted <==**

in the _e_ -coordinates, and that of an _m_ -geodesic is 

**==> picture [212 x 10] intentionally omitted <==**

in the _m_ -coordinates. The KL-divergence is 

**==> picture [259 x 25] intentionally omitted <==**

which is the Bregman divergence derived from _ψ_ [ _θ_ ] and it gives _F_ a dually flat structure. The Pythagorean theorem is written, for three distributions _p(x)_ , _q(x)_ and _r (x)_ , as 

**==> picture [303 x 10] intentionally omitted <==**

when the mixture geodesic connecting _p_ and _q_ is orthogonal to the exponentialgeodesic connecting _q_ and _r_ , that is, when 

**==> picture [261 x 23] intentionally omitted <==**

It is easy to prove this directly. The projection theorem follows similarly. 

The KL-divergence between two nearby distributions _p(x)_ and _p(x)_ + _δ p(x)_ is expanded as 

**==> picture [287 x 54] intentionally omitted <==**

Hence, the squared distance of an infinitesimal deviation _δ p(x)_ is 

**==> picture [213 x 26] intentionally omitted <==**

which defines the Riemannian metric given by the Fisher information. Indeed, the Riemannian metric in _**θ**_ -coordinates are given by 

**==> picture [230 x 10] intentionally omitted <==**

2 Exponential Families and Mixture Families of Probability _. . ._ 

42 

and its inverse is 

**==> picture [218 x 24] intentionally omitted <==**

in _**η**_ -coordinates. 

It appears that most of the results we have studied in _Sn_ hold well even in the function space _F_ with naive treatment. They are practically useful even though no mathematical justification is given. Unfortunately, we are not free from mathematical difficulties. We show some examples. 

The pathological nature in the continuous case has long been known. The following fact was pointed out by Csiszár (1967). We define a quasi- _ε_ -neighborhood of _p(x)_ based on the KL-divergence, 

**==> picture [243 x 10] intentionally omitted <==**

However, the set of the quasi- _ε_ -neighborhoods does not satisfy the axiom of the topological subbase. Hence, we cannot use the KL-divergence to define the topology. More simply, it is demonstrated that the entropy functional 

**==> picture [229 x 23] intentionally omitted <==**

is not continuous in _F_ , whereas it is continuous and differentiable in _Sn_ (Ho and Yeung 2009). 

G. Pistone and his co-workers studied the geometrical properties of _F_ based on the theory of Orlicz space, where _F_ is not a Hilbert space but a Banach space. See Pistone and Sempi (1995), Gibilisco and Pistone (1998), Pistone and Rogathin (1999), Cena and Pistone (2007). This was further developed by Grasselli (2010). See recent works by Pistone (2013) and Newton (2012), where trials for mathematical justification using innocent ideas have been developed. 

## **2.6 Kernel Exponential Family** 

Fukumizu (2009) proposed a kernel exponential family, which is a model of probability distributions of function degrees of freedom. Let _k(x, y)_ be a kernel function satisfying positivity, 

**==> picture [227 x 23] intentionally omitted <==**

for any _f (x)_ not equal to 0. A typical example is the Gaussian kernel 

**==> picture [252 x 25] intentionally omitted <==**

where _σ_ is a free parameter. 

2.6 Kernel Exponential Family 

43 

A kernel exponential family is defined by 

**==> picture [251 x 25] intentionally omitted <==**

with respect to suitable measure _dμ(x)_ , e.g., 

**==> picture [220 x 26] intentionally omitted <==**

The natural or canonical parameter is a function _θ(y)_ indexed by _y_ instead of _θ[i]_ and the dual parameter is 

**==> picture [205 x 10] intentionally omitted <==**

where expectation is taken by using _p(x, θ)_ . _ψ_ [ _θ_ ] is a convex functional of _θ(y)_ . This exponential family does not cover all _p(x)_ of probability density functions. So there are many such models, depending on _k(x, y)_ and _dμ(x)_ . The naive treatment in Sect. 2.5 may be regarded as the special case where the kernel _k(x, y)_ is put equal to the delta function _δ(x_ − _y)_ . 

## **2.7 Bregman Divergence and Exponential Family** 

An exponential family induces a Bregman divergence _Dψ_ � _**θ**_ : _**θ**_[′][�] given in (2.16). Conversely, when a Bregman divergence _Dψ_ � _**θ**_ : _**θ**_[′][�] is given, is it possible to find a corresponding exponential family _p(_ _**x** ,_ _**θ** )_ ? The problem is solved positively by Banerjee et al. (2005). Consider a random variable _**x**_ . It specifies a point _**η**_[′] = _**x**_ in the _**η**_ -coordinates of a dually flat manifold given by _ψ_ . Let _**θ**_[′] be its _**θ**_ -coordinates. The _ψ_ -divergence from _**θ**_ to _**θ**_[′] , the latter of which is the _**θ**_ -coordinates of _**η**_[′] = _**x**_ , is written as 

**==> picture [246 x 13] intentionally omitted <==**

Using this, we define a probability density function written in terms of the divergence as 

**==> picture [302 x 13] intentionally omitted <==**

where _**θ**_[′] is determined from _**x**_ as the _**θ**_ -coordinates of _**η**_[′] = _**x**_ . Thus, we have an exponential family derived from _Dψ_ . 

The problem is restated as follows: Given a convex function _ψ(_ _**θ** )_ , find a measure _dμ(_ _**x** )_ such that (2.8), or equivalently 

**==> picture [237 x 23] intentionally omitted <==**

2 Exponential Families and Mixture Families of Probability _. . ._ 

44 

is satisfied. This is the inverse of the Laplace transform. A mathematical theory concerning the one-to-one correspondence between (regular) exponential families and (regular) Bregman divergences is established in Banerjee et al. (2005). 

**Theorem 2.2** _There is a bijection between regular exponential families and regular Bregman divergences._ 

The theorem shows that a Bregman divergence has a probabilistic expression given by an exponential family of probability distributions. A Bregman divergence is always written in the form of the KL-divergence of the corresponding exponential family. 

_Remark_ A mixture family _M_ = { _p(x,_ _**η** )_ } has a dually flat structure, where the negative entropy _ϕ(_ _**η** )_ is a convex function. We can define an exponential family of which the convex function is _ϕ(_ _**θ** )_ . However, this is different from the original _M_ . Hence, Theorem 2.2 does not imply that a mixture family is an exponential family, even though it is dually flat. 

## **2.8 Applications of Pythagorean Theorem** 

A few applications of the generalized Pythagorean Theorem are shown here to illustrate its usefulness. 

## _**2.8.1 Maximum Entropy Principle**_ 

Let us consider discrete probability distributions _Sn_ = { _p(x)_ }, although the following arguments hold even when _x_ is a continuous vector random variable. Let _c_ 1 _(x), . . . , ck(x)_ be _k_ random variables, that is, _k_ functions of _x_ . Their expectations are 

**==> picture [257 x 15] intentionally omitted <==**

We consider a probability distribution _p(x)_ for which the expectations of _ci (x)_ take prescribed values _**a**_ = _(a_ 1 _, . . . , ak)_ , 

**==> picture [233 x 10] intentionally omitted <==**

There are many such distributions and they form an _(n_ − _k)_ -dimensional submanifold _Mn_ − _k(_ _**a** )_ ⊂ _Sn_ specified by _**a**_ , because _k_ restrictions given by (2.87) are imposed. This _Mn_ − _k_ is _m_ -flat, because any mixtures of distributions in _Mn_ − _k_ belong to the same _Mn_ − _k_ . 

45 

2.8 Applications of Pythagorean Theorem 

When one needs to choose a distribution from _Mn_ − _k(_ _**a** )_ , if there are no other considerations, one would choose the distribution that maximizes the entropy. This is called the maximum entropy principle. 

Let _P_ 0 be the uniform distribution that maximizes the entropy in _Sn_ . The dual divergence between _P_ ∈ _Sn_ and _P_ 0 is written as 

**==> picture [246 x 11] intentionally omitted <==**

where the _e_ -coordinates of _P_ 0 are given by _**θ**_ 0, _**η**_ is the _m_ -coordinates of _P_ and _ϕ(_ _**η** )_ is the negative entropy. This is the KL-divergence _DK L_ [ _P_ : _P_ 0] from _P_ to _P_ 0. Since _P_ 0 is the uniform distribution, _**θ**_ 0 = 0. Hence, maximizing the entropy _ϕ(_ _**η** )_ is equivalent to minimizing the divergence. Let _P_[ˆ] ∈ _Mn_ − _k_ be the point that maximizes the entropy. Then, triangle _P P P_[ˆ] 0 is orthogonal and the Pythagorean relation 

**==> picture [262 x 12] intentionally omitted <==**

holds (Fig. 2.1). This implies that the entropy maximizer _P_[ˆ] is given by the _e_ - projection of _P_ 0 to _Mn_ − _k(_ _**a** )_ . 

_P_ ˆ _(_ _**a**_ Each _)_ form a _Mn_ − _kk(_ -dimensional submanifold _**a** )_ includes the entropy maximizer _Ek_ which is an exponential family, where _P_[ˆ] _(_ _**a** )_ . By changing _**a**_ , all of these the natural coordinates are specified by _**θ**_ = _**a**_ (Fig. 2.1), 

**==> picture [233 x 10] intentionally omitted <==**

It is easy to obtain this result by the variational method that maximizes the entropy _ϕ(_ _**η** )_ under constraints (2.87). 

**Fig. 2.1** The family maximizing entropy under linear constraints is an exponential family 

**==> picture [115 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sn<br>exponential family<br>M n-k  ( a )<br>P<br>E          =[ c ( x ) ] [a]<br>P<br>E          = [ c ( x ) ] [a]<br>a<br>P 0<br>E[ c ( x ) ] =<br>**----- End of picture text -----**<br>


46 

2 Exponential Families and Mixture Families of Probability _. . ._ 

## _**2.8.2 Mutual Information**_ 

Let us consider two random variables _x_ and _y_ and the manifold _M_ consisting of all _p(x, y)_ . When _x_ and _y_ are independent, the probability can be written in the product form as 

**==> picture [214 x 10] intentionally omitted <==**

where _pX (x)_ and _pY (y)_ are respective marginal distributions. 

Let the family of all the independent distributions be _MI_ . Since the exponential family connecting two independent distributions is again independent, the _e_ -geodesic connecting them consists of independent distributions. Therefore, _MI_ is an _e_ -flat submanifold. 

Given a non-independent distribution _p(x, y)_ , we search for the independent distribution which is closest to _p(x, y)_ in the sense of KL-divergence. This is given by the _m_ -projection of _p(x, y)_ to _MI_ (Fig. 2.2). The projection is unique and given by the product of the marginal distributions 

**==> picture [214 x 11] intentionally omitted <==**

The divergence between _p(x, y)_ and its projection is 

**==> picture [279 x 23] intentionally omitted <==**

which is the mutual information of two random variables _x_ and _y_ . Hence, the mutual information is a measure of discrepancy of _p(x, y)_ from independence. 

The reverse problem is also interesting. Given an independent distribution (2.92), find the distribution _p(x, y)_ that maximizes _DK L p_ : _p_ ˆ in the class of distributions having the same marginal distributions as _p_ ˆ. These distributions are the inverse image of the _m_ -projection. This problem is studied by Ay and Knauf (2006) and Rauh (2011). See Ay (2002), Ay et al. (2011) for applications of information geometry to complex systems. 

**==> picture [143 x 55] intentionally omitted <==**

**----- Start of picture text -----**<br>
p ( x , y )<br>I ( X , Y )<br>MI :independent<br>p ( x , y ) distributions<br>**----- End of picture text -----**<br>


**Fig. 2.2** Projection of _p(x, y)_ to the family _MI_ of independent distributions is the _m_ -projection. The mutual information _I (_ _**X** ,_ _**Y** )_ is the KL-divergence _DK L_ [ _p(x, y)_ : _pX (x) pY (y)_ ] 

2.8 Applications of Pythagorean Theorem 

47 

## _**2.8.3 Repeated Observations and Maximum Likelihood Estimator**_ 

Statisticians use a number of independently observed data _**x**_ 1 _, . . . ,_ _**x** N_ from the same probability distribution _p(_ _**x** ,_ _**θ** )_ in an exponential family _M_ for estimating _**θ**_ . The joint probability density of _**x**_ 1 _, . . . ,_ _**x** N_ is given by 

**==> picture [234 x 30] intentionally omitted <==**

having the same parameter _**θ**_ . We see how the geometry of _M_ changes by multiple observations. 

Let the arithmetic average of _**x** i_ be 

**==> picture [196 x 30] intentionally omitted <==**

Then, (2.94) is rewritten as 

**==> picture [283 x 11] intentionally omitted <==**

Therefore, the probability density of _**x**_ ¯ has the same form as _p(_ _**x** ,_ _**θ** )_ , except that _**x**_ ¯ is replaced by _**x**_ and the term _**θ**_ · _**x**_ − _ψ(_ _**θ** )_ becomes _N_ times larger. 

This implies that the convex function becomes _N_ times larger and hence the KL-divergence and Riemannian metric (Fisher information matrix) also become _N_ times larger. The dual affine structure of _M_ does not change. Hence, we may use the original _M_ and the same coordinates _**θ**_ even when multiple observations take place for statistical inference. The binomial distributions and multinomial distributions are exponential families derived from _S_ 2 and _Sn_ by multiple observations. 

Let _M_ be an exponential family and consider a statistical model _S_ = { _p(_ _**x** ,_ _**u** )_ } included in it as a submanifold, where _S_ is specified by parameter _**u**_ = _(u_ 1 _, . . . , uk)_ , _k < n_ . Since it is included in _M_ , the _e_ -coordinates of _p(_ _**x** ,_ _**u** )_ in _M_ are determined by _**u**_ in the form of _**θ** (_ _**u** )_ . Given _N_ independent observations _**x**_ 1 _, . . . ,_ _**x** N_ , we estimate the parameter _**u**_ based on them. 

The observed data specifies a distribution in the entire _M_ , such that its _m_ - coordinates are 

**==> picture [207 x 22] intentionally omitted <==**

of the observed pointdistributionThis is called _p(_ _**x**_ an _,_ _**u** )_ observed in _**η**_ ¯ _S_ . We consider a simple case of is written aspoint. The _DK L_ KL-divergence� _**θ**_ ¯ : _**θ** (_ _**u** )_ �, where _Sn_ , where the observed pointfrom _**θ**_[¯] the is theobserved _**θ**_ -coordinates _**η**_ ¯ to a is given by the histogram 

2 Exponential Families and Mixture Families of Probability _. . ._ 

48 

**==> picture [219 x 30] intentionally omitted <==**

Then, except for a constant term, minimizing _DK L_ [ ¯ _p(x)_ : _p(x,_ _**u** )_ ] is equivalent to maximizing the log-likelihood 

**==> picture [211 x 30] intentionally omitted <==**

Hence, the maximum likelihood estimator that minimizes the divergence is given by the _m_ -projection of _p_ ¯ _(x)_ to _S_ . See Fig. 2.3. In other words, the maximum likelihood estimator is characterized by the _m_ -projection. 

## **Remarks** 

An exponential family is an ideal model to study the dually flat structure and also statistical inference. The Legendre duality between the natural and expectation parameter was pointed out by Barndorff-Nielsen (1978). It is good news that the family _Sn_ of discrete distributions is an exponential family, because any statistical model having a discrete random variable is regarded as a submanifold of an exponential family. Therefore, it is wise to study the properties of the exponential family first and then see how they are transferred to curved subfamilies. 

Unfortunately, this is not the case with continuous random variable _x_ . There are many statistical models which are not subfamilies of exponential families, even though many are curved-exponential families, that is, submanifolds of exponential families. Again, the study of the exponential family is useful. In the case of a truly non-exponential model, we use its local approximation by using a larger exponential family. This gives an exponential fibre-bundle-like structure to statistical models. This is useful for studying the asymptotic theory of statistical inference. See Amari (1985). 

**Fig. 2.3** The maximum likelihood estimator is the _m_ -projection of observed point to _S_ 

**==> picture [75 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>:observed point<br>S<br>u<br>u<br>**----- End of picture text -----**<br>


2.8 Applications of Pythagorean Theorem 

49 

It should be remarked that a generalized linear model provides a dually flat structure, although it is not an exponential family. See Vos (1991). A mixture model also has remarkable characteristics from the point of view of geometry. See Marriott (2002), Critchley et al. (1993). 

## **Chapter 3 Invariant Geometry of Manifold of Probability Distributions** 

We have introduced a dually flat Riemannian structure in the manifolds of the exponential family and the mixture family based on the convexity of the cumulant generating function (free energy) and the negative entropy, respectively. The KL-divergence is derived from these convex functions. However, we need justification for this selection of convex function and divergence. Moreover, such a convex function does not exist for a general statistical model. Therefore, a reasonable criterion is needed for introducing a geometrical structure to a manifold of probability distributions. It is invariance that justifies the above selection. 

Invariance requires that a geometrical structure should be invariant when random variable _**x**_ is represented in a different form _**y**_ = _**y** (_ _**x** )_ , provided _**y** (_ _**x** )_ is invertible. This is an idea introduced by Chentsov (1972). We begin with a simpler idea of information monotonicity by coarse graining, due to Csiszár (1974), a simplified version of Chentsov’s invariance. There exists a unique class of decomposable invariant divergences, known as _f_ -divergences. 

## **3.1 Invariance Criterion** 

We treat a statistical model 

**==> picture [199 x 10] intentionally omitted <==**

parameterized by _**ξ**_ , which forms a manifold with coordinate system _**ξ**_ . Here, _x_ may take discrete, continuous and vector values. What is a natural divergence _D_ � _**ξ**_ : _**ξ**_[′][�] between two probability distributions _p(x,_ _**ξ** )_ and _p(x,_ _**ξ**_[′] _)_ ? In answering this question, we consider the invariance criterion, which states that the geometry is the same when random variable _x_ is transformed into _y_ without losing information. We consider a mapping of _x_ to _y_ 

**==> picture [187 x 10] intentionally omitted <==**

51 

© Springer Japan 2016 

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_3 

52 

3 Invariant Geometry of Manifold of Probability Distributions 

which is in general many-to-one, so we cannot recover _x_ from _y_ . Then, information is lost by this mapping. Let the probability distribution of _y_ be _p_ ¯ _(y,_ _**ξ** )_ , 

**==> picture [219 x 24] intentionally omitted <==**

in the discrete case, which is induced from _p(x,_ _**ξ** )_ by the mapping _y_ = _k(x)_ . In the continuous case, the probability density _p_ ¯ _(y,_ _**ξ** )_ is given by integration. The divergence _p_ ¯ _(y,_ _**ξ** )_ and _Dp_ ¯ _(_ � _y_ _**ξ** ,_ _**ξ**_ : _**ξ**_[′] _)_[′] . Since divergence[�] between _p(x,_ _**ξ** )_ and _D_ � _**ξ** p_ : _**ξ**_ � _x_[′][�] _,_ _**ξ**_ represents the dissimilarity of two[′][�] changes to _D_[¯] � _**ξ**_ : _**ξ**_[′][�] between distributions _p(x,_ _**ξ** )_ and _p_ � _x,_ _**ξ**_[′][�] , it is postulated that it decreases in general by this mapping, 

**==> picture [214 x 13] intentionally omitted <==**

We call this relation information monotonicity. 

Obviously, when _k_ is one-to-one, that is invertible, there is no loss of information and the equality is required to hold in (3.4). However, there is a case when information is not lost even when _k_ is not invertible. This is the case when _x_ includes a redundant part, the distribution of which does not depend on _**ξ**_ . We may abandon this part without losing information concerning _**ξ**_ . The remaining part retains full information. Statisticians call such a part a sufficient statistic. Its definition is given below. 

A function 

**==> picture [185 x 9] intentionally omitted <==**

is called a sufficient statistic when the probability density function _p(x,_ _**ξ** )_ is decomposed as 

**==> picture [212 x 10] intentionally omitted <==**

This implies that the probability _p(x,_ _**ξ** )_ is written as a function of _s_ , except for a multiplicative term _r (x)_ which does not depend on _**ξ**_ . The equality is required to hold in (3.4) when and only when _y_ is a sufficient statistic. 

We formally state the invariance criterion, for which the basic idea was originally due to Chentsov (1972) and which was formulated in this way by Amari and Nagaoka (2000). 

**Invariance Criterion** : A geometrical structure of _M_ is invariant when it satisfies the monotonicity (3.4), where the equality holds if and only if _y_ = _k(x)_ is a sufficient statistic. 

We study the class of invariant divergences and invariant Riemannian metrics. The invariant metric is unique, given by the Fisher information matrix except for a scale constant (Chentsov 1972). 

53 

3.2 Information Monotonicity Under Coarse Graining 

## **3.2 Information Monotonicity Under Coarse Graining** 

## _**3.2.1 Coarse Graining and Sufficient Statistics in Sn**_ 

We consider a family _Sn_ of discrete probability distributions, where random variable _x_ takes on values _X_ = {0 _,_ 1 _, . . . , n_ }. Let us denote a probability distribution by an _(n_ + 1 _)_ -dimensional probability vector _**p**_ . We divide _X_ into _m_ + 1 subsets _X_ 0 _, X_ 1 _, . . . , X m_ such that 

**==> picture [240 x 10] intentionally omitted <==**

where _φ_ is the empty set. This is a partition of _X_ (Fig. 3.1). 

Assume that we cannot observe _x_ directly, but know the subset to which _x_ belongs. This is thecasewhen _X_ is coarse-grained. Wethenintroduceacoarse-grainedrandom variable _y_ , taking on values {0 _,_ 1 _, . . . , m_ }, where _y_ = _a_ implies that _x_ belongs to _X a_ . Let its distribution be denoted by _(m_ + 1 _)_ -dimensional probability vector _**p**_ ¯ = _(_ ¯ _p_ 0 _, . . . , p_ ¯ _m)_ . Coarse graining leads to a new distribution _**p**_ ¯ in _Sm_ given by 

**==> picture [192 x 23] intentionally omitted <==**

Let _D_ � _**p**_ : _**q**_ � be a divergence between two distributions _**p**_ and _**q**_ . It is said to be additive or decomposable when it is written in an additive form of componentwise divergences, 

**==> picture [217 x 29] intentionally omitted <==**

for some function _d( p, q)_ . The divergence _D_ [ _**p**_ : _**q**_ ] changes to _D_[¯] � _**p**_ ¯ : _**q**_ ¯ � by coarse graining, 

**==> picture [222 x 28] intentionally omitted <==**

The information monotonicity criterion requires 

**==> picture [212 x 13] intentionally omitted <==**

**Fig. 3.1** Partition of _X_ into _m_ + 1 subsets 

**==> picture [213 x 51] intentionally omitted <==**

54 

3 Invariant Geometry of Manifold of Probability Distributions 

When does the equality hold in (3.11)? This occurs in the case when there is no loss of information by coarse graining. Since _y_ is a function of _x_ , we have the following decomposition: 

**==> picture [250 x 10] intentionally omitted <==**

where _**ξ**_ is a coordinate system of _Sn_ . We see that _y_ is a sufficient statistic when _p(x_ | _y,_ _**ξ** )_ does not depend on _**ξ**_ . In this case, the conditional distributions of _p(x_ | _y,_ _**ξ** )_ and _q(x_ | _y,_ _**ξ**_[′] _)_ are equal for two distributions _p(x)_ = _p(x,_ _**ξ** )_ and _q(x)_ = _p(x,_ _**ξ**_[′] _)_ , that is, 

**==> picture [257 x 13] intentionally omitted <==**

## _**3.2.2 Invariant Divergence**_ 

When a divergence is written in the form 

**==> picture [224 x 25] intentionally omitted <==**

where _f_ is a differentiable convex function satisfying 

**==> picture [185 x 10] intentionally omitted <==**

it is called an _f_ -divergence. The _f_ -divergence was introduced by Morimoto (1963), Ali and Silvey (1966) and Csiszár (1967). It is easy to prove that this satisfies the criteria of divergence, by expanding _D f_ [ _**p**_ : _**p**_ + _d_ _**p**_ ] in the Taylor series, although it is not a Bregman divergence in general. 

**Theorem 3.1** _An f -divergence is invariant and decomposable. Conversely an invariant and decomposable divergence is an f -divergence, except for the case of n_ = 1 _._ 

_Proof_ We first prove that an _f_ -divergence satisfies the criterion of information monotonicity. Consider a simple partition where _X_ 0 = {1 _,_ 2} and all the other _Xa_ are singleton sets. That is, _x_ = 1 _,_ 2 are put in a subset _X_ 0 but all the other _x_ remain as they are. We prove only this case, but other cases can be proved similarly. We need to prove 

**==> picture [275 x 25] intentionally omitted <==**

55 

3.2 Information Monotonicity Under Coarse Graining 

By introducing 

**==> picture [210 x 21] intentionally omitted <==**

the right-hand side of (3.16) is written as 

**==> picture [251 x 25] intentionally omitted <==**

Since _f_ is convex, 

**==> picture [312 x 25] intentionally omitted <==**

which proves the information monotonicity. 

Conversely, assume that the information monotonicity holds for a decomposable divergence (3.9). Then, the equality holds when (3.13) is satisfied, that is, _u_ 1 = _u_ 2 in the present case. The equality is written as 

**==> picture [262 x 10] intentionally omitted <==**

By putting 

**==> picture [208 x 10] intentionally omitted <==**

we have 

**==> picture [243 x 10] intentionally omitted <==**

for _u >_ 0, and hence _k( p, u)_ is linear in _p_ . So we have 

**==> picture [203 x 10] intentionally omitted <==**

implying 

This proves the theorem. 

**==> picture [209 x 45] intentionally omitted <==**

_Remark 1_ The above proof is not valid when _n_ = 1, because coarse graining causes _m_ = 0. The following is shown by Jiao et al. (2015): There exists a class of invariant divergences which are not necessarily _f_ -divergences when _n_ = 1. So the case with _n_ = 1 is special and Jiao et al. (2015) derived a general class of invariant divergences when _n_ = 1. 

56 

3 Invariant Geometry of Manifold of Probability Distributions 

_Remark 2_ When we treat non-decomposable divergences, there are invariant divergences which are not _f_ -divergences. A function of _f_ -divergence is invariant but is not decomposable in general. A simple example is 

**==> picture [247 x 15] intentionally omitted <==**

Further,anadequatenonlinearfunctionoftwo _f_ -divergences _D f_ 1 and _D f_ 2 isinvariant but is not an _f_ -divergence. 

We will show in Part II that any invariant divergence gives the same geometry called the _α_ -structure. 

When a linear term is added to a convex function _f_ , 

**==> picture [217 x 11] intentionally omitted <==**

where _c_ is a constant, _f_[¯] is also convex. It is easy to see 

**==> picture [218 x 13] intentionally omitted <==**

so (3.26) does not change the divergence. Hence, without loss of generality, we can always use a convex function satisfying 

**==> picture [212 x 11] intentionally omitted <==**

Moreover, since 

**==> picture [217 x 11] intentionally omitted <==**

holds for another constant _c >_ 0, the constant _c_ determines the scale of divergence. To fix the scale, we use _f_ that satisfies 

**==> picture [187 x 11] intentionally omitted <==**

**Definition 3.1** A convex function _f_ satisfying (3.28) and (3.30) is said to be standard. An _f_ -divergence derived from a standard _f_ is a standard _f_ -divergence. 

When _D f_ � _**p**_ : _**q**_ � is a standard _f_ -divergence, its dual _D_[∗] _f_[[] _**[ p]**_[ :] _**[q]**_[] =] _[D][ f]_[ [] _**[q]**_[:] _**[p]**_[]][ is] also a standard _f_ -divergence. To show this, define 

**==> picture [203 x 25] intentionally omitted <==**

Then, _f_[∗] is a standard convex function when _f_ is, and we have 

**==> picture [217 x 11] intentionally omitted <==**

57 

3.3 Examples of _f_ -Divergence in _Sn_ 

## **3.3 Examples of** _**f**_ **-Divergence in** _**Sn**_ 

## _**3.3.1 KL-Divergence**_ 

For 

**==> picture [198 x 10] intentionally omitted <==**

the derived divergence is the KL-divergence 

**==> picture [221 x 22] intentionally omitted <==**

The dual of _f_ is 

**==> picture [199 x 10] intentionally omitted <==**

The derived divergence is the dual of the KL-divergence 

**==> picture [220 x 11] intentionally omitted <==**

which coincides with the divergence derived from the cumulant generating function _ψ_ . 

## _**3.3.2 χ**_ **[2]** _**-Divergence**_ 

For 

**==> picture [271 x 25] intentionally omitted <==**

This is known as the Pearson _χ_[2] -divergence. 

## _**3.3.3 α-Divergence**_ 

Let _α_ be a real parameter. We define the _α_ -function by 

**==> picture [247 x 22] intentionally omitted <==**

58 

3 Invariant Geometry of Manifold of Probability Distributions 

The derived divergence is the _α_ -divergence (Amari 1985; Amari and Nagaoka 2000) given by 

**==> picture [274 x 22] intentionally omitted <==**

The dual of the _α_ -function is the − _α_ -function. Hence, the dual of the _α_ -divergence is the − _α_ -divergence, 

**==> picture [221 x 13] intentionally omitted <==**

When _α_ = 0, we have 

**==> picture [280 x 16] intentionally omitted <==**

which is known as the square of the Hellinger distance. 

We extend the _α_ -function (3.38) to the case of _α_ = ±1, by taking the limit _α_ →±1. Then, 

**==> picture [224 x 25] intentionally omitted <==**

The derived divergences are 

**==> picture [243 x 31] intentionally omitted <==**

Hence, the KL-divergence is −1-divergence and its dual is 1-divergence. For 

**==> picture [196 x 9] intentionally omitted <==**

which is not differentiable, and hence _D f_ is not a divergence by our definition, _D f_ is a symmetric function of _**p**_ and _**q**_ , 

**==> picture [226 x 22] intentionally omitted <==**

known as the variational distance. 

The square of the Euclidean distance, 

**==> picture [222 x 15] intentionally omitted <==**

is a divergence. But it is not an _f_ -divergence and is not invariant. 

59 

3.4 General Properties of _f_ -Divergence and KL-Divergence 

## **3.4 General Properties of** _**f**_ **-Divergence and KL-Divergence** 

## _**3.4.1 Properties of f -Divergence**_ 

The following properties hold in _Sn_ . 

- (1) An _f_ -divergence _D f_ [ _**p**_ : _**q**_ ] is convex with respect to both _**p**_ and _**q**_ . 

- (2) It is bounded from above as 

**==> picture [243 x 52] intentionally omitted <==**

(3) For _α_ ≥ 1, 

**==> picture [191 x 10] intentionally omitted <==**

when _p(x)_ = 0 and _q(x)_ ̸= 0 hold for some _x_ . 

(4) For _α_ ≤−1, 

**==> picture [191 x 10] intentionally omitted <==**

when _p(x)_ ̸= 0 and _q(x)_ = 0 hold for some _x_ . 

Properties (3) and (4) hold for the KL-divergence and its dual, because they are ±1-divergences. They lead to the following results of approximation of a probability distribution by using the _α_ -divergence. Given _**p**_ ∈ _Sn_ , we search for the distribution _**p**_ ˆ _S_ that minimizes the divergence from _**p**_ to a smooth submanifold _S_ ⊂ _Sn_ , 

**==> picture [214 x 18] intentionally omitted <==**

Then, the following holds: 

- (5) Zero-forcing: When _α_ ≥ 1, the best approximation _**p**_ ˆ _S_ in the closure of _S_ satisfies 

**==> picture [179 x 10] intentionally omitted <==**

for _x_ at which _p(x)_ = 0. 

- (6) Zero-avoidance: When _α_ ≤−1, the best approximation _**p**_ ˆ _S_ in the closure of _S_ 

**==> picture [179 x 11] intentionally omitted <==**

for _x_ at which _p(x)_ ̸= 0. 

60 

3 Invariant Geometry of Manifold of Probability Distributions 

## _**3.4.2 Properties of KL-Divergence**_ 

## **A. Large deviation** 

Let _**p**_ be a distribution in _Sn_ from which _N_ independent data _x(_ 1 _), . . . , x(N )_ are ˆ generated. The empirical distribution of the observed data is given by _**p**_ , 

**==> picture [223 x 30] intentionally omitted <==**

where _Ni_ is the number that _x_ = _i_ is observed among _N_ data. This is the maximum likelihood estimator. How far is _**p**_ ˆ from the true _**p**_ ? The probability distribution of _**p**_ ˆ is evaluated by the KL-divergence asymptotically when _N_ is large. 

**Sanov Lemma.** The probability of _**p**_ ˆ is asymptotically given by 

**==> picture [248 x 10] intentionally omitted <==**

that is, the probability decays exponentially as _N_ increases where the exponent of decay is _DK L_ _**p**_ ˆ : _**p**_ . 

The proof is given by evaluating the distribution of _**p**_ ˆ , a multinomial distribution, when _N_ is large, which we omit. When _**p**_ ˆ is close to _**p**_ , by putting 

**==> picture [204 x 24] intentionally omitted <==**

and expanding _N DK L_ [ _**p**_ ˆ : _**p**_ | , we have the central limit theorem. **Central Limit Theorem** The distribution of _**p**_ ˆ is asymptotically Gaussian with mean _**p**_ and covariance 

**==> picture [235 x 175] intentionally omitted <==**

Let _A_ be a region in _Sn_ . Then, we have the theorem of large deviation, which is useful in information theory and statistics (Fig. 3.2). 

**Fig. 3.2** _e_ -projection of _**p**_ to _A_ 

61 

3.4 General Properties of _f_ -Divergence and KL-Divergence 

**Large Deviation Theorem** The probability that _**p**_ ˆ is included in _A_ is given asymptotically by 

**==> picture [254 x 13] intentionally omitted <==**

where 

**==> picture [220 x 19] intentionally omitted <==**

When _A_ is a closed set having a boundary, _**p**_[∗] _A_[is][given][by] _[e]_[-projecting] _**[p]**_[to][the] boundary of _A_ . 

## **B. Symmetrized KL-divergence and Fisher information** 

The Riemannian distance between two points _**p**_ and _**q**_ is given by the minimum of the distance along all curves _**ξ** (t)_ connecting _**p**_ and _**q**_ such that _**ξ** (_ 0 _)_ = _**p**_ , _**ξ** (_ 1 _)_ = _**q**_ , that is, 

**==> picture [220 x 37] intentionally omitted <==**

Since the KL-divergence is 

**==> picture [244 x 22] intentionally omitted <==**

there would be some relation between the KL-divergence and the integration of the Fisher information along a curve. Let us consider the _e_ -geodesic and the _m_ -geodesic connecting two points _**p**_ and _**q**_ , 

**==> picture [268 x 26] intentionally omitted <==**

They are exponential and mixture families, respectively. Let _ge(t)_ and _gm(t)_ be the Fisher information along the curves, 

**==> picture [213 x 28] intentionally omitted <==**

Then, we have the following theorem. 

**Theorem 3.2** _The symmetrized KL-divergence is given by the integration of the Fisher information along the e-geodesic and the m-geodesic,_ 

62 

3 Invariant Geometry of Manifold of Probability Distributions 

**==> picture [225 x 62] intentionally omitted <==**

The proof is technical and is omitted. 

## **3.5 Fisher Information: The Unique Invariant Metric** 

Since an _f_ -divergence is invariant, the Riemannian metric derived from it is invariant. We can easily calculate the metric _gi j_ from an _f_ -divergence by the Taylor expansion, 

**==> picture [319 x 32] intentionally omitted <==**

A simple calculation gives the following lemma. 

**Lemma** _Any standard f -divergence gives the same Riemannian metric which is the Fisher information matrix_ 

**==> picture [245 x 13] intentionally omitted <==**

_where_ 

**==> picture [187 x 24] intentionally omitted <==**

Chentsov (1972) proved a stronger theorem that the Fisher information matrix is the unique invariant metric of _Sn_ . He used the framework of category theory. We show a simpler proof due to Campbell (1986). 

Consider a series of _Sn, n_ = 1 _,_ 2 _,_ 3 _, . . ._ , and reformulate the invariance criterion. We consider coarse graining of _Sn_ by a partition of _X_ = {0 _,_ 1 _,_ 2 _, . . . , n_ } to _Y_ = { _A_ 0 _, A_ 1 _, . . . , Am_ }, where _n_ ≥ _m_ . Random variable _x_ taking on values 0 _,_ 1 _, . . . , n_ is reduced to random variable _y_ taking on values 0 _,_ 1 _, . . . , m_ , such that _y_ = _i_ when _x_ is included in _Ai_ . Obviously, probability distribution _**p**_ ∈ _Sn_ is mapped to _**q**_ ∈ _Sm_ by this coarse graining. It defines a mapping _f_ from _Sn_ to _Sm_ 

**==> picture [218 x 24] intentionally omitted <==**

Conversely, we consider a mapping _h_ from _Sm_ to _Sn_ , which is determined by an arbitrary conditional probability distribution, 

**==> picture [223 x 11] intentionally omitted <==**

3.5 Fisher Information: The Unique Invariant Metric 

63 

**==> picture [309 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
hS 2<br>h<br>S 3<br>A-3 S 2<br>Fig. 3.3 Embedding of S 2 in S 3 (m = 2, n = 3)<br>**----- End of picture text -----**<br>


Given _y_ = _j_ , it generates _x_ = _i_ stochastically based on _ri j_ . We define a mapping by 

**==> picture [216 x 10] intentionally omitted <==**

Given _y_ of which the probability is _**q**_ , the probability distribution _**p**_ = _h_ _**q**_ of _x_ is given by (3.72). The mapping _h_ which depends on _ri j_ embeds _Sm_ in _Sn_ and it satisfies 

**==> picture [188 x 9] intentionally omitted <==**

where Id is the identity mapping (see Fig. 3.3). 

Consider a problem of estimation of _**q**_ ∈ _Sm_ by observing random variable _y_ . When _Sm_ is embedded in a larger manifold _Sn_ by (3.72), the random variable is _x_ . However, _x_ includes a redundant part for estimating _**q**_ . _y_ is a sufficient statistic for estimating _**q**_ . 

The invariance criterion claims that the geometry of _Sm_ is the same as the geometry of embedded _hSm_ in the larger manifold _Sn_ . In particular, the inner product of two basis vectors in _Sm_ should be the same as that in the embedded image. Now we state the theorem of Chentsov. 

**Theorem 3.3** _The invariant metric is unique, given by the Fisher information to within a constant factor._ 

_Proof_ We use _**R**[n]_ +[to prove the theorem, considering] _[ S][n]_[−][1][ as its subspace constrained] by _pi_ = 1. When _m_ = _n_ , the mapping _f_ is only a permutation of indices. We consider the center of _Sn_ −1, 

**==> picture [216 x 22] intentionally omitted <==**

64 

3 Invariant Geometry of Manifold of Probability Distributions 

It is invariant under the permutation group of index _i_ . So the inner product of two basis vectors _**e** i_ and _**e** j_ in _**R**_[+] _n_[is invariant under the permutation of indices. Hence,] we put 

**==> picture [242 x 26] intentionally omitted <==**

or 

**==> picture [220 x 12] intentionally omitted <==**

When _**p**_ is in _Sn_ −1, its small deviation _δ_ _**p**_ inside _Sn_ −1 satisfies 

**==> picture [192 x 29] intentionally omitted <==**

Since _δ_ _**p**_ is a tangent vector of _Sn_ −1, 

**==> picture [189 x 15] intentionally omitted <==**

holds for any tangent vector _Z_ = _Z[i]_ _**e** i_ of _Sn_ −1. 

Therefore, we may put _B(n)_ = 0 when calculating the inner product of two tangent vectors of _Sn_ −1. _B(n)_ is responsible only for the normal direction to _Sn_ −1. So, we put 

**==> picture [204 x 12] intentionally omitted <==**

Let us consider a point 

**==> picture [232 x 25] intentionally omitted <==**

where _ki_ are integers, satisfying[�] _ki_ = _n_ . We then consider the following embedding of _Sm_ −1 in _Sn_ −1 given by the conditional distributions 

**==> picture [212 x 26] intentionally omitted <==**

where � _A j_ � is a partition of {0 _,_ 1 _, . . . , n_ } such that _A j_ includes _k j_ elements. Then, _**q**_ is mapped to the center of _Sn_ −1, 

**==> picture [218 x 25] intentionally omitted <==**

3.5 Fisher Information: The Unique Invariant Metric 

65 

The basis vector _**e**[m]_ 1[∈] _**[R]**[m]_ +[is mapped to] 

**==> picture [211 x 24] intentionally omitted <==**

in _**R**[n]_ +[by this embedding. Similar equations hold for other] _**[ e]** i[n]_[,] _[ i]_[=][ 2] _[,]_[ 3] _[, . . . ,][ m]_[. The] inner product is equal to 

**==> picture [323 x 41] intentionally omitted <==**

Hence, we have 

**==> picture [206 x 21] intentionally omitted <==**

Since the constant _c_ is used only to determine the scale of the Fisher information, we may put _c_ = 1. Similarly, 

**==> picture [204 x 23] intentionally omitted <==**

This holds only at the points where _qi_ are rational numbers, but because of the continuity, it holds for any _**q**_ . This proves the theorem. □ 

_Remark_ We can prove the uniqueness of the cubic tensor _Ti jk_ defined by 

**==> picture [271 x 13] intentionally omitted <==**

under the invariance criterion in a similar way. This will be used to study the uniqueness of the _α_ -connection in Part II. 

## **3.6** _**f**_ **-Divergence in Manifold of Positive Measures** 

We extend the notion of invariance from _Sn_ to _**R**[n]_ +[by][using][the][information] monotonicity under coarse graining. We can prove that the only invariant decomposable divergence is an _f_ -divergence, since the proof of Theorem 4.1 is also valid for _**R**[n][f]_[ -divergence is] +[. An] 

**==> picture [228 x 25] intentionally omitted <==**

66 

3 Invariant Geometry of Manifold of Probability Distributions 

_**m** ,_ _**n**_ ∈ _**R**[n]_ +[, for a manifold of positive measures] _**[R]**[n]_ +[, where] _[f]_[is a standard convex] function satisfying (3.28) and (3.30). We need to use a standard convex function to define a divergence in _**R**[n]_ +[, because (][3.89][) does not satisfy the criteria of divergence] for a general convex _f_ . The criteria are satisfied when a standard convex function _f_ is used. 

We can calculate the invariant Riemannian metric induced in _**R**[n]_ +[by][an] _f_ -divergence. 

**Theorem 3.4** _The Riemannian metric in_ _**R**[n]_ + _[induced by an invariant divergence is] the Euclidean metric_ 

**==> picture [200 x 23] intentionally omitted <==**

_Proof_ It is easy to derive (3.90) by the Taylor expansion of (3.89) 

**==> picture [252 x 52] intentionally omitted <==**

where _f_[′′] _(_ 1 _)_ = 1. By using a new coordinate system given by 

**==> picture [191 x 13] intentionally omitted <==**

the square of an infinitesimal distance is given as 

**==> picture [204 x 16] intentionally omitted <==**

showing that the manifold is Euclidean and the coordinate system is orthonormal. □ 

It should be noted that manifold _Sn_ is a submanifold of _**R**_[+] _n_ +1[.][The][constraint] � _pi_ = 1 becomes 

**==> picture [193 x 16] intentionally omitted <==**

in the new coordinate system. Hence, _Sn_ is a sphere in a Euclidean space, so it is curved. 

As an important special case of _f_ -divergence, we introduce the _α_ -divergence, which is previously defined in _Sn_ , to _**R**[n]_ +[.][It][is][defined][by][using][the][standard] _[α]_[-] function, 

**==> picture [273 x 43] intentionally omitted <==**

3.6 _f_ -Divergence in Manifold of Positive Measures 

67 

**Definition** The _α_ -divergence is defined in _**R**[n]_ +[by] 

**==> picture [312 x 56] intentionally omitted <==**

When both _**m**_ and _**n**_ satisfy the normalization condition, 

**==> picture [209 x 15] intentionally omitted <==**

they are probability distributions and the _α_ -divergence is equal to that in a manifold of probability distributions. 

## **Remarks** 

There is a long history of studies on geometry of manifolds of probability distributions. C.R. Rao is believed to have been the first who introduced a Riemannian metric by using the Fisher information matrix (Rao 1945). This was work he did at the age of twenty-four, and the famous Crámer–Rao theorem was presented in the same seminal paper. It is a monumental work from which Information Geometry has emerged. Jeffreys (1946) used the square root of the determinant of the Fisher metric, which is the Riemannian volume element, as an invariant prior distribution over the manifold in Bayesian statistics. However, there was no such concept in the first edition of his famous book, “Probability Theory”, published in 1939 (Jeffreys 1939). It appeared in the second edition (Jeffreys 1948; see also Jeffreys 1946). 

It was a big surprise that a hidden prehistory was uncovered by Stigler (2007) (Frank Nielsen kindly let me know of this paper). In 1929, Harold Hotelling spent nearly half a year at Rothamsted working with R.A. Fisher on establishing a foundation for mathematical statistics. He submitted a paper entitled “Spaces of statistical parameters” to the American Mathematical Society Meeting in 1929 (which, in his absence, was read by O. Ore). The paper has never been published, so his idea has become entombed and remains unknown. He stated in the paper that the Riemannian metric is given by the Fisher information matrix in a statistical manifold. Moreover, he remarked that the manifold of a location-scale statistical model has a constant negative curvature. Incidentally, I discovered this fact in 1958 when I was a master’s student, and this was the origin of my study of information geometry. 

After Rao, there appeared a number of works using the Riemannian structure, e.g., James (1973). It was Chentsov (1972) who introduced the invariance criterion for defining the geometry of a statistical manifold. He proved that the Fisher information matrix is the only invariant metric in _Sn_ . Moreover, he obtained the class of invariant affine connections ( _α_ -connections studied in Part II). Unfortunately, his work was published only in Russian, so his contributions did not become popular in the western world until an English translation appeared in 1982. Later, Efron (1975) investigated old unpublished calculations by R.A. Fisher and elucidated the results by defining the 

68 

3 Invariant Geometry of Manifold of Probability Distributions 

statistical curvature of a statistical model. He showed that the higher-order efficiency of statistical estimation is given by the statistical curvature which is the _e_ -curvature defined in Part II. This work was commented on by A.P. Dawid in discussions of Efron’s paper, where the _e_ - and _m_ -connections were suggested. 

Following Efron’s and Dawid’s works, Amari (1982) further developed the differential geometry of statistical models and elucidated its dualistic nature. It was applied to statistical inference to establish a higher-order statistical theory (Amari 1982, 1985; Kumon and Amari 1983). The formal theory of a dually flat manifold was first proposed by Nagaoka and Amari (1982), which included the Pythagorean theorem and projection theorem. However, it was not published as a journal paper, because it was rejected by major journals. The editor of the _Annals of Probability_ asked me to withdraw the paper, because he had approached seven reviewers but none reviewed it seriously. So he concluded that most probabilists would not have any interest in the direction of this research. A reviewer for the _Zeitschrift für Wahrsceinlichkeitstheorie und Verwandte Gebiete_ ( _Theory of Probability and its Applications_ ) sent me a letter stating that the paper was useless, because no essential relation exists between statistics and differential geometry. He also pointed out that the differential geometry of this paper is different from that in textbooks so it would be dubious. (We proposed a new framework of duality in differential geometry.) So it was rejected. Several years passed and thirdly a reviewer in _IEEE Transactions on Information Theory_ wrote that the theory was now well known around the world and the paper submitted included few new ideas. This was because a workshop on this subject was organized in London in 1984 by Sir D. Cox, and my “Springer Lecture Notes” (Amari 1985) were published. Since then, information geometry has become widely known and a number of competent researchers have joined from the fields of statistics, vision, optimization, machine learning, etc. Many international conferences have been organized on this subject. 

However, a mathematically rigorous foundation involves difficulty in the case of the function space of probability density functions. This is because the topology of the space of _p(x)_ is different from that of the space of log _p(x)_ . There is a series of studies given by Pistone and his coworkers (Pistone and Sempi 1995; Pistone and Rogatin 1999; Cena and Pistone 2007; Pistone 2013). See also Grasselli (2010). Newton (2012) gave a theory based on a Hilbert space, in the framework that _p(x)_ has finite entropy. Here, _p(x)_ , a probability density function with respect to measure _μ(x)_ , is mapped onto a Hilbert space by using the following representation of _p(x)_ : 

**==> picture [219 x 10] intentionally omitted <==**

where 

**==> picture [252 x 13] intentionally omitted <==**

are presumed. J. Jost and his coworkers are developing a rigorous theory in Leipzig, preparing a monograph. See Ay et al. (2013). 

3.6 _f_ -Divergence in Manifold of Positive Measures 

69 

Information geometry uses the _e_ - and _m_ -geodesic connecting two distributions _p(x)_ and _q(x)_ , KL-divergence _DK L_ [ _p(x)_ : _q(x)_ ], the Pythagorean and projection theorems and the orthogonality of two curves. Therefore, we want to have a framework in which the above structures are guaranteed. We need to search for mild regularity conditions which give such a framework (cf. Pistone 2013; Newton 2012). Fukumizu (2009) proposed a novel idea of the kernel exponential family for treating statistical manifolds with function degrees of freedom. 

## **Chapter 4** _**α**_ **-Geometry, Tsallis** _**q**_ **-Entropy** 

An _f_ -divergence is not necessarily of the Bregman type. Hence, the invariant geometry induced from an _f_ -divergence does not necessarily give a dually flat structure. It is proved that the KL-divergence, which is an _f_ -divergence, is the unique class of decomposable divergences that are invariant and flat in _Sn(n >_ 1 _)_ . However, when we study a manifold _**R**[n]_ +[of positive measures, there are other invariant, flat and] decomposable divergences. They are _α_ -divergences, including the KL-divergence as a special case. The present chapter studies the invariant _α_ -structure originating from the _α_ -divergence. It includes the _α_ -geodesic, _α_ -mean, _α_ -projection, _α_ -optimization and _α_ -family of probability distributions. 

We also remark that the geometry originating from Tsallis _q_ -entropy (Tsallis 1988, 2009; Naudts 2011) is nothing other than the _α_ -geometry, where _α_ = 2 _q_ − 1. We show another type of flat structure, called conformal flattening, induced from the Tsallis _q_ -entropy. It is related to the escort probability distribution. Extending it, we identify a universal class of dually flat divergences in _**R**[n]_ +[. We further study a] general invariant flat structure of the manifold of positive-definite matrices, which is important in its own right. 

## **4.1 Invariant and Flat Divergence** 

## _**4.1.1 KL-Divergence Is Unique**_ 

A divergence is flat when it induces a flat structure in the underlying manifold. A Bregman divergence is flat. We begin with the following well-known result in _Sn_ . See Csiszár (1991) for the characterization of the KL-divergence. 

> The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_4 

71 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

72 

**Theorem 4.1** _The KL-divergence and its dual are the only decomposable, flat and invariant divergences, except for the special case of n_ = 1 _._ 

A proof of the present theorem is given as a corollary of Theorem 4.2 in the next subsection. It will be shown in Part II without assuming the decomposability that the KL-divergence is the unique canonical divergence in a dually flat manifold of probability distributions. 

## _**4.1.2 α-Divergence Is Unique in R**_ **+** _**[n]**_ 

We begin with a theorem due to Amari (2009). 

**Theorem 4.2** _The α-divergences form the unique class of decomposable, flat and invariant divergences of_ _**R**[n]_ + _[.]_ 

_Proof_ We first prove that an _α_ -divergence is a Bregman divergence in the manifold _**R**[n]_[This][does][not][imply][that][its][affine][coordinate][system][is][the][measure][vector] +[.] _**m**_ = _(mi )_ ∈ _**R**[n]_ +[itself. We define a new coordinate system] _**[ θ]**_[=] � _θ[i]_[�] by 

**==> picture [229 x 16] intentionally omitted <==**

and call _θ[i]_ the _α_ -representation of a positive measure _mi_ . Then, 

**==> picture [215 x 17] intentionally omitted <==**

is a convex function of _θ[i]_ when | _α_ | _<_ 1. Therefore, 

**==> picture [256 x 22] intentionally omitted <==**

is a convex function of _**θ**_ for _α >_ −1 and the accompanying affine coordinate system is _**θ**_ . The dual affine coordinate system _**η**_ is given by _**η**_ = ∇ _ψα(_ _**θ** )_ as 

**==> picture [219 x 17] intentionally omitted <==**

Hence, it is the − _α_ -representation of _mi_ . The dual convex function is 

**==> picture [206 x 10] intentionally omitted <==**

Calculations show that the Bregman divergence 

**==> picture [257 x 13] intentionally omitted <==**

is the _α_ -divergence defined in (3.96). 

4.1 Invariant and Flat Divergence 

73 

Conversely, assume that an _f_ -divergence 

**==> picture [225 x 25] intentionally omitted <==**

is a Bregman divergence and further that its affine coordinate system _**θ**_ = � _θ[i]_[�] is connected with _mi_ componentwise as 

**==> picture [192 x 11] intentionally omitted <==**

**==> picture [192 x 11] intentionally omitted <==**

for some function _k_[∗] . Since the cross term of _**θ**_ and _**η**_ in the divergence is included only in the last term of (4.6), the relation 

**==> picture [221 x 25] intentionally omitted <==**

must hold for each _i_ . By differentiating it with respect to _ni_ and omitting suffix _i_ for brevity, we have 

**==> picture [211 x 20] intentionally omitted <==**

By putting _x_ = _n_ and _y_ = 1 _/m_ , we have 

**==> picture [213 x 25] intentionally omitted <==**

Further, by putting 

**==> picture [203 x 11] intentionally omitted <==**

the logarithm of (4.12) is written in the form 

**==> picture [210 x 10] intentionally omitted <==**

for some functions _s_ and _t_ . By differentiating both sides with respect to _x_ , we have 

**==> picture [202 x 10] intentionally omitted <==**

where _c_ is a constant. From this, we see that _f_ is of the form 

**==> picture [194 x 14] intentionally omitted <==**

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

74 

except for a scale factor and a constant. This is a convex function for | _α_ | _<_ 1 but is not a standard _f_ -function. By transforming it to the standard form, we have 

**==> picture [256 x 25] intentionally omitted <==**

and the theorem is proved. 

**==> picture [9 x 8] intentionally omitted <==**

We did not mention the case of _α_ = 1. If we modify the definition (4.1) of the _α_ -representation as 

**==> picture [227 x 22] intentionally omitted <==**

log _m_ is given by the limit _α_ → 1. By using this, the proof holds even in the limiting case of _α_ = ±1. 

_Sn_ is a submanifold of _**R**[n]_ +[+][1][, where the constraint] 

**==> picture [189 x 29] intentionally omitted <==**

is imposed. The constraint is rewritten in the _**θ**_ -coordinate system as 

**==> picture [201 x 29] intentionally omitted <==**

This is a nonlinear constraint for _α_ ̸= −1. So _Sn_ is not dually flat but curved for general _α_ , except for the linear constraint case of _α_ = −1. When _α_ = 1, it is linear in the dual coordinate system. Hence, the _α_ -divergence gives a flat structure to _Sn_ only when _α_ = ±1, that is the KL-divergence and its dual. Therefore, the KL-divergence is the only invariant, flat and decomposable divergence in _Sn_ , proving Theorem 4.1. 

_Remark_ Jiao et al. (2015) proved that the KL-divergence is the only invariant divergence of the Bregman type in _Sn_ without assuming the decomposability. It is also proved in the geometrical framework that the canonical divergence of _Sn_ is the KL-divergence in Part II. The case of _n_ = 1 is fully studied in Jiao et al. (2015), characterizing the class of invariant Bregman-type divergences in _Sn_ . The following is proved: 

- (1) An invariant decomposable divergence is an _f_ -divergence when _n >_ 1, but there is a new class of divergences which are not necessarily _f_ -divergences when _n_ = 1. 

- (2) An invariant Bregman divergence is the KL-divergence for any _n_ . 

From the point of view of geometry, a one-dimensional manifold _S_ 1 is a curve so its curvature always vanishes. The case with _n_ = 1 is special in this sense. 

4.2 _α_ -Geometry in _Sn_ and _R_ + _[n]_ 

75 

## **4.2** _**α**_ **-Geometry in** _**Sn**_ **and** _**R**_ **+** _**[n]**_ 

## _**4.2.1 α-Geodesic and α-Pythagorean Theorem in R**_ **+** _**[n]**_ 

The affine and dual affine coordinates of _**R**[n]_ +[due][to][the] _[α]_[-divergence][are][given] by (4.1) and (4.4), respectively. An _α_ -geodesic passing through _**θ**_ 0 is linear in the _α_ -representation _**θ**_ of (4.1), written as 

**==> picture [200 x 10] intentionally omitted <==**

where _t_ is the parameter of the geodesic and _**a**_ is a constant vector, representing the tangent direction of the geodesic. In particular, the _α_ -geodesic connecting two measures _**m**_ 1 and _**m**_ 2 is 

**==> picture [241 x 20] intentionally omitted <==**

Dually, a − _α_ -geodesic is linear in the − _α_ -representation _**η**_ of (4.4), 

**==> picture [200 x 10] intentionally omitted <==**

The − _α_ -geodesic connecting _**m**_ 1 and _**m**_ 2 is 

**==> picture [241 x 20] intentionally omitted <==**

We have the _α_ -version of the Pythagorean theorem and projection theorem. 

**Theorem 4.3** _Given three positive measures_ _**m** ,_ _**n** ,_ _**k** , when the α-geodesic connecting_ _**m** and_ _**n** is orthogonal to the_ − _α-geodesic connecting_ _**n** and_ _**k** ,_ 

**==> picture [243 x 10] intentionally omitted <==**

**Theorem 4.4** _Given_ _**m** and a submanifold S in_ _**R**[n]_ + _[, the point]_ _**[k]**_[ˆ] _[ in S that minimizes] the α-divergence_ 

**==> picture [231 x 19] intentionally omitted <==**

_is the α-projection of_ _**m** to S. When S is an_ − _α-flat submanifold, the projection is unique._ 

_Remark_ When _α_ = −1, _Dα_ [ _**m**_ : _**n**_ ] is the KL-divergence and the theorems are the Pythagorean and projection theorems given in Chap. 1. 

76 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

## _**4.2.2 α-Geodesic in Sn**_ 

Although the _α_ -divergence is a Bregman divergence in _**R**[n]_ +[+][1][, it is not a flat divergence] in _Sn_ for _α_ ̸= ±1. The _α_ -geodesic connecting two probability vectors _**p**_ and _**q**_ in _**R**[n]_ +[+][1][, given by (][4.22][) with] _**[ m]**_[1][=] _**[p]**_[ and] _**[ m]**_[2][=] _**[ q]**_[, is not included in] _[ S][n]_[. However, we] can normalize (4.22) to obtain the probability vector _**p** (t)_ , 

**==> picture [245 x 20] intentionally omitted <==**

where _c(t)_ is determined from 

**==> picture [195 x 28] intentionally omitted <==**

This is included in _Sn_ . We call it the _α_ -geodesic of _Sn_ . We can define the _α_ -projection in _Sn_ by using the _α_ -geodesic. 

## _**4.2.3 α-Pythagorean Theorem and α-Projection Theorem in Sn**_ 

Since _**R**_ + _[n]_[+][1] is _α_ -flat,itssubmanifold _Sn_ enjoysanextendedversionofthePythagorean theorem. The following theorem is due to Kurose (1994) and it holds for a general dual manifold having a constant curvature. 

**Theorem 4.5** _Let_ _**p** ,_ _**q** and_ _**r** be three points in Sn. When the α-geodesic connecting_ _**p** and_ _**q** is orthogonal to the_ − _α-geodesic connecting_ _**q** and_ _**r** ,_ 

**==> picture [313 x 24] intentionally omitted <==**

We omit the proof. This is a generalization of a theorem in the spherical geometry, which has a constant curvature. 

The projection theorem follows from it. 

**Theorem 4.6** _Let M be a submanifold of Sn. Given_ _**p** , the point in M that minimizes the α-divergence from_ _**p** to M is given by the α-geodesic projection of_ _**p** to M._ 

We can easily see from (4.29) that the _α_ -projection gives the critical point of the _α_ -divergence. See Matsuyama (2003) for the minimization of _α_ -divergence and _α_ -projection in ICA (independent component analysis). 

4.2 _α_ -Geometry in _Sn_ and _R_ + _[n]_ 

77 

## _**4.2.4 Apportionment Due to α-Divergence**_ 

We show an interesting application of _α_ -divergence in social science. There are many methods of deciding the numbers of seats proportionately to the populations in states, since the number of seats in a state must be an integer, whereas the ratios of populations are rational numbers. Let _**p**_ = _( pi )_ be the population quotient vector 

**==> picture [185 x 22] intentionally omitted <==**

where _Ni_ is the populations of state _i_ and _N_ =[�] _Ni_ . Let _**q**_ = _(qi )_ be the apportionment quotient vector and _n_ be the total number of seats such that _nqi_ is the number of seats assigned to state _i_ . 

We cannot simply put _**q**_ = _**p**_ , because _nqi_ should be an integer. Hence, we search for a _**q**_ that is a rational vector of the form _qi_ = _ni /n_ closest to _**p**_ . We can use the _α_ -divergence _Dα_ [ _**p**_ : _**q**_ ] to show the closeness of _**p**_ and _**q**_ and search for a rational vector _**q**_ that minimizes _Dα_ [ _**p**_ : _**q**_ ]. There have been proposed many algorithms to decide _**q**_ . Ichimori (2011) and Wada (2012) showed that most existing methods are interpreted as minimization of some _α_ -divergence and their differences are only in the values of _α_ . 

## _**4.2.5 α-Mean**_ 

By using the _α_ -representation, we define the _α_ -mean. Let us consider two positive numbers _x_ and _y_ . We rescale them by 

**==> picture [212 x 10] intentionally omitted <==**

where _h(x)_ is a monotonically increasing differentiable function satisfying _h(_ 0 _)_ = 0. We may call _h(x)_ the _h_ -representation of _x_ . The _α_ -representation is the case of _h(x)_ = _hα(x)_ . 

The quantity called the _h_ -mean of _x_ and _y_ , 

**==> picture [234 x 24] intentionally omitted <==**

is obtained by using the _h_ -representations of _x_ and _y_ , taking their arithmetic mean, and then rescaling it back by using _h_[−][1] . The _α_ -mean of _x_ and _y_ is 

**==> picture [241 x 28] intentionally omitted <==**

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

78 

We further require that the _h_ -mean is scale-free, implying that, for _c >_ 0, the _h_ -mean of _cx_ and _cy_ is _c_ times their _h_ -mean, 

**==> picture [218 x 10] intentionally omitted <==**

The following theorem characterizes the _α_ -mean. 

**Theorem 4.7** (Hardy et al. 1952) _The α-mean using_ 

**==> picture [234 x 26] intentionally omitted <==**

_is the only scale-free means among h-means._ 

_Proof_ We show the proof given by Amari (2007). Let _h_ beamonotonicallyincreasing differentiable function such that the _h_ -mean is scale-free, 

**==> picture [226 x 22] intentionally omitted <==**

By differentiating Eq. (4.36) with respect to _x_ , we derive 

**==> picture [215 x 21] intentionally omitted <==**

where 

**==> picture [203 x 22] intentionally omitted <==**

By putting _c_ = 1, we have 

**==> picture [206 x 21] intentionally omitted <==**

Hence, we derive from (4.37) and (4.39), 

**==> picture [203 x 24] intentionally omitted <==**

Since _m_ takes an arbitrary value as _y_ varies, we have 

**==> picture [195 x 24] intentionally omitted <==**

for a function _g(c)_ of _c_ . By putting 

**==> picture [202 x 10] intentionally omitted <==**

4.2 _α_ -Geometry in _Sn_ and _R_ + _[n]_ 

79 

we have 

**==> picture [217 x 10] intentionally omitted <==**

Hence, we have 

**==> picture [200 x 11] intentionally omitted <==**

By putting _x_ = 1, 

**==> picture [187 x 22] intentionally omitted <==**

for constant _b_ = _k_[′] _(_ 1 _)_ . We finally derive 

**==> picture [215 x 26] intentionally omitted <==**

neglecting a constant of proportionality. In the case of _α_ = 1, we have log _x_ . □ One sees that the family of _α_ -means includes various known means: 

**==> picture [327 x 117] intentionally omitted <==**

The last two cases show that fuzzy logic is naturally included in the _α_ -mean. The _α_ -mean is inversely monotone with respect to _α_ , 

**==> picture [232 x 10] intentionally omitted <==**

This is a generalization of the well-known inequalities 

**==> picture [225 x 23] intentionally omitted <==**

As _α_ increases, the _α_ -mean relies more on the smaller element of { _a, b_ }, while, as _α_ decreases, the larger one is more emphasized. We may say that the _α_ -mean with smaller _α_ is pessimistic, and with larger _α_ is more optimistic. See Fig. 4.1. 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

80 

**Fig. 4.1** _α_ -mean of 1 and 4 for various _α_ 

**==> picture [206 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
m α(1,4)<br>4<br>1<br>α<br>-1 0 1<br>**----- End of picture text -----**<br>


We can further define the weighted _α_ -mean of _a_ 1 _, . . . , ak_ with weights _w_ 1 _, . . . , wk_ by 

**==> picture [255 x 19] intentionally omitted <==**

where _**w**_ = _(w_ 1 _, . . . , wk)_ and _w_ 1 + · · · + _wk_ = 1. This leads us to the _α_ -family of probability distributions in the next subsection. 

## _**4.2.6 α-Families of Probability Distributions**_ 

Given _k_ probability distributions _pi (x), i_ = 1 _, . . . , k_ , we can define their _α_ -mixture by using the _α_ -mean. 

The _α_ -representation of probability density function _p(x)_ is given (Amari and Nagaoka 2000) by 

**==> picture [238 x 25] intentionally omitted <==**

Their _α_ -mixture is defined by 

**==> picture [238 x 31] intentionally omitted <==**

where normalization constant _c_ is necessary to make it a probability distribution. It is given by 

**==> picture [233 x 26] intentionally omitted <==**

The _α_ = −1 mixture is the ordinary mixture and the _α_ = 1 mixture is the exponential mixture. The _α_ = −∞ mixture, 

4.2 _α_ -Geometry in _Sn_ and _R_ + _[n]_ 

81 

**==> picture [219 x 15] intentionally omitted <==**

is the optimistic integration of component distributions in the sense that, for each _x_ , it takes the largest values of the component probabilities. On the contrary, the _α_ = ∞ mixture is pessimistic, taking the minimum of the component probabilities, 

**==> picture [216 x 10] intentionally omitted <==**

The exponential mixture is more pessimistic than the ordinary mixture in the sense that the resulting probability density is close to 0 at _x_ where some of the components are close to 0. 

Let us next consider weighted mixtures. The weighted _α_ -mixture with weights _w_ 1 _, . . . , wk_ satisfying[�] _wi_ = 1 is given by 

**==> picture [244 x 19] intentionally omitted <==**

This is called the _α_ -integration of _p_ 1 _(x), . . . , pk(x)_ with weights _w_ 1 _, . . . , wk_ . It connects _k_ component distributions _p_ 1 _(x), . . . , pk(x)_ continuously by using the parameter _**w**_ = _(w_ 1 _, . . . , wk)_ . It is called the _α_ -family of probability distributions where _**w**_ plays the role of its coordinate system. When _α_ = −1, this is an ordinary mixture family, 

**==> picture [219 x 15] intentionally omitted <==**

where[�] _wi_ = 1 is imposed. When _α_ = 1, this is an exponential family, 

**==> picture [256 x 19] intentionally omitted <==**

where the normalization constant is given by 

**==> picture [197 x 11] intentionally omitted <==**

The probability simplex _Sn_ (and the function space _F_ of probability distributions) are special, satisfying the following theorem. 

**Theorem 4.8** _The probability simplex Sn is an α-family for any α._ 

_Proof Sn_ is a mixture of _δi (x)_ , 

**==> picture [206 x 29] intentionally omitted <==**

The _α_ -mixture family of _δi (x)_ is 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

82 

**==> picture [231 x 23] intentionally omitted <==**

where 

**==> picture [226 x 16] intentionally omitted <==**

They cover the entire _Sn_ so that _Sn_ is an _α_ -family. 

**==> picture [9 x 7] intentionally omitted <==**

Wecanalsoshowthatan _α_ -geodesicconnecting _**p**_ and _**q**_ in _Sn_ isaone-dimensional _α_ -family. 

## _**4.2.7 Optimality of α-Integration**_ 

When a cluster of _k_ distributions _p_ 1 _(x), . . . , pk(x)_ is given, we search for _q(x)_ that is close to all of _p_ 1 _(x), . . . , pk(x)_ . It is regarded as the center of the cluster. Let _w_ 1 _, . . . , wk_ be weights assigned to _pi (x), i_ = 1 _, . . . , k_ , and we use the weighted average of divergences from _pi (x)_ ’s to _q(x)_ , 

**==> picture [239 x 15] intentionally omitted <==**

as a risk function. We search for the distribution _q(x)_ that minimizes _RD_ [ _q(x)_ ]. The minimizer of _RD_ is called the _D_ -optimal integration of _p_ 1 _(x), . . . , pk(x)_ with weights _w_ 1 _, . . . , wk_ . The following theorem characterizes the _α_ -integration (Amari 2007). 

**Theorem 4.9** (Optimality of _α_ -integration) _The α-integration of probability distributions p_ 1 _(x), . . . , pk(x) with weights w_ 1 _, . . . , wk is optimal under the α-risk,_ 

**==> picture [243 x 15] intentionally omitted <==**

_where Dα is the α-divergence._ 

_Proof_ Let us first prove the case of _α_ ̸= ±1. By taking the variation of _Rα_ [ _q(x)_ ] under the normalizing constraint 

**==> picture [198 x 23] intentionally omitted <==**

we derive 

**==> picture [289 x 62] intentionally omitted <==**

4.2 _α_ -Geometry in _Sn_ and _R_ + _[n]_ 

83 

where _λ_ is the Lagrange multiplier. This gives 

**==> picture [234 x 15] intentionally omitted <==**

and hence, the optimal _q(x)_ is 

**==> picture [235 x 19] intentionally omitted <==**

When _α_ = ±1, we obtain 

**==> picture [272 x 24] intentionally omitted <==**

**==> picture [278 x 25] intentionally omitted <==**

respectively. Hence, the optimal _q_ is proved to be the _α_ -integration for any _α_ . □ 

The case with unnormalized probabilities, i.e., positive measures, is similar. The optimal integration _m_ ˜ _α(x)_ of _m_ 1 _(x), . . . , mk(x)_ under the _α_ -divergence criterion is 

**==> picture [237 x 18] intentionally omitted <==**

where the normalization constant is not necessary. 

There are interesting papers concerning applications of the _α_ -integration of stochastic evidences, see e.g., Wu (2009), Choi et al. (2013) and Soriano and Vergara (2015). 

## _**4.2.8 Application to α-Integration of Experts**_ 

Let us consider a system composed of _k_ experts _M_ 1 _, . . . , Mk_ , each of which processes input signal _**x**_ and emits its own answer. The answer of _Mi_ is a response _y_ corresponding to _**x**_ . More generally, consider the case that the output of _Mi_ is a probability distribution of _y_ , _pi (y_ | _**x** )_ , or a positive measure, _mi (y_ | _**x** )_ . The entire system integrates these answers and provides an integrated answer concerning the distribution of _y_ given _**x**_ (Fig. 4.2). 

Let us assume that _wi (_ _**x** )_ is given as the weight or reliability of _Mi_ for input _**x**_ . The _α_ -risk of an integrated answer _q(y_ | _**x** )_ is given by 

**==> picture [263 x 15] intentionally omitted <==**

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

84 

**==> picture [255 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
p 1 [(] y | x )<br>M 1<br>M 2<br>x . p 2 [(] y | x ) q ( y | x )<br>Mk<br>p y | x )<br>k [(]<br>...<br>**----- End of picture text -----**<br>


**Fig. 4.2** Integration of answers of expert machines 

**Theorem 4.10** _The α-expert machine_ 

**==> picture [246 x 13] intentionally omitted <==**

_is optimal under the α-risk Rα_ [ _q(y_ | _**x** )_ ] _._ 

Similar assertions hold for the case of positive measures. 

The _α_ = 1 machine is the mixture of experts (Jacobs et al. 1991) and the _α_ = −1 machine is the product of experts (Hinton 2002). 

It is important to determine the weights or reliability functions _wi (_ _**x** )_ . When a teacher output _q_[∗] _(y_ | _**x** )_ is available, one may use the soft-max function 

**==> picture [255 x 10] intentionally omitted <==**

as the weight of _Mi_ , where _c_ is the normalization constant and _β_ is the “inverse temperature”, indicating the effectiveness of the weights. 

## **4.3 Geometry of Tsallis** _**q**_ **-Entropy** 

TheBoltzmann–Gibbsdistributioninstatisticalphysicsisanexponentialfamily,such that an invariant flat structure is given to the underlying manifold. Its convex function is free energy and its dual convex function is the negative of the Shannon entropy. C. Tsallis proposed a generalized entropy called the _q_ -entropy for studying various phenomena not included in the conventional Boltzmann–Gibbs framework (Tsallis 1988, 2009). The induced probability distributions are not exponential families which are subject to exponential decay of tail probabilities. This has opened the door to a new world of physics and beyond. The _q_ -logarithm and _q_ -exponential are introduced to this end. However, the _q_ -logarithm is essentially the same as the _α_ -representation, where _q_ and _α_ are connected by _α_ = 2 _q_ − 1. Therefore, the _α_ -geometry covers the 

85 

4.3 Geometry of Tsallis _q_ -Entropy 

geometry of _q_ -entropy physics (Ohara 2007). We treat the discrete case of _Sn_ mostly, but the results hold in the continuous case, too. 

We further extend the _q_ -framework by using the _q_ -escort distribution. This gives a new dually flat structure to _Sn_ , although it is not invariant (Amari and Ohara 2011). It is conformally related to the invariant geometry (Amari et al. 2012). This framework is extended further to deformed exponential families proposed by Naudts (2011). 

## _**4.3.1 q-Logarithm and q-Exponential Function**_ 

Tsallis introduced a generalized logarithm, called the _q_ -logarithm, by 

**==> picture [226 x 24] intentionally omitted <==**

which gives log _u_ in the limit _q_ → 1. The inverse of the _q_ logarithm is the _q_ -exponential, 

**==> picture [227 x 16] intentionally omitted <==**

which gives the ordinary exponential function in the limit _q_ → 1. These functions are the same as the _α_ -representation _hα(u)_ and its inverse, where _α_ = 2 _q_ − 1, except for a scaling factor and a constant. However, we keep the original _q_ -notation rather than the _α_ -notation in this section, respecting the original _q_ -terminology by C. Tsallis. 

The Tsallis _q_ -entropy is defined by 

**==> picture [216 x 23] intentionally omitted <==**

by replacing log by log _q_ , which is concave for 0 _< q_ ≤ 1 and is the Shannon entropy when _q_ = 1. This is closely related to the Rényi entropy (Rényi 1961). Similarly, the _q_ -divergence is defined by 

**==> picture [281 x 25] intentionally omitted <==**

where E is the expectation with respect to _**p**_ . This is the same as the _α_ -divergence (3.39) with _α_ = 2 _q_ − 1. 

The geometry derived from the _q_ -divergence satisfies the invariance criterion, since it belongs to the class of _f_ -divergence. So the Riemannian metric is given by the Fisher information matrix. Further, it is not dually flat except for the limiting cases of _q_ = 0 _(α_ = −1 _)_ and 1 _(α_ = 1 _)_ . However, if we extend it to the manifold of positive measures, it is both invariant and dually flat. 

86 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

## _**4.3.2 q-Exponential Family (α-Family) of Probability Distributions**_ 

We define the _q_ -exponential family by 

**==> picture [227 x 12] intentionally omitted <==**

or equivalently by 

**==> picture [233 x 14] intentionally omitted <==**

wherelog _q_ andexp _q_ areusedinsteadoflogandexpintheordinaryexponentialfamily. This is an _α_ -family (4.60) of _Sn_ , in which _hα_ is used instead of log _q_ , _**θ**_ = _(wi )_ and _**x**_ = { _δi (x)_ }. Here, _ψq (_ _**θ** )_ is determined from the normalization constraint 

**==> picture [232 x 23] intentionally omitted <==**

Another example is the _q_ -Gaussian distribution, given by 

**==> picture [249 x 52] intentionally omitted <==**

where random variable _x_ takes continuous values. Different from a Gaussian distribution, the values of _x_ are limited within a finite range. Another important _q_ -family is _Sn_ . We rewrite Theorem 4.8 in the following form. 

**Theorem 4.11** _The family Sn of all the discrete distributions is a q-family for any q, that is an α-family for any α._ 

_Proof_ By introducing random variables _δi (x)_ and putting _**x**_ = _(δ_ 1 _(x), . . . , δn(x))_ , a probability _**p**_ ∈ _Sn_ is written, using parameter _**θ**_ , in the form 

**==> picture [308 x 31] intentionally omitted <==**

where the coordinate system _**θ**_ is 

**==> picture [252 x 24] intentionally omitted <==**

4.3 Geometry of Tsallis _q_ -Entropy 

87 

Hence, it is a _q_ -family ( _α_ -family). The function corresponding to the free energy is 

**==> picture [207 x 12] intentionally omitted <==**

where _p_ 0 is a function of _**θ**_ . We call it the _q_ -free energy. □ 

## _**4.3.3 q-Escort Geometry**_ 

The _q_ -geometry ( _α_ -geometry) is induced in a _q_ -exponential family from the _q_ - divergence.ItconsistsoftheFisherinformationmetric(3.68)andcubictensordefined in (3.88). It is invariant but not flat in general. This is because the _q_ -divergence ( _α_ - divergence) is not a Bregman divergence in general. However, it is possible to modify it conformally to obtain a new dually flat structure. To begin with, we show that the _q_ -free energy _ψq (_ _**θ** )_ defined by (4.80) is a convex function of _**θ**_ . 

**Lemma 4.1** _The q-free energy is convex._ 

_Proof_ By differentiating (4.79) with respect to _**θ**_ , we have 

**==> picture [238 x 13] intentionally omitted <==**

Its second derivatives are 

_∂i ∂ j p(_ _**x** ,_ _**θ** )_ = _qp(_ _**x** ,_ _**θ** )_[2] _[q]_[−][1][ �] _xi_ − _∂i ψq_ �� _x j_ − _∂ j ψq_ � − _p(_ _**x** ,_ _**θ** )[q] ∂i ∂ j ψq ._ (4.87) 

We introduce a functional 

**==> picture [218 x 23] intentionally omitted <==**

which is the Tsallis _q_ -entropy except for a scale and constant. Then, from (4.86) and (4.87) and by using the identities 

**==> picture [253 x 23] intentionally omitted <==**

we have 

**==> picture [296 x 53] intentionally omitted <==**

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

88 

the latter of which shows that the Hessian of _ψq_ is positive-definite. This is called the _q_ -metric 

**==> picture [202 x 13] intentionally omitted <==**

which is different from the invariant Fisher metric. 

A new dually flat structure is introduced in _Sn_ by the _q_ -free-energy, which is different from the free energy. The affine coordinates are _θ[i]_ given by (4.84). The dual affine coordinate system _**η**_ is given by 

**==> picture [215 x 26] intentionally omitted <==**

The dual convex function is the inverse of the _q_ -entropy 

**==> picture [230 x 25] intentionally omitted <==**

except for a scale and constant. 

The Bregman divergence derived by _ψq_ is 

**==> picture [310 x 25] intentionally omitted <==**

which is different from the _q_ -divergence _Dq_ . _D_[˜] _q_ gives another dually flat Riemannian structure to _Sn_ . 

By putting 

**==> picture [209 x 40] intentionally omitted <==**

**==> picture [225 x 28] intentionally omitted <==**

holds. So _**η**_ gives another probability distribution _**p**_ ˜ of _Sn_ . We call it the escort probability distribution of _**p**_ . The escort distribution is obtained by changing _pi_ to _pi[q][/][h][q]_[which shifts] _**[p]**_[ toward the center (the uniform distribution] _**[p]**_ 0[) as] _[ q]_[ decreases] from _q_ = 1. 

We can define the _q_ -escort geodesic and dual _q_ -escort geodesic in _Sn_ . By using these geodesics, the _q_ -Pythagorean theorem holds with respect to the _q_ -escort divergence. One of the important consequences is the _q_ -max entropy theorem. To this end, we define the _q_ -escort expectation by 

**==> picture [227 x 24] intentionally omitted <==**

4.3 Geometry of Tsallis _q_ -Entropy 

89 

**Fig. 4.3** _q_ -max entropy theorem 

**==> picture [72 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
q -exponential<br>x“<br>family<br>= a 1 Mk (    ) a 1<br>= a 2 iy Mk (    ) a 2<br>p 0<br>...<br>**----- End of picture text -----**<br>


**Theorem 4.12** ( _q_ -Max-Entropy Theorem) _Let Mk(_ _**a** ) be a submanifold of Sn consisting of probability distributions of which the q-escort expectations of random variables c_ 1 _(_ _**x** ), . . . , ck(_ _**x** ) take fixed values,_ 

**==> picture [230 x 13] intentionally omitted <==**

ˆ _where_ _**a**_ = _(a_ 1 _, . . . , ak). The probability distribution_ _**p** (_ _**a** ) in Mk(_ _**a** ) that maximizes the q-entropy is given by the q-geodesic projection of the uniform distribution_ _**p**_ 0 _to Mk(_ _**a** ). The family of such distributions for various_ _**a**_ = _**θ** is a q-exponential family of distributions,_ 

**==> picture [230 x 14] intentionally omitted <==**

_Proof_ This is clear from the fact that _Mk_ is flat in the dual sense and (4.101) is a flat submanifold in the primal sense. See Fig. 4.3. □ 

## _**4.3.4 Deformed Exponential Family: χ-Escort Geometry**_ 

We used the _q_ -logarithm to define the _q_ -structure in _Sn_ . However, we may use a more general representation to study various dually flat structures of _Sn_ . See, for example, a deformed exponential family called the _κ_ -exponential family (Kaniadakis and Scarfone 2002). Following Naudts (2011), we introduce the _χ_ -logarithm defined by 

**==> picture [211 x 24] intentionally omitted <==**

where _χ_ is a positive non-decreasing function. We simply put 

**==> picture [199 x 12] intentionally omitted <==**

_α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

90 

4 

When _χ_ is a power function 

**==> picture [207 x 10] intentionally omitted <==**

it gives the _q_ -logarithm. We use the inverse of _u_ as the _v_ -representation, 

**==> picture [219 x 14] intentionally omitted <==**

The _χ_ -deformed exponential family is defined by using (4.105) as 

**==> picture [234 x 14] intentionally omitted <==**

where _ψχ_ is the free-energy corresponding to the normalization factor. 

**Theorem 4.13** _Sn is a χ-exponential family for any χ function._ 

_Proof_ We can prove the theorem in the same way as Theorem 4.11, by replacing log _q_ by log _χ_ . The affine coordinates are 

**==> picture [233 x 12] intentionally omitted <==**

and the _χ_ -free-energy is 

**==> picture [205 x 11] intentionally omitted <==**

The _χ_ -free-energy is a convex function of _**θ**_ , so we can introduce a new dually flat affine structure together with a Riemannian metric. The Riemannian metric is written anew as 

**==> picture [297 x 27] intentionally omitted <==**

where _hχ(_ _**θ** )_ is the _χ_ -escort entropy defined by 

**==> picture [301 x 24] intentionally omitted <==**

The dual affine coordinates are given by 

**==> picture [256 x 26] intentionally omitted <==**

where 

**==> picture [204 x 24] intentionally omitted <==**

4.3 Geometry of Tsallis _q_ -Entropy 

91 

is used. The dual _**η**_ in (4.111) defines a probability distribution _**p**_ ˜ called the _χ_ -escort distribution. The dual convex function is 

**==> picture [217 x 29] intentionally omitted <==**

The _χ_ -divergence is 

**==> picture [253 x 46] intentionally omitted <==**

The generalized Pythagorean theorem holds as well. 

**==> picture [9 x 8] intentionally omitted <==**

_Remark_ The exp _χ(u)_ is a convex function. Vigelis and Cavalcante (2013) introduced a _ϕ_ -family of probability distributions by using a convex function _ϕ(u)_ . A new representation _f (x)_ of a probability density function _p(x)_ is given by 

**==> picture [201 x 10] intentionally omitted <==**

This is closely related to the _χ_ -representation. A _ϕ_ -family of probability distributions and _ϕ_ -divergence are defined in this framework, giving a dually flat structure. It is possible to extend to the non-parametric case. 

## _**4.3.5 Conformal Character of q-Escort Geometry**_ 

The _q_ -divergence is an invariant divergence, leading to the Fisher information metric. The _q_ -escort divergence (4.95) is not invariant and the derived metric is not the Fisher information metric. However, we see that the _q_ -metric is connected to the Fisher metric _gi j (_ _**θ** )_ by 

**==> picture [235 x 10] intentionally omitted <==**

where 

**==> picture [198 x 25] intentionally omitted <==**

This implies that the metric is changed pointwise isotropically, implying that the magnitude of a vector is enlarged or shrunken by a factor _σ(_ _**p** )_ but the angle of two vectors never changes, keeping the orthogonality invariant. Such a transformation of metric is called a conformal transformation. Hence, the _q_ -escort structure is given by a conformal transformation from the invariant geometry. However, this property does not hold in the general _χ_ -structure. We show the following theorem without proof. See Amari et al. (2012) and Ohara et al. (2012). 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

92 

**Theorem 4.14** _The q-escort geometry is unique among the χ-escort geometries in the sense that its Riemannian metric is derived by a conformal transformation of the invariant Fisher metric._ 

_Remark_ Conformal transformations are used in asymptotic theory of statistical inference (Okamoto et al. 1991; Kumon et al. 2011). They are also used in improving a kernel function in support vector machines, which will be shown later in Chap. 11. 

## **4.4** _**(u, v)**_ **-Divergence: Dually Flat Divergence in Manifold of Positive Measures** 

We have used _p_ and log _p_ representations of probability, which play the role of two dual coordinate systems in the invariant geometry. We have further used the _α_ - or _q_ -representations, which lead us to the _α_ -geometry. The generalized deformed exponential family uses the _χ_ -representation. A representation of probability defines the geometry. The importance of representation was emphasized by Zhang (2004). Eguchi et al. (2014) uses a _U_ -representation to define the _U_ structure which is dually 

The present section considers _**R**[n]_ +[and introduces a dually flat structure by using a] pair of representations. We extend the idea given by Zhang (2011, 2013) and establish a general dually flat structure in _**R**[n]_ +[. The present section mostly follows Amari (2014)] to define general decomposable and non-decomposable Bregman divergences in a manifold of positive measures. In the next section, they are extended to invariant Bregman divergences of a manifold of positive-definite matrices. 

## _**4.4.1 Decomposable (u, v)-Divergence**_ 

Let us use two monotonically increasing and differentiable functions _u(m)_ and _v(m)_ 

**==> picture [214 x 11] intentionally omitted <==**

They are called the _u_ - and _v_ -representations of positive measure _m_ , respectively. Given _**m**_ ∈ _**R**[n]_ +[, we call] _**[ θ]**_[=] � _θ[i]_[�] and _**η**_ = _(ηi )_ defined by 

**==> picture [223 x 12] intentionally omitted <==**

the _u_ - and _v_ -representations of _**m**_ , respectively. The _**θ**_ and _**η**_ are coordinate systems in _**R**_[+] _n_[. We search for a dually flat structure such that the] _[ u]_[- and] _[ v]_[-representations of] _**m**_ become two affine coordinates. To this end, we define a pair of convex functions _ψu,v(_ _**θ** )_ and _ϕu,v(_ _**η** )_ from which a Bregman divergence _Du,v_ � _**m**_ : _**m**_[′][�] is derived. We define two scalar functions of _θ_ and _η_ by 

4.4 _(u, v)_ -Divergence: Dually Flat Divergence in Manifold of Positive Measures 

93 

**==> picture [235 x 57] intentionally omitted <==**

By differentiation, we have 

**==> picture [203 x 41] intentionally omitted <==**

Since˜ _u_[′] _(m) >_ 0, _v_[′] _(m) >_ 0, _ψ_[˜] _u_[′′] _,v[>]_[0. Hence,] _[ψ]_[˜] _[u][,v][(][θ][)]_[ is a convex function. So is] _ϕu,v(η)_ . Moreover, they are the Legendre duals, because 

**==> picture [255 x 51] intentionally omitted <==**

We now define decomposable convex functions of _**θ**_ and _**η**_ by 

**==> picture [218 x 34] intentionally omitted <==**

**Definition 4.1** The _(u, v)_ -divergence between two points _**m** ,_ _**m**_[′] ∈ _**R**_[+] _n_[is][defined] by 

**==> picture [281 x 70] intentionally omitted <==**

where _**θ**_ and _**η**_[′] are _u_ - and _v_ -representations of _**m**_ and _**m**_[′] , respectively. 

The _(u, v)_ -divergence gives a dually flat structure, where _**θ**_ and _**η**_ are affine and dual affine coordinate systems. The transformation between _**θ**_ and _**η**_ is simple in the _(u, v)_ -structure, because it can be done componentwise, 

**==> picture [205 x 29] intentionally omitted <==**

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

94 

This is a merit of the _(u, v)_ -divergence. The Riemannian metric is given by 

**==> picture [209 x 25] intentionally omitted <==**

It is easy to see that this is a Euclidean metric. We have a new coordinate system _**r** (_ _**m** )_ 

**==> picture [221 x 31] intentionally omitted <==**

in which the Riemannian metric is _gi j_ = _δi j_ . The following theorem follows immediately. 

**Theorem 4.15** _A decomposable and dually flat divergence in_ _**R**[n]_ + _[is][a][(][u][, v)][-] divergence when it is invariant under the permutation of indices._ 

Many divergences are written in the form of _(u, v)_ -divergence. 

## **1.** _**(α, β)**_ **-divergence** 

From the following power functions, 

**==> picture [316 x 50] intentionally omitted <==**

is derived. This was introduced by Cichocki and Amari (2010) and Cichocki et al. (2011). The affine and dual affine coordinates are 

**==> picture [229 x 24] intentionally omitted <==**

and the convex functions are 

**==> picture [260 x 19] intentionally omitted <==**

where 

**==> picture [213 x 24] intentionally omitted <==**

## **2.** _**α**_ **-divergence** 

By putting 

**==> picture [255 x 23] intentionally omitted <==**

95 

4.4 _(u, v)_ -Divergence: Dually Flat Divergence in Manifold of Positive Measures 

we have 

**==> picture [321 x 25] intentionally omitted <==**

This is a special case of the _(α, β)_ -divergence. 

## **3.** _**β**_ **-divergence** 

From 

**==> picture [228 x 23] intentionally omitted <==**

we have 

**==> picture [333 x 39] intentionally omitted <==**

This is the _β_ -divergence (Minami and Eguchi 2004). It gives a dually flat structure even in _Sn_ . This is because _u(m)_ is linear in _m_ . 

## **4.** _**U**_ **-divergence** 

From 

**==> picture [226 x 11] intentionally omitted <==**

where _U (m)_ is a convex function, we have the _U_ -divergence (Eguchi et al. 2014). 

## _**4.4.2 General (u, v) Flat Structure in R**_ **+** _**[n]**_ 

We consider a general dually flat structure of _**R**[n]_ +[which is not necessarily decom-] posable. Let us introduce a new coordinate system 

**==> picture [188 x 10] intentionally omitted <==**

in _**R**[n]_ +[, where] _**[ u]**_[ is an arbitrary differentiable bijective vector function. We can define] a dually flat structure in _**R**[n]_ +[by][using][an][arbitrary][convex][function] _[ψ][(]_ _**[θ]**[)]_[.] _**[θ]**_[is][the] associated affine coordinate system and the dual affine coordinates are 

**==> picture [192 x 11] intentionally omitted <==**

We put 

**==> picture [200 x 10] intentionally omitted <==**

96 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

This structure is used in Nock et al. (2015). 

An arbitrary pair _(_ _**u** ,_ _**v** )_ of coordinate systems do not necessarily give a dually flat structure. They give dually flat structure when and only when there exists a convex function _ψ(_ _**θ** )_ such that 

**==> picture [199 x 14] intentionally omitted <==**

is its gradient. In the case of a decomposable pair _(u, v)_ , the condition is always satisfied and the pair always defines a dually flat structure. 

The Riemannian metric induced from a _(_ _**u** ,_ _**v** )_ -structure is _G(_ _**θ** )_ = ∇∇ _ψ(_ _**θ** )_ , which is not Euclidean in general. 

## **4.5 Invariant Flat Divergence in Manifold** 

The present section studies information geometry of the manifold of positive-definite matrices, following Amari (2014). See also Ohara and Eguchi (2013). An extensive review is found in Cichocki et al. (2015). A positive definite matrix **A** is decomposed as 

**==> picture [193 x 11] intentionally omitted <==**

where _**�**_ is a diagonal matrix consisting of positive entries (eigenvalues of **A** ) and **O** is an orthogonal matrix. A positive-definite diagonal matrix is compared with a positive measure distribution. When its trace is 1, it is compared with a probability distribution. So a positive-definite matrix is an extension of a positive measure. Therefore, one can introduce a dually flat structure to the manifold of positivedefinite matrices with the help of the _(u, v)_ -structure. The manifold of positivedefinite Hermitian matrices, in particular those with a trace equal to 1, are important in quantum information theory, but we do not study them, treating only the real case. 

## _**4.5.1 Bregman Divergence and Invariance Under Gl(n)**_ 

Let **P** be a positive-definite symmetric matrix and _ψ(_ **P** _)_ be a convex function. A Bregman divergence is defined between two positive-definite matrices **P** and **Q** by 

**==> picture [262 x 10] intentionally omitted <==**

where ∇ is the gradient operator with respect to matrix **P** = � _Pi j_ � and hence ∇ _ψ_ is a matrix, and the inner product of two matrices is defined by 

**==> picture [201 x 10] intentionally omitted <==**

4.5 Invariant Flat Divergence in Manifold of Positive-Definite Matrices 

97 

It induces a dually flat structure in the manifold of positive-definite matrices, where the affine coordinate system is **P** itself and the dual affine coordinate system is 

**==> picture [194 x 10] intentionally omitted <==**

There is a one-to-one correspondence between positive-definite matrices and zeromean multivariate Gaussian distributions. Indeed, a zero-mean multivariate Gaussian distribution is given by using a positive-definite matrix **P** as 

**==> picture [268 x 25] intentionally omitted <==**

which is an exponential family. Its _e_ -affine coordinates are **P**[−][1] . The flat geometry is, therefore, given by the KL-divergence, 

**==> picture [261 x 14] intentionally omitted <==**

which is obtained from the potential function 

**==> picture [223 x 12] intentionally omitted <==**

Let us consider a linear transformation of **P** by **L** ∈ _Gl(n)_ , which is the set of all non-degenerate _n_ × _n_ matrices, given by 

**==> picture [191 x 12] intentionally omitted <==**

This corresponds to the transformation of random variable _**x**_ to 

**==> picture [184 x 10] intentionally omitted <==**

A divergence is said to be invariant under _Gl(n)_ when it satisfies 

**==> picture [234 x 13] intentionally omitted <==**

Since the KL-divergence is invariant under any transformation of _**x**_ , it is invariant under _Gl(n)_ . 

**Theorem 4.16** _The KL-divergence is a flat divergence which is invariant under Gl(n) in the manifold of positive-definite matrices._ 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

98 

## _**4.5.2 Invariant Flat Decomposable Divergences Under O(n)**_ 

The eigenvalues of a positive-definite matrix do not change under an orthogonal transformation **O** ∈ _O(n)_ , the group of orthogonal matrices. It is natural to consider a dually flat structure which is invariant under _O(n)_ . 

## **4.5.2.1 The Case When P is** _**e**_ 

We have a convex function _ψ(_ **P** _)_ of **P** in this case. It is invariant under _O(n)_ when 

**==> picture [208 x 13] intentionally omitted <==**

An invariant function is a symmetric function of _n_ eigenvalues _λ_ 1 _, . . . , λn_ of **P** (Dhillon and Tropp 2007). An invariant convex function of **P** is written using a convex function _f_ of one variable satisfying _f (_ 0 _)_ = 0 as 

**==> picture [229 x 15] intentionally omitted <==**

when it is decomposable in the additive form of _λi_ . We study this case. We can prove the following lemma. 

## **Lemma** 

**==> picture [215 x 12] intentionally omitted <==**

_Outlineoftheproof._ Weassumethat _f_ isananalyticfunction.Then, _f (_ **P** _)_ is expanded in a power series of **P** . Therefore, we prove the lemma in the case of _f (_ **P** _)_ = **P** _[n]_ , which is easy. Hence, we have the lemma. □ 

Let _g(u)_ be a function such that _g_[′] _(u)_ is the inverse function of _f_[′] _(u)_ , satisfying _g(_ 0 _)_ = 0. Then, the inverse transformation from **P**[′] to **P** is given by 

**==> picture [192 x 13] intentionally omitted <==**

Hence, the dual potential function is 

**==> picture [213 x 13] intentionally omitted <==**

**Theorem 4.17** _An e-flat decomposable O(n)-invariant divergence is given by_ 

**==> picture [268 x 13] intentionally omitted <==**

_where ϕ f is the Legendre dual of ψ f ._ 

We give well-known examples of invariant symmetric convex functions and dually flat divergences. 

4.5 Invariant Flat Divergence in Manifold of Positive-Definite Matrices 

99 

- (1) For _f (λ)_ = _(_ 1 _/_ 2 _)λ_[2] , we have 

**==> picture [201 x 22] intentionally omitted <==**

**==> picture [217 x 22] intentionally omitted <==**

where ∥ **P** ∥[2] is the Frobenius norm 

**==> picture [199 x 14] intentionally omitted <==**

This gives a Euclidean structure. 

(2) For _f (λ)_ = − log _λ_ , we have (4.152) and (4.151), which are invariant under _Gl(n)_ . 

(3) For _f (λ)_ = _λ_ log _λ_ − _λ_ , 

**==> picture [240 x 10] intentionally omitted <==**

**==> picture [256 x 10] intentionally omitted <==**

This divergence is used in quantum information theory. The affine coordinate system is **P** , the dual affine coordinate system is log **P** and _ψ(_ **P** _)_ is related to the von Neumann entropy. 

## **4.5.2.2 General Dually Flat Decomposable Case:** _**(u, v)**_ **-Divergence** 

We use the _(u, v)_ -structure to introduce a general dually flat invariant decomposable divergence. Let 

**==> picture [214 x 10] intentionally omitted <==**

be _u_ - and _v_ -representations of matrices. We use two functions _ψ_[˜] _u,v(θ)_ and _ϕ_ ˜ _u,v(η)_ defined by (4.120) and (4.121) for defining a pair of dually coupled invariant convex functions, 

**==> picture [210 x 27] intentionally omitted <==**

They are not convex with respect to **P** , but convex with respect to _**�**_ and **H** , respectively. The derived Bregman divergence is 

**==> picture [289 x 10] intentionally omitted <==**

It induces a dually flat structure to the manifold of positive-definite matrices. 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

100 

**Theorem 4.18** _A dually flat, invariant and decomposable divergence is a (u, v)divergence in the manifold of positive-definite matrices._ 

The Euclidean, Gaussian and von Neumann divergences given in (4.163), (4.151) and (4.166) are special examples of _(u, v)_ -divergences. They are given by 

**==> picture [233 x 48] intentionally omitted <==**

When _u_ and _v_ are power functions, we have the _(α, β)_ -structure in the manifold of positive-definite matrices. 

(4) _(α_ - _β)_ -divergence 

By using the _(α, β)_ -structure given by (4.132), we have 

**==> picture [249 x 48] intentionally omitted <==**

and the _(α, β)_ -divergence of matrices, 

**==> picture [296 x 25] intentionally omitted <==**

This is a Bregman divergence, where the affine coordinate system is _**�**_ = **P** _[α]_ and its dual is **H** = **P** _[β]_ . 

(5) The _α_ -divergence is derived as 

**==> picture [270 x 48] intentionally omitted <==**

**==> picture [288 x 25] intentionally omitted <==**

The affine coordinate system is 1−2 _α_ **[P]** 1−2 _α_ and its dual is 1+2 _α_ **[P]** 1+2 _α_ . (6) The _β_ -divergence is derived from (4.139) as 

**==> picture [321 x 23] intentionally omitted <==**

4.5 Invariant Flat Divergence in Manifold of Positive-Definite Matrices 

101 

## _**4.5.3 Non-flat Invariant Divergences**_ 

We have so far studied invariant flat divergences. There are other types of invariant divergences which are not necessarily flat. We remark that the eigenvalues of _**P Q**_[−][1] are invariant under _Gl(n)_ , because, for **P**[˜] = **L** _[T]_ **PL** and **W**[˜] = **L** _[T]_ **QL** , 

**==> picture [224 x 16] intentionally omitted <==**

holds. So a divergence _D_ [ **P** : **Q** ] is invariant when it is written as a function of _**�**_ = _diag (λ_ 1 _, . . . , λn)_ , where _λi_ are the eigenvalues of **PQ**[−][1] . Cichocki et al. (2015) introduced the following ( _α_ - _β_ )-log-det divergence: 

**==> picture [293 x 28] intentionally omitted <==**

which can be written in terms of _**�**_ as 

**==> picture [255 x 56] intentionally omitted <==**

It is extended to the case of _α_ = 0 and/or _β_ = 0 by taking the limit _α, β_ → 0. For example, 

**==> picture [276 x 46] intentionally omitted <==**

When _α_ = _β_ , _Dα_[log - det] _,β_ [ **P** : **Q** ] is symmetric with respect to **P** and **Q** and hence the geometry is self-dual and Riemannian. 

It is interesting to see that _Dα_[log - det] _,β_ [ **P** : **Q** ] generates the same Riemannian metric not depending on _α_ and _β_ , although the dual affine connections do depend on _α_ and _β_ . 

**Theorem 4.19** _The Riemannian metric induced from the (α, β)-_ log _-_ det _divergence is_ 

**==> picture [235 x 22] intentionally omitted <==**

We omit the proof. 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

102 

## **4.6 Miscellaneous Divergences** 

Many divergences have been defined in the literature. We show some of them. They are not invariant and not flat in general, but have their own characteristics. An extensive survey on divergence is found in Basseville (2013). See also Cichocki et al. (2009, 2011), for example. Only a Bregman divergence generates a dually flat structure. However, any divergence generates a dual pair of affine connections together with a Riemannian metric, as will be shown in Part II. 

## _**4.6.1 γ-Divergence**_ 

The _γ_ -divergence was proposed by Fujisawa and Eguchi (2008). See also Cichocki and Amari (2010). Let _γ_ be a real parameter. The _γ_ -divergence between two probability distributions _**p**_ and _**q**_ is defined by 

**==> picture [257 x 36] intentionally omitted <==**

It is projectively invariant in the sense that, for any positive constants _c_ 1 and _c_ 2, 

**==> picture [223 x 13] intentionally omitted <==**

## holds. 

The _γ_ -divergence has a super-robust property when we use it in statistical estimation. It is extremely robust even when outliers are mixed in observed data. It is possible to define the _γ_ -divergence between positive-definite matrices **P** and **Q** as 

**==> picture [256 x 29] intentionally omitted <==**

## _**4.6.2 Other Types of (α, β)-Divergences**_ 

Zhang (2004) introduced the following _(α, β)_ -divergence, 

**==> picture [278 x 56] intentionally omitted <==**

4.6 Miscellaneous Divergences 

103 

which is different from that in the previous subsection. The geometry induced from (4.190) is exactly the same as the _α_ -geometry. 

Zhang (2011) presented another _α_ -divergence when a convex function _ψ(_ _**p** )_ exists. It is given by 

**==> picture [280 x 53] intentionally omitted <==**

Furuichi (2010) also introduced another _(α_ - _β)_ -divergence, 

**==> picture [272 x 24] intentionally omitted <==**

## _**4.6.3 Burbea–Rao Divergence and Jensen–Shannon Divergence**_ 

For a convex function _F(_ _**p** )_ , one can construct a symmetric divergence by 

**==> picture [262 x 25] intentionally omitted <==**

This is called the Burbea–Rao divergence (Burbea and Rao 1982). When we use the negative of entropy as a convex function, we have 

**==> picture [266 x 25] intentionally omitted <==**

This is called the Jensen–Shannon divergence. It can be rewritten using the KLdivergence as 

**==> picture [302 x 25] intentionally omitted <==**

These are not flat in general. 

We have the _α_ -version of the Burbea–Rao divergence 

**==> picture [302 x 11] intentionally omitted <==**

This is asymmetric divergence. 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

104 

## _**4.6.4 (ρ, τ )-Structure and (F, G, H)-Structure**_ 

Zhang (2004) considered two representations of probabilities _pi_ in _Sn_ by generalizing ± _α_ -representations. Let _ρ_ be a positive increasing function, and call 

**==> picture [190 x 10] intentionally omitted <==**

the _ρ_ -representation of probability _pi_ . In the continuous case, _ρ(x)_ = _ρ_ { _p(x)_ } is the _ρ_ -representation. For a differentiable convex function _f (ρ)_ , we define a positive increasing function 

**==> picture [205 x 11] intentionally omitted <==**

which is another representation, _τ_ -representation, of probability, 

**==> picture [192 x 10] intentionally omitted <==**

This was proposed earlier and is the same as the _(u, v)_ -structure of Sect. 4.4.1 defined in _**R**[n]_ +[.] 

Harsha and Moosath (2014) introduced a non-invariant dual structure called the _(F, G, H )_ -structure to a manifold of probability distributions. However, it is proved to be equivalent to the _(ρ, τ )_ -structure, Zhang (2015). Let _G(u)_ be a smooth positive function. The _G_ -metric is defined by 

**==> picture [273 x 24] intentionally omitted <==**

which reduces to the invariant Fisher metric when _G(u)_ = 1. Let _F_ and _H_ be two differentiable monotonically increasing positive functions. We call _F_ { _p(x,_ _**ξ** )_ } and _H_ { _p(x,_ _**ξ** )_ } the _F_ - and _H_ -representations of probability, respectively. 

We define the _(F, G)_ -connection by 

**==> picture [235 x 14] intentionally omitted <==**

where ⟨· _,_ ·⟩ _G_ denotes the inner product by using the _G_ -metric. It is represented in the component form as 

**==> picture [298 x 25] intentionally omitted <==**

Similarly, we define the _(H, G)_ -connection. 

**Theorem 4.20** _The (F, G)-connection and (H, G)-connection are dual with respect to the G-metric when the following relation holds:_ 

**==> picture [210 x 22] intentionally omitted <==**

105 

4.6 Miscellaneous Divergences 

The proof is omitted. 

The _α_ - _(ρ, τ )_ divergence is defined by 

**==> picture [290 x 53] intentionally omitted <==**

This is neither a Bregman divergence nor an invariant divergence in general, but covers a wide range of divergences in _Sn_ . 

## **Remarks** 

We have seen that a dually flat structure is derived from a Bregman divergence. There are many divergences of the Bregman type which lead to different dually flat Riemannian structures. The invariance is a criterion which specifies a reasonable divergence in a manifold of probability distributions. We have searched for the divergence that is invariant and, at the same time, dually flat in the manifold _Sn_ of probability distributions. The KL-divergence is the unique divergence of the Bregman type that is invariant. 

If we consider the extended manifold of _**R**[n]_[the] _[α]_[-divergences][are][derived][as] +[,] a unique class of invariant divergences of the Bregman type. This introduces the _α_ -geometry to the manifold of probability distributions. It is invariant geometry but is not necessarily dually flat except for the case of _α_ = ±1, which gives the KL-divergence. The _α_ -geometry is interesting. We have shown the _α_ -Pythagorean theorem and _α_ -projection theorem in an _α_ -family despite the fact that the manifold is not dually flat. More generally, given a general divergence and a point _P_ in a submanifold _S_ ⊂ _M_ , the set of point _Q_ that minimizes _D_ [ _Q_ : _M_ ] at _P_ ∈ _M_ does not form a geodesic submanifold orthogonal to _M_ at _P_ . That is, the minimizer _P_ is not the geodesic projection of _Q_ to _M_ . However, in the case of an _α_ -family, this is given by the _α_ -geodesic projection for the _α_ -divergence. The _α_ -projection is useful in applications. See, e.g., Matsuyama (2003). 

It is a happy coincidence that the Tsallis _q_ -geometry of the _q_ -entropy is exactly the same as the geometry where _α_ = 2 _q_ −1. Furthermore, the _q_ -geometry introduced the escort probability distributions, which lead us to the conformal flattening of the nonflat _q_ -geometry. This gives a new _q_ -divergence of the Bregman type, from which flat (but non-invariant) geometry is derived. This idea has been generalized to a general deformed exponential family. 

Apart from the framework of invariance, we introduced a general class of decomposable and non-decomposable divergences of the Bregman type in _**R**[n]_ +[.][They][are] the _(u, v)_ - and _(_ _**u** ,_ _**v** )_ -divergence. This is extended to give an invariant dually flat geometry to the manifold of positive-definite matrices. Quantum information geometry deals with a manifold of positive-definite Hermite matrices (which is a complex version of positive-definite real matrices). Therefore, the invariant _(u, v)_ -structure would be useful in studying quantum information geometry, although we cannot explore it in the present monograph. 

106 

4 _α_ -Geometry, Tsallis _q_ -Entropy and Positive-Definite Matrices 

Divergences are used in various applications. The choice of a divergence function depends on the purpose of the application. An invariant divergence gives a Fisher efficient estimator but is not robust. There are robust divergences like the _γ_ -divergence. A decomposable divergence is used in many applications, because they are simple and the coordinate transformation between _**θ**_ and _**η**_ is tractable. 

**Part II Introduction to Dual Differential Geometry** 

**Chapter 5 Elements of Differential Geometry** 

Here is an introduction to Riemannian geometry. The reader does not need to understand the detailed derivations of equations. More important are ideas and concepts of differential geometry. They can be understood “intuitively” without tears. 

## **5.1 Manifold and Tangent Space** 

Let us consider an _n_ -dimensional manifold _M_ having a (local) coordinate system _**ξ**_ = � _ξ_[1] _, . . . , ξ[n]_[�] . It is in general curved. The tangent space _T_ _**ξ**_ at point _**ξ**_ is a vector space spanned by _n_ tangent vectors along the coordinate curves of _ξ[i]_ . We denote them as { _**e**_ 1 _, . . . ,_ _**e** n_ }, which is a basis of the tangent space (Fig. 5.1). Tangent space _T_ _**ξ**_ is regarded as a linearization of _M_ in a neighborhood of _**ξ**_ , since a small line element _d_ _**ξ**_ of _M_ connecting two nearby points _P_ = _**ξ**_ and _P_[′] = _(_ _**ξ**_ + _d_ _**ξ** )_ is approximated by an (infinitesimally small) tangent vector 

**==> picture [205 x 16] intentionally omitted <==**

See Fig. 5.2. 

Mathematicians are not satisfied with this intuitive definition. They ask what the tangent vector along the coordinate curve _ξ[i]_ is. They define a tangent vector in terms of a differential operator on a function _f (_ _**ξ** )_ in that direction. That is, they identify tangent vector _**e** i_ with the well-established partial derivative operator 

**==> picture [197 x 25] intentionally omitted <==**

It operates on a differentiable function _f (_ _**ξ** )_ and gives its derivative in the direction of coordinate curve _ξ[i]_ , that is, the partial derivative. Hence, one may write 

**==> picture [193 x 27] intentionally omitted <==**

© Springer Japan 2016 

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_5 

5 Elements of Differential Geometry 

110 

**Fig. 5.1** Tangent space _Tξ_ and basis vectors _**e** i_ 

**Fig. 5.2** Infinitesimal vector _d_ _**ξ**_ in _Tξ_ 

**==> picture [115 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
ξ [j]<br>e M<br>j T<br>ξ<br>ξ [i]<br>. e i<br>j<br>T<br>M<br>+ d<br>. d<br>i<br>**----- End of picture text -----**<br>


A vector 

**==> picture [199 x 12] intentionally omitted <==**

is the directional derivative operator which operates on _f_ as 

**==> picture [197 x 12] intentionally omitted <==**

When the coordinate system is changed from _**ξ**_ = _ξ[i]_ to _**ζ**_ = _(ζ[κ] )_ , the partial derivatives change as follows: 

**==> picture [215 x 12] intentionally omitted <==**

where 

**==> picture [215 x 25] intentionally omitted <==**

5.1 Manifold and Tangent Space 

111 

Therefore, we have the law of transformation for the tangent vectors, 

**==> picture [214 x 12] intentionally omitted <==**

**==> picture [214 x 13] intentionally omitted <==**

Foramanifoldofprobabilitydistributions,wehaveanotherexpressionofatangent vector. We identify _**e** i_ with the score function 

**==> picture [205 x 10] intentionally omitted <==**

which is a random variable because it is a function of _x_ . Then, the tangent space _T_ _**ξ**_ is a linear space spanned by _n_ random variables _∂i_ log _p(x,_ _**ξ** ), i_ = 1 _, . . . , n_ . 

A tangent vector is a geometrical quantity, but it has various representations such as a differentiation operator and a random variable. 

## **5.2 Riemannian Metric** 

When an inner product is defined in the tangent space _T_ _**ξ**_ , we have a matrix **G** = � _gij_ � consisting of the inner products of basis vectors 

**==> picture [199 x 11] intentionally omitted <==**

It is a positive-definite matrix depending on _**ξ**_ . It is called the metric tensor and its components change to 

**==> picture [194 x 14] intentionally omitted <==**

by a coordinate transformation. (See Sect. 5.4 for the definition of a tensor.) A man- 

For the manifold of probability distributions, we define an inner product by using the stochastic expression 

**==> picture [248 x 13] intentionally omitted <==**

This is the Fisher information matrix which is invariant. 

The inner product of two vectors _A_ = _A[i]_ _**e** i_ and _B_ = _B[j]_ _**e** j_ is given by 

**==> picture [226 x 12] intentionally omitted <==**

A Riemannian manifold is Euclidean when there exists a coordinate system in which the metric tensor becomes 

**==> picture [191 x 11] intentionally omitted <==**

5 Elements of Differential Geometry 

112 

A Riemannian manifold is curved from the metric point of view when it does not have a coordinate system satisfying (5.15). We will see later that a manifold is (locally) flat when and only when the Riemann–Christoffel curvature tensor vanishes. We need 

## **5.3** 

Tangent space _T_ _**ξ**_ is a local approximation of _M_ at _**ξ**_ . However, a collection of _T_ _**ξ**_ ’s at all _**ξ**_ does not recover the entire figure of _M_ without specifying how _T_ _**ξ**_ and _T_ _**ξ**_[′] _(_ _**ξ**_ ̸= _**ξ**_[′] _)_ are related. It is the role of an affine connection to establish a one-to-one mapping between _T_ _**ξ**_ and _T_ _**ξ**_[′] , in particular when _**ξ**_ and _**ξ**_[′] are infinitesimally close. The entire figure of _M_ will be recovered from the aggregate of _T_ _**ξ**_ ’s by using an affine connection. 

Let us consider two nearby tangent spaces _T_ _**ξ**_ and _T_ _**ξ**_ + _d_ _**ξ**_ . Let 

**==> picture [221 x 12] intentionally omitted <==**

**==> picture [221 x 12] intentionally omitted <==**

be two tangent vectors belonging to _T_ _**ξ**_ and _T_ _**ξ**_ + _d_ _**ξ**_ , respectively. How different are they? We cannot compare them directly, because they belong to different tangent spaces. The basis vectors _**e** i_ = _**e** i(_ _**ξ** )_ ∈ _T_ _**ξ**_ and ˜ _**e** i_ = _**e** i(_ _**ξ**_ + _d_ _**ξ** )_ ∈ _T_ _**ξ**_ + _d_ _**ξ**_ are different, so even when the components of _X[i]_ and _X_[˜] _[i]_ are the same, we cannot say they are equal. 

A manifold is a continuum, so _T_ _**ξ**_ and _T_ _**ξ**_ + _d_ _**ξ**_ would be very similar, almost the same intuitively speaking, because the two tangent spaces become identical as _d_ _**ξ**_ tends to 0. We define a one-to-one affine correspondence between two nearby tangent spaces such that it becomes identical as _d_ _**ξ**_ tends to 0. As an example, consider a curved surface embedded in a three-dimensional Euclidean space. The tangent spaces at _**ξ**_ and at _**ξ**_ + _d_ _**ξ**_ are slightly different in the three-dimensional space. We shift _T_ _**ξ**_ + _d_ _**ξ**_ in parallel such that the origins of _T_ _**ξ**_ and _T_ _**ξ**_ + _d_ _**ξ**_ coincide in the three-dimensional space. However, the directions of _**e** i_ and _**e**_ ˜ _i_ are slightly different when the surface is curved. We project the shifted _**e**_ ˜ _i_ to _T_ _**ξ**_ (Fig. 5.3) and let it be _**e**_[′] _i_[∈] _[T]_ _**[ξ]**_[. The projected] _**e**_[′] _i_[is the counterpart of] _**[e]**_[˜] _[i]_[∈] _[T]_ _**[ξ]**_[+] _[d]_ _**[ξ]**_[in] _[ T]_ _**[ξ]**_[, so a correspondence between] _[ T]_ _**[ξ]**_[and] _[ T]_ _**[ξ]**_[+] _[d]_ _**[ξ]**_ is established by this projection. This is an example of affine connection. 

We begin with technical expressions of an affine connection. Let us map the basis vector _**e**_ ˜ _i_ of _T_ _**ξ**_ + _d_ _**ξ**_ to _T_ _**ξ**_ , by which an affine correspondence is established. It is the projection in the ambient Euclidean space in the previous example, but we consider a more general situation. The map _**e**_[′] _i_[∈] _[T]_ _**[ξ]**_[of] _**[e]**_[˜] _[i]_[∈] _[T]_ _**[ξ]**_[+] _[d]_ _**[ξ]**_[is][close][to] _**[e]**[i][(]_ _**[ξ]**[)]_[,][so][it][is] represented as 

**==> picture [194 x 11] intentionally omitted <==**

5.3 

113 

**Fig. 5.3** _P_ . The shiftedShift _**e**_ ˜ _**e**_ ˜ _ii_ does not∈ _T_ _**ξ**_ + _d_ _**ξ**_ to belong to _Tp_ . Project it to _Tp_ , obtaining _**e**_[′] _i_[∈] _[T][p]_[which is] slightly different from _**e** i_ ∈ _Tp_ 

**==> picture [75 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
~<br>[e] i .<br>shifted [e] [~] i<br>TP<br>vo,<br>[e] i<br>. [e] i<br>TP<br>**----- End of picture text -----**<br>


The difference _d_ _**e** i_ is a vector of _T_ _**ξ**_ written in the component form as 

**==> picture [197 x 13] intentionally omitted <==**

The components _de[j] i_[become 0 as] _[ d]_ _**[ξ]**_[→][0. So they are linear in] _[ d]_ _**[ξ]**_[ and we put] 

**==> picture [199 x 13] intentionally omitted <==**

as the first-order approximation, where the coefficient _Γki[j]_[is a quantity having three] indices. 

A linear correspondence between _T_ _**ξ**_ and _T_ _**ξ**_ + _d_ _**ξ**_ is established by giving a quantity _Γ_ = _Γki[j]_ having three indices. They are called the coefficients of an affine connection which is to be established. The coefficients are given by the inner products of _d_ _**e** i_ and _**e** m_ as 

**==> picture [234 x 13] intentionally omitted <==**

where 

**==> picture [194 x 14] intentionally omitted <==**

is the covariant expression (lower indices expression) of _Γ_ . 

There still remains the problem of determining _Γkji_ . The traditional way is to use the Riemannian metric _gij_ . It is the Levi–Civita connection (Riemannian connection) introduced in Sect. 5.9. Another way is to use a divergence _D_ _**ξ**_ : _**ξ**_[′] defined in _M_ . This leads us to dually coupled affine connections, which we will see in the next chapter. 

5 Elements of Differential Geometry 

114 

## **5.4 Tensors** 

A tensor is a quantity having a number of components such as _A_ = � _A[i]_[�] , _G_ = � _gij_ � and _T_ = � _Tijk_ �. A vector is a tensor having only one index. More precisely, a tensor is a quantity associated with tangent space _T_ _**ξ**_ spanned by _n_ tangent vectors { _**e** i_ }. A vector _A_ is represented in this basis as 

**==> picture [185 x 12] intentionally omitted <==**

in the component form, where the Einstein summation convention is working. Let � _**e**[i]_[�] be the dual basis, which is given by 

**==> picture [210 x 13] intentionally omitted <==**

by using the metric tensor **G** = � _gij_ � and its inverse **G**[−][1] = � _g[ij]_[�] . Note that the dual basis was denoted previously as _**e**_[∗] _[i]_ , but we hereafter omit ∗, because the upper index _i_ of _**e**[i]_ shows that it is a dual basis vector. Vector _A_ is represented in the dual basis as 

**==> picture [185 x 11] intentionally omitted <==**

so that we have 

**==> picture [188 x 13] intentionally omitted <==**

A tensor _K_ = � _Kij[klm]_[�] , for example, is a quantity represented, as 

**==> picture [208 x 13] intentionally omitted <==**

in the linear form of the product _**e**[i]_ _**e**[j]_ _**e** k_ _**e** l_ _**e** m_ of basis vectors. The product is formal and is just a concatenation of basis vectors. When an index is in the upper position, as in _A[i]_ , it is said to be contravariant, and when it is in the lower position, as in _Ai_ , it is said to be covariant. A tensor may have contravariant and covariant components at the same time, as in _Kij[klm]_ . 

When another coordinate system _**ζ**_ = _(ζ[κ] )_ is adopted, the basis vectors change by the coordinate transformation as in (5.8). Therefore, the component of a vector changes, as in 

**==> picture [188 x 12] intentionally omitted <==**

for a contravariant (upper index) vector and 

**==> picture [188 x 12] intentionally omitted <==**

for a covariant vector. Similarly, for a tensor like _Kij[klm]_ , the components change as in 

**==> picture [224 x 14] intentionally omitted <==**

5.4 Tensors 

115 

For a scalar function _f (_ _**ξ** )_ , its gradient 

**==> picture [228 x 24] intentionally omitted <==**

is a covariant vector, because of 

**==> picture [220 x 24] intentionally omitted <==**

The Fisher information matrix (5.13) is a tensor. We define a quantity 

**==> picture [241 x 13] intentionally omitted <==**

It is a covariant tensor having three indices and is symmetric. We call it a (statistical) cubic tensor for short. Two tensors _G_ and _T_ will play a fundamental role in the manifold of probability distributions. 

Not all indexed quantities are tensors. For example, the second derivative of a scalar function _f_ 

**==> picture [194 x 11] intentionally omitted <==**

gives a quantity having two indices, but it is not a tensor. By changing the coordinate system from _**ξ**_ to _**ζ**_ , we have 

**==> picture [269 x 19] intentionally omitted <==**

This shows that it is not a tensor. (It is a tensor at the critical point where _∂jf_ = 0 holds.) 

It should be noted that _Γ_ is not a tensor. By changing the coordinate system from _**ξ**_ to _**ζ**_ , _d_ _**e** i_ changes as in 

**==> picture [245 x 14] intentionally omitted <==**

in the new coordinate system. By using this relation, after some calculations, we have 

**==> picture [237 x 19] intentionally omitted <==**

So it is not a tensor. Note that, even if 

**==> picture [192 x 11] intentionally omitted <==**

holds in one coordinate system, it does not mean that 

**==> picture [190 x 11] intentionally omitted <==**

5 Elements of Differential Geometry 

116 

in another coordinate system. Although it is not a tensor, it has its own meaning, representing the nature of the coordinate system. In a Euclidean space, 

**==> picture [183 x 11] intentionally omitted <==**

in an orthonormal coordinate system _**ξ**_ , but if we use the polar coordinate system _**ζ**_ 

**==> picture [188 x 11] intentionally omitted <==**

because the tangent vector _**e** r_ in the radial direction changes depending on the position in the polar coordinate system. 

When an equation is written in a tensor form such as 

**==> picture [207 x 13] intentionally omitted <==**

depending on physical quantities _**u** ,_ _**v** . . ._ , it has the same form in other coordinate systems 

**==> picture [210 x 10] intentionally omitted <==**

In this sense, a tensorial equation is invariant. A. Einstein obtained the equation of gravity in terms of tensors, because he believed that the law of nature should have the same form whichever coordinate system we use, and hence it should be written in a tensorial form. 

## **5.5 Covariant Derivative** 

A vector field _X_ is a vector-valued function on _M_ , the value of which at _**ξ**_ is given by a vector 

**==> picture [217 x 13] intentionally omitted <==**

When a vector field is given, it is possible to evaluate the intrinsic change of the vector as position _**ξ**_ changes, by using the affine connection. 

In order to see the intrinsic change between _X(_ _**ξ** )_ and _X(_ _**ξ**_ + _d_ _**ξ** )_ , since they belong to different tangent spaces, we need to map _X(_ _**ξ**_ + _d_ _**ξ** )_ ∈ _T_ _**ξ**_ + _d_ _**ξ**_ to _T_ _**ξ**_ for comparison. ˜ Since the basis vector _**e** i_ = _**e** i(_ _**ξ**_ + _d_ _**ξ** )_ is mapped to _T_ _**ξ**_ by 

**==> picture [212 x 14] intentionally omitted <==**

vector _X(_ _**ξ**_ + _d_ _**ξ** )_ is mapped to _T_ _**ξ**_ as 

**==> picture [283 x 15] intentionally omitted <==**

5.5 Covariant Derivative 

117 

where the Taylor expansion of _X[k] (_ _**ξ**_ + _d_ _**ξ** )_ is used. Hence, their difference is evaluated as 

**==> picture [236 x 14] intentionally omitted <==**

This shows the intrinsic change of _X(_ _**ξ** )_ as _**ξ**_ changes by _d_ _**ξ**_ . The rate of intrinsic change along the coordinate curve _ξ[i]_ is denoted as 

**==> picture [213 x 13] intentionally omitted <==**

This is called the covariant derivative of _X(_ _**ξ** )_ and ∇ _iX[k]_ is a tensor. 

Let _Y (_ _**ξ** )_ be another vector field. Then, the directional covariant derivative of _X_ along _Y_ is denoted as 

**==> picture [248 x 13] intentionally omitted <==**

This is the covariant derivative of _X_ along _Y_ . It is again a vector field. We can define the covariant derivative of a tensor, e.g., 

**==> picture [195 x 14] intentionally omitted <==**

in a similar way, since it is spanned by multilinear vector products of the basis vectors _**e** i,_ _**e** j,_ _**e**[k]_ . 

For a scalar function _f (_ _**ξ** )_ , its change is measured by ordinary differentiation. Hence, vector field _Y (_ _**ξ** )_ gives its directional derivative 

**==> picture [191 x 12] intentionally omitted <==**

Note that, for a vector field _X_ , the partial derivatives of its components _∂iX[j] (_ _**ξ** )_ are not a tensor. We should use the covariant derivative for evaluating its intrinsic change. 

## **5.6 Geodesic** 

A curve _**ξ** (t)_ is called a geodesic when its direction does not change. So it is a generalization of the straight line. Here, a change in direction is measured by the covariant derivative derived from an affine connection. Note that this does not necessarily mean that it is a curve of minimal distance connecting two points, although this is the literal definition of a geodesic. The minimality and straightness can be different in a general manifold. It is possible to define an affine connection by using the metric such that a straight line (geodesic) has the minimality of distance, as is given in Theorem 5.2. But a divergence function gives a more general affine connection. 

The tangent vector of curve _**ξ** (t)_ at _t_ is given by 

**==> picture [201 x 12] intentionally omitted <==**

**==> picture [333 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
118 5 Elements of Differential Geometry<br>Fig. 5.4 Geodesic: ξ [˙] (t  +  dt)<br>corresponds to ξ [˙] (t) M<br>.<br>ξ.( t ) ξ( t + dt )<br>. t<br>. ξ( t + dt )<br>ξ( t )<br>;<br>**----- End of picture text -----**<br>


where _**e** i(t)_ = _**e** i_ { _**ξ** (t)_ } and · denotes the derivative _d/dt_ . When _**ξ** (t)_ is a geodesic, the tangent vector _**ξ**_[˙] _(t_ + _dt)_ ∈ _T_ _**ξ** (t_ + _dt)_ corresponds to _**ξ**_[˙] _(t)_ ∈ _T_ _**ξ** (t)_ by the affine connection. See Fig. 5.4. Since the change of the tangent direction of a curve is measured by the covariant derivative of _**ξ**_[˙] along itself, the equation of the geodesic is 

**==> picture [186 x 14] intentionally omitted <==**

This is given in the component form as 

**==> picture [218 x 15] intentionally omitted <==**

If we consider the equation 

**==> picture [194 x 15] intentionally omitted <==**

_**ξ** (t)_ does not change the direction _**ξ**_[˙] _(t)_ of the curve, too, but its magnitude may change. However, by choosing the parameter _t_ adequately, it is possible to reduce (5.55) to (5.54). Hence we consider only the case of (5.54). 

## **5.7 Parallel Transport of Vector** 

We can transport a vector _A_ ∈ _T_ _**ξ**_ + _d_ _**ξ**_ at _**ξ**_ + _d_ _**ξ**_ to _T_ _**ξ**_ at _**ξ**_ without changing it “intrinsically”. The affine connection determines this parallel transport. For two distant points _**ξ**_ and _**ξ**_[′] , we continue the process of parallel transport of a vector along a curve _**ξ** (t)_ connecting _**ξ**_ and _**ξ**_[′] . 

**==> picture [195 x 12] intentionally omitted <==**

along curve _**ξ** (t)_ connecting _P_ and _Q_ (see Fig. 5.5). When its covariant derivative along the curve vanishes, 

**==> picture [333 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
5.7 Parallel Transport of Vector 119<br>Fig. 5.5 Parallel transport of<br>A( 0 )  at  ξ 0 to  A( 1 )  at  ξ 1<br>along curve  ξ(t) M<br>A( t ) A(1)<br>A(0)<br>t<br>t<br>Q : 1<br>P : 0<br>:<br>∇ ξ ˙ A(t)  = 0 , (5.57)<br>A(t)  is intrinsically the same at any  ξ (t) . This is written in the component form as<br>A ˙ [i] (t)  +  Γjk [i] [(][t][)][A][k][(][t][)] [ ˙] [ξ][j][(][t][)] [ =][ 0] [.] (5.58)<br>**----- End of picture text -----**<br>


When _A(t)_ satisfies (5.57) or (5.58), we say that _A(_ 0 _)_ at _T_ _**ξ** (_ 0 _)_ is transported parallelly to _A(_ 1 _)_ at _T_ _**ξ** (_ 1 _)_ . The parallel transport depends in general on the path along which it is transported. So we denote the parallel transport of a vector _A_ from _**ξ**_ 0 = _**ξ** (_ 0 _)_ to _**ξ**_ 1 = _**ξ** (_ 1 _)_ along curve _c_ = _**ξ** (t)_ by 

**==> picture [204 x 28] intentionally omitted <==**

## **5.8 Riemann–Christoffel Curvature** 

A manifold is curved in general. When a vector is transported in parallel from one point to another, the resultant vector depends on the path along which it is transported. This never happens in a flat manifold. In order to show how curved a manifold is, we define the Riemann–Christoffel (RC) curvature tensor determined from the affine connection. One may skip this section, since we do not use RC curvature in applications in this monograph. When the RC curvature tensor vanishes, that is, when it is identically equal to 0, the manifold is (locally) flat. When it is flat, there exists an affine coordinate system such that each coordinate curve is a geodesic and its tangent vector coincides at any point by parallel transport. 

5 Elements of Differential Geometry 

120 

## _**5.8.1 Round-the-World Transport of Vector**_ 

Let us consider two curves _c_ 1 : _**ξ**_ 1 _(t)_ and _c_ 2 : _**ξ**_ 2 _(t)_ , 0 ≤ _t_ ≤ 1, both connecting the same two points _**ξ**_ 0 = _**ξ**_ 0 _(_ 0 _)_ and _**ξ**_ 1 = _**ξ**_ 1 _(_ 1 _)_ . When a vector _A_ at _**ξ**_ 0 is transported to _**ξ**_ 1 in parallel along curve _c_ 1, it becomes _c_ 1 _[A]_[. If we transport] _c_ 1 _[A]_[ back to] _**[ ξ]**_ 0 along the same curve _c_ 1 in reverse, it is _A_ . Now we transport _A_ in parallel along the two curves _c_ 1 and _c_ 2. The resultant vectors, _c_ 1 _[A]_[ and] _c_ 2 _[A]_[, are different in general] (Fig. 5.6). This implies that when we transport a vector from _**ξ**_ 0 to _**ξ**_ 1 along path _c_ 1 and then transport it back to the original point _**ξ**_ 0 along the other path _c_ 2 in reverse, the resultant vector is different from _A_ . So a vector changes when it is transported along a loop (consisting of path _c_ 1 and reverse path of _c_ 2). In other words, a vector is changed by a round-the-world trip. 

The change may be used to measure how curved _M_ is. To evaluate the change, we consider an infinitesimally small quadrangle connecting four points _P, Q, R_ and _S_ , where their coordinates are 

**==> picture [279 x 10] intentionally omitted <==**

(See Fig. 5.7.) We transport _A_ in parallel first from _P_ to _Q_ by _d_ 1 _**ξ**_ . Then, _A_ becomes _A_ 1 = _A_ + _d_ 1 _A_ , the components of which are 

**==> picture [207 x 14] intentionally omitted <==**

**==> picture [333 x 246] intentionally omitted <==**

**----- Start of picture text -----**<br>
We further transport  A 1 from  Q  to  R  along the path [−→] QR  =  d 2 ξ . Then, the transported<br>vector at R is A 12 =  A  +  d 1 A  +  δ 12 A , where the components of additional change<br>δ 12 A  are<br>δ 12 A [i] = − Γjk [i] [(] [ξ] [ +] [ d] [1] [ξ] [)] [A][k] [+] [ d] [1] [A][k] [d] [2] [ξ][j][.] (5.62)<br>Fig. 5.6 Parallel transport of<br>A  via  c 1 is different from that<br>via  c 2<br>Π c 2 A<br>c 2<br>A .<br>Π c 1 A<br>.<br>c 1<br>@<br>**----- End of picture text -----**<br>


**Fig. 5.6** Parallel transport of _A_ via _c_ 1 is different from that via _c_ 2 

5.8 Riemann–Christoffel Curvature 

121 

**Fig. 5.7** Parallel transports of _A_ along _PQR_ and _PSR_ 

**==> picture [171 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>A + d 1 A +δ12 A<br>S : + d 2<br>d 1 R : + d 1 + d 2<br>d 2 d 2<br>A A + d 1 A<br>d 1<br>P : Q : + d 1<br>**----- End of picture text -----**<br>


Since _Γ_ is evaluated at _**ξ**_ + _d_ 1 _**ξ**_ , the Taylor expansion gives 

**==> picture [299 x 14] intentionally omitted <==**

Now, we transport _A_ along the different route, first along the path[−→] _PS_ = _d_ 2 _**ξ**_ to _S_ and then to _R_ along[−→] _SR_ = _d_ 1 _**ξ**_ . The resultant change is given by exchanging _d_ 1 _**ξ**_ and _d_ 2 _**ξ**_ in (5.63). The result is 

**==> picture [299 x 14] intentionally omitted <==**

How different are the resultant vectors? By subtracting _A_ 21 from _A_ 12 where (5.63) and (5.64) are used, the result is written as 

where we put 

**==> picture [267 x 48] intentionally omitted <==**

We can prove that _Rijk[l]_ is a tensor. It is called the Riemann–Christoffel (RC) curvature tensor. This shows how a vector changes by the round-the-world trip along an infinitesimal loop. We denote the infinitesimal loop encircling _P, Q, R, S_ and _P_ by a tensor 

**==> picture [228 x 12] intentionally omitted <==**

5 Elements of Differential Geometry 

122 

**Fig. 5.8** Small surface element, loop and membrane 

**==> picture [131 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
df ij<br>d 2<br>d 1<br>( t )<br>**----- End of picture text -----**<br>


which is antisymmetric with respect to the two indices _i_ and _j_ , 

**==> picture [193 x 12] intentionally omitted <==**

This is a small surface element, representing a surface spanned by _d_ 1 _**ξ**_ and _d_ 2 _**ξ**_ (Fig. 5.8). Equation(5.65) is written as 

**==> picture [202 x 13] intentionally omitted <==**

When vector _A_ is transported in parallel along a general loop _**ξ** (t),_ 0 ≤ _t_ ≤ 1, _**ξ** (_ 0 _)_ = _**ξ** (_ 1 _)_ , we span a membrane encircled by the loop (see Fig. 5.8). Then, the changed _ΔA_ due to the round-the-world parallel transportation is given by the surface integral 

**==> picture [209 x 13] intentionally omitted <==**

This does not depend on the way of spanning the membrane, as is clear from the Stokes’ Theorem. 

## _**5.8.2 Covariant Derivative and RC Curvature**_ 

The partial derivative is always commutative, 

**==> picture [191 x 11] intentionally omitted <==**

However, this does not in general hold for the covariant derivative, 

**==> picture [203 x 11] intentionally omitted <==**

5.8 Riemann–Christoffel Curvature 

123 

The covariant derivative of _**e** j_ in the direction of basis vector _**e** i_ is 

**==> picture [196 x 13] intentionally omitted <==**

By using this, we have 

**==> picture [237 x 14] intentionally omitted <==**

We omit the proof, but we see that the RC curvature shows the degree of noncommutativity of the covariant derivative. 

In general, we can define the RC curvature by 

**==> picture [262 x 10] intentionally omitted <==**

where 

**==> picture [254 x 13] intentionally omitted <==**

This is a sophisticated definition of the RC curvature tensor which one sees in modern textbooks on differential geometry. However, it is difficult to understand the meaning of the RC curvature from it. 

## _**5.8.3 Flat Manifold**_ 

When the RC curvature vanishes, _M_ is said to be flat. The parallel transport of a vector does not depend on the path in this case. Let us consider a set of basis vectors { _**e** i_ } in the tangent space at a point. We construct _n_ geodesics passing through the point in the directions of _**e** i_ . We then have _n_ coordinate curves _θ[i]_ , of which tangent vectors _**e** i_ are the same everywhere. This generates a flat coordinate system _**θ**_ = � _θ[i]_[�] . Indeed, we transport the tangent vectors _**e** i_ to any point and compose the geodesics the directions of which are _**e** i_ . Vectors _**e** i_ are parallel at any point and we have a net of coordinate curves _**θ**_ . 

Since the tangent vectors of a coordinate curve _θ[i]_ are all in parallel, we have 

**==> picture [187 x 11] intentionally omitted <==**

Therefore, from (5.73) we have 

**==> picture [185 x 11] intentionally omitted <==**

Hence, when _M_ is flat, we have an affine coordinate system consisting of geodesics in which (5.78) holds at any _**ξ**_ . 

5 Elements of Differential Geometry 

124 

## **5.9 Levi–Civita (Riemannian) Connection** 

We have so far treated the metric and affine connection separately. However, it is possible to define an affine connection such that it is essentially related to the metric, giving a unified picture. This is Riemannian geometry. It requires that the magnitude of a vector does not change by the parallel transport. This establishes a relation between the metric and the affine connection (see Fig. 5.9). 

It is easy to see the equivalence of the following two propositions of parallel transportation: (1) The magnitude of a vector does not change by parallel transportation, 

**==> picture [244 x 21] intentionally omitted <==**

(2) The inner product of two vectors does not change by parallel transportation, 

**==> picture [250 x 20] intentionally omitted <==**

We consider an infinitesimal parallel transport of two basis vectors along the coordinate curve _ξ[i]_ . Then, when the length of a vector does not change, we have 

_gij(_ _**ξ**_ + _d_ _**ξ** )_ = ⟨ _**e** i(_ _**ξ**_ + _d_ _**ξ** ),_ _**e** j(_ _**ξ**_ + _d_ _**ξ** )_ ⟩ _**ξ**_ + _d_ _**ξ**_ = ⟨ _**e** i(_ _**ξ** )_ + _d_ _**e** i,_ _**e** j(_ _**ξ** )_ + _d_ _**e** j_ ⟩ _**ξ** ._ (5.81) 

Because _gij(_ _**ξ**_ + _d_ _**ξ** )_ = _gij(_ _**ξ** )_ + _∂kgijdξ[k]_ , this condition is written as 

**==> picture [204 x 11] intentionally omitted <==**

More generally, this condition is equivalent to 

**==> picture [235 x 9] intentionally omitted <==**

**==> picture [311 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 5.9 The magnitude of  A<br>is equal to the magnitude of<br>c [A] Πc A<br>. Q<br>c<br>.<br>P<br>aa<br>**----- End of picture text -----**<br>


5.9 Levi–Civita (Riemannian) Connection 

125 

for three vector fields _X, Y_ and _Z_ . When an affine connection satisfies this condition, it is said to be metric. The metric affine connection is uniquely determined from metric _gij_ , provided the symmetric condition 

**==> picture [188 x 11] intentionally omitted <==**

holds. 

**Theorem 5.1** _Whentheparalleltransportdoesnotchangethemagnitudeofavector, there is a unique symmetric affine connection given by_ 

**==> picture [238 x 22] intentionally omitted <==**

It is an interesting exercise to prove this from (5.82). It is called the Levi–Civita connection or Riemannian connection. Many conventional textbooks on differential geometry study only the Levi–Civita connection. By using the Levi–Civita connection, we have the following convenient property. 

**Theorem 5.2** _A curve that connects two points by a minimal distance is a geodesic under the Levi–Civita connection, where the length of a curve c_ = _**ξ** (t) connecting_ _**ξ** (_ 0 _) and_ _**ξ** (_ 1 _) is given by_ 

**==> picture [220 x 36] intentionally omitted <==**

It is possible to obtain (5.54) and (5.85) by the variational method, _δs_ = 0, of minimizing (5.86) with respect to curve _**ξ** (t)_ . This is also a good exercise. See Fig. 5.10. 

**Fig. 5.10** A Riemannian geodesic _ξ(t)_ is a curve which does not change the direction _ξ_[˙] _(t)_ , and also the distance _s_ is minimized along it 

**==> picture [113 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
. Q<br>.<br>P<br>**----- End of picture text -----**<br>


5 Elements of Differential Geometry 

126 

## **5.10 Submanifold and Embedding Curvature** 

We consider a submanifold embedded in a larger manifold. It has embedding curvaturewhenitiscurvedintheambientmanifold.ThisisdifferentfromtheRCcurvature. It is useful to embed a manifold in a simple (e.g. flat) higher-dimensional ambient manifold and study its properties in the ambient manifold. Geometrical quantities are transferred from a simple ambient manifold to the submanifold by embedding. 

## _**5.10.1 Submanifold**_ 

Let _S_ be a submanifold embedded in _M_ (Fig. 5.11). Let _**ξ**_ = () _ξ[i]_ be a coordinate system of _M, i_ = 1 _, . . . , n_ and _**u**_ = _(u[a] )_ be a coordinate system of _S, a_ = 1 _, . . . , m_ , where we assume _n > m_ . Since a point _**u**_ in _S_ is also a point in the ambient _M_ , its coordinates in _M_ are specified by _**u**_ as 

**==> picture [187 x 11] intentionally omitted <==**

We consider the case that _**ξ** (_ _**u** )_ is differentiable with respect to _**u**_ . The tangent vector _**e** a_ along the coordinate curve _u[a]_ of _S_ is 

**==> picture [183 x 10] intentionally omitted <==**

and the tangent space _T_ _**u**[S]_[of] _[S]_[is][spanned][by][them][(Fig.][5.12][).][However,][they][are] regarded as tangent vectors at point _**ξ** (_ _**u** )_ of _M_ by embedding. They are represented in _M_ as 

**Fig. 5.11** Submanifold _S_ embedded in _M_ 

**==> picture [114 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>= ( u )<br>u<br>S<br>**----- End of picture text -----**<br>


5.10 Submanifold and Embedding Curvature 

127 

**Fig. 5.12** Tangent vectors _**e** a_ of submanifold 

**==> picture [127 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>= ( u ) u [a]<br>u [b]<br>e b e a T u S<br>u<br>S<br>u<br>**----- End of picture text -----**<br>


**==> picture [229 x 26] intentionally omitted <==**

in terms of the basis vectors _**e** i_ ∈ _T_ _**ξ**_ of _M_ . Defining 

**==> picture [189 x 24] intentionally omitted <==**

we have 

**==> picture [188 x 12] intentionally omitted <==**

A vector _X_ = _X[a]_ _**e** a_ ∈ _T_ _**u**[S]_[is a vector] _[ X]_[=] _[ X][i]_ _**[e]**[i]_[∈] _[T]_ _**[ξ]**_[and] 

**==> picture [190 x 13] intentionally omitted <==**

Submanifold _S_ inherits the geometrical structures of _M_ . The magnitude of a tangent vector _A_ in _T_ _**u**[S]_[is given by its magnitude in] _[ M]_[. Hence, the metric] 

**==> picture [194 x 10] intentionally omitted <==**

in _S_ is given by 

**==> picture [196 x 14] intentionally omitted <==**

## _**5.10.2 Embedding Curvature**_ 

˜ An affine connection is naturally transferred to _S_ from _M_ . Let _**e** a_ = _**e** a(_ _**u**_ + _d_ _**u** )_ ∈ _T_ _**u**[S]_ + _d_ _**u**_[be][a][basis][vector][at] _**[u]**_[ +] _[ d]_ _**[u]**_[of] _[S]_[and][we][map][it][in][parallel][to] _[T]_ _**u**[ S]_[.][We][first] 

5 Elements of Differential Geometry 

128 

transport it in _M_ from _**ξ** (_ _**u** )_ to _**ξ** (_ _**u**_ + _d_ _**u** )_ in parallel. The resultant vector is denoted as _**e**_[′] _a_[=] _**[ e]**[a]_[ +] _[ d]_ _**[e]**[a]_[∈] _[T]_ _**[ξ]**[(]_ _**[u]**[)]_[, where] _[ d]_ _**[e]**[a]_[is given by the covariant derivative of] _**[ e]**[a]_[in the] direction of _**e** b_ = _Bb[i]_ _**[e]**[i]_[in] _[ M]_[,] 

**==> picture [200 x 13] intentionally omitted <==**

We calculate ∇ _**e** a_ _**e** b_ in _M_ , 

**==> picture [262 x 54] intentionally omitted <==**

where we put 

**==> picture [222 x 13] intentionally omitted <==**

Here,thevector _d_ _**e** a_ isnotnecessarilyincludedinthetangentspaceof _S_ (Fig. 5.13). So we decompose it in the tangent direction of _S_ and its orthogonal direction, 

**==> picture [203 x 13] intentionally omitted <==**

where _d_ _**e**_[∥] _a_[∈] _[T]_ _**u**[ S]_[and] _[d]_ _**[e]**_[⊥] _a_[is][orthogonal][to] _[S]_[.][We][define][the][parallel][transport][of] _**[e]**_[˜] _[a]_ within _S_ by the change _d_ _**e**_[∥] _a_[, neglecting the change in the orthogonal direction:] 

**==> picture [197 x 13] intentionally omitted <==**

Rewriting _d_ _**e**_[∥] _a_[in][terms][of][basis][vectors][{] _**[e]**[b]_[}][,][the][induced][affine][connection][of] _[S]_[is] given as 

**==> picture [238 x 14] intentionally omitted <==**

The orthogonal direction of _d_ _**e**_[⊥] _a_[represents][how] _[S]_[is][curved][in] _[M]_[.][To][show][the] orthogonal component, we supplement _T_ _**u**[S]_[with] _[n]_[ −] _[m]_[orthogonal][vectors] _**[e]**[κ][,][ κ]_[ =] _n_ − _m_ + 1 _, . . . , n_ , such that the entire vectors { _**e** a,_ _**e** κ_ } span the tangent space of _M_ . Then, the orthogonal part is given by 

**Fig. 5.13** Decomposition of _d_ _**e**_ ˜ _a_ ∈ _Tξ(u)_ in the orthogonal part _d_ _**e**_[⊥] _a_[and parallel part] _d_ _**e**_[||] _a_[with respect to] _[ T]_ _**u**[S]_ 

**==> picture [204 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
δ e [⊥] a [=] [ H][ab] κ e kdub, (5.101)<br>d e [~] a<br>d e a<br>d e a<br>e a T u S<br>**----- End of picture text -----**<br>


5.10 Submanifold and Embedding Curvature 

129 

where we use the covariant derivative in _M_ 

**==> picture [206 x 11] intentionally omitted <==**

This is the embedding curvature of _S_ , sometimes called the Euler–Schouten curvature tensor. 

TheembeddingcurvatureisdifferentfromtheRCcurvature,whichisderivedfrom the affine connection _Γabc_ . The RC curvature is the intrinsic curvature considering only inside _S_ . As a simple example, let us consider a cylinder _S_ embedded in a threedimensional Euclidean manifold _M_ . It is curved in _M_ , so it has non-zero embedding curvature. But its RC curvature vanishes and Euclidean geometry holds inside _S_ . If we live in _S_ and do not know the outer world of three dimensions, we enjoy Euclidean geometry in _S_ where the RC curvature is 0. But _S_ has non-zero embedding curvature. 

## **Remarks** 

Differential geometry studies properties of a manifold by its local structure. A Riemannian manifold is a typical example, where a manifold is equipped with a metric tensor **G** = � _gij_ � by which the distance of two nearby points is measured. It is locally approximated by a Euclidean space but is curved in general. Modern differential geometry further studies the global topological structure of a manifold. It is interesting to see how the global structure is restricted by the local structure such as the curvature. This is an important perspective. However, we have not mentioned the global properties, because most (though not all) applications use only local structure. 

Since differential geometry has been developed as pure mathematics, mathematicianshaveconstructedarigorous,sophisticatedtheory,excludingintuitivedefinitions of geometrical concepts. However, once such a rigorous theory is established, we may use intuitive understanding for applications. Part II is an attempt to introduce the modern concepts of differential geometry without tears to beginners. 

After non-Euclidean geometry was developed in the 19th century, people came to know that there existed non-Euclidean spaces. B. Riemann, in his professorship lecture, proposed the concept of Riemannian geometry, which is non-Euclidean and curved. He conjectured that the real world might be Riemannian on a cosmological scale or on an atomic scale. His view was proved true in the 20th century in relativity theory and elementary particle theory. 

There are many of applications of differential geometry. Relativity theory is one of them, in which Einstein introduced the concept of a torsion tensor to establish a unified theory (unification of gravity and electromagnetism). Unfortunately, this interesting idea failed. But the torsion tensor survived in mathematics. The torsion tensor is a third-order tensor of which the first two indices are anti-symmetric. This is a new quantity to supplement the Riemannian structure of { _M, G_ }, although we have not mentioned it here. 

A Riemannian manifold with torsion plays a fundamental role in continuum mechanics including dislocations. A dislocation field in a continuum is identified with a torsion field, and a rich theory has been established. See, e.g., Amari [1962, 1968]. Another application is the dynamics of electro-mechanical systems, such as 

5 Elements of Differential Geometry 

130 

motors and generators, by Gabriel Kron. Here, non-holonomic constraints play a role, and are converted to torsion. Recent robotics also uses non-holonomic constraints. Differential geometry plays important roles in various areas. 

Information geometry also uses differential geometry, where the invariance criterion plays a fundamental role in defining the geometrical structure of a manifold of probability distributions. However, the conventional edifice of differential geometry in textbooks is not enough to explore its structure. We need a new concept of duality of affine connections with respect to the Riemannian metric. In the next chapter, we study a Riemannian manifold equipped with dually coupled affine connections. 

## **Chapter 6 Dual Affine Connections and Dually Flat Manifold** 

We have considered one affine connection, namely the Levi–Civita connection, in a Riemannian manifold _M_ . However, we can establish a new edifice of differential geometry, by treating a pair of affine connections which are dually coupled with respect to the Riemannian metric. Such a structure has not been described in conventional textbooks, but is the heart of information geometry. Mathematically speaking, in addition to the Riemannian structure { _M, G_ }, we study the structure { _M, G, T_ }, which has a third-order symmetric tensor _T_ in addition to _G_ . As an important special case, we study a dually flat Riemannian manifold. It may be regarded as a dualistic extension of the Euclidean space. The generalized Pythagorean theorem and projection theorem hold in such a manifold. They are particularly useful in applications. 

## **6.1 Dual Connections** 

The Levi–Civita connection is the only metric affine connection (without torsion) that preservesthemetricbyparalleltransport.However,thereisanotherwayofpreserving the metric by using two affine connections. We consider here two symmetric affine connections _Γ_ and _Γ_[∗] and denote the associated parallel transports as[�] and[�][∗] , respectively. These affine connections are dually coupled when the parallel transports of vectors _A_ and _B_ , one by[�] and the other by[�][∗] , do not change their inner product, 

**==> picture [219 x 19] intentionally omitted <==**

See Fig. 6.1. Such a pair of affine connections are said to be dually coupled with respect to the Riemannian metric, which defines the inner product. A pair of connections collaborate to preserve the inner product by parallel transportation of vectors. 

© Springer Japan 2016 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_6 

131 

6 

132 6 Dual Affine Connections and Dually Flat Manifold 

**==> picture [333 x 235] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 6.1 Conservation of<br>inner product by dual * B<br>parallel transports A<br>.<br>Q<br>B<br>A<br>.<br>P<br>:<br>When the two connections are identical, (6.1) reduces to the metric condition (5.80),6.1) reduces to the metric condition (5.80),) reduces to the metric condition (5.80),5.80),),<br>so that this is an extension of the metric connection.<br>We search for analytical expressions of dual connections. Consider two basis<br>vectors e ˜ i and e ˜  j at point ξ + d ξ . We transport them to ξ , one by using affine<br>connection Γ and the other by dual connection Γ [[∗]] . Then, their parallel transports<br>are, respectively,<br>e i +  d e i = e i +  Γki j e  j dξk, (6.2)<br>e  j +  d [∗] e  j = e  j +  Γkj [∗] i e i dξk, (6.3)<br>**----- End of picture text -----**<br>


When the two connections are identical, (6.1) reduces to the metric condition (5.80),6.1) reduces to the metric condition (5.80),) reduces to the metric condition (5.80),5.80),), so that this is an extension of the metric connection. 

We search for analytical expressions of dual connections. Consider two basis vectors _**e**_ ˜ _i_ and _**e**_ ˜ _j_ at point _**ξ**_ + _d_ _**ξ**_ . We transport them to _**ξ**_ , one by using affine connection _Γ_ and the other by dual connection _Γ_[[∗]] . Then, their parallel transports are, respectively, 

where _d_ and _d_[∗] denote the changes induced by the parallel transformations due to _Γ_ and _Γ_[∗] , respectively. From the conservation of the inner product 

**==> picture [245 x 11] intentionally omitted <==**

we have 

**==> picture [265 x 12] intentionally omitted <==**

where higher-order terms are neglected. 

By the Taylor expansion, we have the componentwise expression 

**==> picture [208 x 13] intentionally omitted <==**

Compare this with the self-dual case (5.82). 

This is rewritten in terms of the covariant derivatives as 

**==> picture [237 x 11] intentionally omitted <==**

where _X, Y_ and _Z_ are three vector fields. This is confirmed by using three vector fields _Z_ = _**e** i , X_ = _**e** j_ and _Y_ = _**e** k_ , as 

**==> picture [243 x 12] intentionally omitted <==**

which is the same as (6.6). 

6.1 Dual Connections 

133 

The average of two dual connections is given by 

**==> picture [214 x 22] intentionally omitted <==**

The related covariant derivative is 

**==> picture [209 x 22] intentionally omitted <==**

From (6.7), we see that ∇[0] satisfies (5.83) and _Γi jk_[0][is][the][Levi–Civita][connection.] 

**==> picture [204 x 12] intentionally omitted <==**

Then, the dual connections are written as 

**==> picture [254 x 22] intentionally omitted <==**

**Theorem 6.1** _When Γ and Γ_[∗] _are dual affine connections, T is a symmetric tensor given by_ 

**==> picture [201 x 25] intentionally omitted <==**

_Proof_ We calculate the covariant derivative of tensor _G_ = � _gi j_ �. It is given by 

**==> picture [242 x 11] intentionally omitted <==**

Since ∇[0] is the metric connection, 

**==> picture [235 x 14] intentionally omitted <==**

Hence, we have 

**==> picture [217 x 21] intentionally omitted <==**

Since _g jk_ is symmetric with respect to _j_ and _k_ , we have 

**==> picture [194 x 11] intentionally omitted <==**

Moreover, _Γi jk_ is a symmetric connection, so _Ti jk_ is symmetric with respect to _i_ and _j_ . Hence _Ti jk_ is symmetric with respect to three indices, _i, j_ , and _k_ . _Ti jk_ is a tensor, because it is the covariant derivative of tensor _g jk_ . (6.14) is also derived similarly. □ 

6 Dual Affine Connections and Dually Flat Manifold 

134 

_Remark_ S. Lauritzen called _Ti jk_ the skewness tensor. However, it is symmetric, and so we hesitate to use the term “skewness”, which often implies anti-symmetry. So we use the term cubic tensor. This is called the Amari–Chentsov tensor by some researchers (e.g., Ay et al. 2013), since Chentsov defined it and Amari has developed its theory. The triplet { _M, G, T_ } is also called the Amari–Chentsov structure. 

Dual affine connections are determined from { _G, T_ } by (6.12), where _gi j_ is a positive-definite symmetric matrix and _Ti jk_ is a cubic tensor. When _Ti jk_ = 0, the two affine connections are identical. Hence, the connection is self-dual and _M_ reduces to the ordinary Riemannian manifold, having the Levi–Civita connection. 

## **6.2 Metric and Cubic Tensor Derived from Divergence** 

When a divergence _D_ � _**ξ**_ : _**ξ**_[′][�] is defined in _M_ , we show that two tensors _gi j[D]_[and] _[ T] i jk[ D]_ are automatically induced from it. We consider a neighborhood of diagonal position _**ξ**_ = _**ξ**_[′] of _D_ . Since _D_ has two arguments, we introduce the following notation of differentiation at the diagonal: 

**==> picture [219 x 51] intentionally omitted <==**

Similarly, for multiple differentiation, we use the notation 

**==> picture [238 x 25] intentionally omitted <==**

etc. 

We define the following quantities by using the above notations: 

**==> picture [197 x 31] intentionally omitted <==**

**==> picture [199 x 14] intentionally omitted <==**

We can prove that _Γ[D]_ and _Γ[D]_[∗] define affine connections, by checking how they are transformed by coordinate transformations. We omit the calculations since they are technical and easy. Their difference 

**==> picture [204 x 14] intentionally omitted <==**

135 

6.2 Metric and Cubic Tensor Derived from Divergence 

is a third-order symmetric tensor. Hence, we have two characteristic tensors _gi j[D]_[and] _Ti jk[D]_[from a divergence] _[D]_[. The following is a key result connecting a divergence and] dual geometry, derived by Eguchi (1983). 

**Theorem 6.2** _The two affine connections Γ[D] and Γ[D]_[∗] _are dual with respect to the Riemannian metric g[D] ._ 

_Proof_ By differentiating 

**==> picture [223 x 25] intentionally omitted <==**

with respect to _**ξ**_ , we have 

**==> picture [252 x 14] intentionally omitted <==**

**==> picture [333 x 11] intentionally omitted <==**

When a Legendre pair of convex functions _ψ(_ _**θ** )_ and _ϕ(_ _**η** )_ are given, where _**θ**_ and _**η**_ are connected by the Legendre transformation, we have a Bregman divergence 

**==> picture [243 x 13] intentionally omitted <==**

where _**η**_[′] is the Legendre dual of _**θ**_[′] . The metric tensor derived from it is 

**==> picture [205 x 11] intentionally omitted <==**

in the _**θ**_ -coordinates and 

**==> picture [206 x 12] intentionally omitted <==**

in the _**η**_ -coordinates. Moreover, by differentiating it, we have from (6.23) and (6.24), 

**==> picture [215 x 12] intentionally omitted <==**

in the two coordinate systems. This implies that the geometry derived from a convex function, or the related Bregman divergence, is dually flat and the affine coordinate systems are _**θ**_ and _**η**_ . The cubic tensor is written as 

**==> picture [251 x 13] intentionally omitted <==**

in the two coordinate systems. This justifies our former definition of the dually flat structure introduced in Part I without differential geometry. 

136 

6 Dual Affine Connections and Dually Flat Manifold 

## **6.3 Invariant Metric and Cubic Tensor** 

An _f_ -divergence is an invariant divergence in the manifold of probability distributions. We calculate the two tensors _G[f]_ and _T[f]_ derived from an _f_ -divergence, which are therefore invariant. 

**Theorem 6.3** _Invariant tensors derived from a standard f -divergence in the manifold of probability distributions are given as_ 

**==> picture [194 x 33] intentionally omitted <==**

_where gi j is the Fisher information matrix and_ 

**==> picture [247 x 27] intentionally omitted <==**

_Proof_ By differentiating an arbitrary _f_ -divergence 

**==> picture [254 x 31] intentionally omitted <==**

with respect to _**ξ**_ and _**ξ**_[′] and putting _**ξ**_[′] = _**ξ**_ , we have (6.33) and (6.34). 

**==> picture [9 x 7] intentionally omitted <==**

_Remark_ The uniqueness of the _f_ -divergence under the invariance criterion is derived from the information monotonicity and decomposability. More strongly, the Chentsov theorem proves that _gi j_ and _αTi jk_ are the unique invariant second-order and third-order symmetric tensors in _Sn_ . 

## **6.4** _**α**_ **-Geometry** 

When _Ti jk_ is a symmetric tensor, so is _αTi jk_ for real _α_ . We call the two affine connections derived from { _G, αT_ }, 

**==> picture [258 x 20] intentionally omitted <==**

the _α_ -connection and − _α_ -connection, respectively. 

**Theorem 6.4** _Γ[α] and Γ_[−] _[α] are dually coupled and the α_ = 0 _connection Γ_[0] _is the Levi–Civita connection, which is self-dual._ 

The proof is easy from (6.12). 

6.4 _α_ -Geometry 

137 

When _T[f]_ is derived from an _f_ -divergence, it is _αT_ for _α_ satisfying (6.36) and, moreover, − _αT_ is derived from the dual of the _f_ -divergence. The derived dual structure is the only invariant geometry in the case of a manifold of probability distributions. We call it the _α_ -geometry. The _α_ -geometry is derived from the _α_ -divergence defined in (3.39). It is not dually flat in general. When _α_ = ±1, it reduces to the KL-divergence, giving a dually flat structure. 

For any convex function _ψ_ , we can construct a related _α_ -divergence. In this case, the _α_ -geometry is induced from the _α_ -divergence defined by 

**==> picture [326 x 33] intentionally omitted <==**

This is a Jensen-type divergence introduced by Zhang (2004). 

## **6.5 Dually Flat Manifold** 

We have the following theorem concerning dual curvatures. 

**Theorem 6.5** _When the RC curvature R vanishes with respect to one affine connection, the RC curvature R_[∗] _with respect to the dual connection vanishes and vice versa._ 

_Proof_ When the RC curvature vanishes, _R_ = 0, the round-the-world parallel transportation does not change any _A_ : 

**==> picture [189 x 15] intentionally omitted <==**

For vector transportations, we always have 

**==> picture [219 x 19] intentionally omitted <==**

Hence, when (6.40) holds, we have 

**==> picture [210 x 19] intentionally omitted <==**

for any _A_ and _B_ . This implies 

**==> picture [190 x 17] intentionally omitted <==**

showing that the dual RC curvature vanishes, _R_[∗] = 0. □ 

A manifold is always dually flat when it is flat with respect to one connection. When _M_ is dually flat, there exists an affine coordinate system _**θ**_ for which 

6 Dual Affine Connections and Dually Flat Manifold 

138 

**==> picture [192 x 11] intentionally omitted <==**

Each coordinate curve _θ[i]_ is a geodesic. The basis vectors { _**e** i_ } are transported in parallel to any position, not depending on a path of transportation. 

Similarly, there exists a dual affine coordinate system _**η**_ for which 

**==> picture [194 x 12] intentionally omitted <==**

holds. Each coordinate curve _ηi_ is a dual geodesic. Let its direction be _**e**[i]_ . Here, we use a lower index to denote the components of _**η**_ = _(ηi )_ and the related basis vectors are denoted by upper-indexed quantities such as _**e**[i]_ . This notation fits our index notation of raising and lowering indices by using the metric tensors _gi j_ and its inverse _g[i j]_ . The Jacobians of the coordinate transformations satisfy 

**==> picture [217 x 26] intentionally omitted <==**

Therefore, two bases { _**e** i_ } and � _**e**[i]_[�] satisfy 

**==> picture [216 x 13] intentionally omitted <==**

**Theorem 6.6** _In a dually flat manifold, there exists affine coordinate system_ _**θ** and dual affine coordinate system_ _**η** such that their tangent vectors are reciprocally orthogonal,_ 

**==> picture [216 x 13] intentionally omitted <==**

_Proof_ From (6.47), we have 

**==> picture [240 x 13] intentionally omitted <==**

We also have 

**==> picture [229 x 19] intentionally omitted <==**

at any point. Note that _gi j_ and _g[ji]_ depend on the position, but (6.47) holds at any point. □ 

## **6.6 Canonical Divergence in Dually Flat Manifold** 

We have shown that a dual structure is constructed from a divergence function. In particular, a dually flat structure is induced from a Bregman divergence. However, many divergences give the same dual structure. This is because the differential geometry of the metric and connections is defined from the derivatives of divergence _D_ � _**ξ**_ : _**ξ**_[′][�] 

6.6 Canonical Divergence in Dually Flat Manifold 

139 

at _**ξ**_ = _**ξ**_[′] , given in (6.22)–(6.24). That is, it depends only on the values of _D_ � _**ξ**_ : _**ξ**_[′][�] for infinitesimally close _**ξ**_ and _**ξ**_[′] . There are no unique ways of extending an infinitesimally defined divergence to the entire _M_ . That is, _D_ [ _**ξ**_ : _**ξ**_ ] + _d_ � _**ξ** ,_ _**ξ**_[′][�] gives the same geometry as _D_ � _**ξ** ,_ _**ξ**_[′][�] when a non-negative function _d_ � _**ξ** ,_ _**ξ**_[′][�] satisfies 

**==> picture [262 x 64] intentionally omitted <==**

where _∂i_ = _∂/∂ξ[i]_ and _∂i_[′][=] _[ ∂][/][∂ξ]_[′] _[i]_[.] _[ d]_ � _**ξ** ,_ _**ξ**_[′][�] = � _D_ � _**ξ**_ : _**ξ**_[′][��][2] given in (3.25) is such an example. Interestingly, however, when a manifold is dually flat, we can obtain a unique canonical divergence, despite the fact that there are many locally equivalent divergences. To show this, we begin with the following lemma. 

**Lemma 6.1** _When M is dually flat, there are a pair of dual affine coordinate systems_ _**θ** and_ _**η** and of Legendre-dual convex functions ψ(_ _**θ** ) and ϕ(_ _**η** ) satisfying_ 

**==> picture [218 x 12] intentionally omitted <==**

_such that the metric is given by_ 

**==> picture [250 x 12] intentionally omitted <==**

_and the cubic tensor by_ 

**==> picture [215 x 25] intentionally omitted <==**

_Proof_ By using the affine coordinate system _**θ**_ for which _Γi jk(_ _**θ** )_ = 0, (6.6) reduces to 

**==> picture [193 x 13] intentionally omitted <==**

Because the connections are symmetric, we have 

**==> picture [196 x 11] intentionally omitted <==**

We fix index _j_ and denote it by · . So we have 

**==> picture [194 x 11] intentionally omitted <==**

6 Dual Affine Connections and Dually Flat Manifold 

140 

Then, there is a function _ψ_ · satisfying 

**==> picture [189 x 10] intentionally omitted <==**

or for each _j_ , we have 

**==> picture [190 x 11] intentionally omitted <==**

Since _gi j_ is symmetric, we have 

**==> picture [203 x 11] intentionally omitted <==**

This guarantees the existence of a scalar function _ψ_ such that 

**==> picture [189 x 11] intentionally omitted <==**

Hence 

**==> picture [193 x 11] intentionally omitted <==**

where _ψ(_ _**θ** )_ is convex because _gi j_ is positive-definite. Since ∇ _i_ = _∂i_ for the _**θ**_ - coordinates, _Ti jk_ is given from (6.18) by 

**==> picture [206 x 11] intentionally omitted <==**

By using the dual affine coordinate system, we have a convex function _ϕ(_ _**η** )_ that satisfies (6.56) and (6.58). It is easy to see that the two coordinate systems are connected by a Legendre transformation, so that the two functions are the Legendre duals. □ 

**Theorem 6.7** _When M is dually flat, there exists a Lengdre pair of convex functions ψ(_ _**θ** ), ϕ(_ _**η** ) and a canonical divergence given by the Bregman divergence_ 

**==> picture [240 x 13] intentionally omitted <==**

They are uniquely determined except for affine transformations. Conversely, the canonical divergence gives the original dually flat Riemannian structure. 

**Theorem 6.8** _The KL-divergence is the canonical divergence of an exponential family of probability distributions which is invariant and dually flat._ 

_Remark 1_ Many studies begin with the KL-divergence given a priori without any justification. However, our theory shows that the KL-divergence is an outcome of dual flatness in the invariant geometry. 

_Remark 2_ The KL-divergence is derived as the unique canonical divergence without assuming decomposability in the above theorem. See also another derivation by Jiao et al. (2015). 

6.6 Canonical Divergence in Dually Flat Manifold 

141 

For a dually flat _M_ , its affine coordinates _**θ**_ and _**η**_ are not unique. Any affine transformation 

**==> picture [230 x 12] intentionally omitted <==**

where **A** is an invertible matrix and _**b** ,_ _**c**_ are constants, gives a set of dually coupled coordinate systems. The convex functions _ψ(_ _**θ** )_ are not unique either, because we may add a linear term, as in 

**==> picture [216 x 12] intentionally omitted <==**

where _**a**_ is a vector and _d_ is a scalar. However, the canonical divergence 

**==> picture [240 x 13] intentionally omitted <==**

is uniquely determined, not depending on a specific choice of affine coordinate systems. 

## **6.7 Canonical Divergence in General Manifold of Dual Connections** 

It is known that there always exists a divergence in a manifold having dual connections, such that the same dual structure is given by the divergence (Matumoto 1993). There are many such divergences. So it is an interesting problem to define a canonical divergence, if possible, in a manifold _M_ having non-flat dual connections. When _M_ is dually flat, we have a canonical divergence. Kurose (1994) showed that a canonical divergence called the geometrical divergence exists when _M_ is 1-conformally flat. _M_ is embedded in _**R**[n]_[+][1] in this case. Moreover, when it has constant curvature, the generalized Pythagorean theorem (Theorem 4.5) holds. The _α_ -divergence is a canonical divergence of _Sn_ in this sense. Taking these facts into account, we demonstrate an on-going trial by N. Ay and S. Amari to define a canonical divergence in the general case, briefly without proof (Ay and Amari 2015, Henmi and Kobayashi 2000). 

Consider { _M, g,_ ∇ _,_ ∇[∗] } of a Riemannian manifold with dual affine connections. Let _**ξ**_ be a coordinate system. Given a point _**ξ** p_ and a tangent vector _X_ belonging to the tangent space at _**ξ** p_ , we have a geodesic curve _**ξ** (t)_ , 

**==> picture [192 x 14] intentionally omitted <==**

passing through _**ξ** p_ and its tangent direction is _X_ , 

**==> picture [212 x 14] intentionally omitted <==**

6 Dual Affine Connections and Dually Flat Manifold 

142 

When the geodesic reaches point _**ξ** q_ as _t_ increases from 0 to 1, 

**==> picture [189 x 12] intentionally omitted <==**

_**ξ** q_ is called the exponential map of _X_ , 

**==> picture [199 x 13] intentionally omitted <==**

Given _**ξ** p_ and _**ξ** q_ , we have the inverse of the exponential map, 

**==> picture [216 x 15] intentionally omitted <==**

in a neighborhood of _**ξ** p_ . 

We now define a canonical divergence in a general manifold of dual connections. We first define a divergence between _**ξ** p_ and _**ξ** q_ by 

**==> picture [251 x 26] intentionally omitted <==**

where _**ξ** (t)_ is the primal geodesic connecting _**ξ** p_ and _**ξ** q_ . It can be rewritten as 

**==> picture [252 x 54] intentionally omitted <==**

We then define another divergence by using the dual geodesic _**ξ**_[∗] _(t)_ connecting _**ξ** p_ and _**ξ** q_ : 

**==> picture [271 x 26] intentionally omitted <==**

A canonical divergence is defined by the arithmetic mean of the above two. 

**Definition** A canonical divergence is given by 

**==> picture [263 x 22] intentionally omitted <==**

**Theorem 6.9** _The geometrical structure derived from the canonical divergence (6.80) coincides with the original geometry. When M is dually flat, it gives the canonical divergence of the Bregman type. When M is Riemannian (T_ = 0 _), it is a half of the squared Riemannian distance._ 

Inaduallyflatmanifold,theprojectiontheoremholds:Given _**ξ** p_ andasubmanifold _S_ ⊂ _M_ , the point _**ξ**_[ˆ] _p_ that minimizes _D_ � _**ξ** p_ : _**ξ** q_ �, _**ξ** q_ ∈ _S_ , is the geodesic projection 

6.7 Canonical Divergence in General Manifold of Dual Connections 

143 

of _**ξ** p_ to _S_ such that the geodesic connecting _**ξ** p_ and _**ξ**_[ˆ] _p_ is orthogonal to _S_ at _**ξ**_[ˆ] _p_ . The projection theorem does not hold in general, but we have the following theorem. 

**Theorem 6.10** _The canonical divergence satisfies the projection theorem when_ 

**==> picture [246 x 14] intentionally omitted <==**

_where X[i] is the contravariant component of X_ = exp[−] _**ξ** q_[1] � _**ξ** p_ � _and_ 

**==> picture [189 x 27] intentionally omitted <==**

_Proof_ Consider a divergence ball centered at _**ξ** p_ and with radius _c_ ≥ 0, 

**==> picture [221 x 14] intentionally omitted <==**

Let _S_ be a smooth submanifold of _M_ . Let _**ξ**_[ˆ] _p_ be the minimizer of _D_ � _**ξ** p_ : _**ξ**_ �, _**ξ**_ ∈ _S_ . When _c_ is increasing from 0, the ball _Bc_ touches _S_ at _**ξ**_[ˆ] _p_ . The tangent hypersurfaces of _S_ and _Bc_ are the same at this point, and its normal vector is given by 

**==> picture [227 x 19] intentionally omitted <==**

The tangent direction of the geodesic connecting _**ξ** p_ and _**ξ**_[ˆ] _p_ is given by 

**==> picture [213 x 19] intentionally omitted <==**

So the projection theorem holds when the above two share the same direction. □ 

It is interesting to study when the geodesic projection theorem (6.81) holds. It holds in the dually flat case. It holds for the _α_ -divergence, and hence it is the canonical divergence of the _α_ -geometry. 

## **6.8 Dual Foliations of Flat Manifold and Mixed Coordinates** 

A dually flat manifold admits two types of foliations, _e_ -foliation and _m_ -foliation, which are orthogonal to each other. This structure is useful for separating two quantities, one represented in the _e_ -coordinates and the other in the _m_ -coordinates. This fits particularly well for analyzing a hierarchical system (Amari 2001). 

6 Dual Affine Connections and Dually Flat Manifold 

144 

## _**6.8.1 k-cut of Dual Coordinate Systems: Mixed Coordinates and Foliation**_ 

Let _M_ be a dually flat manifold with dually coupled affine coordinate systems _**θ**_ and _**η**_ . We partition the coordinates into two parts, one consisting of _k_ components and the other consisting of _n_ − _k_ components. We rearrange the suffixes such that the first _k_ components consist of _θ_[1] _, . . . θ[k]_ and the last _n_ − _k_ components consist of _θ[k]_[+][1] _, . . . , θ[n]_ . The same rearrangement is done for the _**η**_ -coordinates. We call such a partition a _k_ -cut. 

Let us compose a new coordinate system _**ξ**_ of which the first _k_ components are the corresponding _**η**_ -coordinates and the last _n_ − _k_ components are _**θ**_ -coordinates such as 

**==> picture [234 x 13] intentionally omitted <==**

This is a new coordinate system called a mixed coordinate system, since _m_ -affine coordinates and _e_ -affine coordinates are mixed in it. It is not an affine coordinate system by itself. The basis vectors of the tangent space in the mixed coordinates are composed of two parts, the first part consisting of 

**==> picture [217 x 25] intentionally omitted <==**

and the second part consisting of 

**==> picture [229 x 22] intentionally omitted <==**

They are orthogonal, because of 

**==> picture [210 x 13] intentionally omitted <==**

Therefore, the Riemannian metric in this coordinate system has a block-diagonal form, 

**==> picture [201 x 26] intentionally omitted <==**

Let us consider an _(n_ − _k)_ -dimensional submanifold obtained by fixing the first _k_ coordinates ( _**η**_ -coordinates) to be equal to _**c**_ = _(c_ 1 _, . . . , ck)_ 

**==> picture [213 x 10] intentionally omitted <==**

and denote it by _M_[∗] _(_ _**c** )_ , in which _θ[k]_[+][1] _, . . . , θ[n]_ run freely. It is an _m_ -flat submanifold, because it is defined by linear constraints on _**η**_ -coordinates. For _**c**_ ̸= _**c**_[′] , _M_[∗] _(_ _**c** )_ and _M_[∗] _(_ _**c**_[′] _)_ do not intersect, 

145 

6.8 Dual Foliations of Flat Manifold and Mixed Coordinates 

**==> picture [107 x 98] intentionally omitted <==**

**----- Start of picture text -----**<br>
M [*] ( c )<br>M *( c )<br>M ( d )<br>M ( d )<br>**----- End of picture text -----**<br>


**Fig. 6.2** Dual orthogonal foliation of manifold 

**==> picture [214 x 21] intentionally omitted <==**

Moreover, the entire _M_ is covered by the aggregate of all _M_[∗] _(_ _**c** )_ ’s 

**==> picture [194 x 20] intentionally omitted <==**

Hence, _M_[∗] _(_ _**c** )_ ’s give a partition of _M_ . Such a partition is called a foliation. 

Dually to the above, we fix the second part of the mixed coordinates ( _**θ**_ -coordinates), 

**==> picture [226 x 12] intentionally omitted <==**

where _**d**_ = _(dk_ +1 _, . . . , dn)_ and _η_ 1 _, . . . , ηk_ run freely. We then have a _k_ -dimensional _e_ -flat submanifold denoted by _M(_ _**d** )_ . Moreover, _M(_ _**d** )_ ’s form another foliation of _M_ . We thus have two foliations. Moreover, _M(_ _**d** )_ and _M_[∗] _(_ _**c** )_ are orthogonal to each other for any _**c**_ and _**d**_ . See Fig. 6.2. 

**Theorem 6.11** _A dually flat M admits a pair of orthogonal k-cut foliations for any k, one of which is m-flat and the other e-flat._ 

## _**6.8.2 Decomposition of Canonical Divergence**_ 

By using the mixed coordinates, the canonical divergence between two points _P_ and _Q_ can be decomposed into a sum of two divergences, one representing the difference in the first part and the other in the second part. Let 

146 

6 Dual Affine Connections and Dually Flat Manifold 

**==> picture [178 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>M ( 6 Q 2) M ( 0 P )<br>RPQ P :( , P , P ) M [*] ( P 1 )<br>Q :( Q , Q ) RQ P M [*] ( Q 1 )<br>**----- End of picture text -----**<br>


**Fig. 6.3** Foliation and decomposition of KL-divergence 

**==> picture [272 x 13] intentionally omitted <==**

be the mixed coordinates of the two points _P_ and _Q_ . _P_ is located at the intersection of _M_[∗] _**η** P_ and _M (_ _**θ** P )_ and _Q_ is at the intersection of _M_[∗] _**η** Q_ and _M_ _**θ** Q_ . We _m_ -project _P_ to _M_ _**θ** Q_ and let the projected point be _R P Q_ . We also _e_ -project _P_ to _M_[∗] _**η** Q_ and let the projected point be _RQP_ . See Fig. 6.3. Since the _m_ -geodesic connecting _P_ and _R P Q_ is orthogonal to the _e_ -geodesic connecting _RP Q_ and _Q, P R P Q Q_ forms a right triangle so that the Pythagorean theorem is applicable. We can do the same thing for the triangle _P RQP Q_ . Then, we have the decomposition theorem. 

**Theorem 6.12** _The canonical divergence D_ [ _P_ : _Q_ ] _is decomposed as_ 

**==> picture [254 x 13] intentionally omitted <==**

_D_ [ _P_ : _R P Q_ | _representing the difference in the first part and D_ [ _R P Q_ : _Q_ | _representing the difference in the second part._ 

## _**6.8.3 A Simple Illustrative Example: Neural Firing**_ 

We show the usefulness of the orthogonal foliation by a simple example. Let us consider a network consisting of two neurons which emit spikes stochastically. Let _x_ 1 and _x_ 2 be two binary random variables, taking values _xi_ = 1 _, i_ = 1 _,_ 2, when neuron _i_ is excited (emitting a spike) and 0 otherwise. Joint probability _p (x_ 1 _, x_ 2 _)_ specifies the 

6.8 Dual Foliations of Flat Manifold and Mixed Coordinates 

147 

stochastic behavior of this network. The manifold of all joint probability distributions _M_ = { _p (x_ 1 _, x_ 2 _)_ } forms a three-dimensional exponential family, because 

**==> picture [252 x 10] intentionally omitted <==**

This is a set of discrete distributions over four elements, and we can write it in the exponential form, 

**==> picture [262 x 31] intentionally omitted <==**

The affine coordinates are given by 

**==> picture [203 x 13] intentionally omitted <==**

The dual coordinates _**η**_ are 

**==> picture [248 x 10] intentionally omitted <==**

showing the firing rate (probability of _xi_ = 1) of neuron _i_ and 

**==> picture [244 x 13] intentionally omitted <==**

showing the joint firing rate (the probability of the two neurons firing at the same time). 

We construct mixture coordinates such that the first part consists of _η_ 1 and _η_ 2 and the second part consists of _θ_[12] . Using the mixed coordinate system 

**==> picture [206 x 14] intentionally omitted <==**

we have a dually orthogonal foliation. The one-dimensional submanifold _M_[∗] _(η_ 1 _, η_ 2 _)_ consists of all the distributions in which the firing rates of the two neurons are fixed to _(η_ 1 _, η_ 2 _)_ . The coordinate _θ_[12] in _M_[∗] _(η_ 1 _, η_ 2 _)_ represents how firing of the two neurons is correlated. When _θ_[12] = 0 _, x_ 1 and _x_ 2 are independent, as is seen from (6.98). Given _θ_[12] , the _e_ -flat submanifold _M_ � _θ_[12][�] represents distributions for which interaction of _x_ 1 and _x_ 2 is fixed to be equal to _θ_[12] but the firing rates of the neurons are arbitrary. Thus, the partition is done in such a way that the first part represents firing rates of neurons and the second part represents the interaction of two neurons (Fig. 6.4). 

One may measure the degree of interaction by the covariance of _x_ 1 and _x_ 2, 

**==> picture [230 x 10] intentionally omitted <==**

It is 0 when the two neurons fire independently. If we use _v_ as a coordinate in _M_[∗] _(η_ 1 _, η_ 2 _)_ , we have another coordinate system _(η_ 1 _, η_ 2 _, v)_ in _M_ . However, the 

6 Dual Affine Connections and Dually Flat Manifold 

148 

**==> picture [333 x 103] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 6.4 Dual foliation of<br>S 3 = { p(x 1 , x 2 ) } M [*] ( 1 2 [)] S 3<br>12<br>M ( 12 )<br>2<br>independent<br>1<br>12 [=0] submanifold<br>**----- End of picture text -----**<br>


_v_ -axis is not orthogonal to the marginal firing rates _η_ 1 _, η_ 2, while _θ_[12] is. Therefore, the mixed coordinates are successful in decomposing the firing rates and interaction orthogonally but _v_ is not. 

Given two distributions _p (x_ 1 _, x_ 2 _)_ and _q (x_ 1 _, x_ 2 _)_ , we have the decomposition of their KL-divergence, as 

**==> picture [243 x 10] intentionally omitted <==**

where _r (x_ 1 _, x_ 2 _)_ is the distribution having the same marginal distributions as _p_ and the same interaction as _q_ . _K L_ [ _p_ : _r_ ] represents the divergence due to the difference in mutual interaction and _K L_ [ _r_ : _q_ ] represents that due to marginal firing rates. 

## _**6.8.4 Higher-Order Interactions of Neuronal Spikes**_ 

We can generalize the idea to a network of _n_ neurons (Amari 2001; Nakahara and Amari 2002; Nakahara et al. 2006; Amari et al. 2003). Let us consider a network consisting of _n_ neurons, which emit spikes stochastically. Let _xi_ be a binary random variable, representing emission of spikes. The state of the network is represented by _**x**_ = _(x_ 1 _, . . . , xn)_ . The set of all probability distributions _p(_ _**x** )_ forms _SN_ −1, where _N_ = 2 _[n]_ , since there are _N_ states _**x**_ . This is an exponential family. By expanding _p(_ _**x** )_ as 

**==> picture [304 x 13] intentionally omitted <==**

we have 

**==> picture [315 x 19] intentionally omitted <==**

6.8 Dual Foliations of Flat Manifold and Mixed Coordinates 

149 

This is called a log linear model. According to the degrees of variables in _xi_ , we partition the entire _**θ**_ in a hierarchical form as 

**==> picture [270 x 27] intentionally omitted <==**

such that each subvector _**θ** k_ consists of coefficients of monomials _x j_ 1 _. . . x jk_ of degree _k_ . 

The dual affine coordinates are composed of 

**==> picture [290 x 13] intentionally omitted <==**

which are joint firing rates of _k_ neurons, _k_ = 1 _, . . . , n_ , and they are hierarchically partitioned as 

**==> picture [213 x 13] intentionally omitted <==**

where 

**==> picture [231 x 13] intentionally omitted <==**

The _k_ th mixed coordinate system is composed of 

**==> picture [260 x 14] intentionally omitted <==**

Since 

**==> picture [206 x 13] intentionally omitted <==**

is composed of the joint firing rates up to _k_ neurons, the other coordinates 

**==> picture [210 x 13] intentionally omitted <==**

represent the directions orthogonal to the joint firing rates up to _k_ neurons. A change in _**θ**[k]_[+][1] _,_ _**θ**[k]_[+][2] _, . . ._ does not affect _**η**_ 1 _, . . . ,_ _**η** k_ but alters the joint firing rates of more than _k_ neurons. Hence, _**Θ**[k]_ represents interactions of more than _k_ neurons orthogonal to the firing rates up to _k_ neurons. 

Among _n_ terms, _**θ**_[1] _, . . . ,_ _**θ**[n]_ , we can say that _**θ**[k]_ represents the degree of mutual interactions among _k_ neurons. _**θ**[k]_ ’s _(k_ ≥ 3 _)_ are called the higher-order correlations or interactions of neurons. Although _**θ**_[1] _, . . . ,_ _**θ**[n]_ are not mutually orthogonal, _**θ**[i]_ are orthogonal to _**η** j ( j_ ̸= _i)_ . 

We show a simple case of _n_ = 3, consisting of three neurons. We have 

**==> picture [226 x 21] intentionally omitted <==**

which represents the third-order interactions of the three neurons. It is orthogonal to firing rates of neurons and joint firing rates of any pair of neurons. Similarly, 

150 

6 Dual Affine Connections and Dually Flat Manifold 

**==> picture [206 x 22] intentionally omitted <==**

represents pairwise interactions of neurons 1 and 2, which are orthogonal to the firing rates of single neurons. 

_Remark_ There are many other hierarchical stochastic systems. One is a Markov chain consisting of various orders. A lower-order system is included in a higherorder system. Hence, we can decompose them in a dually orthogonal way. The auto-regressive (AR) and moving-average (MA) models of time series also form hierarchical stochastic systems, where their degrees compose hierarchy. See Amari (1987, 2001). 

## **6.9 System Complexity and Integrated Information** 

We consider a stochastic system which receives an input signal _**x**_ , processes it and emits output _**y**_ , and study its complexity by using a mixed coordinate system. We regard it a muliterminal stochastic channel having _n_ input and _n_ output terminals, see Fig. 6.5. Input _**x**_ = _(x_ 1 _, . . . , xn)_ and output _**y**_ = _(y_ 1 _, . . . , yn)_ are vectors. When a system is very simple, there is no interaction among different terminals. Hence, output _yi_ depends only on _xi_ and input _x j ( j_ ̸= _i)_ does not affect _yi_ . A complex system has interaction among different terminals and information is integrated to give an integrated output _**y**_ . The degree of interaction is used to define a measure of complexity of the system (Ay 2002, 2015; Ay et al. 2011). Tononi (2008) initiated a new idea of IIT (integrated information theory) to elucidate consciousness. The degree of information integration distinguishes a conscious state from unconscious states in the brain (Balduzzi and Tononi 2008; Oizumi et al. 2014, etc.). 

We propose a measure of complexity, or of information integration, by using a degree of stochastic interaction within a system from the information geometric point of view, based on part of on-going work with M. Oizumi and N. Tsuchiya. This is an extension of the work by Ay (2001, 2015), and is related to the Tononi information integration (Barrett and Seth 2011). 

We consider a 2 × 2 system for simplicity, where input is _**x**_ = _(x_ 1 _, x_ 2 _)_ and output is _**y**_ = _(y_ 1 _, y_ 2 _)_ , having only two terminals (Fig. 6.6), although generalization is easy. We study the binary case where _xi_ and _yi_ take on values 0 and 1, and also the Gaussian case where _**x**_ and _**y**_ are Gaussian random variables with mean 0. The behavior of a system is described by joint probability distribution _p(_ _**x** ,_ _**y** )_ . When the components of _**x**_ and _**y**_ are binary, it belongs to an exponential family _MF_ , called the full model, 

**Fig. 6.5** Stochastic information transmission channel 

**==> picture [196 x 54] intentionally omitted <==**

**----- Start of picture text -----**<br>
x 1 y 1<br>x 2 y 2<br>x y<br>xn yn<br>**----- End of picture text -----**<br>


151 

6.9 System Complexity and Integrated Information 

**Fig. 6.6 a** Channel with two terminals and **b** its split version 

**==> picture [243 x 72] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>x 1 y 1 x 1 y 1<br>x 2 y 2 x 2 y 2<br>**----- End of picture text -----**<br>


**==> picture [313 x 53] intentionally omitted <==**

described by _e_ -coordinates _**θ**_ . The higher-order terms are _θ_[12] _[,]_[1] _x_ 1 _x_ 2 _y_ 1 and so on. We have the corresponding _**η**_ -coordinates. The full model is a graphical model shown in Fig. 6.6a, which is a complete graph, since intrinsic correlations between _x_ 1 and _x_ 2 and also between _y_ 1 and _y_ 2 may exist, as is denoted by the dotted branches in Fig. 6.6a. Refer to information geometry of a graphical model studied in Chap. 11. 

The complexity of a system is measured by the degree to which it is different from split systems where no interaction exists between _xi_ and _y j (i_ ̸= _j)_ (Ay 2002, 2015). So we consider a split system _S_ where no mutual interaction exists, as is shown in Fig. 6.6b. Here, a split model is derived by deleting the branches connecting _xi_ and _y j (i_ ̸= _j)_ . Let the probability distribution of the split model be _q(_ _**x** ,_ _**y** )_ , the _e_ -coordinates of which are _**θ**_[˜] . Since there are no branches connecting _(x_ 1 _, y_ 2 _)_ and _(x_ 2 _, y_ 1 _)_ , we put _θ_[˜] 12 _[XY]_[=] _[θ]_[˜] 21 _[XY]_[=][ 0. (This is because] _[ x][i]_[and] _[ y][ j][(][i]_[̸=] _[j][)]_[ are conditionally] independent where the other variables are fixed.) The higher-order terms are also 0. (This is because no cliques exist connecting three or four nodes in the split model.) Hence, a split model has a probability distribution of the form, 

**==> picture [282 x 53] intentionally omitted <==**

Split models form an exponential family _MS_ , which has ten degrees of freedom and is a submanifold of _MF_ . 

The split model family _MS_ defined in the above is slightly different from the one _MS_[′][defined by N. Ay. In a split model belonging to] _[ M] S_[′][, no direct correlation between] _y_ 1 and _y_ 2 exists, so _θ_[˜] 12 _[Y]_[=][0 in addition to] _[θ]_[˜] 12 _[XY]_[=] _[θ]_[˜] 21 _[XY]_[=][0. That is,] _[M] S_[′][is derived] from _MS_ by deleting the branch connecting _y_ 1 and _y_ 2. _MS_[′][is an] _[ e]_[-flat submanifold] of _MS_ . We do not assume _θ_[˜] 12 _[Y]_[=][0][in] _[M][S]_[,][because] _[y]_[1][and] _[y]_[2][may][be][affected][by] correlated noises directly given from the environment. Since such correlations are given rise to by the environmental situation, even when _x_ 1 and _x_ 2 are independent 

152 

6 Dual Affine Connections and Dually Flat Manifold 

**Fig. 6.7** Split model and orthogonal projection 

**==> picture [111 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
MF p ( x , y )<br>q ( x , y ) MS<br>**----- End of picture text -----**<br>


and _xi_ does not affect _y j ( j_ ̸= _i)_ , _y_ 1 and _y_ 2 can be correlated in _MS_ , but not in _MS_[′][.] To explain this situation, consider a Gaussian model, 

**==> picture [191 x 10] intentionally omitted <==**

where **A** is a 2 × 2 matrix and _**ε**_ is a noise term subject to _N (_ 0 _,_ **V** _)_ , where **V** is the covariance matrix of _**ε**_ . The components _ε_ 1 and _ε_ 2 can be correlated. 

The degree of system complexity, or of integrated information, of _p(_ _**x** ,_ _**y** )_ is measured by the KL-divergence from _p(_ _**x** ,_ _**y** )_ to the split distribution _q_ ˆ _(_ _**x** ,_ _**y** )_ or _q_ ˆ[′] _(_ _**x** ,_ _**y** )_ that is closest to _p(_ _**x** ,_ _**y** )_ in _MS_ or _MS_[′][(Fig.][6.7][),] 

**==> picture [327 x 45] intentionally omitted <==**

They are given by the _m_ -projection of _p(_ _**x** ,_ _**y** )_ to _MS_ and _MS_[′] . Since we have two split models _MS_ and _MS_[′][, we have two definitions of geometric measure of information] integration or stochastic interactions. 

**Definition** Geometric measures of information integration, or system complexity, are defined by 

**==> picture [278 x 28] intentionally omitted <==**

_GI_[′] is the same as that of Ay (2002, 2015) and also that of Barrett and Seth (2011). _GI_ is a new measure. 

Before comparing these two, we show a criterion which such a measure should satisfy. Oizumi et al. (2015) postulated that a degree _φ_ of information integration should satisfy 

**==> picture [205 x 10] intentionally omitted <==**

153 

6.9 System Complexity and Integrated Information 

where _I_ [ _X_ : _Y_ ] is the mutual information between _**x**_ and _**y**_ . _φ_ should be 0 when _I_ [ _X_ : _Y_ ] = 0, that is, when no information is transmitted from _X_ to _Y_ . They argued that various measures of _φ_ so far proposed do not necessarily satisfy the postulate, and defined a new measure _φ_[∗] based on the concept of mismatched decoding, which satisfies the postulate (Oizumi et al. 2015). 

We study properties of _GI_ and _GI_[′] and see if they satisfy the postulate. Since _MS_ is an _e_ -flat submanifold constrained by 

**==> picture [200 x 13] intentionally omitted <==**

where we use _**θ**_ instead of _**θ**_[˜] , we define mixed coordinates 

**==> picture [274 x 13] intentionally omitted <==**

Then, the _m_ -projection of _p(_ _**x** ,_ _**y** )_ to _MS_ , 

**==> picture [218 x 17] intentionally omitted <==**

keeps the _**ξ**_ ˆ of _q_ ˆ _(_ _**x** ,_ _**η y**_ -part of the mixed coordinates invariant. Therefore, the mixed coordinates _)_ are given by 

**==> picture [259 x 13] intentionally omitted <==**

**==> picture [259 x 13] intentionally omitted <==**

where _ηi[X]_[etc. are those of] _[p][(]_ _**[x]**[,]_ _**[ y]**[)]_[. These results are directly obtained by minimizing] _DK L_ [ _p_ : _q_ ] _, q_ ∈ _MS_ , too. We have a similar result in the case of the _m_ -projection to _MS_[′][, where] _[η]_[ˆ] 12 _[Y]_[=] _[ η]_ 12 _[Y]_[is replaced by] _[θ]_[ˆ] 12 _[Y]_[=][ 0.] We see from (6.128) that the _m_ -projection _q_ ˆ _(_ _**x** ,_ _**y** )_ is characterized by 

**==> picture [238 x 10] intentionally omitted <==**

where _pX (_ _**x** )_ etc. are the marginal distributions of _p(_ _**x** ,_ _**y** )_ , etc. This means that the marginal distributions of _q_ ˆ _(_ _**x** ,_ _**y** )_ concerning _**x**_ and _**y**_ are equal to those of _p(_ _**x** ,_ _**y** )_ , respectively. Moreover, the conditional distributions are equal: 

**==> picture [232 x 11] intentionally omitted <==**

The _m_ -projection _q_ ˆ[′] _(_ _**x** ,_ _**y** )_ to _MS_[′][satisfies] 

**==> picture [234 x 41] intentionally omitted <==**

154 

6 Dual Affine Connections and Dually Flat Manifold 

Note that _q_ ˆ _Y_[′] _[(]_ _**[y]**[)]_[ =] _[p][Y][(]_ _**[y]**[)]_[ does not in general hold in] _[M] S_[′][.] 

Although _θ_[ˆ] 12[′] _[Y]_[=][ 0 holds in] _[q]_[ˆ][′] _[(]_ _**[x]**[,]_ _**[ y]**[)]_[, this does not mean that] _[y]_[ˆ] 1[′][and] _[y]_[ˆ] 2[′][are uncorre-] lated. When _x_ 1 and _x_ 2 are correlated, _y_ ˆ1[′][and] _[y]_[ˆ] 2[′][are correlated even in the split model] _MS_[′][.] 

The measures _GI_ and _GI_[′] are represented in terms of entropy and mutual information as follows. Due to the Pythagorean theorem, we have, in the binary case, 

**==> picture [248 x 26] intentionally omitted <==**

where _H_ [ _p_ ] is the entropy of _p(_ _**x** ,_ _**y** )_ and _p_ 0 _(_ _**x** ,_ _**y** )_ is the uniform distribution of which entropy is put equal to _c_ . Therefore, we have 

**==> picture [261 x 13] intentionally omitted <==**

This holds in general, including the Gaussian case, where an independent distribution _p_ 0 _(_ _**x** ,_ _**y** )_ is used instead of the uniform _p_ 0. Similarly, 

**==> picture [232 x 13] intentionally omitted <==**

Since the entropy is decomposed as 

**==> picture [220 x 10] intentionally omitted <==**

we have the following theorem, which is useful for calculating _GI_ and _GI_[′] . 

**Theorem 6.13** _The two geometrical measures GI and GI_[′] _are given, in terms of conditional entropy, as_ 

**==> picture [245 x 41] intentionally omitted <==**

_whereY_ ˆ[′] _denote the random variablesX, and Y denote the random variables_ _**y** subject to q_ _**x**_ ˆ _( and_ _**x** ,_ _**y** )_ _**y** and subject toq_ ˆ[′] _(_ _**x** ,_ _**y** p), respectively.(_ _**x** ,_ _**y** ), and Y_[ˆ] _and_ 

Moreover, we have simpler representations. 

## **Theorem 6.14** 

**==> picture [275 x 38] intentionally omitted <==**

155 

6.9 System Complexity and Integrated Information 

_where I Y_ ˆ1 : _Y_ ˆ2| _X is the conditional mutual information. This elucidates the rela-_ � � _tion between GI and GI_[′] _as follows:_ 

**==> picture [244 x 49] intentionally omitted <==**

**Theorem 6.15** _GI satisfies the postulate (6.124) but GI_[′] _does not._ 

_Proof_ Since both _GI_ and _GI_[′] are given by the KL-divergence, they satisfy 

**==> picture [198 x 10] intentionally omitted <==**

Let us next consider the independent distribution 

**==> picture [218 x 10] intentionally omitted <==**

derived from _p(_ _**x** ,_ _**y** )_ . The mutual information is 

**==> picture [247 x 13] intentionally omitted <==**

Since _p_ ind _(_ _**x** ,_ _**y** )_ satisfies _θ_ 12 _[XY]_[=] _[ θ]_ 21 _[XY]_[=][ 0, this is included in] _[M][S]_[. So] 

**==> picture [198 x 10] intentionally omitted <==**

since _q_ ˆ is the minimizer of divergence in _MS_ . However, _p_ ind _(_ _**x** ,_ _**y** )_ does not necessarily satisfy _θ_ 12 _[Y]_[=][ 0 and hence is not included in] _[M] S_[′][in general. Hence,] 

**==> picture [199 x 10] intentionally omitted <==**

is not guaranteed. Indeed, for _p(_ _**x** ,_ _**y** )_ where _X_ and _Y_ are independent, _I (X_ : _Y )_ = 0, but if _Y_ 1 and _Y_ 2 are correlated 

**==> picture [185 x 10] intentionally omitted <==**

**==> picture [9 x 7] intentionally omitted <==**

We analyze the Gaussian system given in (6.119) for illustration. 

_Example 1_ ( _Gaussian channel_ ) The joint probability distribution of _(_ _**x** ,_ _**y** )_ in (6.119) is 

**==> picture [307 x 25] intentionally omitted <==**

156 

6 Dual Affine Connections and Dually Flat Manifold 

when _**x**_ is subject to _N (_ 0 _,_ **I** _)_ . By putting 

**==> picture [187 x 25] intentionally omitted <==**

it is rewritten as 

**==> picture [233 x 25] intentionally omitted <==**

where **R** is the inverse of the covariance matrix 

**==> picture [199 x 15] intentionally omitted <==**

and they are given explicitly as functions of the system parameters **A** and **V** . 

A full model _p(_ _**x** ,_ _**y** )_ belongs to an exponential family, where the _**θ**_ -coordinates are **R** and _**η**_ -coordinates are **[�]** . A split model is given by 

**==> picture [323 x 28] intentionally omitted <==**

_q_ which does not include termsˆ _(_ _**x** ,_ _**y** )_ from _p(_ _**x** ,_ _**y** )_ . _θi j[XY][x][i][ y][ j][(][i]_[̸=] _[j][)]_[. By using this expression, we obtain] 

However, there is a serious problem concerning the optimal solution. The solution can be written as 

**==> picture [193 x 12] intentionally omitted <==**

but _**A**_[ˆ] is not diagonal. The solution is split in the sense that _θi j[XY]_ = 0 _(i_ ̸= _j)_ is satisfied and its graph does not have diagonal branches, but not split in the sense that _**A**_ ˆ is not diagonal. Hence, _E_ [ _yi_ | _**x**_ ] depends on both _x_ 1 and _x_ 2. This does not happen in _MS_[′][, since] _[E]_[ [] _[y][i]_[|] _**[x]**_[]][ =] _[E]_[ [] _[y][i]_[|] _[x][i]_[] holds.] 

In order to overcome this flaw, we introduce the third model of split systems, 

**==> picture [322 x 13] intentionally omitted <==**

This condition can be written as the Markov conditions 

**==> picture [240 x 10] intentionally omitted <==**

that is, _Xi_ and _Y j (i_ ̸= _j)_ are conditionally independent when _X j_ is fixed, 

**==> picture [242 x 9] intentionally omitted <==**

Since _MS_[′′][includes] _[p][X][(]_ _**[x]**[)][p][Y][(]_ _**[y]**[)]_[,] _[ GI]_[ ′′][satisfies the postulate] 

**==> picture [211 x 10] intentionally omitted <==**

157 

6.9 System Complexity and Integrated Information 

However, _MS_[′′][⊂] _[M][F]_[is neither] _[ e]_[-flat nor] _[ m]_[-flat. It is curved, so we need to study its] properties carefully. This remains as a problem for our future study (Oizumi et al. 2016). 

Before finishing this subsection, we show an example in the binary case. 

_Example 2_ ( _Binary channel_ ) We consider two binary transmission channels. One is _C_ 1 _(ε)_ , in which _yi_ chooses _xi_ with probability 1 − _ε_ and chooses _x j (i_ ̸= _i)_ with probability _ε_ . Once _x_ 1 or _x_ 2 is chosen by _y_ 1, the transmission of _x_ 1 _(x_ 2 _)_ to _y_ 1 is through a binary symmetric channel with error probability _ν_ . This means that, when _x_ 1 = 1, the probability of _y_ 1 = 1 is 1 − _ν_ and that of _y_ 1 = 0 is _ν_ . The other cases are similarly defined. We further consider another channel _C_ 2 which generates _**z**_ = _(_ 0 _,_ 0 _)_ , _(_ 1 _,_ 1 _)_ with probability 1 _/_ 2 each, and its output is _**y**_ = _**z**_ irrespective of _**x**_ . So no information transmission takes place in _C_ 2. We study a combined binary channel _C_ that chooses _C_ 1 with probability 1 − _δ_ and chooses _C_ 2 with probability _δ_ . The split model _MS_ is defined by _ε_ = 0, and _ν_ is not necessarily 0. _ν_ plays the role of correlated _**ε**_ in the Gaussian case. The split model _MS_[′][is defined][by] _[ε]_[=][0] and _δ_ = 0. 

_Remark 1_ We can introduce a hierarchy of split models in a general channel having _n_ input terminals and _n_ output terminals. We partition _k_ inputs _x_ 1 _, . . . , xn_ into _k_ subsets _X_ 1 _, . . . , X k_ , 

**==> picture [242 x 11] intentionally omitted <==**

Similarly, we partition _**y**_ into _Y_ 1 _, . . . , Yk_ . The split model _MS_ with respect to this partition is obtained by deleting all the branches connecting terminals in _Xi_ and _Y j (i_ ̸= _j)_ . Since a refinement of a partition gives a finer partition, we have a hierarchical structure concerning partitions. Hence, _GI_ forms a hierarchical structure with respect to partitions. 

_Remark 2_ We can extend the above results to the dynamical systems of Markov chains, such that the state _**x** t_ +1 at time _t_ + 1 is determined stochastically by a conditional probability distribution _p (_ _**x** t_ +1| _**x** t )_ of a stochastic channel. The initial state distribution _p (_ _**x**_ 0 _)_ is set equal to the stationary distribution of the Markov chain. 

## **6.10 Input–Output Analysis in Economics** 

We show another example of the dual foliation from the field of economics, due to Morioka and Tsuda (2011). The input–output analysis uses a table **A** , which is an _n_ × _n_ matrix, showing the quantities of products and amounts of consumption in _n_ industries and how the products are transferred from one industry to another for consumption. Namely, each row and column of matrix **A** = � _Ai j_ � represent an industry and _Ai j_ is the amount of product that industry _i_ sells to industry _j_ . _Ai j_ are represented in the monetary basis. 

158 

6 Dual Affine Connections and Dually Flat Manifold 

Let 

**==> picture [193 x 30] intentionally omitted <==**

be the row sum of the table, which represents the quantity of gross product of industry _i_ . Similarly, the column sum 

**==> picture [194 x 29] intentionally omitted <==**

represents the amount of gross consumption of industry _j_ . They satisfy 

**==> picture [215 x 22] intentionally omitted <==**

We have an interest not merely in the gross product and consumption of each industry butmoreintheirinteractions,reflectingthestructuralrelationshipbetweenindustries. To this end, let us consider the manifold _M_ consisting of all input–output tables 

**==> picture [188 x 10] intentionally omitted <==**

where _Ai j_ form a coordinate system of _M_ . We define another coordinate system by 

**==> picture [220 x 13] intentionally omitted <==**

and regard it as an _e_ -flat coordinate system of _M_ . The associated convex function is 

**==> picture [213 x 24] intentionally omitted <==**

Then, the dual _m_ -coordinate system is given by ∇ _ψ(_ **L** _)_ which is merely 

**==> picture [188 x 13] intentionally omitted <==**

and the dual convex function is 

**==> picture [233 x 24] intentionally omitted <==**

The canonical divergence between two input–output tables **A** and **B** is 

**==> picture [271 x 26] intentionally omitted <==**

159 

6.10 Input–Output Analysis in Economics 

In order to separate the distributions of gross products and consumptions from their interrelations, we treat _Ai_ · and _A_ · _j_ as a part of new _m_ -affine coordinates, which are linear combinations of _m_ -coordinates _Ai j_ . We replace the last row _Ani_ and last column _A jn_ by _Ai_ · and _A_ · _j_ , respectively. Then we have a modified table in which the last row and column are replaced. We denote the new coordinates by _A_[˜] _i j_ . This is given by an affine coordinate transformation from **A** . The corresponding _e_ -affine coordinates, denoted by _L_[˜] _i j_ are calculated from the invariance relation 

**==> picture [215 x 15] intentionally omitted <==**

as 

**==> picture [316 x 25] intentionally omitted <==**

**==> picture [317 x 13] intentionally omitted <==**

We partition the coordinates and construct the mixed coordinates. The first part˜ consists of � _Ai_ · _, A_ · _j , A_ ··� _, i, j_ = 1 _, . . . , n_ − 1. The second part consists of _L i j , i, j_ = 1 _, . . . , n_ − 1. The first _m_ -coordinates represent the gross products and consumptions in industries, while the second part is orthogonal to the first part, representing the interrelations among industries. The divergence between two tables can be decomposed into a sum, the one due to the difference of gross products and consumptions and the second due to the difference in the interrelations. 

The _L_[˜] _i j_ are obtained by deleting industry _n_ from the table. Hence, it is not symmetric with respect to all the industries. To overcome this difficulty, let _L_[˜] _i j[(][k][)]_[be the] _e_ -coordinates where industry _k_ is replaced, instead of industry _n_ , by the total sums. Then, their average defined by 

**==> picture [200 x 28] intentionally omitted <==**

would be a good measure of interactions among industries. 

Instead of replacing one industry _k_ by the gross distributions, we may add � _Ai_ · _, A_ · _j , A_ ··� to the input–output table as its _(n_ + 1 _)_ th row and _(n_ + 1 _)_ th column. Then, the interaction part based on the _(n_ + 1 _)_ th row and column becomes 

**==> picture [202 x 25] intentionally omitted <==**

Morioka and Tsuda (2011) used this for analysis. Observing the trend of yearly changes in the first part of � _Ai_ · _, A_ · _j_ �, one can understand the developments of the gross products in industries. The yearly changes 

160 

6 Dual Affine Connections and Dually Flat Manifold 

of the second part _L_[˜] _i j_ represent how the industrial interrelationship changes. This reflects the structural change in the interrelations among industries. 

One can try to alter the gross amounts of products of industries from _Ai_ · to 

**==> picture [190 x 12] intentionally omitted <==**

by using arbitrary coefficients _μ_ 1 _, . . . , μn_ . By using another set of coefficients _λ_ 1 _, . . . , λn_ , the gross consumptions are changed to 

**==> picture [193 x 13] intentionally omitted <==**

Such changes can be realized by transforming _Ai j_ into 

**==> picture [197 x 13] intentionally omitted <==**

This is called the RAS transformation, by which the interrelationship _L_[˜] _i j_ does not change but the gross amounts of products and consumptions may change arbitrarily. 

Annual statistics of gross amounts _Ai_ · and _A j_ · are published every year, but _Ai j_ themselves are not, because construction of the entire _Ai j_ table is laborious. So, the entire table is published only every five years in Japan, for example. In such a case, we can interpolate the _L_[˜] _i j_ part (or _Si j_ part) in the unknown years by using the _e_ -geodesic in the interaction part from the known _S_ -parts. Morioka and Tsuda (2011) studied the change in the industrial structure of Japan after the War, finding remarkable changes occurring as the Japanese economy developed. 

See Marriott and Salmon (2011) for other applications of geometry to economics. 

## **Remarks** 

The concept of dual affine connections was introduced in a Riemannian manifold by Amari (1982) and Nagaoka and Amari (1982). See also Amari and Nagaoka (2000). The idea emerged from the invariant geometry of a manifold of probability distributions due to Chentsov (1972). However, the late professor K. Nomizu stated that such a concept exists in affine differential geometry (Nomizu and Sasaki 1994). 

Affine differential geometry studies properties of _n_ -dimensional hypersurfaces embedded in an _(n_ + 1 _)_ -dimensional affine space. This was originally developed by W. Blaschke and also developed by J. L. Koszul (see Nomizu and Sasaki 1994). The Hessian manifold of Shima (2007) also deals with a dually flat manifold. 

The concept of dual (conjugate) affine connections is naturally introduced in affine differential geometry but it has not played a central role. The concept of dual connections in information geometry is more general, since it deals with a manifold which might not be embedded in an _(n_ +1 _)_ -dimensional affine space. However, there is much overlap between these two fields and they have been developping through mutual interactions. The present monograph does not touch upon affine differential geometry, although there are many common interesting problems. Excellent work 

6.10 Input–Output Analysis in Economics 

161 

is found in Kurose (1990, 1994, 2002). See also Matsuzoe (1998, 1999), Matsuzoe et al. (2006), Uohashi (2002) and many others. 

lnvariant geometry is due to Chentsov (1972), where the uniqueness of two tensors _G_ and _T_ is presented. The invariant geometry ( _α_ -geometry) is constructed from these tensors. How is a general dual manifold related to a statistical manifold? Due to a theorem of Banerjee et al. (2005), we know that any dually flat manifold is realized as an exponential family. Lê (2005) proved a stronger theorem that any dual manifold can be realized as a submanifold of an _N_ -dimensional probability simplex _SN_ for a sufficiently large _N_ . There is another interesting problem: Given a Riemannian manifold { _M, G_ }, on what condition does it become dually flat by supplementing an adequate _T_ ? Such a Riemannian manifold is said to be flattenable. It is interesting to know the characterization of flattenable Riemannian manifolds. When _n_ = 2, this is always possible, but when _n >_ 2, it is not. This problem was studied by Amari and Armstrong (2014). 

The Chentsov invariance theorem was proved in the discrete case of _Sn_ . Amari and Nagaoka (2000) formulated the invariance in a general continuous case in terms of sufficient statistics. However, there is no rigorous proof due to difficulties in dealing with a function space. The Leipzig group, including J. Jost and H. V. Lê, is tackling this problem (Ay et al. 2013). 

The global topology of a statistical manifold is another interesting problem of differential geometry. It is interesting to see how a dual pair of local curvatures is related to the global topology of a manifold. 

Finally, we give a list of monographs on information geometry. They each have the own characteristics: Amari (1985), Amari and Nagaoka (2000), Arwini and Dodson (2008), Calin and Udriste (2013), Chentsov (1972), Kass and Vos (1997), Murray and Rice (1993). 

**Part III Information Geometry of Statistical Inference** 

**Chapter 7 Asymptotic Theory of Statistical Inference** 

## **7.1 Estimation** 

Let _M_ = { _p(_ _**x** ,_ _**ξ** )_ } be a statistical model specified by parameter _**ξ**_ , which is to be estimated. When we observe _N_ independent data _D_ = { _**x**_ 1 _, . . . ,_ _**x** N_ } generated from _p(_ _**x** ,_ _**ξ** )_ , we want to know the underlying parameter _**ξ**_ . This is a problem of estimation, and an estimator 

**==> picture [207 x 13] intentionally omitted <==**

is a function of _D_ . The estimation error is given by 

**==> picture [189 x 13] intentionally omitted <==**

when _**ξ**_ is the true value. The bias of the estimator is defined by 

**==> picture [204 x 19] intentionally omitted <==**

where the expectation is taken with respect to _p(_ _**x** ,_ _**ξ** )_ . An estimator is unbiased when _**b** (_ _**ξ** )_ = 0. 

The asymptotic theory studies the behavior of an estimator when _N_ is large. When 

**==> picture [197 x 15] intentionally omitted <==**

it is asymptotically unbiased. 

It is expected that a good estimator converges to the true parameter as _N_ tends to infinity. It is written as 

**==> picture [190 x 17] intentionally omitted <==**

**==> picture [14 x 7] intentionally omitted <==**

© Springer Japan 2016 

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_7 

166 

7 Asymptotic Theory of Statistical Inference 

When this holds, an estimator is consistent. The accuracy of an estimator is measured by the error covariance matrix, **V** = � _Vi j_ �, 

**==> picture [230 x 19] intentionally omitted <==**

It decreases in general in proportion to 1 _/N_ , so that the estimator _**ξ**_[ˆ] becomes sufficiently accurate as _N_ increases. The well-known Cramér–Rao Theorem gives a bound of accuracy. 

**Theorem 7.1** _For an asymptotically unbiased estimator_ _**ξ**_[ˆ] _, the following inequality holds:_ 

**==> picture [232 x 22] intentionally omitted <==**

**==> picture [232 x 22] intentionally omitted <==**

_where_ **G** = � _gi j_ � _is the Fisher information matrix,_ **G**[−][1] = � _g[i j]_[�] _is its inverse, and the matrix inequality implies that_ **V** − **G**[−][1] _/N is positive semi-definite._ 

The maximum likelihood estimator (MLE) is the maximizer of the likelihood, 

**==> picture [227 x 30] intentionally omitted <==**

It is known that the MLE is asymptotically unbiased and its error covariance satisfies 

**==> picture [227 x 25] intentionally omitted <==**

attaining the Cramér–Rao bound (7.7) asymptotically. Such an estimator is said to be Fisher efficient (first-order efficient). 

_Remark_ We do not mention Bayes estimators, where a prior distribution of parameters is used. However, when the prior distribution is uniform, the MLE is the maximum a posteriori Bayes estimator. Moreover, it has the same asymptotic properties for any regular Bayes prior. Information geometry of Bayes statistics will be touched upon in a later chapter. 

## **7.2 Estimation in Exponential Family** 

An exponential family is a model having excellent properties such as dual flatness. We begin with an exponential family 

167 

7.2 Estimation in Exponential Family 

**==> picture [225 x 10] intentionally omitted <==**

to study the statistical theory of estimation, because it is simple and transparent. Given data _D_ , their joint probability distribution is written as 

**==> picture [241 x 10] intentionally omitted <==**

where _**x**_ ¯ is the arithmetic mean of the observed examples, 

**==> picture [196 x 30] intentionally omitted <==**

It is a sufficient statistic. The MLE _**θ**_[ˆ] MLE is given by differentiating (7.12) and is the solution to 

**==> picture [202 x 10] intentionally omitted <==**

Using the _**η**_ -coordinates, this is written as 

**==> picture [189 x 10] intentionally omitted <==**

Observed data defines a point _**η**_ ¯ in _M_ of which the coordinates are 

**==> picture [181 x 10] intentionally omitted <==**

We call it the observed point determined from data _D_ , which is nothing other than the MLE in the _**η**_ -coordinates. The following theorem is easy to prove. 

**Theorem 7.2** _The MLE is unbiased and efficient:_ 

**==> picture [195 x 13] intentionally omitted <==**

**==> picture [195 x 22] intentionally omitted <==**

_Proof_ We see from the central limit theorem that _**η**_ ¯ is asymptotically subject to a Gaussian distribution with mean _**η**_ and covariance matrix **G**[−][1] _/N_ . Since the MLE attains the Cramér–Rao bound, it is the best estimator in an exponential family. □ 

_Remark_ The MLE _**θ**_[ˆ] MLE expressed in the _**θ**_ -coordinates is asymptotically unbiased and asymptotically efficient, but it is not exactly unbiased, nor does it attain the Cramér–Rao bound exactly. This is because the bias and covariance matrix are not tensors so that the results are different in the _**θ**_ -coordinate system. 

168 

7 Asymptotic Theory of Statistical Inference 

## **7.3 Estimation in Curved Exponential Family** 

Estimation in an exponential family is too simple. We study estimation in a curved exponential family, which is a submanifold embedded in an exponential family. Many statistical models belong to this class. A curved exponential family of probability distributions with parameter _**u**_ is written in the following form: 

**==> picture [241 x 10] intentionally omitted <==**

_S_ = { _p(_ _**x** ,_ _**u** )_ } is a submanifold of an exponential family _M_ = { _p(_ _**x** ,_ _**θ** )_ }, where _**u**_ is a coordinate system of _S_ . 

Observed data _D_ specifies the observed point _**η**_ ¯ = _**x**_ ¯ in the ambient exponential family _M_ , which is not included in _S_ in general. An estimated value of _**u**_ is derived by mapping the observed point _**η**_ ¯ to _S_ (Fig. 7.1). That is, an estimator _**u**_ ˆ is derived from a mapping from _M_ to _S_ . Let it be 

**==> picture [190 x 10] intentionally omitted <==**

such that 

**==> picture [190 x 11] intentionally omitted <==**

The observed point _**η**_ ¯ converges to the true point as _N_ goes to infinity, as is clear from the law of large numbers. Hence, a consistent estimator satisfies 

**==> picture [207 x 15] intentionally omitted <==**

Let us consider the set of points _**η**_ in _M_ which are mapped to _**u**_ by the estimator _f (_ _**η** )_ . This is the inverse image of an estimator _f_ , denoted by 

**==> picture [247 x 12] intentionally omitted <==**

**Fig. 7.1** An estimator _f_ : _**η**_ → _**η**_ = _f (_ _**η** )_ defines auxiliary submanifold _A(_ _**u** )_ = _f_[−][1] _(_ _**u** )_ 

169 

7.3 Estimation in Curved Exponential Family 

It forms an _(n_ − _m)_ -dimensional submanifold passing through _**η** (_ _**u** )_ ∈ _M_ (Fig. 7.1). We call it an ancillary submanifold associated with estimator _f_ . _A(_ _**u** )_ is defined at each _**u**_ ∈ _S_ and they give a foliation of _M_ at least in a neighborhood of _S_ , 

**==> picture [226 x 41] intentionally omitted <==**

where _U_ is a neighborhood of _S_ . When _A(_ _**u** )_ ∋ _**η** (_ _**u** )_ , that is, when _A(_ _**u** )_ passes through _**η** (_ _**u** )_ , _A(_ _**u** )_ gives a consistent estimator. 

An estimator defines an ancillary family _A_ = { _A(_ _**u** )_ } associated with it and conversely an ancillary family _A_ defines a consistent estimator when _f_ satisfies (7.22). It is possible to study the performance of an estimator in terms of the geometry of an ancillary family. Let us define a coordinate system _**v**_ inside each _A(_ _**u** )_ such that the origin _**v**_ = 0 is at _**η** (_ _**u** )_ which is the intersection of _A(_ _**u** )_ and _S_ . We denote coordinates of _S_ by 

**==> picture [220 x 9] intentionally omitted <==**

and coordinates in _A(_ _**u** )_ by 

**==> picture [230 x 10] intentionally omitted <==**

Then, combining the two, we have a new coordinate system of _M_ , 

**==> picture [246 x 10] intentionally omitted <==**

defined in a neighborhood _U_ ⊂ _S_ (Fig. 7.2). 

**Fig. 7.2** New coordinate system _**w**_ = _(_ _**u** ,_ _**v** )_ of _M_ 

7 Asymptotic Theory of Statistical Inference 

170 

The _**θ**_ -coordinates and _**η**_ -coordinates in _M_ are written in terms of the new coordinates _**w**_ as 

**==> picture [213 x 25] intentionally omitted <==**

Any point in _S_ satisfies _**v**_ = 0, so that _S_ is represented by 

**==> picture [212 x 10] intentionally omitted <==**

The Jacobian matrices of the coordinate transformations between _**w**_ and _**θ**_ and _**w**_ and _**η**_ are expressed as 

**==> picture [193 x 48] intentionally omitted <==**

and are decomposed as 

**==> picture [221 x 49] intentionally omitted <==**

in terms of the _**u**_ and _**v**_ coordinates. 

The Fisher information is given in the _**w**_ -coordinate system as 

**==> picture [198 x 15] intentionally omitted <==**

and is decomposed as 

**==> picture [201 x 25] intentionally omitted <==**

Given data _D_ , the _**u**_ - and _**v**_ -coordinates _(_ _**u**_ ¯ _,_ ¯ _**v** )_ of the observed point _**η**_ ¯ are determined from 

**==> picture [195 x 10] intentionally omitted <==**

The estimator associated with ancillary family _A_ is given by 

**==> picture [181 x 10] intentionally omitted <==**

7.4 First-Order Asymptotic Theory of Estimation 

171 

## **7.4 First-Order Asymptotic Theory of Estimation** 

When the true distribution is _**u**_ in _S_ , by the law of large numbers, the observed point _**η**_ ¯ converges to 

**==> picture [193 x 10] intentionally omitted <==**

as _N_ tends to infinity. We define the error, that is the deviation of the observed point from the true distribution in the _**η**_ -coordinates, by 

**==> picture [190 x 10] intentionally omitted <==**

Since it is small, we normalize it as 

**==> picture [188 x 12] intentionally omitted <==**

Then, the moments of the error are easily calculated. They are summarized in the following theorem. 

**Theorem 7.3** _The moments of the error (deviation)_ ˜ _**e** in the_ _**η** -coordinates are given by_ 

**==> picture [213 x 55] intentionally omitted <==**

_where_ 

**==> picture [206 x 26] intentionally omitted <==**

Let us also normalize the error in the _**w**_ -coordinates as 

**==> picture [207 x 12] intentionally omitted <==**

where _**w**_ ¯ is the _**w**_ -coordinates of _**η**_ ¯ . By expanding 

we have 

**==> picture [281 x 70] intentionally omitted <==**

7 Asymptotic Theory of Statistical Inference 

172 

where 

**==> picture [203 x 24] intentionally omitted <==**

By inverting (7.50), we have 

**==> picture [239 x 25] intentionally omitted <==**

where 

**==> picture [202 x 13] intentionally omitted <==**

We have, therefore, an asymptotic evaluation of the error in the _**w**_ -coordinates as 

**==> picture [230 x 41] intentionally omitted <==**

˜ ¯ ˜ ˜ Since _**e**_ = √ _N (_ _**x**_ − _**η** )_ are asymptotically Gaussian, the error _**w**_ = _(_ _**u** ,_ ˜ _**v** )_ in (7.48) expressed in the _**w**_ -coordinates is asymptotically 

**==> picture [235 x 25] intentionally omitted <==**

By integrating _p (_ _**u**_ ˜ _,_ ˜ _**v** )_ with respect to _**v**_ ˜, we have the asymptotic distribution of the estimation error 

**==> picture [227 x 25] intentionally omitted <==**

where 

**==> picture [214 x 12] intentionally omitted <==**

When _A(_ _**u** )_ is orthogonal to _M_ , 

**==> picture [208 x 13] intentionally omitted <==**

so that we have 

**==> picture [226 x 25] intentionally omitted <==**

In general 

**==> picture [193 x 10] intentionally omitted <==**

and _(g_ ¯ _ab)_ is maximized in the orthogonal case, where the Cramér–Rao bound is asymptotically attained. An estimator is efficient in this case. 

7.4 First-Order Asymptotic Theory of Estimation 

173 

We summarize the results in the following. 

**Theorem 7.4** _(1) An estimator_ _**u**_ ˆ _is consistent when its ancillary family A(_ _**u** ) passes through_ _**w**_ = _(_ _**u** ,_ 0 _)_ ∈ _S in M. (2) A consistent estimator is efficient when A(_ _**u** ) is orthogonal to S._ 

The maximum likelihood estimator is given by the _m_ -projection of _**η**_ ¯ to _S_ . Therefore, its _A(_ _**u** )_ is orthogonal to _S_ and it is efficient. 

_Remark_ The first-order asymptotic theory is a linear theory in a small neighborhood of the true distribution. Hence, it is enough to consider only the tangent space _T_ _**η**_ instead of the entire _M_ for evaluating the performance of an estimator. Therefore, the asymptotic theory is common for all regular statistical models. We may consider the case where the ancillary family _A(_ _**u** )_ depends on _N_ so that it is denoted as _AN (_ _**u** )_ . Then, the theory holds when _AN (_ _**u** )_ passes through _(_ _**u** ,_ 0 _)_ and is orthogonal to _S_ , as _N_ tends to infinity. Such an ancillary family is important for studying the performance of testing hypotheses. 

## **7.5 Higher-Order Asymptotic Theory of Estimation** 

The covariance matrix of an efficient estimator achieves the CR-bound **G**[−][1] _/N_ asymptotically when we ignore the term of order 1 _/N_[2] . The higher-order asymptotic theory evaluates this higher-order term. This makes it possible to compare the performances of various efficient estimators more accurately. 

In order to compare the higher-order errors, we introduce asymptotic biascorrection of estimators. The asymptotic bias _**b**_ of an estimator is given in (7.54), which is of the order 1 _/N_ . If we modify the estimator by 

**==> picture [201 x 13] intentionally omitted <==**

the bias of the new estimator becomes 

**==> picture [217 x 25] intentionally omitted <==**

We call it a bias-corrected estimator. In order to compare the covariances of various efficient estimators, we use their bias-corrected versions. The idea of bias correction is due to Rao (1962), and is necessary in order to exclude estimators which are good at some specific points but not uniformly good. For example, the trivial estimator 

**==> picture [181 x 10] intentionally omitted <==**

which does not depend on data _D_ , is the best estimator when the true distribution is _**u**_ 0 but very bad for other _**u**_ . 

7 Asymptotic Theory of Statistical Inference 

174 

We evaluate the error terms from (7.52) by using the higher-order terms of the Taylor expansion, where we need higher-order moments of the error given in (7.43)– (7.45). We then have the following theorem. The calculations are technical and they are formidably complicated, so we neglect them and give only the results. See Amari (1985). 

**Theorem 7.5** _The covariance matrix of a bias-corrected efficient estimator is given by_ 

**==> picture [295 x 42] intentionally omitted <==**

_where_ 

**==> picture [238 x 16] intentionally omitted <==**

_is the square of the e-embedding curvature of S,_ 

**==> picture [228 x 16] intentionally omitted <==**

_is the square of the m-embedding curvature of the ancillary family A(_ _**u** ) and_ 

**==> picture [225 x 16] intentionally omitted <==**

_is the square of the m-connection of the coordinate system_ _**u** in S._ 

Thus, the second-order terms of the covariance of error are decomposed into 2[�] _[ab]_ a sum of three non-negative terms. The _e_ -curvature term � _HS[e]_ depends on the statistical model _S_ , showing the degree of its deviation from an exponential family. This vanishes when _S_ itself is an exponential family. This term was introduced by _ab_ Efron (1975) and he named it statistical curvature. The term � _ΓS[m]_[2] � depends on the method of parameterization _**u**_ in _S_ and is common to all estimators. The _m_ -curvature 2[�] _[ab]_ term � _HA[m]_ depends on the _m_ -embedding curvature of _A(_ _**u** )_ . It vanishes when the _m_ -curvature of _A(_ _**u** )_ vanishes. Note that the _m_ -curvature of _A(_ _**u** )_ vanishes for the MLE, since the MLE is given by the _m_ -projection of the observed point to _S_ . This is the only quantity which depends on the estimator. 

**Theorem 7.6** _A bias-corrected efficient estimator is second-order efficient when the embedding m-curvature of the associated A(_ _**u** ) vanishes at S. The bias-corrected MLE is second-order efficient._ 

_Remark_ It is intriguing to ask if the higher-order bias-corrected MLE is third-order efficient or not. Unfortunately, it is not. Kano (1997, 1998) disproved the conjecture, showing that the MLE is not third-order efficient. It was Fisher’s belief that the MLE would be the best estimator, but the dream of Fisher was shattered in the third-order asymptotic theory. 

175 

7.6 Asymptotic Theory of Hypothesis Testing 

## **7.6 Asymptotic Theory of Hypothesis Testing** 

Whenthenumberofobservationsislarge,wehaveanasymptotictheoryofhypothesis testing. A typical situation is to test a null hypothesis 

**==> picture [191 x 10] intentionally omitted <==**

against alternatives 

**==> picture [189 x 10] intentionally omitted <==**

in a one-dimensional curved exponential family _S_ = { _p(_ _**x** ,_ _**θ** (u))_ }. This is a onesided test but we can treat a two-sided test similarly. 

Since _S_ is a curve in _M_ , we design a test by defining a rejection region _R_ in _M_ such that hypothesis _H_ 0 is rejected when the observed point _**η**_ ¯ is included in _R_ and is not rejected (is accepted) otherwise. The observed point _η_ ¯ converges to _u_ 0 as _N_ increases when hypothesis _H_ 0 is true. Hence, the rejection region should not include _u_ 0, but its boundary _B_ = _∂ R_ lies close to _u_ 0, approaching _u_ 0 as _N_ tends to infinity. See Fig. 7.3. The boundary surface _B (u_ 0 _)_ of _R_ depends on the null hypothesis _u_ 0. It is an _(n_ − 1 _)_ -dimensional hypersurface crossing _S_ at point _u_[′] 0[which converges to] _u_ 0 as _N_ increases. We denote it by _AN (u_ 0 _)_ . See Fig. 7.3. 

Weconsider _u_ = _u_ 0 asafreescalarparameter,andformanancillaryfamilyof _A_ = { _AN (u)_ }, depending on _N_ . This is a foliation of _M_ consisting of the boundaries of the rejection regions for various _u_ = _u_ 0. This is useful for analyzing the performance of a hypothesis testing. The first-order asymptotic theory is easy, since _**η**_ ¯ converges to _**η** (u_ 0 _)_ under hypothesis _H_ 0. 

**Theorem 7.7** _A test is (first-order) efficient when the associated ancillary surface AN (u) passing through u N is orthogonal to S and u N converges to u_ 0 _, as N tends to infinity._ 

**Fig. 7.3** Rejection region _R_ and associated auxiliary submanifold _AN (_ _**u**_ 0 _)_ 

176 

7 Asymptotic Theory of Statistical Inference 

There are many first-order efficient tests, the Rao test, Wald test, likelihood-ratio test, locally most powerful test among others. How do these tests differ in their performance? The question is answered by studying the power functions of test _T_ , the probabilities _PT (u)_ of rejecting _H_ 0 when the true distribution is _u_ , up to the higher order. There are no uniformly most powerful tests in the second order except for the case that _S_ is an exponential family. Therefore, one test is powerful at a specific point, while another is good at a different point. Information geometry characterizes the performances of various tests by the geometry of the associated ancillary surfaces, in particular by the _m_ -embedding curvatures of _AN (u)_ and the asymptotic angle between _AN (u)_ and _S_ . The second-order power functions of various tests are analyzed in Kumon and Amari (1983), Amari (1985). See also Amari and Nagaoka (2000). 

## **Remarks** 

Information geometry was developed for elucidating higher-order characteristics of statistical inference, in particular, estimation and hypothesis testing. The firstorder theory was established by the Cramér–Rao theory and the Neyman–Pearson fundamental lemma. Researchers tackled the second-order theories in the late 1970s and many results were obtained independently in Japan, Germany, India, Russia and the U.S.A. See Akahira and Takeuchi (1981). B. Efron was the first to point out the role of statistical curvature in the second-order asymptotic theory (Efron 1975). 

Amari (1982) established the second-order theory of estimation by using differential geometry. Kumon and Amari (1983) extended it to the higher-order theory of hypothesis testing. Information geometry was developed further for this purpose, while the duality theory was established by Nagaoka and Amari (1982). See also Amari and Nagaoka (2000). 

Sir David Cox, one of most influential statisticians, paid attention to differential geometrical theory when he visited Japan, and he organized a Workshop on Differential Geometry of Statistics in London in 1984. Numerous active statisticians, C.R. Rao, B. Efron, A.P. Dawid, R. Kass, N. Read, O.E. Barndorff-Nielsen, S. Lauritzen, D.V. Hinkley, S. Eguchi and many others, participated in the workshop. It was very fortunate for information geometry that the topic was discussed openly at this workshop in its period of early infancy. But it was unfortunate that N.N. Chentsov could not participate, because it was supported by NATO and the world was divided by the Iron Curtain at that time. 

We have shown in this chapter the asymptotic theory of statistics in the framework ofacurvedexponentialfamily.Wehavenotdescribeddetails,butshownonlyintuitive ideas and results. The details are shown in Amari (1985) and also in Amari and Nagaoka (2000) or related journal papers. Since not all regular statistical models are curved exponential families, one might wonder if the theory is valid in a more general regular statistical model. We can prove that most results of higher-order statistical theory hold in a general regular statistical model, by forming a fiber bundle-like structure attached to _S_ , consisting of higher-order derivatives of the score function. This is called a local exponential family. See Amari (1985) for details of higher-order asymptotic theory. 

7.6 Asymptotic Theory of Hypothesis Testing 

177 

How about non-regular statistical models, where the Fisher information matrix is degenerate or not defined (diverging to infinity)? In the former case, a statistical model includes singularities. There are many such models. Typical examples include the multilayer perceptron. We will study such models in Part IV. 

A simple example of the latter type is the location model where _x_ is uniformly distributed in the interval of [ _u_ − 0 _._ 5 _, u_ + 0 _._ 5] and _u_ is the unknown parameter. The Fisher information matrix diverges to infinity. In such a statistical model, there is no inner product in the tangent space. The metric is given by a Minkowski metric in the tangent space, which is different from a Riemannian manifold. In this case, _M_ is a Finsler space. An estimator is not asymptotically Gaussian in such a model but is subject to a stable distribution. It is interesting to see the relation between the Finsler metric, stable distribution, and associated fractal structure, comparing them with the Riemannian metric, the Gaussian distribution due to the Central Limit Theorem and the smooth structure of the regular case. However, such a theory has not yet been explored. See a preliminary study by Amari (1984, in Japanese). 

## **Chapter 8 Estimation in the Presence of Hidden Variables** 

## **8.1 EM Algorithm** 

## _**8.1.1 Statistical Model with Hidden Variables**_ 

Let us consider a statistical model _M_ = { _p(_ _**x** ,_ _**ξ** )_ }, where vector random variable _**x**_ is divided into two parts _**x**_ = _(_ _**y** ,_ _**h** )_ so that _p(_ _**x** ,_ _**ξ** )_ = _p(_ _**y** ,_ _**h**_ ; _**ξ** )_ . When _**x**_ is not fully observed but _**y**_ is observed, _**h**_ is called a hidden variable. In such a case, we estimate _**ξ**_ from observed _**y**_ . These situations occur in many applications. One can eliminate the hidden variable _**h**_ by marginalization such that 

**==> picture [225 x 23] intentionally omitted <==**

Then, we have a statistical model _M_[′] = { _pY (_ _**y** ,_ _**ξ** )_ } which does not include hidden variables. However, in many cases, the form of _p(_ _**x** ,_ _**ξ** )_ is simple and estimation is tractable in _M_ , but _M_[′] is complicated because of integration or summation over _**h**_ . Estimation in such a model is computationally intractable. Typically, _M_ is an exponential family. The EM algorithm is a procedure to estimate _**ξ**_ by using a large model _M_ from which model _M_[′] is derived. 

Let us consider a larger model 

**==> picture [195 x 10] intentionally omitted <==**

consisting of all probability density functions of _(_ _**y** ,_ _**h** )_ . When both _**y**_ and _**h**_ are binary variables, _S_ is a probability simplex so that it is an exponential family. We study the continuous variable case similarly, without considering delicate mathematical problems.Model _M_ isincludedin _S_ asasubmanifold.Observeddatagiveanobserved point 

© Springer Japan 2016 

**==> picture [218 x 40] intentionally omitted <==**

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_8 

8 Estimation in the Presence of Hidden Variables 

180 

in _S_ when examples _**x**_ 1 _, . . . ,_ _**x** N_ are fully observed. This is the empirical distribution. When _S_ is an exponential family, it is given by the sufficient statistic 

**==> picture [205 x 22] intentionally omitted <==**

in the _**η**_ -coordinates. The MLE is given by _m_ -projecting _q_ ¯ _(_ _**x** )_ to _M_ . 

We do not have a full observed point _q_ ¯ _(_ _**x** )_ in the hidden variable case. We observe only _**y**_ so that we have an empirical distribution _q_ ¯ _Y (_ _**y** )_ of _**y**_ only. In order to have a candidate of a joint distribution _q_ ¯ _(_ _**y** ,_ _**h** )_ , we use an arbitrary conditional distribution _q(_ _**h**_ | _**y** )_ and put 

**==> picture [216 x 10] intentionally omitted <==**

Since _q(_ _**h**_ | _**y** )_ is arbitrary, we take all of them as possible candidates of observed points and consider a submanifold 

**==> picture [290 x 10] intentionally omitted <==**

This is the observed submanifold in _S_ specified by the partially observed data _**y**_ 1 _, . . . ,_ _**y** N_ . By using the empirical distribution, it is written as 

**==> picture [244 x 22] intentionally omitted <==**

The data submanifold _D_ is _m_ -flat, because it is linear with respect to _q(_ _**h**_ | _**y** )_ . 

Before analyzing the estimation procedure, we give two simple examples of the hidden variable model. 

## **(1) Gaussian mixture model** 

Let _N (μ)_ be a Gaussian distribution of _y_ with mean _μ_ and variance 1. We can treat more general multivariate Gaussian models with unknown covariance matrices in a similar way, but this simple model is enough for the purpose of illustration. The Gaussian mixture model consists of the mixture of _k_ Gaussian distributions having different means _μ_ 1 _, . . . , μk_ , 

**==> picture [256 x 31] intentionally omitted <==**

where _**ξ**_ = _(w_ 1 _, . . . , wk_ ; _μ_ 1 _, . . . , μk)_ ,[�] _wi_ = 1, are unknown parameters to be estimated. Estimation is easy if, for each _y_ 1 _, . . . , yN_ , we know the Gaussian distribution from which this _yi_ is generated. So we introduce a hidden variable _h_ , which takes value _i_ when _y_ is generated from the _i_ th distribution _N (μi )_ . The _h_ is a random variable, the distribution of which is multinomial, taking value _i_ with probability _wi_ . Hence, the entire joint distribution is 

8.1 EM Algorithm 

181 

**==> picture [280 x 25] intentionally omitted <==**

and (8.8) is the marginal distribution of (8.9), obtained by summing _h_ from 1 to _k_ . 

## **(2) Boltzmann machine with hidden units** 

The Boltzmann machine is a stochastic model having a binary vector random variable _**x**_ = _(x_ 1 _, . . . , xn)_ . It originates from a model of a spin system in physics and a model of associative memory in machine learning. Consider a Markov chain { _**x**_ 1 _,_ _**x**_ 2 _, . . ._ }, where state _**x** t_ +1 at time _t_ + 1 is stochastically determined from _**x** t_ . We do not describe here the stochastic dynamics of the state transition, but simply study its stable distribution given by 

**==> picture [268 x 25] intentionally omitted <==**

This is called a Boltzmann machine specified by parameter _**ξ**_ = _(_ **W** _,_ _**a** )_ , where an element _wi j_ of matrix **W** is regarded as the intensity of connection between units _i_ and _j_ . They are assumed to be symmetric _wi j_ = _w ji_ with _wii_ = 0. The linear term _**a**_ · _**x**_ in the exponent is called a bias term, which specifies the tendency of _xi_ to be 1 rather than 0. 

We consider the case where _**x**_ is divided into two parts, _**x**_ = _(_ _**y** ,_ _**h** )_ and _**y**_ is observable while _**h**_ is hidden. For the sake of simplicity, we consider the restricted Boltzmann machine (RBM), which consists of two layers, an observable layer and a hidden layer (Fig. 8.1). Connections exist only between units in the observable layer and between units in the hidden layer. No connections exist between units within the observable layer, and no connections exist between units within the hidden layer. Then, the stable distribution is written as 

**==> picture [252 x 25] intentionally omitted <==**

where, for the sake of simplicity, we ignore the bias term _**a**_ and let it be 0. 

**Fig. 8.1** Restricted Boltzmann machine 

**==> picture [249 x 107] intentionally omitted <==**

8 Estimation in the Presence of Hidden Variables 

182 

The marginal distribution of _**y**_ is 

**==> picture [257 x 28] intentionally omitted <==**

which is a mixture of exponential family distributions. The conditional distribution of _**h**_ given _**y**_ is 

**==> picture [221 x 24] intentionally omitted <==**

when the parameters **W** are known. This model is used in deep learning and we discuss it in a later chapter from the viewpoint of Bayesian information geometry. 

## _**8.1.2 Minimizing Divergence Between Model Manifold and Data Manifold**_ 

The MLE is the minimizer of KL-divergence from the observed point _q_ ¯ to the model manifold in the fully observed case. We have an observed data submanifold _D_ in the hidden case instead of _q_ ¯. We consider the minimizer of KL-divergence from the data manifold to the model manifold. The problem is then to minimize the divergence between two submanifolds _D_ and _M_ , 

**==> picture [300 x 24] intentionally omitted <==**

where the minimum between two sets _D_ and _M_ is taken with respect to _q_ ¯ ∈ _D, p_ ∈ _M_ . The alternating minimization algorithm ( _em_ algorithm) studied in Chap. 1 is useful for this purpose. 

**Theorem 8.1** _The MLE is the minimizer of the KL-divergence from D to M._ 

_Proof_ The KL-divergence from a distribution _q_ ¯ _Y (_ _**y** )q(_ _**h**_ | _**y** )_ ∈ _D_ to a distribution _p(_ _**y** ,_ _**h** ,_ _**ξ** )_ ∈ _M_ is written as 

**==> picture [297 x 49] intentionally omitted <==**

where _c_ is a term not depending on _**ξ**_ and _q(_ _**h**_ | _**y** )_ . We minimize (8.15) with respect to both _**ξ**_ and _q(_ _**h**_ | _**y** )_ alternately by the _em_ algorithm, that is, the alternating use of the _e_ -projection and _m_ -projection. First, assume that _q(_ _**h**_ | _**y** )_ is given and we minimize (8.15) with respect to _**ξ**_ . We consider one observed _**y**_ for simplicity, although we 

8.1 EM Algorithm 

183 

need to consider the expectation with respect to _q_ ¯ _Y (_ _**y** )_ , which is the summation over all observed _**y** i_ . 

Our task is to maximize the second term of (8.15) 

**==> picture [242 x 23] intentionally omitted <==**

with respect to _**ξ**_ . By differentiating it, the solution is given in the equation 

**==> picture [237 x 24] intentionally omitted <==**

In order to minimize (8.15) with respect to _q(_ _**h**_ | _**y** )_ , we use the following lemma. 

**Lemma 8.1** _The e-projection from a point of M to D does not alter the conditional distribution q(_ _**h**_ | _**y** ) and hence the conditional expectation of_ _**h** ._ 

_Proof_ Given _**ξ**_ and observed data _**y**_ , we search for _q(_ _**h**_ | _**y** )_ that minimizes (8.15). This is to minimize 

**==> picture [230 x 13] intentionally omitted <==**

under the constraint 

**==> picture [202 x 23] intentionally omitted <==**

The minimizer is given by the _e_ -projection of _p(_ _**y** ,_ _**h**_ ; _**ξ** )_ to _D_ and analytically by solving 

**==> picture [248 x 25] intentionally omitted <==**

where _λ_ is the Lagrange multiplier corresponding to (8.19). This proves 

**==> picture [211 x 11] intentionally omitted <==**

which is exactly the same as the conditional probability of _**h**_ at _**ξ**_ . 

**==> picture [9 x 7] intentionally omitted <==**

By substituting (8.21) in (8.17), the minimizer of the KL-divergence satisfies 

**==> picture [248 x 44] intentionally omitted <==**

proving that it is the MLE. 

8 Estimation in the Presence of Hidden Variables 

184 

## _**8.1.3 EM Algorithm**_ 

The EM algorithm (expectation maximization algorithm) is an iterative algorithm for obtaining the MLE in a model including hidden variables. It was formulated by Dempster et al. (1977). We show its geometry due to Csiszár and Tusnady (1984), also by Amari et al. (1992), Byrne (1992) and Amari (1995). It is an application of the _em_ algorithmfromthegeometricalpointofview.Webeginwith _**ξ**_ 0 asaninitialparameter, and _e_ -project it to _D_ to obtain the conditional distribution _q(_ _**h**_ | _**y** )_ = _p_ _**h**_ | _**y**_ ; _**ξ**_ 0 . This determines a candidate for the observed distribution in _D_ . We calculate the conditional expectation of log likelihood to evaluate the likelihood of a new candidate _**ξ**_ , given by 

**==> picture [273 x 26] intentionally omitted <==**

for observed data _**y**_ 1 _, . . . ,_ _**y** N_ . This is called the E-step, because it calculates the conditional expectation. This is the _e_ -projection of _p_ _**y** ,_ _**R** ,_ _**ξ**_ 0 to _D_ . 

We then _m_ -project the new candidate in _D_ to _M_ , to obtain a new candidate _**ξ**_ 1 in _M_ . This is obtained by maximizing (8.23). It is called the M-step, because it is the maximization of the log likelihood (8.23). This is the _m_ -projection. We repeat the procedures. See Fig. 8.2 . 

It is easy to prove the following theorem. 

**Theorem 8.2** _The KL-divergence decreases monotonically by repeating the E-step and the M-step. Hence, the algorithm converges to an equilibrium._ 

It should be noted that the _m_ -projection is not necessarily unique unless _M_ is _e_ -flat. Hence, there might exist local minima. 

## _**8.1.4 Example: Gaussian Mixture**_ 

The parameters to be estimated are the weights _w_ 1 _, . . . , wk_ and the means _μ_ 1 _, . . . , μk_ of component Gaussian distributions, _**ξ**_ = _(wi , μi_ ; _i_ = 1 _, . . . , k)_ . We begin with 

**Fig. 8.2** EM algorithm 

185 

8.1 EM Algorithm 

initial _**ξ**_ 0, and let _**ξ**[t]_ = � _wi[t][,][ μ] i[t]_ � be the candidate at _t_ . The E-step is to _e_ -project _p(y, h_ ; _**ξ**[t] )_ to _D_ to obtain _qt (h_ | _y)_ . This is the same as that at _**ξ**[t]_ , 

**==> picture [269 x 28] intentionally omitted <==**

The conditional expectation is 

**==> picture [269 x 28] intentionally omitted <==**

up to a constant not depending on the parameters. 

The M-step is maximization ( _m_ -projection) searching for a new _**ξ**[t]_[+][1] that maximizes (8.25). By differentiating (8.25) and making it equal to 0, we easily obtain 

**==> picture [284 x 29] intentionally omitted <==**

## **8.2 Loss of Information by Data Reduction** 

Given original data _DX_ = { _**x**_ 1 _, . . . ,_ _**x** N_ }, assume that we summarize it to a statistic 

**==> picture [208 x 9] intentionally omitted <==**

and use it for estimation. Then, we consider an estimator _**ξ**_[ˆ] = _**ξ**_[ˆ] _(_ _**T** )_ , which is a function of _**T**_ . When _**T**_ is a sufficient statistic, there is no loss of information. Otherwise, summarizing the data in _**T**_ will cause loss of information, which is measured by using the Fisher information. When there is a hidden variable _**h**_ and we use _**T**_ = � _**y**_ 1 _, . . . ,_ _**y** N_ � for estimation, _**T**_ is not sufficient in general. We define the conditional Fisher information of the original data _DX_ conditioned on _**T**_ . When _**T**_ = _**t**_ , the probability distribution of _DX_ is given by the conditional probability _p(DX_ | _**t**_ ; _**ξ** )_ . Hence the Fisher information is given as 

**==> picture [277 x 13] intentionally omitted <==**

where E _X_ is the conditional expectation of _DX_ . Taking the average over _**t**_ , we have the conditional Fisher information 

**==> picture [217 x 15] intentionally omitted <==**

From the equality 

**==> picture [221 x 15] intentionally omitted <==**

186 

8 Estimation in the Presence of Hidden Variables 

where _gi j[X]_[,] _[ g] i j[T]_[,] _[ g] i j[X]_[|] _[T]_ are the Fisher information based on _DX ,_ _**T**_ and _DX_ conditionally on _**T**_ . The loss of Fisher information by summarizing data to statistics _**T**_ is given by 

**==> picture [206 x 15] intentionally omitted <==**

Oizumietal.(2011)studiedthelossofinformationinthecaseofspikesofneurons. Let _t_ firing patterns _**x**_ 1 _, . . . ,_ _**x** t_ of neurons be observed. These include firing rates of neurons, covariances of spikes of two neurons and higher-order correlations of a number of neurons. Since the brain reduces information in the process of decision making, it loses some information. Consider a curved exponential family 

**==> picture [230 x 10] intentionally omitted <==**

where _**X**_ = � _xi , xi x j , . . . , x_ 1 _. . . xn_ � and _**ξ**_ is a parameter to specify the probability distribution based on which _**x**_ is generated. When a multiple observation is possible, we have the sufficient statistic (observed point) 

**==> picture [198 x 22] intentionally omitted <==**

It includes all the information concerning firing rates, pairwise and higher-order interactions. An efficient estimator is obtained by _m_ -projecting it to model _M_ of which the coordinates are _**ξ**_ . 

When a part of _**η**_ ¯ is lost, for example higher-order correlations of spikes are lost, we cannot identify the observed point. We have instead an observed data submanifold _D_ . The optimum estimator is the minimizer of _DK L_ [ _D_ : _M_ ]. The amount of loss of information is calculated when correlational information is lost (Oizumi et al. 2011). 

## **8.3 Estimation Based on Misspecified Statistical Model** 

When the true statistical model _M_ = { _p(_ _**x** ,_ _**ξ** )_ } is very complicated, we are apt to use a simplified model _Mq_ = { _q(_ _**x** ,_ _**ξ** )_ } to estimate parameter _**ξ**_ . This is a misspecified model. What is the loss of information by using a misspecified model? We begin with a simple example for illustration of the problem. Assume that _n_ neurons are arranged in a one-dimensional neural field. When a stimulus is applied at position _u_ , 0 _< u <_ 1, the neuron corresponding to that position and neighboring neurons are activated. When the _i_ th neuron corresponds to position 

**==> picture [182 x 21] intentionally omitted <==**

it is excited strongly, and neighboring neurons are also excited. We assume that, for an arbitrary _j_ , the response of neuron _j_ is _r j (u)_ when a stimulus is applied at _u_ . The 

8.3 Estimation Based on Misspecified Statistical Model 

187 

**Fig. 8.3** Tuning _curve_ of 

**==> picture [259 x 122] intentionally omitted <==**

curve _r j (u)_ is called the tuning curve of neuron _j_ . See Fig. 8.3. We assume that _xi_ is the firing rate of neuron _i_ subject to a Gaussian distribution of which the mean is _ri (u)_ and the covariance matrix is _V_ = � _Vi j_ �. Then, the statistical model of excitation is 

**==> picture [272 x 24] intentionally omitted <==**

Consider a simpler model having the same tuning curves but no correlations, 

**==> picture [263 x 25] intentionally omitted <==**

Wu et al. (2002) showed that there is asymptotically no loss of information even if we use the simple misspecified model _Mq_ of (8.36). This is good news for the brain. 

We study a general case of a misspecified model to see its loss of information. We consider the case that both _p(_ _**x** ,_ _**u** )_ and _q(_ _**x** ,_ _**u** )_ are curved exponential families lying in a larger exponential family _S_ . The observed point _**η**_ ¯ is asymptotically subject to the Gaussian distribution with mean _**η** (_ _**u** )_ in the true model _M_ and covariance matrix **G** { _**η** (_ _**u** )_ } _/N_ when the true distribution is _p(_ _**x** ,_ _**u** )_ . The maximum likelihood estimator using model _Mq_ = { _q(_ _**x** ,_ _**u** )_ } is called the _q_ -MLE. The _q_ -MLE is obtained by _m_ -projecting the observed point to _Mq_ by using the _q_ -ancillary family _Aq (_ _**u** )_ , which is an _m_ -flat submanifold of _S_ passing through _q(_ _**x** ,_ _**u** )_ and orthogonal to the tangent space of _Mq_ at _**u**_ . Since the observed point converges to _**η** (_ _**u** )_ as _N_ tends to infinity, the _q_ -MLE is consistent when the _q_ -ancillary family passing through _q(_ _**x** ,_ _**u** )_ passes through _p(_ _**x** ,_ _**u** )_ ∈ _M_ . See Fig. 8.4. 

**Theorem 8.3** _The q-MLE is consistent when and only when_ 

**==> picture [251 x 22] intentionally omitted <==**

_which holds when the q-ancillary family Aq (_ _**u** ) passes through p(_ _**x** ,_ _**u** )_ ∈ _M._ 

8 Estimation in the Presence of Hidden Variables 

188 

**Fig. 8.4** q-auxiliary family and q-MLE 

_Proof_ Let 

**==> picture [245 x 10] intentionally omitted <==**

be the _m_ -geodesic connecting _q(_ _**x** ,_ _**u** )_ and _p(_ _**x** ,_ _**u** )_ . Its tangent vector at _Mq_ is 

**==> picture [283 x 25] intentionally omitted <==**

It is orthogonal to the tangent vectors 

**==> picture [208 x 22] intentionally omitted <==**

of _Mq_ , when ⟨˙ _r , l_[˙] _q_ ⟩ _q_ = 0, which is calculated as 

**==> picture [269 x 49] intentionally omitted <==**

This implies that (8.37) holds and vice versa. 

**==> picture [9 x 7] intentionally omitted <==**

The _q_ -MLE estimator is Fisher efficient when the _m_ -geodesic connecting _q(_ _**x** ,_ _**u** )_ and _p(_ _**x** ,_ _**u** )_ is orthogonal to both _M_ and _Mq_ , because the ancillary submanifold observed _Aq (_ _**u** )_ and the true ancillary submanifold _**η**_ ¯ is mapped to the same _**u**_ ˆ in both _A(_ _**u** M)_ of the true MLE coincide. Hence, theand _Mq_ by the _m_ -projection. When _Aq (_ _**u** )_ is not orthogonal to _M_ , there is information loss. This is easily evaluated from the angles of the _q_ -ancillary submanifold _Aq (_ _**u** )_ and _M_ . 

8.3 Estimation Based on Misspecified Statistical Model 

189 

**Theorem 8.4** _The q-MLE estimator is Fisher efficient when the q-ancillary family is orthogonal to M. When it is not orthogonal, the loss of Fisher information is given by_ 

**==> picture [232 x 12] intentionally omitted <==**

_where v[κ] is the transversal coordinate system in Aq (_ _**u** )._ 

_Proof_ By using the _q_ -ancillary family, we can map the observed point _**η**_ ¯ to _Mq_ . This is efficient when and only when _Aq (_ _**u** )_ is orthogonal to the tangent space of _M_ . Otherwise, there is information loss. By using the _(_ _**u** ,_ _**v** )_ -coordinates, where _**u**_ = _(u[a] )_ and _**v**_ = _(v[κ] )_ are the coordinates along the ancillary family _Aq (_ _**u** )_ , the _q_ -MLE is mapped through it, but this is a non-orthogonal mapping to _M_ . Hence, loss of information occurs, as is given in (7.58) or (8.42). 

_Remark_ When the _q_ -ancillary family _Aq (_ _**u** )_ does not pass _p(_ _**x** ,_ _**u** )_ , the _q_ -estimator is not consistent. However, when this does not hold, let _**f** (_ _**u** )_ be the coordinates of _M_ at which _Aq (_ _**u** )_ intersects _M_ . If we reparameterize _Mq_ such that the new parameter of _Mq_ is _**f**_[−][1] _(_ _**u** )_ , then the consistency always holds. 

## **Remarks** 

The present short chapter introduces statistical models which are different from a regular model. One is a model with hidden variables, in which some random variables are not observed. The EM algorithm is known in such a model. From the geometrical point of view, it is nothing other than the _em_ algorithm, which minimizes the divergence between the model manifold _M_ and data manifold _D_ derived from observed data. This is now a standard method in machine learning. When it was proposed by Csiszár and Tusnady (1984), the paper was rejected by a journal because the reviewer did not admit computationally heavy iterative procedures (I. Csiszár, personal communication). So this remains a conference paper. 

Another model is a misspecified model. Its performance is easily understood from geometry, so that it is a good example to show the power of information geometry. The brain might use a misspecified or unfaithful statistical model for decoding information, because the true model is often unknown or too complicated. Therefore, we need to know the performance of the misspecified model. Oizumi et al. (2015) use a misspecified model to evaluate the amount of integrated information to measure the degree of consciousness. 

## **Chapter 9 Neyman-Scott Problem: Estimating Function and Semiparametric Statistical Model** 

The present chapter studies the famous Neyman–Scott problem, where the number of unknown parameters increases in proportion to the number of observations. The problem gave a shock to the statistics community, because the MLE is not necessarily asymptotically consistent or efficient in this problem. We solve the problem by constructing information geometry of estimating functions. The problem is reformulated in the framework of a semiparametric statistical model, which includes a finite number of parameters of interest and a nuisance parameter of function degrees of freedom. The problem uses a function space but we apply an intuitive description, sacrifying mathematical justification. The results are useful for solving both the semiparametric and Neyman–Scott problems. 

## **9.1 Statistical Model Including Nuisance Parameters** 

Let us consider a statistical model 

**==> picture [202 x 10] intentionally omitted <==**

which includes two types of parameters. One is a parameter which we want to estimate, denoted by _**u**_ . This is called the parameter of interest. The other, denoted by _**v**_ , is a parameter the value of which is of no concern to us. It is called a nuisance parameter. We give two examples. 

**1. Measurement under Gaussian noise:scale problem** : Let us measure the weight of a specimen repeatedly by using a scale. The true weight is _μ_ but measurements _x_ 1 _, . . . , x N_ are independent random Gaussian variables with mean _μ_ and variance _σ_[2] , where _σ_[2] represents the accuracy of the scale. When we have interest in estimating 

The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_9 

191 

9 Neyman-Scott Problem: Estimating Function _. . ._ 

192 

_μ_ but do not care about _σ_[2] , _μ_ is the parameter of interest and _σ_[2] is the nuisance parameter. When we are interested in knowing the accuracy _σ_[2] of the scale but do not care about _μ_ , _σ_[2] is the parameter of interest and _μ_ the nuisance parameter. 

**2. Coefficient of proportionality** : We consider a pair _(x, y)_ of Gaussian random variables, where _x_ and _y_ represent the volume and the weight of a specimen, respectively. Here, _x_ is a noisy observation of the volume _v_ of the specimen and _y_ is the noisy observation of its weight _uv_ , where _u_ is the specific gravity of the specimen. We assume that the noises are independent and Gaussian with mean 0 and variance 1. Then, their joint distribution is specified by 

**==> picture [227 x 10] intentionally omitted <==**

When we are interested only in specific gravity _u_ , i.e., the coefficient of proportionality, but do not care about _v_ , _u_ is the parameter of interest and _v_ is the nuisance parameter. The joint probability is written as 

**==> picture [278 x 25] intentionally omitted <==**

The problem is easy, because given observed data _D_ = { _(x_ 1 _, y_ 1 _) , . . . , (x N , yN )_ }, we can use the MLE to estimate _u_ and _v_ and simply discard the estimator _v_ ˆ of the nuisance parameter. Since MLE � _u_ ˆ _,_ ˆ _v_ � is efficient, the estimator _u_ ˆ is efficient. 

Let the Fisher information matrix in the model (9.1) of all the parameters _**ξ**_ = _(_ _**u** ,_ _**v** )_ be _gαβ_ , where we use suffixes _α, β_ for the entire _**ξ**_ = _(ξ[α] ) , a, b, c, . . ._ for the parameter _**u**_ = _(u[a] )_ of interest and _κ, λ, μ, . . ._ for the nuisance parameter _**v**_ = _(v[κ] )_ . The Fisher information matrix is partitioned as 

**==> picture [204 x 25] intentionally omitted <==**

where, by putting _l_ = log _p_ , 

**==> picture [239 x 25] intentionally omitted <==**

**==> picture [239 x 11] intentionally omitted <==**

ˆ The asymptotic error covariance of the entire estimator _**ξ**_[ˆ] = � _**u** ,_ ˆ _**v**_ � is given by using its inverse as 

**==> picture [240 x 22] intentionally omitted <==**

The inverse of the Fisher information matrix is also partitioned as 

**==> picture [205 x 25] intentionally omitted <==**

9.1 Statistical Model Including Nuisance Parameters 

193 

where its _(a, b)_ -part � _g[ab]_[�] is not the inverse of the _(a, b)_ -part _(gab)_ of � _gαβ_ �. It is the _(a, b)_ -part of the inverse � _g[αβ]_[�] of � _gαβ_ �. The two are different and � _g[ab]_[�] is given by the inverse of 

**==> picture [214 x 12] intentionally omitted <==**

as is clear from the inversion of a partitioned matrix. We have 

**==> picture [193 x 10] intentionally omitted <==**

in the sense of a positive-definite matrix, which means that information is lost in the presence of unknown nuisance parameter _**v**_ . This is because, when _**v**_ is known, the Fisher information is _(gab)_ . Since the covariance of the estimation error, when _**v**_ is unknown, is asymptotically 

**==> picture [236 x 22] intentionally omitted <==**

_(g_ ¯ _ab)_ is called the efficient Fisher information matrix. The tangent vectors _**e** a_ and _**e** κ_ along the _**u**_ and _**v**_ coordinate axes are represented by score functions 

**==> picture [253 x 10] intentionally omitted <==**

Let us project _**e** a_ to the space orthogonal to the subspace spanned by _**e** κ_ (Fig. 9.1). Then, the projected vector is given by 

**==> picture [208 x 12] intentionally omitted <==**

**Fig. 9.1** Efficient score _**e**_ ¯ _a_ in the presence of nuisance parameter 

**==> picture [171 x 162] intentionally omitted <==**

Neyman-Scott Problem: Estimating Function _. . ._ 

194 

9 

or, in terms of the score functions, 

**==> picture [250 x 12] intentionally omitted <==**

This is called the efficient score, because the efficient Fisher information matrix is 

**==> picture [225 x 13] intentionally omitted <==**

This shows that only the part orthogonal to the nuisance direction is effective, keeping information for estimating _**u**_ , and the part in the nuisance direction is useless, because _**v**_ is unknown. 

When the subspace spanned by the scores of the parameter of interest is orthogonal to the nuisance parameters, we have _gaκ_ = 0. In this case, 

**==> picture [186 x 10] intentionally omitted <==**

holds, so there is asymptotically no loss of information. Therefore, it is desirable to choose the nuisance parameters such that the orthogonality holds. Given a statistical model _M_ = { _p(_ _**x** ,_ _**u** ,_ _**v** )_ }, we consider the problem of reparameterizing _**v**_ depending on _**u**_ as 

**==> picture [193 x 10] intentionally omitted <==**

such that 

**==> picture [252 x 13] intentionally omitted <==**

This is in general impossible (see p. 254 in Amari 1985). However, when _**u**_ is a scalar parameter, it is always possible. 

## **9.2 Neyman–Scott Problem and Semiparametrics** 

Neyman and Scott (1948) presented a class of statistical problems and questioned the validity of the MLE, by showing that the asymptotic consistency and efficiency of the MLE are not guaranteed in some of their models. Let _M_ = { _p(_ _**x** ,_ _**u** ,_ _**v** )_ } be a statistical model and let _**x**_ 1 _, . . . ,_ _**x** N_ be _N_ independent observations. The value of _**u**_ (the parameter of interest) is kept the same (unknown) throughout the observations, but _**v**_ changes each time. Hence, _**x** i_ is subject to _p(_ _**x** ,_ _**u** ,_ _**v** i )_ . This is the Neyman–Scott problem and there are many examples of this type. 

The estimation of the radius of the stone circle, Stonehenge in England, is a well-known romantic problem of this type. The stones are supposed to have been arranged in a circle to start with, but their positions have been disturbed in their long history. See Fig. 9.2. The radius _u_ of the stone circle is the parameter of interest, and the declination angle of the _i_ th stones _vi_ is the nuisance parameter. We show later another problem of estimating the shape parameter from neural spikes under 

195 

9.2 Neyman–Scott Problem and Semiparametrics 

**Fig. 9.2** Location of the _i_ th stone 

**==> picture [278 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
stone i<br>vi<br>.<br>u=r<br>**----- End of picture text -----**<br>


changing firing rates. Independent component analysis, treated in Chap. 13, is also of this type. There are similar problems in computer vision (Kanatani 1998; Okatani and Deguchi 2009). 

We use the problem of the coefficient of proportionality as a working example. It consists of _N_ independent observations _(xi , yi ) , i_ = 1 _, . . . , N_ , subject to 

**==> picture [227 x 12] intentionally omitted <==**

where _εi_ and _εi_[′][are independent noises subject to Gaussian distributions with mean] 0 and common variance _σ_[2] . We assume that _σ_[2] is known. The joint probability distribution of _(xi , yi )_ is 

**==> picture [297 x 26] intentionally omitted <==**

Here, _u_ and _vi_ , are scalar parameters. 

Figure 9.3a shows an example of observed data and the problem is to draw a regression line to fit the data. The problem looks very simple, but is not. We show a number of intuitive solutions to this problem. 

**==> picture [420 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b) (c)<br>y y<br>y<br>y = ux y = ux y = ux<br>x x x<br>**----- End of picture text -----**<br>


**Fig. 9.3** Coefficient of proportionality: **a** Observed data; **b** least squares; **c** total least squares 

196 

Neyman-Scott Problem: Estimating Function _. . ._ 

9 

## **1. Least squares solution** 

The least squares solution is the minimizer of 

**==> picture [214 x 22] intentionally omitted <==**

which is the sum of the squares of vertical errors to the regression line (Fig. 9.3b). The solution is 

**==> picture [193 x 26] intentionally omitted <==**

However, this is a bad solution. It is not consistent even asymptotically and it does not converge to the correct _u_ even when _N_ increases to become infinitely large. 

## **2. Averaging method** 

ˆ Let _ui_ = _yi /xi_ be the ratio obtained from one specimen. Their average 

**==> picture [195 x 22] intentionally omitted <==**

gives a consistent estimator. This is better than the least squares solution but is not so good in general. 

## **3. Gross average method** 

Let us sum up all _xi_ and all _yi_ separately. Then calculate their ratio, 

**==> picture [189 x 25] intentionally omitted <==**

This is a good consistent estimator. It is of interest to know how good it is. 

## **4. Total least square solution** 

Instead of minimizing the vertical errors in the least squares solution, we minimize the square of the lengths of orthogonal projection to the regression line (Fig. 9.3c). This is called the total least squares (TLS) solution. It is given by solving 

**==> picture [227 x 15] intentionally omitted <==**

## **5. MLE** 

We estimate all the parameters _u, v_ 1 _, . . . , vN_ , jointly by maximizing the likelihood, and we disregard all _v_ ˆ _i_ , keeping _u_ ˆ only. This is the MLE. We can prove that this is identical with the TLS solution. 

We use a semiparametric formulation of the Neyman–Scott problem. Since the sequence _**v**_ 1 _, . . . ,_ _**v** N_ is arbitrary and unknown, we assume that it is generated from an unknown probability distribution _k(_ _**v** )_ . In order to generate the _i_ th example _**x** i_ ( _(xi , yi )_ in the above example), Nature chooses _**v** i_ from distribution _k(_ _**v** )_ . Then, _**x** i_ 

9.2 Neyman–Scott Problem and Semiparametrics 

197 

is chosen from _p (_ _**x** ,_ _**u** ,_ _**v** i )_ . Thus, each _**x** i_ is subject to one and the same probability distribution 

**==> picture [235 x 23] intentionally omitted <==**

We treat an extended statistical model 

**==> picture [205 x 12] intentionally omitted <==**

which includes two parameters: One is _**u**_ , the parameter of interest, and the other is a function _k(_ _**v** )_ . Each observation is independently and identically distributed (iid) in this setting, but the underlying model includes the nuisance parameter _k_ of function degrees of freedom. Such a model is called a semiparametric statistical model (Begun et al. 1983). We study the problem under this formulation. 

## **9.3 Estimating Function** 

An estimating function is a generalization of the score function which is the derivative of the log likelihood and is used to obtain the ML estimator. It is particularly convenient for a model having a nuisance parameter. For a statistical model _M_ = { _p(_ _**x** ,_ _**u** ,_ _**v** )_ }, we consider a differentiable function _f (_ _**x** ,_ _**u** )_ which does not depend on _**v**_ . Here, we treat the case where _**u**_ and _**v**_ are scalar parameters for simplicity, but it is easy to generalize it to the case with vector _**u**_ and vector _**v**_ . 

A function _f (_ _**x** , u)_ is called an estimating function, or more precisely an unbiased estimating function, when 

**==> picture [229 x 26] intentionally omitted <==**

hold for any _v_ , where E _u,v_ is the expectation with respect to _p(_ _**x** , u, v)_ . See Godambe (1991). We further assume 

**==> picture [209 x 13] intentionally omitted <==**

where _f_[′] is the derivative with respect to _u_ . An estimating function of _M_ satisfies 

**==> picture [279 x 13] intentionally omitted <==**

for an arbitrary function _k(v)_ , when a statistical model _M_ is extended to a semiparametric model _M_[˜] in (9.28). This is because _pK (_ _**x** , u, k)_ is a linear mixture of _p(_ _**x** , u, v)_ with mixing distribution _k(v)_ . 

9 Neyman-Scott Problem: Estimating Function _. . ._ 

198 

The law of large numbers guarantees that the arithmetic mean of _f (_ _**x** i , u)_ over the observed data converges to its expectation. Hence, because of (9.29), the solution of 

**==> picture [207 x 22] intentionally omitted <==**

will give a good estimator; (9.33) is called an estimating equation. In the case of a statistical model without a nuisance parameter, the score function 

**==> picture [217 x 22] intentionally omitted <==**

satisfies (9.29), so it is an estimating function. In this case, (9.33) is the likelihood equation and the derived estimator is the MLE. 

We analyze the asymptotic behavior of the estimator derived from an estimating function. 

**Theorem 9.1** _The estimator_ ˆ _u derived from an estimating function f (_ _**x** , u) is asymptotically unbiased and its error covariance is given asymptotically by_ 

**==> picture [243 x 27] intentionally omitted <==**

_when u_ 0 _is the true parameter._ 

_Proof_ The proof is given by a similar method as the asymptotic analysis of MLE. We expand the left-hand side of (9.33) at _u_ 0, 

**==> picture [277 x 51] intentionally omitted <==**

The first term in the right-hand side converges, due to the central limit theorem, to a Gaussian random variable _ε_ with mean 0 and variance 

**==> picture [212 x 13] intentionally omitted <==**

The last term of (9.36) converges, due to the law of large numbers, to ~~√~~ _N A_ , where 

**==> picture [213 x 12] intentionally omitted <==**

Hence, we have 

**==> picture [203 x 24] intentionally omitted <==**

9.3 Estimating Function 

199 

□ 

from which we have (9.35). 

An estimating function gives an unbiased estimator of which the error covariance converges to 0 in the order of 1 _/N_ . However, there is no guarantee that an estimating function really exists. When does it exist? If there are many estimating functions, how should we choose a good one? These are questions we should address. We use information geometry in answering these questions. 

Although we explain the scalar parameter case, our method holds in the vector case. When the parameter _**u**_ of interest is vector-valued, an estimating function _**f** (_ _**x** ,_ _**u** )_ is vector-valued, having the same dimensions as _**u**_ . An _**f** (_ _**x** ,_ _**u** )_ is an (unbiased) estimating function when it satisfies 

**==> picture [231 x 25] intentionally omitted <==**

and also the matrix 

**==> picture [215 x 25] intentionally omitted <==**

is non-degenerate. The estimating equation is a vector equation 

**==> picture [203 x 15] intentionally omitted <==**

The resulting estimator is asymptotically unbiased and Gaussian, having the asymptotic error covariance matrix 

**==> picture [305 x 22] intentionally omitted <==**

## **9.4 Information Geometry of Estimating Function** 

The statistical model _M_[˜] is parameterized by _u_ and _k(v)_ , the latter of which has function-degrees of freedom. So we are obliged to use intuitive treatment, not mathematically rigorously justified, but the results are useful. In the function space _F_ = { _p(_ _**x** )_ }, let us consider a submanifold _MU (k)_ obtained by fixing the mixing function _k(v)_ . It is one-dimensional, that is, it is a curve, having a scalar parameter _u_ . It is denoted by 

**==> picture [235 x 10] intentionally omitted <==**

**==> picture [236 x 10] intentionally omitted <==**

9 Neyman-Scott Problem: Estimating Function _. . ._ 

200 

**Fig. 9.4** Two submanifolds _MU (k)_ and _MK (u)_ and their tangent vectors 

**==> picture [130 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
M [~]<br>MK ( u )<br>.<br>l b l . u MUu ( k )<br>( u , k )<br>**----- End of picture text -----**<br>


where _u_ is fixed but the mixing _k(v)_ is free. One may consider that, for each _u_ , an infinite-dimensional _MK (u)_ is attached as a fiber. See Fig. 9.4. 

The tangent space at a point _(u, k)_ of _M_ ˜ is spanned by infinitesimally small deviations _δ pK (_ _**x** , u, k)_ of probability density _pK (_ _**x** , u, k)_ . By using the logarithmic expression, _lK (_ _**x** , u, k)_ = log _pK (_ _**x** , u, k)_ , we have 

**==> picture [226 x 24] intentionally omitted <==**

where 

**==> picture [214 x 10] intentionally omitted <==**

E _u,k_ being the expectation with respect to _pK (_ _**x** , u, k)_ . This shows that the tangent space _Tu,k_ at _(u, k)_ ∈ _M_[˜] is composed of random variables _r (_ _**x** )_ satisfying 

**==> picture [199 x 10] intentionally omitted <==**

We assume 

**==> picture [206 x 13] intentionally omitted <==**

and the inner product of two tangent vectors _r (_ _**x** )_ and _s(_ _**x** )_ are defined by 

**==> picture [216 x 11] intentionally omitted <==**

So the tangent space _Tu,k_ is a Hilbert space. An estimating function _f (_ _**x** , u)_ satisfies (9.48) at any _(u, k)_ , so it is a vector belonging to _Tu,k_ for any _k_ . 

The tangent vector along the _u_ -coordinate axis 

**==> picture [221 x 22] intentionally omitted <==**

9.4 Information Geometry of Estimating Function 

201 

satisfies (9.48). The one-dimensional subspace 

**==> picture [216 x 14] intentionally omitted <==**

composed of the _u_ -score vector _l_[˙] _u(_ _**x** , u, k)_ is called the tangent subspace of interest at _(u, k)_ . In order to define tangent vectors along the nuisance parameter _k(v)_ , we consider a curve in the function space of _k(v)_ , written as 

**==> picture [214 x 10] intentionally omitted <==**

where 

**==> picture [197 x 23] intentionally omitted <==**

because 

**==> picture [201 x 23] intentionally omitted <==**

There are infinitely many curves, each specified by _b(v)_ . The tangent vector along a curve (9.53) is defined by 

**==> picture [326 x 33] intentionally omitted <==**

Let us denote by _TK (u, k)_ the space spanned by the tangent vectors of all such curves, called the nuisance tangent subspace at _(u, k)_ . 

Note that there are tangent vectors not belonging to _TU_ and _TK_ , which are not included in the directions of change in _u_ or _k_ . We denote the subspace orthogonal to both of _TU_ and _TK_ by _TA_ , which we call an ancillary tangent subspace (Fig. 9.5). Then, the tangent space is decomposed as 

**==> picture [207 x 10] intentionally omitted <==**

at each point _(u, k)_ , where ⊕ implies the direct sum. _TA_ is orthogonal to _TU_ ⊕ _TK_ , but _TU_ and _TK_ are not orthogonal in general. 

We define _e_ -parallel transport and _m_ -parallel transport of a tangent vector _r (_ _**x** )_ along the nuisance submanifold _MK (u)_ . We consider a small change of log _pK (_ _**x** , u, k)_ in the direction _r (_ _**x** )_ , 

**==> picture [211 x 9] intentionally omitted <==**

where _ε_ is small. Since the _e_ -representation of _pK (_ _**x** , u, k)_ is _lK (_ _**x** , u, k)_ , it is natural to consider that _r (_ _**x** )_ is _e_ -parallelly transported from _k_ to _k_[′] without any change. But when _r (_ _**x** )_ ∈ _Tu,k_ , it does not belong to _Tu,k_[′] , because 

202 9 Neyman-Scott Problem: Estimating Function _. . ._ 

**Fig. 9.5** Decomposition of tangent space T _u,k TK Tu ,k TU_ ( _u_ , _k_ ) . _TA_ ; E _u,k_[′] [ _r (_ _**x** )_ ] ̸= 0 (9.59) in general. We subtract the average and define the _e_ -parallel transport of _r (_ _**x** )_ from _pK (_ _**x** , u, k)_ to _pK_ _**x** , u, k_[′] by _e[k]_[′] _k[r][(]_ _**[x]**[)]_[ =] _[ r][(]_ _**[x]**[)]_[ −][E] _[u][,][k]_[′][[] _[r][(]_ _**[x]**[)]_[]] _[,]_ (9.60) 

_e[k]_[′] 

where _k_[is the operator of the] _[ e]_[-parallel transport from] _[ k][(v)]_[ to] _[ k]_[′] _[(v)]_[ in] _[M][K][(][u][)]_[.] Obviously, 

**==> picture [213 x 37] intentionally omitted <==**

We next define the _m_ -parallel transport. Since the _m_ -representation of a deviation of _p(_ _**x** )_ is _δ p(_ _**x** )_ , it is natural to consider that _δ p(_ _**x** )_ does not change when it is transported in parallel from _k_ to _k_[′] . However, its _e_ -representation is 

**==> picture [211 x 24] intentionally omitted <==**

so its _e_ -representation changes at _k_[′] as _δ p(_ _**x** )/ pK_ _**x** , u, k_[′] . In order to compensate for this change, we define the _m_ -parallel transport of _r (_ _**x** )_ from _k_ to _k_[′] by 

**==> picture [225 x 29] intentionally omitted <==**

_m[k]_[′] 

where _k_[is the] _[ m]_[-parallel transport operator from] _[ k]_[to] _[ k]_[′][. It satisfies] 

9.4 Information Geometry of Estimating Function 

203 

**==> picture [213 x 37] intentionally omitted <==**

The two parallel transports are dual, as is shown in the following theorem. 

**Theorem 9.2** _The e- and m-parallel transports are dual, keeping the inner product invariant:_ 

**==> picture [251 x 33] intentionally omitted <==**

The proof is easy from the definitions (9.60) and (9.63). 

**Lemma** _The nuisance tangent space TK (u, k) is invariant under the m-parallel transport from k to k_[′] _, where u is fixed._ 

_Proof_ Since any tangent vector at _k_ is written in the form of (9.56) by using _b(v)_ , it is _m_ -parallelly transported to _k_[′] and is written in the same form by using the same _b(v)_ , where _k_ is replaced by _k_[′] . □ 

We can now characterize the estimating function in geometrical terms. 

**Theorem 9.3** _An estimating function is a tangent vector orthogonal to the nuisance tangent space and is invariant under the e-parallel transportation along MK (u). It includes a non-zero component in the tangent direction TU of the parameter of interest._ 

_Proof_ Because of (9.32), 

**==> picture [214 x 26] intentionally omitted <==**

holds so that it is invariant under the _e_ -parallel transport along the nuisance direction. Let us take a curve _k(v, t)_ and differentiate (9.32) with respect to _t_ . Then we have 

**==> picture [283 x 23] intentionally omitted <==**

Since the nuisance tangent space _TK_ is spanned by _l_[˙] _b_ , _f_ is orthogonal to all the nuisance tangent vectors. We next differentiate (9.32) with respect to _u_ . We then have 

**==> picture [250 x 14] intentionally omitted <==**

Since 

**==> picture [203 x 13] intentionally omitted <==**

_f_ should include a component in the direction _TU_ of interest. 

**==> picture [9 x 8] intentionally omitted <==**

9 Neyman-Scott Problem: Estimating Function _. . ._ 

204 

Consider the projection of the score vector _l_[˙] _u(_ _**x** , u, k)_ to the subspace orthogonal to the tangent space _TK_ of nuisance parameter and denote it by _l_[˙] _E (_ _**x** , u, k)_ . We call it the efficient score in _M_[˜] . Although it depends on _k(v)_ , it is an estimating function for any _k(v)_ when it is fixed. 

We construct the tangent nuisance space _TK (_ _**x** , u, k)_ in terms of the nuisance score 

**==> picture [229 x 22] intentionally omitted <==**

of _M_ . The tangent nuisance space _TK_ of _M_[˜] is spanned by the tangent vectors in the directions of _b(v)_ along the curve given by (9.53). Let 

**==> picture [211 x 22] intentionally omitted <==**

be the derivative of the delta function. Since _b(v)_ satisfies (9.54), any _b(v)_ is written as a weighted integration of _δw_[′] _[(v)]_[,] 

**==> picture [219 x 23] intentionally omitted <==**

where the weight is 

**==> picture [213 x 24] intentionally omitted <==**

Hence, the tangent vector in the direction of _b(v)_ = _δw_[′] _[(v)]_[ is written from (][9.56][) as] 

**==> picture [264 x 51] intentionally omitted <==**

by using the nuisance score _lv(_ _**x** , u, w)_ of _M_ . Thus, _TK_ at _k_ is spanned by the _m_ - parallel transports of the elementary tangent scores _lv(_ _**x** , u, w)_ for all _w_ and 

**==> picture [230 x 27] intentionally omitted <==**

The following theorem is immediate. 

**Theorem 9.4** _The nuisance tangent space is m-parallelly invariant,_ 

**==> picture [208 x 26] intentionally omitted <==**

205 

9.4 Information Geometry of Estimating Function 

_and spanned by the m-parallel transports of elementary nuisance scores l_[˙] _v(_ _**x** , u, w) for all w._ 

Let _f (_ _**x** , u)_ be an estimating function. It is _e_ -parallelly invariant and orthogonal to _TK_ . Therefore, because 

**==> picture [258 x 33] intentionally omitted <==**

it is orthogonal to the elementary nuisance _v_ -score _l_[˙] _v(_ _**x** , u, w)_ of _M_ for any _v_ = _w_ . In order to obtain the efficient scores in _M_[˜] , we consider the tangent vector in the direction of _u_ at a specific point _(u, δw)_ , where we put _k_ = _δw_ . Then, it is the same as the _u_ -score in _M_ , 

**==> picture [221 x 12] intentionally omitted <==**

We construct an efficient score from it, by making it orthogonal to _TK_ . Since _TK_ is spanned by all the elementary nuisance scores, we need to project _l_[˙] _u_ to the space orthogonal to all the _m_ -transports of _lv_ � _**x** , u, w_[′][�] from _δw_[′] to _δw_ for all _w_[′] . The projected˙ score is _e_ -invariant, so it is an estimating function. The efficient score _lE (_ _**x** , u, k)_ at _k_ is constructed by a linear combination with respect to _k(v)_ of these elementary efficient scores. 

We have the following theorem from this. 

**Theorem 9.5** _An estimating function exists when, and only when, the efficient score is non-zero. Any estimating function is written, using an arbitrary nuisance function k_ 0 _(v), in the form_ 

**==> picture [228 x 12] intentionally omitted <==**

_where an ancillary tangent vector a(_ _**x** )_ ∈ _TA,u,k_ 0 _depends on k_ 0 _._ 

_Proof_ It is easy to see that _a(_ _**x** )_ is orthogonal to both _TK_ and _TU_ . □ 

**Theorem 9.6** _Let pK (_ _**x** , u, k_ 0 _) be the true probability distribution. Then, the best estimating function is l_[˙] _E (x, u, k_ 0 _) and the asymptotic error covariance is_ 

**==> picture [222 x 31] intentionally omitted <==**

The theorem gives a bound on the asymptotic covariance of error. However, since the true _k_ 0 = _k(v)_ is unknown, we cannot use it. But _l_[˙] _E (_ _**x** , u, k_ 1 _)_ works well even _l_ for an approximate value˙ _E (_ _**x** , u, k_ 1 _)_ still gives a consistent estimator. _k_ 1 of _k_ 0. Even when _k_ 1 is quite different from the true one, 

_Remark_ A statistical model in the Neyman–Scott problem is linear in _k(v)_ , because it is a mixture model. The nuisance tangent space is invariant under the _m_ -parallel 

206 

Neyman-Scott Problem: Estimating Function _. . ._ 

9 

transportinsuchalinearmodel.However,ifwestudyageneralsemiparametricmodel where the probability density is not linear with respect to the nuisance function, the tangent nuisance spaces are not invariant by the _m_ -parallel transport. An estimation function is therefore required to be orthogonal to all the tangent nuisance scores at all _k_ . Hence, it is the projection of the _u_ -score vector to the subspace orthogonal to _m_ -transports of the nuisance subspace at all _k_[′] . This is called the information score at _k_ . See Amari and Kawanabe (1997). 

## **9.5 Solutions to Neyman–Scott Problems** 

## _**9.5.1 Estimating Function in the Exponential Case**_ 

We consider a typical case where _p(_ _**x** , u, v)_ is of the exponential type with respect to _v_ , that is, 

**==> picture [265 x 10] intentionally omitted <==**

where _s(_ _**x** , u)_ and _r (_ _**x** , u)_ are functions of _**x**_ and _u_ . 

**Lemma** _The u-score at k is given by_ 

**==> picture [271 x 13] intentionally omitted <==**

_where_ E[·| _s_ ] _is the conditional expectation conditioned on s._ 

_Proof_ We calculate the _u_ -score by differentiating the logarithm of (9.27) with respect to _u_ . By taking (9.81) into account, 

**==> picture [280 x 38] intentionally omitted <==**

where _s_[′] _, r_[′] and _ψ_[′] are derivatives of _s_ , _r_ and _ψ_ with respect to _u_ . Since _v_ is a random variable subject to _k(v)_ , we consider the joint probability of _v_ and _s(_ _**x** , u)_ . Then, we have the conditional distribution of _v_ conditioned on _s(_ _**x** , u)_ , 

**==> picture [307 x 25] intentionally omitted <==**

Hence, we have from (9.83) 

**==> picture [229 x 34] intentionally omitted <==**

9.5 Solutions to Neyman–Scott Problems 

207 

The tangent direction corresponding to a change of _k_ by _δk_ is written as 

**==> picture [241 x 26] intentionally omitted <==**

Hence, by putting _b(v)_ = _δ_[′] _w(v)_ and using (9.74), the tangent nuisance space is spanned by 

**==> picture [246 x 24] intentionally omitted <==**

for all _w_ , which corresponds to a change of _k(v)_ at _w_ . The score corresponding to a change _δk(v)_ in the nuisance function _k(v)_ is similarly written in the form of conditional expectation by using (9.84), 

**==> picture [225 x 25] intentionally omitted <==**

This is a function of _s(_ _**x** , u)_ . Hence, the nuisance subspace is generated by _s(_ _**x** , u)_ and is written as 

**==> picture [207 x 10] intentionally omitted <==**

by using an arbitrary function _h_ of _s_ . We finally have the following theorem. 

**Theorem 9.7** _The efficient score at k is given by_ 

**==> picture [298 x 14] intentionally omitted <==**

_Proof_ The efficient score is the projection of the score of interest to the subspace orthogonal to the nuisance tangent space. Since, for two random variables _s_ and _t_ , _t_ − E[ _t_ | _s_ ] is the projection of _t_ to the subspace orthogonal to the space generated by _s_ , we have the theorem. □ 

**Corollary** _When the derivative of s with respect to u is a function of s, we have_ 

**==> picture [234 x 13] intentionally omitted <==**

_Proof_ In this case, 

**==> picture [204 x 13] intentionally omitted <==**

which gives (9.91). Since (9.91) does not depend on _k_ , this gives the asymptotically optimal estimating function. □ 

9 Neyman-Scott Problem: Estimating Function _. . ._ 

208 

## _**9.5.2 Coefficient of Linear Dependence**_ 

After a long journey, we can now solve specific Neyman–Scott problems. The first is the problem of linear dependence. The problem stated in (9.20) is of the exponential type, so it is written in the form of (9.81), where 

**==> picture [219 x 35] intentionally omitted <==**

Since _r_ does not depend on _u_ , the efficient score is given as 

**==> picture [227 x 23] intentionally omitted <==**

We put 

**==> picture [224 x 10] intentionally omitted <==**

Then, we have a class of estimating functions written as 

**==> picture [228 x 10] intentionally omitted <==**

where _h_ is an arbitrary function. 

When the true nuisance function is _k_ , the best _h(s)_ is given by 

**==> picture [202 x 10] intentionally omitted <==**

which depends on the unknown _k_ . The point is that, even when we do not know _k_ , an estimating function in the class (9.97) gives a consistent estimator of which the error covariance decreases in proportion to 1 _/N_ . 

The TLS estimator is obtained by putting 

**==> picture [186 x 9] intentionally omitted <==**

The gross average estimator is obtained from 

**==> picture [186 x 9] intentionally omitted <==**

where _c_ is a constant. Let us consider a simple linear function 

**==> picture [195 x 10] intentionally omitted <==**

which will give a better estimator than the two above by choosing _c_ adequately. The estimating equation is 

9.5 Solutions to Neyman–Scott Problems 

209 

**==> picture [235 x 15] intentionally omitted <==**

Let _u_ ˆ _c_ be the solution of (9.102). Then we have 

**==> picture [322 x 57] intentionally omitted <==**

where 

**==> picture [232 x 22] intentionally omitted <==**

Therefore, the error is minimized by choosing 

**==> picture [198 x 25] intentionally omitted <==**

This shows that, when the distribution of _k(v)_ is wide-spread, the TLS is a good estimator, whereas, when the distribution of _k(v)_ is tight, the gross average estimator is better. 

## _**9.5.3 Scale Problem**_ 

There are two versions in the scale problem. One is to estimate the accuracy of a scale by using _N_ specimens. The other is to estimate the weight of a specimen by using _N_ scales of different accuracies. 

**1. Accuracy of a scale** : We prepare _N_ specimens of which weights _v_ 1 _, . . . , vN_ are different and unknown. Our aim is to estimate the error variance _σ_[2] of a scale. When the weight is _v_ and error variance is _σ_[2] , the measurement _x_ is a random variable subject to _N_ � _v, σ_[2][�] . We repeat measurements _m_ times for each specimen. Let _**x**_ = _(x_ 1 _, . . . , xm)_ be _m_ measurements by a specimen. The probability density of _**x**_ is 

**==> picture [252 x 26] intentionally omitted <==**

which can be rewritten as 

**==> picture [259 x 19] intentionally omitted <==**

9 Neyman-Scott Problem: Estimating Function _. . ._ 

210 

where we put 

**==> picture [211 x 22] intentionally omitted <==**

**==> picture [234 x 52] intentionally omitted <==**

Since 

**==> picture [207 x 22] intentionally omitted <==**

is a function of _s_ , the efficient score is 

**==> picture [218 x 14] intentionally omitted <==**

This is the orthogonal projection of _x_[¯][2] to the subspace orthogonal to ¯ _x_ . The estimating function is 

**==> picture [245 x 25] intentionally omitted <==**

which does not include _k_ . Hence, this gives an efficient estimator, 

**==> picture [233 x 50] intentionally omitted <==**

This is the best estimator different from the MLE. When the numbers _mi_ of measurements are different, we can solve the problem in a similar way. 

**2. Weight of a specimen by using** _N_ **scales** : We next consider the case in which we have _N_ scales having different unknown error covariances. In this case, we have only one specimen, the weight of which we want to know. We measure its weight _m_ times by using each scale. In this case, we put 

**==> picture [204 x 25] intentionally omitted <==**

so, for one scale, the probability density is 

**==> picture [253 x 19] intentionally omitted <==**

9.5 Solutions to Neyman–Scott Problems 

211 

In this case, we have 

**==> picture [265 x 30] intentionally omitted <==**

**==> picture [265 x 9] intentionally omitted <==**

We can check that _s_[′] is orthogonal to _s_ , so the efficient score is 

**==> picture [217 x 12] intentionally omitted <==**

where _h_ is an arbitrary function. If we fix _h(s)_ , then the estimator is 

**==> picture [201 x 25] intentionally omitted <==**

The optimum _h_ depends on the unknown _k(v)_ , 

**==> picture [198 x 10] intentionally omitted <==**

but any _h_ will give an asymptotically consistent estimator. It is a surprise that this simple problem has such a complicated structure. 

## _**9.5.4 Temporal Firing Pattern of Single Neuron**_ 

Let us consider a single neuron which fires stochastically. We assume that it fires at time _t_ 1 _, t_ 2 _, . . . , tn_ +1, which are random variables. The intervals of spikes are 

**==> picture [227 x 10] intentionally omitted <==**

Obviously, when the firing rate is high, the interval is short. The simplest model of a temporal firing pattern is that all _Ti_ are independent, subject to the exponential distribution 

**==> picture [217 x 10] intentionally omitted <==**

where _v_ is the firing rate. The number of spikes is subject to the Poisson distribution. However, _Ti_ are not independent in reality, because of the effect of refractoriness. It is known that the gamma distribution fits well, 

**==> picture [244 x 23] intentionally omitted <==**

9 Neyman-Scott Problem: Estimating Function _. . ._ 

212 

which includes another parameter _κ_ , called the shape parameter. We want to know _κ_ , which is the parameter of interest, so we put _u_ = _κ_ , whereas _v_ is the nuisance parameter. The average and variance of _Ti_ are 

**==> picture [225 x 22] intentionally omitted <==**

The parameter _κ_ represents the irregularity of spike intervals. When _κ_ is large, the spikes are emitted regularly and have almost the same intervals. When _κ_ = 1 _, Ti_ are independent, and when _κ_ is small, the irregularity increases. 

Given observed data { _T_ 1 _, . . . , Tn_ }, it is easy to estimate the parameters _κ_ and _v_ . This is a simple problem of estimation. However, in a real experimental situation, the firing rate _v_ changes over time but the shape parameter _κ_ is fixed, depending on the type of the neuron. So we regard _v_ as a nuisance parameter changing over time, while _κ_ is the parameter of interest. This is a typical Neyman–Scott problem. 

We assume that _v_ takes the same value for two consecutive times. (It can be _m_ consecutive times for _m_ ≥ 2, but we consider the simplest case.) So we collect two observations _T_ 2 _k_ −1 and _T_ 2 _k_ , and put them in a box. Hence, the _k_ th observation is _**T** k_ = _(T_ 2 _k_ −1 _, T_ 2 _k)_ . The two intervals _T_ 2 _k_ −1, _T_ 2 _k_ in a box are subject to the same distribution 

**==> picture [232 x 29] intentionally omitted <==**

where _vk_ may change arbitrarily in each box. We calculate the _u_ -score and _v_ -score as 

**==> picture [290 x 23] intentionally omitted <==**

The efficient score is obtained in this case after calculations (see Miura et al. 2006) as 

where 

**==> picture [306 x 60] intentionally omitted <==**

is the di-gamma function. Since this does not include _v_ , it is the best estimating function, and the estimating equation is 

**==> picture [206 x 15] intentionally omitted <==**

The statistics used in the estimating function is summarized as 

9.5 Solutions to Neyman–Scott Problems 

213 

**==> picture [241 x 27] intentionally omitted <==**

which includes all the information. 

Shinomoto et al. (2003) proposed to use another statistic: 

**==> picture [237 x 25] intentionally omitted <==**

Interestingly, the two statistics are derived from the same two consecutive time intervals, 

**==> picture [193 x 25] intentionally omitted <==**

The statistic in (9.132) is the geometric mean, whereas Shinomoto’s _L v_ is the arithmetic mean. From the point of the efficiency of estimation, _S_ is theoretically the best but _L v_ may be more robust. 

## **Remarks** 

The Neyman–Scott problem is an interesting estimation problem. It looks simple, but it is very difficult to obtain an optimal solution. Statisticians have struggled with this problem for many years, searching for the optimal solution. In 1984, when Sir David Cox visited Japan and talked about this problem as one of the interesting unsolved problems. I thought it a good challenge for information geometry. It would be wonderful if information geometry could provide a good answer to it. 

It is related to a more general semiparametric problem. Since we need a function space of infinite dimensions, it is difficult to construct a mathematically rigorous theory.Bickeletal.(1994)establishedarigoroustheoryofsemiparametricestimation by using functional analysis. Information geometry could be more transparent in understanding the structure of the Neyman–Scott problem. We were successful in obtaining a complete set of the estimating functions. 

The information-geometric theory is useful, even though the rigorous mathematical foundation is missing. It can solve many famous Neyman–Scott problems. When my official retirement time from the University of Tokyo was approaching, I thought that the results should be publicised even though they include mathematical flaw. So we submitted a paper to Bernoulli. The reviewers pointed out the lack of mathematical justification in the function space. However, the editor Ole Barndorff-Nielsen considered that this was an interesting and useful paper even without rigorous justification being given. So he decided that it was acceptable in the spirit of experimental mathematics, provided that the Theorem–Proof style of statements was replaced by the Proposition and Outline of Proof style. 

We did not have many good examples at that time. But later, we found many examples, including neural spike analysis and independent component analysis, the latter of which will be shown in Chap. 13. 

## **Chapter 10 Linear Systems and Time Series** 

A time series is a sequence of random variables _xt , t_ = _. . . ,_ −1 _,_ 0 _,_ 1 _,_ 2 _, . . ._ , which appears as a function of time. The present chapter deals with an ergodic time series which is generated by a linear system when white noise is applied to its input. We study the geometrical structure of the manifold of the time series. One may identify a time series with a linear system to generate it. Then, the geometry of the time series is identified with the geometry of linear systems, which is important for studying problems of control. For the sake of simplicity, we study only stable systems of discrete time, having one–input and one–output, but generalization is not difficult in principle. The set of all time series has infinite-dimensional degrees of freedom, so our treatment is intuitive and not mathematically rigorous, although it is well-founded in the case of finite-dimensional systems and related time series. 

## **10.1 Stationary Time Series and Linear System** 

Let us consider a time series { _xt_ }, where _t_ denotes discrete time, _t_ = 0 _,_ ±1 _,_ ±2 _, . . ._ . White Gaussian noise { _εt_ } is one of the simplest, which is composed of independent Gaussian random variables with mean 0 and variance 1, so that 

**==> picture [239 x 14] intentionally omitted <==**

We assume that the mean of _xt_ is equal to 0. A time series is stationary when the probability of { _xt_ } is the same as its time-shifted version { _xt_ + _τ_ } for any _τ_ . More strongly, we consider an ergodic time series. 

**Ergodic Theorem** : For an ergodic time series { _xt_ }, the temporal average of a function _f (xt )_ of _xt_ converges to the ensemble average with probability 1, 

215 

© Springer Japan 2016 

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_10 

216 

10 Linear Systems and Time Series 

**==> picture [194 x 8] intentionally omitted <==**

**Fig. 10.1** Linear system and generated time series 

**==> picture [248 x 30] intentionally omitted <==**

We consider a discrete time linear system, which transforms an input time series into an output time series linearly (Fig. 10.1). When the input is white Gaussian { _εt_ }, the output { _xt_ } is written as a linear combination of inputs, 

**==> picture [199 x 29] intentionally omitted <==**

A system is characterized by the sequence of parameters, 

**==> picture [210 x 10] intentionally omitted <==**

called the impulse responses of the system. It is assumed that 

**==> picture [177 x 13] intentionally omitted <==**

because 

**==> picture [200 x 29] intentionally omitted <==**

The output series is stationary when the input is. We introduce a time-shift operator _z_ by 

**==> picture [222 x 12] intentionally omitted <==**

Then, (10.3) is written as 

**==> picture [201 x 28] intentionally omitted <==**

By defining 

**==> picture [204 x 29] intentionally omitted <==**

the output is written as 

**==> picture [193 x 9] intentionally omitted <==**

10.1 Stationary Time Series and Linear System 

217 

_H (z)_ is called the transfer function of the system when it is considered as a function of a complex number _z_ , rather than the time shift operator. We assume that _H (z)_ is analytic in the region | _z_ | ≥ 1. 

We define the Fourier transform of an ergodic time series { _xt_ } in the wide sense by 

**==> picture [232 x 31] intentionally omitted <==**

Then, _X (ω)_ is a complex-valued random function of frequency _ω_ . Its absolute value 

**==> picture [199 x 12] intentionally omitted <==**

is called the power spectrum and is a deterministic function of _ω_ , but the phase of _X (ω)_ is random, uniformly distributed over [− _π, π_ ]. We assume 

**==> picture [217 x 24] intentionally omitted <==**

The power spectrum of { _xt_ } is written using the transfer function as 

**==> picture [206 x 15] intentionally omitted <==**

Conversely, given a time series { _xt_ } having power spectrum _S(ω)_ , we want to identify a system _H (z)_ . Such a system exists but is not unique. When _H (z)_ ̸= 0 outside the unit circle of _z_ (that is | _z_ | _>_ 1), such a system is uniquely determined. It is a system of minimal phase. Under this condition, there is one-to-one correspondence among the set of ergodic time series, the set of power spectra _S(ω)_ and the set of transfer functions _H (z)_ . They form an infinite-dimensional manifold _L_ . We will show their coordinates later. 

## **10.2 Typical Finite-Dimensional Manifolds of Time Series** 

We give typical examples of finite-dimensional systems or time series. 

## **1. AR model** 

An auto-regressive (AR) model is a time series generated from white noise { _εt_ } by 

**==> picture [238 x 29] intentionally omitted <==**

10 Linear Systems and Time Series 

218 

This is an AR model of degree _p_ , denoted by _AR( p)_ , where _xt_ is a linear combination (weighted sum) of past _p_ values _xt_ −1 _, . . . , xt_ − _p_ added to by a new Gaussian noise _εt_ called innovation. A system is specified by _p_ + 1 parameters _**a**_ = � _a_ 0 _, a_ 1 _, . . . , a p_ �. The transfer function is 

**==> picture [207 x 25] intentionally omitted <==**

and the power spectrum is 

**==> picture [218 x 32] intentionally omitted <==**

## **2. MA model** 

A moving-average (MA) model of degree _q_ is a time series generated from white noise by 

**==> picture [199 x 29] intentionally omitted <==**

where _**b**_ = � _b_ 1 _, . . . , bq_ � are the parameters. The present _xt_ is given by a weighted average of past _q_ noise values. Its transfer function and power spectrum are 

**==> picture [211 x 29] intentionally omitted <==**

**==> picture [210 x 21] intentionally omitted <==**

respectively. 

## **3. ARMA model** 

An ARMA model of degrees _( p, q)_ is the concatenation of AR and MA models, given by 

**==> picture [229 x 29] intentionally omitted <==**

Its transfer function and power spectrum are, respectively, given by 

**==> picture [220 x 57] intentionally omitted <==**

10.2 Typical Finite-Dimensional Manifolds of Time Series 

219 

The above three are of frequent use in time series analysis. The transfer functions are rational functions of _z_[−][1] . 

A continuous-time version of a linear system is used in control systems theory, where time _t_ is continuous and the time-shift operator _z_ is replaced by differential operator _s_ = _d/dt_ . The input–output relation of a system is described by 

**==> picture [201 x 10] intentionally omitted <==**

for input _u(t)_ . Information geometry gives a similar theory to it. 

## **10.3 Dual Geometry of System Manifold** 

We introduce a Riemannian metric and dually flat affine connections to the manifold _L_ of linear systems. Since _L_ is infinite-dimensional, our theory is intuitive. The Fourier transform _X (ω)_ of { _xt_ } gives complex-valued Gaussian random variables indexed by frequency _ω_ . We can prove that _X (ω)_ and _X_ � _ω_[′][�] are independent when _ω_ ̸= _ω_[′] so that we have 

**==> picture [244 x 25] intentionally omitted <==**

For complex random variable _X (ω)_ of (10.11), the phase is uniformly distributed. Therefore, we may write its probability density as 

**==> picture [262 x 26] intentionally omitted <==**

This is an exponential family, where random variables are _X (ω)_ and the natural parameter indexed by _ω_ is 

**==> picture [196 x 24] intentionally omitted <==**

This is _e_ -flat coordinates and the expectation parameter is 

**==> picture [241 x 22] intentionally omitted <==**

which is _m_ -flat coordinates. We rewrite the probability density in the form 

**==> picture [268 x 25] intentionally omitted <==**

10 Linear Systems and Time Series 

220 

Two dually coupled potential functions are 

**==> picture [311 x 50] intentionally omitted <==**

and they satisfy 

**==> picture [240 x 24] intentionally omitted <==**

The Riemannian metric is calculated from (10.30) by differentiation, 

**==> picture [231 x 25] intentionally omitted <==**

so that we have 

**==> picture [232 x 32] intentionally omitted <==**

This is diagonal and hence the squared length of deviation _δθ(ω)_ is written as 

**==> picture [241 x 24] intentionally omitted <==**

or in terms _S(ω)_ 

**==> picture [294 x 26] intentionally omitted <==**

Hence the metric is Euclidean. 

The KL-divergence between two systems is written, using their power spectra, as 

**==> picture [311 x 25] intentionally omitted <==**

The Shannon entropy is given by 

**==> picture [246 x 23] intentionally omitted <==**

We expand the _e_ -affine coordinates _S_[−][1] _(ω)_ in Fourier series as 

**==> picture [210 x 29] intentionally omitted <==**

10.3 Dual Geometry of System Manifold 

221 

and _m_ -affine coordinates _S(ω)_ as 

**==> picture [208 x 29] intentionally omitted <==**

where the basis functions are sinusoidal, 

**==> picture [260 x 9] intentionally omitted <==**

Since the resultant coefficients { _rt_ } and � _rt_[∗] � are linear transformations of _θ(ω)_ and _η(ω)_ , respectively, we can use them as new _θ_ - and _η_ -coordinates. It is known that the coefficients _rt_[∗][are expressed as] 

**==> picture [202 x 13] intentionally omitted <==**

which are called the auto-correlation coefficients. Hence, the _m_ -coordinates are the 

The inverse system of _H (z)_ is _H_[−][1] _(z)_ , which is obtained by reversing the input and the output. Its power spectrum is _S_[−][1] _(ω)_ . Hence, _rt_ are the auto-correlation coefficients of the inverse system. They are called the inverse auto-correlations. The inverse auto-correlations form _e_ -flat coordinate systems. 

It is noteworthy that _rt_ and _rs_[∗][are orthogonal,] 

**==> picture [192 x 11] intentionally omitted <==**

where _**e** t_ isthetangentvectorof _rt_ coordinateaxisand _**e**_[∗] _s_[isthatof] _[r] s_[∗][axis.Thisimplies] that _rs, s > k_ are parameters which are orthogonal to the auto-correlation coefficients _r_ 1[∗] _[, . . . ,][r] k_[∗][.][Hence,][they][represent][directions][orthogonal][to][the][auto-correlations][up] to _k_ . 

It is easy to introduce the _α_ -connection to _L_ by using the cubic tensor 

**==> picture [254 x 26] intentionally omitted <==**

We can prove the following theorem. 

**Theorem 10.1** _L is dually flat for any α, having the Euclidean metric. The α- divergence is given by_ 

**==> picture [319 x 47] intentionally omitted <==**

10 Linear Systems and Time Series 

222 

To prove the theorem, we introduce the _α_ -representation of the power spectrum as 

**==> picture [237 x 25] intentionally omitted <==**

Then, its Fourier coefficients are proved to be the _α_ -flat coordinates. The theorem shows that _L_ is like the manifold _**R**[n]_ +[of positive measure rather than the manifold] _Sn_ of probability distributions. 

We have two dually coupled affine coordinate systems 

**==> picture [211 x 26] intentionally omitted <==**

The _AR_ model of degree _p_ , _AR( p)_ , is characterized by 

**==> picture [204 x 13] intentionally omitted <==**

where _**r** p_ = � _r_ 0 _, r_ 1 _, . . . , r p_ �. It is defined by the linear constraints 

**==> picture [213 x 10] intentionally omitted <==**

in the _e_ -coordinates. Hence, it is an _e_ -flat submanifold. Moreover, the families of all AR models of various degrees form a hierarchical system, 

**==> picture [236 x 10] intentionally omitted <==**

The white noise _S(ω)_ = 1 belongs to _AR(_ 0 _)_ , having the coordinates _**r**_ = _(_ 1 _,_ 0 _,_ 0 _, . . .)_ . 

The _M A_ model of degree _q_ , _M A(q)_ , is characterized by 

**==> picture [208 x 13] intentionally omitted <==**

where _**r** q_[∗][=] � _r_ 0[∗] _[,][r]_ 1[∗] _[, . . . ,][r] q_[∗] �. It is defined by 

**==> picture [207 x 13] intentionally omitted <==**

in the _m_ -coordinate system. Hence, it is an _m_ -flat submanifold and the MA models of various degrees form a hierarchical system 

**==> picture [240 x 10] intentionally omitted <==**

10.4 Geometry of AR, MA and ARMA Models 

223 

## **10.4 Geometry of AR, MA and ARMA Models** 

**AR model** : An AR model of degree _p_ , _AR( p)_ , is a finite-dimensional model determined by _**a**_ in (10.15). By expanding the inverse of the its power spectrum _S(ω_ ; _**a** )_ , we have 

**==> picture [217 x 29] intentionally omitted <==**

The _m_ -affine coordinates of _AR( p)_ are the auto-correlation coefficients _**r**_ = ( _r_ 0 _, r_ 1 _, . . . , r p_ . However, the higher-order coefficients _r p_ +1 _, r p_ +2 _, . . ._ are not 0, although they are not free but determined by _**r**_ . Given a system with power spectrum _S(ω)_ having auto-correlations _r_ 0 _, r_ 1 _, r_ 2 _, . . ._ , we consider the system in _AR( p)_ of which the auto-correlations are the same as _S(ω)_ up to _r_ 1 _, . . . , r p_ and its higherdegree auto-correlations _r p_ +1 _, . . ._ are 0. It is called the _p_ -th order stochastic realization of _S(ω)_ . We denote its power spectrum by _Sp[AR][(][ω][)]_[. The set of systems having] the same auto-correlations up to _r_ 1 _, . . . , r p_ form an _m_ -flat submanifold, because they have the same values in the first _p m_ -coordinates but the others are free. We denote it by _M p(_ _**r** )_ . The _Sp[AR][(][ω][)]_[ is the intersection of the] _[ m]_[-flat submanifold] _[ M][p][(]_ _**[r]**[)]_[ and the] submanifold _AR( p)_ . The two submanifolds are orthogonal. Hence, _Sp[AR][(][ω][)]_[ is given] by the _m_ -projection of _S(ω)_ to _AR( p)_ . See Fig. 10.2. 

Let _S_ 0 _(ω)_ be white noise given by 

**==> picture [189 x 10] intentionally omitted <==**

It belongs to _AR( p)_ for any _p_ . From the Pythagorean theorem, we have 

**==> picture [268 x 14] intentionally omitted <==**

The stochastic realization is characterized by maximization of entropy. 

**Fig. 10.2** Stochastic realization of _S(ω)_ up to _p_ -th order auto-correlations 

10 Linear Systems and Time Series 

224 

**Theorem 10.2** (Maximum Entropy) _The stochastic realization Sp[AR][(][ω][)][ is the one] that maximizes entropy among all systems having the same_ _**r**_ = � _r_ 1 _, . . . , r p_ � _. Proof_ From (10.38), we have 

**==> picture [291 x 10] intentionally omitted <==**

From relation (10.57), we see that _Sp[AR]_ is the minimizer of _DK L_ � _S_ ˜ : _S_ 0� for all _S_ ˜ ∈ _M p(_ _**r** )_ . However, _DK L S_ ˜ : _S_ 0 is related to the negative of entropy _HS_ by � � 

**==> picture [319 x 14] intentionally omitted <==**

Hence, _Sp[AR]_ is the maximizer of entropy among all systems having the same _r_ 1 _, . . . , r p_ . □ 

**MA model** : Similar discussions hold for _M A(q)_ families. They are _m_ -flat and _M A(q)_ is defined by the constraint 

**==> picture [214 x 10] intentionally omitted <==**

We can define the dual stochastic realization of a system _S(ω)_ in _M A(q)_ , that is the system in _AR(q)_ of which the inverse auto-correlations _r_ 0[∗] _[,][r]_ 1[∗] _[, . . . ,][r] q_[∗][are the same] as the given _S(ω)_ up to _q_ . It is interesting to see the following minimum entropy theorem. 

**Theorem 10.3** (Minimum Entropy) _The dual stochastic realization Sq[M A] (ω) is the one that minimizes entropy among all systems having the same inverse autocovariances r_ 1[∗] _[, . . . ,][r] q_[∗] _[.]_ 

_Proof_ We have 

**==> picture [268 x 14] intentionally omitted <==**

from the Pythagorean theorem. Now we see 

**==> picture [223 x 10] intentionally omitted <==**

Hence minimizing _DK L_ [ _S_ 0 : _S_ ] is equivalent to minimizing entropy, proving the theorem. □ 

One may say that the Pythagorean relation or the projection theorem is more fundamental than the maximum entropy principle. 

**ARMA model** : The ARMA model of degrees _p, q_ is given by (10.21). This is a finite-dimensional subset of _L_ . They form a doubly hierarchical system. However, 

225 

10.4 Geometry of AR, MA and ARMA Models 

**==> picture [385 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
b<br>a<br>.<br>**----- End of picture text -----**<br>


**Fig. 10.3** Singularity of (1, 1) ARMA model 

they are neither _e_ -flat nor _m_ -flat. Moreover, the set is not a submanifold in the mathematical sense, because it includes singular points. We show this by a simple example. Consider _ARM A(_ 1 _,_ 1 _)_ , which is described by 

**==> picture [217 x 9] intentionally omitted <==**

Its transfer function is 

**==> picture [204 x 24] intentionally omitted <==**

The parameter _(a, b)_ plays the role of coordinates, where | _a_ | _<_ 1 _,_ | _b_ | _<_ 1 should be satisfied because of the stability of the system. However, on the diagonal line _a_ = _b_ , all the systems are equivalent, because the nominator and the denominator of (10.64) cancel one another out. Therefore, all the systems satisfying _a_ = _b_ are the same, simply given by _H (z)_ = 1. 

We reduce the equivalent systems to one point. Then, as is shown in Fig. 10.3, the set _AR(_ 1 _,_ 1 _)_ consists of two subsets (submanifolds) connected by one singular point. This type of reduction happens in any _ARM A( p, q)_ when the denominator and nominator of (10.22) include the same factor which cancels one another out. This fact is pointed out by Brockett (1976). We deal with such singularity later in Chap. 12 where multilayer perceptrons are discussed. 

## **Remarks** 

Linear systems and time series have long histories of research, having highly organized structures in their fields. Therefore, we only touch upon them from the information geometry point of view, not explaining details. Since we have used Gaussian white noise as inputs, our study includes only systems of minimal phase. We need 

226 

10 Linear Systems and Time Series 

non-Gaussian white noise to overcome this difficulty. Finite-dimensional time series and systems are well-founded mathematically, but if we want to treat infinitedimensional cases, we suffer from a lack of rigorous mathematical foundation. The difficulty is the same as in the case of a manifold of infinite-dimensional probability distributions. The present study will be a starting point for investigating information geometry of systems. See a trial by Ohara and Amari (1994). 

There is a statistical problem of estimation from observations of a finite size sample _x_ 1 _, x_ 2 _, . . . , xT_ of time series. We can identify the model which generates the sample by using an adequate degree of AR, MA and ARMA or many other models. The sample is not iid, but we can construct a similar theory of estimation. A higherorder asymptotic theory has been constructed. See Amari and Nagaoka (2000) and Taniguchi (1991) for more details. An AR model is an _e_ -flat manifold, provided we consider time series _xt_ of infinite length _t_ = 0 _,_ ±1 _,_ ±2 _, . . ._ . However, it is a curved exponential family when _x_ 0 _, x_ 1 _, . . . , xT_ only are observed, because of the effect of initial and final _xt_ ’s. See Ravishanker et al. (1990) and Martin (2000) for applications and Choi and Mullhaupt (2015) for recent developments using Khälerian geometry. 

It is interesting to see that an ARMA model includes singularities. Brockett (1976) pointed out that the set of linear systems of which transfer functions are rational functions, nominators with degree _p_ , and denominators with degree _q_ , are split in a number of disjoint components. This is a topological structure of the set of linear systems. When cancellation occurs, the degrees of the nominator and denominator decrease. R. Brockett excluded such low-degree systems from the set. However, a lower degree system is a special case of a higher degree system. Therefore, if we consider rational systems having a nominator degree lower or equal to _p_ and a denominator degree lower than or equal to _q_ , the set splits into multiple components where they are connected by singular points of reduced degrees. 

We have considered regular statistical models, which form a manifold. However, not a few important statistical models include this type of singularities. The behavior of an estimator when the true model lies at or close to singularities is interesting. See Fukumizu and Kuriki (2004). We study multilayer perceptrons in Chap. 12, considering how the singularity affects the dynamics of learning. 

We did not study multi-input and multi-output systems. The manifold of linear systems having _n_ inputs and _m_ outputs is a Grassman manifold. This is another interesting subject of research from the geometrical point of view. 

A Markov chain generates an infinite series of states 

**==> picture [222 x 9] intentionally omitted <==**

where _xt_ is a state from which _xt_ +1 is determined stochastically by a state transition matrix _p (xt_ +1 | _xt )_ . An AR model is regarded as a Markov chain. A Markov chain is an exponential family, so it is dually flat. We can construct a similar geometrical theory (Amari 2001). However, if we consider a finite range 0 ≤ _t_ ≤ _T_ of observations, a Markov chain { _xt_ }, 0 ≤ _t_ ≤ _T_ , is a curved exponential family because of the effects 

10.4 Geometry of AR, MA and ARMA Models 

227 

of initial and final values. Its _e_ -curvature decreases in the order of 1 _/T_ , converging to 0 as _T_ tends to infinity. See Amari (2001), and Hayashi and Watanabe (2014) for information geometry of Markov chains. Takeuchi (2014) used the _e_ -curvature to evaluate the asymptotic error of estimation, which is also related to the minimum regret of a Markov chain (Takeuchi et al. 2013). 

**Part IV Applications of Information Geometry** 

## **Chapter 11 Machine Learning** 

## **11.1 Clustering Patterns** 

Patterns are categorized into a number of classes. Pattern recognition is the problem of identifying the class to which a given pattern belongs. When a divergence is defined in the manifold of patterns, classification is brought into effect by using the divergence. We begin with the problem of obtaining a representative of a cluster of patterns, called the center of the cluster. When patterns are categorized into clusters, pattern recognition determines the cluster to which a given pattern is supposed to belong, based on the closeness due to the divergence. 

Another problem is to divide a non-labeled aggregate of patterns into a set of clusters. This is the problem of clustering. A generalized _k_ -means method is presented by using a divergence. The entire pattern space is divided into regions based on representatives of clusters. Such a division is called a divergence-based Voronoi diagram. When patterns are generated randomly subject to a probability distribution depending on each class, we have a stochastic version of the above problems. Information geometry is useful for understanding these problems in terms of divergence. 

## _**11.1.1 Pattern Space and Divergence**_ 

Let us consider patterns represented by vector _**x**_ . They belong to a pattern manifold _X_ . We study the case where a divergence _D_ _**x**_ : _**x**_[′] is defined between two patterns _**x**_ and _**x**_[′] . In a Euclidean space, we have 

**==> picture [228 x 24] intentionally omitted <==**

The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_11 

231 

11 Machine Learning 

232 

which is a half of the square of the Euclidean distance. We consider a general dually flat manifold induced by a Bregman divergence. For the sake of notational convenience, we suppose that pattern _**x**_ is represented in the dual affine coordinate system, so that it is represented by the _**η**_ -coordinates as 

**==> picture [181 x 10] intentionally omitted <==**

Then, we use the dual divergence between two patterns _**x**_ and _**x**_[′] 

**==> picture [268 x 13] intentionally omitted <==**

which is constructed from a dual convex function _φ_ . 

We will later use the primal affine coordinate system _**θ**_ given by the Legendre transformation 

**==> picture [216 x 25] intentionally omitted <==**

The primal convex function _ψ(_ _**θ** )_ is given by the Legendre relation 

**==> picture [216 x 25] intentionally omitted <==**

## _**11.1.2 Center of Cluster**_ 

Let _C_ be a cluster consisting of _k_ patterns _**x**_ 1 _, . . . ,_ _**x** k_ . We search for the representative of _C_ which should be as close to all the members of _C_ as possible (Fig. 11.1). To obtain such a representative, we calculate the average of the dual divergences from the members of the cluster to a point _**η**_ , as 

**==> picture [232 x 28] intentionally omitted <==**

**Fig. 11.1** _φ_ -center of cluster _C_ 

**==> picture [222 x 80] intentionally omitted <==**

**----- Start of picture text -----**<br>
C<br>. x 2<br>. x 1<br>. x 4 . x 5<br>. x 3 φ-center η c<br>.... xk<br>**----- End of picture text -----**<br>


11.1 Clustering Patterns 

233 

The minimizer of (11.7) is called the _φ_ -center of cluster _C_ due to the divergence _Dφ_ . If we use the _**θ**_ -coordinates, this is written as 

**==> picture [231 x 22] intentionally omitted <==**

where _**θ** i_ is the _**θ**_ -coordinates of _**η** i_ . The following theorem is due to Banerjee et al. (2005). 

**Theorem 11.1** _The φ-center of cluster C is given by_ 

**==> picture [197 x 22] intentionally omitted <==**

_for any φ._ 

_Proof_ By differentiating (11.7) with respect to _**η**_ and using (11.3), we have 

**==> picture [247 x 24] intentionally omitted <==**

where 

**==> picture [333 x 35] intentionally omitted <==**

We can generalize the situation that a probability distribution _p(_ _**x** )_ of _**x**_ is given instead of cluster _C_ . Then the center of the distribution is defined by the minimizer of 

**==> picture [236 x 23] intentionally omitted <==**

The center is merely the expectation of _**x**_ for any _φ_ , 

**==> picture [205 x 23] intentionally omitted <==**

## _**11.1.3 k-Means: Clustering Algorithm**_ 

Assume _N_ points _D_ = { _**x**_ 1 _, . . . ,_ _**x** N_ } are given, and we categorize them into _m_ clusters such that a cluster includes mutually close points. Let _C_ 1 _, . . . , Cm_ be clusters to be formed and let _**η** h, h_ = 1 _, . . . , m_ , be their centers. It is required that a point _**x** i_ belongs to cluster _Ch_ when the divergence _Dφ_ � _**x** i_ : _**η** h_ � is the smallest of _Dφ_ � _**x**_ : _**η**_ 1� _, . . . , Dφ_ � _**x**_ : _**η** m_ �. That is, _**η** h_ is the closest cluster center from _**x** i_ , 

**==> picture [219 x 19] intentionally omitted <==**

11 Machine Learning 

234 

Let 

**==> picture [238 x 23] intentionally omitted <==**

be the total sum of the divergences from each point _**x** i_ to the cluster center _**η** h_ it belongs to. The best clustering with respect to the _φ_ -divergence is the one that minimizes (11.15). We can apply the well-known _k_ -means algorithm, which is usually done by using the Euclidean distance. It is easy to extend it to the general case of a dually flat divergence, because the cluster center is given by the arithmetic mean in the dual coordinates. See Banerjee et al. (2005). 

## **Clustering Algorithm (** _k_ - **means method)** 

1. Initial Step: Choose _m_ cluster centers _**η**_ 1 _, . . . ,_ _**η** m_ arbitrarily such that they are all different. 

2. Classification Step: For each _**x** i_ , calculate the _φ_ -divergences to the _m_ cluster centers. Assign _**x** i_ to cluster _Ch_ that minimizes the _φ_ -divergence, 

**==> picture [251 x 17] intentionally omitted <==**

Thus, new clusters _C_ 1 _, . . . , Cm_ are formed. 

3. Renewal Step: Calculate the _φ_ -centers of the renewed clusters, obtaining new cluster centers _**η**_ 1 _, . . . ,_ _**η** m_ . 

4. Termination Step: Repeat the above procedures until convergence. 

It is known that the procedures terminate within a finite number of steps, giving a good clustering result, although there is no guarantee that it is optimal. The _k_ - means[++] method was proposed for choosing good initial values of _**η** i_ by Arthur and Vassilvitshii (2007). 

## _**11.1.4 Voronoi Diagram**_ 

Given a point _**x**_ , we need to find the cluster it belongs to. This is information retrieval or pattern classification to decide which category it belongs to. A subset _Rh_ of _X_ is called the region of _Ch_ when it is decided that pattern _**x**_ ∈ _Rh_ belongs to _Ch_ . The entire _X_ is partitioned into _m_ regions _R_ 1 _, . . . , Rm_ . 

We consider a simple case consisting of two clusters _C_ 1 and _C_ 2 for an explanation. The entire _X_ is divided into two regions _R_ 1 and _R_ 2. For _**x**_ ∈ _R_ 1, 

**==> picture [222 x 12] intentionally omitted <==**

Therefore, the two regions are separated by the hypersurface _B_ 12 that is the boundary of the regions, 

**==> picture [248 x 13] intentionally omitted <==**

235 

11.1 Clustering Patterns 

**Theorem 11.2** _The hypersurface separating two decision regions is the geodesic hyperplane orthogonal to the dual geodesic connecting the two φ-centers of the clusters at the midpoint of the dual geodesic._ 

_Proof_ Connect two _φ_ -centers _**η**_ 1 and _**η**_ 2 by the dual geodesic 

**==> picture [216 x 10] intentionally omitted <==**

The midpoint _**η**_ 12 is defined by 

**==> picture [230 x 11] intentionally omitted <==**

Let _B_ 12 be the geodesic hypersurface (that is the linear subspace in the _**θ**_ coordinates) passing through _**η**_ 12 and orthogonal to the dual geodesic (Fig. 11.2). Then, due to the Pythagorean theorem, any point _**x**_ on the hyperplane satisfies 

**==> picture [293 x 70] intentionally omitted <==**

Hence, we have 

The boundary surface is linear in the _**θ**_ -coordinates but is nonlinear in the _**η**_ - coordinates. When the divergence is the square of the Euclidean distance, _**η**_ - and _**θ**_ -coordinates are the same, so that the boundary is linear in the _**η**_ -coordinates. This is a special case. 

Whenthereare _m_ clusters _C_ 1 _, . . . , Cm, X_ ispartitionedinto _m_ regions _R_ 1 _, . . . , Rm_ , where the boundary of _Ri_ and _R j_ is the geodesic hypersurface satisfying 

**==> picture [247 x 20] intentionally omitted <==**

Such a partition is called the Voronoi diagram due to the _φ_ -divergence (Fig. 11.3). See Nielsen and Nock (2014), Nock and Nielsen (2009), Boissonnat et al. (2010), etc. for details. 

**Fig. 11.2** Boundary of two cluster regions 

**==> picture [115 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
R 2<br>x<br>.η<br>2<br>R 1<br>η<br>12<br>η1. B 12<br>**----- End of picture text -----**<br>


236 

11 Machine Learning 

**Fig. 11.3** Voronoi diagram 

**==> picture [237 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
B 12 R 2 B 23<br>R 3<br>R 1<br>B 34<br>R 4<br>B 14<br>**----- End of picture text -----**<br>


## _**11.1.5 Stochastic Version of Classification and Clustering**_ 

## **11.1.5.1 Probability Distribution Associated with Category** 

Let us consider a cluster _Ch_ of which _φ_ -center is _**η** h_ . We generate a probability distribution 

**==> picture [249 x 13] intentionally omitted <==**

It is centered at _**η** h_ and the probability density of _**x**_ decreases exponentially as the divergence between _**x**_ and _**η** h_ increases. 

As we have shown in Sect. 2.6, it is an exponential family (Banerjee et al. 2005). 

**Theorem 11.3** _The cluster Ch of which the center is_ _**η** h defines a probability distribution of patterns_ _**x** , which is an exponential family,_ 

**==> picture [227 x 11] intentionally omitted <==**

_with respect to the underlying measure_ 

**==> picture [216 x 10] intentionally omitted <==**

_The natural parameter_ _**θ** h of the distribution is the Legendre dual of_ _**η** h._ 

## **11.1.5.2 Soft Clustering Algorithm** 

We consider a mixture of probability distributions of exponential families, 

**==> picture [247 x 23] intentionally omitted <==**

where _πh_ are the prior probabilities that _**x**_ is generated from category _Ch_ and is the unknown parameters which we estimate from a number of observations _**x**_ 1 _, . . . ,_ _**x** N_ . Here, the parameter vector is 

11.1 Clustering Patterns 

237 

**==> picture [230 x 10] intentionally omitted <==**

The maximum likelihood estimator is given by 

**==> picture [228 x 30] intentionally omitted <==**

Before analyzing the MLE, we consider the conditional distribution of categories given _**x**_ , 

**==> picture [224 x 25] intentionally omitted <==**

For pattern _**x**_ , the above probabilities show the posterior probabilities of the categories. This is a stochastic classification or soft classification which assigns _**x**_ to categories according to the posterior probabilities. When we pick up the category that maximizes the probability, it attains hard classification. 

Since the distribution (11.29) is a mixture of exponential families, we can use the EM algorithm for estimating _**ξ**_ . The M-step is usually computationally heavy, but in the present case, it is simple because of (11.13). 

## **Soft Clustering Algorithm (soft** _k_ - **means)** 

1. Initial Step: Choose prior probabilities _πh_ and different cluster centers _**η** h, h_ = 1 _, . . . , m_ , arbitrarily. 

2. Classification Step: For each _**x** i_ , calculate the conditional probabilities _p (Ch_ | _**x** )_ by using the current _πh_ and _**η** h_ . 

3. Renewal Step: By using the conditional probabilities, the new prior _πh_ of class _Ch_ is calculated as 

**==> picture [207 x 27] intentionally omitted <==**

Calculate the new cluster center by 

**==> picture [212 x 30] intentionally omitted <==**

4. Termination: Repeat the above procedures until convergence. 

The Voronoi diagram is defined in a similar way. When we use hard classification based on the posteriori probabilities, the boundary surface of two categories _Ci_ and _C j_ is given by 

**==> picture [210 x 13] intentionally omitted <==**

**Theorem 11.4** _The boundary of two decision regions is the geodesic hypersurface that is orthogonal to the dual geodesic connecting two cluster centers and passes_ 

11 Machine Learning 

238 

_through it at the point satisfying_ 

**==> picture [230 x 13] intentionally omitted <==**

## _**11.1.6 Robust Cluster Center**_ 

When a cluster _C_ composed of _**x**_ 1 _, . . . ,_ _**x** k_ is given, we can calculate the _φ_ -center of cluster by (11.9). Assume that a new point _**x**_[∗] is added to _C_ that might be far from the others. By adding this point, the cluster center might deviate largely. If this new point is an outlier, for example given by mistake, it is not desirable that the cluster center is affected heavily by this point. A robust clustering reduces the undesirable 

More formally, we define the influence function of an outlier _**x**_[∗] . Let _**η**_ ¯ be the center of cluster _C_ , and let _**η**_[¯][∗] be the center of _C_[∗] in which _**x**_[∗] is newly added. We assume that _k_ is large so that the influence of each _**x** i_ is only of the order 1 _/k_ . Let us denote the change of _**η**_ ¯ to _**η**_[¯][∗] by _δ_ _**η**_ and define _z (_ _**x**_[∗] _)_ by 

**==> picture [217 x 22] intentionally omitted <==**

as a function of _**x**_[∗] 

**==> picture [191 x 13] intentionally omitted <==**

holds for a constant _c_ , i.e., | _**z** (_ _**x**_[∗] _)_ | is bounded, the cluster center is robust, because even if an infinitely large _**x**_[∗] is merged in _C_ , its effect is bounded and is very small when _k_ is large. A robust center does not seriously suffer from contamination by outliers. 

## **11.1.6.1 Total Bregman Divergence** 

The Bregman divergence _Dφ_ � _**η**_[′] : _**η**_ � is measured by the height _φ_ � _**η**_[′][�] at _**η**_[′] from the tangent hypersurface of _φ(_ _**η** )_ drawn at _**η**_ . This is the vertical length of point � _**η**_[′] _, φ_ � _**η**_[′][��] tothetangenthypersurface(Fig. 11.4a).Onemayconsidertheorthogonal projection of � _**η**_[′] _, φ_ � _**η**_[′][��] to the tangent hypersurface (Fig. 11.4b). It defines another measure of divergence from _**η**_[′] to _**η**_ . This idea, hinted at in the total least squares in regression, was proposed by Vemuri et al. (2011) and called the total Bregman divergence, denoted as tBD. 

The length of the orthogonal projection is easily calculated and given by 

**==> picture [240 x 24] intentionally omitted <==**

11.1 Clustering Patterns 

239 

**==> picture [395 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) φ( ) (b) φ( )<br>. .<br>D [ : ] tBD[ : ]<br>.<br>.<br>. .<br>**----- End of picture text -----**<br>


**Fig. 11.4 a** Bregman divergence _D_ ; **b** total Bregman divergence _t BD_ 

where 

**==> picture [224 x 14] intentionally omitted <==**

It is invariant under orthogonal transformations of _(_ _**η** , φ)_ -space. Since the scale of _φ(_ _**η** )_ is arbitrary, we introduce a free parameter _c_ which changes _φ(_ _**η** )_ to _cφ(_ _**η** )_ and define tBD by 

**==> picture [244 x 28] intentionally omitted <==**

This is a conformal transformation of Bregman divergence. The free parameter _c_ controls the degree of conformal modification. 

## **11.1.6.2 Total BD is Robust** 

The following is one of the remarkable characteristics of tBD, proved in Liu et al. (2012). 

**Theorem 11.5** _The tBD φ-center of a cluster is robust._ 

_Proof_ When an outlier _**x**_[∗] is newly added to _C_ of which the previous center is _**η**_ ¯ , the new center _**η**_ ¯[∗] under tBD is the minimizer of 

**==> picture [260 x 26] intentionally omitted <==**

The influence function _**z** (_ _**x**_[∗] _)_ is defined by (11.35). Assuming _k_ is large, we expand the new center in the Taylor series, obtaining 

**==> picture [252 x 23] intentionally omitted <==**

11 Machine Learning 

240 

where 

**==> picture [226 x 24] intentionally omitted <==**

Since 

**==> picture [237 x 27] intentionally omitted <==**

is bounded for any large _**x**_[∗] _,_ _**z** (_ _**x**_[∗] _)_ is bounded, and hence the tBD _φ_ -center is robust. □ 

Vemuri et al. (2011) used tBD to analyze MRI images, obtaining good results. Liu et al. (2012) applied the tBD to the problem of image retrieval, obtaining a stateof-the-art result. Conformal transformations of a Bregman divergence are further developed in Nock et al. (2015). 

## _**11.1.7 Asymptotic Evaluation of Error Probability in Pattern Recognition: Chernoff Information**_ 

We consider two probability distributions 

**==> picture [272 x 10] intentionally omitted <==**

in an exponential family. Here, we use _**θ**_ -coordinates related to _ψ(_ _**θ** )_ and the KLdivergence _Dψ_ = _DK L_ instead of the previous _**η**_ -coordinates related to _φ(_ _**η** )_ and the dual divergence _Dφ_ . When _N_ observations _**x**_ 1 _, . . . ,_ _**x** N_ are derived, all of which are supposed to be generated from either _p_ 1 _(_ _**x** )_ or _p_ 2 _(_ _**x** )_ , we need to decide which is the true distribution. Let us divide the manifold in two regions _R_ 1 and _R_ 2 such that, when the observed point 

**==> picture [196 x 22] intentionally omitted <==**

belongs to _R_ 1 _(R_ 2 _)_ , we decide that the true distribution is _p_ 1 _(_ _**x** ) ( p_ 2 _(_ _**x** ))_ . When _N_ is large, the probability that _**η**_ ¯ is generated from _pi (_ _**x** )_ is given, due to the large deviation theorem in Chap. 3, by 

**==> picture [235 x 14] intentionally omitted <==**

where _**θ**_[¯] is the primal coordinates of _**η**_ ¯ . In order to minimize the probability of misclassification, the regions _Ri_ should be determined as 

**==> picture [249 x 13] intentionally omitted <==**

11.1 Clustering Patterns 

241 

That is, the boundary of _R_ 1 and _R_ 2 is the hypersurface satisfying 

**==> picture [250 x 10] intentionally omitted <==**

Let us consider the _e_ -geodesic connecting _p_ 1 _(_ _**x** )_ and _p_ 2 _(_ _**x** )_ , 

**==> picture [290 x 10] intentionally omitted <==**

or 

**==> picture [213 x 10] intentionally omitted <==**

in the _**θ**_ -coordinates. Its midpoint is defined by _**θ** λ_[∗] satisfying 

**==> picture [235 x 9] intentionally omitted <==**

Due to the Pythagorean theorem, _B_ 12 is the _m_ -geodesic hyperplane orthogonal to the _e_ -geodesic, passing through it at _**θ**_[∗] _λ_[. (See Fig.][11.5][.)] 

The midpoint _λ_[∗] is given by the minimizer of 

**==> picture [230 x 39] intentionally omitted <==**

The asymptotic error bound is hence given by 

**==> picture [234 x 11] intentionally omitted <==**

The negative exponent of error, 

**==> picture [218 x 10] intentionally omitted <==**

**Fig. 11.5** Decision boundary _B_ 12 and separation midpoint _**θ** λ_ ∗ 

**==> picture [110 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
B 12<br>R 1 R 2<br>P 1.: 1 * P 2. [:]<br>**----- End of picture text -----**<br>


11 Machine Learning 

242 

is called the Chernoff information or Chernoff divergence (Chernoff 1952). This is related to the _α_ -divergence _Dα_ [ _p_ 1 : _p_ 2]. We have 

**==> picture [300 x 25] intentionally omitted <==**

Hence, by letting _α_[∗] be the maximizer of ��1 − _α_[2][�] _/_ 4� _Dα_ [ _p_ 1 : _p_ 2], we have 

**==> picture [195 x 22] intentionally omitted <==**

_Remark_ One may use a prior distribution _(π_ 1 _, π_ 2 _)_ on two classes _C_ 1 and _C_ 2 in the Bayesian standpoint. However, the asymptotic error bound does not depend on it. 

## **11.2 Geometry of Support Vector Machine** 

The support vector machine (SVM) is one of the powerful learning machines for pattern recognition and regression (Cortes and Vapnik 1995; Vapnik 1998). It embeds pattern signals to a higher-dimensional space, even an infinite-dimensional Hilbert space, and uses a kernel function to calculate outputs. Although the Hilbert space is infinite-dimensional in general, the kernel trick makes it possible to work within a finite regime, avoiding difficulties of infinitely large degrees of freedom. We do not describe the details of the SVM, but focus only on its Riemannian structure. It is used for modifying a given kernel to improve the performance of the machine. 

## _**11.2.1 Linear Classifier**_ 

We begin with a linear machine for classifying patterns, which is a simple perceptron. Given input pattern _**x**_ ∈ _**R**[n]_ , consider a linear function 

**==> picture [207 x 10] intentionally omitted <==**

having parameters _**ξ**_ = _(_ _**w** , b)_ . The machine classifies patterns into two classes _C_ + and _C_ −, according to the signature of output function _f (_ _**x** ,_ _**ξ** )_ . That is, when 

**==> picture [191 x 10] intentionally omitted <==**

_**x**_ is classified into _C_ +, and otherwise into _C_ −. 

Consider a set of training examples _D_ = { _**x**_ 1 _,_ _**x**_ 2 _, . . . ,_ _**x** N_ } which are divided into two classes _C_ + and _C_ −. When _**x** i_ ∈ _C_ +, it is accompanied by teacher signal _yi_ = 1, and when _**x** i_ ∈ _C_ −, it is accompanied by _yi_ = −1. They are linearly separable when 

11.2 Geometry of Support Vector Machine 

243 

there exists _**w**_ and _b_ , for which 

**==> picture [273 x 10] intentionally omitted <==**

holds. When _(_ _**w** , b)_ is such a solution, _(c_ _**w** , cb)_ is also a solution for any _c >_ 0. We eliminate this indefiniteness of scale by imposing the constraints 

**==> picture [248 x 14] intentionally omitted <==**

Since the Euclidean distance from point _**x**_ to the separating hyperplane 

**==> picture [195 x 10] intentionally omitted <==**

is 

**==> picture [201 x 24] intentionally omitted <==**

the distance from _**x** i_ to the separating hyperplane is given by 

**==> picture [204 x 24] intentionally omitted <==**

The minimum of these distances is given by 

**==> picture [190 x 23] intentionally omitted <==**

and is attained by the points _**x** i_ that satisfy 

**==> picture [206 x 10] intentionally omitted <==**

We call these points _**x** i_ the support vectors of the training set _D_ and the minimal distance the margin. There are in general a number of support vectors. See Fig. 11.6. A good machine has a large margin. So the problem of obtaining the optimal linear machine is to minimize 

**==> picture [197 x 22] intentionally omitted <==**

under the constraint 

**==> picture [206 x 10] intentionally omitted <==**

Let us use Lagrange multipliers _**α**_ = _(α_ 1 _, . . . , αN )_ for solving the problem. Then, the problem reduces to the unconstrained minimization of 

**==> picture [258 x 22] intentionally omitted <==**

11 Machine Learning 

244 

**==> picture [395 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 11.6 Linear classifier<br>and support vectors . . C +<br>. . . C -<br>. . . , support vectors<br>.<br>.<br>.<br>w x +b= 0<br>margin<br>**----- End of picture text -----**<br>


By differentiating it with respect to _**w**_ and _b_ and making the derivatives equal to 0, we have 

**==> picture [231 x 22] intentionally omitted <==**

Substituting (11.70) in (11.69), the problem is reformulated in the dual form using the dual variables _αi_ : 

**==> picture [271 x 22] intentionally omitted <==**

with respect to _**α**_ under the constraint 

**==> picture [214 x 15] intentionally omitted <==**

Since the objective function (11.71) is a quadratic function of _αi_ , there is a wellknown algorithm to solve it. It should be remarked that _αi_ = 0 when _**x** i_ is not a support vector. 

The optimized output function is written as 

**==> picture [224 x 15] intentionally omitted <==**

in terms of the solution _αi_ . The function is given by using only the support vectors and the other non-support examples _**x** i_ are irrelevant. 

The linear output function is useful even when patterns _D_ are not linearly separable. We use slack variables in this case. It can also be used as a regression function, where the output _y_ takes analog values. See textbooks about the support vector machine. 

245 

11.2 Geometry of Support Vector Machine 

## _**11.2.2 Embedding into High-Dimensional Space**_ 

Patterns are not linearly separable in many problems and a linear machine does not work well in many cases. In overcoming this difficulty, it has been known since the early nineteen-sixties that nonlinear embedding of patterns into a high-dimensional space helps. Let us consider a nonlinear transformation of _**x**_ ∈ _**R**[n]_ into a highdimensional space _**R**[m] (m > n)_ by 

**==> picture [223 x 10] intentionally omitted <==**

Then pattern _**x**_ is represented in _**R**[m]_ as 

**==> picture [188 x 10] intentionally omitted <==**

where 

**==> picture [226 x 10] intentionally omitted <==**

The classification problem is formulated in _**R**[m]_ by using _**z**_ = _**ϕ** (_ _**x** )_ , where the linear _**R**[m]_ is written as 

**==> picture [243 x 11] intentionally omitted <==**

This was known as the _Φ_ -function method (see Aizerman et al. 1964). The nonlinear embedding improves the linear separability of patterns. 

Consider a simple example in which patterns belonging to _C_ + are inside a circle and those belonging to _C_ − are outside the circle (see Fig. 11.7a). The patterns are not linearly separable in _**R**_[2] . However, if we use the following embedding to _**R**_[3] , 

**==> picture [239 x 13] intentionally omitted <==**

they become linearly separable, as is seen in Fig. 11.7b. 

It is expected that patterns become linearly separable when _m_ is large. The multilayer perceptron of Rosenblatt (1961) uses random threshold logic functions in the hidden layer for this purpose. The linear separability is assured when _m_ is sufficiently large. The universality of a three-layer perceptron guarantees that any function _f (_ _**x** )_ can be approximated by a linear function after embedding, provided _m_ is sufficiently large. 

However, we need to find good embedding functions for good pattern separation. This is a difficult problem. Moreover, when _m_ is large, in particular infinitely large, calculations of embedded _**z**_ = _**ϕ** (_ _**x** )_ are computationally difficult. It is the kernel trick that resolves the difficulty. 

246 

11 Machine Learning 

**==> picture [473 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
2 2<br>x 2 z 3 x 1 x 2<br>(a)<br>(b)<br>. .<br>. . . C +<br>x 1<br>. . ..<br>. . .<br>. C + [.] . . C _<br>z 2= x 2<br>C _ z 1= x 1<br>**----- End of picture text -----**<br>


**Fig. 11.7 a** Non-separable in _**R**_ 2; **b** separable in _**R**_[3] 

## _**11.2.3 Kernel Method**_ 

We consider the inner product of _**z**_ = _**ϕ** (_ _**x** )_ and _**z**_[′] = _**ϕ**_ � _**x**_[′][�] after embedding, 

**==> picture [256 x 15] intentionally omitted <==**

This is a symmetric function of _**x**_ and _**x**_[′] . Moreover, for any coefficients _**c**_ = _(c_ 1 _, . . . , cm)_ , positivity 

**==> picture [214 x 15] intentionally omitted <==**

is guaranteed for _**c**_ ̸= 0, provided _ϕ_ 1 _(_ _**x** ), . . . , ϕm(_ _**x** )_ are linearly independent. One may consider that _K_ � _**x** ,_ _**x**_[′][�] is an infinite-dimensional positive-definite matrix in an infinite-dimensional space of _**z** (_ _**x** )_ , where _**x**_ and _**x**_[′] are regarded as indices for specifying the rows and columns of the matrix. That is, _K_ � _**x** ,_ _**x**_[′][�] plays the role of _K (i, j)_ , which is a matrix specified by row _i_ and column _j_ . 

We consider the eigenvalue problem, 

**==> picture [236 x 23] intentionally omitted <==**

where _λ_ 1 _, . . . , λm_ are eigenvalues and _k_ 1 _(_ _**x** ), . . . , km(_ _**x** )_ are corresponding eigenfunctions. Here, _m_ can be infinite. We call _K_ � _**x** ,_ _**x**_[′][�] the kernel function operating on a function _k(_ _**x** )_ as in the integral (11.81). By using the eigen-functions, the kernel function is expanded as 

**==> picture [230 x 15] intentionally omitted <==**

11.2 Geometry of Support Vector Machine 

247 

Comparing this with (11.79), we see that the embedding functions are the eigenfunctions divided by the square roots of the eigenvalues, 

**==> picture [206 x 24] intentionally omitted <==**

The optimal output function (11.73) can be written using the kernel function as 

**==> picture [234 x 15] intentionally omitted <==**

This is another expression of (11.77) in terms of the kernel function, where the embedding functions _**ϕ**_ are eliminated. Therefore, even when _m_ is infinite, we do not need to calculate _**z**_ = _**ϕ** (_ _**x** )_ and the kernel is sufficient to compose the optimal output function. This is called the kernel trick. See Scholkopf (1997) and ShaweTaylor and Cristianini (2004). 

We may start from a kernel function _K_ � _**x** ,_ _**x**_[′][�] , without specifying embedding functions,provided _K_ � _**x** ,_ _**x**_[′][�] ispositive-definitesatisfying(11.80),calledtheMercer condition. 

The Gaussian kernel 

**==> picture [230 x 32] intentionally omitted <==**

is used frequently, where _σ_[2] is a free parameter to be adjusted. Its eigen-functions are 

**==> picture [213 x 10] intentionally omitted <==**

so that the expansion of a function _f (_ _**x** )_ in terms of the eigen-functions corresponds to the Fourier expansion. 

Another kernel of frequent use is the polynomial kernel of order _p_ defined by 

**==> picture [220 x 13] intentionally omitted <==**

The eigen-functions are polynomials of _**x**_ up to certain degrees and _m_ is finite. The kernel method can be used even when _**x**_ are discrete symbols, by defining an adequate positive-definite kernel. Therefore, it is a powerful tool in symbol processing and bioinformatics. 

## _**11.2.4 Riemannian Metric Induced by Kernel**_ 

The kernel method is computationally tractable using a modern computer. However, a good choice of kernel depends on the problem to be solved and no good criteria 

11 Machine Learning 

248 

exist except for trial-and-error. This section considers the geometry induced by a kernel and proposes a method to improve a given kernel (Amari and Wu 1999; Wu and Amari 2002; Williams et al. 2005). 

The original space _**R**[n]_ of patterns is embedded in _**R**[m]_ , possibly in _**R**_[∞] , as a curved _n_ -dimensional submanifold. A Riemannian metric is induced in _**R**[n]_ by this embedding. Two nearby points _**x**_ and _**x**_ + _d_ _**x**_ are embedded to _**ϕ** (_ _**x** )_ and _**ϕ** (_ _**x**_ + _d_ _**x** )_ , respectively, and the square of their Euclidean distance in _**R**[m]_ is 

**==> picture [311 x 25] intentionally omitted <==**

Therefore, the induced Riemannian metric is given by 

**==> picture [243 x 25] intentionally omitted <==**

which is expressed in terms of the kernel as 

**==> picture [233 x 27] intentionally omitted <==**

The volume element at point _**x**_ is given by 

**==> picture [231 x 19] intentionally omitted <==**

which shows how the volume is enlarged or contracted at around _**x**_ . Since only the support vectors play a role in the output function, we consider expanding neighborhoods of the support vectors in _**R**[m]_ , while other parts remain as they are. 

To this end, we modify the current kernel _K_ � _**x** ,_ _**x**_[′][�] to 

**==> picture [236 x 14] intentionally omitted <==**

where _σ(_ _**x** )_ represents how the volume is enlarged at around _**x**_ . It should be large near the support vectors, so 

**==> picture [211 x 23] intentionally omitted <==**

was chosen in Amari and Wu (1999), Wu and Amari (2002), where _**x** i_[∗][are the support] vectors and _κi_ are adequate constants. Later, 

**==> picture [219 x 13] intentionally omitted <==**

was proposed as a more natural choice (Williams et al. 2005). 

11.2 Geometry of Support Vector Machine 

249 

The transformation (11.92) is called the conformal transformation of a kernel. The Riemannian metric changes to 

**==> picture [293 x 30] intentionally omitted <==**

where 

**==> picture [267 x 24] intentionally omitted <==**

When 

**==> picture [196 x 10] intentionally omitted <==**

which is satisfied by the Gaussian kernel, we have a simplified expression 

**==> picture [261 x 13] intentionally omitted <==**

Computer simulations show that the performance of recognition is improved by up to ten percent by a conformal transformation. This might shed light on the problem of choosing a good kernel. 

Recently, Lin and Jiang (2015) proposed another method of choosing _σ(_ _**x** )_ adaptively from data. 

## **11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms** 

A graphical model specifies stochastic interactions among a number of random variables. Stochastic reasoning is a procedure to estimate the values of unobserved random variables from those of observed variables based on its graphical structure. Belief propagation (BP) (Pearl 1988) and convex-concave computational procedure (CCCP) (Yuille 2002) are methods in frequent use to obtain good estimates in artificial intelligence and machine learning. 

The joint probability distributions of random variables in a graphical model form an exponential family. It has a dually flat Riemannian structure, so these algorithms are well understood from the point of view of dual geometry. The present section studies the BP and CCCP algorithms based on the dually flat structure, based on Ikeda et al. (2004a, b). The belief of each node about the value of its variable is propagated through _e_ - and _m_ -projections to obtain a harmonized consensus in BP. It is a merit of dual geometry that a new simplified version of CCCP is derived naturally. 

250 

11 Machine Learning 

## _**11.3.1 Graphical Model**_ 

Let us consider a set of mutually interacting random variables _x_ 1 _, . . . , xn_ . That is, _xi_ is a random variable of which the value is determined stochastically under the 

**==> picture [215 x 12] intentionally omitted <==**

A random variable _x j_ is called a parent of _xi_ when it is an element of _Xi_ . We study joint probability distributions of _x_ 1 _, . . . , xn_ . The probability of _xi_ is given by the conditional probability distribution _p (xi_ | _Xi )_ conditioned on the values of its parents. We use a graph to represent the parent–child relation (Fig. 11.8). The graph is composed of _n_ nodes corresponding to the random variables _x_ 1 _, . . . , xn_ . There is a branch between nodes _xi_ and _x j_ when _x j_ is a parent of _xi_ . The branches are oriented in this case, but we consider a non-oriented graph by disregarding the direction of a branch. This is called a graphical model of random variables. See Wainright and Jordan (2008) and Lauritzen (1996), for example. 

The joint probability distribution is written using the product of the conditional distributions as 

**==> picture [230 x 28] intentionally omitted <==**

A graphical model is also called a random Markov field. It is an extension of the Markov chain, representing the stochastic causality. 

A subgraph composed of nodes _C_ = � _xi_ 1 _, . . . , xik_ � is called a clique when it is a complete graph. A graph is complete when any two nodes in it are connected by a branch. See Fig. 11.7, where { _x_ 1 _, x_ 2 _, x_ 3 _, x_ 4} _,_ { _x_ 4 _, x_ 7} and { _x_ 3 _, x_ 5 _, x_ 6} are examples of cliques, but { _x_ 1 _, x_ 2 _, x_ 3 _, x_ 5} and { _x_ 3 _, x_ 7} are not. Assume that a graphical model has _L_ cliques _C_ 1 _, . . . , CL_ . Then, it is known that the joint probability distribution (11.100) is decomposed as 

**==> picture [242 x 23] intentionally omitted <==**

**Fig. 11.8** Graphical model 

**==> picture [86 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
x 1<br>x 2 x 4<br>. x 3 . x 7<br>. .<br>x 5 x 6<br>**----- End of picture text -----**<br>


251 

11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms 

where _c_ is a normalization constant, _φ_[˜] _i , i_ = 1 _, . . . , n_ , is a function of _xi_ and _φr (Cr ) , r_ = 1 _, . . . , L_ , is a function of the variables in clique _Cr_ . The decomposition is not unique in general, but is unique when we use only maximal cliques. A clique is maximal when it is not included in any complete subgraphs. 

Divide the nodes of a graphical model into two parts, _X o_ and _X u_ . Assume that values of the variables in _X o_ areobservedbut thosein _X u_ arenot. Stochasticreasoning is the problem of estimating the values of unobserved variables in _X u_ , under the condition that the variables in _X o_ are observed. We use the conditional probability of _X u_ conditioned on _X o_ to estimate the unknown values of _X u_ . 

Let us fix the values of _X o_ and consider the conditional distribution of _X u_ , 

**==> picture [212 x 10] intentionally omitted <==**

where _X o_ is omitted in the notation of _q(X u)_ . It is again represented by a graphical model consisting of nodes of _X u_ . So the problem is the estimation of the values of _X u_ in the reduced graphical model, where the values of _X o_ are fixed and omitted from the notation. We hereafter denote _X u_ simply as _X_ and use the vector notation 

**==> picture [203 x 9] intentionally omitted <==**

We consider the simple binary case where each _xi_ takes binary values 1 and −1. The maximum likelihood estimate _**x**_ based on _q(_ _**x** )_ is the maximizer of _q(_ _**x** )_ . However, this is computationally heavy when _n_ is large, because there are 2 _[n]_ _**x**_ ’s and we need to compare the values of _q(_ _**x** )_ for all of them. We use the following simple estimate that the estimated value of _xi_ is 1 when the probability of _xi_ = 1 is larger than that of _xi_ = −1, and otherwise −1. In other words, let us calculate the expectation of _xi_ , 

**==> picture [256 x 10] intentionally omitted <==**

and _xi_ = 1 when _ηi_ is positive and _xi_ = −1, when _ηi_ is negative. That is, the estimate is given by 

**==> picture [193 x 10] intentionally omitted <==**

This minimizes the sum of the error probabilities of all the variables. 

The problem reduces to the calculation of the expected value of _xi_ . However, this is again computationally heavy, because 

**==> picture [245 x 23] intentionally omitted <==**

includes 2 _[n]_ terms. 

We need a computationally tractable algorithm of obtaining a good approximation of the mean values. This problem appears in physics, too, and the mean field approximation is well known to obtain such an approximate solution. 

252 

11 Machine Learning 

## _**11.3.2 Mean Field Approximation and m-Projection**_ 

The probability distribution (11.101) of a graphical model can be written as 

**==> picture [252 x 31] intentionally omitted <==**

where _ψ_ is the normalization constant, called free energy in physics, with 

**==> picture [217 x 28] intentionally omitted <==**

and 

**==> picture [225 x 13] intentionally omitted <==**

**==> picture [206 x 24] intentionally omitted <==**

**==> picture [272 x 34] intentionally omitted <==**

which includes two _e_ -affine parameters, namely _**θ**_ and _**v**_ = _(v_ 1 _, . . . , vL )_ . The original _q(_ _**x** )_ is a member of this family and is given by 

**==> picture [219 x 10] intentionally omitted <==**

When _**v**_ = 0,thedistributionsdonotincludeinteractiontermssothatthesubmanifold specified by _**v**_ = 0 is the family of independent distributions of _**x**_ . We denote it by 

**==> picture [250 x 10] intentionally omitted <==**

Figure 11.9 shows the expanded model _M_[˜] and the independent model _M_ 0. The expectation of _**x**_ is easily calculated for a distribution in _M_ 0, because all _x_ 1 _, . . . , xn_ are independent. It is given by 

**==> picture [242 x 24] intentionally omitted <==**

Given _q(_ _**x** )_ , we consider the independent distribution _p_[∗] _(_ _**x** )_ ∈ _M_ 0 that has the same expected value of _**x**_ as _q(_ _**x** )_ . The following theorem shows the relation between _q(_ _**x** )_ and _p_[∗] _(_ _**x** )_ . 

**Theorem 11.6** _The m-projection of q(_ _**x** ) to M_ 0 _keeps the expectation of_ _**x** invariant._ 

253 

11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms 

**Fig. 11.9** _m_ -projection and _e_ -projection of _**v** (x)_ to _M_ 0 

**==> picture [138 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
/\ . [q] ( [x] ) M [~]<br>! \<br>e -projection fy m -projection<br>v ‘SyP|yo<br>M 0<br>p ~ [.] *( x ) . p *( x )<br>.<br>**----- End of picture text -----**<br>


_Proof_ Let us put 

_m_ 

**==> picture [204 x 14] intentionally omitted <==**

_m_ where 0[is the operator of] _[ m]_[-projection to] _[M]_[0][and let the] _[ e]_[-coordinates of] _[p]_[∗] _[(]_ _**[x]**[)]_ be _**θ**_[∗] . The _m_ -coordinates are 

**==> picture [194 x 37] intentionally omitted <==**

The tangent vector of _M_ 0 at _p_[∗] is represented by 

**==> picture [221 x 22] intentionally omitted <==**

On the other hand, the tangent vector of the _m_ -geodesic connecting _q_ and _p_[∗] is given by 

**==> picture [213 x 24] intentionally omitted <==**

They are orthogonal because of the _m_ -projection, so we have 

**==> picture [290 x 10] intentionally omitted <==**

This shows 

**==> picture [333 x 34] intentionally omitted <==**

254 

11 Machine Learning 

However, the _m_ -projection of _q(_ _**x** )_ is not computationally easy. Statistical physics uses the mean field approximation, which replaces the _m_ -projection by the _e_ - projection (Tanaka 2000, see Amari et al. 2001 for the _α_ -projection). The _m_ - projection is given by the minimizer of the KL-divergence _K L_ [ _q_ : _p_ ] _, p_ ∈ _M_ 0. The mean field approximation uses the dual KL-divergence _K L_ [ _p_ : _q_ ] and minimizes it with respect to _p_ ∈ _M_ 0. The minimizer is given by the _e_ -projection of _q_ to _M_ 0. This is computationally tractable so it can be used as an approximate solution. See Fujiwara and Shuto (2010) for higher-order mean-field approximation. 

We consider 

**==> picture [260 x 19] intentionally omitted <==**

as a specific example, which represents a spin system where the interaction of two spins _xi_ and _x j_ are given by _wi j_ . The cliques consist of branches _(i, j), wi j_ ̸= 0. It does not include interactions of more than two nodes and is known as the Boltzmann machine in neural networks, where _wi j_ represents the strength of the synaptic weights of connection between two neurons _xi_ and _x j_ . 

The KL-divergence from _p_ ∈ _M_ 0 to _q_ is given by 

**==> picture [311 x 33] intentionally omitted <==**

It is easy to see 

**==> picture [203 x 13] intentionally omitted <==**

because _xi_ and _x j_ are independent under _p_ and hence, we have 

**==> picture [308 x 15] intentionally omitted <==**

By differentiating it with respect to _ηi_ and making the derivatives equal to 0, we obtain 

**==> picture [225 x 19] intentionally omitted <==**

where 

**==> picture [233 x 25] intentionally omitted <==**

is taken into account. This is the equation to obtain the minimizer _**η**_ ˜[∗] of (11.122). 

˜ This is a well-known equation. The solution _p_[∗] _(_ _**x** )_ is different from the _m_ - projection so that it is an approximation. _M_ 0 is _e_ -flat but not _m_ -flat. Therefore, the _m_ -projection is unique but the _e_ -projection is not necessarily unique. Hence, the solution of (11.125) is not necessarily unique. Moreover, the solution can be a maximum or a saddle point of _K L_ [ _p_ : _q_ ]. 

255 

11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms 

## _**11.3.3 Belief Propagation**_ 

Belief propagation is an algorithm, proposed by Pearl (1988), to obtain an approximate value of the expectation of _**x**_ efficiently. This is a cooperative procedure, where each node exchanges its belief about the expected value through branches. The belief is renewed by taking the beliefs of the other nodes into account. The procedure terminates when a consensus is reached. The information geometry of BP was formulated by Ikeda et al. (2004a, b). We here present a simplified version of it. 

Corresponding to each clique _Cr_ , we construct a submodel _Mr_ of _M_[˜] , 

**==> picture [295 x 10] intentionally omitted <==**

It includes only one nonlinear term _cr (_ _**x** )_ corresponding to clique _Cr_ . The sum of all the other interactions, _cr_[′] _(_ _**x** )_ of _Cr_[′] , _r_[′] ̸= _r_ , is replaced by a linear term _**θ** r_ · _**x**_ . It is an exponential family, having _e_ -parameter _**θ** r_ . This is a submanifold of _M_[˜] obtained by putting 

**==> picture [253 x 11] intentionally omitted <==**

In addition to the independent submodel _M_ 0, there are _L_ such submodels _Mr , r_ = 1 _, . . . , L_ . Since _Mr_ includes only one nonlinear term, it is computationally easy to _m_ -project a member of _Mr_ to _M_ 0. 

To avoid complications, we use notational simplification. Since all the probability distributions have the term exp _(_ _**h**_ · _**x** )_ in common, we neglect it in the following. This term should be added to the final solution. Mathematically, this corresponds to defining probability densities with respect to the common measure exp { _**h**_ · _**x**_ }. By this simplification, our target distribution (11.107) is 

**==> picture [227 x 19] intentionally omitted <==**

and submodels are 

**==> picture [263 x 25] intentionally omitted <==**

All the submodels are _e M_[˜] . 

Each submodel tries to approximate _q(_ _**x** )_ such that the expectation of _**x**_ becomes close to E _q_ [ _**x**_ ]. Since _Mr_ includes only one nonlinear term, all the other interaction terms are replaced by the linear term _**θ** r_ . They exchange their results concerning the expectation, and eventually reach a consensus satisfying 

**==> picture [231 x 10] intentionally omitted <==**

256 

11 Machine Learning 

where E _r_ is the expectation with respect to _pr (_ _**x** ,_ _**θ** r )_ . If the consensus is equal to the expectation of _**x**_ with respect to _q(_ _**x** )_ , it is the true solution. But this does not occur in general. However, it would give a good approximation. 

We consider the following procedure for reaching the consensus: 

**1. Initial step** : Assign arbitrary initial values _**θ** r_[0][to submodels] _[M][r]_[. They can be 0.] Continue the following steps _t_ = 0 _,_ 1 _, . . ._ until convergence. **2.** _**m**_ - **projection step** : _m_ -project _pr_ � _**x** ,_ _**θ** r[t]_ � at time _t_ of _Mr_ to _M_ 0. Denote the resultant distribution in _M_ 0 by _**θ**_[˜] _t_ 0 _r_[,] 

**==> picture [227 x 23] intentionally omitted <==**

## **3. Calculation of belief of** _**Mr**_ : Calculate 

**==> picture [197 x 15] intentionally omitted <==**

_t_ Since the _m_ -projection of _p_ � _**x** ,_ _**θ** r[t]_ � to _M_ 0 is _**θ**_[˜] 0 _r_[, it includes not only] _**[ θ]** r[t]_[but also the] linearization of the _cr (_ _**x** )_ . Hence, _**ξ** r[t]_[in (][11.134][) corresponds to the linearization of] the single nonlinear term _cr (_ _**x** )_ . It represents the linearized version of _cr (_ _**x** )_ in _M_ 0. It is regarded as the belief of _Mr_ that its nonlinear term _cr (_ _**x** )_ is effectively given by _**ξ** r[t]_[in] _[M]_[0][.] 

**4. Renewal of the candidate in** _**M**_ **0 at** _**t**_ **+ 1** : Add all the beliefs _**ξ** r[t]_[of] _[ c][r]_[of] _[M][r]_[to] give a distribution of _M_ 0 at _t_ + 1, 

**==> picture [197 x 15] intentionally omitted <==**

**5. Renewal of** _**Mr**_ **at** _**t**_ **+ 1** : Construct a new candidate _**θ** r[t]_[+][1] of _Mr_ , where the nonlinear terms _cr_[′] � _r_[′] ̸= _r_ � other than _cr_ are replaced by the sum of the beliefs _**ξ** r[t]_[′] of _Mr_[′] , but _cr_ is used as it is. Therefore, 

**==> picture [224 x 24] intentionally omitted <==**

When the procedure converges, the converged _**θ**_[∗] 0[and] _**[ θ]** r_[∗][satisfy] 

**==> picture [224 x 23] intentionally omitted <==**

so all the models reach a consensus, having the same expectation of _**x**_ . 

257 

11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms 

## _**11.3.4 Solution of BP Algorithm**_ 

We study the solution to which the BP algorithm converges from the geometrical point of view. It should be remarked that there is no guarantee of convergence for the BP algorithm. Note that the CCCP algorithm in the next section always converges. 

**Theorem 11.7** _When the BP algorithm converges, the following two conditions are satisfied:_ 

**==> picture [246 x 44] intentionally omitted <==**

_Proof_ The _m_ -condition is the consequence of consensus (11.137). The _e_ -condition is derived by using (11.134) and (11.135). □ 

We remark that the _e_ -condition is always satisfied for _**θ**[t]_ 0[and] _**[θ]** r[t]_[after][step][5][of] the procedure, but the _m_ -condition is not. The procedure terminates when the _m_ - condition is satisfied. The implications of the two conditions are as follows. See Figs. 11.10 and 11.11. Let _M_[∗] be the _m_ -flat submanifold connecting all of _pr_ _**x** ,_ _**θ** r_[∗] and _p_ 0 _**x** ,_ _**θ**_[∗] 0[,] 

**==> picture [318 x 24] intentionally omitted <==**

**Fig. 11.10** _m_ -condition 

**==> picture [131 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
M [~]<br>. q ( x )<br>M [*]<br>* M r<br>r<br>* Mr<br>r<br>* M 0<br>0<br>...<br>...<br>**----- End of picture text -----**<br>


258 

11 Machine Learning 

**Fig. 11.11** _e_ -condition 

**==> picture [121 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
M [~]<br>E [*]<br>. q ( x )<br>* M r<br>r<br>* M r<br>r<br>* M 0<br>0<br>...<br>...<br>**----- End of picture text -----**<br>


Let _E_[∗] be the _e_ -flat submanifold connecting all of them, 

**==> picture [316 x 34] intentionally omitted <==**

**Corollary** _The m- and e-conditions are equivalent to the following two, respectively:_ 

_**m** -_ _**condition** : M_[∗] _is orthogonal to M_ 0 _._ 

_**e** -_ _**condition** : E_[∗] _includes the true distribution q(_ _**x** )._ 

If _M_[∗] includes _q(_ _**x** )_ , its _m_ -projection to _M_ 0 is _**θ**_[∗] 0[. The solution is exact in such a] case. The following theorem is known. 

**Theorem 11.8** _When the underlying graph is acyclic, that is, it does not include cycles, M_[∗] _includes q(_ _**x** ) and the solution gives the exact answer._ 

The BP algorithm is stated in geometrical terms in the above explanation. It is beneficial to show the relation between the geometrical algorithm and the conventional BP algorithm written in textbooks. The two are essentially the same. We show only the case where interactions exist between pairs of nodes and no higher-order interactions exist. The conventional algorithm calculates the belief _b(xi )_ at node _xi_ and message _mki (xi )_ , which is transmitted from node _xk_ to node _xi_ through branch _(i, k)_ . The belief is constructed from the messages by 

**==> picture [235 x 28] intentionally omitted <==**

259 

11.3 Stochastic Reasoning: Belief Propagation and CCCP Algorithms 

where _Z_ is the normalization constant and _N (i)_ is the set of nodes which are connected with node _xi_ . The messages at _t_ + 1 are updated by 

**==> picture [295 x 28] intentionally omitted <==**

The correspondence of the quantities appearing in the two approaches are given by 

**==> picture [238 x 60] intentionally omitted <==**

where _r_ is the branch (clique) connecting _i_ and _j_ . 

## _**11.3.5 CCCP (Convex–Concave Computational Procedure)**_ 

A new algorithm called CCCP was proposed by Yuille (2002), see also Yuille and Rangarajan (2003). We show a new version of it based on information geometry, which is much simpler than the original one, because the new one does not include double loops in the procedure. 

The BP algorithm chooses a set _(_ _**θ** r ,_ _**θ**_ 0 _)_ at each step that satisfies the _e_ -condition and _m_ -projects this set to _M_ 0. It modifies the results toward the satisfaction of the _m_ -condition in the renewal steps. Contrary to this, we may choose _(_ _**θ** r ,_ _**θ**_ 0 _)_ at each step that satisfies the _m_ -condition. Then, we modify them in the renewal steps toward satisfying the _e_ -condition. 

This gives a new algorithm (Ikeda et al. 2004a): 

**1. Initial step** : Assign an initial value _**θ**_[0] 0[. It can be] _**[ θ]**_[0] 0[=][ 0. Do the following iterations] until convergence, for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ **2.** _**m**_ - **condition step** : Inversely _m_ -project _p_ 0 � _**x** ,_ _**θ**[t]_ 0� ∈ _M_ 0 to _Mr_ , that is, to find _pr_ � _**x** ,_ _**θ** r[t]_ � ∈ _Mr_ such that 

**==> picture [225 x 23] intentionally omitted <==**

Then, � _**θ**[t]_ 0 _[,]_ _**[ θ]** r[t]_ � satisfies the _m_ -condition. **3.** Renew the _**θ**[t]_ 0[by] 

**==> picture [246 x 22] intentionally omitted <==**

The _e_ -condition is satisfied when the algorithm converges. 

260 

11 Machine Learning 

The original form proposed by Yuille (2002) is based on a different idea. In analogy with physics, the BP algorithm is proved to search for the critical point of a function _F(_ _**z** )_ called free energy where _**z**_ is the state variables, which in our case is _**z**_ = _(_ _**θ**_ 0 _,_ _**θ**_ 1 _, . . . ,_ _**θ** r )_ (Yedidia et al. 2001). This function is not convex, so there is no guarantee that the gradient descent method converges. Yuille (2002) proved that a function _F(_ _**z** )_ of _**z**_ is always decomposed into a sum of a convex function and a concave function, 

**==> picture [231 x 10] intentionally omitted <==**

The decomposition is not unique. The CCCP is an iterative algorithm for obtaining the critical point of _F_ by 

**==> picture [238 x 13] intentionally omitted <==**

It always converges, whereas BP does not necessarily do so. When it converges, the convergent point satisfies both the _m_ -condition and _e_ -condition. 

The original CCCP algorithm by Yuille is written in our geometrical terminology as follows: 

**==> picture [93 x 13] intentionally omitted <==**

**==> picture [207 x 15] intentionally omitted <==**

where _**θ** r[t]_[+][1] is given by solving 2. 

**==> picture [273 x 23] intentionally omitted <==**

When comparing these with (11.144) and (11.145), _**θ** r[t]_[+][1] is used in (11.148) instead of _**θ** r[t]_[in][(][11.145][).][Hence,][we][need][to][solve][the][nonlinear][equations][to][obtain] _**[θ]**_ 0 _[t]_[+][1] and _**θ** r[t]_[+][1] in one step. After that, we proceed to the next iteration step increasing _t_ by 1. So it includes double loops and is computationally expensive. Our geometrical algorithm is simpler, and does not include the double loops. The approximation errors due to BP or CCCP are analyzed in Ikeda et al. (2004a) by using the curvature. 

## **11.4 Information Geometry of Boosting** 

A single learning machine might not be powerful. There is an idea due to M. Kearns and L. Valiant: A powerful machine might be constructed from a number of weak learning machines by integration. This idea was realized by Freund and Schapire (1997) and Schapire et al. (1998) under the name of “boosting”. It was shown by Lebanon and Lafferty (2001) that information geometry is useful for understanding 

261 

11.4 Information Geometry of Boosting 

the boosting algorithm. The idea was expanded further by Japanese researchers (including Murata et al. 2004; Takenouchi and Eguchi 2004; Kanamori et al. 2007; and Takenouchi et al. 2008). 

## _**11.4.1 Boosting: Integration of Weak Machines**_ 

Consider a pattern classifier, which learns from training examples _D_ = _**x**_ 1 _, y_ 1[∗] _[,]_ {() 

_. . . ,_ _**x** N , yN_[∗] . Here _**x** t_ is an input pattern at time _t_ and _yt_[∗][is][the][correct][answer] 7 corresponding to _**x** t_ , which takes binary values 1 and −1. A classifier uses an analogvalued output function _F(_ _**x** )_ and the output _y_ is decided by the decision function _h(_ _**x** )_ which is the signature of _F(_ _**x** )_ , 

**==> picture [212 x 10] intentionally omitted <==**

Assume that we have _T_ weak machines of which the decision functions are 

**==> picture [245 x 10] intentionally omitted <==**

The performance of a weak machine may be very weak, although its error probability should be less than 0.5. By integrating them, we construct a machine of which the output function is 

**==> picture [210 x 30] intentionally omitted <==**

where _αa_ are parameters to be determined from the data. See Fig. 11.12. We begin with a weak machine and add new weak machines one by one. The weights _αa_ are also determined sequentially. 

There are two problems to be solved. One is how to compose the next weak machine _ht (_ _**x** )_ at time _t_ , and the other is how to determine the weight _αt_ . 

**Fig. 11.12** Integration of weak machines 

**==> picture [171 x 74] intentionally omitted <==**

**----- Start of picture text -----**<br>
h 1( x )<br>h 2( x ) α2α1<br>x . F ( x ) y<br>α T<br>hT  ( x )<br>... ...<br>**----- End of picture text -----**<br>


262 

11 Machine Learning 

## _**11.4.2 Stochastic Interpretation of Machine**_ 

Although a weak learning machine is deterministic, we introduce a stochastic interpretation to evaluate its performance. We consider it as if it were a stochastic machine such that the probability of emitting _y_ is given by 

**==> picture [224 x 25] intentionally omitted <==**

where _c_ is a normalization constant. Obviously, when _F(_ _**x** )_ takes a large positive value, the probability of _y_ = 1 is large and when it takes a negative value with a large magnitude, the probability of _y_ = −1 is large. We rewrite (11.153) as 

**==> picture [249 x 25] intentionally omitted <==**

where _y_[∗] _(x)_ is the true output value to _**x**_ and 

**==> picture [223 x 25] intentionally omitted <==**

Note that _c_[′] does not depend on _y_ . Since an error occurs when _y_ = − _y_[∗] , the probability of error for _**x**_ is 

**==> picture [238 x 13] intentionally omitted <==**

We define the loss caused by a machine for input _**x**_ 

**==> picture [222 x 13] intentionally omitted <==**

by neglecting the constant _c_[′] . We normalize the losses for all the data as 

**==> picture [209 x 21] intentionally omitted <==**

where 

**==> picture [201 x 23] intentionally omitted <==**

Then, _W (_ _**x** i )_ is a distribution of losses over the training examples such that their sum is normalized to 1. 

263 

11.4 Information Geometry of Boosting 

Let _I_ − be the set of indices _i_ such that _**x** i_ are erroneously answered by machine _F(_ _**x** )_ . The performance of the machine is evaluated by the error probability 

**==> picture [203 x 23] intentionally omitted <==**

## _**11.4.3 Construction of New Weak Machines**_ 

The weak machines are constructed one by one. Assume that we have constructed _t_ weak machines _h_ 1 _(_ _**x** ), . . . , ht (_ _**x** )_ and integrated them into the current machine 

**==> picture [211 x 29] intentionally omitted <==**

The performance of a machine is evaluated by the error distribution given by 

**==> picture [233 x 23] intentionally omitted <==**

It is reasonable to add a new machine of which the performance is good for those examples that are bad in the current machine. 

To this end, we set up a new machine and train it using the training examples _D_ , but patterns _**x** i_ ∈ _D_ are applied not equally, but with frequency _Wt (_ _**x** i )_ . This implies that the new training examples are generated from _D_ by resampling such that those which are difficult for the current machine appear frequently. Any type of machine can be used as a new weak machine to be trained, a simple or multilayer perceptron, a support vector machine, a decision tree, and others. 

## _**11.4.4 Determination of the Weights of Weak Machines**_ 

We add a newly trained weak machine _ht_ +1 _(_ _**x** )_ to the previous weak machines, forming a new machine 

**==> picture [240 x 30] intentionally omitted <==**

264 

11 Machine Learning 

**Fig. 11.13** Determination of weight _α_ 

**==> picture [203 x 61] intentionally omitted <==**

Here, _α_ is the parameter to be decided. The conditional probability of _y_ by the new machine is 

**==> picture [327 x 25] intentionally omitted <==**

This forms a one-dimensional exponential family _Et_ +1 where the _e_ -coordinate is _α_ . Therefore, given the training data _D_ , the best distribution to fit the training data is given by the _m_ -projection of the empirical distribution of data to the exponential family _Et_ +1. See Fig. 11.13. 

The coefficient _c_ in (11.164) is a complicated function of _α_ and _D_ . We ignore this term, considering _Et_ +1 as a family of unnormalized positive measures, 

**==> picture [282 x 25] intentionally omitted <==**

Then, the optimum solution is obtained by _m_ -projecting 

**==> picture [250 x 22] intentionally omitted <==**

to _Et_ +1, that is, by minimizing _K L_ � _p_ emp : _q(y_ | _**x** , α)_ �. From 

**==> picture [283 x 31] intentionally omitted <==**

where _c_ is ignored, the KL-divergence is written as 

**==> picture [295 x 105] intentionally omitted <==**

265 

11.4 Information Geometry of Boosting 

where _C_ is a term not depending on _α_ . Since _yi_[∗][=] _[y]_[∗] _[(]_ _**[x]**[i][)]_[ and the objective function] to be minimized is 

**==> picture [300 x 24] intentionally omitted <==**

by differentiating it with respect to _α_ , we have 

**==> picture [251 x 23] intentionally omitted <==**

We introduce a new index set _I_ − _[t]_[+][1] such that _i_ ∈ _I_ − _[t]_[+][1] implies that pattern _**x** i_ is wrongly classified by the new machine _ht_ +1, that is, 

**==> picture [204 x 11] intentionally omitted <==**

Let us put 

**==> picture [261 x 24] intentionally omitted <==**

Then, (11.170) reduces to 

**==> picture [230 x 11] intentionally omitted <==**

We obtain the solution 

**==> picture [287 x 82] intentionally omitted <==**

The weight of example _**x** i_ is renewed as 

## **11.5 Bayesian Inference and Deep Learning** 

Information geometry of Bayesian statistics has not yet been well developed except for preliminary studies (e.g., Zhu and Rohwer 1995). Bayesian theory regards data and parameters as random variables at the same time. Hence, information geometry is applied to their joint probability distributions. It is hoped to construct a deeper structure beyond superficial Bayesian information geometry, which would be useful for machine learning, in particular for deep learning. This section proposes a preliminary trial concerning information geometry of Bayesian statistics. We use the restricted Boltzmann machine (RBM) for this purpose, which is an important constituent in deep learning. 

266 

11 Machine Learning 

## _**11.5.1 Bayesian Duality in Exponential Family**_ 

An exponential family of probability distributions is represented by 

**==> picture [243 x 14] intentionally omitted <==**

where _**x**_ is a vector random variable, _**θ**_ is a vector parameter and _k_[¯] _(_ _**x** )_ corresponds to the underlying measure of _**x**_ , 

**==> picture [220 x 14] intentionally omitted <==**

Bayesian statistics assumes that the parameter _**θ**_ is also a random variable subject to a prior distribution _π(_ _**θ** )_ . Then, the joint probability of _**θ**_ and _**x**_ is 

**==> picture [244 x 13] intentionally omitted <==**

where 

**==> picture [218 x 12] intentionally omitted <==**

The Bayesian posterior distribution is the conditional distribution of _**θ**_ given _**x**_ and is written as 

**==> picture [243 x 13] intentionally omitted <==**

where 

**==> picture [218 x 38] intentionally omitted <==**

Itisanexponentialfamily,wheretherandomvariableis _**θ**_ andthenaturalparameterto specify a distribution is _**x**_ . Although the roles of _**θ**_ and _**x**_ are different, the conditional distributions have the same exponential form shown in (11.176) and (11.180). We call it the Bayesian duality. 

The _e_ -affine parameter is _**θ**_ in the manifold of probability distributions (11.176) and hence, the dual _m_ -affine parameter is 

**==> picture [226 x 24] intentionally omitted <==**

whereas, the _e_ -affine parameter is _**x**_ in the manifold of the posterior probability distributions (11.180) and hence the _m_ -affine parameter is the conditional posterior expectation of _**θ**_ , 

**==> picture [227 x 23] intentionally omitted <==**

11.5 Bayesian Inference and Deep Learning 

267 

We extend (11.178) to a family of joint probability distributions parameterized by a hyper parameter _**ζ**_ . Then, _M_ = { _p(_ _**x** ,_ _**θ**_ ; _**ζ** )_ } forms a manifold consisting of exponential families. Its simple example is the case when a prior distribution _π(_ _**θ** )_ is given in a parametric form as _π(_ _**θ** ,_ _**ζ** )_ . Here, the extra parameter _**ζ**_ is called a hyper parameter. A family of prior distributions called conjugate priors is used sometimes, because of its simplicity. A conjugate prior _π(_ _**θ** ,_ _**ζ** )_ has the same form as the conditional distribution _p(_ _**θ**_ | _**x** )_ . In our exponential case, because of (11.180), the conjugate prior is written as 

**==> picture [255 x 10] intentionally omitted <==**

where _**ζ**_ = _(_ _**α** , β)_ is the hyper parameter and _χ(_ _**α** , β)_ is a normalization factor. When we use _N_ independent observations _D_ = { _**x**_ 1 _,_ _**x**_ 2 _, . . . ,_ _**x** N_ }, the posterior distribution under prior _π(_ _**θ** ,_ _**α** , β)_ is explicitly given by 

**==> picture [315 x 10] intentionally omitted <==**

where 

**==> picture [195 x 22] intentionally omitted <==**

is the observed point. This makes the role of the conjugate prior clear: The conjugate prior has the effect of shifting the observed point from _**x**_ ¯ to _**x**_ ¯ + _**α** /N_ , that is, of adding _β_ additional pseudo-observations of which the observed value is _**α** /β_ to the previous _N_ ¯ _**x**_ . Alternatively, observed data _D_ change the parameter of the conjugate prior as follows: 

**==> picture [229 x 10] intentionally omitted <==**

The geometry of the conjugate prior is studied by Agarwal and Daumé III (2010). We can enlarge our framework by considering a curved exponential family, where _**θ**_ is specified by a low-dimensional parameter _**u**_ such that 

**==> picture [188 x 10] intentionally omitted <==**

The random variable _**x**_ may be an embedded version of low-dimensional signals _**v**_ , 

**==> picture [187 x 10] intentionally omitted <==**

Then, probability distributions of _**u**_ and _**v**_ form a curved exponential family. 

We may further consider an extended family of distributions such that a joint distribution (11.178) is specified by an additional parameter _W_ as _p(_ _**x** ,_ _**θ**_ ; _W )_ . We use this as a model of machine learning or the brain. Here, _**x**_ or _**x** (_ _**v** )_ is information given from the environment. _**θ**_ or _**θ** (_ _**u** )_ represents a higher-order concept which specifies the distribution of _**x**_ . An inference system guesses _**θ**_ from _**x**_ such that _**x**_ is generated from _p(_ _**x**_ | _**θ** )_ . See Fig. 11.14. This is a simple layered model of the brain, 

268 

11 Machine Learning 

**Fig. 11.14** Bayesian inference of higher information _**θ**_ from _**x**_ 

**==> picture [232 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
( h )<br>generative<br>inference<br>x ( v )<br>input<br>**----- End of picture text -----**<br>


where _**x**_ is given to an input layer and _**θ**_ is generated in the next layer by Bayesian inference. There may be feedback connections from the higher-order layer to the lower-order layer so that a dynamical process takes place between them. The RBM is its stochastic model. 

## _**11.5.2 Restricted Boltzmann Machine**_ 

The Boltzmann machine was proposed by Ackley et al. (1985). It is a Markov chain over state _**x**_ , of which the stable distribution is given by 

**==> picture [253 x 25] intentionally omitted <==**

where _**c**_ is a vector and **W** is a symmetric matrix. 

The restricted Boltzmann machine (RBM) is a layered machine consisting of two layers and there are no interactions among elements (we call them neurons) within each layer. Interactions (connections) exist only between neurons of different layers. This was proposed by Smolensky (1986) and has been extensively used in deep learning (Hinton and Salakhutdinov 2006 and others). 

We divide _**x**_ into two parts, _**x**_ = _(_ _**v** ,_ _**h** )_ , where _**v**_ and _**h**_ are binary vector random variables representing activities of neurons of the two layers in the RBM (Fig. 11.15). The first layer is called an input layer or visible layer, to which a signal _**v**_ is applied from the environment. The second layer is called a hidden layer of which activity pattern _**h**_ is generated from input _**v**_ in the first layer. 

The stable probability distribution of an RBM is written as 

**==> picture [310 x 13] intentionally omitted <==**

since there are no connections among the neurons in each layer. This is an exponential family of distributions. The stable probabilities of _**v**_ and _**h**_ are given by its marginal probability distributions, 

11.5 Bayesian Inference and Deep Learning 

269 

**Fig. 11.15** RBM (restricted Boltzmann machine) 

**==> picture [23 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
h<br>W<br>v<br>**----- End of picture text -----**<br>


**==> picture [20 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
input<br>**----- End of picture text -----**<br>


**==> picture [211 x 50] intentionally omitted <==**

and they are not of the exponential type. 

We compare the RBM with the Bayesian scheme in the previous section. When the number _m_ of neurons in the hidden layer is smaller than the number _n_ in the visible layer, we introduce new random variables by 

**==> picture [186 x 25] intentionally omitted <==**

In the opposite case, we introduce 

**==> picture [190 x 27] intentionally omitted <==**

In either case, the stationary probability distribution is written in the standard form (11.178) of Bayesian joint distribution. Therefore, we may consider an RBM as representing the Bayesian mechanism of statistical inference. 

## _**11.5.3 Unsupervised Learning of RBM**_ 

For an RBM having the stationary joint probability (11.192), we have the two conditional distributions 

**==> picture [241 x 51] intentionally omitted <==**

11 Machine Learning 

270 

They show the probabilities of activities of one layer given the activities of the other layer. Let _q(_ _**v** )_ be a probability distribution of _**v**_ given from the environment, subject to which input _**v**_ is generated. An RBM is trained by receiving _**v**_ such that its stationary marginal distribution _pV (_ _**v**_ ; _**a** ,_ _**b** ,_ **W** _)_ approximates _q(_ _**v** )_ . This is done by modifying **W** _,_ _**a**_ and **b** so that the KL-divergence _DK L_ [ _q(_ _**v** )_ : _pV (_ _**v** ,_ _**a** ,_ _**b** ,_ **W** _)_ ] is minimized. The minimizing **W** _,_ _**a** ,_ _**b**_ are the maximum likelihood estimator. For the sake of notational simplicity, we hereafter neglect the bias terms _**a**_ and _**b**_ by making them equal to 0, but they can be treated in a similar manner. This is only for the purpose of avoiding unnecessary complication. 

Let _MV_ be a submanifold consisting of the marginal probability distributions of _**v**_ of the RBM, 

**==> picture [201 x 10] intentionally omitted <==**

in the entire manifold _SV_ of probability distributions of _**v**_ . The minimizer **W** of the KL-divergence _DK L_ [ _q(_ _**v** )_ : _p(_ _**v** ,_ **W** _)_ ] is given by the _m_ -projection of _q(_ _**v** )_ to the submanifold _MV_ (Fig. 11.16). However, it is simpler to treat the manifold of joint distributions of _(_ _**v** ,_ _**h** )_ rather than the marginal distributions of _**v**_ . To this end, we consider a manifold _SV,H_ consisting of all joint probability distributions of _**v**_ and _**h**_ . We study two submanifolds in it. One is the submanifold of the RBM, 

**==> picture [213 x 11] intentionally omitted <==**

parameterized by **W** . The other is the data submanifold _MV,H_ | _q_ given by 

**==> picture [216 x 11] intentionally omitted <==**

where _q(_ _**v** )_ is fixed and _r (_ _**h**_ | _**v** )_ is anarbitraryconditional distributionof _**h**_ conditioned on _**v**_ . The marginal distribution of any member of _MV,H_ | _q_ is _q(_ _**v** )_ . Consider the KLdivergence between the two submanifolds, 

**Fig. 11.16** _m_ -projection of _q(_ _**v** )_ to _MV_ 

**==> picture [114 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
SV . q ( v )<br>m -projection<br>M V<br>. W<br>**----- End of picture text -----**<br>


11.5 Bayesian Inference and Deep Learning 

271 

**==> picture [309 x 17] intentionally omitted <==**

**Theorem 11.9** _TheminimizersoftheKL-divergence DK L_ � _MV,H_ | _q_ : _MV,H_ � _between two submanifolds are given by r (_ _**h**_ | _**v** )_ = _p(_ _**h**_ | _**v** ,_ **W**[ˆ] _) and p(_ _**v** ,_ _**h** ,_ **W**[ˆ] _), where_ **W**[ˆ] _is the MLE of pV (_ _**v** ,_ **W** _) for data_ _**v** generated from q(_ _**v** )._ 

_Proof_ We can decompose _DK L_ as follows: 

**==> picture [319 x 93] intentionally omitted <==**

Therefore, the minimum of the _DK L_ with respect to _r (_ _**h**_ | _**v** )_ is attained by _p (_ _**h**_ | _**v** ,_ **W** _)_ and the minimum with respect to **W** is attained by the minimizer of _DK L_ [ _q(_ _**v** )_ : _p(_ _**v** ,_ **W** _)_ ]. □ 

ˆ ˆ ˆ Let _q_ = _q(_ _**v** )r (_ _**v**_ | _**h** )_ and _p_ = _p_ _**v** ,_ _**h** ,_ **W**[ˆ] be the closest pair of _DK L_ � � of� _MVp_ ˆ _,_ . _H_ This| _q_ : _M_ is _V,_ clear _H_ �. Then,from _p_ ˆthe is given by the _em_ (EM) algorithm _m_ -projection ofin the _q_ ˆpresence and _q_ ˆ is theof _e_ hidden-projectionvariable _**h**_ , since the _e_ -projection keeps the conditional probability _p(_ _**h**_ | _**v** ,_ **W** _)_ and the _m_ -projection maximizes the log likelihood. See Fig. 11.17, where the minimization problem in _SV,H_ is mapped onto that in _SV_ . 

We now give the learning algorithm established by Ackley et al. (1985). This is the stochastic descent method of _DK L_ . 

**Theorem 11.10** _The averaged learning rule of RBM is given by_ 

**==> picture [231 x 13] intentionally omitted <==**

_where ε is a learning constant,_ ⟨ _hi v j_ ⟩ _q is the average of hi v j subject to the joint probability distribution_ 

**==> picture [228 x 10] intentionally omitted <==**

_and_ ⟨ _hi v j_ ⟩ _p is the average over the stationary distribution p(_ _**v** ,_ _**h** ,_ **W** _) of the RBM._ 

11 Machine Learning 

272 

**==> picture [311 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
SVH SV<br>. . q ( v )<br>MV , H|q<br>m -projection<br>m -projection e -projection<br>.<br>. W MV<br>MV , H<br>**----- End of picture text -----**<br>


**Fig. 11.17** Minimizer of _DK L MV,H_ | _V_ : _HV,H_ 

_Proof_ Since we have 

we have 

because 

**==> picture [328 x 205] intentionally omitted <==**

This is the ordinary gradient descent method. The natural gradient method would work better, if we had its computational algorithm. Since the learning rule (11.206) includes only the expectation of the cross term of _**v**_ and _**h**_ with respect to _p(_ _**v** ,_ _**h** ,_ **W** _)_ and _q(_ _**v** ,_ _**h** ,_ **W** _)_ , all the other higher-order interaction terms are irrelevant. Therefore, this suggests the use of a mixed coordinate system, which separates the second-order terms from higher-order terms of interactions (see Akaho and Takabatake 2008). 

11.5 Bayesian Inference and Deep Learning 

273 

## _**11.5.4 Geometry of Contrastive Divergence**_ 

The learning algorithm (11.206) is computationally heavy. This is because, in order to calculate the expectation of ⟨ _**hv**[T]_ ⟩ _p_ , we need a long run of MCMC procedures for obtaining samples from the stable distribution _p(_ _**v** ,_ _**h** ,_ **W** _)_ . The MCMC procedures work as follows: 

1. Begin with an arbitrary _**v** t_ and generate _**h** t_ by using the conditional distribution _p(_ _**h**_ | _**v** ,_ **W** _)_ . 

2. Generate _**v** t_ +1 from the current _**h** t_ by using the conditional distribution _p(_ _**v**_ | _**h** ,_ **W** _)_ . 

3. Repeat the procedures, _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . 

We then have a sequence of _(_ _**v** t ,_ _**h** t )_ of which the empirical distribution converges to _p(_ _**v** ,_ _**h** ,_ **W** _)_ . These data can be used to calculate the average ⟨ _**hv**[T]_ ⟩ _p_ in (11.206) or (11.209). 

The contrastive divergence is an approximation of the KL-divergence, proposed by Hinton (2002). This has been used frequently in deep learning. It runs a finite number, say _k_ , of iterations of the above procedures. The order _k_ contrastive divergence ( _C Dk_ ) uses a pair of _(_ _**v** k,_ _**h** k)_ , where _**v**_ 0 is derived from _q(_ _**v** )_ as an initial value, _**h** t_ is derived from _p (_ _**h**_ | _**v** t_ ; **W** _)_ and _**v** t_ +1 is derived from _p (_ _**v**_ | _**h** t_ ; **W** _)_ . Repeating the procedures up to _t_ = _k_ from many initial _**v**_ ’s, the derived empirical distribution of _(_ _**v** k,_ _**h** k)_ is used to obtain an approximation of ⟨ _**hv**[T]_ ⟩ _p_ . 

We study the probability distribution _pk(_ _**v** ,_ _**h** ,_ **W** _)_ of _(_ _**v** k,_ _**h** k)_ , which we call the _C Dk_ distribution, following Karakida et al. (2014). Let its marginal distributions be _pV k(_ _**v** ,_ **W** _)_ and _pHk(_ _**h** ,_ **W** _)_ . They are 

**==> picture [236 x 50] intentionally omitted <==**

Then, the _C D j_ distributions are calculated recursively by 

**==> picture [275 x 26] intentionally omitted <==**

In order to understand the _C Dk_ distributions, we consider two submanifolds _MH_ | _V (_ **W** _)_ and _M_[˜] _V_ | _H (_ **W** _)_ in _SV,H_ . They are defined by 

**==> picture [231 x 27] intentionally omitted <==**

where _r (_ _**v** )_ and ˜ _r (_ _**h** )_ arearbitrarydistributions.Theyintersectat _p(_ _**v** ,_ _**h** ,_ **W** _)_ ,because, when _r (_ _**v** )_ = _pV (_ _**v** ,_ **W** _)_ and when ˜ _r (_ _**h** )_ = _pH (_ _**h** ,_ **W** _)_ , both the distributions are equal to _p(_ _**v** ,_ _**h** ,_ **W** _)_ . Moreover, both _MH_ | _V_ and _M_[˜] _V_ | _H_ are _e_ -flat, because the _e_ -geodesic 

11 Machine Learning 

274 

**Fig. 11.18** CDR distribution _Pk (_ _**v** ,_ _**h** ,_ **W** _)_ 

**==> picture [173 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
SV , H<br>MH | V [(] W ) M ~ H | V [(] W )<br>p 0 [(] v , h , W )<br>e -flat<br>e -flat ~<br>p 1 [(] v , h , W )<br>p 1 ( v , h , W )<br>p ~2( v , h , W )<br>p 2 [(] v , h , W )<br>MV , H<br>. W<br>m -projection<br>m -projection<br>...<br>**----- End of picture text -----**<br>


connecting _r_ 1 _(_ _**v** ) p(_ _**h**_ | _**v** )_ and _r_ 2 _(_ _**v** ) p(_ _**h**_ | _**v** )_ , 

_t_ {log _r_ 1 _(_ _**v** ) p(_ _**h**_ | _**v** )_ } + _(_ 1 − _t)_ {log _r_ 2 _(_ _**v** ) p(_ _**h**_ | _**v** )_ } = | log _r_ 1 _(_ _**v** )[t] r_ 2 _(_ _**v** )_[1][−] _[t] p(_ _**h**_ | _**v** ) ,_ (11.217) 

is included in _MH_ | _V_ , where we have omitted the normalization factor _c(t)_ . The same situation holds for _M_[˜] _V_ | _H_ . See Fig. 11.18. 

The initial distribution is given by putting _p_ 0 _(_ _**v** )_ = _q(_ _**v** )_ as 

**==> picture [233 x 10] intentionally omitted <==**

Then, the sequence of _C Dk_ distributions is given by the geometrical procedures in the following theorem, due to R. Karakida. 

˜ **Theorem 11.11** _p j (_ _**v** ,_ _**h** ,_ **W** _) is the m-projection of p j_ −1 _(_ _**v** ,_ _**h** ,_ **W** _) to M_[˜] **H** | **V** _(_ **W** _) and p j (_ _**v** ,_ _**h** ,_ **W** _) is the m-projection of p_ ˜ _j (_ _**v** ,_ _**h** ,_ **W** _) to M_ **V** | **H** _(_ **W** _)._ 

_Proof_ Given _p_ ˜ _j (_ _**v** ,_ _**h** ,_ **W** _)_ , its _m_ -projection to _M_ **H** | **V** is given by the minimizer of 

> _DK L_ [1 _p_ ˜ _j (_ _**v** ,_ _**h** ,_ **W** _)_ : _r (_ _**v** ) p(_ _**h**_ | _**v** )_ = − _p_ ˜ _j (_ _**v** ,_ _**h** ,_ **W** _)_ log _r (_ _**v** )d_ _**v** d_ _**h**_ + _c_ (11.219) | with respect to _r (_ _**v** )_ , where _c_ is a term not depending on _r (_ _**v** )_ . By adding the constraint 

**==> picture [196 x 23] intentionally omitted <==**

11.5 Bayesian Inference and Deep Learning 

275 

the variation of _DK L_ gives 

**==> picture [333 x 34] intentionally omitted <==**

The theorem shows that _p j (_ _**v** ,_ _**h** ,_ **W** _)_ converges to _p(_ _**v** ,_ _**h** ,_ **W** _)_ as _j_ increases. Hence, _p j (_ _**v** ,_ _**h** ,_ **W** _)_ may be used as an approximation of _p(_ _**v** ,_ _**h** ,_ **W** _)_ in calculations of ⟨ _**hv**[T]_ ⟩ _p_ . 

The following is an interesting observation based on the Pythagorean theorem. 

**Theorem 11.12** _The KL-divergence from p_ 0 _(_ _**v** ,_ _**h** ,_ **W** _) to p(_ _**v** ,_ _**h** ,_ **W** _) is decomposed as_ 

**==> picture [303 x 24] intentionally omitted <==**

_Proof_ Since _p_ ˜ _j p j p_ is an orthogonal triangle in which the _m_ -geodesic _p_ ˜ _j p j_ is orthogonal to the _e_ -geodesic _p j p_ , we can apply the Pythagorean theorem to decompose _DK L_ � _p_ ˜ _j_ : _p_ � (Fig. 11.17). Similar decomposition holds for _DK L_ � _p j_ : _p_ �. Hence, repeating the decomposition recursively, we have the theorem. □ 

## _**11.5.5 Gaussian RBM**_ 

We may consider an analog RBM in which both _**v**_ and _**h**_ take analog values. A typical one is a Gaussian RBM in which both _**v**_ and _**h**_ are Gaussian random variables. The stationary distribution is written as 

**==> picture [302 x 31] intentionally omitted <==**

Here, the quadratic terms of _**v**_ and _**h**_ exist but they do not include cross terms such as _vi v j (i_ ̸= _j)_ , so that there are no mutual connections among the neurons in each layer. 

The Gaussian RBM is simple and hence tractable, because all related distributions are described in the framework of Gaussian distributions. The conditional distributions are Gaussian given by 

**==> picture [261 x 59] intentionally omitted <==**

276 

11 Machine Learning 

and the marginal distribution is also Gaussian, 

**==> picture [262 x 26] intentionally omitted <==**

where _c_ , _c_[′] and _c_[′′] are adequate constants. 

Karakida et al. (2014) analyzed the behavior of the Gaussian RBM when the distribution _q(_ _**v** )_ of _**v**_ given from the outside is mean 0 and its covariance matrix is **C** . Since 

**==> picture [223 x 24] intentionally omitted <==**

**==> picture [224 x 15] intentionally omitted <==**

hold, the equation of learning (11.206) is written as 

**==> picture [238 x 24] intentionally omitted <==**

where we use continuous time. They also calculated the equation of learning for _C Dk_ , obtaining 

**==> picture [321 x 31] intentionally omitted <==**

We can easily see that (11.230) converges to (11.229) as _k_ tends to infinity. 

We study the equilibrium solutions and their stability for the above equations. The following theorem shows that a Gaussian RBM performs a PCA-like analysis. To this end, let _λ_ 1 _, . . . , λn_ be _n_ eigenvalues of **C** (where we assume that they are all distinct) and let **O** be the orthogonal matrix that diagonalizes **C** , 

**==> picture [193 x 11] intentionally omitted <==**

**Theorem 11.13** _Assume that there arer eigenvalues which are larger than σv_[2] _[. Then,] the equilibrium solutions of (11.229) and (11.230) are the same, given by_ 

**==> picture [192 x 12] intentionally omitted <==**

_where_ **U** _is an arbitrary m_ × _m orthogonal matrix and_ 

**==> picture [300 x 32] intentionally omitted <==**

11.5 Bayesian Inference and Deep Learning 

277 

The proof is technical and is omitted (see Karakida et al. 2014). The stability of solutions is also analyzed. 

By choosing the coordinate axes of _**v**_ adequately, we see that the marginal distribution of RBM is given: 

**==> picture [259 x 31] intentionally omitted <==**

This shows that the Gaussian RBM performs the PCA analysis, neglecting smaller eigenvalues. It is also shown that the _C D_ 1 learning method has a sufficiently good performance compared to the original RBM learning method (maximum likelihood method). 

## **Remarks** 

We have glanced at topics of machine learning from the information geometry point of view. Since stochastic uncertainty is involved in the real world, it is expected that information geometry will provide good ideas, useful suggestions and clear understanding of aspects of machine learning. Clustering techniques are the main tools of information retrieval, where divergence functions are used. They are connected with information geometry. We have demonstrated that robust clustering is achieved by tBD. This field is developing quickly. See Nock et al. (2015). 

Support vector machines are useful tools in pattern recognition and regression. We have avoided following the main stream of the kernel method and instead touched upon how the performance of a kernel is improved by a conformal transformation. This might give a hint for a good choice of kernels. 

Stochastic reasoning is an important procedure, where belief propagation (BP) plays akeyrole. WecanreformulatetheBPalgorithm byusinginformationgeometry. This gives a more transparent understanding of the algorithm than the conventional one. Moreover, it provides an efficient algorithm of stochastic inference, which is a new version of the convex–concave computational procedure (CCCP). The boosting of weak learners is also outlined. 

Deep learning is a hot topic, for which we still lack convincing theories. We have proposed a way to understand it from information geometry of Bayesian statistics. The restricted Boltzmann machine (RBM) is understood in the framework of Bayesianinformationgeometry.Karakidaetal.(2014;2016)studiedtheperformance of the Gaussian–Bernoulli RBM and showed that it performs ICA in restricted situations. However, this still remains as a half-baked idea, emerging in the last stage of completing this monograph. The geometry of contrast divergences is mostly due to on-going research by R. Karakida (PhD student at the University of Tokyo) and it might be too early to be included here. In order to understand deep learning, we 

11 Machine Learning 

278 

need to construct a good model of _q(_ _**v** )_ which involves hierarchical structure. Hierarchies of hidden layers unveil their hidden structure one layer at a time. This is unsupervised learning. The supervised aspect of deep learning is related to singularities existing ubiquitously in a neuromanifold, and will be one of the main topics of the next chapter. 

## **Chapter 12 Natural Gradient Learning and Its Dynamics in Singular Regions** 

Learning takes place in a parameter space, which is not Euclidean in general but Riemannian. Therefore, we need to take the Riemannian structure into account when designing a learning method. The natural gradient method, which is a version of stochastic descent learning, is proposed for this purpose, using the Riemannian gradient. It is a Fisher efficient on-line method of estimation. Its performance is excellent in general and it has been used in various types of learning problems such as neural learning, policy gradient in reinforcement learning, optimization by means of stochastic relaxation, independent component analysis, Monte Carlo Markov Chain (MCMC) in a Riemannian manifold and others. 

Some statistical models are singular, implying that its parameter space includes singular regions. The multilayer perceptron (MLP) is a typical singular model. Since supervised learning of MLP is involved in deep learning, it is important to study the dynamical behavior of learning in singular regions, in which learning is very slow. This is known as plateau phenomena. The natural gradient method overcomes this difficulty. 

## **12.1 Natural Gradient Stochastic Descent Learning** 

## _**12.1.1 On-Line Learning and Batch Learning**_ 

Huge amounts of data exist in the real world. Consider a set of data which are generated randomly subject to a fixed but unknown probability distribution. A typical example is shown in the regression problem, where input signal _**x**_ is generated randomly, accompanied by a desired response _f (_ _**x** )_ . A teacher signal _y_ , which is a noisy version of the desired output _f (_ _**x** )_ , 

_y_ = _f (_ _**x** )_ + _ε,_ (12.1) © Springer Japan 2016 279 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8_12 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

280 

is given together with _**x**_ , where _ε_ is random noise. The task of a learning machine is, in this case, to estimate the desired output mapping _f (_ _**x** )_ by using the available examples of input–output pairs _D_ = { _(_ _**x** i , yi ) , i_ = 1 _,_ 2 _, . . . , T_ }, called training examples. They are subject to an unknown joint probability distribution, 

**==> picture [266 x 10] intentionally omitted <==**

where _q(_ _**x** )_ is the probability distribution of _**x**_ and _pε(ε)_ is the probability distribution of noise _ε_ , typically Gaussian. This is a usual scheme of supervised learning. 

We use a parameterized family _f (_ _**x** ,_ _**ξ** )_ of functions as candidates for the desired output, where _**ξ**_ is a vector parameter. The set of _**ξ**_ is a parameter space and we search for the optimal _**ξ**_[ˆ] that approximates the true _f (_ _**x** )_ by using training examples _D_ . When _y_ takes an analog value, this is a regression problem. When _y_ is discrete, say binary, this is pattern recognition. 

In order to evaluate the performance of machine _f (_ _**x** ,_ _**ξ** )_ , we define a loss function or cost function. The instantaneous loss of processing _**x**_ by machine _f (_ _**x** ,_ _**ξ** )_ is typically given by 

**==> picture [230 x 21] intentionally omitted <==**

in the case of regression, which is a half of the square of the difference between the teacher output _y_ and machine output _f (_ _**x** ,_ _**ξ** )_ . 

The loss function of machine _**ξ**_ is the expectation of the instantaneous loss over all possible pairs _(_ _**x** , y)_ , 

**==> picture [214 x 11] intentionally omitted <==**

where the expectation is taken with respect to the unknown joint probability distribution _p(_ _**x** , y)_ . However, since we do not know _p(_ _**x** , y)_ , we use the average over the training data, 

**==> picture [228 x 30] intentionally omitted <==**

This is called the training error, since the average loss is evaluated by using the data that we used for training. In contrast, (12.4) is called the generalization error, since it evaluates the performance over all possible data _(_ _**x** , y)_ not used in the process of training. Since we do not know _L_ , we minimize the training error _L_ train to obtain _**ξ**_[ˆ] . A regularization term may be added to _L_ train in order to obtain a regularized optimal solution _**ξ**_[ˆ] by learning. 

A loss function is defined similarly in the case of pattern recognition by the expectation of an instantaneous loss. Even in the case of binary _y_ , _y_ = 0 or 1, we can use (12.3) as a loss. However, it is more natural to formulate the problem in terms of logistic regression such that the probability of _y_ is given as a function of _**ξ**_ · _**x**_ by 

**==> picture [251 x 10] intentionally omitted <==**

12.1 Natural Gradient Stochastic Descent Learning 

281 

where the normalization factor _ψ_ is 

**==> picture [232 x 10] intentionally omitted <==**

This implies 

**==> picture [243 x 24] intentionally omitted <==**

The instantaneous loss function is the negative of log Prob { _y_ | _**ξ**_ · _**x**_ }, 

**==> picture [233 x 10] intentionally omitted <==**

In the problem of estimation of parameters _**ξ**_ in a statistical model { _p(_ _**x** ,_ _**ξ** )_ }, we use 

**==> picture [216 x 10] intentionally omitted <==**

the negative of log likelihood, where only _**x**_ ’s are observed. The generalization error is 

**==> picture [223 x 13] intentionally omitted <==**

where _**ξ**_ 0 is the true parameter, such that _**x**_ is generated from _p_ � _**x** ,_ _**ξ**_ 0�. The regression problem is regarded as an estimation problem to estimate _**ξ**_ of _p(_ _**x** , y_ ; _**ξ** )_ , where random variables are _(_ _**x** , y)_ and we do not care about _q(_ _**x** )_ . 

An on-line learning procedure modifies the current candidate _**ξ** t_ at time _t_ to obtain _**ξ** t_ +1 at the next time based on the current training example _(_ _**x** t , yt )_ so as to decrease the instantaneous loss (Rumelhart et al. 1986). Usually, the negative of the gradient is used to update _**ξ** t_ , 

**==> picture [227 x 13] intentionally omitted <==**

where ∇ is the gradient with respect to _**ξ**_ and coefficient _ηt_ is called a learning constant, which may depend on _t_ . Since training data are given one by one, the change 

**==> picture [218 x 13] intentionally omitted <==**

is a random variable depending on _(_ _**x** t , yt )_ . The expectation of ∇ _l_ is equal to ∇ _L(_ _**ξ** )_ . Therefore, the change _Δ_ _**ξ** t_ is random but its expectation is in the direction of −∇ _L_ � _**ξ** t_ �. See Fig. 12.1. Hence, (12.12) is called a stochastic descent learning method. Amari (1967) might be the first to have used this idea for training a multilayer perceptron. The method is now well established as the back-propagation learning method. 

Natural Gradient Learning and Its Dynamics in Singular Regions 

282 

12 

**Fig. 12.1** Gradient descent of expected loss _L_ and stochastic gradient descent of _l_ 

**==> picture [214 x 72] intentionally omitted <==**

**----- Start of picture text -----**<br>
L<br>ξ<br>ξ<br>l .<br>ξ ξ . .<br>. . .<br>**----- End of picture text -----**<br>


A batch learning procedure is an iterative method which uses all the training data for modifying _**ξ** t_ at one step, such that _**ξ** t_ is modified to _**ξ** t_ +1 by 

**==> picture [237 x 30] intentionally omitted <==**

The two types of learning, batch and on-line, have different merits and demerits. 

## _**12.1.2 Natural Gradient: Steepest Descent Direction in Riemannian Manifold**_ 

Given a function _L(_ _**ξ** )_ in a manifold, it is widely believed that the gradient 

**==> picture [204 x 24] intentionally omitted <==**

is the direction of the steepest change of _L(_ _**ξ** )_ . In a geographical map with contour lines, the steepest direction is given by the gradient of the height function _H (_ _**ξ** )_ , that is ∇ _H (_ _**ξ** )_ , which is orthogonal to contour lines. However, this is true only when an orthonormal coordinate system is used in a Euclidean space. 

In a Riemannian manifold, the square of local distance between two nearby points _**ξ**_ and _**ξ**_ + _d_ _**ξ**_ is given by the quadratic form 

**==> picture [202 x 13] intentionally omitted <==**

where **G** = � _gi j_ � is a Riemannian metric tensor. Note that we use the Einstein convention so that the summation symbol[�] is omitted in (12.16). Let us change the current point _**ξ**_ to _**ξ**_ + _d_ _**ξ**_ , and see how the value of _L(_ _**ξ** )_ changes, depending on the direction _d_ _**ξ**_ . We search for the direction in which _L_ changes most rapidly. In order to make a fair comparison, the step-size of _d_ _**ξ**_ should have the same magnitude in all directions, so that the length of _d_ _**ξ**_ should be the same, 

**==> picture [206 x 13] intentionally omitted <==**

12.1 Natural Gradient Stochastic Descent Learning 

283 

where _ε_ is a small constant. We put _d_ _**ξ**_ = _ε_ _**a**_ and require that 

**==> picture [206 x 13] intentionally omitted <==**

Then, the steepest direction of _L_ is the maximizer of 

**==> picture [233 x 10] intentionally omitted <==**

under the constraint (12.18). See Fig. 12.2. By using the variational method of maximizing (12.19) under the constraint (12.18), we easily obtain the following formulation: 

**==> picture [233 x 16] intentionally omitted <==**

This is a quadratic problem and the steepest direction is obtained as 

**==> picture [200 x 11] intentionally omitted <==**

We call 

**==> picture [216 x 12] intentionally omitted <==**

the Riemannian gradient or natural gradient of _L_ , where 

**==> picture [190 x 12] intentionally omitted <==**

is the natural gradient operator. 

From the point of view of geometry, the natural gradient is a contravariant vector 

**==> picture [200 x 13] intentionally omitted <==**

**Fig. 12.2** Natural gradient ˜∇ _L_ of _L_ 

**==> picture [139 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
L (ξ)<br>.<br>ξ<br>. dξ [2] 2<br>**----- End of picture text -----**<br>


12 Natural Gradient Learning and Its Dynamics in Singular Regions 

284 

and the ordinary gradient is a covariant vector 

**==> picture [193 x 11] intentionally omitted <==**

in the index notation. They are equal when and only when 

**==> picture [193 x 11] intentionally omitted <==**

that is, when an orthonormal coordinate system is used in a Euclidean space. 

The natural gradient learning method, which was suggested in Amari (1967), was formally introduced in Amari (1998) and defined by 

**==> picture [227 x 13] intentionally omitted <==**

In the batch mode, it is 

**==> picture [241 x 30] intentionally omitted <==**

In the case of statistical estimation where the Fisher information is a Riemannian metric, the loss function _L_ and the Riemannian metric **G** is defined by using the same log likelihood function log _p(_ _**x** ,_ _**ξ** )_ . In this case, the natural gradient method is regarded as a version of the Gauss–Newton method. However, there are many other cases where the loss function and the Riemannian metric are not related. The natural gradient learning method is useful in such cases, too. Independent component analysis (ICA) is such an example, where the parameter space is a set of mixing matrices and the Riemannian metric is given by the invariant metric of the underlying Lie group, but the loss is measured by the degree of independence of unmixed signals. In the next subsection, we show an interesting new idea of natural gradient using the “absolute value” of the Hessian as a Riemannian metric (Daupin et al. 2014). 

The natural gradient is also used in deep learning (Roux et al. 2007; Ollivier 2015) and in reinforcement learning as a policy natural gradient (e.g., Kakade 2002; Peters and Schaal 2008; Morimura et al. 2009). Another application is found in the optimization problem with stochastic relaxation technique (Malagò and Pistone 2014; Malagò et al. 2013; Yi et al. 2009; see also Hansen and Ostermeier 2001). 

## _**12.1.3 Riemannian Metric, Hessian and Absolute Hessian**_ 

The Newton method uses the Hessian of _L(_ _**ξ** )_ for obtaining the minimizer of _L(_ _**ξ** )_ by solving ∇ _L(_ _**ξ** )_ = 0 recursively. It updates the current _**ξ** t_ to give 

**==> picture [246 x 13] intentionally omitted <==**

285 

12.1 Natural Gradient Stochastic Descent Learning 

where 

**==> picture [203 x 10] intentionally omitted <==**

The natural gradient replaces **H** by the Riemannian metric **G** . Therefore, it is interesting to see the relation between **G** and **H** . 

We study the case where the noise is Gaussian with mean 0 and variance _σ_[2] . The joint probability distribution is written as 

**==> picture [267 x 25] intentionally omitted <==**

Hence, the loss function is the same as the negative of the log likelihood except for the constant. Minimizing _L(_ _**ξ** )_ is equivalent to maximizing the likelihood of the unknown parameter _**ξ**_ . The on-line learning algorithm (12.27) is regarded as a sequential estimation procedure, and the batch learning algorithm is an iteration procedure of obtaining the maximum likelihood estimator. 

The Fisher information in this case is given by 

**==> picture [256 x 11] intentionally omitted <==**

On the other hand, the Hessian of the loss function _L(_ _**ξ** )_ is 

**==> picture [260 x 13] intentionally omitted <==**

where the expectation is taken with respect to the true distribution _p_ � _**x** , y,_ _**ξ**_ 0� from which teacher signal _y_ is generated. 

By using (12.3) or by assuming _σ_[2] = 1 in (12.31), we easily have 

**==> picture [282 x 28] intentionally omitted <==**

where E _**x**_ is the expectation with respect to _q(_ _**x** )_ . **G** is in general positive-definite, but **H** is not necessarily so. (We discuss the singular case later where **G** and **H** degenerate.) However, **H** and **G** are exactly equal at _**ξ**_ = _**ξ**_ 0. Moreover, they are equal when _f (_ _**x** ,_ _**ξ** )_ = _f_ � _**x** ,_ _**ξ**_ 0� holds. We show later that they are equal at critical or singular regions in MLP. 

Recently, an interesting new idea of defining a Riemannian metric by the “absolute value” of the Hessian matrix was proposed (Dauphin et al. 2014). The Hessian is decomposed as 

**==> picture [194 x 12] intentionally omitted <==**

where **O** is an orthogonal matrix and _Λ_ = diag _(λ_ 1 _, . . . , λn)_ is a diagonal matrix having eigenvalues of **H** as the diagonal elements. The matrix of the absolute value of **H** is defined by 

286 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

**==> picture [234 x 11] intentionally omitted <==**

When | **H** | is used as a Riemannian metric, the natural gradient method becomes 

**==> picture [250 x 15] intentionally omitted <==**

The method is called the saddle-free Newton method (SFN) and its good performance is demonstrated. When _**ξ**_[′] is a saddle point, the Newton method stabilizes the saddle and converges to it. Hence, the Newton method does not work well. It is shown that most critical points of _L_ are saddles in high dimensions (Dauphin et al. 2014). Hence, the new idea is introduced as a method of avoiding saddle points, but keeping the good performance of the Newton method. Any natural gradient method is not trapped in a saddle whereas the Newton method is. Moreover, the behaviors of the Fisher information-based natural gradient and the absolute-value-based Hessian natural gradient are the same at around the optimal point _**ξ**_ 0, both enjoying the Fisher efficiency. It is also interesting to see that their behaviors are the same in the critical or singular regions studied later, which are the main source of plateau phenomena (retardation of learning). 

## _**12.1.4 Stochastic Relaxation of Optimization Problem**_ 

We show a problem in which the natural gradient plays an important role. Let us considertheproblemofsearchingfortheminimizerof _f (_ _**x** )_ over _**x**_ ∈ _X_ .Theproblem is difficult to solve when _f_ is not convex, in particular when _**x**_ is discrete. The integer programming is a typical example of the discrete type. 

Let us introduce a family of probability distribution _M_ = { _p(_ _**x** ,_ _**ξ** )_ } and consider the expectation 

**==> picture [212 x 10] intentionally omitted <==**

The problem of searching for the minimizer of _L(_ _**ξ** )_ with respect to _**ξ**_ is called the stochastic relaxation of the original problem (Malagò and Pistone 2014; see also Hansen and Ostermeier 2001). It changes the problem of a search in _X_ to a search in _M_ , so the gradient descent method is applicable even when _X_ is discrete. Since _M_ is a Riemannian manifold, we can apply the natural gradient method, 

**==> picture [234 x 15] intentionally omitted <==**

By choosing model _M_ carefully, it works well. Yi et al. (2009) proposed an efficient way of implementing the natural gradient. 

12.1 Natural Gradient Stochastic Descent Learning 

287 

## _**12.1.5 Natural Policy Gradient in Reinforcement Learning**_ 

We summarize the natural gradient method in reinforcement learning, following Peters and Schaal (2008). It is called the natural policy gradient method, formulated in the framework of the Markov decision process. See a survey paper by Grondman et al. (2012). Let us consider a system having state space _X_ = { _**x**_ } and action space _U_ = { _**u**_ }. At each discrete time _t_ , an action is chosen, depending on the current state _**x** t_ , subject to policy _π (_ _**u**_ | _**x** t )_ , which specifies the probability (density) of action _**u** t_ . We assume that it is a parameterized family of conditional probabilities specified by a vector parameter _**θ**_ , denoted as _π(_ _**u**_ | _**x**_ ; _**θ** )_ . The state transition takes place stochastically depending on the current _**x** t_ and _**u** t_ , and its probability (density) function is given by _p (_ _**x** t_ +1 | _**x** t ,_ _**u** t )_ . While a state transition takes place, an instantaneous reward is derived, which is a function of the current _**x** t_ and _**u** t_ , written as _r_ = _r (_ _**x** t ,_ _**u** t )_ . See Fig. 12.3. 

The expected reward at time _t_ is a sum of the current reward _rt_ and future rewards _rt_ +1 _, rt_ +2 _, . . ._ , but future rewards are discounted. Hence, the expected reward at state _**x**_ , including future rewards, is written as 

**==> picture [234 x 29] intentionally omitted <==**

where _γ <_ 1 is a discount factor. It depends on policy _π_ or its parameter _**θ**_ . This is 

**==> picture [231 x 19] intentionally omitted <==**

which is the expected reward when the state is at _**x**_ and action _**u**_ is chosen. The expectation is taken throughout all the possible trajectories of _(_ _**x** t ,_ _**u** t )_ pairs. 

**==> picture [156 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
rt rt +1 rt +2<br>x t x t +1 xt +2<br>p p<br>π π π<br>u t u t +1 u t +2<br>**----- End of picture text -----**<br>


**Fig. 12.3** Markov decision process, reward and action 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

288 

Let us fix an initial state _**x**_ = _**x**_ 0. The expected reward by taking the policy _π(_ _**u**_ | _**x**_ ; _**θ** )_ is 

**==> picture [215 x 19] intentionally omitted <==**

which is rewritten as 

**==> picture [259 x 25] intentionally omitted <==**

where 

**==> picture [232 x 22] intentionally omitted <==**

is the discounted probability of a sequence of states. 

We define the Fisher information matrix at the current state _**x**_ by 

**==> picture [294 x 23] intentionally omitted <==**

The entire Fisher information matrix is its expectation along all the trajectories, 

**==> picture [223 x 23] intentionally omitted <==**

See Kakade (2001), Peters and Schaal (2008). 

The natural gradient method, called the natural policy gradient or natural actorcritic, is given by 

**==> picture [235 x 12] intentionally omitted <==**

However, this is computationally heavy. A good idea is to approximate the stateaction value function by a linear combination of adequate basis functions { _ai (_ _**x** ,_ _**u** )_ } as 

**==> picture [252 x 15] intentionally omitted <==**

where _**w**_ is the parameters of weight to be adjusted. We choose 

**==> picture [222 x 10] intentionally omitted <==**

as basis functions. Since the gradient of the expected reward is written as 

**==> picture [271 x 23] intentionally omitted <==**

its gradient becomes 

**==> picture [192 x 10] intentionally omitted <==**

12.1 Natural Gradient Stochastic Descent Learning 

289 

Therefore, the natural gradient takes a very simple form as 

**==> picture [219 x 12] intentionally omitted <==**

In order to implement the natural policy gradient, we need to evaluate _**w**_ which gives the best approximation of _Q_ . We use the TD error 

**==> picture [231 x 10] intentionally omitted <==**

and solve the linear regression problem recursively as 

**==> picture [216 x 10] intentionally omitted <==**

where the basis function _**a** (_ _**x** )_ is 

**==> picture [225 x 24] intentionally omitted <==**

It is reported that the natural policy gradient demonstrates excellent performance in many cases. 

## _**12.1.6 Mirror Descent and Natural Gradient**_ 

The mirror descent method was introduced by Nemirovski and Yudin (1983) (see also Beck and Teboulle 2003) as a tool to search for the minimum of a convex function _f (_ _**θ** )_ . It is used in convex optimization problems with a constrained region. It uses another convex function _ψ(_ _**θ** )_ together with its Legendre dual _ϕ(_ _**η** )_ . They implicitly use a dually flat structure together with a Riemannian metric 

**==> picture [203 x 11] intentionally omitted <==**

The dual coordinates 

**==> picture [191 x 10] intentionally omitted <==**

are used to update the current _**η** t_ as 

**==> picture [215 x 11] intentionally omitted <==**

where _ε_ is a learning rate. Since both _**η**_ and ∇ _f_ are covariant quantities, it is invariant. The result is transformed back to the primal coordinates by 

**==> picture [206 x 13] intentionally omitted <==**

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

290 

Since 

**==> picture [201 x 13] intentionally omitted <==**

we have 

**==> picture [216 x 12] intentionally omitted <==**

This is the natural gradient method with the Riemannian metric **G** _(_ _**θ** )_ . See Raskutti and Mukherjee (2015). 

Since the underlying manifold is dually flat, _e_ - and _m_ -projections can be used to project a point on the restricted region. See sparse signal processing in the next chapter. 

## _**12.1.7 Properties of Natural Gradient Learning**_ 

## **12.1.7.1 Natural Gradient Learning is Fisher Efficient** 

On-line learning is a sequential procedure of modifying the current estimator _**ξ** t_ by using one example _(_ _**x** t , yt )_ at a time. Once an example has been used, it is discarded and not used again. This is useful for the estimator _**ξ**_[ˆ] _t_ to trace the change when the optimal _**ξ**_ 0 is slowly changing over time or suddenly changes at certain times. However, when the true target is fixed, this might cause loss of efficiency compared with the maximum likelihood estimator which is obtained by batch learning using all the data. This would be a cost to be paid for the benefit of traceability. To our surprise, this is not true. On-line learning can attain Fisher efficient estimation asymptotically, provided the learning constant is chosen adequately. The following theorem shows this (Amari 1998). 

**Theorem 12.1** _The estimator obtained by on-line natural gradient learning_ 

**==> picture [226 x 22] intentionally omitted <==**

_is Fisher efficient, attaining the Cramér–Rao bound asymptotically._ 

_Proof_ Let us denote the error covariance matrix of the estimator at time _t_ by 

**==> picture [245 x 18] intentionally omitted <==**

where _**ξ**_ 0 is the true value of _**ξ**_ . We expand the loss at _**ξ** t_ as 

**==> picture [308 x 13] intentionally omitted <==**

12.1 Natural Gradient Stochastic Descent Learning 

291 

Then, subtracting _**ξ**_ 0 from both sides of (12.63) and substituting it in (12.64), we have 

**==> picture [249 x 25] intentionally omitted <==**

where 

**==> picture [225 x 28] intentionally omitted <==**

are taken into account. We also note that 

**==> picture [224 x 25] intentionally omitted <==**

Then the solution of (12.66) is asymptotically 

**==> picture [193 x 22] intentionally omitted <==**

which proves the theorem. 

**==> picture [9 x 7] intentionally omitted <==**

## **12.1.7.2 Natural Gradient is Saturation Free** 

Consider a regression problem, where the output is written as 

**==> picture [201 x 10] intentionally omitted <==**

First we explain a simple perceptron, where _f_ is written as 

**==> picture [206 x 10] intentionally omitted <==**

Here, we neglect the bias term for simplicity. The parameter is a vector _**ξ**_ = _**w**_ and the activation function _ϕ_ is a sigmoid function, for example, 

**==> picture [198 x 10] intentionally omitted <==**

The gradient is written as 

**==> picture [240 x 11] intentionally omitted <==**

When the absolute value of _**w**_ is large, function _ϕ(_ _**w**_ · _**x** )_ saturates for most _**x**_ , becoming nearly equal 1 or −1. This is the saturation problem, where the gradient becomes 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

292 

almost equal to 0 because _ϕ_[′] ≈ 0, and ordinary stochastic gradient descent learning becomes slow. 

This is not serious in the case of a simple perceptron, but is serious in the case of multilayer perceptrons used in deep learning, where _f (_ _**x** ,_ _**ξ** )_ is composed of a concatenation of many _f_ ’s. We may write the output as 

**==> picture [252 x 10] intentionally omitted <==**

in the case of MLP, where **W** _j_ is the connection weight matrix of the _j_ th layer to the _( j_ + 1 _)_ th layer, _**ξ**_ = _(_ **W** 1 _, . . . ,_ **W** _k)_ . Its derivative with respect to **W** 1, for example, includes the product of many _ϕ_[′] ’s. Hence, it is almost vanishing in many cases. This is considered as a flaw of back-propagation in deep learning. 

The natural gradient learning method is free of such a saturation problem. The gradient is written as 

**==> picture [237 x 10] intentionally omitted <==**

The Fisher information is given by 

**==> picture [235 x 13] intentionally omitted <==**

The magnitude of the ordinary gradient would be very small in many cases but the natural gradient is different. We evaluate the magnitude of the natural gradient vector 

**==> picture [229 x 12] intentionally omitted <==**

by its Riemannian magnitude, 

**==> picture [223 x 19] intentionally omitted <==**

**Theorem 12.2** _The magnitude of the natural gradient is given by_ 

_where_ 

**==> picture [247 x 55] intentionally omitted <==**

_It does not vanish even when ϕ_[′] _is small. Moreover,_ 

**==> picture [197 x 19] intentionally omitted <==**

_in a neighborhood of the optimal_ _**ξ**_ 0 _, where k is the dimension of_ _**ξ** ._ 

12.1 Natural Gradient Stochastic Descent Learning 

293 

_Proof_ From (12.78), we have 

**==> picture [318 x 19] intentionally omitted <==**

which proves (12.80). When _**ξ**_ = _**ξ**_ 0, we easily have (12.82). □ 

## **12.1.7.3 Adaptive Natural Gradient Learning** 

The natural gradient method uses **G**[−][1][ �] _**ξ** t_ �, so that we need to calculate the inverse of **G** � _**ξ** t_ � at each step. When the number of parameters is large, this is computationally intractable. Moreover, calculation of **G** _(_ _**ξ** t )_ is not easy in the case when the distribution _q(_ _**x** )_ of _**x**_ is unknown. To avoid this situation, an adaptive method of obtaining **G**[−][1][ �] _**ξ** t_ � recursively has been proposed (Amari et al. 2000). By using the Taylor expansion of 

**==> picture [228 x 13] intentionally omitted <==**

and inverting it, we have an adaptive method of calculating **G** _t_[−][1] = **G**[−][1][ �] _**ξ** t_ � recursively by 

**==> picture [322 x 14] intentionally omitted <==**

where _εt_ is another learning constant. 

Park et al. (2000) demonstrated performance of adaptive natural gradient learning using a number of simple examples, and confirmed that its performance is excellent. See also Zhao et al. (2015). The adaptive method can be used to calculate the inverse of the Hessian, 

**==> picture [271 x 13] intentionally omitted <==**

## **12.1.7.4 Approximation and Practical Implementation of Natural Gradient** 

It is not easy to implement the natural gradient in a large network because of a large computational cost. There are many trials to overcome the difficulty and to give a good approximate solution. See Martens (2015) for the perspectives of the natural gradient method. 

Martens and Grosse (2015) proposed an efficient method of approximating natural gradient descent in deep neural networks, called the Kronecker-factored approximate curvature (K-FAC). It uses two stages for the approximation of the Fisher information. One is to use the Kronecker product of the matrices due to error terms and activation terms, and the expectation is taken separately for calculating the Fisher information. The other is to use the tridiagonal approximation for the inverse of 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

294 

the Fisher information matrix (the Riemannian metric). A deep network consists of a concatenation of many layers, and the Fisher information matrix has a block structure. The tridiagonal approximation neglects off-diagonal blocks except for the blocks corresponding to consecutive _(i_ − 1 _, i, i_ + 1 _)_ layers. It is demonstrated that this is not only computationally tractable but its performance is excellent. 

We remark that the two approximations do not destroy most of the singular structure of the original Fisher information, studied in the next section. Since the singular regions are the main cause of retardation in learning, the K-FAC works well, getting rid of the plateau phenomena. 

## **12.1.7.5 Adaptive Learning Constant** 

The dynamical behavior of learning depends on the learning constant _ηt_ . When the current _**ξ** t_ is far from the optimal value _**ξ**_ 0, it is desirable to use large _ηt_ , because we need to shift _**ξ** t_ toward _**ξ**_ 0 with a large step-size. On the other hand, when _**ξ** t_ is near the optimal value, if _ηt_ is large, the stochastic fluctuation of ∇ _l_ dominates so that it is better to choose a small _ηt_ . When the optimal value of the target is fixed, a good choice of learning constant is given by stochastic approximation, 

**==> picture [222 x 28] intentionally omitted <==**

When _ηt_ satisfies(12.87),theestimator _**ξ** t_ convergestotheoptimal _**ξ**_ 0 withprobability one. A typical case is given by 

**==> picture [183 x 19] intentionally omitted <==**

When the target does not move, the trade-off between the speed of convergence and the accuracy of estimation is given in Amari (1967) for a fixed _η_ . For the cases when the target moves, the idea of modifying _ηt_ adaptively depending on the current situation of the estimator was considered from the early time. An excellent idea of modifying the learning constant was proposed by Barkai et al. (1995) in the case when _y_ is binary. Amari (1998) generalized it and analyzed its behavior. A new adaptive learning method is given by 

**==> picture [249 x 29] intentionally omitted <==**

where _α, β_ are constants. Here, the natural gradient method is fortified by a learning rule of learning constant (12.90). The learning rate _ηt_ increases, roughly speaking, when the instantaneous loss _l_ � _**x** t , yt_ ; _**ξ** t_ � is large, which implies that the target lies far away and _ηt_ decreases when the target is closer. 

295 

12.1 Natural Gradient Stochastic Descent Learning 

In order to analyze its behavior mathematically, we use the continuous-time version of the learning equation, 

**==> picture [240 x 47] intentionally omitted <==**

where the equations are averaged over possible input–output pairs _(_ _**x** t , yt )_ , ⟨⟩ representing the average with respect to _p(_ _**x** , y)_ . 

By using the Taylor expansion 

**==> picture [303 x 29] intentionally omitted <==**

where we put **G** 0 = **G** � _**ξ**_ 0�, we have 

**==> picture [263 x 50] intentionally omitted <==**

We introduce the squared error at time _t_ by 

**==> picture [231 x 22] intentionally omitted <==**

Then, the equations reduce to 

**==> picture [212 x 22] intentionally omitted <==**

**==> picture [213 x 22] intentionally omitted <==**

when _**ξ**_ 0 is fixed. The behaviors of the error _et_ and learning constant _ηt_ described by (12.97) and (12.98) are interesting. The origin _(_ 0 _,_ 0 _)_ is its stable equilibrium, so both _et_ and _ηt_ converge to 0. The solution is written approximately as 

**==> picture [210 x 24] intentionally omitted <==**

**==> picture [211 x 22] intentionally omitted <==**

296 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

for large _t_ . This shows that the error converges to 0in the order of 1 _/t_ as _t_ goes to infinity when _**ξ**_ 0 is fixed. When the target changes over time, _**ξ** t_ traces its change nicely by modifying _ηt_ . 

## **12.2 Singularity in Learning: Multilayer Perceptron** 

The multilayer perceptron (MLP), proposed by Rosenblatt (1961), is a universal machine that can approximate any input–output function, provided it includes a sufficiently large number of hidden neurons. Although it seemed to be gradually being replaced by new powerful learning machines such as the support vector machine (SVM), MLPhas beenrevivedinthe21st centuryin“deeplearning”, whereanetwork has a considerably large number of layers. Lots of new tricks are proposed to facilitate deep learning, including unsupervised learning (self-organization) as preprocessing, the convolutional structure, and the drop-out technique in supervised learning. Deep learning has recorded benchmark performances, winning most competitions on pattern recognition. See Schmidhuber (2015) for example. Researchers are astonished by the reincarnation of the multilayer perceptron. The back-propagation learning method is used at the final stage. 

There is, however, a serious problem in the parameter space of a multilayer perceptron. It includes singularities, in the sense that the same output function is realized by continuously many parameters in a specific region. One cannot determine the parameter uniquely in such a region, and so the parameter is not identifiable. The Fisher information matrix degenerates in this region. This causes the dynamics of learning to become extremely slow, which is known as a critical slowdown or the plateau phenomena. 

The present section studies typical singular structure in the manifold of multilayer perceptrons and clarifies its implications for statistical inference. The dynamical behavior of learning near singularities is studied in detail. Finally, it is shown that the natural gradient learning method, including SFN, overcomes these difficulties. 

## _**12.2.1 Multilayer Perceptron**_ 

The multilayer perceptron is a layered machine composed of artificial neurons, which receives input _**x**_ and emits output _y_ . The behavior of an analog artificial neuron is described as follows: It receives a vector input signal _**x**_ , calculates a weighted sum of inputs and subtracts a threshold as 

**==> picture [230 x 15] intentionally omitted <==**

12.2 Singularity in Learning: Multilayer Perceptron 

297 

where _**w**_ = _(w_ 1 _, . . . , wn)_ . It emits an output 

**==> picture [187 x 10] intentionally omitted <==**

where _ϕ_ is a sigmoidal function. We use 

**==> picture [231 x 27] intentionally omitted <==**

because this is convenient for obtaining explicit analytical solutions. The coefficients _wi_ are called the synaptic weights. In order to make descriptions simpler, we put _h_ = 0 in the following. 

A multilayer perceptron consists of many layers in deep learning, but we consider here only three layers, an input layer, a hidden layer and an output layer (Fig. 12.4). The _i_ th neuron of the hidden layer calculates the weighted sum of input _**x**_ as 

**==> picture [190 x 9] intentionally omitted <==**

and emits output _ϕ (ui )_ , where _**w** i_ is the weight vector of the _i_ th hidden neuron. We consider a simple case that the output layer consists of only one output neuron. It calculates a weighted sum of the outputs of the hidden neurons and the final output is written as 

**==> picture [210 x 15] intentionally omitted <==**

where _vi_ are the weights of the output neuron. We may apply a sigmoidal nonlinear function to _y_ , but it is only a nonlinear scale change. So we use a linear output neuron, but a nonlinear function is used when the output neurons are connected to the next layer as its input. 

A multilayer perceptron is specified by synaptic weights 

**==> picture [230 x 10] intentionally omitted <==**

Let _M_ be the parameter space of perceptrons. Then, it is an _N_ -dimensional manifold, where _**ξ**_ is a coordinate system including _N_ = _(n_ + 1 _)m_ components. We write the input–output relation of the perceptron specified by _**ξ**_ as 

**Fig. 12.4** Multilayer perception 

**==> picture [253 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
w 1 ( w 1 x )<br>.<br>input x . output  y<br>.<br>w m ( w m x )<br>...<br>...<br>**----- End of picture text -----**<br>


12 Natural Gradient Learning and Its Dynamics in Singular Regions 

298 

**==> picture [232 x 28] intentionally omitted <==**

Learning takes place in the manifold _M_ , where the current value _**ξ**_ is modified by a stochastic gradient descent method using the current input–output example _(_ _**x** t , yt )_ . 

## _**12.2.2 Singularities in M**_ 

The manifold _M_ includes a set of points which have the same output functions 

**==> picture [207 x 13] intentionally omitted <==**

for _**ξ**_ ̸= _**ξ**_[′] . Two such points _**ξ**_ and _**ξ**_[′] are said to be equivalent and are denoted by 

**==> picture [182 x 11] intentionally omitted <==**

since their output functions are the same. When _**ξ**_ has an equivalent point in _M_ other than itself, we cannot identify _**ξ**_ uniquely from the output function. There are two types of unidentifiability, originating from the invariance under the following transformations of parameters: 

1. Sign change: _**ξ**_ ≈− _**ξ**_ : This is because _ϕ_ is an odd function, _ϕ(_ − _u)_ = − _ϕ(u)_ , so that _f (_ _**x** ,_ _**ξ** )_ = _f (_ _**x** ,_ − _**ξ** )_ . The unidentifiability due to the sign change is simple, and we may eliminate the unidentifiability by restricting the region within _vi_ ≥ 0 _, i_ = 1 _, . . . , m_ . However, the boundary _vi_ = 0 causes singularities, as will be shown soon. 

2. Permutation: Let[�] be a permutation of indices and _i_ be transformed to _i_[′] as _i_[′] =[�] _i_ . Then, 

**==> picture [306 x 23] intentionally omitted <==**

We divide _M_ by the equivalence relation ≈ and put 

**==> picture [193 x 12] intentionally omitted <==**

Equivalent points in _M_ are reduced to one point in _M_ ˜ , the space of the output functions of multilayer perceptrons. _M_[˜] is not a manifold in the exact mathematical sense, as will be shown in the following, because it includes singular points due to unidentifiability. It is a manifold if we simply remove the singular points. _M_[˜] is called a behavior manifold or neuromanifold, although it is not a manifold in the exact sense. 

12.2 Singularity in Learning: Multilayer Perceptron 

299 

We explain the singularity by using simple examples. Consider a very simple perceptron consisting of one hidden neuron, which is included in a larger model as a subnetwork. Its output function is 

**==> picture [207 x 10] intentionally omitted <==**

and the parameter space _M_ is _**ξ**_ = _(_ _**w** , v)_ . When _v_ = 0, whatever _**w**_ is, the output function is 0. On the other hand, when _**w**_ = 0, whatever _v_ is, the output function is also 0, because _ϕ(_ 0 _)_ = 0. We call the set of these points a critical or singular region _R_ of _M_ , that is, 

**==> picture [220 x 10] intentionally omitted <==**

All the points in _R_ are equivalent. By dividing _M_ by the equivalence relation, _M_[˜] consists of two parts (not four because _(_ _**w** , v)_ and _(_ − _**w** ,_ − _v)_ are equivalent), which are connected by a single point corresponding to _v_ = 0 or _**w**_ = 0. It is a singular point in _M_[˜] . See Fig. 12.5. More generally, we consider the following eliminating singularity. 

- (1) Eliminating singularity: When _vi_ = 0, whatever the value of _**w** i_ is, any _**w** i_ gives the same output function. Hence, _**w** i_ is not identifiable in this case. When _**w** i_ = 0, whatever _vi_ is, the output of the neuron is 0. Such a neuron has no effect on the output and it can be eliminated. 

Consider a subnetwork consisting of two hidden neurons _i_ and _j_ . Their output function is 

**==> picture [244 x 13] intentionally omitted <==**

- (2) Overlapping singularity: When two neurons _i_ and _j_ in the hidden layer have identical weight vectors, 

**==> picture [189 x 11] intentionally omitted <==**

their contribution to the output is 

**==> picture [333 x 148] intentionally omitted <==**

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

300 

Therefore, the output is the same whatever values _vi_ and _v j_ take, as long as _vi_ + _v j_ is equal to a fixed value _v_ . That is, the output is the same on the line satisfying 

**==> picture [183 x 11] intentionally omitted <==**

for any constant _v_ . Hence, _vi_ and _v j_ themselves are not identifiable. This occurs when two neurons have the same weight vector _**w** i_ = _**w** j_ = _**w**_ , with their weight vectors overlapping completely. A similar situation holds when _**w** i_ = − _**w** j_ , but we omit this case for simplicity’s sake. 

The critical region due to the overlapping singularity is given by 

**==> picture [263 x 11] intentionally omitted <==**

See Fig. 12.6, where _Roi j (_ _**w** , v)_ is mapped to a single point in _M_[˜] . The images of the _Roi j (_ _**w** , v)_ form a continuous submanifold as _**w**_ and _v_ vary. The critical region in _M_ is written as 

**==> picture [253 x 37] intentionally omitted <==**

which is a union of critical submanifolds (12.118). 

We consider an equivalence class _Ri j (_ _**w** , v)_ specified by two parameters _**w**_ and _v_ , such that any networks in this class have the same output function 

**==> picture [215 x 10] intentionally omitted <==**

It consists of three parts, _Ro_ , _Rei_ and _Rej_ , 

_Ri j (_ _**w** , v)_ = _Ro_ ∪ _Rei_ ∪ _Rej ,_ (12.121) 

**==> picture [284 x 106] intentionally omitted <==**

**----- Start of picture text -----**<br>
vi+vj =v<br>w i = w j<br>. [v]<br>v w j<br>w i Ne vi+vj =v<br>**----- End of picture text -----**<br>


**Fig. 12.6** Overlapping singularity 

12.2 Singularity in Learning: Multilayer Perceptron 

301 

where 

**==> picture [288 x 42] intentionally omitted <==**

_Ro_ isaone-dimensionalsubspacecorrespondingtotheoverlappingsingularity,where _z_ = _vi_ − _v j_ is a free parameter in it, keeping the sum _vi_ + _v j_ = _v_ constant. _Rei_ and _Rej_ correspond to the eliminating singularity. They are _n_ -dimensional, since _**w** i_ and _**w** j_ , respectively, can take any values. _Ri j (_ _**w** , v)_ is an elementary critical region which is a union of three parts, as is shown in Fig. 12.7. All the points in it are mapped to a single point _f_ = _vϕ(_ _**w**_ · _**x** )_ in the behavior manifold _M_[˜] . This is a singular point in _M_[˜] . 

There are infinitely many such critical regions, because we have an elementary critical region for eacha continuum of singular _**w**_ andpoints _v_ and they are distributed continuously. So they formin the behavior manifold _M_ ˜ where _**w**_ and _v_ are parameters. The region is further contracted when 

**==> picture [186 x 9] intentionally omitted <==**

holds. Such critical regions exist for each pair _(i, j)_ in a larger network and they intersect. So _M_ includes a rich net of critical regions spreading over _M_ . 

The trajectory of learning is given by (12.12) in _M_ . It is mapped to _M_[˜] and it may pass through a critical region in _M_ or a singular point in _M_[˜] . We study the dynamical behavior of learning near singularities. 

The loss function takes the same value in a critical region _Ri j (_ _**w** , v)_ , so that its derivative in the tangent directions of _Ri j (_ _**w** , v)_ is always 0. This also implies that the Fisher information degenerates in the critical region _Ri j_ of _M_ , because there are directions _**a**_ in _Ri j_ such that 

**==> picture [214 x 10] intentionally omitted <==**

**Fig. 12.7** Critical region _Ri j (_ _**w** , v)_ 

**==> picture [174 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
Rei Rej<br>w i w j<br>z<br>vi=0 Ro vj=0<br>**----- End of picture text -----**<br>


12 Natural Gradient Learning and Its Dynamics in Singular Regions 

302 

holds for any _c_ , as is derived from (12.118). _**a**_ is one-dimensional in region _Ro_ and _n_ -dimensional in regions _Rei_ and _Rej_ (Fig. 12.7). Hence, the score function, that is the derivative of log-likelihood, becomes 0in these directions. This implies that the Fisher information matrix has null directions in which 

**==> picture [196 x 12] intentionally omitted <==**

So it degenerates and **G**[−][1] diverges on the critical region. The Fisher information exists and is non-degenerate in _M_[˜] except for singular points. No tangent space exists at a singular point of _M_[˜] . This is the same for the absolute Hessian metric and 

**==> picture [198 x 12] intentionally omitted <==**

holds in _R_ in the direction satisfying _**ξ**_ ≈ _**ξ**_ + _**a**_ . 

A probability distribution _p(_ _**x** , y,_ _**ξ** )_ accompanies each point of _M_ and _M_[˜] , but these probability distributions do not form a regular statistical model, because the non-degenerate Fisher information does not exist in critical regions or at singular points. We will discuss how the singularity affects statistical inference in a later subsection. 

## _**12.2.3 Dynamics of Learning in M**_ 

Multilayer perceptrons suffer from two types of flaw in their learning behavior. One is local minima such that the global minimum might not be attained by the gradient method. The second is the slowness of convergence, because the trajectory of learning is often trapped on a plateau, staying there for a long time before escaping from it (Amari et al. 2006). This is mostly due to the symmetric structure, such that its behavior is invariant under sign changes and permutations of hidden neurons. 

Geometrically speaking, the plateau phenomena are given rise to by the singular structure. A critical region forms a plateau. We will analyze the dynamics of vanilla stochastic gradient learning in the neighborhood of a critical region. We will also show that the natural gradient is free of the plateau phenomena. 

In order to analyze the dynamics, we use a very simple model consisting of two hidden neurons described in (12.114). Such simple models are embedded in a general perceptron as parts and cause a serious slowdown in learning. Instead of the difference Eq. (12.12) of stochastic descent learning, we use the averaged version in the continuous time, 

**==> picture [223 x 24] intentionally omitted <==**

where ⟨⟩ is the average with respect to the joint probability distribution _p(_ _**x** , y,_ _**ξ**_ 0 _)_ of the true or teacher system from which training examples are generated. We further assume that the probability distribution of input _**x**_ is subject to the Gaussian 

12.2 Singularity in Learning: Multilayer Perceptron 

303 

distribution _N (_ 0 _,_ **I** _)_ with mean 0 and covariance matrix **I** , the identity matrix. These assumptions are useful for obtaining explicit solutions. 

In order to analyze the behavior of dynamics (12.129) consisting of two hidden neurons, we use a new coordinate system _**ζ**_ (Wei et al. 2008), 

**==> picture [199 x 10] intentionally omitted <==**

where 

**==> picture [240 x 22] intentionally omitted <==**

**==> picture [238 x 21] intentionally omitted <==**

and we use suffixes 1, 2 instead of _i, j_ . The critical region _R_ = _R_ 12 _(_ _**w** , v)_ is given in this new coordinate system by 

**==> picture [220 x 10] intentionally omitted <==**

in which _**s**_ = _**w**_ and _r_ = _v_ hold. We divide it into two parts _R_ = _Ro_ ∪ _Re_ , 

**==> picture [206 x 25] intentionally omitted <==**

where _Ro_ is the overlapping singularity and _Re_ = _Re_ 1 ∪ _Re_ 2 is the eliminating singularity. 

The dynamics (12.129) are described in the new coordinate system as 

**==> picture [221 x 24] intentionally omitted <==**

where **T** is the Jacobian matrix of the coordinate transformation from _**ξ**_ to _**ζ**_ , 

**==> picture [185 x 25] intentionally omitted <==**

The output function _f_ is written as 

**==> picture [281 x 53] intentionally omitted <==**

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

304 

in terms of the new coordinates. We expand it in the Taylor series in the neighborhood of _Ro_ , 

**==> picture [245 x 48] intentionally omitted <==**

where higher-order terms of _**u**_ are neglected. We then have the learning dynamics in terms of _**ζ**_ = _(_ _**u** , z)_ in the neighborhood of _Ro_ . The dynamics concerning variables _**s**_ and _r_ are subject to the usual differential equations (fast dynamics) and their values converge rapidly to their equilibrium values, even when the behaviors of _**u**_ and _z_ are suffering from a critical slowdown (slow dynamics). Hence, we analyze the equations concerning _**u**_ and _z_ , where _**s**_ and _r_ are assumed to have converged to their equilibrium values _**w**_ and _v_ . The resultant dynamics are 

**==> picture [215 x 41] intentionally omitted <==**

where 

**==> picture [218 x 19] intentionally omitted <==**

It is clear that 

**==> picture [182 x 22] intentionally omitted <==**

in the region _R_ = _Ro_ ∪ _Re_ , so any points in _R_ are equilibria. The stability of the equilibria depends on **K** . We show the results without proofs (which are technical and complicated but not difficult, see Wei et al. 2008; Wei and Amari 2008). 

**Theorem 12.3** _When the teacher output function is in the critical region, the equilibria are stable._ 

## This case occurs when the system is over-realizable, having redundant parameters. 

**Theorem 12.4** _When the teacher output function is outside the critical region, we have three cases, depending on the eigenvalues of_ **K** _:_ 

- _(1) The equilibrium solutions on Ro satisfying_ | _z_ | _>_ 1 _are stable and those satisfying_ | _z_ | _<_ 1 _are unstable when_ **K** _is positive-definite._ 

- _(2) The equilibrium solutions on Ro satisfying_ | _z_ | _<_ 1 _are stable and those satisfying_ | _z_ | _>_ 1 _are unstable when_ **K** _is negative-definite._ 

- _(3) The solutions on Ro are unstable when some eigenvalues are positive and some negative._ 

305 

12.2 Singularity in Learning: Multilayer Perceptron 

We further analyze the trajectories of the solutions in the neighborhood of _Ro_ . Let us introduce a function 

**==> picture [196 x 22] intentionally omitted <==**

which shows how far the current _**ζ**_ is from _Ro_ . Its time derivative is given, from (12.141) and (12.142), as 

**==> picture [228 x 29] intentionally omitted <==**

The equation is integrable, and the solution is 

**==> picture [229 x 28] intentionally omitted <==**

where _c_ is an arbitrary constant that specifies a trajectory. 

**Theorem 12.5** _The trajectories of learning are_ 

**==> picture [228 x 28] intentionally omitted <==**

_in the neighborhood of Ro._ 

The family of trajectories shows how the dynamics proceed in the neighborhood of _Ro_ . The behaviors are the same for any _**ξ**_ ∈ _Ro_ , but their stabilities depend on _**ξ**_ and **K** . See Fig. 12.8. When _**ξ**_ 0 is in _R_ , _R_ is stable. When **K** is positive-definite or negative-definite, the trajectory starting from the basin of attraction reaches a stable point in _Ro_ and is trapped in it, fluctuating in it randomly before escaping from it. 

## _**12.2.4 Critical Slowdown of Dynamics**_ 

We consider the two cases separately. 

**Case 1** : **The teacher function is in** _**R**_ . When the number of hidden neurons is larger in the model network (student network) to be trained than in the teacher network (true network), some neurons are redundant because the optimal solution is realized by using a smaller number of neurons. This is the over-realizable case. In this case, elimination of neurons or overlap of synaptic weight vectors occurs, implying that the optimal solution is in _R_ . 

306 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

**Fig. 12.8** Landscape of error function and learning trajectory 

**==> picture [197 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
.<br>z<br>1<br>0<br>1<br>or<br>rr<br>E<br>**----- End of picture text -----**<br>


When the teacher network is _**ξ** o_ ∈ _R_ , (12.143) is written as 

**==> picture [201 x 24] intentionally omitted <==**

where 

**==> picture [220 x 13] intentionally omitted <==**

is the error term and is 0 when _**ζ**_ ∈ _R_ , in particular, when _**u**_ = 0. By expanding the error term, we can easily obtain 

**==> picture [197 x 12] intentionally omitted <==**

This implies that the dynamics of _**u**_ are 

**==> picture [199 x 22] intentionally omitted <==**

Hence, the speed of convergence of _**u**_ to 0 is extremely slow, taking a long time for training (Fig. 12.9a). This is frequently observed in simulations. 

**Case 2** : **The optimal solution lies outside** _**R**_ . Points in _R_ are equilibrium solutions. **K** is not small in this case, because the error term is not small at _R_ . When **K** is positive-definite or negative-definite, the part of _Ro,_ | _z_ | _>_ 1 or | _z_ | _<_ 1, respectively, is stable but the other part is unstable. The landscape of the loss function is shown in this case in Fig. 12.8, where _Ro_ is shown by the solid line. Starting _**ζ**_ at some initial point belonging to the basin of attraction, the state is attracted to the stable part of _Ro_ . See Fig. 12.9b, c. The value of the loss function is the same and its derivative is 0 on _Ro_ since all points in _Ro_ are equivalent. However, this is not the optimal point. The 

12.2 Singularity in Learning: Multilayer Perceptron 

307 

**Fig. 12.9** Trajectories of learning near singularity: **a** Teacher is at singularity; **b** | _z_ | _<_ 1 is stable; **c** | _z_ | _>_ 1 is stable 

**==> picture [213 x 308] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) h ( u )<br>0.4<br>0.3<br>0.2<br>0.1<br>0 z<br>ee 3 2 1 1 2 3<br>0<br>(b) h ( u )<br>0.4<br>0.3<br>0.2<br>0.1<br>0 z<br>a) 3 2 1  Ae 1 2 3<br>0<br>(c) h ( u )<br>0.4<br>0.3<br>0.2<br>0.1<br>0 z<br>O 3 i 2 1 a 1 2 3<br>0<br>**----- End of picture text -----**<br>


state fluctuates in the neighborhood of _Ro_ by stochastic dynamics due to randomly selected input _**x**_ . Thus, a random walk of the state takes place in the neighborhood of _Ro_ and the state eventually reaches the boundary | _z_ | = 1 of the stable region. It thus enters the unstable region and then escapes from _Ro_ immediately, moving toward the true optimal point. However, it takes a long time before leaving the stable critical region. See Fig. 12.10. Precisely speaking, the fluctuation around _Ro_ is not a random walk, because there are systematic flows out of the stable region in the neighborhood of _Ro_ , but the flow is very small when _**u**_ is small. 

Although the trajectories passing through _R_ have incoming flows and outgoing flows at _R_ , this is completely different from those at a saddle point. The basin of attraction has measure 0in the case of a saddle. Therefore, it is at measure 0 that the state reaches the saddle. Moreover, the state escapes from the saddle quickly by a small perturbation. On the other hand, the basin of attraction of _R_ has a finite measure and the trajectory exactly reaches _R_ in this case. A small perturbation moves the state but it again reaches _R_ . This does not prevent a trajectory reaching _R_ . A saddle does not cause any serious effect on the slowdown of dynamics. It is a critical region that causes a critical slowdown. 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

308 

**Fig. 12.10** Trajectory of learning near the singularity 

**Fig. 12.11** Trajectories in _M_[˜] 

Learning trajectory near the singularity 

**==> picture [172 x 201] intentionally omitted <==**

**----- Start of picture text -----**<br>
L(ξ)<br>_ WI REE i<br>= WS SSS oe<br>R0<br>/ Basin of attraction<br>/<br>WAl b, Z<br>Z<br>.<br>**----- End of picture text -----**<br>


We can consider the same dynamics in _M_[˜] where _R_ is reduced to one point by the equivalence.Thepointcorrespondingto _M_ ˜ ,ofwhichthebasinofattractionhasafinitemeasure(Milnor1985).Thetrajectories _R_ isasingularpoint.ItisaMilnorattractorin enter it and then emerge from it (Fig. 12.11). A general multilayer perceptron includes a net of such critical regions within it. The trajectory of vanilla stochastic gradient learning is trapped in such critical regions many times before it reaches the optimum solution. This is known as the plateau phenomena. See Fig. 12.12 for an example of learning curves. 

**Fig. 12.12** Plateaus 

**==> picture [136 x 88] intentionally omitted <==**

**----- Start of picture text -----**<br>
L ( t )<br>t<br>**----- End of picture text -----**<br>


12.2 Singularity in Learning: Multilayer Perceptron 

309 

## _**12.2.5 Natural Gradient Learning Is Free of Plateaus**_ 

The plateau phenomena are given rise to by the singularities. Let us consider a simple case of (12.114), where the horizontal line ( _z_ -axis) in Fig. 12.7 is the critical region and all the points in this line are equivalent. The Riemannian length is 0 along this line and the Riemannian metric degenerates in this direction. The inverse of the Fisher metric diverges in this direction to infinity at _R_ . The gradient of the cost function is also 0in this direction because all the points in _R_ are equivalent. Therefore, the natural gradient, ∇[˜] _l_ = _G_[−][1] ∇ _l_ , is 0 multiplied by infinity at the singular points. Because of this, the natural gradient takes an ordinary value even in a very small neighborhood of _R_ . 

Cousseau et al. (2008) analyzed the dynamics of natural gradient learning near singularity when the teacher _**ζ**_ 0 is in _R_ . After complicated calculations, 

**==> picture [208 x 20] intentionally omitted <==**

**==> picture [207 x 19] intentionally omitted <==**

is derived in the one-dimensional case. This shows that the dynamics converges to _R_ in the linear order. Hence, no retardation takes place. 

When _**ζ**_ 0 is outside _R_ , the trajectory is trapped in plateaus in the case of ordinary stochastic gradient learning. However, in the case of natural gradient learning, no retardation takes place, because the Riemannian metric is 0 along the _Ro_ -direction so that all the points are reduced to a single point. That is, the trajectory enters a point in _R_ and goes out immediately not staying within it. This is well understood by considering the trajectory in _M_[˜] . 

In _M_[˜] , _R_ reduces to the single singular point, and all the other points in _M_[˜] are regular, having a non-degenerate Riemannian metric. Even in a very small neighborhood of _R_ , **G**[−][1] ∇ _l_ takes ordinary values. Hence, a critical slowdown does not occur. To show this, Cousseau et al. (2008) used the blow-down technique of algebraic geometry. They introduced a new coordinate system _**μ**_ = _(δ, γ)_ , 

**==> picture [204 x 30] intentionally omitted <==**

when _**u**_ is one-dimensional. All the points in singular region _R_ is mapped to a single point _**μ**_ = _(_ 0 _,_ 0 _)_ . The Fisher information **G** takes ordinary values even in a small neighborhood of _R_ except for _(_ 0 _,_ 0 _)_ at which it is not defined. They showed that 

**==> picture [190 x 10] intentionally omitted <==**

Natural Gradient Learning and Its Dynamics in Singular Regions 

310 

12 

**Fig. 12.13** Learning _curves_ 

**==> picture [212 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
3.5<br>Standard Gradient<br>3 Adaptive Natural<br>Gradient<br>2.5<br>3<br>1.5<br>1<br>0.5<br>0<br>0 50 100 150 200<br>LearningStep<br>Expected Loss<br>**----- End of picture text -----**<br>


holds in this coordinate system when the teacher is in _R_ . Hence, the natural gradient learning dynamics becomes very simple, 

**==> picture [189 x 10] intentionally omitted <==**

in a neighborhood of _R_ , when the teacher is inside _R_ . When the teacher is outside _R_ , the trajectory enters _R_ , that is, _**μ**_ = 0 without retardation, and then escapes from it immediately. It is interesting to see that, starting from various initial points, the trajectories once enter _R_ and then go out. The basin of attraction of _R_ has a finite major, although the trajectories leave it immediately (see Fig. 12.11). This is a typical Milnor attractor. The new coordinate system _**μ**_ , using the blow-down technique, is useful. It should be remarked that absolute Hessian dynamics have the same characteristics. 

See Fig. 12.13 for examples of the learning curves of the adaptive natural gradient learning method compared to the ordinary back-propagation method. 

## _**12.2.6 Singular Statistical Models**_ 

A statistical model _M_ = { _p(_ _**x** ,_ _**ξ** )_ } is regular when it satisfies the two conditions: 

- (1) The parameter _**ξ**_ belongs to an open set in a Euclidean space. 

- (2) The Fisher information matrix exists and is non-singular. 

In this case, _n_ score functions 

**==> picture [249 x 25] intentionally omitted <==**

12.2 Singularity in Learning: Multilayer Perceptron 

311 

are linearly independent and the tangent space _T_ _**ξ**_ is spanned by them. The standard asymptotic theory of statistics holds, as is highlighted by the Cramér–Rao theorem. However, the theory is violated in a singular statistical model. 

There are many singular statistical models. One type is the case in which the Fisher information matrix degenerates at singularities. A mixture model 

**==> picture [291 x 15] intentionally omitted <==**

where _p(_ _**x** ,_ _**w** )_ is a regular statistical model specified by _**w**_ , belongs to this class. The MLP belongs to this class. When _p(_ _**x** ,_ _**w** )_ is a Gaussian distribution with varying mean and variance, it is called a Gaussian mixture model. The changing time model (sometimes called the Nile River model) and the ARMA model in time series also belong to this type. 

Another type deals with the case where the Fisher information matrix diverges to infinity. A typical example is the location model written as 

**==> picture [207 x 10] intentionally omitted <==**

where _f (x)_ is a function having a finite support and its derivative is not 0 at the boundaries. The unknown parameter is the mean value _ξ_ . A typical example is the uniform distribution over [ _ξ,_ 1 + _ξ_ ]. We do not discuss this case, although its geometry is interesting, because its metric is not Riemannian but Finslerian. We do not have a good geometrical theory yet. See a preliminary study by Amari (1984). 

For _N_ observations from a probability distribution _p(_ _**x** ,_ _**ξ** )_ , consider the log likelihood ratio divided by ~~√~~ _N_ , 

**==> picture [214 x 30] intentionally omitted <==**

It is asymptotically subject to the _χ_[2] -distribution with _n_ degrees of freedom, where _n_ is the dimension number of _**ξ**_ , when _M_ is regular. By analyzing its behavior, we can prove that the maximum likelihood estimator is asymptotically best, unbiased and Gaussian, the error covariance matrix of which is the inverse of the Fisher information matrix divided by _N_ asymptotically. 

The maximum likelihood estimator is no more subject to the Gaussian distribution even asymptotically in a singular statistical model of the first type when the true distribution is at a singular point. However, it is asymptotically consistent and its convergence speed is in the order of 1 _/_ √ _N_ . It has been known for many years that some statistical models are singular. Fukumizu (2003) proved that the log likelihood (12.162) diverges to infinity in the order of log _N_ and log log _N_ in the cases of multilayer perceptrons and mixture models, respectively. There is a Japanese monograph by Fukumizu and Kuriki (2004), which studies singular statistical models in detail. 

Model selection is an important problem, which decides the number of hidden neurons from observed data in the case of the multilayer perceptron. As is well 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

312 

known, a model having a large number of free parameters fits the observed data well. The training error decreases as the number of parameters increases. However, the estimated parameters overfit and are not useful for predicting the behavior of future data, because the generalization error increases as the number of parameters increases beyond a certain value. There is an adequate number of parameters, which should be decided from the observed data. 

The Akaike Information Criterion (AIC) and Minimum Description Length (MDL) are two well-known criteria for model selection. The Baysian Information Criterion (BIC) is the same as MDL, although their underlying philosophies are different. 

Multilayer perceptrons and Gaussian mixtures are models of frequent use in applications. They are hierarchical singular models in which a lower degree model is included in the critical region of a higher degree model. We need to decide an adequate degree, that is, the number of parameters from the observed data. AIC and MDL are frequently used for this purpose without the singular structure being taken into account. There have been many discussions concerning which criteria are to be used, AIC or MDL. Both AIC and MDL are derived by using the maximum likelihood estimator, assuming that it is asymptotically Gaussian with covariance matrix 1 _/N_ times the inverse of the Fisher information. However, it is not Gaussian when the true parameter is in the critical region. When the true distribution is in a smaller model, it is in a critical region of a larger model. So neither MDL nor AIC are valid in such hierarchical models. They need to be modified. We should take account of corrections due to the singularity. In the case of multilayer perceptrons, the penalty term of AIC should be log _N_ times the number of parameters, instead of twice the number of parameters. This comes from the asymptotic property of log likelihood. Watanabe (2010) proposed a new information criterion taking the singular structure into account. 

## _**12.2.7 Bayesian Inference and Singular Model**_ 

Bayesian inference presumes a prior distribution _π(_ _**ξ** )_ on the parameters _**ξ**_ of a statistical model. For a family of probability distributions _M_ = { _p(_ _**x** ,_ _**ξ** )_ }, the joint probability of _**ξ**_ and _**x**_ is given by 

**==> picture [213 x 10] intentionally omitted <==**

Therefore, the conditional distribution of _**ξ**_ , conditioned on the observed training data is 

**==> picture [254 x 27] intentionally omitted <==**

12.2 Singularity in Learning: Multilayer Perceptron 

313 

Its logarithm divided by _N_ is 

**==> picture [318 x 22] intentionally omitted <==**

where _c_ is a term not depending on _**ξ**_ . The maximum posterior estimate is its maximizer, 

**==> picture [254 x 22] intentionally omitted <==**

As is shown in (12.165), a penalty term due to the Bayesian prior distribution is added to the loss function, which is the negative of the log prior probability. 

Theeffectofthepriordistributiondecreasesasthenumberofthetrainingexamples _N_ increases in a regular statistical model, as is seen from (12.165). The maximum a posteriori estimator (MAP) converges to the maximum likelihood estimator in this case. However, a singular statistical model has different characteristics. 

Let us consider a smooth non-zero prior in a singular model like the multilayer perceptron. It includes the critical region _R_ which is a union of subspaces, including an infinite number of points. Such a region is reduced to one point in the space of the outputs functions _M_[˜] . Hence, a uniform prior (improper prior) on the parameter space _M_ is not uniform on _M_[˜] . The prior of a singular point is an integration of prior probabilities over an equivalence class _R_ , so that the prior distribution of _M_[˜] is singular, because singular points in _M_[˜] have an infinitely large prior probability measure compared to a regular point. 

The parameter space _Mn_ of a perceptron including _n_ hidden neurons is included in _Mn_ +1 as a submanifold. But _Mn_ is included in _Mn_ +1 as a critical region, because it is given by _vi_ = 0, | _**w** i_ | = 0 or _**w** i_ = _**w** j_ in _Mn_ +1. Hence, when we consider a smooth non-zero prior in _Mn_ +1, a singular point _M_[˜] _n_ +1 collects prior probabilities of infinitely many points in a critical region of _Mn_ +1. 

When we take the maximum a posteriori estimator, a model having a smaller number of parameters is advantageous because of the singular prior. Hence, the Bayesian MAP has a tendency to select a smaller model, automatically selecting an adequate model, although there is no guarantee that this is optimal. 

Watanabe and his school (Watanabe 2001, 2009) have studied the effects of singularity in Bayesian inference by using modern algebraic geometry. The theory uses deeper knowledge of mathematics and is beyond the scope of the present monograph. 

## **Remarks** 

ThepresentchapterfocusesonthenaturalgradientmethodinaRiemannianmanifold. Since many engineering problems are formulated in a Riemannian manifold, the natural gradient is useful. We have treated on-line and batch learning procedures and shown that the natural gradient method demonstrates excellent performance. 

The multilayer perceptron uses the gradient method (back-propagation) in a Riemannian manifold of parameters. It is a constituent of deep learning, so its dynamical performance should be studied carefully. However, the parameter space includes 

12 Natural Gradient Learning and Its Dynamics in Singular Regions 

314 

widely spread singular regions in which the Fisher metric degenerates. Hence it is not a regular statistical model but is a singular statistical model. We have studied the dynamics of back-propagation learning based on the vanilla gradient, showing its bad performance due to singularities. The natural gradient method is free from such flaws both for the Fisher metric and the absolute Hessian metric. This characteristic is retained in the K-FAC approximation (Martens and Grosse 2015). However, it remains as a problem to be studied how the dynamics of learning behaves in a neighborhood of singularity when the true model is not in the singular region. We will be able to show by using the blow-down technique that the trajectory is not trapped in the singularity. We have also studied the statistical problem related to singularities. 

There are other interesting topics related to the natural gradient in a Riemannian manifold. One may use any Riemannian metric, such as the Killing metric in _Gl(n)_ and the absolute Hessian metric (Dauphin et al. 2014). Girolami and Calderhead (2011) presented the MCMC method in a Riemannian manifold by using the natural gradient. Reinforcement learning also uses the natural gradient in a policy manifold which is Riemannian. See, e.g., Kakade (2001), Kim et al. (2010), Roux et al. (2014), Peters and Schaal (2008), Thomas et al. (2013). Optimization in the stochastic relaxation regime is another area where natural gradient learning is effective (Malagò and Pistone 2014; Malagò et al. 2013, Hansen and Ostermeier 2001). One important problem is to evaluate the inverse of the Fisher information or its approximation effectively. See Martens (2015) and Martens and Grosse (2015). The adaptive natural gradient method is one solution. 

The natural gradient method is a first-order gradient method in a Riemannian manifold and is different from a second-order method such as the Newton method. We can further extend the natural gradient method to the natural Newton method, natural conjugate gradient method, etc. in a Riemannian manifold. See Edelman et al. (1998), Honkela et al. (2010) and Malago and Pistone (2014). 

## **Chapter 13 Signal Processing and Optimization** 

In the real world, signals are mostly stochastic. Signal processing makes use of stochastic properties to find the hidden structure we want to know about. The present chapter begins with principal component analysis (PCA), by studying the correlational structure of signals to find principal components in which the directions of signals are widely spread. Orthogonal transformations are used to decompose signals into non-correlated principal components. However, “no correlation” does not mean “independence” except in the special case of Gaussian distributions. Independent component analysis (ICA) is a technique of decomposing signals into independent components. Information geometry, in particular semi-parametrics, plays a fundamental role in this. It has stimulated the rise of new techniques of positive matrix decomposition and sparse component analysis, which we also touch upon. The optimization problem under convex constraints and a game theory approach are briefly discussed in this chapter from the information geometry point of view. The Hyvärinen scoring method shows an attractive direction to be studied further from information geometry. 

## **13.1 Principal Component Analysis** 

## _**13.1.1 Eigenvalue Analysis**_ 

Let _**x**_ be a vector random variable, which has already been preprocessed such that its expectation is 0, 

**==> picture [187 x 10] intentionally omitted <==**

The original version of this chapter was revised: The incomplete texts have been updated. The correction to this chapter is available at https://doi.org/10.1007/978-4-431-55978-8_14 

315 

© Springer Japan 2016, corrected publication 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_13 

316 

13 Signal Processing and Optimization 

Then, its covariance matrix is 

**==> picture [200 x 13] intentionally omitted <==**

If we transform _**x**_ into _**s**_ by using an orthogonal matrix **O** , 

**==> picture [187 x 12] intentionally omitted <==**

the covariance matrix of _**s**_ is given by 

**==> picture [221 x 13] intentionally omitted <==**

Let us consider the eigenvalue problem of **V** _X_ , 

**==> picture [190 x 9] intentionally omitted <==**

Then, we have _n_ eigenvalues _λ_ 1 _, . . . , λn, λ_ 1 _> λ_ 2 _> . . . > λn >_ 0 and corresponding _n_ unit eigenvectors _**o**_ 1 _, . . . ,_ _**o** n_ , where we assume that there are no multiple eigenvalues. (When there exist multiple eigenvalues, rotational indefiniteness appears. We do not treat such a case here.) Let **O** be the orthogonal matrix consisting of the eigenvectors 

**==> picture [200 x 10] intentionally omitted <==**

Then, **V** _S_ is a diagonal matrix 

**==> picture [206 x 42] intentionally omitted <==**

and the components of _**s**_ are uncorrelated, 

**==> picture [210 x 13] intentionally omitted <==**

## _**13.1.2 Principal Components, Minor Components and Whitening**_ 

Signal _**x**_ is decomposed into a sum of uncorrelated components as 

**==> picture [193 x 29] intentionally omitted <==**

13.1 Principal Component Analysis 

317 

**==> picture [332 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 13.1 Principal x 2<br>components  s 1 , s 2 , . . .<br>s 1<br>s 2<br>[.]<br>[..] . [.]<br>. .  [.] . .<br>. . x 1<br>... . . .<br>...<br>:<br>**----- End of picture text -----**<br>


Since the variance of _si_ is _λi_ , _s_ 1 has the largest magnitude on average, _s_ 2 the second, and finally _sn_ has the smallest magnitude. See Fig. 13.1. We call _s_ 1 the (first) principal component of _**x**_ , which is obtained by projecting _**x**_ to _**o**_ 1. The first _k_ largest components are given by _s_ 1 _, . . . , sk_ . We call the subspace spanned by _k_ eigenvectors _**o**_ 1 _, . . . ,_ _**o** k_ the _k_ -dimensional principal subspace. The vector 

**==> picture [192 x 30] intentionally omitted <==**

is the projection of _**x**_ to the principal subspace. 

The dimensions of _**x**_ are reduced by the projection, keeping the resultant vector as close to the original one as possible in the sense that the magnitude of the lost part 

**==> picture [222 x 37] intentionally omitted <==**

is minimized. So the principal components are used for approximating _**x**_ with a small number of components, reducing the dimensions. 

Similarly, the _k_ minor components are given by _sn_ − _k_ +1 _, . . . , sn_ , which are projections of _**x**_ to _**o** i , i_ = _n_ − _k_ + 1 _, . . . , n_ . The subspace spanned by _**o** n_ − _k_ +1 _, . . . ,_ _**o** n_ , is called the _k_ -dimensional minor subspace. The projection of _**x**_ to the minor subspace is given by 

**==> picture [200 x 29] intentionally omitted <==**

13 Signal Processing and Optimization 

318 

This is the maximizer of 

**==> picture [224 x 37] intentionally omitted <==**

Note that the minor components of **V** _X_ are the principal components of **V**[−] _X_[1][, because] the eigenvalues of **V**[−] _X_[1][are 1] _[/][λ][n][,]_[ 1] _[/][λ][n]_[−][1] _[, . . . ,]_[ 1] _[/][λ]_[1][. The eigenvectors of] **[ V]**[−] _X_[1][are the] same as those of **V** _X_ , but the order is reversed as _**o** n, . . . ,_ _**o**_ 1. Let us rescale the magnitudes of _n_ eigenvectors to give a new set of basis vectors 

**==> picture [223 x 13] intentionally omitted <==**

Then, _**x**_ is written in the new basis as 

**==> picture [193 x 15] intentionally omitted <==**

where 

**==> picture [192 x 24] intentionally omitted <==**

so that 

**==> picture [196 x 13] intentionally omitted <==**

This implies that the covariance matrix of _**s**_ ˜ is the identity matrix 

**==> picture [183 x 11] intentionally omitted <==**

The transformation of _**x**_ to _**s**_ ˜ is called whitening of _**x**_ . This naming originates from the fact that, when we deal with time series _x(t), t_ = 1 _,_ 2 _,_ 3 _, . . ._ , the transformation (13.15) changes the time series _x(t)_ into white noise series _s_ ˜ _(t)_ . 

Since **V** ˜ _S_ is the identity matrix, it is invariant if we further transform _**s**_ ˜ by using an arbitrary orthogonal matrix **U** as 

**==> picture [183 x 12] intentionally omitted <==**

Hence, whitening is not unique and there remains the indefiniteness of rotation, i.e., a further transformation by **U** . In factor analysis, this fact is known as the indefiniteness of rotation. In order to dissolve the indefiniteness, we need to use higher-order statistics by assuming that the signals are not Gaussian. This is the motivation for discussing independent component analysis (ICA) in the next section. 

13.1 Principal Component Analysis 

319 

## _**13.1.3 Dynamics of Learning of Principal and Minor Components**_ 

When _N_ examples _**x**_ 1 _, . . . ,_ _**x** N_ are observed as data _D_ , we estimate the covariance matrix by 

**==> picture [205 x 22] intentionally omitted <==**

and find the principal components by calculating its eigenvalues and eigenvectors. When examples are given one by one, we use a learning algorithm. We begin with a simple case of deriving the first principal component _**o**_ 1. Let _**w**_ be the candidate of the first principal eigenvector, satisfying 

**==> picture [186 x 11] intentionally omitted <==**

Let 

**==> picture [186 x 10] intentionally omitted <==**

be the projection of _**x**_ to _**w**_ . Then the loss function to be minimized is 

**==> picture [202 x 22] intentionally omitted <==**

under the constraint (13.21). By using the Lagrangian multiplier, the stochastic gradient method of obtaining the principal component is given by 

**==> picture [256 x 12] intentionally omitted <==**

This was derived by Amari (1977) as a special case of neural learning, because the relation (13.22) is regarded as the output of a linear neuron. The same algorithm was discovered by Oja (1982) and was generalized to obtain the _k_ -dimensional principal subspace (Oja 1992). 

Let **W** be an _n_ × _k_ matrix consisting of _k_ orthogonal unit column vectors _**w**_ 1 _, . . . ,_ _**w** k_ , 

**==> picture [209 x 10] intentionally omitted <==**

satisfying 

**==> picture [192 x 12] intentionally omitted <==**

where **I** _k_ is the _k_ × _k_ unit matrix. The set of all such matrices forms a manifold _Sn,k_ , called the Stiefel manifold. The projection of _**x**_ to the subspace spanned by _**w**_ 1 _, . . . ,_ _**w** k_ is 

**==> picture [218 x 15] intentionally omitted <==**

13 Signal Processing and Optimization 

320 

where 

**==> picture [190 x 10] intentionally omitted <==**

For obtaining the _k_ -dimensional principal subspace spanned by the column vectors of **W** , the loss function to be minimized is 

**==> picture [230 x 22] intentionally omitted <==**

The gradient descent learning equation for **W** is 

**==> picture [319 x 24] intentionally omitted <==**

Its averaged version in continuous time is 

**==> picture [233 x 12] intentionally omitted <==**

˙ where denotes the time derivative _d/dt_ . 

The solution _**w**_ 1 _, . . . ,_ _**w** k_ of learning Eqs. (13.30) or (13.31) converges to the subspace spanned by _k_ principal eigenvectors. However, each _**w** i_ does not correspond to the eigenvectors _**o** i_ , although the principal subspace is spanned by _**w**_ 1 _, . . . ,_ _**w** k_ . 

In order to obtain the _k_ principal eigenvectors, Xu (1993) introduced a diagonal matrix 

**==> picture [206 x 43] intentionally omitted <==**

satisfying _d_ 1 _> . . . > dk_ and modified (13.31) as 

**==> picture [242 x 12] intentionally omitted <==**

This algorithm gives the principal eigenvectors _**w** i_ = _**o** i_ . 

It appears that a similar algorithm would be applicable to the problem of obtaining the minor component subspace. We need to find **W** that maximizes (13.29). If we use gradient ascent instead of gradient descent, the algorithm would be 

**==> picture [226 x 11] intentionally omitted <==**

However, this does not work. Why (13.34) does not work had been a puzzle. 

Both algorithms (13.31) and (13.34) work well when **W** is limited in the Stiefel manifold _Sn,k_ . The manifold _Sn,k_ is a submanifold of _Mn,k_ , which is the manifold of all _n_ × _k_ matrices. When we solve (13.34) or its stochastic version numerically, **W** _(t)_ deviates from _Sn,k_ because of numerical errors. Algorithms (13.31) and (13.34) define flows **M**[˙] in the entire _Mn,k_ , where **M** _(t)_ ∈ _Mn,k_ , when **W** is replaced by **M** . The 

13.1 Principal Component Analysis 

321 

**==> picture [373 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>Mn,k Mn,k<br>Sn,k Sn,k<br>**----- End of picture text -----**<br>


**Fig. 13.2** Flow in **a** principal subspace, **b** minor subspace 

flow is closed in _Sn,k_ , that is, **M**[˙] ∈ _Sn,k_ when **M** ∈ _Sn,k_ . _Sn,k_ is a stable submanifold of the flow (13.31) in _Mn,k_ . Hence, when a small fluctuation occurs in **W** and it deviates from _Sn,k_ into _Mn,k_ , it automatically returns to _Sn,k_ (Fig. 13.2a). However, in the case of the flow (13.34) for minor components, _Sn,k_ is not stable in _Mn,k_ and **W** leaves _Sn,k_ due to the small deviation (Fig. 13.2b). This is the reason why the algorithm (13.34) does not work. 

Consider two modified differential equations in _Mn,k_ due to Chen et al. (1998), 

**==> picture [243 x 26] intentionally omitted <==**

Then, we can prove that the submanifold _Sn,k_ is neutrally stable with regard to both of the flows. Therefore, we can use (13.35) to obtain the principal components and (13.36) to obtain the minimal components. The on-line learning versions of (13.35) and (13.36) are 

**==> picture [307 x 24] intentionally omitted <==**

where _**m** i_ is the _i_ th column vector of **M** . 

The dynamics (13.35) and (13.36) possess interesting invariants. Let 

**==> picture [213 x 9] intentionally omitted <==**

be the singular decomposition of **M** _(t)_ , where **W** _(t)_ is an element of _Sn,k_ consisting of _k_ orthogonal unit vectors, **U** _(t)_ is a _k_ × _k_ orthogonal matrix and **D** is a _k_ × _k_ diagonal matrix with diagonal entries _d_ 1 _, . . . , dk_ . 

- **Lemma 13.1** _(1)_ _**M**[T] (t)_ _**M** (t) is an invariant of (13.35) and (13.36),_ _**M**[T] (t)_ _**M** (t)_ = _**M**[T] (_ 0 _)_ _**M** (_ 0 _)._ 

- _(2)_ _**D** (t) is an invariant of (13.35) and (13.36),_ _**D** (t)_ = _**D** (_ 0 _)._ 

- _(3)_ _**U** (t) is an invariant of (13.35) and (13.36),_ _**U** (t)_ = _**U** (_ 0 _)._ 

13 Signal Processing and Optimization 

322 

We omit the proof (see Chen et al. 1998). We immediately obtain the algorithm of Xu (1993) by using an initial condition **D** _(_ 0 _)_ = diag { _d_ 1 _, . . . , dk_ } and rewriting (13.35) in terms of **W** _(t)_ . When _k_ = _n_ , both (13.35) and (13.36) give the Brockett flow (Brockett 1991), where the cost function is 

**==> picture [215 x 14] intentionally omitted <==**

This is the natural gradient flow in the manifold of the orthogonal matrices (see Chen et al. 1998). 

Since _Sn,k_ is neutrally stable in Eqs. (13.35) and (13.36), numerical errors may accumulate. Chen and Amari (2001) proposed the following equations 

**==> picture [302 x 30] intentionally omitted <==**

where **D** is a positive diagonal matrix related to the initial value of **M** , 

**==> picture [214 x 84] intentionally omitted <==**

_Sn,k_ is stable both under (13.40) and (13.41), so both the principal eigenvectors and minor eigenvectors are extracted stably by the respective equations, which differ only in signature. 

## **13.2 Independent Component Analysis** 

Consider the problem of decomposing vector random variable _**x**_ into _n_ independent components, 

**==> picture [194 x 28] intentionally omitted <==**

such that _si_ are independent random variables and { _**a**_ 1 _, . . . ,_ _**a** n_ } is a new set of basis vectors. We consider the case where _n_ independent component signals _s_ 1 _, . . . , sn_ exist under an adequate basis. When _**x**_ is Gaussian, PCA is successful for performing this job. However, there are infinitely many such decompositions due to rotational indefiniteness, as stated in the previous section. Moreover, when _**x**_ is non-Gaussian, 

13.2 Independent Component Analysis 

323 

**==> picture [284 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) s 2 (b) x 2<br>principal vector o 1<br>o 2<br>s 1 x 1<br>eye<br>**----- End of picture text -----**<br>


**Fig. 13.3 a** Uniform distribution _P(s)_ ; **b** Its linear transformation _p(x)_ 

PCA does not work for this purpose. This is because, even if no correlations exist among _n_ signals _s_ 1 _, . . . , sn_ , this does not imply that they are independent. 

We give a simple example. Let _s_ 1 and _s_ 2 be two independent signals, where both _s_ 1 and _s_ 2 are subject to the uniform distribution over [−0 _._ 5 _,_ 0 _._ 5]. They are distributed uniformly over the square (Fig. 13.3a). We construct their mixtures _**x**_ = _(x_ 1 _, x_ 2 _)[T]_ by 

**==> picture [196 x 24] intentionally omitted <==**

Then, _**x**_ is uniformly distributed in a parallelepiped (see Fig. 13.3b). Its covariance matrix is 

**==> picture [196 x 20] intentionally omitted <==**

of which the eigenvectors are different from the original _s_ 1 and _s_ 2 axes. The PCA solution gives non-correlated components but they are not independent. So we need other methods to decompose _**x**_ into independent components. Higher-order statistics beyond the covariance is useful for solving the problem. 

An illustrative example of ICA is the cocktail party problem. There are _n_ persons in a cocktail party room who are speaking independently. Let _si (t)_ be the voice of person _i_ at time _t_ . _m_ microphones are placed in the party room, so that each microphone records a mixture of voices of _n_ persons. Let _x j (t)_ be the sound recorded by microphone _j_ at time _t_ . See Fig. 13.4. They are written as 

**==> picture [242 x 11] intentionally omitted <==**

where _A ji_ is a coefficient of mixing depending on the distance between person _i_ and microphone _j_ . The problem is to recover the sounds _**s** (_ 1 _),_ _**s** (_ 2 _), . . ._ of all the persons from the recorded mixtures _**x** (_ 1 _),_ _**x** (_ 2 _), . . ._ , without any knowledge of _A ji_ . Here we assume that the numbers of persons and microphones are the same, _n_ = _m_ . When _n < m_ , we first apply PCA to _**x**_ , projecting it to the _n_ -dimensional principal 

13 Signal Processing and Optimization 

324 

**Fig. 13.4** _n_ persons and _m_ microphones in a room 

**==> picture [261 x 119] intentionally omitted <==**

**----- Start of picture text -----**<br>
xm ...<br>. .<br>. Am 1 . s 3 .<br>sn . s 1 A 13 . x 2<br>A 11 . s 2<br>. A 12<br>x 1<br>**----- End of picture text -----**<br>


subspace. Then, the problem reduces to the case of _m_ = _n_ . When _m < n_ , we need techniques of sparse signal processing. 

We assume that **A** is a regular _n_ × _n_ matrix. When **A** is known, the problem is trivially solved by 

**==> picture [199 x 12] intentionally omitted <==**

and _**y** (t)_ is equal to the original _**s** (t)_ . However, **A** or **A**[−][1] is unknown. We transform _**x**_ by using a matrix **W** as 

**==> picture [196 x 10] intentionally omitted <==**

and check if _n_ components of _**y**_ in time series _**y** (_ 1 _), . . . ,_ _**y** (T )_ are independently distributed or not. If they are not independent, we modify **W** such that the degree of non-independence decreases. To this end, we need to define the degree of nonindependence of _n_ random variables _y_ 1 _, . . . , yn_ . Since it is a function of **W** , we can apply the stochastic gradient descent or the natural gradient descent method to obtain **W** that recovers the independent signals. 

Before defining the degree of non-independence, we note the indefiniteness of the solution. As is known, the independent components are recovered only when all the components of _**s**_ except for one are non-Gaussian. Further, the order of signals _s_ 1 _, . . . , sn_ is not recovered, since any permutation of _n_ independent signals keeps their independence. Moreover, the magnitude of _si_ is not recovered, because, when _s_ 1 _, . . . , sn_ are independent, _c_ 1 _s_ 1 _, c_ 2 _s_ 2 _, . . . , cnsn_ are independent for any constants _c_ 1 _, . . . , cn_ . Hence, the independent components are recovered to within the scales and order. 

We formulate the problem mathematically. Let _ki (si )_ be the probability density function of the _i_ th independent component _si_ , where we assume that 

**==> picture [188 x 10] intentionally omitted <==**

Then, the joint probability density of _**s**_ is 

**==> picture [203 x 15] intentionally omitted <==**

325 

13.2 Independent Component Analysis 

For _**y**_ determined from (13.49), the joint probability density is written as 

**==> picture [241 x 14] intentionally omitted <==**

Here, we used the general formula that probability density function _p(_ _**x** )_ changes to 

**==> picture [213 x 27] intentionally omitted <==**

when _**x**_ is transformed to _**y**_ as 

**==> picture [187 x 10] intentionally omitted <==**

The KL-divergence from _pY (_ _**y** )_ to _k(_ _**y** )_ , 

**==> picture [247 x 24] intentionally omitted <==**

would be used as a degree of non-independence. This would be a good choice if we knew _k(_ _**s** )_ . However, we do not know _k(_ _**s** )_ and what we know is only the fact that _k(_ _**s** )_ is decomposed into the product of unknown _ki (si )_ . We use _n_ arbitrary independent distributions, 

**==> picture [203 x 15] intentionally omitted <==**

**==> picture [240 x 24] intentionally omitted <==**

as a function to show the degree of non-independence. This choice is reasonable as follows. 

We consider the manifold of all the probability distribution 

**==> picture [190 x 10] intentionally omitted <==**

to understand the situation geometrically. We define the submanifold _SI_ of all the independent distributions 

**==> picture [321 x 19] intentionally omitted <==**

which is an _e_ -flat submanifold of _S_ . It includes both _k(_ _**y** )_ and _q(_ _**y** )_ . Another submanifold we consider is 

**==> picture [206 x 10] intentionally omitted <==**

which is parameterized by **W** . For each **W** , we have a distribution _pY (_ _**y**_ ; **W** _)_ given by the transformation of _**y**_ = **W** _**x**_ . It is not a flat submanifold. See Fig. 13.5. 

326 

13 Signal Processing and Optimization 

**Fig. 13.5** _SI e_ -flat submanifold of independent distributions, _SN_ submanifold generated by _**W**_ . They are orthogonal 

**==> picture [95 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
S<br>S W<br>pY( [y] [;] [W] )<br>SI<br>k ( y ). . q ( y )<br>**----- End of picture text -----**<br>


We use a loss function 

**==> picture [238 x 13] intentionally omitted <==**

when we know _k(_ _**s** )_ . _SW_ and _SI_ intersect at **W** = **A**[−][1] and the loss function _L_ is 0 at this point. However, we do not know _k(_ _**s** )_ , so we use 

**==> picture [234 x 13] intentionally omitted <==**

by using an adequately chosen _q_ (Bell and Sejnowski 1995). We can show that _SW_ and _SI_ intersect orthogonally. In spite of this, we cannot apply the Pythagorean theorem, because _SW_ is not _m_ -flat. However, because of the orthogonality, we show that **W** = **A**[−][1] is a critical point of _L_ . It is a local minimum, saddle or local maximum depending on the choice of _q_ . The stability of the critical point depends on _q_ and the _m_ -embedding curvature of _SW_ at _q_ = _k_ . When _q_ is close to _k_ , **A**[−][1] is certainly a global minimum. We neglect the indefiniteness of **W** concerning scales and permutations in the present discussions, but the situation is the same for all equivalent **W** . 

We should remark that there are many loss functions other than (13.62). By mixing independent _s_ 1 _, . . . , sn_ , the central limit theorem suggests that the distribution of _**x**_ approaches a jointly Gaussian distribution. Hence, the degree of non-Gaussianity can be used as a loss function. The higher-order cumulants of _**y**_ vanish when _**y**_ is Gaussian, so that the sum of the absolute values of the third- and fourth-order cumulants play the role of a loss function. We may use other measures of nonGaussianity as a loss function. See Hyvärinen et al. (2001) and Cichocki and Amari (2002). The following analysis is common to all such loss functions. 

The stochastic descent on-line learning algorithm is given by 

**==> picture [255 x 23] intentionally omitted <==**

13.2 Independent Component Analysis 

327 

The loss function is written as 

**==> picture [262 x 40] intentionally omitted <==**

where 

**==> picture [236 x 23] intentionally omitted <==**

is the entropy of _**y**_ expressed as a function of **W** . We see 

**==> picture [219 x 10] intentionally omitted <==**

In order to calculate the gradient of the instantaneous loss 

**==> picture [240 x 10] intentionally omitted <==**

with respect to **W** , where _H (X )_ is neglected because it does not depend on **W** , we consider a small change of _l(_ _**y** ,_ **W** _)_ due to a small change of **W** , from **W** to **W** + _d_ **W** . We have 

**==> picture [291 x 13] intentionally omitted <==**

Similarly, we have 

**==> picture [217 x 24] intentionally omitted <==**

We put 

**==> picture [206 x 25] intentionally omitted <==**

Further, from 

**==> picture [196 x 10] intentionally omitted <==**

we have, for _**ϕ** (_ _**y** )_ = [ _ϕ_ 1 _(y_ 1 _) , . . . , ϕn (yn)_ ] _[T]_ , 

**==> picture [233 x 12] intentionally omitted <==**

Hence, we have 

**==> picture [263 x 13] intentionally omitted <==**

from which the gradient of the instantaneous loss _l_ with respect to **W** , _∂ D/∂Wi j_ , is calculated by using the component form. 

13 Signal Processing and Optimization 

328 

In order to obtain the natural gradient, we need to introduce a Riemannian metric in the manifold _Gl(n)_ of matrices. Let _d_ **W** be a small line element, which is written as 

**==> picture [208 x 10] intentionally omitted <==**

where **E** _i j_ is a matrix whose _(i, j)_ element is 1 and all the other elements are 0. They form a basis in the tangent space. We consider the Lie group structure of _Gl(n)_ . **W** is mapped to the identity matrix by multiplying **W**[−][1] from the right, 

**==> picture [192 x 11] intentionally omitted <==**

We also map a nearby point **W** + _d_ **W** by multiplying **W**[−][1] from the right, giving 

**==> picture [233 x 12] intentionally omitted <==**

Hence, a small line element _d_ **W** in the tangent space of _Gl(n)_ at **W** is mapped to 

**==> picture [198 x 12] intentionally omitted <==**

in the tangent space at **I** . See Fig. 13.6. We define the magnitude of _d_ **X** at **I** simply by 

**==> picture [250 x 16] intentionally omitted <==**

A Riemannian metric is defined by defining the magnitude of _d_ **W** at the tangent space at **W** . We use the Lie group invariance such that the magnitude does not change by 

**Fig. 13.6** Mapping of _T_ **W** to _T_ **I** 

**==> picture [130 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
W<br>W + d W<br>.<br>multiplication of  W [-1]<br>. I + d X<br>I<br>**----- End of picture text -----**<br>


13.2 Independent Component Analysis 

329 

the right multiplication of **W**[−][1] . Then, the magnitude of _d_ **W** is defined by that of the corresponding _d_ **X** , 

**==> picture [221 x 10] intentionally omitted <==**

This is rewritten as 

**==> picture [251 x 18] intentionally omitted <==**

which is called the Killing metric. The length of a tangent vector is invariant by multiplying a matrix from the right. 

One may wonder if there is a coordinate transformation of **W** , 

**==> picture [190 x 10] intentionally omitted <==**

from which _d_ **X** is derived by 

**==> picture [202 x 22] intentionally omitted <==**

Unfortunately, there is no such coordinate transformation. We can define _d_ **X** but it is not integrable, that is, the integration of _d_ **X** 

**==> picture [224 x 26] intentionally omitted <==**

from **W** to **W**[′] depends on the path connecting **W** and **W**[′] . So we do not have a coordinate system **X** in _Gl(n)_ such that _d Xi j_ are increments along new coordinate curves. Such virtual coordinates **X** are called a non-holonomic coordinate system, in which only _d_ **X** is defined. This non-holonomic basis of the tangent space is convenient for introducing a Riemannian metric to _Gl(n)_ and defining the natural gradient. 

The small change (13.73) of _l_ is written in terms of _d_ **X** as 

**==> picture [227 x 11] intentionally omitted <==**

This is written in the components as 

**==> picture [219 x 25] intentionally omitted <==**

Since the inner product ⟨ _d_ **X** _, d_ **X** ⟩ is Euclidean, as is seen from (13.78), it is the natural gradient due to the Killing metric. The increment of **W** is written as 

**==> picture [298 x 13] intentionally omitted <==**

by using _d_ **X** , where ∇ _X_ is the gradient with respect to **X** . By using (13.77), this is rewritten in terms of the gradient with respect to **W** as 

13 Signal Processing and Optimization 

330 

**==> picture [225 x 13] intentionally omitted <==**

Because of this, the natural gradient has an invariant property that the convergence of learning dynamics is the same whatever the true **W** is. The stability does not depend on **W** , either. These are desirable properties given by Cardoso and Laheld (1996) and Amari et al. (1996). 

## _**13.2.3 Estimating Function of ICA: Semiparametric Approach**_ 

The probability density function of observed _**x**_ can be written as 

**==> picture [237 x 37] intentionally omitted <==**

In this statistical model, the unknown parameters include not only **W** but also _n_ functions _k_ 1 _(s_ 1 _) , . . . kn (sn)_ , which are the probability densities of the independent source signals. The probability distribution of _**x**_ is specified by _n_ × _n_ matrix **W** , which are the parameters of interest to be estimated, and also by _n_ functions _k_ 1 _(s_ 1 _) , . . . kn (sn)_ , which are nuisance parameters of function-degrees of freedom. Therefore, ICA is a semi-parametric statistical problem (Amari and Cardoso 1997). 

An estimation function is a matrix **F** _(_ _**x** ,_ **W** _)_ which satisfies 

**==> picture [236 x 37] intentionally omitted <==**

Here, the expectation is taken with respect to _p(_ _**x** ,_ **W** _)_ , and **W** ≈ **W**[′] implies that **W** and **W**[′] are equivalent to within the scales and permutations. The estimating equation is given by 

**==> picture [236 x 30] intentionally omitted <==**

A sequential estimation is realized by the learning equation 

**==> picture [225 x 9] intentionally omitted <==**

which is expected to converge to the solution of (13.90), although the convergence is not necessarily guaranteed. 

Information geometry gives a general class of estimating functions. See Amari (1999) for details. Let _**ϕ** (_ _**y** )_ be an arbitrary vector function of _**y**_ . Then, an effective 

13.2 Independent Component Analysis 

331 

class of estimating functions is generated from 

**==> picture [233 x 11] intentionally omitted <==**

including arbitrary vector function _**ϕ**_ . Let **R** _(_ **W** _)_ be a linear reversible transformation of matrices acting on **F** as 

**==> picture [222 x 12] intentionally omitted <==**

**R** is a tensor having four indices and written in the component form as 

**==> picture [233 x 23] intentionally omitted <==**

The estimating equation is the same for **F** and **RF** , because 

**==> picture [211 x 22] intentionally omitted <==**

is equivalent to (13.90). 

The on-line learning equation using **RF** is 

**==> picture [219 x 10] intentionally omitted <==**

Although, the equilibrium point does not depend on **R** , its stability depends on **R** and so does the speed of convergence. Therefore, we need to choose _**ϕ** (_ _**y** )_ and **R** _(_ **W** _)_ carefully. 

Once _**ϕ** (_ _**y** )_ is chosen, the Newton method is applicable to solve the iterative procedure. From the estimating Eq. (13.90), we have 

**==> picture [305 x 27] intentionally omitted <==**

where _**x** t_ = _**x** (t)_ and ◦ is used for taking the trace of matrix multiplication. Using 

**==> picture [203 x 13] intentionally omitted <==**

we define the operator 

**==> picture [228 x 25] intentionally omitted <==**

The Newton method is written as 

**==> picture [235 x 13] intentionally omitted <==**

13 Signal Processing and Optimization 

332 

Therefore, the Newton method is derived by choosing **R** in the following way: 

**==> picture [203 x 12] intentionally omitted <==**

The operator **J** is a fourth-order tensor, and we can calculate it explicitly, but it depends on the true _k(_ _**s** )_ , which we do not know. 

An estimating function **F**[˜] _(_ _**x** ,_ **W** _)_ is said to be standard when it satisfies 

**==> picture [245 x 31] intentionally omitted <==**

Given an estimating function **F** , we have its standard version by 

**==> picture [217 x 12] intentionally omitted <==**

ThelearningequationusingastandardestimatingfunctioncorrespondstotheNewton method. The Hyvärinen fast algorithm (Hyvärinen 2005) uses a standard estimating function. 

Since the standard estimating function using _**ϕ** (_ _**y** )_ is written in the form of 

**==> picture [231 x 12] intentionally omitted <==**

where _α_ and _β_ are adequate parameters, we can use an adaptive method of choosing them from the data. The separating **W** is stable when we use a standard estimating function, because the Newton method is applied. 

One of surprising results is the following “super efficiency”. We define the covariance of the recovered signal at _t_ by 

**==> picture [232 x 13] intentionally omitted <==**

Then, it converges to 0 when the source separation is successful. We have the following super efficiency results: 

**Theorem 13.1** _When_ 

**==> picture [198 x 10] intentionally omitted <==**

_by using the standard estimating function_ _**F** , the covariances decrease in the order of_ 1 _/t_[2] _for the natural gradient learning,_ 

**==> picture [221 x 22] intentionally omitted <==**

_and in the order of η_[2] _when the learning constant η is fixed,_ 

**==> picture [222 x 10] intentionally omitted <==**

13.2 Independent Component Analysis 

333 

The condition (13.106) is satisfied in the following two cases: 

**==> picture [308 x 38] intentionally omitted <==**

See Amari (1999) for detailed discussions and proofs. 

_Remark_ When independent source signals _si (t)_ have temporal correlations such that 

**==> picture [220 x 10] intentionally omitted <==**

which are not 0 for some _τ >_ 0, we can use this information even if we do not know _ci (τ )_ explicitly. The previous results are valid even in this case, but we have more efficient methods by taking the existence of temporal correlation into account. The joint diagonalization of the delayed covariance matrices is one good idea. See Cardoso and Souloumiac (1996). The method works well even when the source signals are Gaussian. 

It is possible to develop a method of estimating functions even in this case. We obtain a general form of estimating functions, which includes arbitrary temporal filters to be applied to the observed signals _**x** (t)_ . The joint diagonalization is a special example of the estimating function method. See Amari (2000) for details. 

## **13.3 Non-negative Matrix Factorization** 

Given a series of observed signals _**x** (_ 1 _), . . . ,_ _**x** (T )_ , let us arrange all of them in an _n_ × _T_ matrix form, 

**==> picture [210 x 10] intentionally omitted <==**

ICA searches for the basis vectors { _**a**_ 1 _, . . . ,_ _**a** n_ }, which form an _n_ × _n_ mixing matrix 

**==> picture [198 x 10] intentionally omitted <==**

and _**x**_ is decomposed as 

**==> picture [223 x 15] intentionally omitted <==**

such that _s_ 1 _, . . . , sn_ are independent. (13.114) is represented as 

**==> picture [184 x 10] intentionally omitted <==**

in the matrix notation. 

13 Signal Processing and Optimization 

334 

There are many cases where _**x**_ is not a mixture of independent sources. ICA does not work in such cases. On the other hand, there are cases where the components _si_ are all non-negative. Visual images are such signals, where _s(i, j)_ are the brightness of an image at pixel _(i, j)_ . 

When all the components of _**s**_ are non-negative, they are distributed on the first quadrant of the signal space, which is a cone. When signals are transformed linearly by **A** as 

**==> picture [184 x 10] intentionally omitted <==**

_**x**_ ’s are distributed in another cone, because linear transformation **A** transforms one cone to another cone. Hence, from a number of observations _**x** (t)_ , we can find the cone in which the _**x**_ ’s sit (Fig. 13.7). The mixture matrix **A** is recovered from the cone of **X** . When the elements of **A** are also non-negative, those of **X** are non-negative. Therefore, the problem is formulated as follows: 

**Non-negative matrix factorization (NMF)** : Given non-negative matrix **X** , factorize it as the product of two non-negative matrices **A** and **S** , 

**==> picture [185 x 9] intentionally omitted <==**

We define a divergence _D_ [ **M** : **N** ] between two non-negative matrices **M** and **N** . Then, the loss function of decomposition is given by 

**==> picture [212 x 10] intentionally omitted <==**

The Frobenius matrix norm 

**==> picture [224 x 28] intentionally omitted <==**

**==> picture [256 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
sn xn<br>A x = As<br>s 1 x 1<br>A transforms the positive quadrant to a positive cone Oo 4<br>**----- End of picture text -----**<br>


**Fig. 13.7** A transforms the positive quadrant to a positive cone 

335 

13.3 Non-negative Matrix Factorization 

is a divergence of frequent use. This is the square of the Euclidean norm and is symmetric with respect to **A** and **B** . Another divergence is the KL-divergence defined by 

**==> picture [252 x 29] intentionally omitted <==**

Other divergences such as _α_ -, _β_ - and _(α, β)_ -divergences are also used on their own merits. See Cichocki et al. (2011). 

The alternating minimization is a useful procedure to find the minimum of two variables _L(_ **A** _,_ **S** _)_ . We fix **A** _[(][t][)]_ at time _t, t_ = 1 _,_ 2 _, . . ._ , and minimize _L(_ **A** _[(][t][)] ,_ **S** _)_ with respect to **S** . Let the minimizer be **S** _[(][t][)]_ . We then fix **S** _[(][t][)]_ and minimize _L(_ **A** _, S[(][t][)] )_ with respect to **A** . The minimizer is written as **A** _[(][t]_[+][1] _[)]_ . We repeat this procedure until convergence. 

The gradient descent method is used to obtain the minimizer of the loss function. However, we need to take the non-negativity of **A** and **S** into account. The conventional gradient descent method does not satisfy this requirement and components of matrices would become negative in the procedure. 

The exponential gradient descent (Kivinen and Warmuth 1997) is proposed to overcome this difficulty. Its procedure is as follows: 

**==> picture [303 x 25] intentionally omitted <==**

where _η_ is a learning constant. By using the logarithm, we have 

**==> picture [309 x 23] intentionally omitted <==**

Hence, (13.121) is the gradient descent applied to log **S** and log **A** . When _D_ is the Frobenius norm (13.119), we have 

**==> picture [303 x 23] intentionally omitted <==**

In this analogy, we have the following algorithm, originally proposed by Lee and Seung (1999): 

**==> picture [272 x 32] intentionally omitted <==**

TherearemanyalgorithmsforNMF.SeeCichockietal.(2011),forexample.NMF is further generalized to non-negative tensor factorization (NTF), where tensors are quantities having more than two indices. 

336 

13 Signal Processing and Optimization 

## **13.4 Sparse Signal Processing** 

We have studied linear signal decomposition from _**x**_ to _**s**_ , 

**==> picture [206 x 29] intentionally omitted <==**

This section deals with the case that they are mixtures of a very few non-zero components, that is, a vector signal _**s**_ is sparse. A signal _**s**_ is said to be _k_ -sparse when the components of _**s**_ are zero except for at most _k_ components. When _k_ is much smaller than the dimension number _n_ of _**s**_ , it is called a sparse vector. We consider a typical case that _k_ is of the order log _n_ or smaller, when _n_ is large. 

We interpret (13.126) such that _**x**_ is a linear combination of _n_ basis vectors _**a**_ 1 _, . . . ,_ _**a** n_ and a basis _**a** i_ is activated when _si_ is non-zero. Only a small number of basis vectors are activated in the sparse case. We assume that _**x**_ is generated sparsely but do not know which basis vectors are activated. Let _m_ be the dimension number of vector _**x**_ . We regard the _m_ components of _**x**_ as _m_ measurements concerning an unknown signal _**s**_ , where _**a**_ 1 _, . . . ,_ _**a** n_ are known. When _m > n_ , (13.126) is overdetermined, that is, the number _m_ of equations is larger than the number _n_ of unknowns. We usually assume that the observations are contaminated by noise, such that 

**==> picture [192 x 10] intentionally omitted <==**

where _**ε**_ is a noise vector, and we search for the least–squares solution. 

When _m < n_ ,theequationisunderdetermined.Thereareinfinitelymanysolutions satisfying (13.126) even when it is noise contaminated. A conventional solution is the generalized inverse that minimizes the Euclidean norm among all possible solutions. When we know that _**s**_ is sparse, we have a different solution. This was first noted by Chen et al. (1998). The following surprising theorem is known (Donoho 2006; Candes et al. 2006). 

**Theorem 13.2** _When n and m are large,_ _**s** is recovered correctly in most cases, provided_ _**s** is k-sparse and_ 

**==> picture [195 x 10] intentionally omitted <==**

Roughly speaking, when _k_ is a constant, a constant multiple of log _n_ observations are enough to recover the _n_ -dimensional _**s**_ . Since a very small number of sensors are enough, provided the original signal is sparse, the paradigm is called compressed sensing (Donoho 2006; Candes and Walkin 2008). Such a paradigm has emerged from statistics, ICA, signal processing and many related fields. It has grown to form a very hot field. There are many monographs and papers on this topic, see, e.g., Elad (2010), Eldar and Kutyniok (2012) and Bruckstein et al. (2009). 

13.4 Sparse Signal Processing 

337 

## _**13.4.1 Linear Regression and Sparse Solution**_ 

Let us formulate the linear regression problem 

**==> picture [193 x 10] intentionally omitted <==**

where _**x**_ is the observation vector, **A** = � _Ai j_ � is a known design matrix, _**θ**_ is the factor or explanatory vector to be determined and _**ε**_ is a noise vector. We use _**θ**_ instead of _**s**_ for the purpose of emphasizing that _**θ**_ is an _e_ -affine coordinate system. The loss function to be minimized is 

**==> picture [219 x 21] intentionally omitted <==**

We use _ψ(_ _**θ** )_ for the loss function in this subsection, because it plays the role of a convexfunctiondefiningduallyflat structure. This is thenegativeof thelog likelihood when the noises are independent Gaussian. Since _ψ_ is a quadratic function in the case of (13.130), by defining 

**==> picture [189 x 12] intentionally omitted <==**

we have 

**==> picture [229 x 22] intentionally omitted <==**

where _c_ is a constant. When _m > n_ , **G** is regular in general and the optimal solution is 

**==> picture [198 x 12] intentionally omitted <==**

When _m < n_ , **G** is singular and there are infinitely many solutions in this underdetermined case. Let _**s**_ 0 be a solution. Then, for any null vector satisfying 

**==> picture [185 x 10] intentionally omitted <==**

_**s**_ 0 + _**n**_ is a solution. The solution that minimizes the _L_ 2-norm is given by 

**==> picture [189 x 12] intentionally omitted <==**

where **A**[†] is the generalized inverse defined by 

**==> picture [207 x 15] intentionally omitted <==**

However, this solution is not sparse and almost all components are non-zero. 

13 Signal Processing and Optimization 

338 

The sparsest solution is the one that minimizes the number of non-zero components 

**==> picture [205 x 29] intentionally omitted <==**

However, this is a combinatorial problem and computationally difficult to solve for large _n_ . One may use the _L_ 1-norm instead of _L_ 0-norm, 

**==> picture [203 x 29] intentionally omitted <==**

to obtain a sparse solution (Ishikawa 1996). There are many studies concerning when the minimum _L_ 1-norm solution is identical to the minimum _L_ 0-norm solution. It is now known that the solutions of the two problems coincide when 

**==> picture [193 x 10] intentionally omitted <==**

for a randomly generated **A** with high probability. See, e.g., Candes et al. (2006). 

## _**13.4.2 Minimization of Convex Function Under L**_ **1** _**Constraint**_ 

We generalize the linear regression problem and study the problem of minimizing a general convex function _ψ(_ _**θ** )_ under the _L_ 1-constraint. See Hirose and Komaki (2010). The constraint is given by 

**==> picture [209 x 15] intentionally omitted <==**

We define a region of _**θ**_ by 

**==> picture [217 x 19] intentionally omitted <==**

As _c_ decreases, the constraint becomes stronger and finally when _c_ = 0, it includes only _**θ**_ = 0, the extremely sparse solution. See Fig. 13.8. 

We have assumed in (13.129) that the noise is Gaussian. When it is not Gaussian, the negative of the log likelihood function, _ψ(_ _**θ** )_ , is convex but is not a quadratic function. Another typical example is the logistic regression. In this case, given input _**x** i_ , the response _yi_ is binary, taking values 0 and 1. Its probability is given by 

**==> picture [256 x 19] intentionally omitted <==**

13.4 Sparse Signal Processing 

339 

**Fig. 13.8** Convex set _Bc_ and _m_ -projection of _**θ**_[∗] to it 

**==> picture [87 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bc . *<br>m -projection<br>*<br>c<br>**----- End of picture text -----**<br>


where 

**==> picture [211 x 12] intentionally omitted <==**

The loss function is the negative of log probability of the correct answer, 

**==> picture [247 x 13] intentionally omitted <==**

This is convex and is strictly convex when _m > n_ . The problem is the minimization of 

**==> picture [213 x 10] intentionally omitted <==**

where _λ_ is the Lagrange multiplier. We begin with the overdetermined case because it is simpler. The underdetermined case can be treated similarly, as will be stated later (see Donoho and Tsaig 2008). In the overdetermined case, there is a unique optimum _**θ**_[∗] minimizing _L(_ _**θ** )_ , that satisfies 

**==> picture [195 x 10] intentionally omitted <==**

This is the solution corresponding to a large enough _c_ and is not sparse. 

We introduce the dually flat geometry, where the _e_ -affine coordinates are _**θ**_ and the dual coordinates ( _m_ -flat coordinates) are given by 

**==> picture [192 x 10] intentionally omitted <==**

The Riemannian metric is 

**==> picture [203 x 10] intentionally omitted <==**

13 Signal Processing and Optimization 

340 

The divergence from _**θ**_ to _**θ**_[′] , derived from _ψ_ , is 

**==> picture [284 x 13] intentionally omitted <==**

Therefore, from (13.146), we see that 

**==> picture [222 x 12] intentionally omitted <==**

Hence, minimizing _ψ(_ _**θ** )_ is equivalent to minimizing the divergence from _**θ**_ to _**θ**_[∗] , that is the dual divergence from _**θ**_[∗] to _**θ**_ . Since the area _Bc_ defined by the constraint (13.141) is _e_ -convex, the following is immediate from the projection theorem. 

**Theorem 13.3** _The solution_ _**θ**_[∗] _c[that minimizes][ ψ][(]_ _**[θ]**[)][ in the area][B][c][is given by the] m-projection of_ _**θ**_[∗] _to Bc. The projection is unique._ 

The analytical equation for _**θ**_[∗] _c_[is obtained, by differentiating (][13.145][) with respect] to _**θ**_ , 

**==> picture [217 x 13] intentionally omitted <==**

Since the solution is the _m_ -projection of _**θ**_[∗] to _Bc_ , the _m_ -geodesic connecting _**θ**_[∗] and _**θ**_[∗] _c_[is orthogonal to the boundary of] _[ B][c]_[ if it lies on a smooth surface of] _[ B][c]_[ (Fig.][13.8][).] The gradient ∇ _L(_ _**θ** )_ is the normal vector of the surface of _L_ , which is the supporting hypersurface of _Bc_ at this point. However, since convex set _Bc_ is a polyhedron, it is not differentiable at low-dimensional faces, such as vertices, edges, etc., where some components satisfy 

**==> picture [182 x 12] intentionally omitted <==**

There are infinitely many supporting hypersurfaces at a non-differentiable point. The set of the normal vectors of the supporting hypersurfaces is called the subgradient of _L_ at that point (Fig. 13.9). 

We give an explicit form of the subgradient. Let _A(_ _**θ** )_ be the set of indices for which _θ[i]_ ̸= 0, 

**==> picture [208 x 13] intentionally omitted <==**

It is called the active set of _**θ**_ , because _θ[i]_ is active, that is, not 0, for _i_ ∈ _A(_ _**θ** )_ . Then, the subgradient is written as 

**==> picture [246 x 37] intentionally omitted <==**

where _εi_ may take an arbitrary value in [−1 _,_ 1]. 

There is only one _m_ -geodesic passing through a regular boundary point of _Bc_ orthogonally. On the other hand, there are infinitely many _m_ -geodesics which pass through a non-regular point and their tangent directions belong to the subgradient. 

13.4 Sparse Signal Processing 

341 

**==> picture [332 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fig. 13.9 Gradient and<br>subgradient of L . 7) *<br>L<br>.<br>. 6 *<br>L<br>.<br>. 6 *<br>...<br>**----- End of picture text -----**<br>


Therefore, there exist a larger number of points _**θ**_[∗] that are mapped to a non-regular point by the _m_ -projection as the sparsity becomes large. This explains why a sparse solution is obtained by the _L_ 1 regularization. See Fig. 13.9. 

## _**13.4.3 Analysis of Solution Path**_ 

Let us call _**θ**_[∗] _c_[the][solution][path,][considering] _[c]_[as][a][parameter][along][the][path.][It] connects the origin 0 and the optimal point _**θ**_[∗] as _c_ changes from 0 to a large value. Hence, the solution path gives sparse solutions of which the sparsity is specified by _c_ . LASSO is proposed for this purpose (Tibshirani 1996). Since the Lagrangian multiplier _λ_ is determined as a monotone function _λ(c)_ of _c_ , we may also regard _λ_ as another parameter of the path (Efron et al. 2004). The dual coordinates of the optimal solution satisfy 

**==> picture [205 x 13] intentionally omitted <==**

By differentiating it with respect to _c_ , the path satisfies 

**==> picture [333 x 51] intentionally omitted <==**

Let us trace the path _**θ**_[∗] _c_[starting from a sufficiently large] _[ c]_[, where] _**[ θ]**_[∗] _c_[=] _**[ θ]**_[∗][. As] _[ c]_ decreases, the path follows (13.156) as long as the active set _A_ _**θ**_[∗] _c_[does not change.] But at a point where some _θc_[∗] _[i]_[becomes][newly][0,][the][active][set] _[A]_[changes][and][the] 

13 Signal Processing and Optimization 

342 

direction _**θ**_ **[˙]** ∗ _c_[of the path changes discontinuously, because][ ∇] _[L]_[of (][13.154][) changes,] although the path itself is continuous. 

We divide the indices into two parts, one belonging to the active set _A_ and the other to its complement (inactive set) _A_[¯] , and use the mixed coordinates 

**==> picture [199 x 41] intentionally omitted <==**

Then, we have the following lemma. 

**Lemma 13.2** _The solution path satisfies_ 

**==> picture [224 x 14] intentionally omitted <==**

_while the active set does not change, where_ _**s**_ = ∇ _L (_ _**θ** c) is the vector of which the components are sgn θc_[∗] _[i][.]_ 

The following least equiangle theorem of Efron et al. (2004) holds even in our general case. 

**Theorem 13.4** (Least Equiangle Property) _The direction_ _**θ**_ **[˙]** ∗ _c[of the solution path has] the following properties:_ 

_(1) For any coordinate axis belonging to the active set A, the angle between_ _**θ**_ **[˙]** ∗ _λ and the coordinate axis is the same,_ 

**==> picture [236 x 20] intentionally omitted <==**

_where_ _**e** i is the tangent vector along the coordinate θ[i] ._ 

_(2) For any axis belonging to A, the angle between_[¯] _**θ**_ **[˙]** ∗ _λ[and the coordinate axis is] larger than that of the axis belonging to A,_ 

**==> picture [245 x 19] intentionally omitted <==**

∗ _Proof_ The angle between _**θ**_ **[˙]** _λ_[and][any][coordinate][axis] _**[e]**[i]_[is][calculated][by][the][inner] product, 

**==> picture [217 x 15] intentionally omitted <==**

Since _**η**_ **˙**[∗] _λ_[is proportional to][ ∇] _[L]_ � _**θ**_[∗] _λ_ �, whereas 

**==> picture [198 x 13] intentionally omitted <==**

for _i_ ∈ _A_ and 

**==> picture [187 x 10] intentionally omitted <==**

13.4 Sparse Signal Processing 

343 

∗ for _i_ ∈ _A_[¯] , (13.160) and (13.162) hold. The direction of _**θ**_ **[˙]** _λ_[changes][only][when] _[i]_ changes from _A_[¯] to _A_ . □ 

This is the principle of Least Angle Regressions (LARS) of Efron et al. (2004), extended to the general class of convex optimization. 

## _**13.4.4 Minkovskian Gradient Flow**_ 

A gradient flow is the set of paths satisfying 

**==> picture [199 x 13] intentionally omitted <==**

for some function _f (_ _**θ** )_ . A gradient flow converges to a minimum of _ψ_ when _ψ_ is bounded, and no oscillation occurs. We show that the solution path of the extended LARS is a gradient flow under the Minkovskian gradient, which is defined in the following (Amari and Yukawa 2013). The natural gradient of _f (_ _**θ** )_ is the direction _**a**_ in which the change of _f_ is the largest. We define it by 

**==> picture [234 x 18] intentionally omitted <==**

under the condition that the norm of _**a**_ is kept constant. The natural gradient uses the Riemannian norm. We consider the _L q_ -norm 

**==> picture [203 x 15] intentionally omitted <==**

which is a Minkovskian norm. The _L_ 2-norm is a special case of the Minkovskian norm. It is easy to see that the steepest direction is given by 

**==> picture [233 x 14] intentionally omitted <==**

where _c_ is a constant. 

Since we are dealing with the _L_ 1-constraint, we define the Minkovskian gradient with respect to the _L_ 1-norm by taking the limit of _q_ approaching to 1 from the above. We take the constant _c_ as 

**==> picture [208 x 32] intentionally omitted <==**

Then, the limit is 

**==> picture [314 x 25] intentionally omitted <==**

13 Signal Processing and Optimization 

344 

This is the Minkovskian gradient corresponding to the _L_ 1-norm. The Minkovskian gradient of _f_ is written as 

**==> picture [195 x 12] intentionally omitted <==**

Its components are ±1 when the absolute values of _∂i f_ are maximal and 0 for all the other components. See Amari and Yukawa (2013). Consider the Minkovskian gradient flow, 

**==> picture [218 x 13] intentionally omitted <==**

starting from the origin in terms of the dual coordinates. This is the solution path of our problem. The components of ∇[˜] _M ψ_ � _**θ**_[∗][�] are zero except for those indices that give the maximal values of �� _ηi_ ∗��, since _ηi_ ∗[is the derivative of] _[f][ (]_ _**[θ]**[)]_[ with respect to] _[ i]_[.] Hence, along the Minkovskian gradient flow, only the components _ηi_[∗][, which have the] largest absolute values change. We need to solve the equation in terms of the primal coordinate system _**θ**_[∗] _c_[. Any components of] _**[ θ]**_[∗] _c_[will change subject to the equiangle] property. 

We restate the LARS algorithm. Starting from the origin 0, we calculate the Minkovskian gradient of ∇[˜] _M ψ_ � _**θ**_[∗][�] and pick up the index _i_[∗] , 

**==> picture [204 x 19] intentionally omitted <==**

The active set consists of a single _i_[∗] . (We ignore cases where two or more indices become the maximizer, but it is easy to consider such cases.) The path _**η**_[∗] _c_[proceeds in] this direction of the Minkovskian gradient as _c_ increases, while �� _ηci_ ∗[∗] �� is the smallest. As _c_ becomes larger, another index _j_[∗] joins the set of the indices of the maximizer, satisfying 

**==> picture [196 x 14] intentionally omitted <==**

We then add this to the active set, and the Minkovskian gradient is calculated for the new active set. In this way, the active set increases stepwise, until the path converges to _**θ**_[∗] . The Minkovskian gradient flow explains the properties of LARS in terms of the geometry of the gradient flow. 

## _**13.4.5 Underdetermined Case**_ 

We have so far studied the overdetermined case, where the unique unconstrained optimum _**θ**_[∗] exists. In the underdetermined case of _m < n_ , _ψ(_ _**θ** )_ is not strictly convex and the solution of 

**==> picture [190 x 11] intentionally omitted <==**

345 

13.4 Sparse Signal Processing 

is not unique. The solutions form a submanifold. The problem is to obtain the one that has the minimum _L_ 1-norm. The Hessian **G** is not strictly positive-definite in this case. Hence, the Riemannian metric does not exists. The transformation (13.147) from _**θ**_ to _**η**_ exists but is not bijective and the inverse transformation is not necessarily unique. 

In spite of these differences, the Eq.(13.151) obtained from the Lagrangian holds. Hence, the equation of the solution path (13.156) holds as well. We can prove the least–angle theorem in a similar way. Therefore, the solution path is given by a Minkovskian gradient flow starting at the origin _**θ** c_ = 0. We can use the same algorithm for solving the problem in the underdetermined case. See Donoho and Tsaig (2008) in the regression case. 

## **13.5 Optimization in Convex Programming** 

Mathematical programming is a problem of finding the optimum solution under various constraints. A typical example is linear programming (LP), which minimizes a linear function under constraints given by linear inequalities. More generally, there is a problem of minimizing a linear loss function in a convex region. See Nesterov and Nemirovski (1993). This is called convex programming. A typical example of it is positive-semidefinite programming. An inner point method searches for the optimum solution sequentially inside the convex region. Since a convex region defines a dually flat structure, information geometry is useful in understanding these problems. 

## _**13.5.1 Convex Programming**_ 

Let us consider a manifold _M_ having a coordinate system _**θ**_ and a bounded convex region _Ω_ . A differentiable function _ψ(_ _**θ** )_ is called a barrier function when it is convex and diverges to infinity at the boundary _∂Ω_ of the region _Ω_ . Let 

**==> picture [215 x 22] intentionally omitted <==**

be the supporting hypersurface of _Ω_ at point _ω_ ∈ _∂Ω_ (Fig. 13.10). The convex region _Ω_ is defined by 

**==> picture [292 x 31] intentionally omitted <==**

Since 

**==> picture [223 x 19] intentionally omitted <==**

346 

13 Signal Processing and Optimization 

**Fig. 13.10** Convex region _Ω_ and supporting hyperplane at _**ω**_ 

**==> picture [11 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
ω<br>.<br>**----- End of picture text -----**<br>


diverges to infinity at the boundary, the convex function 

**==> picture [377 x 56] intentionally omitted <==**

**==> picture [240 x 14] intentionally omitted <==**

Hence, _Ω_ is a polyhedron and the convex function is 

**==> picture [241 x 24] intentionally omitted <==**

The cost function to be minimized is 

**==> picture [201 x 15] intentionally omitted <==**

The positive semi-definite programming is the problem of obtaining the positive **X** that minimizes the linear function 

**==> picture [200 x 10] intentionally omitted <==**

where **C** is a constant matrix. The set of all positive semi-definite matrices forms a cone. We impose the constraints which **X** must satisfy: 

**==> picture [240 x 10] intentionally omitted <==**

13.5 Optimization in Convex Programming 

347 

where **A** _κ_ are constant matrices. The region defined by (13.184) is convex. This type of problem is also called the cone programming problem, appearing in many fields of research, e.g., in control theory. See Ohara (1999). 

The barrier function for positive-definite matrices is given by 

**==> picture [211 x 10] intentionally omitted <==**

The geometrical structure is the same as the invariant geometry of Gaussian distributions with mean 0 and covariance matrix **X** . 

## _**13.5.2 Dually Flat Structure Derived from Barrier Function**_ 

Since a barrier function _ψ(_ _**θ** )_ is convex, it gives a dually flat structure to the manifold _M_ , where _**θ**_ is _e_ -affine coordinates and its Legendre transform 

**==> picture [191 x 10] intentionally omitted <==**

is _m_ 

The Riemannian metric **G** is given by 

**==> picture [205 x 11] intentionally omitted <==**

(Nesterov and Todd 2002). Hence, 

**==> picture [245 x 55] intentionally omitted <==**

in the case of (13.181). 

The interior point method is a sequential search for the solution that minimizes _C(_ _**θ** )_ , by changing _**θ**_ in the decreasing direction of _C_ inside _Ω_ . The natural gradient gives the steepest direction of _C_ and is given by 

**==> picture [219 x 12] intentionally omitted <==**

The LP problem uses a linear function 

**==> picture [193 x 10] intentionally omitted <==**

13 Signal Processing and Optimization 

348 

as a cost function. By using continuous time, the natural gradient flow is 

**==> picture [208 x 12] intentionally omitted <==**

where _ε_ is a constant. The affine-projection method of Karmarkar solves this by using the discrete time step, 

**==> picture [233 x 12] intentionally omitted <==**

It is known that this gives an algorithm of polynomial-time complexity. See Tanabe (1980). 

The dynamic equation (13.192) reduces to the simple equation given by 

**==> picture [191 x 11] intentionally omitted <==**

in the dual coordinates. The solution is a _m_ -geodesic, 

**==> picture [205 x 10] intentionally omitted <==**

Although the solution is very simple in the dual coordinates, we need the solution in the _**θ**_ coordinate system. Hence, the algorithm is not simple in the _**θ**_ coordinates and the transformation between _**θ**_ and _**η**_ is expensive. It is popular to solve the problem in the primal-dual formulation by using the Newton method. 

## _**13.5.3 Computational Complexity and m-curvature**_ 

In order to evaluate the number of steps to reach the optimal solution, we analyze the solution path. To this end, consider the following loss function parameterized by _t_ : 

**==> picture [218 x 10] intentionally omitted <==**

where the barrier function is added to the cost function. Let _**θ**_[∗] _(t)_ be the minimizer of _L(_ _**θ** , t)_ . This defines a path inside _Ω_ parameterized by _t_ , which cannot cross the boundary of _Ω_ . As _t_ →∞, the effect of the barrier function disappears, so _**θ**_[∗] _(t)_ converges to the optimum solution _**θ**_[∗] of the original problem. 

By differentiating (13.196) with respect to _**θ**_ , we obtain the solution path in the dual coordinates, 

**==> picture [194 x 11] intentionally omitted <==**

We call the point _**η**_[∗] _(_ 0 _)_ = 0 the center of _Ω_ . The solution path is a dual geodesic connecting the center and the optimum solution _**η**_[∗] . This is the steepest descent path starting at the center by using the natural gradient. 

13.5 Optimization in Convex Programming 

349 

The path is an _m_ -geodesic but is curved in the _e_ -coordinates _**θ**_ . When the curvature of the path is small, we can solve the discretized path equation by taking a large step size, but when the curvature is large, we need to use a small step size. Therefore, the number of steps depends on the curvature of the path. Kakihara, Ohara and Tsuchiya (2012) evaluated the necessary number of steps to obtain the optimum solution within a preassigned accuracy in terms of the embedding curvature of the path. 

## **13.6 Dual Geometry Derived from Game Theory** 

## _**13.6.1 Minimization of Game-Score**_ 

Statistical inference can be regarded as a game against Nature, where the player estimates the probability distribution Nature has assigned. Nature shows a realized value of random variable _x_ subject to the true probability distribution _p(x)_ . The player chooses an action _a_ from the set _A_ of actions. Let _l(x, a)_ be the instantaneous loss when _a_ is chosen for _x_ . The expected loss is 

**==> picture [251 x 23] intentionally omitted <==**

See Topsoe (1979), Grünwald and Dawid (2004), Dawid (2007) and Dawid et al. (2012) for a detailed formulation. 

In the case of estimation, the player’s action is to choose a probability distribution _q(x)_ from a set of actions consisting of probability distributions, _A_ = { _q(x)_ }. We call the loss _l(x, q)_ a game-score in the case of probability distributions and denote it by _S(x, q)_ , 

**==> picture [203 x 10] intentionally omitted <==**

When _N_ independentobservations _x_ 1 _, . . . , x N_ areavailable,thegame-scoreiswritten as 

**==> picture [289 x 30] intentionally omitted <==**

where _p_ ˆ _(x)_ is the empirical distribution 

**==> picture [219 x 30] intentionally omitted <==**

The conventional loss used in statistics is the log loss, so the corresponding gamescore is 

**==> picture [211 x 10] intentionally omitted <==**

350 

13 Signal Processing and Optimization 

Minimization of the game-score (13.200) under log loss (13.202) gives the maximum likelihood estimator. We study another type of the game-score in the next subsection, called the Hyvärinen score (Hyvärinen 2005) given by 

**==> picture [224 x 22] intentionally omitted <==**

where 

**==> picture [204 x 10] intentionally omitted <==**

and _l_[˙] etc. are differentiations with respect to _x_ . 

For two probability distributions _p(x)_ and _q(x)_ , let us define the game-relativeentropy by 

**==> picture [224 x 11] intentionally omitted <==**

The game-entropy of _p(x)_ is given by _HS_ [ _p_ : _p_ ]. When the game-score is given by (13.202), it is the Shannon entropy. A game-score is proper when 

**==> picture [213 x 10] intentionally omitted <==**

holds for any _p_ and _q_ . It is strictly proper when the equality holds only for _q_ = _p_ . We study a strictly proper game-score. In this case, we define the game-divergence between _p(x)_ and _q(x)_ by 

**==> picture [244 x 10] intentionally omitted <==**

This is the KL-divergence when the game-score is given by (13.202). We can derive a dual geometrical structure { _g,_ ∇ _,_ ∇[∗] } induced from the game-divergence (Dawid 2007) for any strictly positive game-score _S(x, q)_ . We call it the _S_ -geometry, which includes the invariant geometry as a special case of log loss. 

Let us consider a parametric form of statistical model _M_ = { _p(x,_ _**ξ** )_ }, where _x_ is a scalar or a vector. We show only a scalar case, but it is easy to generalize results to the vector case. For a strictly proper game-score 

**==> picture [218 x 10] intentionally omitted <==**

the divergence is written as a function of _**ξ**_ and _**ξ**_[′] as 

_DS_ � _**ξ**_ : _**ξ**_[′][�] = _DS_ � _p(x,_ _**ξ** )_ : _p_ � _x,_ _**ξ**_[′][��] = _E p(x,_ _**ξ** )_ � _S(x,_ _**ξ**_[′] _)_ − _S (x,_ _**ξ** )_ � _._ (13.209) Hence, from 

**==> picture [216 x 24] intentionally omitted <==**

351 

13.6 Dual Geometry Derived from Game Theory 

we have 

**==> picture [218 x 25] intentionally omitted <==**

This shows that 

**==> picture [210 x 24] intentionally omitted <==**

is an estimating function derived from game-score _S_ . The estimating equation is 

**==> picture [207 x 30] intentionally omitted <==**

This is equivalent to minimizing _p_ ˆ _(x)_ . _DS_ � _p_ ˆ _(x)_ : _p(x,_ _**ξ** )_ � for the empirical distribution 

We show that there are strict proper game-scores other than _l(x,_ _**ξ** )_ = − log _p(x,_ _**ξ** )_ . One type is derived from a Bregman divergence _Dψ_ [ _p(x)_ : _q(x)_ ] given by 

**==> picture [323 x 23] intentionally omitted <==**

where _ψ(q)_ is a strictly convex function. It is easy to see that this is a Bregman divergence, and the related game-score is 

**==> picture [305 x 23] intentionally omitted <==**

It reduces to the log score when 

**==> picture [202 x 10] intentionally omitted <==**

The estimating function in this case is 

**==> picture [249 x 11] intentionally omitted <==**

where 

**==> picture [239 x 13] intentionally omitted <==**

Since _Dψ_ is a Bregman divergence, a dually flat structure is introduced in the manifold _M_ = { _p(x)_ }. As is seen from (13.214), the convex function is _ψ(q)_ , where the _θ_ -coordinates of _q_ ∈ _M_ are of function degrees of freedom, 

**==> picture [196 x 10] intentionally omitted <==**

352 

13 Signal Processing and Optimization 

and the _η_ -coordinates are 

**==> picture [206 x 11] intentionally omitted <==**

The Riemannian metric and cubic tensor are derived from _ψ_ . 

The estimator _**ξ**_[ˆ] derived from a game-score is consistent, because _**s** (x,_ _**ξ** )_ is an estimating function. We study its efficiency. Let _**ξ**_ be the true value and let us put 

**==> picture [193 x 13] intentionally omitted <==**

where _**ξ**_[ˆ] is the estimator satisfying the estimating equation, 

**==> picture [209 x 22] intentionally omitted <==**

By the Taylor expansion, we have 

**==> picture [326 x 25] intentionally omitted <==**

Due to the central limit theorem, 1 _/_ √ _N_ of the first term of (13.223) converges to a Gaussian random variable _**ε**_ , the mean of which is 0 and the covariance is 

**==> picture [241 x 13] intentionally omitted <==**

The coefficient of the second term converges, due to the law of large numbers, to 

**==> picture [213 x 13] intentionally omitted <==**

Therefore, the estimation error is 

**==> picture [207 x 24] intentionally omitted <==**

The asymptotic error covariance of _**ξ**_[ˆ] is 

**==> picture [226 x 21] intentionally omitted <==**

which is larger than the inverse _**G**_[−][1] of the Fisher information matrix in general. 

The loss of information or efficiency is analyzed as follows. Let us decompose random variable _**s** (x,_ _**ξ** )_ in the direction of the score vector _∂_ _**ξ** l(x,_ _**ξ** )_ , which consists of random variables representing the tangent vectors along the coordinate curves _**ξ**_ , and orthogonal to it, 

353 

13.6 Dual Geometry Derived from Game Theory 

**==> picture [241 x 29] intentionally omitted <==**

We may put _c(_ _**ξ** )_ = 1, since the estimating equation is the same for any _c(_ _**ξ** )_ . Then, we have 

**==> picture [241 x 26] intentionally omitted <==**

because 

**==> picture [255 x 13] intentionally omitted <==**

and 

**==> picture [204 x 12] intentionally omitted <==**

The term _**a**_ is explicitly given by 

**==> picture [303 x 13] intentionally omitted <==**

Hence, we have 

**==> picture [227 x 13] intentionally omitted <==**

and 

**==> picture [227 x 13] intentionally omitted <==**

where 

**==> picture [219 x 13] intentionally omitted <==**

Therefore, the asymptotic error covariance increases by **GAG**[−][1] . The estimator is Fisher efficient when and only when _**a** (x,_ _**ξ** )_ = 0. 

## _**13.6.2 Hyvärinen Score**_ 

Hyvärinen (2005, 2007) proposed an interesting game-score given by 

**==> picture [224 x 22] intentionally omitted <==**

where _l(x)_ = log _q(x)_ and ˙ denotes the differentiation with respect to _x_ . When _**x**_ is a vector, it is 

**==> picture [241 x 22] intentionally omitted <==**

354 

13 Signal Processing and Optimization 

where _Δ_ is the Laplacian and ∇ is the gradient with respect to _**x**_ . The related gameentropy is 

**==> picture [237 x 24] intentionally omitted <==**

and the divergence is 

**==> picture [313 x 73] intentionally omitted <==**

**Lemma 13.3** _The Hyvärinen divergence is rewritten as_ 

_Proof_ We calculate E _p_ [ _S(x, q)_ ] by putting 

**==> picture [242 x 10] intentionally omitted <==**

Then 

**==> picture [278 x 78] intentionally omitted <==**

where the formula of partial integration is used. E _p_ [ _S(x, p)_ ] is calculated similarly, and we have (13.241). 

The Hyvärinen divergence is not a Bregman divergence and hence the geometry derived from it is not dually flat. Note that it does not depend on the normalizing constant of _q_ , because 

**==> picture [237 x 9] intentionally omitted <==**

for any _c_ . Hence, it can be used for estimation when the normalization factor is 

For parametric family of probability distributions _p(_ _**x** ,_ _**ξ** )_ , the Hyvärinen estimating function is given by 

**==> picture [299 x 13] intentionally omitted <==**

It is a homogeneous estimating function, because it does not depend on the normalization factor _c(_ _**ξ** )_ of a probability distribution. For example, an exponential family 

355 

13.6 Dual Geometry Derived from Game Theory 

is written as 

**==> picture [243 x 10] intentionally omitted <==**

but _l_[˙] and _l_[¨] do not include _ψ(_ _**θ** )_ . Hence, one can easily obtain an estimator without calculating _ψ(_ _**θ** )_ . Calculation of the normalization factor _ψ_ is computationally heavy in Bayesian inference, so the Hyvärinen score is useful in such a case. 

We give a simple illustrative example. 

_Example 13.1_ Consider a simple exponential family, 

**==> picture [261 x 13] intentionally omitted <==**

We can calculate _ψ_ in this case as 

**==> picture [207 x 22] intentionally omitted <==**

Therefore, the _η_ -coordinate is 

**==> picture [185 x 22] intentionally omitted <==**

The MLE is given by 

**==> picture [197 x 25] intentionally omitted <==**

The Hyvärinen score is 

**==> picture [214 x 11] intentionally omitted <==**

Hence, the related estimator is 

**==> picture [194 x 25] intentionally omitted <==**

which is asymptotically unbiased but is not efficient, because the score _s(x, θ)_ is not included in the space of 

**==> picture [224 x 12] intentionally omitted <==**

The following theorem shows the case when the Hyvärinen estimator is Fisher efficient. See Hyvärinen (2005). 

**Theorem 13.5** _The Hyvärinen estimator is Fisher efficient for multivariate Gaussian distributions and is not efficient for other distributions._ 

_Proof_ Both _**s** (_ _**x** ,_ _**ξ** )_ and _∂_ _**ξ** l(_ _**x** ,_ _**ξ** )_ are quadratic functions of _**x**_ in the multi-variate Gaussian case, _∂_ _**ξ** l(_ _**x** ,_ _**ξ** )_ spanning all the quadratic functions of _**x**_ . Hence, _**s** (_ _**x** ,_ _**ξ** )_ is included in the space spanned by _∂_ _**ξ** l(_ _**x** ,_ _**ξ** )_ and _**a** (_ _**x** ,_ _**ξ** )_ = 0. On the other hand, this occurs only for multivariate Gaussian distributions. □ 

356 

13 Signal Processing and Optimization 

Parry et al. (2012) and Hyvärinen (2007) extend the Hyvärinen score applicable to the case of discrete _**x**_ such as a graphical model. We show another new idea. 

Consider the case where _**x**_ is a discrete random variable having a graphical structure. When _**x**_[′] and _**x**_ are connected by a branch, _**x**_[′] is a neighbor of _**x**_ , _**x**_[′] ∈ _N_ _**x**_ , where _N_ _**x**_ is the set of neighbors of _**x**_ . A typical example is a Boltzmann machine, where _**x**_[′] is a neighbor of _**x**_ when one and only one component of _**x**_[′] is different from _**x**_ . Hence, the graph is represented by an _n_ -cube. 

The graph Laplacian _Δ_ is an operator, acting on function _f (_ _**x** )_ as 

**==> picture [245 x 28] intentionally omitted <==**

where | _N_ _**x**_ | is the cardinality of _N_ _**x**_ . It can be rewritten as 

**==> picture [229 x 22] intentionally omitted <==**

where 

**==> picture [229 x 37] intentionally omitted <==**

An interesting property is shown in the following lemma. 

## **Lemma** 

_where_ 

**==> picture [238 x 67] intentionally omitted <==**

_When the graph is homogeneous, having constant_ | _N_ _**x**_ | _,_ 

**==> picture [184 x 10] intentionally omitted <==**

_Proof_ From 

**==> picture [255 x 23] intentionally omitted <==**

(13.257) follows immediately. 

357 

13.6 Dual Geometry Derived from Game Theory 

We define a new game score when _**x**_ is discrete and the graph is homogenous, that is, _Δ_ = _Δ_[′] , by 

**==> picture [248 x 27] intentionally omitted <==**

This does not depend on the normalization factor of _p(_ _**x** )_ . The estimating function _**s** (_ _**x** ,_ _**ξ** )_ is defined in the parametric case as 

**==> picture [223 x 11] intentionally omitted <==**

This gives the estimating equation 

**==> picture [200 x 15] intentionally omitted <==**

not depending on the normalization factor. 

The meaning of this score is given by the following theorem. 

**Theorem 13.6** _The divergence derived from the score (13.261) is_ 

**==> picture [283 x 37] intentionally omitted <==**

_Proof_ We calculate _E_ _**ξ**_ � _S_ � _**x** , p_ � _**x** ,_ _**ξ**_[′][���] as before. However we use 

**==> picture [276 x 65] intentionally omitted <==**

instead of the formula of partial integration used in the continuous case. We then have the theorem. 

We can calculate the efficiency of the derived estimator by calculating _**a** (_ _**x** ,_ _**ξ** )_ . 

## **Remarks** 

The last chapter deals with miscellaneous subjects concerning signal processing. PCA is an old subject but is still active. We have focused on the dynamics of learning for PCA from the point of view of geometry. ICA is a relatively newly developed subject, in which non-Gaussianity of distributions plays an important role. Information geometry elucidates its structure. The natural gradient in the manifold of matrices is useful for this purpose. Moreover, it is formulated as a semi-parametric 

358 

13 Signal Processing and Optimization 

statistical problem, so that a general form of estimating functions is given by information geometry. We can stabilize and accelerate its learning dynamics by using the Newton method in the manifold of matrices. We have further touched upon the NMF problem. 

Sparse signal processing is a hot topic on which many researchers are working. We are not able to overview most of the excellent results in this field. Instead, we have touched upon the minimization problem from the information geometry point of view. The Minkovskian gradient is a new topic, reinterpreting the _L_ 1-constrained minimization. The problem of minimization under _L p(_ 0 _< p <_ 1 _)_ is another interesting subject. See Xu et al. (2012), Yukawa and Amari (2015) and Jeong et al. (2015), for example. 

Convex programming is a big field in operations research. We discussed only the interior point method, in which information geometry plays an interesting role. Another important topic related to optimization is the stochastic relaxation framework which is useful even for discrete optimization (Malagò et al. 2013), touched upon in the previous chapter. We also touched upon an information geometry framework given by game theory (Dawid 2007). The Hyvärinen score _S(_ _**x** , p)_ when _**x**_ is discrete is a new idea emerged at the last stage in preparing the monograph. The dual geometry derived from the Hyvärinen score is an interesting subject in future research. 

## **Correction to: Information Geometry and Its Applications** 

## **Correction to:** 

**S. Amari,** _**Information Geometry and Its Applications**_ **, Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8** 

In the original version of the book, the following belated corrections have been incorporated. The correction book has been updated with changes. 

## **Corrections:** 

Page 15, line 4 from bottom: (2.12) has been updated to (1.52) Page 17, line 3 from bottom: (1.57) has been updated to (1.60) Page 21, Fig. 1.6: _ηi_ and _η j_ has been updated to _θi_[∗][and] _[ θ]_[∗] _j_[, respectively] Page 24, Eq. (1.112) has been updated to 

**==> picture [162 x 10] intentionally omitted <==**

Page 25, Eq. (1.114) has been updated to 

**==> picture [252 x 12] intentionally omitted <==**

The updated version of these chapters can be found at https://doi.org/10.1007/978-4-431-55978-8_1 https://doi.org/10.1007/978-4-431-55978-8_2 https://doi.org/10.1007/978-4-431-55978-8_4 https://doi.org/10.1007/978-4-431-55978-8_9 https://doi.org/10.1007/978-4-431-55978-8_11 https://doi.org/10.1007/978-4-431-55978-8_13 https://doi.org/10.1007/978-4-431-55978-8 

© Springer Japan 2020 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, https://doi.org/10.1007/978-4-431-55978-8_14 

C1 

Correction to: Information Geometry and Its Applications 

C2 

Page 25, Eq. (1.120) has been updated to 

**==> picture [171 x 11] intentionally omitted <==**

Page 33, line after (2.16): Insert This implies that the KL-divergence is the dual of the canonical divergence derived from _ψ_ . Page 97, Eq. (4.150): 2 _π_ has been updated to _(_ 2 _π)[n]_ Page 203, line 6 from top: (9.64) has been updated to (9.63) Page 240, line 11 from top: Asmptotic has been updated to Asymptotic Page 240, Eq. (11.46): _n_ has been updated to _N_ Page 247, line 6 from top: Delete because of (11.69) Page 330, line 4 from bottom: expected converge has been updated to expected to converge 

## **References** 

- D. Ackley, G. E. Hinton and J. Sejnowski, A learning algorithm for Boltzmann machines. Cognitive Science, 9, 147–169, 1985. 

- A. Agarwal and H. Daumé III, A geometric view of conjugate priors. Machine Learning, 81, 99–113, 2010. 

- M. Aizerman, E. Braverman and L. Rozonoer, Theoretical foundations of the potential function method in pattern recognition learning. Automation and Remote Control, 25, 821–837, 1964. 

- M. Akahira and K. Takeuchi, Asymptotic Efficiency of Statistical Estimators: Concepts and Higher Order Asymptotic Efficiency, Springer LN in Statistics, vol. 7, 1981. 

- S.AkahoandK.Takabatake,Informationgeometryofcontrastivedivergence.InInformationTheory and Statistical Learning, 3–9, 2008. 

- M. S. Ali and S. D. Silvey, A general class of coefficients of divergence of one distribution from another. Journal of Royal Statistical Society, B, 28, 131–142, 1966. 

- S. Amari, On some primary structures of non-Riemannian plasticity theory. RAAG Memoirs, 3, D-IX, 99–108, 1962. 

- S. Amari, A geometrical theory of moving dislocations. RAAG Memoirs, 4, D-XVII, 153–161, 1968. 

- S. Amari, Theory of adaptive pattern classifiers. IEEE Transactions on Electronic Computers, 16, 299–307, 1967. 

- S. Amari, Neural theory of association and concept-formation. Biological Cybernetics, 26, 175–185, 1977. 

- S. Amari, Differential geometry of curved exponential families—curvature and information loss. Annals of Statistics, 10, 357–385, 1982. 

- S. Amari, Finsler geometry of non-regular statistical models. RIMS Kokyuroku (in Japanese), NonRegular Statistical Estimation, Ed. M. Akahira, 538, 81–95, 1984. 

- S. Amari, Differential-Geometrical Methods in Statistics. Lecture Notes in Statistics, 28, Springer, 1985. 

- S. Amari, Differential geometry of a parametric family of invertible linear systems—Riemannian metric, dual affine connections and divergence. Mathematical Systems Theory, 20, 53–82, 1987. 

- S.Amari,InformationgeometryoftheEMandemalgorithmsforneuralnetworks.NeuralNetworks, 8, 1379–1408, 1995. 

- S. Amari, Natural gradient works efficiently in learning. Neural Computation, 10, 251–276, 1998. 

- S. Amari, Superefficiency in blind source separation. IEEE Transactions on Signal Processing, 47, 936–944, 1999. 

- S.Amari,Estimatingfunctionsofindependentcomponentanalysisfortemporallycorrelatedsignals. Neural Computation, 12, 2083–2107, 2000. 

359 

© Springer Japan 2016 S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8 

360 

References 

- S. Amari, Information geometry on hierarchy of probability distributions. IEEE Transactions on Information Theory, 47, 1701–1711, 2001. 

- S. Amari, Integration of stochastic models by minimizing _α_ -divergence. Neural Computation, 19, 2780–2796, 2007. 

- S. Amari, _α_ -divergence is unique, belonging to both _f_ -divergence and Bregman divergence classes. IEEE Transactions on Information Theory, 55, 11, 4925–4931, 2009. 

- S. Amari, Information geometry of positive measures and positive-definite matrices: Decomposable dually flat structure. Entropy, 16, 2131–2145, 2014. 

- S. Amari and J. Armstrong, Curvature of Hessian manifolds, Differential Geometry and its Applications 33, 1–12, 2014. 

- S. Amari and J-F. Cardoso, Blind source separation—Semiparametric statistical approach. IEEE Transactions on Signal Processing, 45, 2692–2700, 1997. 

- S. Amari, A. Cichocki and H. Yang, A new learning algorithm for blind signal separation. In Advances in Neural Information Processing Systems (Eds. M. Mozer et al.), 8, 757–763, 1996. 

- S. Amari and M. Kawanabe, Information geometry of estimating functions in semi-parametric statistical models. Bernoulli, 3, 29–54, 1997. 

- S. Amari, S. Ikeda and H. Shimokawa, Information geometry of _α_ -projection in mean field approximation. In M. Opper and D. Saad (Eds), Advanced Mean Field Methods: Theory and Practice, 241–257. MIT Press, 2001. 

- S. Amari, K. Kurata and H. Nagaoka, Information geometry of Boltzmann machines. IEEE Transactions on Neural Networks, 3, 260–271, 1992. 

- S. Amari and H. Nagaoka, Methods of Information Geometry. American Mathematical Society and Oxford University Press, 2000. 

- S. Amari, H. Nakahara, S. Wu and Y. Sakai, Synchronous firing and higher-order interactions in neuron pool. Neural Computation, 15, 127–142, 2003. 

- S. Amari and A. Ohara, Geometry of _q_ -exponential family of probability distributions. Entropy, 13, 1170–1185, 2011. 

- S. Amari, A. Ohara and H. Matsuzoe, Geometry of deformed exponential families: Invariant, dually flat and conformal geometry. Physica A, 391, 4308–4319, 2012. 

- S. Amari, H. Park and K. Fukumizu, Adaptive method of realizing natural gradient learning for multilayer perceptrons. Neural Computation, 12, 1399–1409, 2000. 

- S. Amari, H. Park and T. Ozeki, Singularities affect dynamics of learning in neuromanifolds. Neural Computation, 18, 1007–1065, 2006. 

- S. Amari and S. Wu, Improving support vector machine classifiers by modifying kernel functions. Neural Networks, 12, 783-789, 1999. 

- S. Amari and M. Yukawa, Minkovskian gradient for sparse optimization. IEEE Journal of Selected Topics in Signal Processing, 7, 576–585, 2013. 

- D. Arthur and S. Vassilvitskii, _k_ -means++: The advantages of careful seeding, Proceedings of the 18th Annual ACM-SIAM Symposium on Discrete Algorithms, 1027–1035, 2007. 

- K. Arwini and C. T. J. Dodson, Information Geometry. Springer, 2008. 

- N. Ay, An information-geometric approach to a theory of pragmatic structuring. Annals of Probability, 30, 416–436, 2002. 

- N. Ay, Information geometry on complexity and stochastic interaction. Entropy, 17, 2432–2458, 2015. 

- N. Ay, J. Jost, H. V. Lê and L. Schwachhöfer, Information Geometry and Sufficient Statistics. arXiv:1207.6736, 2013. 

- N. Ay and S. Amari, A novel approach to canonical divergences within information geometry. Entropy, 17, 8111–8129, 2015. 

- N. Ay and A. Knauf, Maximizing multi-information. Kybernetika, 42, 517–538, 2006. 

- N. Ay, E. Olbrich, N. Bertschinger and. J. Jost, A geometric approach to complexity. Chaos, 21, 037103, 2011. 

- D. Balduzzi and G. Tononi, Integrated information in discrete dynamical systems: Motivation and theoretical framework. PLos Computational Biology, 4, e1000091, 2008. 

361 

References 

- A. Banerjee, S. Merugu, I. Dhillon and J. Ghosh, Clustering with Bregman divergences. Journal of Machine Learning Research, 6, 1705–1749, 2005. 

- N. Barkai, H. S. Seung, and H. Sompolinsky. On-line learning of dichotomies. Advances in Neural Information Processing Systems, 7, 303–310, 1995. 

- O. E. Barndorff-Nielsen, Information and Exponential Families in Statistical Theory. Wiley, 1978. 

- A. B. Barrett and A. K. Seth, Practical measures of integrated information for time-series data. PLoS Computational Biology, 7, e1001052, 2011. 

- M. Basseville, Divergence measures for statistical data processing—An annotated bibliography. Signal Processing, 93, 621–633, 2013. 

- A. Beck and M. Teboulle, Mirror descent and nonlinear projected subgradient methods for convex optimization. Operations Research Letters, 31, 167–175, 2003. 

- J. M. Begun, W. J. Hall, W. M. Huang and J. A. Wellner, Information and asymptotic efficiency in parametric-nonparametric models. Annals of Statistics, 11, 432-452, 1983. 

- A. J. Bell and T. Sejnowski, An information maximization approach to blind separation and blind deconvolution. Neural Computation, 7, 1129–1159, 1995. 

- P. J. Bickel, C. A. J. Ritov, and J. A. Wellner, Efficient and Adaptive Estimation for Semiparametric Models. Johns Hopkins University Press, 1994. 

- J.-D. Boissonnat, F. Nielsen and R. Nock, Bregman Voronoi diagrams. Discrete and Computational Geometry, 44, 281–307, 2010. 

- L. Bregman, The relaxation method of finding a common point of convex sets and its applications to the solution of problems in convex programming. USSR Computational Mathematics and Mathematical Physics, 7, 200–217, 1967. 

- R. Brockett, Some geometric questions in the theory of linear systems. IEEE Transactions on Automatic Control, 21, 449–455, 1976. 

- R. Brockett, Dynamical systems that sort lists, diagonalize matrices, and solve linear programming problems. Linear Algebra and its Applications, 146, 79–91, 1991. 

- A. Bruckstein, D. Donoho and M. Elad, From sparse solutions of systems of equations to sparse modeling of signals and images. SIAM Review, 51, 34–81, 2009. 

- J. Burbea and C. R. Rao, On the convexity of some divergence measures based on entropy functions. IEEE Transactions on Information Theory, 28, 489–495, 1982. 

- W. Byrne, Alternating minimization and Boltzmann machine learning. IEEE Transactions on Neural Networks, 3, 612–620, 1992. 

- O. Calin and C. Udriste, Geometric Modeling in Probability and Statistics. Springer, 2013. 

- L. L. Campbell, An extended Chentsov characterization of a Riemannian metric. Proceedings of American Mathematical Society, 98, 135–141, 1986. 

- E. J. Candes, J. Romberg and T. Tao, Stable signal recovery from incomplete and inaccurate measurements. Communications on Pure and Applied Mathematics 59, 1207–1223, 2006. 

- E. J. Candes and M. B. Walkin, An introduction to compressive sampling. IEEE Signal Processing Magazine, 25, 21–30, 2008. 

- J.-F. Cardoso and B. H. Laheld, Equivariant adaptive source separation. IEEE Transactions on Signal Processing, 44, 3017–3030, 1996. 

- J.-F. Cardoso and A. Souloumiac, Jacobi angles for simultaneous diagonalization. SIAM Journal on Mathematical Analysis and Applications, 17, 161–164, 1996. 

- A. Cena and G. Pistone, Exponential statistical manifold. Annals of Institute of Statistical Mathematics, 59, 27–56, 2007. 

- T. Chen and S. Amari, Unified stabilization approach to principal and minor components extraction algorithms. Neural Networks, 14, 1377–1387, 2001. 

- T. P. Chen, S. Amari and Q. Lin, A unified algorithm for principal and minor components extraction. Neural Networks, 11, 3, 385–390, 1998. 

- S. S. Chen, D. L. Donoho and M. A. Saunders, Atomic decomposition by basis pursuit. SIAM Journal on Scientific Computation, 20, 33–61, 1998. 

- N. N. Chentsov, Statistical Decision Rules and Optimal Inference, AMS, 1982 (originally published in Russian, Nauka, 1972). 

362 

References 

- H. Chernoff, A measure of asymptotic efficiency for tests of a hypothesis based on a sum of observations. Annals of Mathematical Statistics, 23, 493–507, 1952. 

- H. Choi, S. Choi, A. Katake and Y. Choe, Parameter learning for _α_ -integration. Neural Computation, 25, 1585–1604, 2013. 

- J. Choi and A. P. Mullhaupt, Kahlerian information geometry for signal processing. Entropy, 17, 1581–1605, 2015. 

- A. Cichocki and S. Amari, Adaptive Blind Signal and Image Processing. John Wiley, 2002. 

- A. Cichocki and S. Amari, Families of _α_ -, _β_ - and _γ_ -divergences: flexible and robust measures of similarities. Entropy, 12, 1532–1568, 2010. 

- A. Cichocki, S. Cruces and S. Amari, Generalized _α_ - _β_ divergences and their application to robust nonnegative matrix factorization. Entropy, 13, 134–170, 2011. 

- A. Cichocki, S. Cruces and S. Amari, Log-determinant divergences revisited: _α_ - _β_ and _γ_ log-det divergences. Entropy, 17, 2988–3034, 2015. 

- A. Cichocki, R. Zdunek, A. H. Phan and S. Amari, Nonnegative Matrix and Tensor Factorizations. John Wiley and Sons, UK, 2009. 

- C. Cortes and V. Vapnik, Support-vector networks. Machine Learning, 20, 273–297, 1995. 

- F. Cousseau, T. Ozeki and S. Amari, Dynamics of learning in multilayer perceptrons near singularities. IEEE Transactions on Neural Networks, 19, 1313–1328, 2008. 

- F. Critchley, P. K. Marriott and M. Salmon, Preferred point geometry and statistical manifolds. Annals of Statistics, 21, 1197–1224, 1993. 

- I. Csiszár, Information-type measures of difference of probability distributions and indirect observation. Studia Scientiarum Mathematicarum Hungarica, 2, 229–318, 1967. 

- I. Csiszár, Information measures: A critical survey. in Proceedings of 7th Conference on Information Theory, Prague, Czech Republic, 83–86, 1974. 

- I. Csiszár, Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems. Annals of Statistics, 19, 2032–2066, 1991. 

- I. Csiszár and G. Tusnady, Information geometry and alternating minimization procedure. In E. F. Dedewicz, et. al. (Eds.), Statistics and Decision, 205–237, Oldenburg Verlag, 1984. 

- Y. Dauphin, R. Pascanu, C. Gulcehre, K. Cho, S. Ganguli and Y. Bengio, Identifying and attacking the saddle point problem in high-dimensional non-convex optimization. arXiv:1406.2572, NIPS, 2014. 

- A. P. Dawid, The geometry of proper scoring rules. Annals of Institute of Statistical Mathematics, 59, 77–93, 2007. 

- A. P. Dawid, S. Lauritzen and M. Parry, Proper local scoring rules on discrete sample spaces. Annals of Statistics, 40, 593–608, 2012. 

- A. P. Dempster, N. M. Laird and D. B. Rubin, Maximum likelihood from incomplete data via the EM algorithm. Journal Royal Statistical Society, B, 39, 1–38, 1977. 

- S. Dhillon and J. A. Tropp, Matrix nearness problems with Bregman divergences. SIAM Journal on Matrix Analysis and Applications, 29, 1120–1146, 2007. 

- D. L. Donoho, Compressed sensing. IEEE Transactions on Information Theory, 52, 1289–1306, 2006. 

- D. L. Donoho and Y. Tsaig, Fast solution of _L_ 1-norm minimization problems when the solution may be sparse. IEEE Transaction on Information Theory, 54, 4789–4812, 2008. 

- A. Edelman, A. A. Arias and S. T. Smith, The geometry of algorithms with orthogonality constraints. SIAM Journal on Matrix Analysis and Applications, 20, 303–353, 1998. 

- B. Efron, Defining the curvature of a statistical problem (with application to second order efficiency). Annals of Statistics, 3, 1189–1242, 1975. 

- B. Efron, T. Hastie, I. Johnstone and R. Tibshirani, Least angle regression. Annals of Statistics, 32, 407–499, 2004. 

- S. Eguchi, Second order efficiency of minimum contrast estimators in a curved exponential family. Annals of Statistics, 11, 793–803, 1983. 

- S. Eguchi, O. Komori and A. Ohara, Duality of maximum entropy and minimum divergence. Entropy, 16, 3552–3572, 2014. 

363 

References 

- M. Elad, Sparse and Redundant Representations: From Theory to Applications in Signal and Image Processing. Springer, 2010. 

- Y. Eldar and G. Kutyniok, Compressed Sensing. Cambridge University Press, 2012. 

- Y. Freund and R. E. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting. Journal Computer and Systems Sciences, 55, 119–139, 1997. 

- H. Fujisawa and S. Eguchi, Robust parameter estimation with a small bias against heavy contamination. Journal Multivariate Analysis, 99, 2053–2081, 2008. 

- A. Fujiwara and S. Shuto, Hereditary structure in Hamiltonians: Information geometry of Ising spin chains. Physics Letters A, 374, 911–914, 2010. 

- K. Fukumizu, Likelihood ratio of unidentifiable models and multilayer neural networks. Annals of Statistics, 31, 833–851, 2003. 

- K. Fukumizu, Exponential manifold by reproducing kernel Hilbert spaces. In Algebraic and Geometric Methods in Statistics (P. Gibilisco, E. Riccomagno, M.-P. Rogantin and H. Winn Eds.), 291–306, Cambridge University Press, 2009. 

- K. Fukumizu and S. Kuriki, Statistics of Singular Models. Frontiers in Statistical Sciences, 7, Iwanami, 2004 (in Japanese). 

- S. Furuichi, An axiomatic characterization of a two-parameter extended relative entropy. Journal of Mathematical Physics, 51, 2010. 

- P. Gibilisco and G. Pistone, Connections on non-parametric statistical manifolds by Orlicz space geometry: infinite-dimensional analysis. Quantum Probabilities and Related Topics, 1, 325–347, 1998. 

- M. Girolami and B. Calderhead, Riemannian manifold Langevin and Hamiltonian Monte Carlo methods. Journal of Royal Statistical Society, B-73, 123–214, 2011. 

- V. P. Godambe, Estimating Functions. Oxford University Press, 1991. 

- M. Grasselli, Dual connections in nonparametric classical information geometry. Annals of Institute of Statistical Mathematics, 62, 873–896, 2010. 

- I. Grondman, L. Bu¸soniu, G.A.D. Lopes and R. Babuška, A survey of actor-critic reinforcement learning: Standard and natural policy gradients. IEEE Transactions on Systems, Man, and Cybernetics–Part C: Applications and Reviews, 42, 1291–1307, 2012. 

- P. D. Grünwald and A. P. Dawid, Game theory, maximum entropy, minimum discrepancy and robust Bayesian decision theory. Annals of Statistics, 32, 1367–1433, 2004. 

- N. Hansen and A Ostermeier, Completely derandomized self-adaptation in evolution strategies. Evolutionary Computation, 9, 159–195, 2001. 

- G. H. Hardy, J. E. Littlewood and G. Polya, Inequalities (2nd ed.). Cambridge: Cambridge University Press, 1952. 

- K. V. Harsha and K. S. S. Moosath, _F_ -geometry and Amari’s _α_ -geometry on a statistical manifold. Entropy, 16, 2472–2487, 2014. 

- M. Hayashi and S. Watanabe, Information geometry approach to parameter estimation in Markov chains. IEEE Transactions on Information Theory, 2014. 

- M. Henmi and R. Kobayashi, Hooke’s law in statistical manifolds and divergence. Journal Nagoya Mathematical, 159, 1–24, 2000. 

- G. E. Hinton, Training products of experts by minimizing contrastive divergence. Neural Computation, 14, 1771–1800, 2002. 

- G. E. Hinton and E. R. Salakhutdinov, Reducing the dimensionality of data with neural networks. Science, 313, 504–507, 2006. 

- Y. Hirose and F. Komaki, An extension of least angle regression based on the information geometry of dually flat spaces. Journal of Computational and Graphical Statistics, 19, 1007–1023, 2010. 

- S. W. Ho and R. W. Yeung, On the discontinuity of the Shannon information measures. IEEE Transactions on Information Theory, 55, 5362–5374, 2009. 

- A. Honkela, T. Raiko, M. Kuusela, M. Tornio and J. Karhunen, Approximate Riemannian conjugate gradient learning for fixed-form variational Bayes. Journal of Machine Learning Research, 11, 3235–3268, 2010. 

364 

References 

- A. Hyvärinen, Estimation of non-normalized statistical models by score matching. Journal of Machine Learning Research, 6, 695–709, 2005. 

- A. Hyvärinen, Some extensions of score matching. Computational Statistics & Data Analysis, 51:2499–2512, 2007. 

- A. Hyvärinen, J. Karhunen and E. Oja, Independent Component Analysis. John Wiley, 2001. 

- T. Ichimori, On rounding off quotas to the nearest integers in the problem of apportionment methods. JSIAM Letters, 3, 21–24, 2011. 

- S. Ikeda, T. Tanaka and S. Amari, Stochastic reasoning, free energy, and information geometry. Neural Computation, 16, 1779–1810, 2004a. 

- S. Ikeda, T. Tanaka and S. Amari, Information geometry of turbo and low-density parity-check codes. IEEE Transactions on Information Theory, 50, 1097–1114, 2004b. 

- M. Ishikawa, Structural learning with forgetting. Neural Networks, 9, 509–521, 1996. 

- R. A. Jacobs, M. I. Jordan, S. J. Nolwan and G. E. Hinton, Adaptive mixtures of local experts. Neural Computation, 3, 79–87, 1991. 

- A. T. James, The variance information manifold and the function on it. Multivariate Statistical Analysis, Ed. P. K. Krishnaiah, Academic Press, 157–169, 1973. 

- H. Jeffreys, Theory of Probability, 1st ed. Clarendon Press, 1939. 

- H. Jeffreys, An invariant form for the prior probability in estimation problems. Proceedings of Royal Society of London, Series A, Mathematical and Physical Sciences, 186, 453–461, 1946. 

- H. Jeffreys, Theory of Probability, 2nd ed. Oxford University Press, 1948. 

- K. Jeong, M. Yukawa and S. Amari, Can critical-point paths under _lp_ -regularization (0⟨ _p_ ⟨1) reach the sparsest least square solutions?. IEEE Transactions on Information Theory, 60, 2960–2968, 2014. 

- J. Jiao, T. M. Courtade, A. No, K. Venkat and T. Weissman, Information measure: The curious case of the binary alphabet. IEEE Transactions on Information Theory, 60, 7616–7626, 2015. 

- S.Kakade,Anaturalpolicygradient.InAdvancesinNeuralInformationProcessing,14,1531–1538, 2001. 

- S. Kakihara, A. Ohara and T. Tsuchiya, Information geometry and interior-point algorithms in semidefinite programs and symmetric cone programs. Journal of Optimization Theory and Applications, DOI 10.1007/s10957-012-0189-9, 2012. 

- T. Kanamori, T. Takenouchi, S. Eguchi and N. Murata, Robust loss function for boosting. Neural Computation, 19, 2183–2244, 2007. 

- K. Kanatani, Statistical optimization and geometric inference in computer vision. Philosophical Transactions of Royal Society of London, Ser. A, 356, 1303–1320, 1998. 

- Y. Kano, Beyond third-order efficiency. Sankhya, 59, 179–197, 1997. 

- Y. Kano, More higher order efficiency. Journal of Multivariate Analysis. 67, 349–366, 1998. 

- R. Karakida, M. Okada and S. Amari, Analyzing feature extraction by contrastive divergence learning in RBM. NIPS Workshop on Deep Learning, 2014. 

- R. Karakida, M. Okada and S. Amari, Dynamical analysis of contrastive divergence learning. Restricted Boltzmann machines with Gaussian visible units, To appear, 2016. 

- R. E. Kass and P. Vos, Geometrical Foundations of Asymptotic Inference. Wiley, 1997. 

- A. Kim, J. Park S. Park and S. Kang, Impedance learning for robotic contact tasks using natural actor-critic algorithm. IEEE Transactions on Systems, Man and Machine, B39, 433–443, 2010. 

- J. Kivinen and M. K. Warmuth, Exponentiated gradient versus gradient descent for linear predictors. Information and Computation, 132, 1–63, 1997. 

- G. Kniadakis and A. Scarfone, A new one parameter deformation of the exponential function. Physica A, 305, 69–75, 2002. 

- K. Kumon and S. Amari, Geometrical theory of higher-order asymptotics of test, interval estimator and conditional inference. Proceedings of Royal Society of London, A 387, 429–458, 1983. 

- M. Kumon, A. Takemura and K. Takeuchi, Conformal geometry of statistical manifold with application to sequential estimation. Sequential Analysis, 30, 308–337, 2011. 

- T. Kurose, Dual connections and affine geometry. Mathematische Zeitschrift, 203, 115–121, 1990. 

365 

References 

- T. Kurose, On the divergence of 1-conformally flat statistical manifolds. Tohoku Mathematical Journal, 46, 427–433, 1994. 

- T. Kurose, Conformal-projective geometry of statistical manifolds. Interdisciplinary Information Sciences, 8, 89–100, 2002. 

- S. Lauritzen, Graphical Models. Oxford University Press, 1996. 

- H. V. Lê, Statistical manifolds are statistical models. Journal of Geometry, 84, 83–93, 2005. 

- G. Lebanon and J. Lafferty, Boosting and maximum likelihood for exponential models. In Advances in Neural Information Processing Systems (NIPS), 14, 2001. 

- D. D. Lee and S. Seung, Algorithms for nonnegative matrix factorization. Nature, 401, 788–791, 1999. 

- C. Lin and J. Jiang, Supervised optimizing kernel locality preserving projection with its application to face recognition and palm biometrics. Submitted, 2015. 

- M. Liu, B. C. Vemuri, S. Amari and F. Nielsen, Shape retrieval using hierarchical total Bregman soft clustering. IEEE Transactions on Pattern Analysis and Machine Learning, 34, 2407–2419, 2012. 

- L. Malagò, M. Matteucci and G. Pistone, Natural gradient, fitness modelling and model selection: A unifying perspective. IEEE Congress on Evolutionary Computation, 486–493, 2013. 

- L. Malagò and G. Pistone, Combinatorial optimization with information geometry: Newton method. Entropy 16, 4260–4289, 2014. 

- P. Marriott, On the local geometry of mixture models. Biometrika, 89, 77–93, 2002. 

- P. Marriott and M. Salmon, Applications of Differential Geometry to Econometrics. Academic Press, 2011. 

- J. Martens, New perspectives on the natural gradient method. arXiv:1412.1193, 2015. 

- J. Martens and R. Grosse, Optimizing neural networks with Kronecker-factored approximate curvature. arXiv:1503.05671, 2015. 

- R. J. Martin, A metric for ARMA processes. IEEE Transactions on Signal Processing, 48, 1164– 1170, 2000. 

- T. Matumoto, Any statistical manifold has a contrast function—On the C3-functions taking the minimum at the diagonal of the product manifold. Hiroshima Mathematical Journal, 23, 327– 332, 1993. 

- Y. Matsuyama, The _α_ -EM algorithm: Surrogate likelihood maximization using _α_ -logarithmic information measures. IEEE Transactions on Information Theory, 49, 692–706, 2003. 

- H. Matsuzoe, On realization of conformally-projectively flat statistical manifolds. Hokkaido Mathematical Journal, 27, 409–421, 1998. 

- H. Matsuzoe, Geometry of contrast functions and conformal geometry. Hokkaido Mathematical Journal, 29, 175–191, 1999. 

- H. Matsuzoe, J. Takeuchi and S. Amari, Equiaffine structures on statistical manifolds and Bayesian statistics. Differential Geometry and Its Applications, 24, 567–578, 2006. 

- J. Milnor, On the concept of attractor. Communications of Mathematical Physics, 99, 177–195, 1985. 

- M. Minami and S. Eguchi, Robust blind source separation by _β_ -divergence. Neural Computation, 14, 1859–1886, 2004. 

- K. Miura, M. Okada and S. Amari, Estimating spiking irregularities under changing environments. Neural Computation, 18, 2359–2386, 2006. 

- T. Morimoto, Markov processes and the _H_ -theorem. Journal of Physical Society of Japan, 12, 328–331, 1963. 

- T. Morimura, E. Uchibe, J. Yoshimoto and K. Doya, A generalized natural actor-critic algorithm. In Advances in Neural Information Processing Systems, 22, MIT Press, 1312–1320, 2009. 

- R. Morioka and K. Tsuda, Information geometry of input-output table. Technical Report IEICE, 110, 161–168, 2011 (in Japanese). 

- N. Murata, T. Takenouchi, T. Kanamori and S. Eguchi, Information geometry of _U_ -boost and Bregman divergence. Neural Computation, 16, 1432–1481, 2004. 

- M. K. Murray and J. W. Rice, Differential Geometry and Statistics. Chapman Hall, 1993. 

366 

References 

- H. Nagaoka and S. Amari, Differential geometry of smooth families of probability distributions. Technical Report METR 82–7, University of Tokyo, 1982. 

- H. Nakahara and S. Amari, Information-geometric measure for neural spikes. Neural Computation, 14, 2269–2316, 2002. 

- H. Nakahara, S. Amari and B. Richmond, A comparison of descriptive models of a single spike train by information-geometric measure. Neural Computation, 18, 545–568, 2006. 

- J. Naudts, Generalized Thermostatistics. Springer, 2011. 

- A. Nemirovski and D. Yudin, Problem Complexity and Method Efficiency in Optimization, Wiley, 1983. 

- Y. Nesterov and A. Nemirovski, Interior Point Polynomial Methods in Convex Programming: Theory and Algorithms. SIAM Publications, 1993. 

- Y. Nesterov and M. Todd, On the Riemannian geometry defined by self-concordant barriers and interior-point methods. Foundations of Computational Mathematics, 2, 333–361, 2002. 

- N. J. Newton, An infinite-dimensional statistical manifold modeled on Hilbert space. Journal of Functional Analysis, 263, 1661–1681, 2012. 

- J. Neyman and E. L. Scott, Consistent estimates based on partially consistent observation. Econometrica, 16, 1–32, 1948. 

- F. Nielsen and R. Nock, On the _χ_ -square and higher-order _χ_ -distances for approximating _f_ - divergences. IEEE Signal Processing Letters, 21, 10–13, 2014. 

- R. Nock and F. Nielsen, Bregman divergences and surrogates for learning. IEEE Transactions on Pattern Analysis and Machine Intelligence, 31, 2048–2059, 2009. 

- R. Nock, F. Nielsen and S. Amari, On conformal divergences and their population minimizers. IEEE Transactions on Information Theory, accepted, 2015. 

- K. Nomizu and T. Sasaki, Affine Differential Geometry. Oxford University Press, 1994. 

- A. Ohara, Information geometric analysis of an interior point method for semidefinite programming. In O. Barndorff-Nielsen and E. Jensen Eds, Geometry in Present Day Science, World Scientific, 49–74, 1999. 

- A. Ohara, Geometry of distributions associated with Tsallis statistics and properties of relative entropy minimization. Physics Letters, A, 370, 184–193, 2007. 

- A. Ohara and S. Amari, Differential geometric structures of stable state feedback systems with dual connections. Kybernetika, 30, 369–386, 1994. 

- A. Ohara and S. Eguchi, Group invariance of information geometry on _q_ -Gaussian distributions induced by beta-divergence. Entropy, 15, 4732–4747, 2013. 

- A. Ohara, H. Matsuzoe and S. Amari, Conformal geometry of escort probability and its applications. Modern Physics Letters B, 26, 10, 1250063, 2012. 

- M. Oizumi, L. Albantakis and G. Tononi, From phenomenology to the mechanism of consciousness: Integrated information theory 3.0. PLoS Computational Biology, 10, e1003588, 2014. 

- M. Oizumi, S. Amari, T. Yanagawa, N. Fujii and N. Tsuchiya, Measuring integrated information from the decoding perspective. arXiv:1505.04368 [q-bio.NC], To appear in PLoS Computational Biology, 2015. 

- M. Oizumi, M. Okada and S. Amari, Information loss associated with imperfect observation and mismatched decoding. Frontiers in Computational Neuroscience, 5, 1–13, 2011. 

- M. Oizumi, N. Tsuchiya and S. Amari, A unified framework for information integration based on information geometry. Submitted, 2016. 

- E. Oja, A simplified neuron model as a principal component analyzer. Journal of Mathematical Biology, 15, 267–273, 1982. 

- E. Oja, Principal components, minor components, and linear neural networks. Neural Networks, 5, 927–935, 1992. 

- I. Okamoto, S. Amari and K. Takeuchi, Asymptotic theory of sequential estimation: Differentialgeometrical approach. Annals of Statistics, 19, 961–981, 1991. 

- T. Okatani and K. Deguchi, Easy calibration of a multi-projector display system. International Journal of Computer Vision, 2009. 

367 

References 

- Y. Ollivier, Riemannian metric for neural networks I: Feedforward networks. Information and Inference, 4, 108-153, 2015, DOI 10.1093/imaiai/iav006. 

- H. Park, S. Amari and K. Fukumizu, Adaptive natural gradient learning algorithms for various stochastic models. Neural Networks, 13, 755–764, 2000. 

- M. Parry, A. P. Dawid and S. Lauritzen, Proper local scoring rule. Annals of Statistics, 40, 561–592, 2012. 

- J. Pearl, Probabilistic Reasoning in Intelligent Systems. Morgan Kaufmann, 1988. 

- J. Peters and S. Schaal, Natural actor-critic. Neurocomputing, 71, 1180–1190, 2008. 

- G. Pistone, Examples of the application of nonparametric information geometry to statistical physics. Entropy, 15, 4042–4065, 2013. 

- G. Pistone and M. P. Rogantin, The exponential statistical manifold: mean parameters, orthogonality and space transformations. Bernoulli, 5, 721–760, 1999. 

- G. Pistone and C. Sempi, An infinite-dimensional geometric structure on the space of all the probability measures equivalent to a given one. Annals of Statistics, 23, 1543–1561, 1995. 

- C. R. Rao, Information and accuracy attainable in the estimation of statistical parameters. Bulletin of the Calcutta Mathematical Society, 37, 81–91, 1945. 

- C. R. Rao, Efficient estimates and optimum inference procedures in large samples. Journal of Royal Statistical Society, B, 24, 46–72, 1962. 

- G. Raskutti and S. Mukherjee, The information geometry of mirror descent. IEEE Transactions on Information Theory, 61, 1451–1457, 2015. 

- J. Rauh, Finding the maximizers of the information divergence from an exponential family. IEEE Transactions on Information Theory, 57, 3236–3247, 2011. 

- N. Ravishanker, E. L. Melnik and C. Tsai, Differential geometry of ARMA models. Journal of Time Series Analysis, 11, 259–274, 1990. 

- A. Rényi, On measures of entropy and information, in Proc. 4th Symposium on Mathematical Statistics and Probability Theory, Berkeley, CA, 1, 547–561, 1961. 

- F. Rosenblatt, Principles of Neurodynamics. Spartan, 1962. 

- N. L. Roux, P.-A. Manzagol and Y. Bengio, Topmoumoute online natural gradient algorithm. In Advances in Neural Information Processing Systems, 17, 849–856, 2007. 

- D. E. Rumelhart, G. E. Hinton and R. J. Williams, Learning representations by back-propagating errors. Nature, 323, 533–536, 1986. 

- R. E. Schapire, Y. Freend, P. Bartlett and W. S. Lee, Boosting the margin: A new explanation for the effectiveness of voting methods. Annals of Statistics, 26, 1651–1686, 1998. 

- J. Schmidhuber, Deep Learning in Neural Networks: An Overview. Neural Networks, 61, 85–117, 2015. 

- B. Scholkopf, Support Vector Learning. Oldenbourg, 1997. 

- J. A. Schouten, Ricci Calculus. Springer, 1954. 

- J. Shawe-Taylor and N. Cristianini, Kernel Methods for Pattern Analysis. Cambridge University Press, 2004. 

- H. Shima, The Geometry of Hessian Structures. World Scientific, 2007. 

- S. Shinomoto, K. Shima and J. Tanji, Differences in spiking patterns among cortical neurons. Neural Computation, 15, 2823–2842, 2003. 

- P. Smolensky, Information processing in dynamical systems: Foundations of harmony theory, In D. E. Rumelhart and J. L. McLelland (Eds.), Parallel Distributed Processing, 1, 194–281, MIT Press, 1986. 

- A. Soriano and L. Vergara, Fusion of scores in a detection context based on alpha integration. Neural Computation, 27, 1983–2010, 2015. 

- S. M. Stigler, The epic story of maximum likelihood. Statistical Science, 22, 598–620, 2007. 

- T. Takenouchi and S. Eguchi, Robustifying AdaBoost by adding the naive error rate. Neural Computation 16, 767–787, 2004. 

- T. Takenouchi, S. Eguchi, N. Murata and T. Kanamori, Robust boosting algorithm against mislabeling in multiclass problems. Neural Computation, 20, 1596–1630, 2008. 

368 

References 

- J. Takeuchi, Geometry of Markov chains, finite state machines and tree models. Technical Report of IEICE, 2014. 

- J. Takeuchi, T. Kawabata and A. Barron, Properties of Jeffreys mixture for Markov sources. IEEE Transactions on Information Theory, 41, 643–652, 2013. 

- K. Tanabe, Geometric method in nonlinear programming. Journal of Optimization Theory and Applications, 30, 181–210, 1980. 

- T. Tanaka, Information geometry of mean field approximation. Neural Computation, 12, 1951–1968, 2000. 

- M. Taniguchi, Higher-Order Asymptotic Theory for Time Series Analysis. Springer Lecture Notes in Statistics, 68, 1991. 

- P. S. Thomas, W. Dabney, S. Mahadeven and S. Giguere, Projected natural actor-critic. In Advances in Neural Information Processing Systems, 26, 2013. 

- R. Tibshirani, Regression shrinkage and selection via the LASSO. Journal of Royal Statistical Society, Series B, 58, 267–288, 1996. 

- G. Tononi, Consciousness as integrated information: a provisional manifest. Biological Bulletin, 215, 216–242, 2008. 

- F. Topsoe, Information-theoretical optimization techniques. Kybernetika, 15, 8–27, 1979. 

- C. Tsallis, Possible generalization of Boltzmann-Gibbs statistics. Journal of Statistical Physics, 52, 479–487, 1988. 

- C. Tsallis, Introduction to Nonextensive Statistical Mechanics: Approaching a Complex World, Springer, 2009. 

- K. Uohashi, _α_ -conformal equivalence of statistical submanifolds. Journal of Geometry, 75, 179– 184, 2002. 

- V. N. Vapnik, Statistical Learning Theory. John Wiley, 1998. 

- B. C. Vemuri, M. Liu, S. Amari and F. Nielsen, Total Bregman divergence and its applications to DTI analysis. IEEE Transactions on Medical Imaging, 30, 475–483, 2011. 

- R. F. Vigelis, and C. C. Cavalcante, On _φ_ -families of probability distributions. Journal of Theoretical Probabilities, 26, 870–884, 2013. 

- P. Vos, A geometric approach to detecting influential cases. Annals of Statistics, 19, 1570–1581, 1991. 

- J. Wada, A divisor apportionment method based on the Kolm-Atkinson social welfare function and generalized entropy. Mathematical Social Sciences, 63, 243–247, 2012. 

- M. J. Wainwright and M. I. Jordan, Graphical models, exponential families, and variational inference. Foundations and Trends in Machine Learning, 1, 1–305, 2008. 

- S. Watanabe, Algebraic geometrical methods for hierarchical learning machines. Neural Networks, 14, 1409–1060, 2001. 

- S. Watanabe, Algebraic Geometry and Statistical Learning Theory. Cambridge University Press, 2009. 

- S. Watanabe, Asymptotic equivalence of Bayes cross validation and widely applicable information criterion in singular statistical learning theory. Journal of Machine Learning Research, 11, 3571– 3591, 2010. 

- H. Wei and S. Amari, Dynamics of learning near singularities in radial basis function networks. Neural Networks, 21, 989–1005, 2008. 

- H. Wei, J. Zhang, F. Cousseau, T. Ozeki and S. Amari, Dynamics of learning near singularities in layered networks. Neural Computation, 20, 813–843, 2008. 

- P. Williams, S. Wu and J. Feng, Two scaling methods to improve performance of the support vector machine. In Support Vector Machines: Theory and Applications, Ed. L. Wang, 205–218, Springer, 2005. 

- D. Wu, Parameter estimation for _α_ -GMM based on maximum likelihood criterion. Neural Computation, 21, 1776–1795, 2009. 

- S. Wu and S. Amari, Conformal transformation of kernel functions: A data-dependent way to improve support vector machine classifiers. Neural Processing Letters, 15, 59–67, 2002. 

369 

References 

- S. Wu, S. Amari and H. Nakahara, Population coding and decoding in a neural field: A computational study. Neural Computation, 14, 999–1026, 2002. 

- L. Xu, Least mean square error reconstruction principle for self-organizing neural nets. Neural Networks, 6, 627–648, 1993. 

- Z. Xu, X. Chang, F. Xu and H. Zhang, _L_ 1 _/_ 2 regularization: A thresholding representation theory and a fast solver. IEEE Transactions on Neural Networks and Learning Systems, 23, 1013–1027, 2012. 

- S. Yi, D. Wierstra, T. Schaul and J. Schmidhuber, Stochastic search using the natural gradient. ICML Proceedings of the 26th Annual Internatinal Conference on Machine Learning, 1161–1168, 2009. 

- J. S. Yedidia, W. T. Freeman and Y. Weiss, Generalized belief propagation. In T. K. Leen, T. G. Dietrich and V. Tresp (Eds.), Advances in Neural Information Processing Systems, 13, 689–695, MIT Press, 2001. 

- A. Yuille, CCCP algorithms to minimize the Bethe and Kikuchi free energies: Convergent alternatives to belief propagation. Neural Computation, 14, 1691–1722, 2002. 

- A. L. Yuille and A. Rangarajan, The concave-convex procedure. Neural Computation, 15, 915–936, 2003. 

- M. Yukawa and S. Amari, _l p_ -regularized least squares (0 < _p_ < 1) and critical path. IEEE Transactions on Information Theory, 62, 1–15, 2016. 

- J. Zhang, Divergence function, duality and convex analysis. Neural Computation, 16, 159–195, 2004. 

- J. Zhang, From divergence function to information geometry: Metric, equiaffine and symplectic structures. Geometry Symposium, Japan Mathematical Society, Proceedings, 47–62, 2011. 

- J. Zhang, Nonparametric information geometry: From divergence function to referentialrepresentational biduality on statistical manifolds. Entropy, 15, 5384–5418, 2013. 

- J. Zhang, On monotone embedding in information geometry. Entropy, 17, 4485–4499, 2015. 

- J. Zhao, H. Wei, C. Zhang, W. Li, W. Guo and K. Zhang, Natural gradient learning algorithms for RBF networks. Neural Computation, 27, 481–505, 2015. 

- H. Y. Zhu and R. Rohwer, Bayesian invariant measurements of generalization. Neural Processing Letters, 2, 28–31, 1995. 

## **Index** 

## **Symbols** 

_(α_ - _β)_ -divergence, 100 _(α, β)_ -divergence, 94 ( _α_ - _β_ )-log-det divergence, 101 _α_ -divergence, 58, 67, 72 _α_ -expert machine, 84 _α_ -family of probability distributions, 81 _α_ -function, 57 _α_ -geodesic, 75 _α_ -geometry, 136 _α_ -integration, 82 _α_ -mean, 77 _α_ -projection theorem, 76 _α_ -Pythagorean theorem, 76 _β_ -divergence, 95 _χ_ -divergence, 91 _χ_ -escort distribution, 91 _χ_ -exponential family, 90 _e_ -affine parameter, 38 _e_ -condition, 257 _e_ -flat, 38 _e_ -geodesic, 38 _e_ -parallel transport, 202 _em_ algorithm, 28 _(F, G, H )_ -structure, 104 _f_ -divergence, 54 _γ_ -divergence, 102 _k_ -cut, 144 _k_ -means, 234 _k_ -sparse, 336 _κ_ -exponential family, 89 _L_ 0-norm, 338 _L_ 1-norm, 338 _m_ -affine parameter, 38 _m_ -condition, 257 _m_ -flat, 38 _m_ -geodesic, 38 

_m_ -parallel transport, 202 _m_ -projection, 46, 252 _φ_ -center of cluster, 233 _�_ -function method, 245 _q_ -divergence, 85 

_q_ -entropy, 85 

_q_ -escort geometry, 92 _q_ -exponential, 85 _q_ -exponential family, 86, 89 

_q_ -free energy, 87 _q_ -logarithm, 85 _q_ -metric, 88 _(ρ, τ)_ -structure, 104 _U_ -divergence, 95 _(u, v)_ -divergence, 92 _(u, v)_ -structure, 99 

**A** Absolute-value-based Hessian natural gradient, 286 Active set, 340 Adaptive learning method, 294 Adaptive natural gradient learning, 293 Affine connection, 112 Affine coordinate system, 18 Affine flat structure, 19 Akaike information criterion, 312 Alternating minimization algorithm, 27 Amari–Chentsov structure, 134 Amari–Chentsov tensor, 134 Ancillary submanifold, 169 Ancillary tangent subspace, 201 ARMA model, 218 AR model, 217 Asymptotic theory of hypothesis testing, 175 Auto-correlation coefficients, 221 

© Springer Japan 2016 

S. Amari, _Information Geometry and Its Applications_ , Applied Mathematical Sciences 194, DOI 10.1007/978-4-431-55978-8 

371 

Index 

372 

Auto-regression model, 217 

## **B** 

Back-propagation learning, 281 Barrier function, 345 Basis vectors, 20 Bayesian duality, 266 Bayesian posterior distribution, 266 Belief propagation, 249 Blow-down technique, 309 Boltzmann machine, 181, 268 Boosting, 261 Bregman divergence, 13 

## **C** 

Canonical divergence, 138 Canonical parameter, 32 Central limit theorem, 60 Chernoff divergence, 242 Chernoff information, 242 Clique, 250 Clustering, 231 Clustering algorithm, 234 Coarse graining, 53 Cocktail party problem, 323 Coefficient of proportionality, 191 Coefficients of affine connection, 113 Conformal transformation, 91 Conformal transformation of a kernel, 249 Conjugate priors, 267 Consistent estimator, 168 Contrastive divergence, 273 Convex-concave computational procedure, 249 Convex function, 12 Convex programming, 345 Coordinate system, 4 Coordinate transformation, 4 Covariant derivative, 117 Cramér–Rao bound, 166 Cramér–Rao theorem, 166 Critical region, 300 Critical slowdown, 305 Cubic tensor, 115 Cumulant generating function, 32 

## **D** 

Decomposable divergence, 55 Deep learning, 292, 296 Deformed exponential family, 89 Divergence, 9 

Dual affine structure, 19 Dual connections, 131 Dual convex function, 17 Dual geodesic, 19 Dually flat manifold, 137 

## **E** 

Efficient, 173 Efficient score, 194 Einstein summation convention, 20 Eliminating singularity, 299 EM algorithm, 179 Embedding curvature, 129, 349 Ergodic time series, 215 Error covariance matrix, 166 Escort probability distribution, 88 Estimating function, 197 Estimator, 165 Euler–Schouten curvature, 129 Exponential family, 31 

## **F** 

First-order asymptotic theory, 173 Fisher information matrix, 33 Foliation, 145 Free energy, 32 

## **G** 

Game, 349 Game-divergence, 350 Game-score, 349 Gaussian kernel, 247 Gaussian mixture model, 180 Gaussian RBM, 275 Generalization error, 280 Generalized inverse, 337 Generalized Pythagorean theorem, 24 Geodesic, 19, 117 Graph Laplacian, 356 Graphical model, 250 

## **H** 

Hidden variable, 179 Higher-order asymptotic theory of estimation, 173 Higher-order correlations, 149 Higher-order cumulants, 326 Hyvärinen divergence, 354 Hyvärinen score, 353 

Index 

373 

## **I** 

Independent component analysis, 322 Information integration, 150 Information monotonicity, 52 Inner product, 23 Input–output analysis, 157 Instantaneous loss, 280 Integrated information, 152 Integration of weak machines, 261 Invariance criterion, 51 Invariant divergences, 52 Invariant Riemannian metrics, 52 

## **K** 

Kernel exponential family, 42 Kernel function, 246 Killing metric, 329 KL-divergence, 71, 220 Kronecker-factored approximate curvature, 293 Kullback–Leibler (KL) divergence, 11 

Mixed coordinate system, 144 Mixture family, 37 Moving-average model, 218 Multilayer perceptron, 292, 296 

## **N** 

Natural gradient, 283 Natural gradient learning method, 284 Natural parameter, 32 Natural policy gradient, 288 Negative entropy, 33 Neyman–Scott problem, 191 Non-holonomic coordinate system, 329 Non-negative matrix factorization, 333 Nuisance parameter, 191 Nuisance tangent subspace, 201 

## **O** 

Observed point, 47 Observed submanifold, 180 On-line learning, 281 Overlapping singularity, 299 

## **L** 

Large deviation, 60 Large deviation theorem, 61 Learning constant, 294 Least angle regressions, 343 Least equiangle theorem, 342 Legendre transformation, 16 Levi–Civita connection, 113, 125 Linear machine, 242 Linear system, 215 Loss of information by data reduction, 185 

## **M** 

Machine learning, 231 MA model, 218 Manifold, 3 Margin, 243 Maximum entropy, 223 Maximum entropy principle, 45 Maximum likelihood estimator, 48 Mean field approximation, 254 Metric affine connection, 125 Milnor attractor, 310 Minimum description length, 312 Minimum entropy, 224 Minkovskian gradient, 343 Minor subspace, 317 Mirror descent method, 289 Misspecified model, 186 

## **P** 

Parallel transport, 22, 118 Parameter of interest, 191 Plateau, 302 Plateau phenomena, 308 Policy natural gradient, 284 Polynomial kernel, 247 Positive-definite symmetric matrix, 96 Power spectrum, 217 Principal component, 317 Principal component analysis, 315 Principal subspace, 317 Prior distribution, 266 Projection theorem, 25, 143 

## **R** 

RAS transformation, 160 RC curvature, 119 Reinforcement learning, 287 Restricted Boltzmann machine, 268 Riemann–Christoffel curvature tensor, 119 Riemannian connection, 113 Riemannian geometry, 109 Riemannian gradient, 283 Riemannian metric, 19 Riemannian structure, 10 Robust cluster center, 238 

Index 

374 

## **S** 

Saddle-free Newton method, 286 Scale problem, 191 Score function, 111 Semi-definite programming, 346 Shape parameter, 212 Singular point, 301 Singular prior, 313 Singular statistical models, 311 Singular structure, 296 Soft clustering, 236 Solution path, 341 Sparse vector, 336 Standard estimating function, 332 Standard _f_ -divergence, 56 Stiefel manifold, 320 Stochastic descent learning method, 281 Stochastic relaxation, 286 Submanifold, 126 Sufficient statistic, 52 Super efficiency, 332 Support vector, 244 

Support vector machine, 242 System complexity, 152 

## **T** 

Tangent space, 19, 109 Tangent subspace of interest, 201 Temporal firing pattern, 211 Tensor, 114 Time series, 215 Total Bregman divergence, 238 Total least squares, 196 Training error, 280 Transfer function, 217 

## **U** 

Unidentifiability, 298 

## **V** 

Voronoi diagram, 234 

