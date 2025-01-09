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


# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def introduce(self):
#         print(f"Hi I am {self.first_name} {self.last_name}")
#
#
# class Student(Person):
#     def __init__(self, first_name, last_name, section, school_name):
#         super().__init__(first_name,last_name)
#         self.section = section
#         self.school_name = school_name
#
#     def introduce(self):
#         super().introduce()
#         print(f"I am a student from {self.school_name} and my section is {self.section}")
#
#
# class Employee(Person):
#     def __init__(self, first_name, last_name, job, years_exp):
#         super().__init__(first_name,last_name)
#         self.job = job
#         self.years_exp = years_exp
#
#     def introduce(self):
#         super().introduce()
#         print(f"I work as {self.job} and I have {self.years_exp} years of experience")
#
#
# person_one = Person("Bugoy", "Azarcon")
# student_one = Student("Alyssa", "Villamer", "BSE 4B", "URS-A")
# employee_one = Employee("Carl", "Azarcon", "Programmer", 1)
#
# person_one.introduce()
# student_one.introduce()
# employee_one.introduce()

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

# my_list = ["Carl", "Alyssa", "Alieya", "Bugoy", "Lalay", "Ali"]
#
# for index, name in enumerate(my_list, start=1):
#     print(index, name)

