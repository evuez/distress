# -*- coding: utf-8 -*-


from things import *
from stuff import Point
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

		self.map = []
		for x in range(0, 8):
			for y in range(0, 8):
				self.map.append(Soil(Point(x * 10, y * 10)))

	def draw(self):
		for m in self.map:
			m.draw()
