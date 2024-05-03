class comx :
    def __init__(self, x, y) :
        self.real = x
        self.image = y
    def __add__(self, other) :
        return comx(self.real+other.real, self.image+other.image)
    def __sub__(self, other) :
        return comx(self.real-other.real, self.image-other.image)
    def __mul__(self, other) :
        return comx(self.real*other.real, self.image*other.image)
    def __truediv__(self, other) :
        return comx(self.real/other.real, self.image/other.image)
    def __str__(self) :
        return '({}, {})'.format(self.real, self.image)

a = comx(1, 2)
b = comx(2, 3)
c = a+b
d = a-b
e = a*b
f = a/b

print('a+b =', c)
print('a-b =', d)
print('a*b =', e)
print('a/b =', f)
