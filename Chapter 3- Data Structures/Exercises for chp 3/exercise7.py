#Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#•Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse() to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# Create a list of locations
locations = ['Abudhabi', 'Dubai', 'Sharjah', 'Ajman', 'Fujairah']

# Print the original list
Original_list = locations
print(locations)

# Print the list in alphabetical order using sorted()
locations.sort()
print(locations)

# Print the original list again
Original_list = locations
print(locations)

# Print the list in reverse alphabetical order using sorted()
locations.reverse()
print(locations)

# Print the original list again
Original_list = locations
print(locations)

# Change the order of the list using reverse()
locations.reverse()
print("List after first reverse():", locations)

# Change the order of the list back to its original order using reverse()
locations.reverse()
print("List after second reverse():", locations)

# Change the order of the list so it's stored in alphabetical order using sort()
locations.sort()
print("List after first sort():", locations)

# Change the order of the list so it's stored in reverse alphabetical order using sort()
locations.sort(reverse=True)
print("List after second sort():", locations)