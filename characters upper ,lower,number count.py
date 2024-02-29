uppercase_count = 0
lowercase_count = 0
number_count = 0

while True:
    char = input("Enter any character:")

    if char == '*':
        break
    if char.isalpha():
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count = 1
    elif char.isdigit():
        number_count += 1

print("Uppercase count:",uppercase_count)
print("Lowercase count:",lowercase_count)
print("Number count:",number_count)
