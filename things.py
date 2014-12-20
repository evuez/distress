# -*- coding: utf-8 -*-


from stuff import THING_SIZE
from stuff import matrix_distance
from stuff import shuffle_matrix
from stuff import lighten
from stuff import rectangle
from stuff import hex_to_rgb


class Thing(object):
	"""
	Every thing as only one color, and are
	represented by a matrix of any size.
	 - MATRIX is a tuple of tuple(s) of heights (0 being the ground). The
	number of rows and columns must be an odd number. Note that they are
	rotated 90 degrees counterclockwise.
	 - COLOR is the base color of the thing, real color is calculated
	using heights. It must contain the alpha channel.
	 - SHUFFLE allows to shuffle the matrix before rendering it
	 - DENSITY is the density of the thing on the map, max is 100
	 - location set the top left corner of the first cell of the thing.
	"""
	MATRIX = None
	COLOR = None
	SHUFFLE = False
	DENSITY = None

	def __init__(self, location):
		self.location = location
		if self.SHUFFLE:
			self.MATRIX = shuffle_matrix(self.MATRIX)

	def draw(self):
		for x, row in enumerate(self.MATRIX):
			for y, height in enumerate(row):
				if height is None:
					continue
				dist = matrix_distance(0, 0, x, y, THING_SIZE)
				self._draw_cell(
					lighten(self.COLOR, height),
					self.location.x + dist[0],
					self.location.y + dist[1]
				)


	def _draw_cell(self, color, x1, y1):
		x2, y2 = x1 + THING_SIZE, y1 + THING_SIZE
		rectangle(color, x1, y1, x2, y2)


class Tree(Thing):
	pass


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
	DENSITY = 30


class Bush(Tree):
	MATRIX = [
		[1.3, 1.2, 1.1, 1.9],
		[  1, 1.5, 1.3,   1],
		[1.4, 1.2,   2, 1.3],
		[  1, 1.6,   1, 1.8],
	]
	COLOR = hex_to_rgb('00380eff')
	SHUFFLE = True
	DENSITY = 10


class Ground(Thing):
	"""
	Things can be placed on top of any ground
	"""
	pass


class Soil(Ground):
	MATRIX = [
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
		[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
	]
	COLOR = hex_to_rgb('241105ff')
	SHUFFLE = True
	DENSITY = 100


class Rock(Ground):
	MATRIX = [
		[ 1.2, 1.3, 1.2, 2.7, 1.3, 1.9, 1.0, 1.8, 1.3],
		[ 1.6, 1.1, 2.3, 2.2, 2.9, 1.2, 1.5, 1.4, 1.2],
		[ 1.8, 2.9, 2.1, 3.7, 2.5, 2.9, 1.5, 1.3, 1.7],
		[ 2.3, 2.4, 2.8, 2.7, 2.3, 2.2, 2.5, 1.1, 1.2],
		[ 1.1, 2.2, 2.0, 3.9, 2.7, 2.9, 1.5, 1.7, 1.0],
		[ 1.3, 1.6, 2.2, 2.3, 2.5, 1.8, 1.2, 1.3, 1.4],
		[ 1.1, 1.8, 1.1, 2.9, 1.7, 1.8, 1.2, 1.1, 1.5],
		[ 1.0, 1.9, 1.8, 1.7, 1.9, 1.4, 1.1, 1.3, 1.6],
		[ 1.3, 1.1, 1.9, 1.6, 1.4, 1.5, 1.4, 1.9, 1.1],
	]
	COLOR = hex_to_rgb('2d3939ff')
	SHUFFLE = True
	DENSITY = 20

class Gravel(Ground):
	MATRIX = [[1]]
	COLOR = hex_to_rgb('232424ff')
	DENSITY = 40

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
