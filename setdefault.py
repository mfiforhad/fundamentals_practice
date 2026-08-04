# Group Students by grade


person: list[str] = ["Forhad", "Alice", "Nick", "John"]
grades: list[str] = ["A", "B", "B", "A"]

group: dict[str, list[str]] = {}

for name, grade in zip(person, grades, strict=True):
    group.setdefault(grade, []).append(name)

print(group)


# Group Students by Subject

students: list[tuple[str, str]] = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("David", "Science"),
    ("Eva", "Math"),
]

students_group: dict[str, list[str]] = {}

for name, subject in students:
    students_group.setdefault(subject, []).append(name)

print(students_group)


# Word Positions :
"""
expected output
{
    "apple": [0, 2, 5],
    "banana": [1, 4],
    "orange": [3]
}"""
words: list[str] = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_position: dict[str, list[int]] = {}

for index, word in enumerate(words):
    word_position.setdefault(word, []).append(index)

print(word_position)


# Group by First Letter
"""
Expected output
{
    "a": ["apple", "ant"],
    "b": ["banana", "boat"],
    "c": ["cat", "car"]
}
"""
fruits: list[str] = ["apple", "ant", "banana", "boat", "cat", "car"]

first_letter_group: dict[str, list[str]] = {}

for fruit in fruits:
    first_letter_group.setdefault(fruit[:1], []).append(fruit)

print(first_letter_group)


# Counting
"""
Expected output
{
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 1
}
"""

numbers: list[int] = [2, 1, 3, 2, 2, 1, 4, 5, 1]

counting: dict[int, int] = {}

for num in sorted(numbers):
    counting.setdefault(num, numbers.count(num))

print(counting)


# count letter

"""
{
    "m": 1,
    "i": 4,
    "s": 4,
    "p": 2
}
"""

text: str = "mississippi"

count_letter: dict[str, int] = {}

for letter in text:
    count_letter.setdefault(letter, text.count(letter))

print(count_letter)


# Nested Dictionaries

sales = [
    ("Alice", "Book", 2),
    ("Alice", "Pen", 5),
    ("Bob", "Book", 1),
    ("Alice", "Book", 1),
    ("Bob", "Pen", 2),
]

employee: dict[str, dict[str, int]] = {}

for name, item, qty in sales:
    employee.setdefault(name, {}).setdefault(item, qty)

print(employee)


# Challenge (Most Important) -> Build a dictionary from this list:

"""
Expected output
{
    "Math": {
        "Alice": 95,
        "Charlie": 91,
        "Eva": 99
    },
    "Science": {
        "Bob": 88,
        "David": 85
    }
}
"""


data = [
    ("Math", "Alice", 95),
    ("Science", "Bob", 88),
    ("Math", "Charlie", 91),
    ("Science", "David", 85),
    ("Math", "Eva", 99),
]

subject_wise_data: dict[str, dict[str, int]] = {}

for subject, name, mark in data:
    subject_wise_data.setdefault(subject, {}).setdefault(name, mark)

print(subject_wise_data)
