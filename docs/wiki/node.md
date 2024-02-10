# Node and Scenes

## Node
If you want a player or an enemy or some moving object in your game, you can use an Node, thats an object that
helps you manage things in your game:

```python
#                                x    y    w   h
your_node = fusion.Node(window, 100, 100, 50, 50)
```

### Get Cordinates
If you want to get the cordinates, then there are a few ways to do it.

#### As a tuple
If you want to get the Cordinates as a tuple, then do the following:
```python
my_cor = your_node.get_coord_tuple()
```

#### As a Vector2D
If you want to get the Cordinates as a Vector2D, then do the following:
```python
my_cor = your_node.get_coord_vec2()
```

### Loading a Rect
If you plan on having the main shape of your Node a rect, or just having a rect connected to the size and position of youe Node,
then you can load the rect using this way:
```python
your_node.load_rect(fusion.BLACK)
```

### Loading an Image
If you just want a static image on your Node or just a image on the size and position of your Node then use this.

```python
your_node.load_image("image_path")
```

### Animations with a Node
Fusion has some build-in features into Node system to make animations more easy, here are some ways to use it.

#### Animation object
If you want to load a object of Animation, then you can do it like this:
```python
your_node.load_animation(animation: Animation)
```
#### Load frames
First of all, you need to load frames, and you can do this using this way:
```python
your_node.load_animation(images: tuple)
```

#### Setting current frame
You can set the current frame with this function
```python
your_node.set_frame(frame: int)
```

#### Getting current frame
To get the current frame, run:
```python
my_frame_var = your_node.get_frame()
```

### Drawing everything
If you want to draw everything, in the same order as you loaded it, you can do that this way:
```python
my_node.update()
```

## Scene manager
See in [this example](https://github.com/dimkauzh/fusion-engine/blob/main/examples/example4.py) how to use the scene manager.
