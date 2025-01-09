# identifier = {
#     "key1" : "value1",
#     "key2" : "value2",
#     "key3" : "value3"
# }
studentOneAttributes = {
    "Height": 172,
    "Weight": 63,
    "Skin": "Brown"
}

studentOne = {
    "name": "Carl",
    "course": "CpE",
    "age": 23,
    "physical": studentOneAttributes
}

studentTwo = {
    "name": "Alyssa",
    "course": "BSE",
    "age": 24
}

students = [studentOne, studentTwo]

# print(studentOne.get("name"))
# print(studentTwo["name"])
#
# studentOne["name"] = "Bugoy"
# print(studentOne["name"])

# print(len(studentOne))

# studentOne["sex"] = "Male"
# print(studentOne)

# studentOne.popitem()
# studentOne.pop("name")
# studentOne.clear()

# print(studentOne.keys())
# print(studentOne.values())

print(students[0]["physical"]["Height"])
# print(students[1].get("name"))
