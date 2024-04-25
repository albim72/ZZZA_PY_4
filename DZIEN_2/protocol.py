from typing import List,Protocol
from decimal import Decimal

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price


def calculate_total(items:List[Item])->float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total(
    [
        Product('masło',3,6.4),
        Product('ser kozi',1,13.5),
        Product('papryka',1.5,11.99),
        Product('woda mineralna',12,1.89)
    ]
)

d = Decimal("93.02")
print(f"do zapłaty: {total:.2f} zł")
print(f"wartość decimal: {d}")



