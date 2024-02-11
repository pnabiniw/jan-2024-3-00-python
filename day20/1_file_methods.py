# read(), write()

filename = "info.txt"
with open(filename, "w") as fp:
    fp.write("Hello World\nI am learning file handling")


with open(filename, "r") as fp:
    print(fp.readline())
    fp.seek(0)
    print(fp.readlines())
    print(fp.tell())


data = ['Hello World\n', 'Python is high level language']
with open(filename, "w") as fp:
    fp.writelines(data)
