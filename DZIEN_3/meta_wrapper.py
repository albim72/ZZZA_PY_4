from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

class DebugMeta(type):
    def __new__(cls, clsname, bases, attrs):
        obj = super().__new__(cls, clsname, bases, attrs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=DebugMeta):
    pass

class Calculate(Base):
    def add(self,x,y):
        return 2*x+4*y

    def mul(self,x,y):
        return 5*x*y

mob = Calculate()

print(mob.add(5,2))
print(mob.mul(1,6))
