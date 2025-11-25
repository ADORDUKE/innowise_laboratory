"""The Student Grade Analyzer"""
from random import choice
from typing import TypedDict, Optional



class Student(TypedDict):
    name: str
    grades: list[int]

def find_a_student(students:list[Student], name) -> bool | None:
    for stud in students:
        if stud.get("name").strip().lower() == name.strip().lower():
            return True
    return None


def add_a_new_student(students: list[Student]) -> None:
    name_student = input("Enter student name: ").strip()

    if find_a_student(students, name_student):
        print("Student already exists")
    else:
        students.append(
            Student(name=name_student,
                    grades=list()
                    )
        )






def menu() -> None:
    """Show the menu"""
    print("\n---Student Grade Analyzer---")
    print("1. Add a new Student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit the program")


def main():
    menu()


    students = [
        {
            "name": "Bob",
            "grades": []
        }
    ]


    actions = {
        1: add_a_new_student,
    }

    choice_action = int(input("Enter your choice: "))

    action = actions.get(choice_action)

    if action:
        action(students)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

