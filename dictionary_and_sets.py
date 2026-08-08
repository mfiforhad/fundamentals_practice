# -----------------
# Dictionary Basic
# -----------------

"""
Exercise 1: Student Grades
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
grades.update(David=88)
print(grades)
grades["Alice"] = 91
grades.pop("Charlie", "Not Found")
print(grades.keys())
print(grades.values())
print(grades.items())

"""
Exercise 2: Word Frequency
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
Exercise 3: Phone Book
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
phone_book.update(Jessie=88624584754)
phone_book.pop("Ying", "Not Found")
print(sorted(phone_book.items(), key=lambda x: x[0]))


"""
Exercise 4

Questions
1.	Add:
{
    "grape": 20,
    "banana": 25
}
2.	Add "mango" only if it doesn't already exist.
3.	Create a copy.
4.	Empty the original dictionary.

"""

inventory: dict[str, int] = {"apple": 30, "banana": 12, "orange": 18}

inventory.update(grape=20, banana=25)

inventory.setdefault("mango", 38)

inventory2 = inventory.copy()

inventory.clear()
print(inventory)

print(inventory2)


"""
Exercise 5
Find
•	Highest-priced product
•	Lowest-priced product
•	Total inventory value
"""
prices: dict[str, int] = {"Laptop": 850, "Mouse": 25, "Keyboard": 50}
print(max(prices.items(), key=lambda item: item[1]))
print(min(prices.items(), key=lambda item: item[1]))
print(sum(prices.values()))


# Part 3: Dictionary Comprehensions

"""
Exercise 6
Given
numbers = [1,2,3,4,5]
Create
{
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
"""
numbers = [1, 2, 3, 4, 5]

sqr_numbers = {n: n**2 for n in numbers}

print(sqr_numbers)


# Exercise 7
"""
Given
students = {
    "Alice":88,
    "Bob":61,
    "Charlie":95,
    "David":58
}
Create a new dictionary containing only students with marks ≥70.
"""
students = {"Alice": 88, "Bob": 61, "Charlie": 95, "David": 58}

filtered_students = {
    student: marks for student, marks in filter(lambda x: x[1] >= 70, students.items())
}

print(filtered_students)


"""
Convert
{
    "a":1,
    "b":2,
    "c":3
}
into
{
    1:"a",
    2:"b",
    3:"c"
}
"""

primary_dictionary = {"a": 1, "b": 2, "c": 3}

converted_dictionary = {value: key for key, value in primary_dictionary.items()}

print(converted_dictionary)


# Part 4: Sets
"""
Exercise 9
Create
A = {1,2,3,4}
B = {3,4,5,6}
Find
•	Union
•	Intersection
•	Difference
•	Symmetric difference
"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C: set[int] = A | B
D: set[int] = A & B
E: set[int] = A - B
F: set[int] = A ^ B
print(f"Union: {C}")
print(f"Intersection: {D}")
print(f"Difference: {E}")
print(f"Symmetric difference: {F}")


"""
Exercise 10
Using methods
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
Compare them with the operators above.
"""

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_difference_set = A.symmetric_difference(B)

print(union_set)
print(intersection_set)
print(difference_set)
print(symmetric_difference_set)


# Exercise 11
"""
Practice
add()
remove()
discard()
pop()
clear()
Questions
•	Add 10
•	Remove 5
•	Try removing 100
•	What's the difference between remove() and discard()?
"""
my_set = {5, 9, 6, 2}
my_set.add(10)
my_set.remove(5)
my_set.discard(100)
my_set.pop()
print(my_set)
"""The difference between remove() and discard() is raising KeyError. using remove() returns a KeyError if not found and discard() doesn't raise any error"""

"""
Part 5: Set Comprehensions
Exercise 12
Given
numbers = [1,2,2,3,3,4,5,5]
Create a set of squares.
Expected
{1,4,9,16,25}
"""
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
print(set(number**2 for number in numbers))


"""
Exercise 13
Given
words = ["Apple","Banana","APPLE","banana"]
Create a set containing unique lowercase words.
Expected
{"apple","banana"}
"""
words = ["Apple", "Banana", "APPLE", "banana"]
words_sorted = sorted(words)
print(words_sorted)
print(set(word.lower() for word in words))
print({word.lower() for word in words})

