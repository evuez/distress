# -*- coding: utf-8 -*-


import things
from things import Soil
from logger import logger
from stuff import Point
from stuff import matrix_distance
from stuff import matrix_size
from stuff import CELL_SIZE
from stuff import BODY_HERO
from stuff import BODY_LOST
from stuff import NotFertileError
from random import randint
from random import choice
from pyglet.graphics import Batch
from pyglet.graphics import OrderedGroup
from pyglet.gl import GL_QUADS



class Map(object):
	LAYERS = [ # use dict with meaningful name for keys instead
		OrderedGroup(0),
		OrderedGroup(1),
		OrderedGroup(2),
		OrderedGroup(3),
		OrderedGroup(4)
	]

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self._map = Batch()

		Soil.SIZE = matrix_size(Soil.MATRIX, CELL_SIZE)

		for x in xrange(0, self.width, Soil.SIZE[0]):
			for y in xrange(0, self.height, Soil.SIZE[1]):
				soil = Soil(x, y)
				self._map.add(
					len(soil.vertices) / 2,
					GL_QUADS,
					self.LAYERS[soil.LAYER],
					('v2i', soil.vertices),
					('c4B', soil.colors)
				)
				try:
					soil.grow(self._map, self.LAYERS, Soil.SIZE, x, y)
				except NotFertileError, e:
					logger.debug(str(e))


	# def add_hero(self, body_name):
	# 	getattr(things, body_name)

	# def add_lost(self, body_name):
	# 	pass

	# def _add_body(self, body_name):
	# 	getattr(things, body_name)(pos)

	def draw(self):
		# for thing in self._map:
		# 	thing.draw()
		self._map.draw()

