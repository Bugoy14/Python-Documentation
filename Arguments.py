
#             Arbitrary, Keyword Arguments
#                  ^        ^
# def print_names(*names, last_name):
#     for name in names:
#         print(f"Hello, {name} {last_name}")
#
# print_names("Carl", "Alyssa", "Alieya", last_name="Azarcon")


#   Arbitrary Keyword Argument
# def students(**student):
#     print(student["name"])
#     print(student["course"])
#     print(student["age"])
#     print(student["average"])
#
# students(name="Carl", age=23, course="CpE", average=90)


def summation(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
#   return sum(numbers)

print(summation(1,2,3,4,5,6,7,8,9,10))
