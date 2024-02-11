import pickle

with open("info.dat", "rb") as fp:
    name = pickle.load(fp)   # Deserialization
    age = pickle.load(fp)
    address = pickle.load(fp)

print(name)
print(age)
print(address)
