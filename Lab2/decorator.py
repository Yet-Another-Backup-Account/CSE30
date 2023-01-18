import time

def calculate_time(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f'It took {(end - start)} secs.')
        return func(*args, **kwargs)
    return wrap

@calculate_time
def sum1(n):
    result=0
    for i in range(1, n+1):
        result += i
    return result
if __name__ == '__main__':
    n = 1000000
    s = sum1(1000000)
    print(f'The sum of numbers from 1 to {n} is {s}.')
