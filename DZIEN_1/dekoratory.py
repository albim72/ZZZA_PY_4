import time

#przykład 1

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie programu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka...")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie baloników na {czego}")

dmuchanie("urodziny")

# def info(i):
#     print("coś tam!")

def info(func):
    def wrapper(*args):
        print("coś tam!")
        func(*args)
    return wrapper

@info
def msg(i):
    print(f"informacja: {i}")

msg("728574835738")

#przykład 2
def pomiarczasu(funkcja):
    def wrapper(*args):
        starttime = time.perf_counter()
        funkcja(*args)
        endtime = time.perf_counter()
        print(f"czas wykonania funkcji {funkcja.__name__}:{endtime-starttime}s")
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(2)
        return funkcja()
    return wrapper


lt = [i**3 for i in range(1_000_000)]


@pomiarczasu
@sleep
def big_lista():
    sum(lt)

big_lista()

import numpy as np

ltnp = np.array(lt)


@pomiarczasu
@sleep
def numpy_list():
    np.sum(ltnp)

numpy_list()


@pomiarczasu
def info():
    inf = []
    for u in range(1000):
        inf.append(u)

info()
