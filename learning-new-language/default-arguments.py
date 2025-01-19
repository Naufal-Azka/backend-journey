# default arguments = arguments that take a default value if no argument value is passed during the function call

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1, 0))


# counting function with default start value
import time

def count(end, start=0):
    for i in range(start, end):
        print(i, end=' ')
        time.sleep(1)
    print('\nCounting completed!')

count(30, 15)