# Intentional bug: divide returns wrong value (for QA demo)
def divide_buggy(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b   # BUG: should be a / b
