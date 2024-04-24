# import dane
# import dane as dn
from dane import nrfilii as filia
from dane import book as bk
from funkcje.funkcjab import czytaj_liste,czytaj_slownik

print("____________ wyświetlanie bezpośrednie _______________")
print(filia)
print(bk)

print("____________ wyświetlanie za pomocą funkcji _______________")
czytaj_liste(filia)
czytaj_slownik(bk)
