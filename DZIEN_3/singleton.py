class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Regular:
    pass

r1 = Regular()
r2 = Regular()

print(r1==r2)
print(r1)
print(r2)

class Sng(metaclass=Singleton):
    pass

s1 = Sng()
s2 = Sng()

print(s1==s2)
print(s1)
print(s2)

class A(Sng):
    pass

class B(Sng):
    pass

a1 = A()
b1 = B()

print(a1==b1)
print(a1)
print(b1)
