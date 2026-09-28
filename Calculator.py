def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print(f"Addition: {add(x, y)}")
print(f"Subtraction: {sub(x, y)}")
print(f"Multiplication: {mul(x, y)}")
print(f"Division: {div(x, y)}")
