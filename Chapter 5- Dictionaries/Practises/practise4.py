# Write a Python program to iterate through both the keys and values of a dictionary and print them

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

dictionary = {"Name": "Faisal",
               "Age": 18,
                 "Nationality": "Indian",
                   "University": "Bathspa University RAK"}

print_dict(dictionary)
