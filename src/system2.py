from src.determinant2 import calc2
from fractions import Fraction
from src.prompt import default_prompt


def system2():
    d, dx, dy, x, y = xy_calc(xy_prompt())

    print(f"\nΔ: {d}")
    print(f"(Δx, Δy) = ({dx}, {dy})")
    if d != 0:
        print(f"(x, y) = ({x}, {y})\n")
    else:
        print("There are no possible solutions!\n")


def xy_prompt():
    print("Example: \n")
    print("1 2 3")
    print("4 5 6\n")
    print("Enter your system: \n")

    return default_prompt(3, 2)


def xy_calc(system):
    d = calc2([system[0], system[1]])
    dx = calc2([system[2], system[1]])
    dy = calc2([system[0], system[2]])

    x = Fraction(dx, d)
    y = Fraction(dy, d)

    return d, dx, dy, x, y
