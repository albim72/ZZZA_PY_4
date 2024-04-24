liczby = [56,78,1009,-1112,0,12,78,199,-99,567,677,-345,177,844,94]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    sr_arytm = suma_el/liczba_el
    return minimum,maksimum,rozstep,suma_el,sr_arytm

wyniki = pokaz_statystyki(liczby)
print(wyniki)
print(type(wyniki))

mini,maxi,rozt,sume,srart = pokaz_statystyki(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp wartości: {rozt},"
      f"suma elementów: {sume}, średnia arytmwtyczna: {srart}")
