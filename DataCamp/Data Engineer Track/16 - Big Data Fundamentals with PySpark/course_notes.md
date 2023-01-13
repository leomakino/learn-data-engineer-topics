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

# Workflows, functions, collections

Scala scripts
- A sequence of instructions in a file, executed sequentially
- Useful for smaller projects that can fit into a single file
- The ```scala``` command executes a script by wrapping it in a template and then compiling and executing the resulting program. eg:

```bash
$ scala code.scala
```
**Interpreted language**: a program that directly executes instructions written in a programming language, without requiring them previously to have been commpiled into machine code.


**Compilar**: a program that translates source code from a high-level programming language to a lower level language to create an executable program.

**Scala Applications**

Applications consist of many source files, compiled individually.
- Compiled explicitly then run explicitly
- Consist of many source files that can be complied individually
- Useful for larger programs
- No lag time since applications are precomplied

Scala application example:

If we write the code below and named it as Code.scala

```scala
Object Code extends App {
    println("Hello world")
}
```

Then, you have to compile it first with scalac:
```bash
$ scalac Code.scala
```

Second, run the code with scala:
```
$ scala Code
```

Pros and cons of compiled languages
- **Pros**: Increased performance once compiled
- **Cons**: It takes time to compile code

**Scala workflows**

There are two main ways people prefer to work in Scala:
- Using the command line
- Using an IDE (Integrated development environment)


Functions:

- are invoked with a list of arguments to produce a result
- Function body: follows equals sign = in curly braces {}
- Parts of a function: 
    - Parameter list
    - Body
    - Result type

```scala
// Define a function
def function_name(number: Int): Boolean = {
    number > 10
}
```

Collections. like variables, there are two types: mutable and immutable.

Array
The Scala Array is a mutable collection that stores a fixed-size sequential collection of elements of the same type.
- is a mutable sequence of objects that all share the same type
- Parameterize an array, means, configure its type and parameter values
```scala
// Create array with type parameter: String
// and value parameter: length wich is 3    
val players = new Array[String](3)

// Give data to the array
players(0) = "Leo"

// String is mutable, therefore we can overwrite player(0)
players(0) = "Leonardo"

// The any supertype
val mixedTypes = new Array[Any](3)

// Create and parameterize an array
val hands: Array[Int] = new Array[Int](3)
```
- *Note: the array players is a **val**, and **vals cannot be reassigned** but if the object to which that val **refers is mutable**, that **object can change***
- *Note2: Recommendation: use val with Array. If we made players a var, the elements in our original array could change*

List

The List in Scala is like the Array in that they are a sequence of objects that share the same type. The List collection, however, is immutable. When performing operations on lists, the result will be a new list with a new value. The cons operator (::) prepends an element to a list.
- List has methods, functions that belongs to an object.
- The colon colon operator is pronounced "cons" and it's an operator unique to lists in Scala. Cons prepends an item to a list
- Nil is an empty list.
- A common way to initialize new lists combines Nil and ```::```
- ```:::``` for concatenation
```scala
var players = List("name0", "name1", "name2")

// pre append name3 to players
players = "name3" :: players

// Initialize a new list
val players = "name0" :: "name1" :: "name2" :: Nil

val newPlayers = playerlist1 ::: playerlist2
```
- *Note: Concatenation demonstrates immutability because it's necessary to create a new list to receive them*

# Type Systems, Control Structures, Style

After learning how to control your program with if/else, while loops, and the foreach method, you’ll convert imperative-style code to the Scala-preferred functional style.

Scala's static type system
-**Type**: restricts the possible values to which a variable can refer, or an expression can produce, at run time.
- **Compile time**: when source code is translated into machine code. When scala code is compiled to Java bytecode.
- **Run time**: time executing commands after compilation.

## Type Systems
Static type systems: A language is statically typed if the type of a variable is known at compile time. That is, types checked before run-time. E.g.:
- C/C++
- Fortran
- Java
- Scala

Dynamic type systems: A language is dynamically typed if types are checked on fly. That is, types are checked during execution (i.g., run time)
- JavaScript
- Python
- Ruby
- R

Pros of static type systems
- Increased performance at run time
- Properties of your program verified (i.e., prove the absence of common type-related bugs)
- Safe refactorings
- Documentation in the form of type annotations (: Int in val val_name: Int = 1)

Cons of static type systems
- It takes time to check types (i.g., dalay before execution)
- Code is verbose (i.e., code is longer/more annoying to write)
- The language is not flexible

Compiled, statically-typed languages
- **Compiled languages**: Increased performance at run time
- **Statically-typed languages**: Increased performance at run time

## If else

if expressions result in values, they can be the result of functions, which also result in values.


```scala
// Scala 3 If else example 1
if x < 0 then
  println("negative")
else if x == 0 then
  println("zero")
else
  println("positive")

// Scala if else example
// Inform a player where their current hand stands
val informPlayer: String = {
  if (hand>21) 
    "Bust! :("
  else if (hand == 21)
    "Twenty-One! :)"
  else
    "Hit or stay?"
}
```

| Relational operators description | Symbol         | Logical operators description | Symbol |
|----------------------------------|----------------|-------------------------------|--------|
| Greater than                     | >              | And                           | &&     |
| Less than                        | <              | Or                            | \|\|   |
| Greater than or equal to         | >=             | Not                           | !      |
| Less than or equal to            | <=             |                               |        |
| Equal to                         | ==             |                               |        |
| Not equal                        | !=             |                               |        |



## While

A while loop is another control structure, like if/else. while lets us automate the repetition of instructions to make our code more readable and concise.

```scala
// scala2 while 
// Define counter variable
var i = 0
// Define the number of times for the cheer to repeat
val numRepetitions = 3
// Loop to repeat the cheer
while (i < numRepetitions) {
// BODY OF LOOP
// example
    println("Hip hip hooray!")
    i += 1 // i = i + 1
}
```

```scala
// Loop with while over a collection
// Define counter variable
var i = 0
// Create an array with each player's hand
var hands = Array(17, 24, 21)
// Loop through hands and see if each busts
while (i < hands.length) {
println(bust(hands(i)))
i = i + 1
}
```

Scala is a imperative/functional hybrid. Scala Usually is functional but can also be imperative sometimes

Scala can be imperative:

- One command at a time
- Iterate with loops
- Mutate shared state (e.g. mutating variables out of scope)

**Signs of style**

Scala is a hybrid imperative/functional language. Imperative-style Scala code often has the following traits:

- One command at a time
- Iterate with loops
- Mutate shared state (e.g., mutating variables out of scope)

Functional-style Scala code often has the following traits:

- Functions are used as first-class values
- Operations of a program map input values to output values rather than change data in place


Imperative:
- var
- side effects
- unit

Functional
- val
- No side effects
- Non-Unit value types
    - Int
    - Boolean
    - Double


Scala is functional, functions are first-class values. 
- One aspect of functions being first-class values is that functions can be passed as arguments to functions
- side effects should be avoided, where a side effect means code modifying some variable outside of its local scope


A common way to iterate over a Scala List is with the foreach method. 

The foreach method promotes concise code by allowing a function (pointsToBust) to be passed into it as an argument, which is a feature of Scala being a functional language. Note that if the function had more than one argument, simply writing the function name wouldn't work. 

foreach takes a procedure — a function with a result type Unit — as the right operand. It simply applies the procedure to each List element. The result of the operation is again Unit; no list of results is assembled.


```scala
array_name.foreach(INSERT FUNCTION HERE)
```

