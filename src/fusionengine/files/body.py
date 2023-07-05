import fusionengine.files.data as data
import fusionengine.files.window as window
from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *
import fusionengine.files.image as image

class _RigidBody:
    def __init__(self, window: window._CustomRenderer, x: int, y: int, width: int, height: int) -> None:
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
        
class _StaticBody:
    def __init__(self, window: window._CustomRenderer, x: int, y: int, width: int, height: int) -> None:
        self._body = data.DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space
    
class Entity: 
    def __init__(self, bodytype: BodyType, window: window._CustomRenderer, x: int, y: int, width: int, height: int) -> None:
        self.image = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self._set_body_type(bodytype)
    
    def open_image(self, window: window._CustomRenderer, image: image._CustomImage, x: int, y: int, width: int, height: int) -> None:
        image.open_image(window, image, x, y, width, height)
        self.image = image
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def new_rect(self, window: window._CustomRenderer, color: tuple) -> None:
        data.draw_rect(window,
                      self.x,
                      self.y,
                      self.width,
                      self.height,
                      color
                      )
    def set_gravity(self, gravity: int) -> None:
        self.gravity = gravity
    
    def _set_body_type(self, bodytype: BodyType) -> None:
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
