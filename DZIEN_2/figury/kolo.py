from figura import Figura
import math

class Kolo(Figura):
    def __init__(self, a):
        super().__init__(a, b=None)

    def policz_pole(self):
        return math.pi*self.a**2
