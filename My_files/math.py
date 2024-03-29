def add(a, b):
    print(f"result = {a + b}")


def sub(a, b):
    print(f"result = {a - b}")


def mult(a, b):
    print(f"result = {a * b}")


def div(a, b):
    print(f"result = {a / b}")


num1 = int(input("Enter your first digit: "))
num2 = int(input("Enter your second digit: "))

try:
    div(num1, num2)
except Exception as error:
    print(error)

print("Hello")

print("Friday")

print("Saturday")

