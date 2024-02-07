import fusionengine as fusion

window = fusion.Window("Spritesheet test", 200, 200)
window.set_fps(30)
main_image = fusion.Image(fusion.DEBUGIMAGE, 200, 200, 50, 50)

spr = fusion.SpriteSheet(fusion.DEBUGIMAGE, 100, 100)
spr.frame_size(100, 100)
spr.frame_pos(50, 50)

anim = fusion.Animation(window, spr, 0.1)


@window.loop
def loop():
    anim.play()
