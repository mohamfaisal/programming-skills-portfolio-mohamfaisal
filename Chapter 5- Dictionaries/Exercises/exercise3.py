# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
# to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "list": "A data structure in Python that stores multiple itemsin a squared brackets.",
    "dictionary": "A data structure in Python that stores key-value pairs in a curly brackets.",
    "Tuple": "A collection data type that is immutable and ordered.",
    "Control Flow": "A program's control flow is the order in which the program's code executes.",
    "Data Structure": "A way of organizing and storing data so that they can be accessed and worked with efficiently",
    "if statement": "A programming construct that allows the program to make decisions.",
    "Variables": "Python variables are simply containers for storing data values.",
    "Comments": "Comments in Python are identified with a hash symbol, #, and extend to the end of the line.",
    "For Loop": "A programming construct that allows code to be executed repeatedly.",
    "Functions": "A function is a block of code which only runs when it is called."

}

for word, meaning in glossary.items():
    print(word + ":")
    print(meaning)
    print("\n")