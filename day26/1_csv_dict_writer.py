import csv

students = [
    {'id': '1', 'name': 'Jon', 'age': '30', 'address': 'KTM'},
    {'id': '2', 'name': 'Jane', 'age': '45', 'address': 'PKR'},
    {'id': '3', 'name': 'Ken', 'age': '21', 'address': 'BKT'},
    {'id': '4', 'name': 'Ram', 'age': '34', 'address': 'BKT'},
    {'id': '5', 'name': 'Raj', 'age': '22', 'address': 'BKT'},
]


with open("filtered.csv", "w") as cw:
    fields = students[0].keys()
    csv_writer = csv.DictWriter(cw, fieldnames=fields)
    csv_writer.writeheader()
    for student in students:
        if student["address"] == "KTM" or int(student["age"]) > 30:
            csv_writer.writerow(student)

print("CSV created !!")
