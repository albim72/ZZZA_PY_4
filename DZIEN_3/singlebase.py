class SingleBase(type):
    def __new__(cls,clsname,bases,attrs):
        if len(bases) > 1:
            raise TypeError("Wielodziedziczenie zabronione!!!")
        return super().__new__(cls,clsname,bases,attrs)

class Base(metaclass=SingleBase):
    pass

class Extra:
    pass

class A(Base):
    def __new__(cls, *args, **kwargs):
        return object.__new__(A)

class B(A):
    pass
#
# class C(B,Extra):
#     pass
