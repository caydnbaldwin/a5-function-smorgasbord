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