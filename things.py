# -*- coding: utf-8 -*-


from pyglet.sprite import Sprite


class Thing(object):
	"""
	Every thing as only one color, and are
	represented by a matrix of any size.
	 - MATRIX is a tuple of tuple(s) of heights (0 being the ground).
	 - COLOR is the base color of the thing, real color is calculated
	using heights
	"""
	MATRIX = None
	COLOR = None


class Tree(Thing):
	pass


class Pine(Tree):
	MATRIX = [
		[None, None, None, None, None,    1, None, None, None, None, None],
		[None, None, None, None,    1,    2,    1, None, None, None, None],
		[None, None, None,    1,    2,    3,    2,    1, None, None, None],
		[None, None,    1,    2,    3,    4,    3,    2,    1, None, None],
		[None,    1,    2,    3,    4,    5,    4,    3,    2,    1, None],
		[   1,    2,    3,    4,    5,    6,    5,    4,    3,    2,    1],
		[None,    1,    2,    3,    4,    5,    4,    3,    2,    1, None],
		[None, None,    1,    2,    3,    4,    3,    2,    1, None, None],
		[None, None, None,    1,    2,    3,    2,    1, None, None, None],
		[None, None, None, None,    1,    2,    1, None, None, None, None],
		[None, None, None, None, None,    1, None, None, None, None, None],
	]
	COLOR = (1, 121, 111)
