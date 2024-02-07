# External tools

## Using OpenGL
Fusion is build on its own custom OpenGL binding using CTypes (FusionGL). If you want to use GL for yourself, you can try to use our own wrapper, but keep in mind that our own implementation only has the functions we need. Use it like this: `fusionengine.fusiongl`

If you want to use PyOpenGL, you should be able to do that without any problems.

### Where to put code
All the rendering code should be placed inside the while loop, and fusion should render it for you. Do not clear the screen as that will be automatically done for you.

### Warning
This is not tested. It may not work or work as expected. If you find any bugs, please create a issue on github. Thank you.

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
