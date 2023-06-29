from src.engine.files.enums import BodyType
from src.engine.files.imports import *
import src.engine.files.data as data

class _RigidBody:
    def __init__(self, window, x, y, width, height):
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
        
class _StaticBody:
    def __init__(self, window, x, y, width, height):
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
    
class Entity: 
    def __init__(self, bodytype, window, x, y, width, height):
        self.image = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self._setBodyType(bodytype)
    
    def openImage(self, window, image, x, y, width, height):
        image.openImage(window, image, x, y, width, height)
        self.image = image
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def newRect(self, window, color):
        data.drawRect(self.window,
                      self.x,
                      self.y,
                      self.width,
                      self.height,
                      color
                      )
    def setGravity(self, gravity):
        self.gravity = gravity
    
    def _setBodyType(self, bodytype):
        if bodytype == BodyType.RIGID_BODY:
            self.body = _RigidBody(self.window,
                                   self.x,
                                   self.y,
                                   self.width,
                                   self.height
                                   )
        elif bodytype == BodyType.STATIC_BODY:
            self.body = _StaticBody(self.window,
                                    self.x,
                                    self.y,
                                    self.width,
                                    self.height
                                    )
