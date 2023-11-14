# Write a function called make_shirt() that accepts a size and the text of a message that should be 
# printed on the shirt. The function should print a sentence summarizing the size of the shirt and
# the message printed on it. Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

#def function to define function 
def make_shirt(size,message):
  print("Your shirt size is ",size," and it says ",message,) 

#ask user thier shirt size and what they want on thier shirt
shirtsize = str(input("Enter your shirt size (S,M,L,XL,XXL): "))##S,M,L
txt = str(input("Enter the message you want to print on the shirt: "))

#prints message with size and message 
make_shirt(shirtsize,txt)