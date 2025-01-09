class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hi I am {self.first_name} {self.last_name}")


class Student(Person):
    def __init__(self, first_name, last_name, section_year, school_name):
        super().__init__(first_name, last_name)
        self.section_year = section_year
        self.school_name = school_name

    def introduce(self):
        super().introduce()
        print(f"I am student from {self.school_name}")

    def say_section(self):
        print(f"section is {self.section_year}")


class Employee(Person):
    def __init__(self, first_name, last_name, job_name, salary):
        super().__init__(first_name, last_name)
        self.job_name = job_name
        self.salary = salary

    def introduce(self):
        super().introduce()
        print(f"I work as a {self.job_name}")

    def say_salary(self):
        print(f"My salary is {self.salary}")


person_one = Person("Alieya", "Azarcon")
person_one.introduce()
print()

student_one = Student("Alyssa", "Villamer", "BSE 4B", "URS-A")
student_one.introduce()
student_one.say_section()
print()

employee_one = Employee("Carl", "Azarcon", "Software Engineer", 50_000)
employee_one.introduce()
employee_one.say_salary()
