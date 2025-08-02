def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def nth_power(num, n):
    value = 1
    for _ in range(n):
        value = multiply(num, value)
    return value


print(nth_power(2,2))
print(nth_power(3,3))

print(square(5) == 25)   # True
print(square(-8) == 64)  # True