from funkcje.funkcjab import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(CDane)

    def __repr__(self):
        return "To jest obiekt klasy służącej do przetwarzania list oraz słowników"
    
    def czytaj_l(self):
        return czytaj_liste(self.lista)
    
    def czytaj_s(self):
        return czytaj_slownik(self.slownik)
