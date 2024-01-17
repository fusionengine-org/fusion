## Using colors
Our engine has some build in predefined colors so it's a bit easier for you with colors, to acess the colors you run:
```python
fusion.WHITE
```
## All colors
The color name is always capitalised as per [PEP 8 → Constants](https://peps.python.org/pep-0008/#constants). All colors are defined and named (with capitalised form) as per [Sublime Text → Docs → Color Schemes → Appendix - CSS Colors](https://www.sublimetext.com/docs/color_schemes.html#appendix-css-colors).

## Custom color
If you want your own color, you just give your function a tuple argument with RGBA colors, here is an example:
```python
fusion.draw_rect(window, 100, 100, 400, 400, (255, 255, 255, 0))
```

## Hex to rgba
If you have a hex color and want to convert it to rgba you can use this function:
```python
fusion.hex_to_rgba(hex)
```

## HSV to RGB
If you have a HSV color and want to convert it to RGB you can use this function:
```python
fusion.hsv_to_rgb(h, s, v)
```
hsv_to_rgb(hue, sat, val, alpha) -> tuple[int, int, int, int]