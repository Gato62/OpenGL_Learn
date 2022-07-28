import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def point():
    glPointSize(7)              # Point size

    glBegin(GL_POINTS)          # Draw points
    glColor3f(.9, .9, .9)       # Color points
    glVertex2f(0.0, 0.0)  # point 1
    glVertex2f(1.0, 0.0)  # point 2
    glVertex2f(0.0, 1.0)  # point 3
    glEnd()


def edge():
    glLineWidth(2)              # Line size

    glBegin(GL_LINE_LOOP)       # Draw lines
    glColor3f(.2, .2, .2)       # Color points
    glVertex2f(0.0, 0.0)  # point 1
    glVertex2f(1.0, 0.0)  # point 2
    glVertex2f(0.0, 1.0)  # point 3
    glEnd()


def triangle():
    glBegin(GL_TRIANGLES)      # Draw triangle
    glColor3f(.1, .2, .4), glVertex2f(0.0, 0.0)  # point 1
    glColor3f(.1, .7, .2), glVertex2f(1.0, 0.0)  # point 2
    glColor3f(.7, .3, .2), glVertex2f(0.0, 1.0)  # point 3
    glEnd()


def main(width, height):
    pygame.init()
    display = (width, height)                                  # Display resolution
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)   # Perspective


    while True:
        for event in pygame.event.get():                        # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(.0, .0, .05, .0)                            # Color of the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      # Screen cleaning

        glLoadIdentity()
        glScalef(.5, .5, 1)
        glTranslatef(.2, .2, .0)

        for index in range(220):
            # glLoadIdentity()                                        # Coordinate reset
            glPushMatrix()
            glScalef(.8, .8, 1)
            glRotatef(23 * index - index, 0, 0, 1)
            glTranslatef(.1, .5, .0)
            triangle()
            glPopMatrix()



        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == '__main__':
    main(1000, 1000)
