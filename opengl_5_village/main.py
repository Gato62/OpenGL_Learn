import math as m
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from opengl_6_graph import graphs as gr


def main(width, height):
    pg.init()
    screen = (width, height)
    pg.display.set_mode(screen, DOUBLEBUF | OPENGL)

    # ratio = (width / height)
    # glScalef(1 / ratio, 1, 1)
    #
    # print('ratio: ', ratio)

    # alpha = 0
    count = 100
    current_x = 10

    gr.init(0, current_x, count)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClearColor(.2, .2, .2, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # alpha -= 2\
        #
        # glPushMatrix()
        # glTranslatef(0, -1, 0)
        # glRotatef(alpha, 0, 0, 1)
        # glTranslatef(1.7, 0, 0)
        # ob.circle(32, 1)  # edges, radius, x, y
        #
        # glPopMatrix()
        #
        # ob.rectangle(-10, -10, 20, 12, 4, 5, 3)
        # ob.house(5, -4, 5)  # scale, x, y
        # ob.house(10, 0, 0)
        # ob.house(7, 3, 3)

        glLineWidth(2)
        glColor3f(.8, .3, .2)
        gr.axes(0, 1)
        glColor3f(.4, .8, .1)
        gr.axes(90, 1)

        current_x += .1
        gr.add(current_x, m.sin(current_x), count)

        glColor3f(.2, .3, .9)
        gr.graph_show(count)

        pg.display.flip()
        pg.time.wait(20)


if __name__ == '__main__':
    main(800, 800)
