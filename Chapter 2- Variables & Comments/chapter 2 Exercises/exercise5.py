# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

# Define the cost of a USB stick and the amount of money the girl has
per_usb_stick = 6
amount_of_money = 50

# Calculate the number of USB sticks the girl can buy
number_of_usb_sticks = amount_of_money // per_usb_stick

# Calculate the amount of money the girl will have left
money_left = amount_of_money % per_usb_stick

# print the result 
print(f"The girl can buy {number_of_usb_sticks} USB sticks.")
print(f"She will have {money_left} pounds left.")