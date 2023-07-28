import fusionengine.files.data as data
import fusionengine.files.window as window
from fusionengine.files.enums import BodyType
from fusionengine.files.imports import *
import fusionengine.files.image as image_fe
import fusionengine.files.draw as draw_fe


class _RigidBody:
    def __init__(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int
    ) -> None:
        """A class that creates a new rigid body. (Not for the user)"""
        self._body = data._DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space


class _StaticBody:
    def __init__(
        self, window: window._CustomRenderer, x: int, y: int, width: int, height: int
    ) -> None:
        """A class that creates a new static body. (Not for the user)"""
        self._body = data._DataBodies(window, x, y, width, height)
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = self._body.body
        self.space = self._body.space


class Entity:
    def __init__(
        self, bodytype: str, window: window._CustomRenderer, x: int, y: int, width: int, height: int
    ) -> None:
        """A class that creates a new entity."""
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
            self.body = _RigidBody(self.window, self.x, self.y, self.width, self.height)
        else:
            self.body = _StaticBody(self.window, self.x, self.y, self.width, self.height)
        self._addspace.append(self.body.body)
        self._set_body_data(self.x, self.y, self.width, self.height, self.body.space)
        self.box = pymunk.Poly.create_box(self.body.body)
        self._addspace.append(self.box)

        self._addspaces()

    def image(
        self,
        window: window._CustomRenderer,
        image_path: str,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """Gives the entity an image and laters draws it on the screen."""
        drawimage = self.image_fe.open_image(window, image_path, x, y, width, height)
        self.image_fe.draw_image(drawimage)
        self.image_path = image_path
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def new_rect(self, window: window._CustomRenderer, color: tuple) -> None:
        """Gives the entity a rectangle and later draws it on the screen."""
        self.draw_fe.draw_rect(window, self.x, self.y, self.width, self.height, color)

    def set_gravity(self, gravity: int) -> None:
        """Sets the gravity of the entity."""
        self.gravity = gravity
        self.body.space.gravity = self.gravity

    def set_mass(self, mass: int) -> None:
        """Sets the mass of the entity."""
        self.box.mass = mass

    def _set_body_data(self, x, y, width, height, space) -> None:
        """Function that sets the body data. (Not for the user)"""
        space.position = x, y

    def _addspaces(self) -> None:
        """Function that adds the spaces to the body list. (Not for the user)"""
        for space in self._addspace:
            self.body.space.add(space)
