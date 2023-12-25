# Void function 
def print_message():
    print("Hello Students")
# Calling function 
print_message()

# Local variable 
def print_message():
    message = "Hello Students"   # Local variable 
    print(message)
# Calling Function 
print_message()

# Different functions have same local variables name - No syntax error 

def print_message():
    message = "hy"
    print(message)

def print_message_2():
    message ="hello"
    print(message)
