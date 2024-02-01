import fusionengine as fusion
import time

checked_time = False
start_time = time.time()

window = fusion.Window("test", 600, 600)


if fusion.__version__ == "5.1.0" or fusion.__version__ == "5.0.0":
    image = fusion.Image(fusion.DEBUGIMAGE, 0, 0, 600, 600)

else:
    image = fusion.Image(window, fusion.DEBUGIMAGE, 0, 0, 600, 600)


@window.loop
def loop():
    global checked_time
    image.draw()

    if not checked_time:
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(elapsed_time)
        checked_time = True
