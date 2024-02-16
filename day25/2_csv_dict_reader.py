import csv
from estd_connection import estd_connection
filename = "students.csv"

cursor = estd_connection()

with open(filename, "r") as cr:
    students = csv.DictReader(cr)
    for student in students:
        id = student['id']
        age = student['age']
        name = student["name"]
        address = student["address"]
        sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE, ADDRESS) VALUES ('{name}', {age}, '{address}')
        """
        cursor.execute(sql)
