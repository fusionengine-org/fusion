---
hide:
  - navigation
---

# Main Wiki

## Create window

To create a window were thing are draw, then you need to use this:

```python
your_window = fusion.Window("Example: 1", 800, 600)
```

## Start loop

In a loop you can draw things and it will run with the FPS that is setup. To start a loop, you have two choices:

Choice 1:

```python
@your_window.loop
def loop():
    ... # Your own loop things
```

Choice 2:

```python
while your_window.running():
    ... # Your own loop thing

```

There is basically no difference, they all are doing the same thing, you use what you prefer. In our examples we use choice 1.

## Default message
If you tried using our engine you may have encountered this message being printed to terminal:

```bash
Fusion Engine 1.0.2 (Pygame-ce 2.3.0, Python 3.11.4)
Welcome to Fusion Engine! https://github.com/dimkauzh/fusion-engine
```

To disable this behavior, you just give the main class when initting this argument, set your "FUSION_HIDE_PROMPT" enviorment variable to "no".

## Set Background color

If you want to set a background color, you use this function before all draw functions:

```python
fusion.set_background_color(window, fusion.WHITE)
```

## DeltaTime

if you want to access delta time, you use this:

```python
your_window.DELTATIME
```

## Predefined shapes

We have some predefined shapes that can be used and be drew on the screen. Here are some:

Rectangle:

```python
your_shape = fusion.Rect(window, x, y, width, height, color)
```

### Drawing the shape
To draw your shape, you use this:
```python
your_shape.draw()
```

- More shapes will be coming soon

## Window icon
So you want to change the icon of your window? Well, its easy:

```python
your_window.change_icon("path_to_icon")
```

## Set FPS
To set the framerate of your window, you use this:

```python
your_window.set_fps(60)

```

## Vectors
### Vector2d

If you want to create a 2d vector that stores x and y, then you do this:

```python
vector = fusion.Vector2D(10, 10)
```

## Draw a line
To draw a line, you use this:

```python
#                        x1   y1   x2   y2      color
fusion.draw_line(window, 100, 100, 200, 200, fusion.BLUE)
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

## Create entity WARNING: PRE ALPHA (It's in really early stages)

If you want a player or an enemy or some moving object in your game, you can use an entity, thats an object that
helps you manage things in your game:

```python
#                                    x    y    w   h
your_entity = fusion.Entity(window, 100, 100, 50, 50)
```

### Draw rect with entity

If you want to draw a rectangle that is basically in your entity, then you do it like this:

```python
your_entity.load_rect(fusion.BLACK)
```
Then you can draw it with:

```python
your_entity.draw_rect()
```

### Draw image with entity

If you want to draw a image on your entity, then you do this:

```python
your_entity.load_image("image_path")
```

Then you can draw it with:

```python
your_entity.draw_image()
```

## Sound

### Load sound

To load a sound you do this:

```python
your_sound = fusion.Sound("path_to_sound")
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

### Get volume
To get the volume of your sound you use this:
```python
your_sound.get_volume()
```

### Set volume
To set the volume of your sound you use this:
```python
your_sound.set_volume(0.5)
```

### Fadeout
To fadeout your sound you use this:
```python
your_sound.fadeout(1000)
```


### Backround music
To start playing background music you use this:
```python
your_backgroundmusic = fusion.BackgroundMusic("path_to_sound")
```

#### Set background music volume
To set the volume of your background music you use this:
```python
your_backgroundmusic.set_volume(0.5)
```

## Storage system
### Init

```python
my_db = fusion.JsonStorage("my_db.json")
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
 if fusion.key_down(fusion.KEY_a):
     print("Key A pressed")
```

### Keydown once

If you need keydown to be only once, then you use this:

```python
if fusion.key_down_once(fusion.KEY_a):
    print("Key A pressed")
```


## User Interface (UI)

Creating a small ui for your application/game is easy with our following tools:

### Buttons

To create a simple button we do the following:

```python

# Create the button outside the loop
your_button = fusion.Button(
    fusion.Rect(200, 200, 200, 200),
    "Hello World"
)

```

#### Button clicked

If you want to check if your button was pressed or is being pressed, then you do that this way:

```python
@main.window.loop
def loop():
    if your_button.button_pressed():
        ... # Do your stuff
```

### Rendering text
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

## Quit

The quitting of the engine is done automaticly for you, so you dont have to worry about it.

### Force to quit
If you want to force quit due to some reason, its pretty easy:
```python
your_window.force_quit()
```

