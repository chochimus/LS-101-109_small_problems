def get_num():
    while True:
        try:
            num = int(input("Please enter an integer greater than 0: "))
            if num > 0:
                return num
            print("Number should be greater than 0!")
        except ValueError:
            print("Invalid input, not a number.")

def get_choice():
    while True:
        choice = input('Enter "s" to compute the sum, or "p" to computer the product. ')
        if choice in ["s", "p"]:
            return choice
        print("Invalid choice (s/p)")

def solve(num, op):
    match op:
        case 's':
            return sum(range(1, num + 1))
        case 'p':
            return product(num)
        
def product(num):
    total = 1
    for num in range(1, num + 1):
        total *= num
    return total

number = get_num()
operation = get_choice()
result = solve(number, operation)
print()
print(f'The {'product' if operation == 'p' else 'sum'} of the integers' 
      f' between 1 and {number} is {result}.')