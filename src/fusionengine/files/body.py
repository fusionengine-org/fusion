import fusionengine.files.data as data

from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *

class _RigidBody:
    def __init__(self, window, x: int, y: int, width: int, height: int) -> None:
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
        
class _StaticBody:
    def __init__(self, window, x: int, y: int, width: int, height: int) -> None:
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
    
class Entity: 
    def __init__(self, bodytype: BodyType, window, x: int, y: int, width: int, height: int) -> None:
        self.image = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self._setBodyType(bodytype)
    
    def openImage(self, window, image, x: int, y: int, width: int, height: int) -> None:
        image.openImage(window, image, x, y, width, height)
        self.image = image
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def newRect(self, window, color: tuple) -> None:
        data.drawRect(self.window,
                      self.x,
                      self.y,
                      self.width,
                      self.height,
                      color
                      )
    def setGravity(self, gravity: int) -> None:
        self.gravity = gravity
    
    def _setBodyType(self, bodytype: BodyType) -> None:
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
