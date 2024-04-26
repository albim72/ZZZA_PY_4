from sum_prime import find_prime_numbers_sum
import time

def synchr():
    nb = [(1,10_000),(3,50_000),(5000,100_000),(4,900),(800,15_100)]
    start_time = time.time()
    for pair in nb:
        prime_sum = find_prime_numbers_sum(*pair)
        print(prime_sum)
    end_time = time.time()
    print(f'całkowity czas wykonania zadania: {end_time - start_time} s')
