import fusionengine as fusion

main = fusion.Main()

window = main.window.newWindow("Example: 1", 800, 600)
image = main.image.openImage(window, main.DEBUGIMAGE, 100, 100, 400, 400)

while main.window.running(window):
        
    main.image.drawImage(image)

main.quit(window)
