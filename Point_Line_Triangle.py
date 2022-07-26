import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def point():
    glPointSize(7)              # Point size

    glBegin(GL_POINTS)          # Draw points
    glColor3f(.9, .9, .9)       # Dolor points

    glVertex3f(0.0, 0.0, 0.0)   # point 1
    glVertex3f(0.0, 1.0, 0.0)   # point 2
    glVertex3f(1.0, 1.0, 0.0)   # point 3
    glVertex3f(1.0, 0.0, 0.0)   # point 4
    glEnd()


def edge():
    glLineWidth(2)              # Point size

    glBegin(GL_LINE_LOOP)       # Draw points
    glColor3f(.2, .2, .2)       # Dolor points

    glVertex3f(0.0, 0.0, 0.0)   # point 1
    glVertex3f(0.0, 1.0, 0.0)   # point 2
    glVertex3f(1.0, 1.0, 0.0)   # point 3
    glVertex3f(1.0, 0.0, 0.0)   # point 4
    glEnd()


def triangle():
    glBegin(GL_TRIANGLES)       # Draw triangle
    glColor3f(.2, .6, .2)       # Dolor points

    glVertex3f(0.0, 0.0, 0.0)   # point 1
    glColor3f(.1, .2, .7)
    glVertex3f(0.0, 1.0, 0.0)   # point 2
    glColor3f(.7, .3, .1)
    glVertex3f(1.0, 1.0, 0.0)   # point 3
    glEnd()


def main(width, height):
    pygame.init()
    display = (width, height)                                   # Display resolution
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)    # Perspective

    glTranslatef(-.4, -0.5, -2.0)

    while True:
        for event in pygame.event.get():                        # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(.4, .4, .4, .0)                            # Color of the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      # Screen

# Draw objects

        edge()
        triangle()
        point()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main(800, 600)
