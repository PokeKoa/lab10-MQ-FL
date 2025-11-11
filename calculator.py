import math
<<<<<<< HEAD
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
def log(a,b):
    if a <= 0:
        raise ValueError("Logarithm arguments must satisfy: a > 0, b > 0, b != 1")
    if b <= 0 or b == 1:
        raise ValueError("Logarithm arguments must satisfy: a > 0, b > 0, b != 1")
    return math.log(b,a)
def exp(a, b):
    return a ** b
=======
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b


def log(a, b): 
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Logarithm arguments must satisfy: a > 0, b > 0, a != 1")
    else:
        return math.log(b,a)

def exp(a, b): 
    return a**b

