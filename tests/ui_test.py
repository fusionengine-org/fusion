import fusionengine as fusion

window = fusion.Window()

button = fusion.Button(fusion.Rect(window, 64, 64, 64, 64), "Click me")

@window.loop
def loop():
    if button.button_pressed():
        print("hi")

