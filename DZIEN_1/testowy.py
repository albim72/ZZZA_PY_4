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



