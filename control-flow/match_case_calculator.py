num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print(f"The result is {num_1 + num_2}.")
    case "-":
        print(f"The result is {num_1 - num_2}.")
    case "*":
        print(f"The result is {num_1 * num_2}.")
    case "/":
        if num_2 == 0:
            print('Cannot devide by zero.')
        else:
            print(f"The result is {num_1 / num_2}.")
