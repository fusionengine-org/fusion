# User Interface (UI)

Creating a small ui for your application/game is easy with our following tools:

## Buttons
Creating simple buttons
### Normal button
```python
# Create the button outside the loop.
my_button = fusion.Button(window, 15, 15, 200, 200, 20, "Test")
```
### Custom font button
```python
# Create the button outside the loop.
my_button = fusion.Button(15, 15, 200, 200, 20, "Test", "path/to/my_font.ttf")
```

### Button clicked

If you want to check if your button was pressed or is being pressed, then you do that this way:

```python
@window.loop
def loop():
    if your_button.is_pressed():
        ... # Do your stuff
```


## Rendering text
If you want to render some fonts, then you can do it like this:

 - Option 1: Render text with build into fusion or your own font
```python
#                                 x   y         font          size    color
mytext = fusion.Text("Your text", 10, 10, fusion.DEBUGFONT, 20, fusion.WHITE)
```

 - Option 2: Render text with system font
Its the same option 1, but you change the font to name of the font, like this:
```python
mytext = fusion.Text("Your text", 10, 10, "Arial", 20, fusion.WHITE)
```

And then you can render if inside your loop:
```python
@window.loop
def loop():
    mytext.draw()
```
