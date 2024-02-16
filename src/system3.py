from src.determinant3 import calc3
from fractions import Fraction
from src.prompt import prompt


def system3():
    d, dx, dy, dz, x, y, z = xyz_calc(xyz_prompt())

    print(f"\nΔ: {d}")
    print(f"(Δx, Δy, Δz) = ({dx}, {dy}, {dz})")
    if d != 0:
        print(f"(x, y, z) = ({x}, {y}, {z})\n")
    else:
        print("There are no possible solutions!\n")


def xyz_prompt():
    print("Example: \n")
    print("1  2  3  4")
    print("5  6  7  8")
    print("9 10 11 12\n")
    print("Enter your system: \n")

    return prompt(4, 3)


def xyz_calc(system):
    d = calc3([system[0], system[1], system[2]])
    dx = calc3([system[3], system[1], system[2]])
    dy = calc3([system[0], system[3], system[2]])
    dz = calc3([system[0], system[1], system[3]])

    x = Fraction(dx, d)
    y = Fraction(dy, d)
    z = Fraction(dz, d)

    return d, dx, dy, dz, x, y, z
