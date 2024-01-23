import fusionengine as fusion

window = fusion.Window("GL-Test", 800, 600)
my_rect = fusion.Rect(window, 10, 10, 100, 100)

my_text = fusion.Text(window, "Hello World!", 40, 40, "Arial", 40, fusion.WHITE)


@window.loop
def loop():
    # my_rect.draw(fusion.RED)
    # fusion.draw_rect(window, 40, 40, 500, 500, fusion.BLUE)
    my_text.draw()
