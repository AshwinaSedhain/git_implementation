"""
Integration tests — test multiple operations chained together,
simulating real-world usage of the calculator.
"""
from calculator import add, subtract, multiply, divide


def test_chain_operations():
    # (10 + 5) * 2 = 30
    result = multiply(add(10, 5), 2)
    assert result == 30

def test_formula():
    # (100 - 20) / 4 = 20
    result = divide(subtract(100, 20), 4)
    assert result == 20.0

def test_complex_expression():
    # ((3 + 7) * 5 - 10) / 4 = 10
    step1 = add(3, 7)       # 10
    step2 = multiply(step1, 5)  # 50
    step3 = subtract(step2, 10) # 40
    result = divide(step3, 4)   # 10
    assert result == 10.0
