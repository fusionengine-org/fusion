import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame as pg

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
import fusionengine.files.ui as ui
import fusionengine.files.fonts as fonts
import fusionengine.files.debug as debug
import fusionengine.files.vector as vector
