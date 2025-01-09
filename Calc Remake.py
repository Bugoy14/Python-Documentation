while True:
    try:
        inputOne = float(input("First number: "))
        while True:
            try:
                operation = input("Operation (+ - x / % // ^): ")
                if len(operation) == 1 and operation in '+-x/^%':
                    break
                elif operation == '//':
                    break
            except ValueError:
                print("Enter a valid operator")
        while True:
            try:
                inputTwo = float(input("Enter second number: "))
                break
            except ValueError:
                print("Please enter a valid number")
        break
    except ValueError:
        print("Enter a valid number")

result_dict = {
    '+': inputOne + inputTwo,
    '-': inputOne - inputTwo,
    'x': inputOne * inputTwo,
    '/': inputOne / inputTwo,
    '//': inputOne // inputTwo,
    '^': inputOne ** inputTwo,
    '%': inputOne % inputTwo
}

if operation in result_dict:
    print(f"{inputOne} {operation} {inputTwo} = {result_dict[operation]}")
else:
    print(f"{operation} is not in the dictionary")
