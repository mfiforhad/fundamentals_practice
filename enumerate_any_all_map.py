# **********************
#  Part 1: enumerate()
# **********************

# Print the index and value of each fruit.


fruits = ["apple", "banana", "kiwi", "mango"]

# solution 1:
for i, item in enumerate(fruits):
    print(f"{i}: {item}")

# solution 2:
[print(f"{i}: {item}") for i, item in enumerate(fruits)]

# Print the items starting from 1 instead of 0.

# solution 1:
for i, item in enumerate(fruits, start=1):
    print(f"{i}: {item}")


# solution 2:
[print(f"{i}: {item}") for i, item in enumerate(fruits, start=1)]

# Print only the indices where the score is 90 or higher.

scores = [78, 95, 82, 60, 99]

[
    print(f"Student {student} scored {score}")
    for student, score in enumerate(scores)
    if score >= 90
]

# Create a dictionary where the keys are the indices.

letters = ["a", "b", "c", "d"]

created_dictionary = {key: value for key, value in enumerate(letters)}
print(created_dictionary)


# Print each character with its position.

sentence = "Python"

[print(f"{index} -> {letter}") for index, letter in enumerate(sentence)]


# **********************
#  Part 2: any()
# **********************


# Check if any number is even.
numbers = [1, 3, 5, 8, 9]

print(any(number for number in numbers if number % 2 == 0))


# Check if any word starts with "z".

words = ["apple", "banana", "kiwi"]

print(any(letter for letter in words if letter == "z"))


# Determine whether any user is an admin.

users = [
    {"name": "Alice", "admin": False},
    {"name": "Bob", "admin": False},
    {"name": "Charlie", "admin": True},
]

any(user["admin"] for user in users)


# Exercise 6: Check if any number is even. Expected: True

numbers = [1, 3, 5, 8, 9]

any(num % 2 == 0 for num in numbers)


# Exercise 7: Check if any word starts with "z". Expected: False

words = ["apple", "banana", "kiwi"]

any(word.startswith("z") for word in words)

# Check if any temperature is greater than 28.

temperatures: list[int] = [18, 21, 25, 17, 30]

any(temp > 28 for temp in temperatures)


# <====> Part 3: all() <====>

# Check if all numbers are even. Expected: True

numbers = [2, 4, 6, 8, 3]

print(all(num % 2 == 0 for num in numbers))


# Check whether all passwords have at least 8 characters.

passwords = ["Python123", "Secret456", "abc"]

all(len(password) >= 8 for password in passwords)


# Check if all grades are at least 60.

grades = [80, 76, 91, 85]

all(grade >= 60 for grade in grades)


# Check if all emails end with "@gmail.com".

emails = [
    "alice@gmail.com",
    "bob@gmail.com",
    "charlie@yahoo.com",
]

all(email.endswith("@gmail.com") for email in emails)

# --------------------------
# Part 4: map()
# --------------------------

# Use map() to square every number.

numbers = [1, 2, 3, 4, 5]

(map(lambda num: num**2, numbers))


# Convert every word to uppercase using map().

words = ["apple", "banana", "kiwi"]

list(map(lambda x: x.upper(), words))


# Convert the strings into integers using map().

prices = ["100", "250", "75", "60"]

list(map(lambda price: int(price), prices))

# %%
# Capitalize every name using map().

names = ["alice", "bob", "charlie"]

list(map(lambda x: x.capitalize(), names))

# %%

# Convert Celsius to Fahrenheit using: F = C × 9/5 + 32

temperatures_c = [0, 20, 35]

list(map(lambda c: c * 9 / 5 + 32, temperatures_c))


# ================
# Mixed Practice
# ================

# Use enumerate() to number the students.
# Use any() to check if anyone failed (score < 50).
# Use all() to check if everyone scored at least 40.
# Use map() to extract only the student names.

students = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 91),
    ("David", 76),
]


"""


Exercise 19

Given:



Exercise 20

Given:

products = [
    ("Laptop", 1200),
    ("Phone", 800),
    ("Tablet", 600),
    ("Monitor", 300),
]
Use enumerate(start=1) to print a numbered product list.
Use any() to determine whether any product costs more than 1000.
Use all() to determine whether all products cost at least 250.
Use map() to create a list of prices with a 10% discount applied.
Challenge
Exercise 21

Given:

employees = [
    {"name": "Alice", "salary": 70000, "active": True},
    {"name": "Bob", "salary": 50000, "active": False},
    {"name": "Charlie", "salary": 90000, "active": True},
    {"name": "David", "salary": 65000, "active": True},
]

Complete all of the following:

Print the employees numbered from 1 using enumerate().
Use any() to check if any employee earns more than 80000.
Use all() to check if every employee is active.
Use map() to create a list containing only employee names.
Use map() again to create a list of salaries increased by 5%.
Print the names of employees whose increased salary exceeds 75000.

These exercises will help you understand not just the syntax of enumerate(), any(), all(), and map(), but also when each is a natural fit in everyday Python code.
"""

# %%
