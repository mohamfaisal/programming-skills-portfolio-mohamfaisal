# while loop 

a = 1
while a<10:
    print(a)
    a+=1      # a=a+1

i = 2
while i<10:
    print(i)
    i+=1      # i=i+1

# Infinite Loop 

count = 1
while count <=5:
    print("count is :",count)
    count+=1

# Break Loop

j=1
while j<6:
    print(j)
    if j ==3:
        break   # Terminated 
j+=1            # j=j+1 

# Continue Loop 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# List Loop

fruits = ["apple","banana","orange"]
for x in fruits:
    print(x)

# Range Loop

for x in range(6):
    print(x)

# To improve readibility

for x in range(2,6):
    print(x,end=",")

# count + 5 

for X in range(0,20,2):
    print(x,end=",")

# Getting input from user - controlled loop 
N = int (input("Enter max number for range :"))
for x in range (0,20,5):
    print(x,end=",")

# Take input 5 numbers from user and sum of the 5 numbers by using for loop 

sum = 0 
for i in range(5):
    x = float(input("Enter Number:"))
    sum += x   # sum = sum + 1 
    if x ==-1 :
        break
    print(sum)

# Sentinels value loop control 

sum = 0
while True:
    x = int(input("Enter Number:"))
    sum += x   # sum = sum + 1
    if x ==-1 :
        break 
    print(sum)

# Running time total 

sum = 0
for i in range(5):
    x = int(input("Enter Number:"))
    sum += x   # sum = sum + 1        
    print(sum)

# Nested loop 

x = [1,2,3]
y = [4,5,6]
for i in x:
    for j in y:
        print(i,j)

# Looping through string 

for x in "banana":
  print(x)

# The Pass statement 

for x in [0, 1, 2]:     # for loops cannot be empty, but if you for some reason have a for loop with no content,
    pass                # put in the pass statement to avoid getting an error.

# Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")