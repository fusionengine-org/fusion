from fusionengine.engine.physics import Staticbody
from fusionengine.engine.vector import Vector2D


class Node:
    def __init__(
        self,
        x: int,
        y: int,
        node_type,
        body_type=Staticbody,
    ):
        self.x = x
        self.y = y
        self.x = node_type.x
        self.y = node_type.y
        self.body_type = body_type
        self.node_type = node_type

    pass

    def get_coord_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def get_vec2_coord(self) -> Vector2D:
        return Vector2D(self.x, self.y)
