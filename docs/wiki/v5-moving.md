# Moving to v5
If your moving to v5 from v4. then here is the things you might need to take care about for your application to support v5.

## Drawing functions
All functions that draw something on the screen got rid of the first argument, aka your window. These function/classes include:

Classes:
```python
fusion.Image()
fusion.Button()
fusion.Text()
```

Functions:
```python
fusion.draw_rect()
fusion.draw_image()
fusion.set_background_color()
fusion.draw_line()
fusion.draw_line_rect()
fusion.draw_arbitrary_polygon_outline()
fusion.set_pixel()
```

## Custom colors
If you used color that are not automatically specified in the api, but rather with a custom tuple, then you might need to migrate to the
new way of colors in fusion engine. Here is the new way to handle colors in fusion v5:
```python
fusion.Color(255, 255, 255, 255)
```
So instead of using a tuple, you use a object of Color class. This is appleid to all functions from before.

## Drawing text
Normally if you used the text class, then you used it inside a loop. The new way is to load it ouside the loop and then render it inside the loop. Here is a example
```python
my_text = fusion.Text("test", 10, 10, "Arial", 12, fusion.BLUE)

@your_window.loop
def loop():
    my_text.draw()
```

## Build-in fonts
There are no build-in font anymore except the DEBUGFONT in fusion. This font is Nunito Light font, that you can use as you want. If not, you can always use your own font or the os build in font.

## draw_image_file
This function has been renamed to draw_image.

## Removal of pygame-gui and some aspects of pygame-ce
### pygame-gui
You can no longer use pygame-gui with fusion. Instead, you can use build in UI library
### pygame-ce
You can no longer use your own drawing code in pygame-ce with fusion, as fusion moved to PyOpenGL for rendering purposes. If you want to know how to use PyOpenGL with fusion, go to the external page of the wiki.

## Buttons
Making button is now different than before. Now you don't pass a rect, instead you pass all of this:

 - Window
 - X
 - Y
 - Width
 - Height
 - Font_size
 - Text
 - Font (Optional, if not given then the default font will be used)

So like this:
```python
my_button = fusion.Button(15, 15, 200, 200, 20, "Test")
```

### Drawing it
Drawing the button is really easy, just like this:

```python
@your_window.loop
def loop():
    my_button.draw()
```

### Gettig if clicked
If you want to get if a button is pressed, just do it this new way:
```python
@window.loop
def loop():
    if your_button.is_pressed():
        ... # Do your stuff
```

## Force quit naming
The force_quit() function inside the window class has been changed to quit() instead. It operates the same way as before.