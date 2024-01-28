# Scenes and Entities

## Scene manager
See in [this example](https://github.com/dimkauzh/fusion-engine/blob/main/examples/example5.py) how to use the scene manager.

## Entities

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

### Custom animations with entities
Fusion has some build-in features into entity system to make animations more easy, here are some ways to use it

#### Load frames
First of all, you need to load frames, and you can do this using this way:
```python
your_entity.load_animation(images: tuple)
```

#### Setting current frame
You can set the current frame with this function
```python
your_entity.set_frame(frame: int)
```

#### Getting current frame
To get the current frame, run:
```python
my_frame_var = your_entity.get_frame()
```

#### Drawing current frame
To draw current frame, use this function
```python
your_entity.draw_animation()
```

