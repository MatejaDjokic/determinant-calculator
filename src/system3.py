from src.prompt import default_prompt
from src.determinant3 import calc3
from fractions import Fraction


def system3():
    sys = xyz_prompt()
    d, dx, dy, dz, x, y, z = xyz_calc(sys)
    # print(det)
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

    return default_prompt(4, 3)


def xyz_calc(system):
    d = calc3([system[0], system[1], system[2]])
    dx = calc3([system[3], system[1], system[2]])
    dy = calc3([system[0], system[3], system[2]])
    dz = calc3([system[0], system[1], system[3]])

    x = 0
    y = 0
    z = 0
    if d != 0:
        x = Fraction(dx, d)
        y = Fraction(dy, d)
        z = Fraction(dz, d)

    return d, dx, dy, dz, x, y, z
