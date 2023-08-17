# Api docs

## Create window

To create a window were thing are draw, then you need to use this:

```python
window = main.window.new_window("Example: 1", 800, 600)
```

## Start loop

In a loop you can draw things and it will run with the FPS that is setup. To start a loop, you have two choices:

Choice 1:

```python
@main.window.loop
def loop():
    ... # Your own loop things
```

Choice 2:

```python
while main.window.running(window):
    ... # Your own loop thing

```

There is basically no difference, they all are doing the same thing, you use what you prefer. In our examples we use choice 1.

## Default message
If you tried using our engine you may have encountered this message being printed to terminal:

```bash
Fusion Engine 1.0.2 (Pygame-ce 2.3.0, Python 3.11.4)
Welcome to Fusion Engine! https://github.com/dimkauzh/fusion-engine
```

To disable this behavior, you just give the main class when initting this argument: ``` message=False ```, like this:
```python
import fusionengine as fusion

main = fusion.Main("message=False")
```

## Set Background color

If you want to set a background color, you use this function before all draw functions:

```python
main.draw.set_background_color(window, main.color.WHITE)
```

## DeltaTime

if you want to access delta time, you use this:

```python
main.window.DELTATIME
```

## Predefined shapes

We have some predefined shapes that can be used and be drew on the screen. Here are some:

Rectangle:

```python
main.shape.new_rect(x, y, width, height, color)
```

- More shapes will be coming soon

## Draw rectangle

If you just want to draw a rectangle to test or to use it for your game/app, then you have two options:

Option one: just draw a rectangle

```python
main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)
```

Second option: draw predefined rectangle:

```python
main.draw.draw_own_rect(window, your_rect)
```

## Draw image

You first need to create a variable with your image and image data:

```python
image = main.image.open_image(window, main.DEBUGIMAGE, 100, 100, 400, 400)
```

main.DEBUGIMAGE is an image that is included with the engine, so you can use it freely.
Then you need to render it (In the best situation this will happen in your loop):

```python
main.image.draw_image(image)
```

## Create entity WARNING: PRE ALPHA (It's in really early stages)

If you want a player or an enemy or some moving object in your game, you can use an entity, thats an object that
helps you manage things in your game:

```python
#                                  x    y    w   h
entity = main.body.Entity(window, 100, 100, 50, 50)
```

### Draw rect with entity

If you want to draw a rectangle that is basically in your entity, then you do it like this:

```python
entity.draw_image(main.color.BLACK)

```

### Draw image with entity

If you want to draw a image on your entity, then you do this:

```python
entity.image("image_path")
```


## Keyboard input

if you need keyboard input, then use this if statement with your own key (see key tab for all key names):

```python
 if main.event.key_down(main.keys.KEY_a, window):
     print("Key A pressed")
```

## User Interface (UI)

Creating a small ui for your application/game is easy with our following tools:

### Buttons

To create a simple button we do the following:

```python

# Create the button outside the loop
button = main.ui.button.new_button(
    window,
    main.shape.new_rect_button(200, 200, 200, 200),
    "Hello World"
)

```

#### Button clicked

If you want to check if your button was pressed or is being pressed, then you do that this way:

```python
@main.window.loop
def loop():
    if button.button_pressed():
        ... # Do your stuff
```

### Rendering text
If you want to render some fonts, then you can do it like this:

 - Option 1: Render text with build into fusion or your own font
```python
#                                            x   y         font              size      color
main.ui.text.print_text(window, "Your text", 10, 10, main.fonts.NUNITO_LIGHT, 20, main.color.WHITE)
```

 - Option 2: Render text with system font
Its the same option 1, but you change the font to name of the font, like this:
```python
main.ui.text.print_text(window, "Your text", 10, 10, "Arial", 20, main.color.WHITE)
```

## Quit

The quitting of the engine is done automaticly for you, so you dont have to worry about it.

[Back](https://dimkauzh.github.io/fusion-engine/docs/index.html)
[Next](<https://dimkauzh.github.io/fusion-engine/docs/wiki/color_api.html>)


[Back to main page](https://dimkauzh.github.io/fusion-engine/docs/index.html)
