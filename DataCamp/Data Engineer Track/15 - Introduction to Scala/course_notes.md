# Course Description
Introduction to the programming language Scala. You'll learn why and how companies like Netflix, Airbnb, and Morgan Stanley are choosing Scala for large-scale applications and data engineering infrastructure. You'll learn the basics of the language, including syntax and style, focusing on the most commonly used features in the Scala standard library. You'll learn by writing code for a real program that plays a computer version of the popular card game Twenty-One. You’ll get a taste of the value of a hybrid object-oriented and functional programming language, of which Scala is the foremost example. We recommend this course for learners with intermediate-level programming experience, which can be acquired in the listed prerequisites.

# A Scalable Language
You'll learn what Scala is, who uses it, and why you should use it. You'll explore four common data types: integers, floating-point numbers, logical values, and text, using the Scala interpreter. 

What is Scala?
- Scala is a general purpose programming language providing support for functional programming and a strong static type system.
- Designed to be concise.
- Scala source code is intended to be compled to Java bytecode, so that the resulting executable code runs on a Java virtual machine
- Scala is like a newer, improved Java
- Scala combines object-oriented and functional programming in one concise, high-level language.
- Scala's static types help avoid bugs in complex applications, and its JVM and JavaScript runtimes let you build high-performance systems with easy access to huge ecosystems of libraries.

Why use Sala?
- **SCA**lable **LA**nguage
- **Flexible**: Scala lets you add new types, collections, and control constructs that feel like they are built-in to the language
- **Convenient**: The Scala standard library has a set of convenient predefined types, collections, and control constructs.

Who uses Scala?
- Roles: Software Engineers, Data Engineers, Data Scientiss, ML Engineers...
- Industries: Finance, Tech, Healthcare

Scala is Object-oriented programming (OOP)
- Every value is an object
- every operation is a method call

Scala is functional
1. Functions are first-class values
2. Operations of a program should map input values to output values rather than change data in place

Scala Variables
- val: immutable
- var: mutable
- java.lang.Double
- java.lang.Float
- java.lang.Long
- java.lang.Int
- java.lang.Short
- java.lang.Byte
- java.lang.Char
- java.lang.Boolean
- java.lang.Unit

Scala value types have equivalent Java types

| Scala types   | Java types        |
|---------------|-------------------|
| scala.Double  | java.lang.Double  |
| scala.Float   | java.lang.Float   |
| scala.Long    | java.lang.Long    |
| scala.Int     | java.lang.Int     |
| scala.Short   | java.lang.Short   |
| scala.Byte    | java.lang.Byte    |
| scala.Char    | java.lang.Char    |
| scala.Boolean | java.lang.Boolean |
| scala.Unit    |   |

```Scala
// Define an immutable int 
val two: Int = 2
// or simply
val two = 2

// Define an immutable string
val name: String = Leo
```