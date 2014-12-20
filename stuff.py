# -*- coding: utf-8 -*-

from collections import namedtuple
from copy import deepcopy
from math import sqrt
from random import shuffle
from struct import unpack
from pyglet.gl import glBegin
from pyglet.gl import glColor4f
from pyglet.gl import glVertex2f
from pyglet.gl import glEnd
from pyglet.gl import GL_POLYGON


Point = namedtuple('Point', 'x y')


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

MAP_WIDTH = 900
MAP_HEIGHT = WINDOW_HEIGHT

CELL_SIZE = 4


def lighten(color, scale=1.0):
	"""
	Lighten a color.
	 - color is a tuple (r, g, b, a)
	 - scale can be any number, if < 1, color will be darken
	"""
	return map(
		lambda x: min(max(x * scale, 0), 1),
		color[:3]
	) + list(color[3:])


def hex_to_rgb(hex_):
	return [v / 255.0 for v in unpack('BBBB', hex_.decode('hex'))]


def matrix_distance(x1, y1, x2, y2, ratio=1):
	return [n * ratio for n in (x2 - x1 , y2 - y1)]


def shuffle_matrix(matrix, rows_only=False):
	"""
	Perform in-place shuffling
	"""
	matrix = deepcopy(matrix)
	if not rows_only:
		shuffle(matrix)
	for row in matrix:
		shuffle(row)
	return matrix


def distance(x1, y1, x2, y2, ratio=1):
	return sqrt(sum([n**2 for n in matrix_distance(x1, y1, x2, y2, ratio)]))


def rectangle(color, x1, y1, x2, y2):
	glColor4f(*color)
	glBegin(GL_POLYGON)
	glVertex2f(x1, y1)
	glVertex2f(x1, y2)
	glVertex2f(x2, y2)
	glVertex2f(x2, y1)
	glEnd()
