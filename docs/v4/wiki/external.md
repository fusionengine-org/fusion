---
hide:
  - navigation
---


# External tools

## Using pygame
If you cant find some function you need in this engine, the you could use pygame as the engine is build on pygame. You dont need to import pygame, as that can make some issues, you just use:
```python
fusion.pg
```

## Using pygame
If you cant find some gui functions, you can use pygame gui, as the engine is using pygame_gui library. You dont need to import pygame gui, as that can make some issues, you just use:
```python
fusion.gui
```

## Using Codon Compiler
So you heard of [codon](https://docs.exaloop.io/codon/), a python compiler with can compile your python code to machine code, which makes your code a lot faster But how do you use it? Well, its easy! You just install it and then modify these things in your code:

Imports:
```python
from python import fusionengine as fusion
```

Loop:
You need to modify our loop to support codon, so you need to change it to this:
```python
while your_window.running():
    ... # Your own loop thing
```
You may reconise this type of while loop from the main wiki as your second option.