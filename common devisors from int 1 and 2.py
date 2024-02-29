def find_common_divisors(num1, num2):
    common_divisors = []
    
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    
    return common_divisors

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = find_common_divisors(num1, num2)
print("Common divisors:",result)
