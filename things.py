# -*- coding: utf-8 -*-


from random import choice
from random import randint
from sys import modules
from stuff import CELL_SIZE
from stuff import matrix_distance
from stuff import shuffle_matrix
from stuff import matrix_size
from stuff import lighten
from stuff import rectangle
from stuff import hex_to_rgb
from stuff import Point
from stuff import NotFertileError


class Thing(object):
	"""
	Every thing as only one color, and are
	represented by a matrix of any size.
	 - MATRIX is a tuple of tuple(s) of heights (0 being the ground). The
	number of rows and columns must be an odd number.
	 - COLOR is the base color of the thing, real color is calculated
	using heights. It must contain the alpha channel.
	 - SHUFFLE allows to shuffle the matrix before rendering it
	 - DENSITY is the density of the thing on the map, max is 100
	 - SURROUNDING is a dict of things that must be around for this
	thing to exist: {thing1: distance_max, thing2: ...} (with max distance
	in cells)
	 - GROWS sets everything that can "grow" on that thing
	 - location set the top left corner of the first cell of the thing.
	"""
	MATRIX = None
	COLOR = None
	SHUFFLE = False
	DENSITY = None
	SURROUNDING = None
	GROWS = None

	def __init__(self, x=0, y=0):
		self._location = Point(x, y)
		if self.SHUFFLE:
			self.MATRIX = shuffle_matrix(self.MATRIX)

	@property
	def x(self):
		return self._location.x
	@x.setter
	def x(self, value):
		self._location = Point(value, self.y)

	@property
	def y(self):
		return self._location.y
	@y.setter
	def y(self, value):
		self._location = Point(self.x, value)

	def draw(self):
		# Optimize later, uses vertex lists and per-thing-type-batches
		# to draw
		for y, row in enumerate(self.MATRIX):
			for x, height in enumerate(row):
				if height is None:
					continue
				dist = matrix_distance(0, 0, x, y, CELL_SIZE)
				self._draw_cell(
					lighten(self.COLOR, height),
					self.x + dist[0],
					self.y + dist[1]
				)

	def _draw_cell(self, color, x1, y1):
		x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
		rectangle(color, x1, y1, x2, y2)

	def grow(self, size, x, y):
		if not self.GROWS:
			return []
		thing = getattr(modules[__name__], choice(self.GROWS))(x, y)
		thing.SIZE = matrix_size(thing.MATRIX, CELL_SIZE)
		if thing.SIZE[0] < size[0]:
			thing.x += (size[0] - thing.SIZE[0]) / 2
		if thing.SIZE[1] < size[1]:
			thing.y += (size[1] - thing.SIZE[1]) / 2
		if randint(0, 100) > thing.DENSITY:
			raise NotFertileError(self, thing) # Stop from top to bottom of the pile if no inner GROWS
		things = [thing]
		try:
			things.extend(thing.grow(size, x, y))
		except NotFertileError, e:
			pass
		return things


class Tree(Thing):
	pass


class Ground(Thing):
	"""
	Things can be placed on top of any ground
	"""
	pass


class Soil(Ground):
	MATRIX = [
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
	]
	COLOR = hex_to_rgb('241105ff')
	SHUFFLE = True
	DENSITY = 100 # Not taken into account anyway: Soil everywhere
	GROWS = ['Pine', 'Rock', 'Lake', 'Pine', 'Bush']


class Rock(Ground):
	MATRIX = [
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
	]
	COLOR = hex_to_rgb('2d3939ff')
	SHUFFLE = True
	DENSITY = 40
	GROWS = ['Pine', 'Bush']


class Water(Thing):
	pass


class Lake(Water):
	MATRIX = [
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.0, 1.1, 1.2],
	]
	COLOR = hex_to_rgb('001442ff')
	DENSITY = 20
	SHUFFLE = True


class Pine(Tree):
	MATRIX = [
		[None, None, None, None, None,    1, None, None, None, None, None],
		[None, None, None, None,    1,    1,    1, None, None, None, None],
		[None, None, None,    1,    1,    2,    1,    1, None, None, None],
		[None, None,    1,    1,    2,    2,    2,    1,    1, None, None],
		[None,    1,    1,    2,    2,    3,    2,    2,    1,    1, None],
		[   1,    1,    2,    2,    3,    4,    3,    2,    2,    1,    1],
		[None,    1,    1,    2,    2,    3,    2,    2,    1,    1, None],
		[None, None,    1,    1,    2,    2,    2,    1,    1, None, None],
		[None, None, None,    1,    1,    2,    1,    1, None, None, None],
		[None, None, None, None,    1,    1,    1, None, None, None, None],
		[None, None, None, None, None,    1, None, None, None, None, None],
	]
	COLOR = hex_to_rgb('001f08ff')
	DENSITY = 100
	SHUFFLE = False


class Bush(Tree):
	MATRIX = [
		[1.0, 1.2, 1.4, 1.6, 1.8],
		[1.0, 1.2, 1.4, 1.6, 1.8],
		[1.0, 1.2, 1.4, 1.6, 1.8],
		[1.0, 1.2, 1.4, 1.6, 1.8],
		[1.0, 1.2, 1.4, 1.6, 1.8],
	]
	COLOR = hex_to_rgb('00380eff')
	SHUFFLE = True
	DENSITY = 40
	SURROUNDING = {'Lake': 10}
	GROWS = ['Cranberry']


class Cranberry(Tree):
	MATRIX = [
		[None, None, None, None, None],
		[1.0, None, None, None, None],
		[1.0, None, None, None, None],
		[1.0, None, None, None, None],
		[1.0, None, None, None, None],
	]
	COLOR = hex_to_rgb('770124ff')
	SHUFFLE = True
	DENSITY = 30


class Body(Thing):
	pass


class Orphon(Body):
	"""
	The hero
	"""
	MATRIX = [
		[1, 1],
		[1, 1]
	]
	COLOR = hex_to_rgb('05ffeeff')


class Phampled(Body):
	"""
	The lost one
	"""
	MATRIX = [
		[1, 1],
		[1, 1]
	]
	COLOR = hex_to_rgb('ff6905ff')
