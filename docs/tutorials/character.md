# Basic Moving Character Tutorial
This is a tutorial how to build a basic moving character using fusion-engine. We wil be using the new Node system introduced in V5.2 to make everything easier.
We are going to make a small moving character. The character is gonna be a node with the fusion icon as image.

## Setting up
First, make sure you have the latest version of Fusion installed (V5.2 and later). Without this it won't work, as we will be using a feature introduced in that version.
If you want have fusion yet setup, then go back to [the setup tutorial](setup.md)

## Basic things
First, lets get the basic things setup, like a window and a loop.

First, we import `fusionengine` as `fusion`:
```python
import fusionengine as fusion
```

Then we create a window where all drawing will take place:
```python
window = fusion.Window("Basic Character - Fusion Engine", 800, 600)
```

After the window is done, we can create the loop:
```python
@window.loop
def loop():
    ... # Our code is gonna go here
```
Thats it! We have a basic window and loop setup!

## Getting the Node setup

