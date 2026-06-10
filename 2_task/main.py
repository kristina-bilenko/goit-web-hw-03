from time import time
from multiprocessing import Pool, cpu_count

def factorize(*numbers):
    final_list = []
    for number in numbers:
        current_list = []
        for num in range(1, number + 1):
            if number % num == 0:
                current_list.append(num)
        final_list.append(current_list)
    return final_list

def factorize_one_number(number):
    final_list = []
    for num in range(1, number + 1):
        if number % num == 0:
            final_list.append(num)
    return final_list

if __name__== "__main__":

    start_sync = time()
    a1, b1, c1, d1 = factorize(128, 255, 99999, 10651060)
    end_sync = time()
    proces_time_sync = end_sync - start_sync
    print(f"Час виконання обчислень для синхроного виконання: {proces_time_sync:.4f} секунд.")

    start_multiprocess = time()
    numbers = (128, 255, 99999, 10651060)
    with Pool(cpu_count()) as p:
        result = p.map(factorize_one_number, numbers)
    a2, b2, c2, d2 = result
    end_multiprocess = time()
    proces_time_multiprocess = end_multiprocess - start_multiprocess
    print(f"Час виконання обчислень для паралельного виконання: {proces_time_multiprocess:.4f} секунд.")

    assert a1 == a2 == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b1 == b2 == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c1 == c2 == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d1 == d2 == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
