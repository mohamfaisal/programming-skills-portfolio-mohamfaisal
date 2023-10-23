#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
# •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

def send_invitation(guest_name):
    print(f"Hello {guest_name}, please join us for dinner on Friday at 7:00 pm ")

# List of dinner guests
dinner_guests = ["Mohammed Rashid", "Abdullah Kamran", "Abubakkar Zahid", "Md Adil Hussain"]

# Mohammed Rashid can't make it, so we need to find a replacement
MohammedRashid_index = dinner_guests.index("Mohammed Rashid")

# Find a replacement guest
replacement_guest = "Rahma"

# Remove Mohammed Rashid from the list and add Rahma
dinner_guests[MohammedRashid_index] = replacement_guest

# Send invitations to all the guests
for guest in dinner_guests:
    send_invitation(guest)

# Print the name of the guest who can't make it
print(f"Sorry, Mohammed Rashid can't make it to the dinner.")

#efkc
dinner_guest =["Mohammed Rashid", "Abdullah Kamran", "Abdullah Zahid"]
print(f"Hola!,",dinner_guest[0],"please join us for dinner on Friday at 8:00 pm ")
print(f"Hola!,",dinner_guest[1],"please join us for dinner on Friday at 8:00 pm ")
print(f"Hola!,",dinner_guest[2],"please join us for dinner on Friday at 8:00 pm ")
print(dinner_guest[0],"can't join the dinner party")
dinner_guest[0] = "Rahma"
print(dinner_guest)