# Level 1 – *args


"""
Exercise 1:
Write a function total() that accepts any number of numbers and returns their sum.
"""


def total(*num) -> int:
    return sum(num)


print(total(1, 2, 3))

print(total(5, 10, 20, 30))


"""
Exercise 2
Write a function largest() that accepts any number of numbers and returns the largest.
"""


def largest(*args) -> int:
    return max(args)


print(largest(3, 9, 2, 8))
# 9


"""
Exercise 3
Write a function print_words() that prints each word on a new line.
"""


def print_words(*words):
    print(*words, sep="\n")
    # for word in words:
    #     print(word)


print_words("apple", "banana", "orange")


# Level 2 – **kwargs
# Write a function display_student() that accepts any keyword arguments and prints them like this:


def display_student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


display_student(name="Alice", age=20, grade="A")


"""
Exercise 5

Write a function create_profile() that returns the keyword arguments as a dictionary.
"""


def create_profile(**kwargs):
    return kwargs
    # return {key: value for key, value in kwargs.items()}


profile = create_profile(name="John", city="London")
print(profile)


"""
Exercise 6
Write a function that counts how many keyword arguments were passed.
"""


def count_kwargs(**kwargs):
    return len(kwargs)


count_kwargs(a=1, b=2, c=3)


# Level 3 – Mixing *args and **kwargs
"""
Exercise 7

Write a function that prints when called

Positional:
10
20
30

Keyword:
name = Tom
age = 25
"""


def info(*args, **kwargs):
    print("Positional:")
    for arg in args:
        print(arg)

    print("Keyword:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


info(10, 20, 30, name="Tom", age=25)


"""
Exercise 8
Write a function that calculates
the sum of all positional numbers
prints all keyword arguments

Sum: 35
city = Paris
country = France
"""


def report(*args, **kwargs):
    print(f"Sum: {sum(args)}")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


report(5, 10, 20, city="Paris", country="France")


# Level 4 – Unpacking with *
"""
Exercise 9: Call the function without writing the numbers manually.
"""

numbers = [10, 20, 30]


def add(a, b, c):
    return a + b + c


add(*numbers)


"""
Exercise 10: Call the function using unpacking.
"""
values = (2, 4, 6)


def multiply(a, b, c):
    return a * b * c


multiply(*values)


"""
Exercise 11: Call greet() using unpacking.
"""
names = ["Alice", "Bob", "Charlie"]


def greet(a, b, c):
    print(a)
    print(b)
    print(c)


greet(*names)


# Level 5 – Unpacking with **
"""
Exercise 12: Call the function using dictionary unpacking.
"""
person = {"name": "Alice", "age": 22}


def introduce(name, age):
    print(f"{name} is {age} years old.")


introduce(**person)


"""
Exercise 13: Call the function using **.
"""

car = {"brand": "Toyota", "year": 2022, "color": "Blue"}


def car_info(brand, year, color):
    print(brand, year, color)


car_info(**car)


"""
Exercise 14: Fix the code
"""


def employee(name, age):
    print(name, age)


data = {"name": "Sam", "age": 30}

employee(**data)


# Level 6 – Real-world Practice

"""
Exercise 15: Write a function Then call it
"""


def order(item, quantity, price):
    return f"Item: {item}\n" f"Quantity: {quantity}\n" f"Price: ${price:.2f}"


details = {"item": "Book", "quantity": 3, "price": 12.5}

print(order(**details))


"""
Exercise 16: Write a function Then call it
"""


def average(*numbers):
    print(sum(numbers) / len(numbers))


scores = [80, 90, 100, 70]

average(*scores)


"""
Exercise 17: Write a function and Call it using a dictionary.
"""


def send_email(to, subject, body, urgent=False):
    return f"To: {to} \nSubject: {subject}\nBody: {body}\nUrgent: {urgent}"


email = {
    "to": "forhad@abc.com",
    "subject": "Greetings from the dictionary calls",
    "body": "Hi, How are you?",
    "urgent": True,
}

print(send_email(**email))


# Challenge (Uses Everything)
"""
Create this function:
Requirements:

title is required.
Accept any number of numeric positional arguments.
Compute their average.
If round_result=True, round the average.
Print every extra keyword argument.
Call the function by unpacking both a list and a dictionary.

Expected output (approximately):

Scores
Average: 25
author = Alice
version = 2
"""


def process_data(title, *numbers, round_result=False, **extra):
    print(title)
    print(f"Avarage: {sum(numbers) / len(numbers)}")
    for k, v in extra.items():
        print(f"{k} = {v}")


nums = [10, 20, 30, 40]

options = {"round_result": True, "author": "Alice", "version": 2}

process_data("Scores", *nums, **options)
