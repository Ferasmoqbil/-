# اختبار سرعه داخل فانكشن داخل دكتاتوري 

import time
def speedtest(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print(f"finally time's {end - start}")
        
    return wrapper

@speedtest
def print_numbers():
    for num in range(1, 20001):
        print(num)


print_numbers()