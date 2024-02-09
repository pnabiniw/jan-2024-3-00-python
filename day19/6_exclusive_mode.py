# If a file is already created and we try to open that file in exclusive mode then it raises error


with open("messg.txt", "x") as fp:
    fp.write("Sth")
