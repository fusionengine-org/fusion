from enum import Enum

class BodyType(Enum):
    RIGID_BODY = "rigid body"
    STATIC_BODY = "static body"

class RendererFlag(Enum):
    PREVENT_SYNC = "prevent sync"
    SOFTWARE = "software"
    TARGET_TEXTURE = "target texture"
