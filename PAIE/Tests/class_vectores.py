class Vector:
    def __init__(self, x, y=0, z=0):
        self._x = x
        self. _y = y
        self. _z = z

    def sumaVectorial(self, v):
        suma = Vector(self._x + v._x, self._y + v._y, self._z + v._z)
        return suma
    
    def mostrar(self):
        print("(" + "x=" + str(self._x) + ", y=" + str(self._y) + ", z=" + str(self._z) + ")")

    def multiplicacionVectorial(self, v):
        xm = self._y * v._z - self._z * v._y
        ym = -self._x * v._z + self._z * v._x 
        zm = self._x * v._y - self._y * v._x 
        multiplicacion = Vector(xm, ym, zm)
        return multiplicacion
    
    def __eq__(self, otherV):
        if(self._x == otherV._x and self._y == otherV._y and self._z == otherV._z):
            return True
        return False
    
    def __str__(self):
        return "(" + "x=" + str(self._x) + ", y=" + str(self._y) + ", z=" + str(self._z) + ")"
