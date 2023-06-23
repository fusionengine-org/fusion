import warnings
with warnings.catch_warnings():	
	warnings.simplefilter("ignore")
	from sdl2 import *
	import sdl2
	import sdl2.ext
import ctypes
import pymunk
import time
import src.engine.files.window as window
import src.engine.files.draw as draw
import src.engine.files.color as color
import src.engine.files.event as event
import src.engine.files.image as image
import src.engine.files.body as body
import src.engine.files.shape as shape



