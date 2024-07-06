def perform_operation(num1:float, num2:float,operation:str):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return 'Cannot devide by zero'
            else:
                return num1 / num2
            

        