from src.prompt import prompt


def determinant3():
    print(f"\nΔ: {calc3(prompt3())}\n")


def prompt3():
    print("Example: \n")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9\n")
    print("Enter your determinant: \n")

    return prompt(3, 3)


def calc3(det):
    a = det[0][0] * det[1][1] * det[2][2]
    b = det[1][0] * det[2][1] * det[0][2]
    c = det[2][0] * det[0][1] * det[1][2]
    d = det[0][2] * det[1][1] * det[2][0]
    e = det[1][2] * det[2][1] * det[0][0]
    f = det[2][2] * det[0][1] * det[1][0]
    return a + b + c - d - e - f
