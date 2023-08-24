# API

## Window
### main.window
```python
new_window(title: str, width: int, height: int)
change_icon(image_path: str)
loop(your_loop_func)
set_fps(self, fps: int)
```

## Event
### main.event
```python
key_down(key)
key_down_once(key)
```

## Draw
### main.draw
```python
draw_line(window, x1: int, y1: int, x2: int, y2: int, color: tuple)
draw_line_rect(window, x: int, y: int, width: int, height: int, color: tuple)
draw_rect(window, x: int, y: int, width: int, height: int, color: tuple)
draw_own_rect(window, rect)
set_background_color(window, color: tuple)
```

## Image
### main.image
```python
open_image(window, image_path: str, x: int, y: int, width: int, height: int)
draw_image(image)
```

## Body
### main.body
```python
Entity(window, x: int, y: int, width: int, height: int)
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
new_button(window: windowfe._CustomRenderer, rect: shape._CustomShape, text: str)
```
Some button functions:
```python
your_button.button_pressed() -> bool
```

#### main.ui.text
```python
    def print_text(window, text: str, x: int, y: int, font_path: str, font_size: int, color: tuple)
```

## Debug
### main.debug
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

