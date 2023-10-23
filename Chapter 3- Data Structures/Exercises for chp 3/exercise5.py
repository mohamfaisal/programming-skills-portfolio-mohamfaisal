#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
# •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

dinner_guest =["Mohammed Rashid", "Abdullah Kamran", "Abdullah Zahid"]
print(f"Hola!,",dinner_guest[0],"please join us for dinner on Friday at 8:00 pm ")
print(f"Hola!,",dinner_guest[1],"please join us for dinner on Friday at 8:00 pm ")
print(f"Hola!,",dinner_guest[2],"please join us for dinner on Friday at 8:00 pm ")
print(dinner_guest[0],"can't join the dinner party")
dinner_guest[0] = "Rahma"
print(dinner_guest)