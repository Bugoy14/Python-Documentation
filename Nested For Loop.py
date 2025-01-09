
# var = "Python"
# design = 20
# print(f"{var:~^{design}}")


# # REMOVES THE 'WWW.'
# links = [
#     "www.facebook.com",
#     "www.youtube.com",
#     "www.google.com",
#     "www.wikipedia.com"
# ]
#
# for link in links:
#     print(link[4:])
#     # print(link[:-4])

students = [
    ["BSIT", ["David", "Alenere"]],
    ["BSCS", ["Jaymar", "Emman", "Patrick"]]
]

for course in students:
    print(course[0])
    for student in course[1]:
        print(f" -{student}")
    print()
