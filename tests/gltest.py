import fusionengine as fusion

window = fusion.Window("GL-Test", 800, 600)
# my_rect = fusion.Rect(10, 10, 100, 100, fusion.BLACK)
# my_rect1 = fusion.Rect(200, 10, 100, 100, fusion.LIME)
# my_rect2 = fusion.Rect(10, 200, 100, 100, fusion.VIOLET)


# my_text = fusion.Text("Hello World!", 40, 40, fusion.DEBUGFONT, 40, fusion.WHITE)

my_button = fusion.Button(15, 15, 200, 200, 20, "Test")


@window.loop
def loop():
    fusion.set_background_color(fusion.BLUE)
    # my_rect.draw()
    # my_rect1.draw()
    # my_rect2.draw()
    # fusion.draw_rect(40, 40, 500, 500, fusion.BLUE)
    my_button.draw()

    if my_button.is_pressed():
        print("Test pressed")
    # my_text.draw()
