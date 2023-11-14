# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a 
# different message.

def make_shirt( size, message ):
  print("Your Shirt size is",size,"and it says",message,)
First_shirt = "Large" 
text = "I Love Python" 
Second_shirt = "Medium"
make_shirt(First_shirt,text)  
make_shirt(Second_shirt,text)