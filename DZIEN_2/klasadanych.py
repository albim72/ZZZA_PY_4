from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x=x

zk = Liczba(2)
print(zk.x)
print(zk)

print("_________ klasa danych _____________")

@dataclass
class DLiczba:
    x:int
    y:float

dk = DLiczba(8,3)
print(dk.x)

tst = DLiczba(12,3.56)
print(tst)

# class Norm:
#     g:int
#     h:bool
#
# n = Norm(6,True)
# print(n)

@dataclass
class Kolor:
    id:int
    nazwa:str
    # paleta_nr:int
    nazwa_paleta:str

    def __init__(self,id:int,nazwa:str,nazwa_paleta:str,obraz:str):
        self.id = id
        self.nazwa = nazwa
        self.nazwa_paleta = nazwa_paleta
        self.obraz = obraz



k = Kolor(3,"czerwony","X","las")
print(k)
