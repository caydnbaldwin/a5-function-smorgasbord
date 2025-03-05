# Caydn Baldwin
# IS 303
# A5 - Function Smorgasbord

# Function 1: welcome_message
def welcome_message(name):
    print(f"Hello {name}, welcome to IS 303!")

# call function
welcome_message("Diego")
welcome_message("Mai")

# Function 2: sum_two_numbers
def sum_two_numbers(a, b):
    return a + b

# call function
print(sum_two_numbers(5, 7))
print(sum_two_numbers(1000.5, -30))

# Function 3: is_even
def is_even(num):
    return num % 2 == 0

# call function
print(is_even(7))
print(is_even(120))

# Function 4: get_number_parity
def get_number_parity(num):
    if is_even(num):
        return f"{num} is even."
    else:
        return f"{num} is odd."

# call function
print(get_number_parity(5))
print(get_number_parity(10))

# Function 5: fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# call function
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

# call function
print(min_max_mean([20, 45, 23, 2, 87, 3]))

# Function 7: dog_message
def dog_message(name, age=0):
    return f"I am a dog named {name} and I'm {age} years old!"

# call function
print(dog_message("Spot", 7))
print(dog_message("Peppy"))

# Function 8: classify_age
def classify_age(age, senior_age=65):
    if age < 18:
        return "Minor"
    elif age < senior_age:
        return "Adult"
    else:
        return "Senior"

# call function
print(classify_age(60, 55))
print(classify_age(62))

# Function 9: calculate_total
def calculate_total(price, quantity, discount_percent, threshold_total=100, bonus_discount=0.02):
    total_price = price * quantity
    if total_price <= threshold_total:
        return total_price * (1 - discount_percent)
    elif total_price > threshold_total:
        return total_price * (1 - (discount_percent + bonus_discount))

# call function
for i in range(0, 2):
    price = float(input("Enter the price for the product purchased: "))
    quantity = int(input("Enter the quantity of the product purchased: "))
    discount_percent = float(input("Enter the discount percent (formatted as a decimal): "))
    print(f"The total price after discounts is: ${round(calculate_total(price, quantity, discount_percent), 2)}")