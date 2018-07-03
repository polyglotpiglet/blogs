# Algebraic Data Type

An algebraic data type comprises any subset of the following where none has any methods or fields other than the constructor params:

```scala
  // value types
  case object Bow
  type Name = String
  type Age = Int

  // product types
  final case class Cat(name: Name, age: Age)

  // coproduct types
  sealed abstract class CatType
  case object Tortie extends CatType
  case object Tabby extends CatType


//generalised algebraic data type has a type param
  sealed abstract class CatList[T]
  case object CatNil extends CatList
  case class CatCons[T](t: T, tail: CatList[T]) extends CatList[T]

// This example is also recursive because it is self referencing

```
eg list



