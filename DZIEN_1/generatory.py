#przykład 1
def liczby():
    for i in range(16):
        yield i

print(liczby())
for p in liczby():
    print(p)


#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania!")
    yield 1001
    print("wznowienie działania...")

    print("wstrzymanie działania!")
    n = 2*n
    k= 4*(k-1)
    yield n+k
    print("wznowienie działania...")

    print("wstrzymanie działania!")
    yield n-k
    print("wznowienie działania...")

    print("wstrzymanie działania!")
    yield n*k
    print("wznowienie działania...")

    print("wstrzymanie działania!")
    yield n/k
    print("wznowienie działania...")
    yield "to jest już koniec"

print(wznowienie(5,6))

for i in wznowienie(6,7):
    if i == 1001:
        continue
    print(f'wartość z yield: {i}')
