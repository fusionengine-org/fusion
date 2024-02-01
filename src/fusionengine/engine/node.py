from pymunk import Constraint
from fusionengine.engine.physics import STATICBODY
from fusionengine.engine.shape import Rect
from fusionengine.engine.image import Image
from fusionengine.engine.vector import Vector2D


class Node:
    def __init__(
        self, x: int, y: int, node_type: Rect | Image, body_type: int = STATICBODY
    ):
        self.x = x
        self.y = y
        self.x = node_type.x
        self.y = node_type.y
        self.node_type = node_type
        self.body_type = body_type

    def get_coord_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def get_coord_vec2(self) -> Vector2D:
        return Vector2D(self.x, self.y)

    def get_node_type(self):
        return type(self.node_type)

    def get_body_type(self):
        return type(self.body_type)

    def draw(self):
        self.node_type.draw()

    def update(self):
        # Todo
        pass
