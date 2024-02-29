def find_season(month, day):
    if (month == "Mar" and day >= 20) or (month == "Apr" or month == "May"):
        return "Spring"
    elif (month == "Jun" and day >= 21) or (month == "Jul" or month == "Aug"):
        return "Summer"
    elif (month == "Sep" and day >= 22) or (month == "Oct" or month == "Nov"):
        return "Fall"
    elif (month == "Dec" and day >= 21) or (month == "Jan" or month == "Feb"):
        return "Winter"
    else:
        return "Invalid input"

month_input = input("Enter the month: ").capitalize()[:3]  # Capitalizing and taking the first three letters
day_input = int(input("Enter the date: "))

season = find_season(month_input, day_input)
print(f"The season associated with the date is: {season}")
