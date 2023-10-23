#homogeneous list / python supports heterogeneous list other than C, java
names =["faisal","creative computing","codlab"]
print(names)

#heterogeneous list 
student =["Mohammed Faisal","Bathspa","year 1","89.56"]
print(student)

#repetition of a single list multiple times 
numbers =[1,2,3,4]
new_numbers = numbers * 5
print(new_numbers)

#indexing (0,1,2,3.....)
#positive indexing starts from 0
numbers =[5,6,7,8,3,4]
print(numbers[3])

#negative indexing starts from -1
numbers =[5,6,7,8,3,4]
print(numbers[-4])

#lens function ( to know how much is the length of the list)
numbers =[1,2,3,4,45,5,6,67,7,8,8,99,9,65,54,33,23]
print("number of elements in a list :" ,len(numbers))

#list is mutable (changeble / update your list)
numbers =[5,6,7,8,3,4]
numbers[0] = 1
numbers[1] = 9
print(numbers)

#concatenation ( mixing of different list together )
List_1 =[2,3,4,5,6]
List_2 =[9,8,7,6,5]
List_3 =[List_1 + List_2]
print(List_3)

#List slicing ( taking a portion from a part of list )
new_list =[1,2,3,10,15,6,7]
result = new_list [3:5]  # 2nd index exclusive index - 0-2 index, 3rd one is not counted eg:-(5)
print(result)

#Find elements in list  -if operator
new_list =[1,2,3,4,5,6,7,8,9]
if 10 in new_list:
    print("found")
else:
    print("not found")

#(not in) operator
new_list2 =[1,2,3,4,5,6,7,8,9]
if 20 not in new_list2:
    print("yes")
else:
    print("no")

#built in methods - append
New_list3 =[4,5,6,6,7]
New_list3.append(100)
print(New_list3)

#built in methods - index (to identify index of the particular string or int from the list)
New_list4 =[4,5,6,6,7]
print(New_list4.index(7))  #to identify index of 7

#built in methods - sort (to arrange in order wise)
New_list5 = [4,7,6,3,1]
New_list5.sort()
print(New_list5)

#built in methods - reverse (to reverse the string/int from right hand side )
New_list6 = [4,7,6,3,1]
New_list6.reverse()
print(New_list6)

#built in methods - remove (to remove a particular string/int from the list)
New_list7 = [4,7,6,3,1]
New_list7.remove(6)
print(New_list7)

#min max number
print(max(New_list7))     #(to identify the highest value from the list)
print(min(New_list7))