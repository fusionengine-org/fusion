class _CustomVector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class _CustomVectorEntity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# Not needed for now
class _CustomVector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vectors:
    def __init__(self):
        pass

    def new_vector2d(self, x, y):
        return _CustomVector2D(x, y)

    def _new_vector3d(self, x, y, z):
        return _CustomVector3D(x, y, z)
