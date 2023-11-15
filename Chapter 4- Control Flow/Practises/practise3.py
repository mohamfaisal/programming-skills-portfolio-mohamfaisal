# Write a python program with nested decision structures that perform the following: 
# If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

# Function to compare and display greater amount
def compare_and_display(amount1, amount2):
    if amount1 > 10 and amount2 < 100:
        if amount1 > amount2:
            print(f"The greater amount is: {amount1}")
        else:
            print(f"The greater amount is: {amount2}")
    else:
        print("Both conditions are not met.")

# Variables to compare
amount1 = 20
amount2 = 50

# Call the function
compare_and_display(amount1, amount2)