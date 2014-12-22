# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
from pyglet.window import key, Window
from stuff import WINDOW_WIDTH, WINDOW_HEIGHT
from stuff import MAP_WIDTH, MAP_HEIGHT
from tiles import Map


# Create window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1.0)

# Enable alpha channel
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)

# Create map
map_ = Map(MAP_WIDTH, MAP_HEIGHT)


@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	# Draw map
	map_.draw()

from stuff import CELL_SIZE
@window.event
def on_key_press(symbol, modifiers):
	unit = CELL_SIZE
	if symbol == key.UP:
		map_.hero.move(0, unit)
	if symbol == key.DOWN:
		map_.hero.move(0, -unit)
	if symbol == key.RIGHT:
		map_.hero.move(unit, 0)
	if symbol == key.LEFT:
		map_.hero.move(-unit, 0)


pyglet.app.run()
