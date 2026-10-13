def classify(a, b, c):
    # BUG 1: Missing validation for zero/negative sides
    # BUG 2: Wrong triangle inequality (uses < instead of <=)
    if a + b < c or a + c < b or b + c < a:
        return "Not a triangle"
    # BUG 3: Wrong order - checks isosceles before equilateral
    if a == b or b == c or a == c:
        return "Isosceles"
    if a == b == c:
        return "Equilateral"
    return "Scalene"