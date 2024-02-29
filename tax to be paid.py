income = int(input("Enter the income: "))

if income <= 150000:
    tax = 0
elif 150001 <= income <= 300000:
    tax = 0.1 * (income - 150000)
elif 300001 <= income <= 500000:
    tax = 0.1 * (150000) + 0.2 * (income - 300000)
else:
    tax = 0.1 * (150000) + 0.2 * (200000) + 0.3 * (income - 500000)

print("Tax to be paid:",tax)
