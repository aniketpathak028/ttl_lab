# Write a program that keeps student's name and his marks in a dictionary as key-value pairs. The program should store records of 10 students and display students name and marks of five students in decreasing order of marks obtained.
# Create a dictionary to store student records
student_dict = {}

# Store records for 10 students
for i in range(10):
    # Get the student's name and marks
    name = input("Enter the name of student {}: ".format(i+1))
    marks = float(input("Enter the marks obtained by {}: ".format(name)))
    
    # Add the student's record to the dictionary
    student_dict[name] = marks

# Sort the dictionary by decreasing order of marks
sorted_dict = dict(sorted(student_dict.items(), key=lambda x: x[1], reverse=True))

# Display records for the top 5 students
print("Top 5 students by marks:")
count = 0
for name, marks in sorted_dict.items():
    if count < 5:
        print("{}: {}".format(name, marks))
        count += 1
    else:
        break