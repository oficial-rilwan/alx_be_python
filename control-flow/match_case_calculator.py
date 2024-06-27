num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        print(f"The result is {num_1 + num_2}.")
    case "-":
        print(f"The result is {num_1 - num_2}.")
    case "*":
        print(f"The result is {num_1 * num_2}.")
    case "/":
        if operator == '/' and num_2 == 0:
            print('Cannot devide by zero')
        else:
            print(f"The result is {num_1 / num_2}.")
