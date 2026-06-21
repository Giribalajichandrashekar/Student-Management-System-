with open("test_students.txt", "w") as file:
    file.write("Hello, World\n")

with open("test_students.txt", "a") as file:
    file.write("next line\n")
    
with open("test_students.txt", "r") as file:
    content = file.read()
    
print(content)