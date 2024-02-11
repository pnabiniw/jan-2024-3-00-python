## Reading the binary file

import pickle
with open("output.dat", "rb") as fp:
    students = pickle.load(fp)

print(students)



