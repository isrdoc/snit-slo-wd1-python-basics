result = 12

def sum_two_numbers(number_a, number_b):
    result = number_a + number_b

    def inner_function():
        thing = "chair"
        print(thing)
        print(result)

    inner_function()

    return result

# def print(value_to_print):
#     # side effect
#     return None

my_age = 35
# result = 12

print(sum_two_numbers(my_age, 5))
print(result)
