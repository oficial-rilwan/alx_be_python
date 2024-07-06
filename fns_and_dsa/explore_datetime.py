from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date=current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)


display_current_datetime()

def calculate_future_date():
    number_of_days = int(input('Enter the number of days: '))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(future_date)

calculate_future_date()