import calculator
import math
import pytest
#Margin is used everywhere floats are compared, they need to be closer than 
#the margin to be considered equal
margin = 1E-12

sin_test = 0.3
cos_test = 0.3

@pytest.mark.parametrize("arg, expected_output", [[(1, 5), 6], [(2, -4), -2], [(2, -2), 0]])
def test_add(arg, expected_output):
	assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(1.5, 5.2), 6.7], [(2.1, -2.4), -0.3], [(2.2, -2), 0.2]])
def test_add_float(arg, expected_output):
	assert abs(calculator.add(arg[0], arg[1]) - expected_output) < margin

@pytest.mark.parametrize("arg, expected_output", [[('Marie', 'kjeks'), 'Mariekjeks'],
                                                 [('Papp', 'skalle'), 'Pappskalle'], 
                                                 [('Hello', ' world'), 'Hello world']])
def test_add_string(arg, expected_output):
	assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[3, 6], [4, 24], [10, 3628800]])
def test_factorial(arg, expected_output):
	assert expected_output == calculator.factorial(arg)

@pytest.mark.parametrize("arg, expected_output", [[(20, 5), 4], [(32, 4), 8], [(10, 4), 2.5]])
def test_divide(arg, expected_output):
	assert abs(calculator.divide(arg[0], arg[1])) - expected_output < margin

@pytest.mark.parametrize("arg, expected_output", [[0.2, math.sin(0.2)], [0.3, math.sin(0.3)], [0.4, math.sin(0.4)]])
def test_sin(arg, expected_output):
	#N = 7 gives high accuracy
	assert abs(calculator.sin(arg, 7)) - expected_output < margin


@pytest.mark.parametrize("arg, expected_output", [[0.2, math.cos(0.2)], [0.3, math.cos(0.3)], [0.4, math.cos(0.4)]])
def test_cos(arg, expected_output): #Optional1
	#N = 5 gave error, 6 needed to be within margin
	assert abs(calculator.cos(arg, 7)) - expected_output < margin

@pytest.mark.parametrize("arg, expected_output", [[16, 610], [21, 6765], [100, 218922995834555169026]])
def test_fibonacci(arg, expected_output): #Optional2
	#Obtained 100th (F_99) from table
	assert calculator.fibonacci(arg) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[('a', 2), True],
                                                 [(2, 3), False], 
                                                 [('Hello', 'world'), False]])
def test_TypeError(arg, expected_output):

    try:
        calculator.add(arg[0], arg[1])
        b = False
    except TypeError:
        b = True
    assert b == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(5, 2), False],
                                                 [(2, 0), True], 
                                                 [(7, 0.0001), False]])

def test_ZeroDivisionError(arg, expected_output):
    try:
        calculator.divide(arg[0], arg[1])
        b = False
    except ZeroDivisionError:
        b = True
    assert b == expected_output