
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
#
# numbers_one = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers_one))
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers_one))
# print(f"Even: {even_numbers}")
# print(f"Odd: {odd_numbers}")

user_input = int(input("Enter number: "))
container = []

while user_input > 0:
    container.append(user_input)
    user_input -= 1

container.sort()
even_numbers = list(filter(lambda x: x % 2 == 0, container))
odd_numbers = list(filter(lambda x: x % 2 != 0, container))

print(f"Even: ")
for number in even_numbers:
    print(number, end=" ")

print(f"\nOdd: ")
for number in odd_numbers:
    print(number, end=" ")
