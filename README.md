# Basic Interpreter in Python

ShadowScript is a Python-based interpreter designed for a custom scripting language. It provides a versatile environment for executing scripts with various features like variable declarations, arithmetic operations, conditional statements, and loops.

## Installation
To use ShadowScript, simply clone this repository and ensure you have Python installed on your system or test this code in a VM environment, provided in the description of this repository.

![](https://i.imgur.com/JTl6nAx.png)


## Components
ShadowScript consists of several key components:
- `Lexer`: Tokenizes the input script into meaningful tokens.
- `Parser`: Parses the tokens into an abstract syntax tree (AST).
- `Interpreter`: Interprets the AST and executes the script.
- `Data`: Handles storage and retrieval of variables.


## Examples

### Example 1: Variable Declaration and Arithmetic Operation
```python
ShadowScript: make x = 10
ShadowScript: make y = 20
ShadowScript: x + y
```
This example demonstrates declaring two variables and performing an addition operation.

### Example 2: Conditional Statement
```python
ShadowScript: make a = 5
ShadowScript: make b = 10
ShadowScript: if a < b do a = a + 1
```
This example shows the use of a conditional `if` statement to modify a variable based on a comparison.

### Example 3: While Loop
```python
ShadowScript: make counter = 0
ShadowScript: while counter < 5 do make counter = counter + 1
```
In this example, a `while` loop is used to increment a variable until a certain condition is met.

## Limitations
ShadowScript is a basic interpreter and may not support all features of a fully-fledged programming language. It's primarily for educational and experimental purposes.


![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

# Links for additional learning content
1. [Create a Programming Language and Learn Advanced Python](https://www.youtube.com/watch?v=1WpKsY9LBlY)
2. [Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer](https://www.youtube.com/watch?v=RBSGKlAvoiM&list=PLkNZMXPAMnwPWawqMHs5Y2Q5B3Sh5Iwbo&index=22&t=14388s)
3. [Data Structures - Computer Science Course for Beginners](https://www.youtube.com/watch?v=zg9ih6SVACc&list=PLkNZMXPAMnwPWawqMHs5Y2Q5B3Sh5Iwbo&index=3&t=115s)
4. [Recursion in Programming](https://www.youtube.com/watch?v=IJDJ0kBx2LM&t=12s)
5. [Big O Notation](https://www.youtube.com/watch?v=Mo4vesaut8g)