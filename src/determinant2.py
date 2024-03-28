from src.prompt import default_prompt


def determinant2():
    print(f"\nΔ: {calc2(prompt2())}\n")


def prompt2():
    print("Example: \n")
    print("1 2")
    print("3 4\n")
    print("Enter your determinant: \n")

    return default_prompt(2, 2)


def calc2(det):
    a = det[0][0] * det[1][1]
    b = det[0][1] * det[1][0]
    return a - b
