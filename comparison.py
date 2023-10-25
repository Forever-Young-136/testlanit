# def compare(comparison_1):



# print(compare('2>5'))


def compare(comparison_1):
    line = comparison_1
    numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
    #print(numbers)

    a = int(numbers[0])
    b = int(numbers[1])

    if '=' in line:
        c = int(a) == int(b)
    elif '>' in line:
        c = int(a) > int(b)
    else:
        c = int(a) < int(b)
    #print(c)
    return c
print(compare('123>-4'))


