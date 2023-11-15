print("Name", ":Faisal", 2005)
print("address", ":al nuaimiya-1","al enjaaz street", 2023467)

#Variable Reassighnment 
name = "Faisal"
name = "bathspa"
print(name)

#Data types int, float, str

#by default / sign gives floating numbers // it gives integer
print(15/4)
print(12//5)

#How to take input from the user (By default it takes string from user)
name = input("Enter Name:")
print(name)

#User age (By default it takes string from user) we need to type casting 
'''age = input("Enter your age :")
print(age)'''

#Type Casting
age = int(input ("Enter your age"))
print(age)

#Math operators
print((2*3/8+(23+5)))

#type cast float to int
ans=((2*3/8+(23+5)))
print(int(ans))

#how to write name in one line with something 
f_name = " Mohammed "
l_name = " Faisal "
name = f_name + l_name
print(name,end ="")
print (" New line message")

##special characters appearning in string literal 
#preceeded by backslash (\)
# examples newline (\n), horizontal tab(\t)
f_name = " Mohammed "
l_name = " Faisal "
name = f_name + l_name
print(name,end ="\n")
print (" New line message")

#f-string function helps us to compute the both values 
#example1-
print('The value is {10 + 2}.' )
#ans- the output is 10 + 2 
print(f'The value is {10 + 2}')
#ans- the output is 12
#example2- 
val = 10
print(f'The value is {val + 2} ')
#ans- the output is 12





