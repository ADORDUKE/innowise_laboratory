"""The Student Grade Analyzer"""
from random import choice
from typing import TypedDict, Optional


class Student(TypedDict):
    name: str
    grades: list[float]


def add_a_grade_for_a_student(students:list[Student]) -> None:
    name_student = input("Enter student name: ").strip()
    stud = find_a_student(students, name_student)

    if stud:
        while True:
            grade = input("Enter a grade (or 'done' to finish): ").strip()
            if grade == "done":
                break

            if grade.isdigit():
                if 0 <= int(grade) <= 100:
                    stud.get("grades").append(int(grade))
                else:
                    print("Invalid grade. Please enter a value between 0 and 100.")
                    continue
            else:
                print("Invalid input. Please enter a number.")
                continue
    else:
        print("Student not found")





def calc_avg(student: dict) -> float | None:
    grades = student["grades"]
    return sum(grades) / len(grades) if grades else None




def find_a_student(students:list[Student], name_stud) -> Student | None:
    for stud in students:
        if stud.get("name").strip().lower() == name_stud.strip().lower():
            return stud
    return None


def add_a_new_student(students: list[Student]) -> None:
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


def show_report(students:list[Student]) -> str | None:
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


def find_top_performer(students) ->None:
    highest_average = max(students, key=lambda x: calc_avg(x))
    print(f"The student with the highest average is {highest_average.get("name")} with a grade of {calc_avg(highest_average)}")






def menu() -> None:
    """Show the menu"""
    print("\n---Student Grade Analyzer---")
    print("1. Add a new Student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit the program")


def main():
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

