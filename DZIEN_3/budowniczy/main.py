from director import Director
from conretebuilder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Produkt podstawowy: ")
director.built_minimal_product()
builder.product.list_parts()

print("\n_____________________________________")

print("Produkt pełny: ")
director.built_full_product()
builder.product.list_parts()

print("\n_____________________________________")
print("Produkt użytkownika...")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
