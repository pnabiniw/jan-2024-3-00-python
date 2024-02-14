import json

filename = "students.json"


def delete_student():
    id = input("Enter student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student['id'] == id:
                students.remove(student)
                break
        else:
            print("Invalid student id")
            want_to_continue = input("Do you want to continue? (y/n)")
            return True if want_to_continue.lower() == 'y' else False
    with open(filename, "w") as fp:
        fp.write(json.dumps(students))

    print("Student deleted successfully !!")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False

