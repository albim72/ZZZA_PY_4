from oldresistor import OldResistor

r0 = OldResistor(10.2E2)
print(f"________________ klasa {r0.__class__.__name__} ______________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E2)
print(r0.get_ohms())
