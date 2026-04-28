def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exp):
    """Raise base to the power of exp."""
    return base ** exp

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
