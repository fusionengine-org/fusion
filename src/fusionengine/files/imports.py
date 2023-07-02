import warnings

with warnings.catch_warnings():	
	warnings.simplefilter("ignore")
	from sdl2 import *
	import sdl2
	import sdl2.ext

import ctypes
import time

import pymunk

import fusionengine.files.body as body
import fusionengine.files.color as color
import fusionengine.files.draw as draw
import fusionengine.files.event as event
import fusionengine.files.image as image
import fusionengine.files.shape as shape
import fusionengine.files.window as window
