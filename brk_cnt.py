students=("ram", "shyam", "radha", "rashmi", "amit")
for student in students:
    if student == "rashmi":
        break
    print(student)

students=("ram", "shyam", "radha", "rashmi", "amit")
for student in students:
    if student == "rashmi":
        continue
    print(student)
