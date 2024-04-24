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
