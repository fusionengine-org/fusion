## Using colors
Our engine has some build in predefined colors so it's a bit easier for you with colors, to acess the colors you run:
```python
main.color.WHITE
```
## All colors
The color name is always in capital letters. Here are all predefined colors:
```python
BLUE = (0, 0, 255, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREEN = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
YELLOW = (255, 255, 0, 255)
PURPLE = (255, 0, 255, 255)
CYAN = (0, 255, 255, 255)
ORANGE = (255, 165, 0, 255)
GRAY = (128, 128, 128, 255)
BROWN = (165, 42, 42, 255)
PINK = (255, 192, 203, 255)
MAGENTA = (255, 0, 255, 255)
SILVER = (192, 192, 192, 255)
GOLD = (255, 215, 0, 255)
BRONZE = (205, 127, 50, 255)
LIME = (0, 255, 0, 255)
OLIVE = (128, 128, 0, 255)
TEAL = (0, 128, 128, 255)
NAVY = (0, 0, 128, 255)
MAROON = (128, 0, 0, 255)
INDIGO = (75, 0, 130, 255)
TURQUOISE = (64, 224, 208, 255)
VIOLET = (238, 130, 238, 255)
AQUA = (0, 255, 255, 255)
TAN = (210, 180, 140, 255)
BEIGE = (245, 245, 220, 255)
IVORY = (255, 255, 240, 255)
LAVENDER = (230, 230, 250, 255)
MINT = (189, 252, 201, 255)
SALMON = (250, 128, 114, 255)
SCARLET = (255, 36, 0, 255)
TEAL = (0, 128, 128, 255)
TOMATO = (255, 99, 71, 255)
```
## Custom color
If you want your own color, you just give your function a tuple argument with RGBA colors, here is an example:
```python
main.draw.drawRect(window, 100, 100, 400, 400, (255, 255, 255, 0))
```
[Back](<https://dimkauzh.github.io/fusion-engine/docs/wiki/api.html>)
[Next](<https://dimkauzh.github.io/fusion-engine/docs/wiki/fonts.html>)
