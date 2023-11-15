# Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

Sum = 0
for numbers in range(1, 101):
    Sum += numbers
    if Sum >= 1500:
        break
print("The Sum of all the numberss from 1 to", numbers, "is:", Sum)