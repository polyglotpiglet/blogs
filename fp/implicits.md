# Implicit Parameters

Let's say we have a type class and one concrete instance of it. 

```scala
  trait Funky[F[_]] {
    def chicken() = println("chicken")
  }

  implicit val funkyOption = new Funky[Option] {}
```

I want to write a method which takes in a funky and calls the chicken method on it. There are several ways I can write such a method. 

**Option 1:** pass as an implicit parameter

```scala
  def f1[F[_]](implicit funky: Funky[F]) = funky.chicken()
```

**Option 2:** Using a context bound and implicitly accessing the funky

```scala
  def f2[F[_]: Funky] = implicitly[Funky[F]].chicken()

```

**Option 3:** Write my own version of implicitly

```scala
  object Funky {
    def myImplicitly[F[_]](implicit f: Funky[F]) = f
  }

  def f3[F[_]: Funky] = Funky.myImplicitly[F].chicken()
```

This is a bit rubbish so why don't I rename the method from 'myImplicitly' to 'apply'. 

```scala
  object Funky {
    def apply[F[_]](implicit f: Funky[F]) = f
  }

  def f3[F[_]: Funky] = Funky[F].chicken()
```