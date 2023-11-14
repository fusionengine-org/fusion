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
draw_line(window: window.Window, x1: int, y1: int, x2: int, y2: int, color: tuple)
draw_line_rect(window: window.Window, x: int, y: int, width: int, height: int, color: tuple)
draw_rect(window: window.Window, x: int, y: int, width: int, height: int, color: tuple)
set_background_color(window: window.Window, color: tuple)
set_pixel(window: window.Window, x: int, y: int, color: tuple)
```

## Image
```python
Image(window: window.Window, image_path: str, x: int, y: int, width: int, height: int)
```

## Body
```python
Entity(window: window.Window, x: int, y: int, width: int, height: int)
```

## Shape
### main.shape
```python
new_rect(x: int, y: int, width: int, height: int, color: tuple)
new_rect_button(x, y, width, height)
```

## UI
### main.ui
#### main.ui.button
```python
new_button(window: window.Window, rect: shape.Rect, text: str)
```
Some button functions:
```python
your_button.button_pressed() -> bool
```

#### main.ui.text
```python
print_text(window: window.Window, text: str, x: int, y: int, font_path: str, font_size: int, color: tuple)
```

## Debug files
```python
DEBUGIMAGE
```

## Vector
### main.vector
```python
new_vector2d(x: int, y: int)
```

## Sound
### main.sound
```python
load_sound(sound_path: str)
play_background_music(sound_path: str)
set_volume_global(volume)
```

### Loaded sound API
```python
play()
stop()
get_volume()
set_volume(volume: int)
fadeout(time: str)
```

# Math
```python
PI = 3.141592653589793238462643383279502884197
EULERNUMBER = 2.718281828459045
main.math.FLOOR(3.4)
```

