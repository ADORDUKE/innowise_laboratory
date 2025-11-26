"""The Student Grade Analyzer
A simple console program for managing student records, adding grades,
calculating averages, and generating reports.
"""


from typing import TypedDict


class Student(TypedDict):
    """ Representation of a student record.

    Attributes:
        name (str): The student's name.
        grades (list[float]): A list of numeric grades (0–100).

    """
    name: str
    grades: list[float]


def add_a_grade_for_a_student(students:list[Student]) -> None:
    """Add grades to an existing student.

       Prompts the user for a student's name, searches for that student,
       and then repeatedly asks for grades until the user types 'done'.
       Only numeric grades between 0 and 100 are accepted.

       Args:
           students (list[Student]): List of student records.
    """

    name_student = input("Enter student name: ").strip()
    stud = find_a_student(students, name_student)

    if stud:
        while True:
            grade = input("Enter a grade (or 'done' to finish): ").strip()
            if grade == "done":
                break

            try:
                value = float(grade)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if not (0 <= value <= 100):
                print("Grade must be between 0 and 100.")
                continue

            stud["grades"].append(value)
    else:
        print("Student not found")


def calc_avg(student: Student) -> float | None:
    """Calculate the average grade of a student.

        Args:
            student (Student): A student record.

        Returns:
            float | None: The average grade, or None if no grades exist.
    """

    grades = student["grades"]
    return sum(grades) / len(grades) if grades else None




def find_a_student(students:list[Student], name_stud: str) -> Student | None:
    """Find and return a student by name.

        The search is case-insensitive and ignores extra whitespace.

        Args:
            students (list[Student]): List of student records.
            name_stud (str): Name of the student to search for.

        Returns:
            Student | None: The found student, or None if not found.
    """

    for stud in students:
        if stud.get("name").strip().lower() == name_stud.strip().lower():
            return stud
    return None


def add_a_new_student(students: list[Student]) -> None:
    """Add a new student to the list.

    Prompts the user for a name. If a student with this name already
    exists (case-insensitive), the function prints a warning.

    Args:
        students (list[Student]): List of student records.
    """

    name_student = input("Enter student name: ").strip()

    if find_a_student(students, name_student):
        print("Student already exists")
    else:
        students.append(
            Student(
                name=name_student,
                grades=list()
            )
        )


def show_report(students:list[Student]) -> None:
    """Print a full report of student averages and overall statistics.

    For each student, prints either the average grade or "N/A" if no grades exist.
    Then prints the maximum, minimum, and overall average of all available averages.

    Args:
        students (list[Student]): List of all student records.
    """

    averages: list[float] = []


    if len(students) == 0:
        print("Students not found")
        return None

    print("--- Student Report ---")
    for stud in students:
        try:
            avg_grades = calc_avg(stud)
        except ZeroDivisionError:
            print("Division by zero")

        if avg_grades is None:
            print(f"{stud.get('name')}'s average grade is N/A.")
        else:
            print(f"{stud.get('name')}'s average grade is {avg_grades}.")
            averages.append(avg_grades)


    print("-" * 26)
    print(f"Max Average: {max(averages)}")
    print(f"Min Average: {min(averages)}")
    print(f"Overall Average: {sum(averages) / len(averages)}")

    return None


def find_top_performer(students: list[Student]) -> None:
    """Determine and print the student with the highest average grade.

    Students without any grades are ignored. If no students have grades,
    the function prints a warning.

    Args:
        students (list[Student]): List of student records.
    """

    students_with_grades = [s for s in students if s.get("grades")]

    if not students_with_grades:
        print("No grades found to determine top performer.")
        return

    highest_average = max(students, key=lambda x: calc_avg(x))
    print(f"The student with the highest average is {highest_average.get("name")} with a grade of {calc_avg(highest_average)}")


def menu() -> None:
    """Display the main menu options."""

    print("\n---Student Grade Analyzer---")
    print("1. Add a new Student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit the program")


def main() -> None:
    """Entry point of the program.

    Handles the menu loop, user choices, and dispatching to action functions.
    """
    students = []

    actions = {
        1: add_a_new_student,
        2: add_a_grade_for_a_student,
        3: show_report,
        4: find_top_performer,


    }

    while True:
        menu()
        try:
            choice_action = int(input("Enter your choice: "))
            if choice_action == 5:
                print("Exiting the program.")
                break
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        action = actions.get(choice_action)

        if action:
            action(students)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

