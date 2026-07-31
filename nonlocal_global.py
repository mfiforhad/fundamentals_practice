# ------------------------
# Global Practice
# ------------------------


"""
1. Global Counter

    -Create a global variable count = 0.
    -Write a function that increments count by 1 each time it is called.
    Call it five times and print the result.
"""

count = 0


def increment() -> None:
    global count
    count += 1


print(count)
increment()
increment()
increment()
increment()
print(count)


"""
Global Configuration

    Create a global variable tax_rate = 0.08.
    Write a function that updates the tax rate.
    Write another function that calculates the final price using the current tax rate.
"""
tax_rate = 0.08


def product_price() -> tuple:
    print(f"current tax rate is: {tax_rate}")

    def update_tax(n) -> None:
        global tax_rate
        tax_rate += n
        print(f"total tax after adding {n}: {tax_rate}")

    def final_price(amount) -> None:
        final_amount = amount + tax_rate
        print(f"total after added {tax_rate} with amount {amount}: {final_amount}")

    return update_tax, final_price


update_tax, final_price = product_price()

update_tax(3)
final_price(20)

# 2. Bank Balance

balance = 1000


def deposit(amount):  # -> Any:
    global balance
    balance += amount
    return balance


def withdraw(amount):
    global balance
    balance -= amount
    return balance


deposit(500)
withdraw(200)
print(balance)

"""
3. Global Greeting
Create:

greeting = "Hello"

Write a function that changes it to "Welcome".

Print before and after.
"""
greeting = "Hello"
print(greeting)


def greet():
    global greeting
    greeting = "Welcome"
    return greeting


greet()
print(greeting)

"""
4. Global Maximum
Create:highest = 0

Write a function check(score) that updates highest if score is larger.

Example:

check(50)
check(90)
check(80)
print(highest)

Output: 90
"""
highest = 0


def check(number):
    global highest
    if number > highest:

        highest = number
        return highest


check(50)
check(90)
check(80)
print(highest)

"""
5. Global List
Create a global list:
items = []

Write:

add_item(item)
remove_item(item)
Modify the same global list.
"""

items = []


def add_item(item):
    global items
    return items.append(item)


def remove_item(item):
    global items
    return items.remove(item)


print(items)
add_item(23)
print(items)
remove_item(23)
print(items)


# ------------------------
# Nonlocal Practice
# ------------------------

"""
Simple Counter
Write an outer function that initializes:

count = 0

Return an inner function that increases count using nonlocal.

Example:

counter = make_counter()
print(counter())
print(counter())
print(counter())

Output:

1
2
3
"""


def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


counter = make_counter()
print(counter())
print(counter())
print(counter())
print(counter())

"""
Score Keeper
Create:

def game():
    score = 0

Return two inner functions:

add(points)
show()
Both should work on the same score.
"""


def game():
    score = 0

    def add(points):
        nonlocal score
        score += points
        return score

    def show():
        return score

    return add, show


add, show = game()

print(add(10))
print(show())


"""
Secret Password
Create:

def password_manager():
    password = "python123"

Return:

change(new_password)
display()
Use nonlocal to update the password.
"""


def password_manager():
    password = "python123"

    def change(new_password):
        nonlocal password
        password = new_password
        return password

    def display():
        return password

    return change, display


change_password, view_password = password_manager()

print(change_password("forhad123"))
print(view_password())


"""
Temperature Tracker
Create an outer function with:

temperature = 25

Return:

increase()
decrease()
current()
All functions should share the same temperature.
"""


def temp():
    temperature = 25

    def increase(num):
        nonlocal temperature
        temperature += num
        return temperature

    def decrease(num):
        nonlocal temperature
        temperature -= num
        return temperature

    def current():
        return temperature

    return increase, decrease, current


increased, decreased, current = temp()

increased(3)
decreased(2)
current()


"""
x = 10

def outer():
    x = 20

    def inner():
        # modify x from outer
"""

x = 10
print(x)


def outer():
    global x
    x = 20

    def inner():
        # modify x from outer
        pass


outer()
print(x)


"""
13. Fix the Error
Why does this fail?

count = 0

def increase():
    count += 1

Fix it.


"""
count = 0


def increased():
    global count
    count += 1
    return count


increased()
increased()
increased()


"""
14. Closure Challenge
Create a function that returns another function which multiplies an internal number by 2 every time it is called.

Example:

10
20
40
80
"""


def external():
    internal_number = 5

    def internal():
        nonlocal internal_number
        internal_number *= 2
        return internal_number

    return internal


internal = external()


internal()
internal()
internal()


"""
Challenge Problem ⭐
Implement a simple login system.

Global:

logged_in_users = 0

Create:

def login_system():
    username = None

Inside, return:

login(name) → stores the username using nonlocal and increments logged_in_users using global
logout() → clears the username and decrements logged_in_users
current_user() → returns the current username
"""
logged_in_users = 0


def login_system():
    username = None

    def login(name):
        nonlocal username
        global logged_in_users
        username = name
        logged_in_users += 1
        return username, logged_in_users

    def logout():
        nonlocal username
        global logged_in_users
        username = None
        logged_in_users -= 1
        return username, logged_in_users

    def current_user():
        nonlocal username
        return print(f"current user is {username}")

    return login, logout, current_user


login, logout, current_user = login_system()

print(logged_in_users)
print(login("Forhad"))
print(logged_in_users)
print(logout())

current_user()
