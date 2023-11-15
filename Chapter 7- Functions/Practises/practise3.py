# Write a Python program that uses a function to check if a given number is prime or not.

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
        number = int(input("Please enter a number (or enter 0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if number == 0:
        break

    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")