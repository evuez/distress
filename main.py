# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
from pyglet.window import key, Window
from stuff import WINDOW_WIDTH, WINDOW_HEIGHT


window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1.0)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)

@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	glColor4f(1.0, 0.0, 0.0, 0.4);
	glBegin(GL_POLYGON)
	glVertex2f(0, 0)
	glVertex2f(0, 100)
	glVertex2f(100, 100)
	glVertex2f(100, 0)
	glEnd()


pyglet.app.run()
