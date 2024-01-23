# Rendering
## Set Background color

If you want to set a background color, you use this function before all draw functions:

```python
fusion.set_background_color(fusion.WHITE)
```


## Predefined shapes

We have some predefined shapes that can be used and be drew on the screen. Here are some:

Rectangle:

```python
your_shape = fusion.Rect(x, y, width, height, color)
```

### Drawing the shape
To draw your shape, you use this:
```python
your_shape.draw()
```

- More shapes will be coming soon


## Draw a line
To draw a line, you use this:

```python
#                        x1   y1   x2   y2      color
fusion.draw_line(100, 100, 200, 200, fusion.BLUE)
```

## Draw rectangle

If you just want to draw a rectangle to test or to use it for your game/app, then you have 3 options:

Option one: just draw a rectangle

```python
#                         x    y    w    h      color
fusion.draw_rect(window, 100, 100, 400, 400, fusion.BLUE)
```

Third option: Draw a rectangle of lines
    
```python
#                              x    y    w    h      color
fusion.draw_line_rect(window, 100, 100, 400, 400, fusion.BLUE)
```


## Draw image

You first need to create a variable with your image and image data:

```python
your_image = fusion.Image(window, fusion.DEBUGIMAGE, 100, 100, 400, 400)
```

main.DEBUGIMAGE is an image that is included with the engine, so you can use it freely.
Then you need to render it (In the best situation this will happen in your loop):

```python
your_image.draw()
```

