def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

# for n, take second param n and use as second argument to multiply.

print(square(5) == 25)   # True
print(square(-8) == 64)  # True