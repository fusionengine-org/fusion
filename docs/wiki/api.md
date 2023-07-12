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
    # Your own loop things
    pass
```

Choice 2:
```python
while main.window.running(window):

   # Your own loop things
   pass

```
There is basically no difference, they all are doing the same thing, you use what you prefer. In our examples we use choice 1.

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

## Draw rectangle
If you just want to draw a rectangle to test or to use it for your game/app:
```python
main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)
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

## Create entity (being worked on)
If you want a player or an enemy or some moving object in your game, you can use an entity, thats an object that does some physics for you
and helps you manage things in your game:
```python
entity = main.body.Entity("rigid", window, 100, 100, 50, 50)
```

## Keyboard input
if you need keyboard input, then use this if statement with your own key (see key tab for all key names):
```python
 if main.event.key_down(main.keys.KEY_a, window):
     print("Key A pressed")
```
## Quit
To quit the application, you run this command on the end of your code:
```python
main.quit(window)
```
[Back](wiki.md)
[Next](color_api.md)