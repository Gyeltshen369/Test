# Initialize empty lists and dictionary
students_list = []
students_dict = {}

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student information added successfully.")

# Function to display all students' information
def display_students():
    print("\nStudent Information:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

# Function to search for a student
def search_student():
    name = input("Enter student's name to search: ")
    if name in students_dict:
        info = students_dict[name]
        print(f"\nStudent found - Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("Student not found.")

# Function to remove a student
def remove_student():
    name = input("Enter student's name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

# Main menu
while True:
    print("\n===== Student Information Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        remove_student()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
