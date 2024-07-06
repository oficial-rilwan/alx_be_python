FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {result}°C")

def convert_to_fahrenheit(celsius):
    result = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}°C is {result}°F")

user_input = int(input("Enter the temperature to convert: "))
conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match conversion_type:
    case 'F':
        convert_to_celsius(user_input)
    case 'C':
        convert_to_fahrenheit(user_input)
    