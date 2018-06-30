# **Monad Transformers**

**The problem**

This code does not compile:

```scala
    def fo1: Future[Option[Int]] = Future.successful(Some(2))
    def fo2: Future[Option[Int]] = Future.successful(Some(5))

    for {
        i <- fo1
        j <- fo2
    } yield i * j
```
because 'value * is not a member of Option[Int]'


**The solution using a monad transformer in scalaz**

We can change `Future[Option[_]]` into `OptionT[Future, _]`

```scala
    for {
        i <- OptionT(fo1)
        j <- OptionT(fo2)
    } yield i * j
```

**Future[Int]**

Let's add another method:

```scala
    def fo3: Future[Int] = Future.successful(3))
```

Now we can use the lift method to use this is our for loop.

```scala
  for {
    i <- OptionT(fo1)
    j <- OptionT(fo2)
    k <- fo3.liftM[OptionT]
  } yield i * j * k
```


**Option[Int]**

And finally:

```scala
 def fo4: Option[Int] = Some(4)

  for {
    i <- OptionT(fo1)
    j <- OptionT(fo2)
    k <- fo3.liftM[OptionT]
    l <- OptionT(fo4.pure[Future])
  } yield i * j * k * l
```

**A final beautiful example**

```scala

  def liftFutureOption[T](fo: Future[Option[T]]): OptionT[Future, T] = OptionT(fo)
  def liftFuture[T](f: Future[T]): OptionT[Future, T] = f.liftM[OptionT]
  def liftOption[T](o: Option[T]): OptionT[Future, T] = OptionT(o.pure[Future])
  def lift[T](t: T): OptionT[Future, T] = liftOption(Option(t))

  for {
    i <- fo1 |> liftFutureOption
    j <- fo2 |> liftFutureOption
    k <- fo3 |> liftFuture
    l <- fo4 |> liftOption
    m <- 5   |> lift
  } yield i * j * k * l * m
```

**Notes**

build.sbt

```scala
    scalacOptions in ThisBuild ++= Seq(
      "-language:_",
      "-Ypartial-unification",
      "-Xfatal-warnings"
    )
    libraryDependencies ++= Seq(
      "com.github.mpilquist" %% "simulacrum" % "0.12.0",
      "org.scalaz" %% "scalaz-core" % "7.2.22"
    )
    addCompilerPlugin("org.spire-math" %% "kind-projector" % "0.9.6")
    addCompilerPlugin("org.scalamacros" % "paradise" % "2.1.1" cross CrossVersion.full)
```

Imports:
```scala
    import scalaz._, Scalaz._
```
