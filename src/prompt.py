from fractions import Fraction
from re import compile


def default_prompt(cols, rows):
    str = ""
    for i in range(0, rows):
        str += input().strip() + "\n"

    numbers = [int(num) for num in str.split()]

    return [[numbers[row + col * cols]
             for col in range(rows)] for row in range(cols)]


def advanced_prompt(rows):
    for i in range(rows):
        s = input()
        parse = parse_linear_equation(s)
        print(parse)


def parse_linear_equation(equation):
    # Use regular expression to extract coefficients and constant term
    pattern = compile(r'([-+]?\d*\.?\d*/?\d*)[a-zA-Z]?')
    matches = pattern.findall(equation)

    print(matches)

    coefficients = []
    for m in matches:
        if m != '':
            if '+' in m:
                m = m.replace('+', '')
            if '/' in m:
                coefficients.append(float(Fraction(m)))
            else:
                coefficients.append(float(m))

    return coefficients

# def parse_linear_equation(equation):
#     pattern = compile(r'([-+]?\d*\.?\d*)[a-zA-Z]?')
#     matches = pattern.findall(equation)

#     coef = []
#     for m in matches:
#         if str(m).find('+') != -1:
#             m = str(m).replace('+', '')
#         if m != '':
#             coef.append(float(m))

#     return coef
