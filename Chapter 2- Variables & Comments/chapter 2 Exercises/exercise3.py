#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
#Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed. 
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#Define a variable to represent a person's name
name = "\tFaisal\n"

#Print the name once, so the whitespace around the name is displayed
print("Original name:", name)

#Print the name using each of the three stripping functions
print("Name after lstrip():", name.lstrip())
print("Name after rstrip():", name.rstrip())
print("Name after strip():", name.strip())