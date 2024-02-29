lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

result_list = [(num, num ** 2) for num in range(lower_range, upper_range + 1)]

print("List of Tuples:",result_list)
