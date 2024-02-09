fp = open("message.txt", "r")
content = fp.read()
fp.close()
print(content)

fp = open("message.txt", "r")
try:
    content = fp.read()
except Exception as e:
    print(e)
    print("Sth Went Wrong")
else:
    print(content)
finally:
    fp.close()


# We can use context managers which closes the file automatically
with open("message.txt", "r") as fp:
    content = fp.read()
    print(content)  # Prints the content before closing the file

# File closes automatically after execution the "with" block
print(content)  # Prints the content after closing the file
