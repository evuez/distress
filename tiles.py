# -*- coding: utf-8 -*-


import things
from logger import logger
from things import Soil
from stuff import Point
from stuff import rectangle
from stuff import matrix_distance
from stuff import matrix_size
from stuff import CELL_SIZE
from stuff import NotFertileError
from random import randint
from random import choice



class Map(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.map = []

		Soil.SIZE = matrix_size(Soil.MATRIX, CELL_SIZE)

		for x in xrange(0, self.width, Soil.SIZE[0]):
			for y in xrange(0, self.height, Soil.SIZE[1]):
				soil = Soil(x, y)
				self.map.append(soil)
				try:
					self.map.extend(soil.grow(Soil.SIZE, x, y))
				except NotFertileError, e:
					logger.error(str(e))


	def draw(self):
		for thing in self.map:
			thing.draw()
