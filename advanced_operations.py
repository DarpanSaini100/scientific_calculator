import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def power(a, b):
    return math.pow(a, b)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)
