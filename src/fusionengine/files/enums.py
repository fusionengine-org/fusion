from enum import Enum


class BodyType(Enum):
    """Class that stores all the body types. (Not for the user)"""

    RIGID_BODY = "rigid body"
    STATIC_BODY = "static body"


class RendererFlag(Enum):
    """Class that stores all the renderer flags. (Not for the user)"""

    PREVENT_SYNC = "prevent sync"
    SOFTWARE = "software"
    TARGET_TEXTURE = "target texture"
