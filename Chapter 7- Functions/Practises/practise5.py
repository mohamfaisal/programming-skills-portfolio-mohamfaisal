# Write a Python program that defines a function to check whether a given number is prime.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    try:
        number = int(input("Enter a number (or enter 0 to exit): "))
    except ValueError:
        print("Invalid input. Enter a valid number.")
        continue
    if number == 0:
        break
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")