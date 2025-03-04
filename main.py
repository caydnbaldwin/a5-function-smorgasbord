# Caydn Baldwin
# IS 303
# A5 - Function Smorgasbord

# Function 1: welcome_message
def welcome_message(name):
    print(f"Hello {name}, welcome to IS 303!")

welcome_message("Diego")
welcome_message("Mai")

# Function 2: sum_two_numbers
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(5, 7))
print(sum_two_numbers(1000.5, -30))

# Function 3: is_even
def is_even(num):
    return num % 2 == 0

print(is_even(7))
print(is_even(120))

# Function 4: get_number_parity
def get_number_parity(num):
    if is_even(num):
        return f"{num} is even."
    else:
        return f"{num} is odd."
    
print(get_number_parity(5))
print(get_number_parity(10))

# Function 5: fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(75))

# Function 6: min_max_mean
def min_max_mean(numbers_list):
    lowest_number = None
    highest_number = None
    total = 0

    for number in numbers_list:
        if (lowest_number is None) or (number < lowest_number):
            lowest_number = number
        elif (highest_number is None) or (number > highest_number):
            highest_number = number
        total += number    
    return [lowest_number, highest_number, (total / len(numbers_list))]

print(min_max_mean([20, 45, 23, 2, 87, 3]))