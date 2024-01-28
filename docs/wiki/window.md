# Windowing

## Create window

To create a window were thing are draw, then you need to use this:

```python
your_window = fusion.Window("Example", 800, 600)
```

## Start loop

In a loop you can draw things and it will run with the FPS that is setup. To start a loop, you have two choices:

Choice 1:

```python
@your_window.loop
def loop():
    ... # Your own loop things
```

Choice 2:

```python
while your_window.running():
    ... # Your own loop thing

```

There is basically no difference, they all are doing the same thing, you use what you prefer. In our examples we use choice 1.


## Set FPS
To set the framerate of your window, you use this:

```python
your_window.set_fps(60)

```

## Window icon
So you want to change the icon of your window? Well, its easy:

```python
your_window.change_icon("path_to_icon.png")
```

## DeltaTime

if you want to access delta time, you use this:

```python
your_window.DELTATIME
```

## Quit

The quitting of the engine is done automaticly for you, so you dont have to worry about it.

### Force to quit
If you want to force quit due to some reason, its pretty easy:
```python
your_window.force_quit()
```

## Full Screen
If you want to know if the window is full screen then run the following command:
```python
your_var = your_window.is_fullscreen()
```

If you want to toggle the fullscreen on your window then run the following command:
```python
your_window.toggle_fullscreen()
```

## Screen Safer
If you want to know if screen safer is allowed on the current machine then run the following command:
```python
your_var = your_window.get_screensafer_allowed()
```

If you want to toggle the screen safer allowed on the current machine then run the following command:
```python
your_window.toggle_screensafer_allowed()
```

## Vsync
If you want to know if VSync in enabled on the current machine then run the following command:
```python
my_var = your_window.get_vsync_enabled()
```

## Displays
### Refresh rate
If you want to get the display refresh rate on the current machine then run the following command:
```python
my_var = your_window.get_screen_refresh_rate()
```

## Display amount
If you want to get the display amount on the current machine then run the following command:
```python
my_var = your_window.get_display_amount()
```

## Active
If you want to get the active state on the current machine then run the following command:
```python
my_var = your_window.get_active()
```