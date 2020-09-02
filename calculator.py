import pytest

def add(x, y):

    if(type(x) != type(y)):
        try:
            float(x)
            float(y)
        except:
            raise TypeError(f"Trying to add {x, type(x)} and {y, type(y)}")
            
        
        return x+y
    else:
        return x+y

def factorial(x):
	ret = 1
	for i in range(1, x+1):
		ret = ret*i
	return ret

def sin(x, N):
	ret = 0
	for i in range(N):
		a = (-1)**i*x**(2*i+1)
		b = factorial(2*i+1)
		ret += a/b
	return ret

def cos(x, N):
	ret = 0
	for i in range(N):
		a = (-1)**i*x**(2*i)
		b = factorial(2*i)
		ret += a/b
	return ret

def divide(x, y):
	#Converting to float for divisiding

    if(y == 0):
        raise ZeroDivisionError
    else:
	    return float(x)/y

def fibonacci(N):
	a = 0
	b = 1
	for i in range (0, N-1):
		c = a + b
		b = a
		a = c
	return a

x = 1
y = "y"

print()
