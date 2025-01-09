# SETS ARE CURLY BRACES
evenNumbers = {2, 4, 6, 8, 10}
oddNumbers = [1, 3, 5, 7, 9]
evenNumbers.update(oddNumbers)

# evenNumbers.add(12)
# evenNumbers.remove(6)
# evenNumbers.discard(22)
# evenNumbers.pop()
# extension = evenNumbers.copy()


# for number in evenNumbers:
#     print(number, end=' ')

#                       UNION SET
# allNumbers = evenNumbers.union(oddNumbers)
# print(allNumbers)

# num1 = {1,2,3}
# num2 = {1,5,7}
# num3 = num1.union(num2)
# print(num3)


#                        DIFFERENCE
# setOne = {1,2,3,4,5}
# setTwo = {3,4}
# setThree = setOne.difference(setTwo)
# print(setThree)

#                       INTERSECTION
# setOne = {1,2,3,4,5}
# setTwo = {3,4}
# setThree = setOne.intersection(setTwo)
# print(setThree)

#                   SYMMETRIC DIFFERENCE
# setOne = {1,2,3,4,5}
# setTwo = {3,4,5,6,7}
# setThree = setOne.symmetric_difference(setTwo)
# print(setThree)

#                       DISJOINT SET
# setOne = {1,2,3,4,5}
# setTwo = {3,4,5,6,7}
# setThree = setOne.isdisjoint(setTwo)
# print(setThree)

#                    SUBSET and SUPERSET
# numbers = {1,2,3,4,5,6,7,8,9,10}
# evenNumbers = {2,4,6,8,10}
# setThree = numbers.issuperset(evenNumbers)
# print(setThree)




# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# evenNumbers = {2, 4, 6, 8, 10}
#
# numbers = list(numbers)
# numbers[0] = "Hatdog"
# print(numbers)
