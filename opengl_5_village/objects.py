import math

from OpenGL.GL import *


def rectangle(dx, dy, width, height, red, green, blue):
    dx, dy, width, height = dx / 10, dy / 10, width / 10, height / 10
    red, green, blue = red / 10, green / 10, blue / 10

    glBegin(GL_QUADS)
    glColor3f(red, green, blue)

    glVertex2f(dx, dy)
    glVertex2f(dx, dy + height)
    glVertex2f(dx + width, dy + height)
    glVertex2f(dx + width, dy)
    glEnd()


def triangle(dx, dy, hypotenuse, height, red, green, blue):
    dx, dy, hypotenuse, height = dx / 10, dy / 10, hypotenuse / 10, height / 10
    red, green, blue = red / 10, green / 10, blue / 10

    glColor3f(red, green, blue)

    glBegin(GL_TRIANGLES)
    glVertex2f(dx + hypotenuse / 2, dy + height)
    glVertex2f(dx, dy)
    glVertex2f(dx + hypotenuse, dy)
    glEnd()


def house(scale, x, y):
    scale, x, y = scale / 10, x / 10, y / 10

    glPushMatrix()

    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)

    rectangle(-.5, -6, 1, 3, 6, 2, 1)
    rectangle(-4, -8, 5, 3, 8, 4, 2)        # dx, dy, width, height, red, green, blue
    rectangle(-2.5, -7, 2, 1, 6, 8, 10)
    triangle(-4.5, -5, 6, 2, 6, 4, 2)       # dx, dy, hypotenuse, height , r, g, b

    glPopMatrix()


def circle(edge, radius):
    radius = radius / 10
    a = math.pi * 2 / edge

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, .8, 0)
    glVertex2f(0, 0)

    for i in range(-1, edge):
        x = math.sin(a * i) * radius
        y = math.cos(a * i) * radius
        glVertex2f(x, y)
    glEnd()
