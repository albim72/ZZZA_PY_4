from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

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


r2 = VoltageResistance(1.13E3)
print(f"________________ klasa {r2.__class__.__name__} ______________")
print(f"układ elektryczny - stan początkowy:\n"
      f"oporność: {r2.ohms} omów\n"
      f"napięcie początkowe: {r2.voltage} V\n"
      f"natężenie początkowe: {r2.current} A\n")

r2.voltage = 45
print(f"układ elektryczny - zmiana:\n"
      f"oporność: {r2.ohms} omów\n"
      f"napięcie: {r2.voltage} V\n"
      f"natężenie: {r2.current} A\n")

r3 = BoundedResistance(1E3)
print(f"________________ klasa {r3.__class__.__name__} ______________")
try:
      r3.ohms = 12
      print(f'oporność obwodu: {r3.ohms} omów')
except ValueError as r:
      print(r)
