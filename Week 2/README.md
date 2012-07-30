Plan For Week 2 (28 JUL 12)
===========================
## Types ##
### Integers ###
- Store Whole Numbers.
- input() Can be used in place of raw_input() to store directly to int.
- Increment/Decrement: +=, -=

### Strings ###
- Stores a word, phrase or even character
- Can 'slice' with [start:end:step]

### Lists ###
- Similar to an array in other languages
- Store a collection of any other object
- Can be accessed with slicing

### Booleans ###
- Holds 'True' or 'False'
- Can be generated with conditionals:
  - == - Equal To
  - != - Not Equal To
  - < - Less Than
  - > - Greater Than
  - <= - Less Than Or Equal To
  - >= - Greater Than Or Equal To

### Dictionaries ###
- Use ['name'] to access
- Can be defined JSON-Style

## Program Flow ##
### For Loop ###
- for x in y:
- Use tabbed block
- Range() can be used to run a for loop a specific number of times

### If ###
- Used to evaluate a conditional or check boolean value
- Also checks if object is not None, or a string of ''
- elif - elseif
- else - Default Executed if nothing else does

### While ###
- Checks condition at beginning and performs until condition is False (always checks as loop starts again)

### Errata Program Control ###
- break: Jumps out of current loop block and keeps executing
- continue: skips rest of block and goes to top/rechecks condition

## Advanced Topics ##
### Slicing ###
- Indexing starts at 0!
- Negative indeces
- [start:end:step]

### Arguments ###
- sys.argv -> list of arguments

## Functions ##
- What used for?:
  - Repeating a block of code
  - Modularity

- How to define:

> def testfunc():
  
- def keyword - Defines a function

- Arguments
  - def testfunc(arg1):
  - can now be called with testfunc(arg1)