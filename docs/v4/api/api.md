---
hide:
  - navigation
---

# API

## Window
```python
Window(title: str, width: int, height: int) -> your_window
```
### your_window:
```python
change_icon(image_path: str)
loop(your_loop_func)
running(self) -> bool
set_fps(self, fps: int)
force_quit()
toggle_quittable(self)
```

## Events
```python
key_down(key)
key_down_once(key)
```

## Draw
```python
draw_line(window: Window, x1: int, y1: int, x2: int, y2: int, color: tuple)
draw_line_rect(window: Window, x: int, y: int, width: int, height: int, color: tuple)
draw_rect(window: Window, x: int, y: int, width: int, height: int, color: tuple)
set_background_color(window: Window, color: tuple)
set_pixel(window: Window, x: int, y: int, color: tuple)
```

## Image
```python
Image(window: Window, image_path: str, x: int, y: int, width: int, height: int)
```

## Body
```python
Entity(window: Window, x: int, y: int, width: int, height: int)
```

## Shape
```python
Rect(window: Window, x: int, y: int, width: int, height: int, color: tuple) -> your_rect
```
your_rect:
```python
draw()
```

## UI
```python
Button(rect: Rect, text: str) -> your_button
Text(window: Window, text: str, x: int, y: int, font_path: str, font_size: int, color: tuple)
```
your_button:
```python
your_button.button_pressed() -> bool
```

## Debug files
```python
DEBUGIMAGE
```

## Vector
```python
Vector2D(x: int, y: int)
Vector3D(x: int, y: int, z: int)
```

## Sound
```python
Sound(sound_path: str) -> your_sound
BackgroundMusic(sound_path: str) -> your_backgroundmusic
```
your_sound:
```python
play()
stop()
get_volume()
set_volume(volume: int)
fadeout(time: str)
```
your_backgroundmusic:
```python
set_volume(volume: int)
```


# Math
```python
PI = 3.141592653589793238462643383279502884197
EULERNUMBER = 2.718281828459045
main.math.FLOOR(3.4)
```

