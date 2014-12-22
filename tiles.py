# -*- coding: utf-8 -*-


import things
from things import Soil
from things import Thing
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
	LAYERS = {
		'soil': OrderedGroup(0),
		'ground': OrderedGroup(1),
		'bodies': OrderedGroup(2),
		'trees': OrderedGroup(3),
		'berries': OrderedGroup(4)
	}

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self._map = Batch()

		Soil.SIZE = matrix_size(Soil.MATRIX, CELL_SIZE)

		for x in xrange(0, self.width, Soil.SIZE[0]):
			for y in xrange(0, self.height, Soil.SIZE[1]):
				soil = Soil(x, y)
				self.add(soil)
				try:
					soil.grow(self, Soil.SIZE, x, y)
				except NotFertileError, e:
					logger.debug(str(e))


	# def add_hero(self, body_name):
	# 	getattr(things, body_name)

	# def add_lost(self, body_name):
	# 	pass

	# def _add_body(self, body_name):
	# 	getattr(things, body_name)(pos)

	def add(self, thing):
		self._map.add(
			len(thing.vertices) / 2,
			GL_QUADS,
			self.LAYERS[thing.LAYER],
			('v2i', thing.vertices),
			('c4B', thing.colors)
		)

	def draw(self):
		hero = things.Orphon(100, 100)
		self.add(hero)

		self._map.draw()


