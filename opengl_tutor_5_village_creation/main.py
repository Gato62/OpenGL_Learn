import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def main(width, height):
    pg.init()
    screen = (width, height)
    pg.display.set_mode(screen, DOUBLEBUF | OPENGL)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClearColor(.2, .2, .25, .0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        triangles()

        size = 2
        up, down = 4, 0
        left, right = 8, 0
        r, g, b = 6, 4, 2

        size_2 = 3
        up_2, down_2 = 0, 4
        left_2, right_2 = 8, 0
        r_2, g_2, b_2 = 1, 2, 6

        squad(size, up, down, left, right, r, g, b)
        squad(size_2, up_2, down_2, left_2, right_2, r_2, g_2, b_2)

        pg.display.flip()
        pg.time.wait(20)


def triangles():
    right = 8
    left = 5
    right /= 10
    left /= 10

    glBegin(GL_TRIANGLES)
    glColor3f(.7, .3, .2)

    glVertex2f(-.3 - left, .3)
    glVertex2f(-.3 - left, .0)
    glVertex2f(.0 - left, .0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(.2, .7, .3)

    glVertex2f(-.3 + right - left, .3)
    glVertex2f(-.3 + right - left, .0)
    glVertex2f(.0 + right - left, .0)
    glEnd()


def squad(size, up, down, left, right, red, green, blue):
    right /= 10
    left /= 10
    up /= 10
    down /= 10
    size /= 10
    red /= 10
    green /= 10
    blue /= 10

    for index in range(10):
        dx = index * .12
        red = index * .07
        glBegin(GL_QUADS)
        glColor3f(red, green, blue)

        glVertex2f(dx - left + right, .0 - down + up)
        glVertex2f(dx - left + right, .0 + size - down + up)
        glVertex2f(dx + size - left + right, .0 + size - down + up)
        glVertex2f(dx + size - left + right, .0 - down + up)
        glEnd()


if __name__ == '__main__':
    main(800, 800)
