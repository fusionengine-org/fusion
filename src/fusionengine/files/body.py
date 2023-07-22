import fusionengine.files.data as data
import fusionengine.files.window as window
from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *
import fusionengine.files.image as image_fe
import fusionengine.files.draw as draw_fe

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
    def __init__(self, bodytype: str, window: window._CustomRenderer, x: int, y: int, width: int, height: int) -> None:
        self._addspace = []
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        self.gravity = 0
        self.image_fe = image_fe.Image()
        self.draw_fe = draw_fe.Draw()

        if bodytype == BodyType.RIGID_BODY:
            self.body = _RigidBody(self.window,
                                   self.x,
                                   self.y,
                                   self.width,
                                   self.height
                                   )
        else:
            self.body = _StaticBody(self.window,
                                    self.x,
                                    self.y,
                                    self.width,
                                    self.height
                                    )
        self._addspace.append(self.body.body)
        self._set_body_data(self.x, self.y, self.width, self.height, self.body.space)
        self.box = pymunk.Poly.create_box(self.body.body)
        self._addspace.append(self.box)

        self._addspaces()

    def image(self, window: window._CustomRenderer, image_path: str, x: int, y: int, width: int, height: int) -> None:
        drawimage = self.image_fe.open_image(window, image, x, y, width, height)
        self.image_fe.draw_image(drawimage)
        self.image_path = image_path
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def new_rect(self, window: window._CustomRenderer, color: tuple) -> None:
        self.draw_fe.draw_rect(window,
                      self.x,
                      self.y,
                      self.width,
                      self.height,
                      color
                      )
    def set_gravity(self, gravity: int) -> None:
        self.gravity = gravity
        self.body.space.gravity = self.gravity

    def set_mass(self, mass: int) -> None:
        self.box.mass = mass

    def _set_body_data(self, x, y, width, height, space) -> None:
        space.position = x, y

    def _addspaces(self) -> None:
        for space in self._addspace:
            self.body.space.add(space)
