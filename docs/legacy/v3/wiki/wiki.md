
# Main Wiki

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

## Window icon
So you want to change the icon of your window? Well, its easy:

```python
main.window.change_icon("path_to_icon")
```

## Set FPS
To set the framerate of your window, you use this:

```python
main.window.set_fps(60)

```

## Vectors

### Vector2d

If you want to create a 2d vector that stores x and y, then you do this:

```python

vector = main.vector.new_vector2d(10, 10)
```

## Draw a line
To draw a line, you use this:

```python
#                           x1   y1   x2   y2       color
main.draw.draw_line(window, 100, 100, 200, 200, main.color.BLUE)
```


## Draw rectangle

If you just want to draw a rectangle to test or to use it for your game/app, then you have 3 options:

Option one: just draw a rectangle

```python
main.draw.draw_rect(window, 100, 100, 400, 400, main.color.BLUE)
```

Second option: draw predefined rectangle:

```python
main.draw.draw_own_rect(window, your_rect)
```

Third option: Draw a rectangle of lines
    
```python
#                                 x    y    w    h        color
main.draw.draw_line_rect(window, 100, 100, 400, 400, main.color.BLUE)
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

## Sound

### Load sound

To load a sound you do this:

```python
your_sound = main.sound.load_sound("path_to_sound")
```

### Play sound

To play your loaded sound you use this:

```python
your_sound.play()
```

### Stop sound
To stop your playing sound you use this:
```python
your_sound.stop()
```

### Backround music
To start playing background music you use this:
```python
main.sound.play_background_music("path_to_sound")
```


## Storage system
### Init

```python
my_db = JsonStorage("my_db.json")
```
This how you initialize your json storage system

### Insertion

```python
my_db.insert({"first_name": "john", "last_name": "wick", "gold": 50})
my_db.insert({"first_name": "alexander", "last_name": "wick", "gold": 20})
```
The code inserts two entries into the storage. The inserted data contains information about individuals' first names, last names, and gold amounts.

### Reading

```python
Copy code
my_db.search({"last_name": "wick"})
my_db.search({"last_name": "wick"}, get_index=True)
```
The code demonstrates reading operations. It searches for entries with the last name "wick" and retrieves results with and without index information.

### Updating

```python
alex['gold'] += 20
my_db.update(alex_index, alex)
```
The code showcases how to update data in the storage. In this case, it increases the "gold" value for an entry with the first name "alexander" by 20.

### Deleting

```python
my_db.delete(john_index)
```
The code demonstrates deletion of data by removing an entry with the first name "john" from the storage.

### Saving to Disk
```python
my_db.save()
```
The code shows how to save the modified data back to the storage file on disk.


## Keyboard input

### Keydown

if you need keyboard input, then use this if statement with your own key (see key tab for all key names):

```python
 if main.event.key_down(main.keys.KEY_a):
     print("Key A pressed")
```

### Keydown once

If you need keydown to be only once, then you use this:

```python
if main.event.key_down_once(main.keys.KEY_a):
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

### Force to quit
If you want to force quit due to some reason, its pretty easy:
```python
main.window.force_quit()
```

