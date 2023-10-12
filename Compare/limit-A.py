import sympy

def f(x):
    return x**2

derivative = sympy.diff(f, x)

print(derivative)