# Part 6: Real-World Problems
# Exercise 14: Website Visitors

"""
Find
•	New visitors
•	Returning visitors
•	Visitors who came only yesterday
"""
# %%
today = {"Alice", "Bob", "David", "John"}
yesterday = {"Bob", "David", "Emma", "Frank"}

new_visitors = today - yesterday
returning_visitors = today & yesterday
yesterday_visitors = yesterday - today
print(f"New Visitors: {new_visitors}")
print(f"Returning Visitors: {returning_visitors}")
print(f"Yesterday Visitors: {yesterday_visitors}")


# Exercise 15: Shopping Cart
"""
Calculate
•	Total bill
•	Most expensive purchased item
•	Average item price
"""

cart = {"Apple": 4, "Banana": 2, "Milk": 1}

prices = {"Apple": 30, "Banana": 15, "Milk": 80}

# print(f"Total bill: {sum(cart * price for cart, price in zip(cart.values(), prices.values(), strict=True))}")

print(sum(value * prices[key] for key, value in cart.items()))

print(
    f"Most expensive purchased item: {max(cart, key=lambda item: cart[item] * prices[item])}"
)

print(f"Average item price: {round(sum(prices.values()) / len(prices.values()), 2)}")

print(f"Expensive Product: {max(prices, key= lambda item: prices[item])}")


# Exercise 16: Inventory Merge
"""
Warehouse A
{
    "Pen":40,
    "Book":20,
    "Pencil":60
}
Warehouse B
{
    "Book":15,
    "Pen":30,
    "Eraser":50
}
Merge them by adding quantities.
Expected
{
    "Pen":70,
    "Book":35,
    "Pencil":60,
    "Eraser":50
}
"""
Warehouse_A: dict[str, int] = {"Pen": 40, "Book": 20, "Pencil": 60}
Warehouse_B: dict[str, int] = {"Book": 15, "Pen": 30, "Eraser": 50}

merged_warehouse: dict[str, int] = {**Warehouse_A}

for key, value in Warehouse_B.items():
    merged_warehouse[key] = value + merged_warehouse.get(key, 0)

print(merged_warehouse)


# Exercise 17: Employee Department Lookup

"""
Create
{
    "Sales":[101,105],
    "IT":[102,104],
    "HR":[103]
}
"""

employees = {101: "Sales", 102: "IT", 103: "HR", 104: "IT", 105: "Sales"}

department = {}

for key, value in employees.items():
    department.setdefault(value, []).append(key)

print(department)


# Exercise 18: Common Skills
"""
Find
•	Common skills
•	Skills only Alice has
•	Skills only Bob has
•	All unique skills
"""

alice = {"Python", "SQL", "Excel", "Power BI"}

bob = {"Python", "Java", "SQL", "AWS"}

common_skills = alice & bob
print(common_skills)
alice_skills = alice - bob
print(alice_skills)
bob_skill = bob - alice
print(bob_skill)
unique_skill = alice ^ bob
print(unique_skill)


# Exercise 19: Log Analysis
"""
Create
{
    "INFO":3,
    "ERROR":3,
    "WARNING":1
}
Then determine the most frequent log level.
"""


logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO"]

logs_analysis = {}

for k in logs:
    logs_analysis[k] = logs.count(k)  # logs_analysis.get(k, 0) + 1

most_frequent_log = max(logs_analysis.values())

print(most_frequent_log)


# Exercise 20: Movie Recommendations
"""
•	Common movies
•	Movies to recommend to User A
•	Movies to recommend to User B
"""


user_a = {"Inception", "Interstellar", "Avatar", "Titanic"}

user_b = {"Titanic", "Avatar", "The Matrix", "Dune"}

common_movies = user_a & user_b

recommended_user_a = user_b - user_a

recommended_user_b = user_a - user_b

print(f"Common movies: {common_movies}")
print(f"Movies to recommend to User A: {recommended_user_a}")
print(f"Movies to recommend to User B: {recommended_user_b}")
