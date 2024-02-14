import json
filename = "students.json"


# def update_student():
#     id = input("Enter the student id ")
#     which_info = input("Enter the info you want to change ")
#     new_info = input(f"Enter the new {which_info} ")
#
#     with open(filename, "r+") as fp:
#         students = json.loads(fp.read())
#         for student in students:
#             if student["id"] == id:
#                 student[which_info] = new_info
#                 break
#         else:
#             print("Invalid student id")
#             want_to_continue = input("Do you want to continue? (y/n)")
#             return True if want_to_continue.lower() == 'y' else False
#         fp.seek(0)
#         fp.write(json.dumps(students, indent=2))
#
#     print("Student Updated Successfully")
#     want_to_continue = input("Do you want to continue? (y/n)")
#     return True if want_to_continue.lower() == 'y' else False



def update_student():
    id = input("Enter the student id ")
    which_info = input("Enter the info you want to change ")
    new_info = input(f"Enter the new {which_info} ")

    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        filtered_student = list(filter(lambda x: x['id'] == id, students))
        if filtered_student:
            student = filtered_student[0]
            student[which_info] = new_info
        else:
            print("Invalid Student id")
            want_to_continue = input("Do you want to continue? (y/n)")
            return True if want_to_continue.lower() == 'y' else False
        fp.seek(0)
        fp.write(json.dumps(students, indent=2))

    print("Student Updated Successfully")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False
