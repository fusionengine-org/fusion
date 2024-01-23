import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from fusionengine import DEBUGIMAGE


def draw_image(texture):
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(-0.5, -0.5)

    glTexCoord2f(1, 0)
    glVertex2f(0.5, -0.5)

    glTexCoord2f(1, 1)
    glVertex2f(0.5, 0.5)

    glTexCoord2f(0, 1)
    glVertex2f(-0.5, 0.5)
    glEnd()


def load_texture(filename):
    image_surface = pygame.image.load(filename)
    image_data = pygame.image.tostring(image_surface, "RGB", 1)
    width, height = image_surface.get_width(), image_surface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data
    )

    # Set texture parameters (optional)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-1, 1, -1, 1)

    image_texture = load_texture(DEBUGIMAGE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1.0, 1.0, 1.0)
        draw_image(image_texture)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
