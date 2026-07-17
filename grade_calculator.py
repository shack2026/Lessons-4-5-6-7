def main():
    grades = []

    while True:
        grade = int(input("Enter your grade or -1 to stop: "))

        if grade == -1:
            break
        else:
            grades.append(grade)

    print("Grades entered:")
    print(grades)

    print("\\nRemoving the lowest grade")
    lowest_grade = min(grades)
    lowest_index = grades.index(lowest_grade)
    grades.pop(lowest_index)
    print(grades)

    print("\\nRemoving a random grade")
    random_grade = choice(grades)
    grades.remove(random_grade)
    print(grades)

    print("\\nEditing a grade")

    for index, grade in enumerate(grades, start=1):
        print(f"{index}. {grade}")

    grade_to_edit = int(input("Enter the number of the grade you would like to edit: "))

    while grade_to_edit > len(grades) or grade_to_edit < 1:
        print("Error: That number is not in the list.")
        grade_to_edit = int(input("Enter the number of the grade you would like to edit: "))

    new_grade = int(input("Enter the new grade: "))
    grades[grade_to_edit - 1] = new_grade
    print(grades)

    print("\\nSorting and reversing the list")
    grades.sort()
    grades.reverse()
    print(grades)

    print("\\nGetting the grade total and average")
    total = sum(grades)
    print("Total:", total)

    average = sum(grades) / len(grades)
    print("Average:", average)

    print("Completed by, Asekun Shackleford")

if __name__ == "__main__":
    main()

path = Path("/mnt/data/grade_calculator.py")
path.write_text(code)

print(f"Created: {path}")
