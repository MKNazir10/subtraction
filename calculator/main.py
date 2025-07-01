"""Module for performing subtraction."""

def sub(a, b):
    """Return the result of subtracting b from a."""
    print("subtract called with:", a, b)
    return a - b


if __name__ == '__main__':
    RESULT = sub(10, 5)
    print(RESULT)
