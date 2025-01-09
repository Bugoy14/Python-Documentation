# +INDEX      0       1        2      3       4
# -INDEX     -5      -4       -3     -2      -1
courses = ["BSIT", "BSCS", "BLIS", "BSCpE", "BSEd", "BSIT"]
print(courses)


# READING LIST RANGE
# print(list[startIndex:endIndex])
# print(list[:endIndex])
# print(list[startIndex:])
print(courses[1:4])

# List Length
print(f"List Length: {len(courses)}")

# CHANGING VALUE IN A LIST
courses[3] = "Hatdog"

# List count /How many times an item repeat
print(f"Count of BSIT: {courses.count('BSIT')}")

# Add Items in a List / append (dulo ng list)
courses.append("Cheesedog")

# Add Items in a specified index (gitna ng list)
courses.insert(2,"BSHM")

# Delete items in a list
# courses.remove("Hatdog")
# courses.pop(0)
# del courses[0]

# CLearing a list
# courses.clear()

for course in courses:
    print(course, end=", ")

courses2 = ["longgadog", "hungarian"]
courses.extend(courses2)
print(courses)


numbers = [21, 123, 41, 413, 13]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print("-----------------------------------")

nestedList = ["BSIT", "BSCS", "BLIS", ["Hatdog", "Cheesedog", ["Shampoo", "Alcohol"]]]
print(nestedList[3][2][0])

# TUPLES (READ ONLY)
foods = ("Burger", "Pizza", "Chicken")
foods = list(foods)
# foods = tuple(foods)
print(foods)
