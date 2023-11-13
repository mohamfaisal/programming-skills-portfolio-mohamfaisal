# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['chicken sandwich', 'falafel sandwich', 'egg sandwich', 'grilled cheese sandwich', 'beef sandwich','pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich']
finished_sandwiches = []

pastrami_count = sandwich_orders.count('pastrami sandwich')
if pastrami_count < 3:
    print("The deli has run out of pastrami sandwich.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')
else:
    print("We have enough pastrami sandwiches.")

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)