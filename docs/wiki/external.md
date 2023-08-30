# External tools

## Using pygame
If you cant find some function you need in this engine, the you could use pygame as the engine is build on pygame. You dont need to import pygame, as that can make so issues, you just use:
```python
fusion.pg
```
Make sure your not using main (the initialized class) but the module itself.

## Using Codon Compiler
So you heard of [codon](https://docs.exaloop.io/codon/), a python compiler with can compile your python code to machine code, which makes your code a lot faster But how do you use it? Well, its easy! You just install it and then modify these things in your code:

Loop:
You need to modify our loop to support codon, so you need to change it to this:
```python
while main.window.running(window):
    ... # Your own loop thing
```
You may reconise this type of while loop from the main wiki as your second option.