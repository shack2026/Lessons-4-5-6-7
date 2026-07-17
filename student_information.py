def main():
    # Create an empty dictionary to store student information
    student_information = {}

    # Add students using each student's name as the key
    student_information["Ayorinde Shackleford"] = {
        "ID": 1001,
        "GPA": 3.7,
        "Credits Completed": 45,
        "Grades": [90, 85, 93, 88]
    }

    student_information["Jordan Smith"] = {
        "ID": 1002,
        "GPA": 3.4,
        "Credits Completed": 38,
        "Grades": [82, 87, 91, 84]
    }

    student_information["Taylor Johnson"] = {
        "ID": 1003,
        "GPA": 3.9,
        "Credits Completed": 52,
        "Grades": [95, 92, 97, 94]
    }

    # Print the dictionary containing all student information
    print("Student Information Dictionary:")
    print(student_information)

    # List all student names
    print("\nListing Student Names:")
    for student_name in student_information:
        print(student_name)

    # Access and display student information
    print("\nAccessing Student Information:")
    print("Name\t\t\tID\tGPA\tCredits Completed\tGrades")

    # Use items() to access both the student name and information
    for student_name, information in student_information.items():
        print(
            f"{student_name}\t"
            f"{information['ID']}\t"
            f"{information['GPA']}\t"
            f"{information['Credits Completed']}\t\t\t"
            f"{information['Grades']}"
        )

    # Remove a student using pop()
    print("\nRemoving a Student:")
    removed_student = student_information.pop("Jordan Smith")
    print("Removed Student:", removed_student)

    print("\nUpdated Student Information Dictionary:")
    print(student_information)

    # Access GPA information using get()
    print("\nAccessing GPA Information:")
    for student_name, information in student_information.items():
        student_gpa = information.get("GPA")
        print(f"{student_name}'s GPA: {student_gpa}")

    # Clear the student registry
    print("\nClearing the Student Registry:")
    student_information.clear()

    # Print the dictionary to confirm it is empty
    print(student_information)

    # Assignment completion statement
    print("\nCompleted by, Ayorinde Shackleford")


if __name__ == "__main__":
    main()
