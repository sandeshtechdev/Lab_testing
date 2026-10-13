import pytest
import triangle
import triangle_broken

# Test data: (a, b, c, expected)
TEST_CASES = [
    (3, 3, 3, "Equilateral"),
    (3, 3, 5, "Isosceles"),
    (3, 4, 5, "Scalene"),
    (1, 2, 3, "Not a triangle"),
    (0, 4, 5, "Invalid"),
    (-1, 2, 2, "Invalid"),
]

@pytest.mark.parametrize("a,b,c,expected", TEST_CASES)
def test_triangle_correct(a, b, c, expected):
    assert triangle.classify(a, b, c) == expected

@pytest.mark.parametrize("a,b,c,expected", TEST_CASES)
def test_triangle_broken(a, b, c, expected):
    # This will FAIL for broken cases - demonstrating CI catches bugs
    assert triangle_broken.classify(a, b, c) == expected