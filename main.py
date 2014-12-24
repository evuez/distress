# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
from pyglet.window import key, Window
from stuff import WINDOW_WIDTH, WINDOW_HEIGHT
from stuff import MAP_WIDTH, MAP_HEIGHT
from stuff import LOG_WIDTH, LOG_HEIGHT
from tiles import Map
from tiles import Log


# Create window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1.0)

# Enable alpha channel
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)

# Create tiles
map_ = Map(MAP_WIDTH, MAP_HEIGHT)
log = Log(LOG_WIDTH, LOG_HEIGHT, MAP_WIDTH, 0)


@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	# Draw tiles
	map_.draw()
	log.draw()

from random import random
@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.UP:
		log.scroll(10)
	if symbol == key.DOWN:
		log.scroll(-10)
	if symbol == key.RIGHT:
		log.update("test" + str(random()))

pyglet.app.run()
