# Write a Python program that uses a while loop to find the largest number among a series of
# user-input values until they enter '0' to exit the loop.

largest_number = None
while True:
    try:        
        number = int(input(" Enter a number (or enter 0 to exit): "))
    except ValueError:
        print("Invalid input. Enter a valid number.")
        continue
    if number == 0:
        break
    if largest_number is None or number > largest_number:
        largest_number = number
print("The largest number entered is:", largest_number)