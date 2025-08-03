def center_of(str):
    if len(str) % 2 == 0:
        start = (len(str) // 2) - 1
        end = start + 2
        return str[start:end]
    else:
        return str[len(str)//2]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True