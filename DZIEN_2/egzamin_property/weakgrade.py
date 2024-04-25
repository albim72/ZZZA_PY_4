from weakref import WeakKeyDictionary

class Grade:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance,0),self.a,self.b

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być wartością z zakresu 0-100')
        self._values[instance] = value

class ExamC:
    math_grade = Grade(3,5)
    writing_grade = Grade(7,3)
    science_grade = Grade(1,4)
