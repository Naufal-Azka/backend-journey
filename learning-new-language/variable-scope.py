# local variable scope
def func1():
    x = 10
    print(x)

def func2():
    x = 20
    print(x)

func1()
func2()


# enclosing variable scope
def outer():
    x = 10
    def inner():
        print(x)
    inner()

outer()


# global variable scope
x = 10
def func():
    print(x)

func()


# built-in variable scope
from math import e

def func_e():
    print(e)

func_e()