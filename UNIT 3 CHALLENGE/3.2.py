class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students = [
    Student("gayu", "G123", 3.8),
    Student("kishore", "k456", 3.5),
    Student("saran", "s789", 4.0),
    Student("karthik", "k101", 3.2),
    Student("gaya3", "G222", 3.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
