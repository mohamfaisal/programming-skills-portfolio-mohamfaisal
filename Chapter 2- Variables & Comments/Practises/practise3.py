# Write a python program that takes an input 5 from user and then type cast those values to string, int
# and float in the separate variables. Print all the variables
# Function to calculate the average

def calculate_average(course_marks):
    return sum(course_marks) / len(course_marks)

# Function to calculate the percentage
def calculate_percentage(average, total_marks):
    return (average / total_marks) * 100

# Take courses marks as input from the user
course_marks = list(map(int, input("Enter the marks for each course separated by space: ").split()))

# Take the total marks from the user as input
total_marks = int(input("Enter the total marks: "))

# Calculate average of all the courses marks
average = calculate_average(course_marks)

# Calculate the percentage of a student using total marks
percentage = calculate_percentage(average, total_marks)

# Type cast the values to string, int and float
str_marks = list(map(str, course_marks))
int_marks = list(map(int, course_marks))
float_marks = list(map(float, course_marks))

# Print all the variables
print("String Marks:", str_marks)
print("Integer Marks:", int_marks)
print("Float Marks:", float_marks)
print("Average Marks:", average)
print("Percentage of a student:", percentage)