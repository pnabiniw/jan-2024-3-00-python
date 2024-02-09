with open("message.txt", "r+") as fp:
    content = fp.read()
    new_content = content[1: 3]
    fp.seek(0)
    fp.write(new_content)

print("Successful !!")