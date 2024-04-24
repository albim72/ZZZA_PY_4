from oldresistor import OldResistor
from resistor import Resistor

r0 = OldResistor(10.2E2)
print(f"________________ klasa {r0.__class__.__name__} ______________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E2)
print(r0.get_ohms())


r1 = Resistor(5.01E3)
print(f"________________ klasa {r1.__class__.__name__} ______________")
print(r1.ohms)
r1.ohms = 2.2E3
print(r1.ohms)
