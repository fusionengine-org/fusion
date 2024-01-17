# Small math module
## Vectors
### Vector2d

If you want to create a 2d vector that stores x and y, then you do this:

```python
vector = fusion.Vector2D(10, 10)
```
This creates a vector with the x being 10 and the y also being 10.

### Vector3d
if you want to create a 3d vector that stores x, y and z, then you do this:
```python
vector = fusion.Vector3D(10, 10, 10)
```
This creates a 3d vector with the x, y and z being 10.

## Types of PI in Fusion Engine
These are used for certain miscellaneous math things.

Full version of pi (3.141592653589793238462643383279502884197):
```python
	fusion.PI
```
A slightly smaller version that python's math library uses (3.141592653589793):
```python
	fusion.SMALLERPI
```
An extremely shortened version of pi (3.14):
```python
	fusion.SMALLPI
```

This allows you to get the floor value of a number.
```python
  fusion.FLOOR(3.4)
```
## Euler's Number
You can read more about it [here.](https://en.wikipedia.org/wiki/E_(mathematical_constant))
```python
	fusion.EULERNUMBER
```
