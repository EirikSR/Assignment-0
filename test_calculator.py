import calculator
import math
import pytest
#Margin is used everywhere floats are compared, they need to be closer than 
#the margin to be considered equal
margin = 1E-12

sin_test = 0.3
cos_test = 0.3
x = 'f3'
y = '1f'

def test_add():
	with pytest.raises(ValueError):
		float(x)
		float(y)
	assert calculator.add(x, y) == 4

def test_add_float():
	assert calculator.add(0.1, 0.2) - 0.3 < margin

def test_add_string():
	assert calculator.add('Hello ' , 'World') == 'Hello World'


def test_factorial():
	assert 120 == calculator.factorial(5)

def test_sin():
	#N = 5 gives high accuracy
	assert calculator.sin(sin_test, 5) - math.sin(sin_test) < margin

def test_divide():
	assert calculator.divide(25, 3) - 25./3. < margin


def test_cos(): #Optional1
	#N = 5 gave error, 6 needed to be within margin
	assert calculator.cos(cos_test, 6) - math.cos(cos_test) < margin

def test_fibonacci(): #Optional2
	#Obtained 100th (F_99) from table
	assert calculator.fibonacci(100) == 218922995834555169026
