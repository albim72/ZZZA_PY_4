#przykład 1
def liczby():
    for i in range(16):
        yield i

print(liczby())
for p in liczby():
    print(p)
