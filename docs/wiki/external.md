# External tools

## Using PyOpenGL
If you cant find some function you need in this engine, the you could use PyOpenGL as the engine is build on PyOpenGL. You can import the PyOpenGL library or use the build in wrapper functions like this:
```python
import fusionengine.backend.gl as gl
```
Keep in mind that this will not have all functions you mind need as the wrapper only has functions that fusion requires. If you want, you can import PyOpenGL by yourself.

### Where to put code
All the rendering code should be placed inside the while loop, and fusion should render it for you.

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