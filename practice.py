# rows = int(input("Enter number of rows: "))
#
# def right_triangle(n): return '\n'.join(map(lambda i: '*' * i, range(1, n+1)))
# def inverted_right_triangle(n): return '\n'.join(map(lambda i: '*' * i, range(n, 0, -1)))
#
# print(right_triangle(rows))
# print()
# print(inverted_right_triangle(rows))


# class MotorcycleBrand():
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#         print(f"Brand Name: {name}")
#         print(f"Model: {model}")
#         print(f"Year: {year}")
#         print()
#
#
# honda = MotorcycleBrand("Honda", "Winner X", 2024)
# yamaha = MotorcycleBrand("Yamaha", "Sniper 150R", 2024)
# suzuki = MotorcycleBrand("Suzuki", "Raider 150 fi", 2023)

# import mysql.connector
#
# my_database = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='alieya30',
#     database='dbschool',
#     autocommit=True
# )
#
#
# my_cursor = my_database.cursor()
#
# my_sql_query = "SELECT * FROM tblstudents"
#
# try:
#     my_cursor.execute(my_sql_query)
# except Exception as e:
#     print(f"Error {e}")
#
# my_result = my_cursor.fetchall()
#
# for item in my_result:
#     print(item)

while True:
    try:
        user_input = int(input("Enter number: "))
        break
    except ValueError:
        print("Whole numbers only!")
# # container = []
# #
# # while user_input > 0:
# #     container.append(user_input)
# #     user_input -= 1
# #
# # container.sort()
# # even_numbers = [i for i in container if i % 2 == 0]
# # even_numbers = list(filter(lambda i: i % 2 == 0, container))
# # odd_numbers = [i for i in container if i % 2 != 0]
even_numbers = [i for i in range(1, user_input + 1) if i % 2 == 0]
odd_numbers = [i for i in range(user_input + 1) if i % 2 != 0]

print("Even: ", end='')
print(', '.join(str(i) for i in even_numbers))
print("Odd: ", end=' ')
print(', '.join(str(i) for i in odd_numbers))

names = ["Carl", "Alyssa", "Alieya", "Bugoy", "Lalay", "Ali"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}")


name_list = []
while True:
    user_input = input("Enter first name: ")
    user_input1 = input("Enter last name: ")
    person = Person(user_input, user_input1)
    name_list.append(person)

    choice = input("Continue to add names? yes or no: ").lower()
    if choice in ['y', 'yes', 'yea']:
        pass
    else:
        break

for name in name_list:
    name.introduce()
