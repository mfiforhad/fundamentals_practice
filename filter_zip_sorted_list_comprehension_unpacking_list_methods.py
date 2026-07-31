# **********************
# Part 1: filter()
# **********************

# all even numbers


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even: list[int] = list(filter(lambda x: x % 2 == 0, numbers))

# remove empty string

words: list[str] = ["apple", "", "banana", "", "kiwi", "grape"]

removed_empty_string: list[str] = list(filter(lambda a: a != "", words))

# Use filter() to keep only students with grades 60 or above.

students: list[tuple[str, int]] = [
    ("Alice", 85),
    ("Bob", 45),
    ("Charlie", 72),
    ("David", 38),
]

pass_students: list[tuple[str, int]] = list(filter(lambda n: n[1] >= 60, students))

# **********************
# Part 2: zip()
# **********************

# Combine these lists:

names: list[str] = ["Alice", "Bob", "Charlie"]
scores: list[int] = [90, 85, 78]

combined_list = list(zip(names, scores))


# Print: Japan -> Tokyo Canada -> Ottawa Brazil -> Brasilia using zip().

countries = ["Japan", "Canada", "Brazil"]
capitals = ["Tokyo", "Ottawa", "Brasilia"]

for x in zip(countries, capitals):
    print(f"{x[0]} -> {x[1]}")

for country, capital in zip(countries, capitals):
    print(f"{country} -> {capital}")


# Use zip() to calculate the total cost.

prices = [5, 8, 12]
quantities = [2, 3, 4]

total_2 = sum(price * quantity for price, quantity in zip(prices, quantities))


# **********************
# Part 3: sorted()
# **********************

# sort by ascending

numbers = [8, 2, 6, 1, 9, 3]

sort_number = sorted(numbers)

# sort by length

words = ["pear", "banana", "kiwi", "apple"]

sorted_by_length = sorted(words, key=len)


# Sort students by grade from highest to lowest.

students = [("Alice", 80), ("Bob", 95), ("Charlie", 70), ("David", 90)]

sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)

# **********************
# Part 4: List Comprehension
# **********************

# Create a list of squares from 1 to 10.

squares = [num**2 for num in range(1, 11)]

# Create a new list containing only even numbers.

numbers = [3, 7, 10, 14, 15]

even_numbers = [num for num in numbers if num % 2 == 0]

# Create a list of word lengths.

words = ["python", "java", "go", "rust"]

word_lengths = [len(w) for w in words]

# uppercase list

uppercase_list = [item.upper() for item in ["apple", "banana", "kiwi"]]


# **********************
# Part 5: Unpacking
# **********************

# Unpack it into three variables.

person = ("Alice", 25, "Engineer")

name, age, job = person

# Unpack the first value into first, the last into last, and everything else into middle

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

# Swap the values without using a temporary variable.

point = (4, 7)
x, y= point

x, y = y, x


# **********************
# Part 6: List Methods
# **********************

# Use a list method to add 4.

numbers = [1, 2, 3]

numbers.append(4)


# to the same list using a list method.

numbers = [1, 2, 3]

numbers.extend([4, 5, 6])


# Remove the first "green".

colors = ["red", "green", "blue", "green"]

colors.remove("green")


# Sort the list in place.

numbers = [5, 2, 8, 1]

numbers.sort()


# Reverse the list without using sorted().

letters = ["a", "b", "c", "d"]

letters.reverse()

# **********************
# Mixed Practice
# **********************

# Combine them using zip().
# Keep only students with scores ≥ 80 using filter().
# Sort them by score (highest first).

names = ["Alice", "Bob", "Charlie"]
scores = [88, 65, 91]

sorted(
    filter(lambda x: x[1] >= 80, zip(names, scores, strict=True)),
    key=lambda a: a[1],
    reverse=True,
)

# Remove empty strings using filter().
# Sort by length.
# Create a list of uppercase words using list comprehension.

words = ["apple", "", "banana", "kiwi", "", "pear"]

uppercase_words = [
    item.upper() for item in sorted(filter(lambda x: x != "", words), key=len)
]

print(uppercase_words)

# Keep employees earning at least 65000.
# Sort by salary descending.
# Extract just the employee names using list comprehension.

employees = [("Alice", 70000), ("Bob", 50000), ("Charlie", 90000), ("David", 65000)]

employee_names = [
    name[0]
    for name in sorted(
        filter(lambda x: x[1] >= 65000, employees), key=lambda i: i[1], reverse=True
    )
]


# Exercise 25 (Challenge)

"""
Use filter() to keep only products with stock greater than 5.
Use sorted() to sort them by price (highest first).
Use list comprehension to create strings like:
"Phone ($800)"
Use unpacking in your loop.
Use zip() with another list of categories:
categories = ["Electronics", "Electronics", "Electronics", "Accessories"]

to pair each product with its category.
"""

products = [
    ("Laptop", 1200, 5),
    ("Phone", 800, 10),
    ("Tablet", 600, 4),
    ("Monitor", 300, 8),
]

product_pr = [
    f"{name} (${price})"
    for name, price, stock in sorted(
        filter(lambda i: i[2] > 5, products), key=lambda z: z[1], reverse=True
    )
]

product1, product2 = product_pr

categories = ["Electronics", "Electronics", "Electronics", "Accessories"]

for (name, price, stock), category in zip(products, categories):
    print(category, name)
