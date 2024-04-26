from sum_prime import find_prime_numbers_sum
import time
import concurrent.futures

def heavy_function(params):
    t1 = time.time()
    w = find_prime_numbers_sum(*params)
    t2 = time.time()
    tc=t2-t1
    return w,tc

def asynchr():
    nb = [(1, 10_000), (3, 50_000), (5000, 100_000), (4, 900), (800, 15_100)]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        # st = time.time()
        result = executor.map(heavy_function,nb)
        # kn = time.time()
        # tm=kn-st
        # print(tm)
        print(list(result))

    end_time = time.time()
    print(f'całkowity czas wykonania zadania asynchronicznie: {end_time - start_time} s')
