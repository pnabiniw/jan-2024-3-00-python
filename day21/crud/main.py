from create import create_student
from delete import delete_student
from update import update_student
from read import read_student


def crud_student():
    selection = input("Enter your choice (c/r/u/d/e) ")
    selection = selection.lower()

    def exit_message():
        print("Thank you. See you again !!")

    if selection == "c":
        cont = create_student()
        crud_student() if cont else exit_message()
    elif selection == "r":
        cont = read_student()
        crud_student() if cont else exit_message()
    elif selection == "u":
        cont = update_student()
        crud_student() if cont else exit_message()
    elif selection == "d":
        cont = delete_student()
        crud_student() if cont else exit_message()
    else:
        exit_message()


if __name__ == '__main__':
    crud_student()
