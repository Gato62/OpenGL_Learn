import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from opengl_tutor_5_village_creation import objects as ob


def main(width, height):
    pg.init()
    screen = (width, height)
    pg.display.set_mode(screen, DOUBLEBUF | OPENGL)

    alpha = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClearColor(.3, .8, .9, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        alpha -= 2

        glPushMatrix()
        glTranslatef(0, -1, 0)
        glRotatef(alpha, 0, 0, 1)
        glTranslatef(1.7, 0, 0)
        ob.circle(32, 1)  # edges, radius, x, y

        glPopMatrix()

        ob.rectangle(-10, -10, 20, 12, 4, 5, 3)
        ob.house(5, -4, 5)  # scale, x, y
        ob.house(10, 0, 0)
        ob.house(7, 3, 3)



        pg.display.flip()
        pg.time.wait(20)


if __name__ == '__main__':
    main(800, 800)
