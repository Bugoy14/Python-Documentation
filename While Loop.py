
# mySet = ["hatdog", "cheesedog", "pencil", "ruler", "eraser", "ballpen"]
# i = 0
# while i < len(mySet):
#     print(mySet[i])
#     i += 1


numbers = [13,134,2452,167,25,86572,364568,345,7456]
counter = 0
odd = []
even = []

while counter < len(numbers):
    if numbers[counter] % 2 == 0:
        even.append(numbers[counter])
    else:
        odd.append(numbers[counter])
    counter += 1



print("Odd: ")
for i in odd:
    print(i, end= ' ')


print("\n\nEven: ")
for i in even:
    print(i, end= ' ')


# chances = 3
# rightAnswer = 3.14
#
# while True:
#     userInput = float(input("What is approximately value of Pi: "))
#     if userInput == rightAnswer:
#         print("CORRECT")
#         break
#     else:
#         print(f"Chances left: {chances}")
#         chances -= 1
#         if chances < 0:
#             print("Sorry you failed")
#             break
#
# while chances > 0:
#     userInput = float(input("What is approximately value of Pi: "))
#     if userInput == rightAnswer:
#         print("CORRECT")
#         break
#     else:
#         chances -= 1
#         print(f"Chances left: {chances}")
# else:
#     print("Sorry You Failed")
