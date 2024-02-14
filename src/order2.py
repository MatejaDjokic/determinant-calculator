
def prompt2():
    print("Example: \n")
    print("1 2")
    print("3 4\n")
    print("Enter your determinant: \n")

    det = [[0, 0], [0, 0]]
    for i in range(0, 2):
        str = input()
        row = [
            int(number) for number in str.split()]
        det[i] = row
    return det


def calc2(det):
    a = det[0][0] * det[1][1]
    b = det[0][1] * det[1][0]
    return a - b
