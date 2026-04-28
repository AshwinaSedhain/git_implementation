import pytest
from calculator import add, subtract, multiply, divide


# --- Unit Tests ---

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

# --- Tests for new operations (feature/power-modulo branch) ---

def test_power():
    from calculator import power
    assert power(2, 10) == 1024
    assert power(3, 0) == 1
    assert power(5, 2) == 25

def test_modulo():
    from calculator import modulo
    assert modulo(10, 3) == 1
    assert modulo(20, 4) == 0

def test_modulo_by_zero():
    from calculator import modulo
    import pytest
    with pytest.raises(ValueError):
        modulo(5, 0)
