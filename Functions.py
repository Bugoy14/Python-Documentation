
# def add(num_one, num_two):
#     return num_one + num_two
#
#
# user_input: int = int(input("Enter first number: "))
# user_input2: int = int(input("Enter second number: "))
#
# print(add(user_input, user_input2))

def squared(number):
    # return number * number
    return number ** 2


user_input: int = int(input("Input: "))

result = squared(user_input)

print(f"Output: {result}")
