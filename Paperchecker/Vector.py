import math
class Vector:
    def __init__(self, a):
        self._coords = a[:]
        self._n = len(a)
    def __getitem__(self, i):
        return self._coords[i]
    def __add__(self, other):#计算向量和
        result = []
        for i in range(self._n):
            result.append(self._coords[i] + other._coords[i])
        return Vector(result)
    def __sub__(self, other):#计算向量差
        result = []
        for i in range(self._n):
            result.append(self._coords[i] - other._coords[i])
        return Vector(result)
    def dot(self, other):#计算向量内积
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result
    def multi_minus(self, n):
        result = []
        for i in range(self._n):
            result.append(self._coords[i] * n)
        return Vector(result)
    def __abs__(self):
        return math.sqrt(self.dot(self))
    def direction(self):
        return self.multi_minus(1.0 / abs(self))
    def __str__(self):
        return str(self._coords)
    def __len__(self):
        return self._n