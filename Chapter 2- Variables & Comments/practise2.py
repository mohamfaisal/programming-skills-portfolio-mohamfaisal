# Write a python program that takes courses marks as input and then calculates average of all the courses. 
# After calculating the average, calculate the percentage of a student using total marks. 
# Assume the total of all the courses marks is 500 or take the total marks from the user as input.

# Function to calculate the average
def calculate_average(course_marks):
    return sum(course_marks) / len(course_marks)

# Function to calculate the percentage
def calculate_percentage(average, total_marks):
    return (average / total_marks) * 100

# Take courses marks as input
course_marks = list(map(int, input("Enter the marks for each course separated by space: ").split()))

# Take the total marks from the user as input
total_marks = int(input("Enter the total marks: "))

# Calculate average of all the courses marks
average = calculate_average(course_marks)

# Calculate the percentage of a student using total marks
percentage = calculate_percentage(average, total_marks)

# Print the average and percentage
print("The average marks for all the courses is:", average)
print("The percentage of a student is:", percentage) 