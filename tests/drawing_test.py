import fusionengine as fe

main = fe.Main()

window = main.window.new_window("test", 400, 400)

@main.window.loop
def loop():
    main.draw.draw_rect(window, 0, 0, 300, 200, (234, 43, 54, 100))
        
    image = main.image.open_image(window, main.debug.DEBUGIMAGE, 64, 64, 64, 64)
    main.image.draw_image(image)