"""Property exercises"""
import math

class Circle:
    """Circle with radius, area, etc."""
    def __init__(self, radius=1):
        if (radius < 0):
            raise ValueError("Radius cannot be negative!")
        self._radius = radius
        self.radius_changes = [self._radius]
    @property
    def area(self):
        return math.pi*(self._radius**2)
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
        if (val < 0):
            raise ValueError("Radius cannot be negative!")
        self._radius = val
        self.radius_changes.append(val)
    @property
    def diameter(self):
        return self._radius*2
    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("diameter cannot be negative")
        self._radius = diameter/2
        self.radius_changes.append(self._radius)

#@total_ordering
class Vector:
    """Class representing a 3 dimensional vector."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
   
    @property
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**(0.5)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        elif self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x - other, self.y - other, self.z - other)
        else:
            return TypeError

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return TypeError

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return TypeError

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)**0.5
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return TypeError


    def __rmul__(self, other):
        if isinstance(other, Vector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)**0.5
        elif isinstance(other, int) or isinstance(float):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return TypeError


class Person:
    """Person with first and last name."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def name(self):
        return self.first_name + " " + self.last_name
