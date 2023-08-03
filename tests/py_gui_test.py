import pygame as pg
import pygame_gui

pg.init()
pg.display.set_mode((800, 600))

manager = pygame_gui.UIManager((800, 600))
hello_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)), text='Hello', manager=manager)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        manager.process_events(event)

    manager.update(1.0 / 60.0)

    if hello_button.check_pressed():
        print('Hello World!')

    manager.draw_ui(pg.display.get_surface())

    pg.display.flip()

pg.quit()
