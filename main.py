# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
from pyglet.window import key, Window
from stuff import WINDOW_WIDTH, WINDOW_HEIGHT
from stuff import MAP_WIDTH, MAP_HEIGHT


window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1.0)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)


from tiles import Map

@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	Map(MAP_WIDTH, MAP_HEIGHT).draw()


pyglet.app.run()
