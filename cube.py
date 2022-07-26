import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def cube():
    vertices = (
        (0.0, 0.0, 0.0),  # 0
        (0.0, 2.0, 0.0),  # 1
        (2.0, 2.0, 0.0),  # 2
        (2.0, 0.0, 0.0),  # 3
        (2.0, 2.0, 2.0),  # 4
        (2.0, 0.0, 2.0)   # 5

    )

    edges = (
        (0, 1),
        (0, 3),
        (1, 2),
        (2, 3),
        (3, 5),
        (5, 4),
        (4, 2)
    )

    surfaces = (
        (0, 1, 2, 3),
        (3, 5, 4, 2)
    )

    colors = (
        (.7, .4, .2)
    )

    glPointSize(10)
    glColor3fv((.8, .8, .8))

    # glBegin(GL_POINTS)
    # for point in int(points):
    #     for vertex in point:
    #         glVertex3fv(vertices[vertex])
    # glEnd()

    glLineWidth(8)
    glColor3fv((.1, .1, .1))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((colors))
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)
    glTranslatef(.5, -1, -10)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(2, 0, 8, 0)
        glTranslatef(-.05, 0, -.02)

        glClearColor(.2, .2, .3, .0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cube()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
