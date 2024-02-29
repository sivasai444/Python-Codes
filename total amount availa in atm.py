denominations = [2000, 500, 200, 100]
total_amount = 0

for i in range(len(denominations)):
    denomination = int(input(f"Enter the {i + 1} Denomination: "))
    num_of_notes = int(input(f"Enter the {i + 1} Denomination number of notes: "))
    total_amount += denomination * num_of_notes

print("Total amount available in the ATM machine:",total_amount)
