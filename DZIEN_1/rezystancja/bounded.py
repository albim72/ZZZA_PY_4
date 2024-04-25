from resistor import Resistor

class BoundedResistance(Resistor):
    def __init__(self,ohms,abc):
        super().__init__(ohms)
        self.abc = abc
        self.MSTALA = 1.09

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self,ohms):
        if ohms <= 0:
            raise ValueError(f'zadana wartość: {ohms} jest niewłaściwa')
        self._ohms = ohms
