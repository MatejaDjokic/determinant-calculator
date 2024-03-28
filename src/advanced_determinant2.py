def adv_prompt2(rows=2, cols=2):
    print("Example: \n")
    print("a 2")
    print("4 a\n")
    print("Enter your determinant: \n")

    str = ""
    for i in range(2):
        str += input().strip() + "\n"

    coeffs = [n for n in str.split()]
    return [[coeffs[row + col * cols]
             for col in range(rows)] for row in range(cols)]


def adv_calc2(det):
    a = calc(det[0][0], det[1][1])
    b = calc(det[0][1], det[1][0])

    if a is str and b is str and a.isdigit() and b.isdigit():
        return a - b
    elif a is str and b is not str and a.isdigit():
        return f"{a*b[0]}{b[1]}{to_unicode(b[2])}"
    elif b is str and a is not str and b.isdigit():
        return f"{b*a[0]}{a[1]}{to_unicode(a[2])}"
    else:
        if a[2] == b[2]:
            return f"{a[0] * b[0]}{a[1]}{to_unicode(a[2])}"
        else:
            sa = f"{a[0]}{a[1]}{to_unicode(a[2])}"
            sb = f"{b[0]}{b[1]}{to_unicode(b[2])}"
            if a[2] > b[2]:
                return f"{sa}-{sb}"
            else:
                return f"{sb}-{sa}"


def calc(x, y):
    z = None
    try:
        xi = int(x)
        yi = int(y)
        return str(xi * yi)
    except:
        cx = condense_and_separate(x)
        cy = condense_and_separate(y)
        cz = (cx[0] * cy[0], cx[1], cx[2] + cy[2])
        return cz


def condense_and_separate(input: str):
    num = ""
    param_data = (None, 0)
    for s in input:
        if s.isdigit():
            num += s
        else:
            if param_data[0] is None:
                param_data = (s, 1)
            else:
                count = param_data[1]
                param_data = (param_data[0], count + 1)

    n = "1"
    if num != "":
        n = num
    return (int(n), param_data[0], param_data[1])


def to_unicode(num: int) -> str:
    match num:
        case 0: return "⁰"
        case 1: return "¹"
        case 2: return "²"
        case 3: return "³"
        case 4: return "⁴"
        case 5: return "⁵"
        case 6: return "⁶"
        case 7: return "⁷"
        case 8: return "⁸"
        case 9: return "⁹"
