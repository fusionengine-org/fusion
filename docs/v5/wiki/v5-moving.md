# Moving to v5
If your moving to v5 from v4. then here is the things you might need to take care about for your application to support v5.

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
my_text = fusion.Text(your_window,
                    "test", 
                    10,
                    10,
                    "Arial",
                    12,
                    fusion.BLUE
)

@your_window.loop
def loop():
    my_text.draw()
```

## Build in fonts
There are no build in font anymore in fusion. Instead use system fonts or your own custom font.

## Rect class
Now the rect class doesn't get the color argument for shape reasons. Instead, you pass the color argument to the draw method.
The rect argument now works like this
```python
my_rect = fusion.Rect(
                    your_window,
                    10,
                    10,
                    100,
                    100
                    )

@your_window.loop
def loop():
    my_rect.draw(fusion.BLUE)
```
If you don't pass the color argument, it will automatically use blue color instead.

## Drawing images

### draw_image_file
This function has been renamed to draw_image.

