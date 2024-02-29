REGULAR_PRICE = 185  
DISCOUNT_PERCENTAGE = 60  

fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))

regular_price = fresh_loaves * REGULAR_PRICE
discounted_price = day_old_loaves * REGULAR_PRICE * (100 - DISCOUNT_PERCENTAGE) / 100
total_price = regular_price + discounted_price

print(f"Regular Price:   {regular_price:.2f}")
print(f"Discounted Price: {discounted_price:.2f}")
print(f"Total Price:      {total_price:.2f}")
