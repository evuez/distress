# -*- coding: utf-8 -*-

import json
import logging
from logging import StreamHandler
from logging import FileHandler
from logging import Formatter
from functools import wraps


class LiveStream(object):
	def write(self, data):
		decoded = json.loads(data)
		print decoded

	def flush(self):
		pass


logs = {
	'live': {
		'handler': StreamHandler(LiveStream()),
		'formatter': Formatter("""{
			"level": "%(levelname)s",
			"message": "%(message)s"
		}"""),
	},
	'file': {
		'handler': FileHandler('diary.log'),
		'formatter': Formatter('%(asctime)s - %(levelname)s - %(message)s'),
	}
}

logger = logging.getLogger('distress')
logger.setLevel(logging.INFO)

for info in logs.values():
	info['handler'].setFormatter(info['formatter'])
	logger.addHandler(info['handler'])


def debug(message):
	def log(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			logger.debug(message)
			return func(*args, **kwargs)
		return wrapper
	return log


def info(message):
	def log(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			logger.info(message)
			return func(*args, **kwargs)
		return wrapper
	return log


def error(message):
	def log(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			logger.error(message)
			return func(*args, **kwargs)
		return wrapper
	return log


def warning(message):
	def log(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			logger.warning(message)
			return func(*args, **kwargs)
		return wrapper
	return log


def critical(message):
	def log(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			logger.critical(message)
			return func(*args, **kwargs)
		return wrapper
	return log
