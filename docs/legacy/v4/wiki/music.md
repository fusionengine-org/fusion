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
