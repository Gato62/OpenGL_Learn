import math as m
from OpenGL.GL import *

x = []
y = []


def axes(degree, ratio):
    shift = .05
    glPushMatrix()

    glRotatef(degree, 0, 0, 1)

    glBegin(GL_LINES)
    glVertex2f(-ratio, 0)
    glVertex2f(ratio, 0)
    glVertex2f(ratio, 0)
    glVertex2f((ratio - shift), 0 + shift)
    glVertex2f(ratio, 0)
    glVertex2f(ratio - shift, 0 - shift)
    glEnd()

    glPopMatrix()


def init(start, finish, count):
    dx = (finish - start) / (count - 1)

    for i in range(count):
        x.append(start)
        y.append(m.sin(start))
        start += dx


def graph_show(count):
    sx = 2 / (x[count - 1] - x[0])
    dx = (x[count - 1] + x[0]) * .5

    glPushMatrix()
    glScalef(sx, 1, 1)
    glTranslatef(-dx, 0, 0)

    glBegin(GL_LINE_STRIP)
    for i in range(count):
        glVertex2f(x[i], y[i])
    glEnd()

    glPopMatrix()


def add(new_x, new_y, count):
    for i in range(1, count):
        x.insert(i - 1, x[i])
        y.insert(i - 1, y[i])
        x.insert(i - 1, new_x)
        y.insert(i - 1, new_y)
