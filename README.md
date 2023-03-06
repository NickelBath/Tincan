# Tincan
Tincan is a tiny  interpreter/compiler  for the Tin-n-Can Programming Langugage.

it has 7 Instructions:

the pointer starts at 0
+ = Adds 1 to the pointer
- = Subtracts 1 to the pointer
$ = Multiplies the pointer by 2
/ = Divides the pointer by 2
: = Prints the pointer
§ = Exits the shell
^ = Resets the pointer back to 0

the source code is in the Main.py file

this is an example of what a theoretical Tin-N-Can program would look like:
  ++-$/:^:§
  "this program adds 2 to the pointer, subtracts one, multiplies it, divides it, prints it, resets it, prints it again and exits the shell

# Issues

Will generate a file even if you don't want it to
There is no error handling
Can't open files
I'm 100% sure it isn't anywhere close to turing complete

# What i hope to fix/add in future versions

The issues in the issues part
More instructions
Rewrite it to be a more traditional language with a parser, lexer and tokenizer
