# Write a Python program that uses the elif statement to determine the season based on the
# month provided as input.

def determine_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

month = int(input("Enter a month number: "))
season = determine_season(month)
print(f"The season for month {month} is {season}")