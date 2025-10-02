# SM3B
SMall3Bit Instruction Set

## Files
- sm3b.c
  - A code golf style 528 character implementation of SM3B in C
  - Details:
    - Build it using any C compiler (Should work on any compiler since 1973)
    - Values are stored as integers
    - 64 integers of memory
  - Usage: `sm3b instructions...`
  - Example: `sm3b 10++`
- rsm3b.c
  - Really small sm3b.c
  - Unnessesary whitespace and comments removed
  - 437 characters
- sm3b.js
  - A visual implementation of SM3B in Javascript
  - Has animations
  - 65536 integers of memory
- sm3b.html
  - HTML for sm3b.js

## Registers
| Register | Description                                  |
|----------|----------------------------------------------|
| X        | The main register                            |
| Y        | The general purpose register                 |
| A        | The address register                         |
| I        | The instruction address register             |
| C        | The accumulator value                        |


## Instructions
2^3=8 Instructions
| Instruction | Behavior                                                                                          |
|-------------|---------------------------------------------------------------------------------------------------|
| 0           | If previous instruction was not 0 or 1, reset X to zero, otherwise, leftshift X and insert a zero |
| 1           | If previous instruction was not 0 or 1, reset X to one, othersise, leftshift X and insert a one   |
| +           | Add the value of X to the accumulator and copy the result into X                                  |
| -           | Subtract the value of X from the accumulator and copy the result into X                           |
| #           | Swap the values of X and Y                                                                        |
| @           | Swap the values of X and A                                                                        |
| $           | Swap the values of X and the value at the memory address pointed to by A                          |
| ?           | Swap the values of A and I, jumping the the program address, if X is not zero                     |
