"""
Day 1-2: Variables, Strings, f-strings, Arithmetic
Python Crash Course - Chapter 2
Date: Aug 30, 2026
"""

# --- Variables & basic print ---
print("Gautham Reddy Rachamallu")

city = "Hyderabad"
print(city)

age = 19
print(age)

first_name = "Gautham"
last_name = "Reddy Rachamallu"
print(first_name, last_name)

# --- String methods: .upper() / .lower() / .title() ---
word = "hyderabad"
print(word.upper())   # HYDERABAD
print(word.lower())   # hyderabad
print(word.title())   # Hyderabad

# --- f-strings: the professional way to build sentences ---
print(f"Welcome to {city.title()}!")
print(f"Your full name is {first_name} {last_name}.")

# --- String concatenation with + (and why it fails on numbers) ---
greeting = "Hello, " + "World" + "!"
print(greeting)

# age is an int, so "+" between a string and an int raises a TypeError.
# Fixed two ways:
print("I am " + str(age) + " years old")
print(f"I am {age} years old")

# --- Arithmetic operators ---
price = 250
quantity = 3
print(f"Total: {price * quantity}")   # 750

print(10 % 3)    # 1  -> modulo gives the remainder
print(7 / 2)     # 3.5 -> normal division, always float
print(7 // 2)    # 3   -> floor division, drops the decimal
print(2 ** 3)    # 8   -> power


# --- Functions: return vs. print ---
# Key lesson: print() only displays a value and throws it away.
# return hands the value back to whoever called the function so it can be reused.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(4))   # True
print(is_even(7))   # False
