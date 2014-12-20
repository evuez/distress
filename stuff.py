# -*- coding: utf-8 -*-

from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

MAP_WIDTH = 400
MAP_HEIGHT = 400

THING_SIZE = 4


def color_variant(color, scale=1.0):
	"""
	Darken or lighten a color.
	 - color is a tuple (r, g, b, a)
	 - scale can be any number
	"""
	return map(
		lambda x: int(min(max(x * scale, 0), 255)),
		color[:3]
	) + list(color[3:])


def matrix_center(matrix):
	return (len(matrix) / 2, len(matrix[0]) / 2)


def matrix_distance(x1, y1, x2, y2):
	return (x2 - x1, y2 - y1)


def distance(x1, y1, x2, y2):
	return sqrt(sum([n**2 for n in matrix_distance(x1, y1, x2, y2)]))
