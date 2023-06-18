from src.engine.files.imports import *

class _RigidBody:
    def __init__(self, window, x, y, width, height):
        self.body = data.DataBodies(window, x, y, width, height)
        
class _StaticBody:
    def __init__(self, window, x, y, width, height):
        self.space = pymunk.Space()
    
class Entity:
    def __init__(self, bodytype, window, x, y, width, height):
        self.image = None
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.window = window
    
    def openImage(self, window, image, x, y, width, height):
        image.openImage(window, image, x, y, width, height)
        self.image = image
        self.window = window
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        
        
    def setGravity(self, gravity):
        pass
    
    def _setBodyType(self, bodytype):
        pass
