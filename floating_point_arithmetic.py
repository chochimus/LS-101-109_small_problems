def prompt(text):
    print(f"==> {text}")


def calculate(num1, num2, op):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "//":
            return num1 // num2
        case "%":
            return num1 % num2
        case "**":
            return num1 ** num2

prompt("Enter the first number:")
number1 = float(input())

prompt("Enter the second number:")
number2 = float(input())

for operator in ["+", "-", "*", "/", "//", "%", "**"]:
    prompt(f"{number1} {operator} {number2} = {calculate(number1, number2, operator)}")