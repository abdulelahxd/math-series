from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

# fibonacci func
def fibonacci_test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
    
def fibonacci_test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def fibonacci_test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

# lucas func
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 7
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 4
    assert actual == expected

# sum func
def test_sum_fibonacci_one():
    actual = sum_series(1,0,1)
    expected = 1
    assert actual == expected

def test_sum_fibonacci_five():
    actual = sum_series(5,0,1)
    expected = 5
    assert actual == expected

def test_sum_fibonacci_five_x():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_lucas_one():
    actual = sum_series(1,2,1)
    expected = 1
    assert actual == expected

def test_sum_lucas_five():
    actual = sum_series(5,2,1)
    expected = 7
    assert actual == expected