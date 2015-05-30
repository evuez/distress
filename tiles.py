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
from threading import Thread
from pyglet.graphics import Batch
from pyglet.graphics import OrderedGroup
from pyglet.gl import GL_QUADS
from pyglet.text import decode_text
from pyglet.text import Label
from pyglet.text.layout import ScrollableTextLayout
from pyglet.clock import schedule_interval



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
		for x in range(0, self.width, Soil.size()[0]):
			for y in range(0, self.height, Soil.size()[1]):
				soil = Soil(x, y)
				self.add(soil)
				try:
					soil.grow(self, x, y)
				except NotFertileError as e:
					logger.debug(str(e))

	def add(self, thing):
		thing.vertex_list = self._map.add(
			len(thing.vertices) // 2,
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


class Log(object):
	GROUPS = {
		'text_bac'
	}

	def __init__(self, width, height, x, y, queue):
		self.width = width
		self.height = height
		self._log = Batch()
		self._create(x, y)
		self.queue = queue

	def _create(self, x, y):
		self._title = Label(
			"_______________ LOG _______________",
			x=x,
			y=y + self.height + 5,
			height=20,
			batch=self._log
		)
		self._doc = decode_text("\n")
		self._doc.set_style(0, 0, dict(color=(255, 255, 255, 255)))

		self._box = ScrollableTextLayout(
			self._doc, self.width, self.height,
			multiline=True, batch=self._log
		)
		self._box.x = x
		self._box.y = y

	def draw(self):
		self._log.draw()

	def insert(self, message):
		self._doc.insert_text(-1, message + "\n")
		self._box.view_y = -self._box.content_height

	def scroll(self, height):
		self._box.view_y += height

	def start(self):
		schedule_interval(self.update, 0.3)

	def update(self, dt):
		try:
			item = self.queue.popleft()
			self.insert(item['message'])
		except IndexError:
			pass
