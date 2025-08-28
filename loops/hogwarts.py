# students = ["Harry","Ron","Hermione"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i,students[i])

# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Sytherin"
# }

# for student in students:
#     print(student,students[student], sep=', ')

students = [
    {"name":"Harry","house":"Gryffindor","petronus":"Stag"},
    {"name":"Hermione","house":"Gryffindor","petronus":"Otter"},
    {"name":"Ron","house":"Gryffindor","petronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Sytherin","petronus":None}
]

for student in students:
    print(student['name'],student['house'],student['petronus'], sep=", ")