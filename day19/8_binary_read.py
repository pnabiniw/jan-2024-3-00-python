import pickle

with open("info.dat", "rb") as fp:
    name = pickle.load(fp)   # Deserialization
    age = pickle.load(fp)
    address = pickle.load(fp)

print(name)
print(age)
print(address)


students = ["Jon", "Jane", "Hary", "Alex"]
# Write the above list in a binary file "student.dat"

# Read the binary file and create a dictionary with information of student and their respective exam marks
# Finally write the info again to the binary file "marks.dat"
