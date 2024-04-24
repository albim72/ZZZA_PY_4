print("program testowy")


def xy(a:int,b:int)->int:
    return 2*a-b

print(xy(4,6))
print(xy(1.2,0.5434))
print(xy(True,5))


print((lambda g:g**4)(56))

b = lambda x,v,m=1:(x+v)*m
print(b(8,4,2))
print(b(8,4))

def policz(n):
    return lambda a:a*n

print(policz(5)(9))

print("funkcje wyższego rzędu...")

num = [67,9,-45,2,0,11,5,23,7,90,3,-3,-98,101,46,8,2,-3,1]

parzyste = list(filter(lambda x:x%2==0,num))
print(parzyste)

cube = list(map(lambda x:x**3,num))
print(cube)

print("___________ własna funkcja wyższgo rzędu _____________")

def witaj(imie):
    return f"Miło Cię widzieć {imie}!"

def konkurs(imie,miasto,punkty):
    return f"uczestnik konkursu -> {imie}, miasto: {miasto}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Olaf"))
print(konkurs("Olga","Kraków",56))

