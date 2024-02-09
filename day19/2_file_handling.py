# We can manipulate files (read, write, append, close) using Python (or any other programming language)
# There are several modes in which we can open a file
# 1. Read Mode (r)
# 2. Write Mode (w)
# 3. Append (a)
# 4. Read and Write (r+)
# 5. Write and Read (w+)
# 6. Append and Read (a+)
# 7. Exclusive Write (x)

# 8. Read Binary (rb)
# 9. Write Binary (wb)

fp = open("message.txt", "w")
fp.write("Hello I am learning file handling")
fp.close()
print("Successful !!")

fp = open("message.txt", "w")
try:
    fp.write("Hello I am learning file")
except:
    print("Something Went Wrong")
else:
    print("Successful !!")
finally:
    fp.close()

# If we open file in write mode then it overrides the previous content
