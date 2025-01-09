
# age = int(input("Enter your age: "))
# height = int(input("Enter your height: "))
#
#
# print(f"Age: {age} \nHeight: {height}")
#
# if age >= 18:
#     print("Legal Age and", end=' ')
#     if height >= 167:
#         print("you are tall")
#     else:
#         print("you are short")
#
# else:
#     print("Underage and", end=' ')
#     if height >= 167:
#         print("you are tall")
#     else:
#         print("you are short")

gradeOne = float(input("first grade: "))
gradeTwo = float(input("second grade: "))
gradeThree = float(input("third grade: "))
average = (gradeOne + gradeThree + gradeTwo) / 3

if average > 100 or average <= 50:
    print("Invalid Grade")
elif average >= 98:
    print("Highest Honor")
elif average >= 95:
    print("High Honor")
elif average >= 90:
    print("With Honor")
elif average >= 75:
    print("Passed")
else:
    print("Failed")
