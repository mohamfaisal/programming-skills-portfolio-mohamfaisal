# Python have collection of data in the form of key pair value, there is a key and there is a value.
# key is immutable buit value is against key is mutable 
# curly braces used in dictionary - operators are used to check data (in , not in)
#len function used for list -tuple -dictionary 


# Creation of dictionary 

dictionary = {}
print(dictionary)


# Check the type od dictionary 

dictionary ={}
print(dictionary, type(dictionary))


# Another way to create dictionary 

dictionary = dict()
print(dictionary, type(dictionary))


# To add something in dictionary 

example = {'color' : 'red', 'fruit' : 'apple', 'place' : 'United Arab Emirates'}
print(example)


# To add some value in dictionary 

dictionary = {'Name' : 'Mohammed', 'Roll No' : '1234', 'Fathers name' : 'faisal'}
print(dictionary, type(dictionary))   # Name, roll no are keys and mohammed, 1234 are values 


# lets check if we want to return one value, so its is a dictionary 

dictionary = {'Name' : 'Mohammed', 'Roll No' : '1234', 'Fathers name' : 'faisal'}
print(dictionary['Name'], type(dictionary))


# Testing dictionary 

dictionary = {'Name' : 'Mohammed', 'Roll No' : '1234', 'Fathers name' : 'faisal'}
print(dictionary['student']) # there is an exception that this key is not in the dictionary 

                                # OR 

# We can use get method to check whether the student is available in the dict or not 

dictionary = {'Name' : 'Mohammed', 'Roll No' : '1234', 'Fathers name' : 'faisal'}
print(dictionary.get("student"))


# As student is not in dict we get None , lets assign a default value to avoid exception 

dictionary = {'Name' : 'Mohammed', 'Roll No' : '1234', 'Fathers name' : 'faisal'}
print(dictionary.get("student", "Anmol"))















# To add some value in dictionary 
example = {'color' : 'red',
            'fruit' : 'apple',
              'place' : 'united arab emirates'}
print(example)

# to know particular key from many key's 
example = {'color' : 'red',
            'fruit' : 'apple',
              'place' : 'united arab emirates'}
print(example["color"],type(example))       #"color" (double quotes for showing particular key)

# or another way of doing the upper one 
example = {'color' : 'red',
            'fruit' : 'apple',
              'place' : 'united arab emirates'}
print(example.get("color"))                  # using 'get' method and without writing 'type'

# To check hw many keys are in our dictionary 
example = {'color' : 'red',
            'fruit' : 'apple',
              'place' : 'united arab emirates'}
print(example.keys())  

        




