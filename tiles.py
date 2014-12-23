# -*- coding: utf-8 -*-


import things
from things import Soil
from logger import logger
from logger import debug, info, error, warning, critical
from stuff import matrix_size
from stuff import CELL_SIZE
from stuff import BODY_HERO
from stuff import BODY_LOST
from stuff import START_POS
from stuff import NotFertileError
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
		self._create()
		self._add_hero()
		self._add_lost()


	def _create(self):
		for x in xrange(0, self.width, Soil.size()[0]):
			for y in xrange(0, self.height, Soil.size()[1]):
				soil = Soil(x, y)
				self.add(soil)
				try:
					soil.grow(self, x, y)
				except NotFertileError, e:
					logger.debug(str(e))

	def add(self, thing):
		thing.vertex_list = self._map.add(
			len(thing.vertices) / 2,
			GL_QUADS,
			self.LAYERS[thing.LAYER],
			('v2i/dynamic', thing.vertices),
			('c4B/static', thing.colors)
		)
		return thing.vertex_list

	def _add_body(self, body_name, kind):
		body = getattr(things, body_name)(*START_POS[kind])
		setattr(self, kind, body)
		self.add(body)
		return body

	@info("Adding {}".format(BODY_HERO))
	def _add_hero(self):
		self._add_body(BODY_HERO, 'hero')

	@info("Hiding {}".format(BODY_LOST))
	def _add_lost(self):
		self._add_body(BODY_LOST, 'lost') # keep a list of every tree to hide him

	def draw(self):
		self._map.draw()


