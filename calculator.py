#https://github.com/PokeKoa/lab10-MQ-FL/tree/main
#Partner 1: Mike Quick
#Partner 2: Frankie Lin
import math
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a, b):
    return a * b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
def exp(a, b):
    return a ** b

def log(a, b): 
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm arguments must satisfy: a > 0, b > 0, a != 1")
    else:
        return math.log(b,a)

def square_root(a): 
    if a < 0:
        raise ValueError("a has to be greater than 0!")
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)


