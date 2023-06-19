from src.engine.files.imports import *

class _RigidBody:
    def __init__(self, window, x, y, width, height):
        self.body = data.DataBodies(window, x, y, width, height)
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
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.window = window
        self.gravity = 0
        self._setBodyType(bodytype)
    
    def openImage(self, window, image, x, y, width, height):
        image.openImage(window, image, x, y, width, height)
        self.image = image
        self.window = window
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        
    def setGravity(self, gravity):
        self.gravity = gravity
    
    def _setBodyType(self, bodytype):
        if bodytype == "rigid" or bodytype == "Rigid":
            self.body = _RigidBody(self.window, self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        else:
            self.body = _StaticBody(self.window, self.rect.x, self.rect.y, self.rect.width, self.rect.height)
