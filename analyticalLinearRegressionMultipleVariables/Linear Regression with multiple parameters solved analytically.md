# Linear Regression with Multiple Parameters Solved Analytically

Let's say we want to find the line with following equation:

<div style="text-align:center"><img src ="equationOfLine.png" /></div>

We have m samples in our training set (ie we know m `y`s for real-world `x` values) so the training data takes the following form where ![](theta0.png) to ![](thetaN.png) are unknown:  

<div style="text-align:center"><img src ="trainingDataEquations.png" /></div>

Let's define the following matrices: 

<div style="text-align:center"><img src ="yMatrixEquals.png" /></div>

<div style="text-align:center"><img src ="xMatrixEquals.png" /></div>

<div style="text-align:center"><img src ="thetaMatrixEquals.png" /></div>

Then we can define our problem with the following matrix equation: 

<div style="text-align:center"><img src ="matrixEquation.png" /></div>

To solve for ![](thetaHat.png):

<div style="text-align:center"><img src ="proof.png" /></div>


Code: 



```scala
  type Matrix = IndexedSeq[IndexedSeq[Double]]

  def solve(x: Matrix, y: Matrix): Matrix = {
    val xT = x.transpose
    val yT = y.transpose
    ((xT dot x).inverse dot xT) dot y
  }
```

Auxillary methods are [here](https://github.com/polyglotpiglet/catistics/blob/master/src/main/scala/com/ojha/core/MatrixUtil.scala) on my github. 