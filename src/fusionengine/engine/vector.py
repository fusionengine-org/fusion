import math


class Vector2D:
    """
    2-element structure that can be used to represent positions in 2d.
    If there are no arguments, a zero vector will be created
    """

    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x + other[0], self.y + other[1])
        elif isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
        elif isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        else:
            return NotImplemented

        return self

    def __sub__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x - other[0], self.y - other[1])
        elif isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        if isinstance(other, tuple):
            self.x -= other[0]
            self.y -= other[1]
        elif isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        else:
            return NotImplemented

        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            return NotImplemented

        return self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
        else:
            return NotImplemented

        return self

    def normalize(self) -> None:
        """
        The method normalizes this vector and displays the unit vector.
        """
        magnitude = math.sqrt(self.x**2 + self.y**2)
        self.x = self.x / abs(magnitude)
        self.y = self.y / abs(magnitude)

    def from_tuple(self, value: tuple[int, int] | tuple[float, float]) -> None:
        """
        Setting vector values from tuple
        Args:
            value (tuple): A value that allows you to get values for a vector
        """

        self.x, self.y = value

    def get_tuple(self) -> tuple[int, int]:
        """
        Get vector values (int)
        Returns:
            tuple[int, int]: x and y values
        """

        return int(self.x), int(self.y)

    def get_tuplef(self) -> tuple[float, float]:
        """
        Get vector values (float)
        Returns:
            tuple[float, float]: x and y values
        """

        return float(self.x), float(self.y)


class Vector3D:
    """
    3-element structure that can be used to represent positions in 3d.
    If there are no arguments, a zero vector will be created
    """

    def __init__(self, x: int | float = 0, y: int | float = 0, z: int | float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, tuple):
            return Vector3D(self.x + other[0], self.y + other[1], self.z + other[2])
        elif isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
            self.z += other[2]
        elif isinstance(other, Vector3D):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            return NotImplemented

        return self

    def __sub__(self, other):
        if isinstance(other, tuple):
            return Vector3D(self.x - other[0], self.y - other[1], self.z - other[2])
        elif isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        if isinstance(other, tuple):
            self.x -= other[0]
            self.y -= other[1]
            self.z -= other[2]
        elif isinstance(other, Vector3D):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            return NotImplemented

        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            return NotImplemented

        return self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x / other, self.y / other, self.z / other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            return NotImplemented

        return self

    def normalize(self) -> None:
        """
        The method normalizes this vector and displays the unit vector.
        """

        magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        self.x = self.x / abs(magnitude)
        self.y = self.y / abs(magnitude)
        self.z = self.z / abs(magnitude)

    def from_tuple(
        self, value: tuple[int, int, int] | tuple[float, float, float]
    ) -> None:
        """
        Setting vector values from tuple
        Args:
            value (tuple): A value that allows you to get values for a vector
        """

        self.x, self.y, self.z = value

    def get_tuple(self) -> tuple[int, int, int]:
        """
        Get vector values (int)
        Returns:
            tuple[int, int, int]: x, y and z values
        """

        return int(self.x), int(self.y), int(self.z)

    def get_tuplef(self) -> tuple[float, float, float]:
        """
        Get vector values (float)
        Returns:
            tuple[float, float, float]: x, y and z values
        """

        return float(self.x), float(self.y), float(self.z)
