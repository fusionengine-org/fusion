import pygame
import pygame.locals as pl
from OpenGL.GL import *
from OpenGL.GLU import *
import imgui
from imgui.integrations.pygame import PygameRenderer

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pl.DOUBLEBUF | pl.OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    imgui.create_context()
    renderer = PygameRenderer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                imgui.get_io().keys_down[pl.K_ESCAPE] = True

        imgui.new_frame()

        # ImGui UI
        imgui.begin("Controls")
        if imgui.button("Rotate"):
            glRotatef(90, 0, 1, 0)
        imgui.end()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()

        imgui.render()
        renderer.render(imgui.get_draw_data())

        pygame.display.flip()
        pygame.time.wait(10)

    imgui.get_io().keys_down[pl.K_ESCAPE] = True  # Handle ESC key for ImGui
    renderer.shutdown()
    imgui.destroy_context()
    pygame.quit()


if __name__ == "__main__":
    main()
