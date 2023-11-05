# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    "list": "A data structure in Python that stores multiple itemsin a squared brackets.",
    "dictionary": "A data structure in Python that stores key-value pairs in a curly brackets.",
    "Control Flow": "A program's control flow is the order in which the program's code executes.",
    "Data Structure": "A way of organizing and storing data so that they can be accessed and worked with efficiently",
    "if statement": "A programming construct that allows the program to make decisions."
}

for word, meaning in glossary.items():
    print(word + ":")
    print(meaning)
    print("\n")