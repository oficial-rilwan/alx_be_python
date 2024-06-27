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
        print(f"The result is {num_1 / num_2}.")
