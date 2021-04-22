import datetime
from helpers import sum_two_numbers

result = 12


def turn_light_on():
    print("The light is turned on")


def get_current_time_formatted(label):
    # turn_light_on()
    return f"{label}{datetime.datetime.now()}"


# ... read file
# time_now = datetime.datetime.now()
# print(get_current_time_formatted("The time is: "))

my_age = 35
# result = 12

print(sum_two_numbers(my_age, 5))
# print(result)
