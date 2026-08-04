# -----------------
# Dictionary Basic
# -----------------

"""
Tasks:
•	Print Bob's grade.
•	Add "David": 81.
•	Update Alice's grade to 91.
•	Remove Charlie.
•	Print all student names.
•	Print all grades.
•	Print all (name, grade) pairs.
Practice methods
•	get()
•	keys()
•	values()
•	items()
•	pop()
"""

grades: dict = {"Alice": 88, "Bob": 72, "Charlie": 95}

print(grades.get("Bob"))
grades["Alice"] = 91
grades.pop("Charlie", "Not Found")
print(grades.keys())
print(grades.values())
print(grades.items())

"""
Count how many times each word appears.
Expected:
{
    "python": 2,
    "is": 2,
    "fun": 1,
    "and": 1,
    "powerful": 1
}
Practice:
•	get()
•	Looping
•	Dictionary updates
"""

sentence = "python is fun and python is powerful"

expected_dictionary: dict[str, int] = {
    word: sentence.count(word) for word in sentence.split()
}

print(expected_dictionary)


"""
Create a phone book dictionary.
Tasks:
•	Search a person safely.
•	Add a new contact.
•	Delete a contact.
•	Print all contacts alphabetically.
Methods:
•	get()
•	pop()
•	sorted()
"""
phone_book = {
    "Mustarin": 8801706362529,
    "Deepak": 60123345027,
    "Forhad": 8801643794060,
    "Ying": 8801710921084,
}

phone_book.get("Forhad")
phone_book.update(Jessie = 88624584754)
phone_book.pop("Ying", "Not Found")
print(sorted(phone_book.items(), key=lambda x: x[0]))

inventory = {"apple": 30, "banana": 12, "orange": 18}
