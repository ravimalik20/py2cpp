- Type Dictionary:
  1. Terminal
  2. Literal
  3. Identifier

- Terminal Table:
  1. Id
  2. Token

- Literal Table:
  1. Id
  2. Token

- Identifier Table:
  1. Id
  2. Token

- Uniform Symbol Table
  1. Token Reference: int [Reference to the token placed in one of the three 
  tables.]
  2. Type : int [Reference to the type dictionary to decide what kind of token
  is placed, and also to decide which table to query while taking the
  token reference.]

- Role of the Parser:
  1. Identify the tokens.
  2. Place them into their respective tables and mark their reference into
	the UST.

# SYNTAX ANALYSIS

- Types of Statements:
  1. Declarative:
  	- integer
	- float
	- string
  2. Print
  3. Arithmetic (containing calls to objects and functions too)
  4. Decision Making:
    - if
  5. Looping:
    - while
    - for
  6. Function Declaration
  7. List Object Declaration
  8. Tupple Object declaration
  9. Dictionary Object Declaration
  10. Class Declaration
  11. Exceptions
