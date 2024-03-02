class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

# Przykładowe użycie:
v = Vector3D(1, 2, 3)
print(v)  # Wyświetli: Vector3D(1, 2, 3)

v.x = 4
v.y = 5
v.z = 6
print(v)  # Wyświetli: Vector3D(4, 5, 6)
