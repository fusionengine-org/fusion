# User Interface (UI)

Creating a small ui for your application/game is easy with our following tools:

## Buttons

To create a simple button we do the following:

```python

# Create the button outside the loop
your_button = fusion.Button(
    fusion.Rect(200, 200, 200, 200),
    "Hello World"
)

```

### Button clicked

If you want to check if your button was pressed or is being pressed, then you do that this way:

```python
@main.window.loop
def loop():
    if your_button.button_pressed():
        ... # Do your stuff
```


## Rendering text
If you want to render some fonts, then you can do it like this:

 - Option 1: Render text with build into fusion or your own font
```python
#                                 x   y         font          size    color
fusion.Text(window, "Your text", 10, 10, fusion.NUNITO_LIGHT, 20, fusion.WHITE)
```

 - Option 2: Render text with system font
Its the same option 1, but you change the font to name of the font, like this:
```python
fusion.Text(window, "Your text", 10, 10, "Arial", 20, main.color.WHITE)
```

