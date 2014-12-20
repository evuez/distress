# -*- coding: utf-8 -*-


from things import *
from stuff import rectangle




class Map(object):
	THINGS = [
		Soil,
		Rock,
		Gravel,
		Bush,
		Pine,
	]

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def draw(self):
		rectangle(
			(1, 1, 1, 1),
			0, 0,
			self.width, self.height
		)
