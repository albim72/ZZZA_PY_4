class Documentation:
    def __init__(self,nr_obowodu,tytul,data,opis):
        self.nr_obowodu = nr_obowodu
        self.tytul = tytul
        self.data = data
        self.opis = opis
        
    @property
    def tytul(self):
        return self._tytul
    
    @tytul.setter
    def tytul(self,tytul):
        self._tytul = tytul
