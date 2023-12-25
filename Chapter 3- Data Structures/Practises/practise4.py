# Assume the lists numbers1 has 100 elements and numbers2 is an empty list. 
# Write code that copies the values in numbers to numbers2.

List = [i for i in range(1, 101)]  
numbers2 = []
numbers2 = List.copy()
print("numbers2:", numbers2)