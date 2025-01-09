
# ODD OR EVEN CHECKER BASED ON USER INPUT
numbers = []
userInput = int(input("Enter a number: "))

while userInput > 0:
    numbers.append(userInput)
    userInput -= 1
else:
    numbers.sort()
#   numbers.reverse()

oddEvenCheck = [[],
                []]

for number in numbers:
    if number % 2 == 0:
        oddEvenCheck[0].append(number)
    else:
        oddEvenCheck[1].append(number)


for row in oddEvenCheck:
    for items in row:
        print(items, end=' ')
    print()

# USER AUTHENTICATION USING FORLOOP IN RANGE
# username = ["John", "Alenere", "David"]
# password = ["abc123", "123abc", "hahatdog"]
#
# usernameInput = input("Username: ")
# passwordInput = input("Password: ")
#
# for x in range(len(username)):
#     if usernameInput == username[x] and passwordInput == password[x]:
#         print(f"Welcome, {username[x]}")
#         break
# else:
#     print("Account not found!")

