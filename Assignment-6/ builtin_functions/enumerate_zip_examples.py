# Sample lists
students = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]

# ----------------------------
# enumerate()
# ----------------------------

print("Student List:")

# Print index and student name
for index, student in enumerate(students):
    print(index, student)

# ----------------------------
# zip()
# ----------------------------

# Combine two lists
student_marks = list(zip(students, marks))

print("\nStudents and Marks:")

for student, mark in student_marks:
    print(student, "-", mark)

# ----------------------------
# sorted()
# ----------------------------

numbers = [40, 10, 70, 20, 50]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("\nAscending Order:", ascending)
print("Descending Order:", descending)

# ----------------------------
# Type Conversion
# ----------------------------

number_string = "100"
decimal_string = "45.75"
number = 500

print("\nInteger:", int(number_string))
print("Float:", float(decimal_string))
print("String:", str(number))
