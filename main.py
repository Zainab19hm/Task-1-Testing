def add_numbers(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def divide_numbers(a: float, b: float) -> float:
    """Returns the division of a by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"10 / 2 = {divide_numbers(10, 2)}")
