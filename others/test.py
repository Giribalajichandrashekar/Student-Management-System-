file = open("test_students.txt", "a")
file.write("\nHello World")
file.close()

file = open("test_students.txt", "r")
content = file.read()
print (content)
file.close() 