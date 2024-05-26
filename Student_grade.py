num_students = int(input("Enter the number of student: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_subjects = int(input(f"Enter the number of subject for the student {i}: "))

    for j in range(1, num_subjects + 1):
        grade = float(input(f"Enter the subject{j} grade of the student {i} :"))
        total_grade += grade

    average_grade = total_grade / num_students
    print(f"Average grade of student{i} : {average_grade:.2f}")
    i+=1
    
