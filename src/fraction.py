from fractions import Fraction


def to_fraction(m, n):
    if n == 0:
        return "Cannot divide by zero."

    result = m / n
    if result.is_integer():
        return int(result)
    else:
        simplified_fraction = Fraction(m, n)
        return simplified_fraction
