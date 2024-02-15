def prompt(cols, rows):
    str = ""
    for i in range(0, rows):
        str += input().strip() + "\n"

    numbers = [int(num) for num in str.split()]

    return [[numbers[row + col * cols]
             for col in range(rows)] for row in range(cols)]
