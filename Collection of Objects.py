is_running = True


class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section
        # print(f"{name} Created!")

    def print_students(self):
        print(f"   Name   : {self.name}")
        print(f"   Course : {self.course}")
        print(f"   Year   : {self.year}")
        print(f"   Section: {self.section.upper()}")


print("Student Registration System")
student_list = []
while is_running:
    user_name = input("Enter name: ")
    user_course = input("Enter course: ")
    user_year = input("Enter year: ")
    user_section = input("Enter section: ")
    student_n = Student(user_name, user_course, user_year, user_section)
    student_list.append(student_n)
    print()

    while True:
        user_choice = input("Register more? Y/N: ").lower()
        if user_choice in ['y', 'yes']:
            print()
            break
        elif user_choice in ['n', 'no']:
            is_running = False
            break
        else:
            print("Invalid Choice!")

for person in student_list:
    counter = 1
    print(f"{'':->20}")
    print(f'Student #{counter}')
    person.print_students()
    counter += 1
