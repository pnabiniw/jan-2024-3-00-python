import pickle

name = "Jon"
age = 30
address = "KTM"

with open("info.dat", "wb") as fp:
    pickle.dump(name, fp)  # Serialization
    pickle.dump(age, fp)
    pickle.dump(address, fp)

print("Successful !!")