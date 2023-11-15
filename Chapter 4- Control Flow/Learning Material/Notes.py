#sales 
Sales = float(input("Enter sales :"))
bonus = 0
if Sales > 10000 :
    bonus = 400
else:
    bonus = 0
print("Your Bonus : "+str(bonus))

#temperature 
Temperature = float(input("Enter Temperature:"))
if Temperature < 40 :
    degree = "Nice weather we're having"
else:
    degree = "A little cold, isn't it?"
print("Current weather : "+str(degree))