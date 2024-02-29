def power(x, n):
    return x ** n

def add(x, n):
    return x + n

def subtract(x, n):
    return x - n

def multiply(x, n):
    return x * n

def divide(x, n):
    if n != 0:
        return x / n
    else:
        return "Cannot divide by zero."

x = float(input("Enter the value of X: "))
n = float(input("Enter the value of N: "))
choice = int(input("Enter your choice (1: Pow, 2: Add, 3: Sub, 4: Mul, 5: Div): "))

if choice == 1:
    result = power(x, n)
elif choice == 2:
    result = add(x, n)
elif choice == 3:
    result = subtract(x, n)
elif choice == 4:
    result = multiply(x, n)
elif choice == 5:
    result = divide(x, n)
else:
    result = "Invalid choice."

print("Result:", result)
