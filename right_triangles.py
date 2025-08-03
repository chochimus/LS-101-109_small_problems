def triangle(num):
    result = ""
    for i in range(num):
        for j in range(num):
            if j + i < num - 1:
                result += " "
            else:
                result += "*"
        result += "\n"
    print(result)

def triangle2(num):
    for i in range(1, num + 1):
        space = num - i
        stars = i
        print(f'{" " * space}{"*" * stars}')

triangle(5)
triangle(9)

triangle2(5)
triangle2(9)