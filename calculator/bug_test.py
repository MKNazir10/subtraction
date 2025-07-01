# bug_test.py
import unittest
from main import sub



# def test_subtract_positive():
#     assert sub(5, 2) == 3, "Test Failed: sub(5, 2) should be 3"

# def test_subtract_negative():
#     assert sub(2, 5) == -3, "Test Failed: sub(2, 5) should be -3"


def test_with_negative_input_a():
    result = sub(-5, 3)
    print("🔍 result:", result)
    assert False, "Forcing failure to see output"


if __name__ == "__main__":
    test_with_negative_input_a()
    # test_subtract_positive()
    # test_subtract_negative()

    print("All subtraction tests passed")


if __name__ == '__main__':
    unittest.main()