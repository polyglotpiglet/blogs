# Scala Keywords

**Sealed Abstract Class**

Use sealed when defining coproducts like the following, because if we try and do a partial match the compiler can warn us about it: 

```scala
  sealed abstract class CatList[T]
  case object CatNil extends CatList
  case class CatCons[T](t: T, tail: CatList[T]) extends CatList[T]

  def nonEmpty[T](cl: CatList[T]): Boolean = cl match {
    case CatCons(_, _) => true
  }

```

Normally this is just w warning but becuase I have set warnings to be errors* I see the following output:
```
[error] /home/abatey/polyglotpiglet/scalaz-book/src/main/scala/com/ojha/Chapter4Main.scala:24:46: match may not be exhaustive.
[error] It would fail on the following input: CatNil
[error]   def nonEmpty[T](cl: CatList[T]): Boolean = cl match {

```

However this doesn't work if we have guards in the match. The following code compiles just fine without throwing the above error:

```scala
  def nonEmpty[T](cl: CatList[T]): Boolean = cl match {
    case CatCons(t, tail) if t.toString.equals("cat") => true
  }
```

* To set warnings to be errors I have the following in my build.sbt:

```scala
scalacOptions in ThisBuild ++= Seq(
  // other settings 
  "-Xfatal-warnings"
)
```