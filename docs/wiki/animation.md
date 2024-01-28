# Animations and Spritesheets

## Animation system (Early stages)
If you want to draw a animation, then you can do it this way

### Loading the animations
To load the animation, run
```python
my_anim = fusion.Animation(your_window: Window, your_images: tuple | Spritesheet)
```

### Drawing animation
To draw it then, run:
```python
my_anim.draw(frames: int)
```
The frames specify the number of frames to draw each time. It can be as low as you like, or as high as you like, depending on the speed of the animation that you want.

## Spritesheets
### Creating spritesheets
First, create your spritesheet. You can do it this way:
```python
spr = fusion.SpriteSheet(fusion.DEBUGIMAGE, 100, 100)
```
This will cut down your spritesheet in 100x100 pixels images. Then it will be places inside `spr.frames` as `Image` objects. The images are cut from corner down-left to down-right. Then it goes a row higher and cuts futher. 

Then, set the size of each image and then set the coordinates. (This is required or else they will be automatically set to 0)
Set the size:
```python
spr.frame_size(60, 60)
```

This will set the size of each image 60x60 pixels. 
Then, set the coordinates:
```python
spr.frame_pos(50, 50)
```
This will set the X-axis and Y-axis to 50.