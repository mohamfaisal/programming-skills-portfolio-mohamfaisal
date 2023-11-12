# Make several dictionaries, where each dictionary represents a different pet. In each dictionary,
# include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet

pets = [
    {"kind": "dog", "owner": "Abubakkar"},
    {"kind": "cat", "owner": "Rashid"},
    {"kind": "parrot", "owner": "Faisal"},
]


for pet in pets:
    print(f"This pet is a {pet['kind']} and it belongs to {pet['owner']}.")