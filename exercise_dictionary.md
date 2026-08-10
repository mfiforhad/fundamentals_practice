**Title:** ChatGPT

**Source:** [https://chatgpt.com/](https://chatgpt.com/)

---

# Page Structure Map
```text
ChatGPT
├── How to approach these
├── Level 1 — Dictionary Thinking
│   └── 1\. E-commerce Order Analyzer
├── Level 2 — Inventory Management
│   └── 2\. Warehouse Inventory
├── Level 3 — Student Performance System
│   └── 3\. Student Grade Analysis
├── Level 4 — Social Media Analytics
│   └── 4\. User Interests
├── Level 5 — Restaurant Analytics
│   └── 5\. Restaurant Orders
├── Level 6 — Multidimensional Sales Data
│   └── 6\. Company Sales Dashboard
├── Level 7 — Employee Project Tracking
│   └── 7\. Project Allocation System
├── Level 8 — Banking Transactions
│   └── 8\. Transaction Analysis
├── Level 9 — Flight Booking System
│   └── 9\. Airline Seat Management
├── Level 10 — Inventory + Orders + Customers
│   └── 10\. E-commerce Backend Simulation
├── Level 11 — Multidimensional Attendance System
│   └── 11\. School Attendance
├── Level 12 — Real-World Capstone
├── 12\. Food Delivery Analytics
│   ├── Customer analytics
│   ├── Restaurant analytics
│   ├── Recommendation system
│   └── Cross-analysis
├── Bonus Challenge — Data Restructuring
│   ├── View 1 — Customer-centric
│   ├── View 2 — Product-centric
│   └── View 3 — Flat records
├── Recommended Order
│   └── Your main dictionary skills to deliberately practice
├── dictionary → dictionary → dictionary
├── dictionary → list → tuple
├── dictionary → set
├── list → dictionary → set
├── Building a dictionary dynamically
└── Dictionary aggregation
```

---

Absolutely. Since you're **weak in dictionaries**, I'll make dictionaries the backbone of the exercises and force you to combine them with **lists, tuples, and sets**, including **nested/multidimensional data**.

I’ll deliberately skip things like “create a dictionary,” “find max in a list,” simple set union, etc. These are meant to build **practical problem-solving ability**, not syntax familiarity.

## How to approach these

For every exercise:

1.  First decide **what data structure should represent the data**.

2.  Identify which parts should be:

    -   `dict`

    -   `list`

    -   `tuple`

    -   `set`

3.  Write the solution without classes/OOP.

4.  Don't use `try/except`.

5.  Don't use external libraries unless an exercise explicitly says so.

6.  Try to solve each problem in **small transformations** rather than one giant expression.

---

## Level 1 — Dictionary Thinking

### 1\. E-commerce Order Analyzer

You receive orders like:

Python

```
orders = [
    {
        "order_id": 101,
        "customer": "Rahim",
        "items": [
            ("Laptop", 1, 800),
            ("Mouse", 2, 20)
        ]
    },
    {
        "order_id": 102,
        "customer": "Karim",
        "items": [
            ("Keyboard", 1, 50),
            ("Mouse", 1, 20)
        ]
    },
    {
        "order_id": 103,
        "customer": "Rahim",
        "items": [
            ("Monitor", 2, 200),
            ("Mouse", 1, 20)
        ]
    }
]
```

Build a program that produces:

Python

```
{
    "Rahim": {
        "orders": 2,
        "items_bought": {
            "Laptop": 1,
            "Mouse": 3,
            "Monitor": 2
        },
        "total_spent": 1240
    },
    "Karim": {
        "orders": 1,
        "items_bought": {
            "Keyboard": 1,
            "Mouse": 1
        },
        "total_spent": 70
    }
}
```

Then determine:

-   Which customer spent the most?

-   Which product sold the most units?

-   Which products were bought by **both customers**?

-   Which products were bought by only one customer?

**Focus:** nested dictionaries + lists + tuples + sets.

---

## Level 2 — Inventory Management

### 2\. Warehouse Inventory

You have multiple warehouses:

Python

```
inventory = {
    "Dhaka": {
        "electronics": {
            "laptop": 15,
            "phone": 30,
            "tablet": 10
        },
        "furniture": {
            "chair": 50,
            "desk": 20
        }
    },

    "Chittagong": {
        "electronics": {
            "laptop": 8,
            "phone": 20,
            "tablet": 5
        },
        "furniture": {
            "chair": 30,
            "desk": 10
        }
    }
}
```

Write code to:

-   Calculate total quantity of every product across all warehouses.

-   Find the warehouse with the highest total inventory.

-   Find products that exist in **every warehouse**.

-   Find products that exist in only one warehouse.

-   Find the category with the highest total quantity.

-   Create:

Python

```
{
    "laptop": {
        "Dhaka": 15,
        "Chittagong": 8
    },
    ...
}
```

**Important:** Don't manually access `"Dhaka"` and `"Chittagong"`. Your code should work if another warehouse is added.

---

## Level 3 — Student Performance System

### 3\. Student Grade Analysis

Given:

Python

```
students = {
    "S001": {
        "name": "Amin",
        "subjects": {
            "Python": [80, 85, 90],
            "SQL": [75, 80, 85],
            "Git": [90, 95, 88]
        }
    },

    "S002": {
        "name": "Nadia",
        "subjects": {
            "Python": [95, 90, 92],
            "SQL": [88, 85, 90],
            "Git": [80, 85, 82]
        }
    }
}
```

Determine:

-   Average score per student.

-   Average score per subject.

-   Best student in each subject.

-   Best overall student.

-   Subjects where **every student scored above 80**.

-   Subjects where at least one student scored below 80.

-   Highest individual score.

-   All students who achieved that score.

Then create:

Python

```
{
    "S001": {
        "name": "Amin",
        "overall_average": ...,
        "best_subject": ...,
        "subjects_above_85": {...}
    }
}
```

**Focus:** dictionary traversal several levels deep.

---

## Level 4 — Social Media Analytics

### 4\. User Interests

Python

```
users = {
    "rahim": {
        "age": 24,
        "interests": {"python", "football", "music", "travel"},
        "friends": {"karim", "nabil"}
    },

    "karim": {
        "age": 26,
        "interests": {"python", "gaming", "music"},
        "friends": {"rahim", "nabil"}
    },

    "nabil": {
        "age": 23,
        "interests": {"football", "music", "travel"},
        "friends": {"rahim", "karim"}
    }
}
```

Build a recommendation system.

For a selected user:

-   Find common interests with every other user.

-   Find users sharing at least 2 interests.

-   Find users who are not already friends.

-   Recommend users based on the highest number of shared interests.

-   Find interests shared by everyone.

-   Find unique interests belonging to only one user.

For example:

Python

```
recommend("rahim")
```

might produce:

Python

```
[
    ("nabil", 2),
    ("karim", 2)
]
```

**Focus:** dictionary + nested sets.

---

## Level 5 — Restaurant Analytics

### 5\. Restaurant Orders

Python

```
orders = [
    ("Rahim", [
        ("Burger", 2),
        ("Fries", 1),
        ("Coke", 2)
    ]),

    ("Karim", [
        ("Pizza", 1),
        ("Coke", 1)
    ]),

    ("Rahim", [
        ("Pizza", 2),
        ("Fries", 2)
    ])
]

prices = {
    "Burger": 8,
    "Fries": 3,
    "Coke": 2,
    "Pizza": 12
}
```

Calculate:

-   Total revenue.

-   Revenue per customer.

-   Quantity sold per item.

-   Most popular item.

-   Customer who spent the most.

-   Customers who ordered both Pizza and Coke.

-   Items ordered by more than one customer.

-   Create a customer summary dictionary.

Then produce:

Python

```
{
    "Rahim": {
        "orders": 2,
        "items": {"Burger", "Fries", "Coke", "Pizza"},
        "quantity": ...,
        "spent": ...
    }
}
```

Notice that `items` should be a **set**.

---

## Level 6 — Multidimensional Sales Data

### 6\. Company Sales Dashboard

This is intentionally more complex:

Python

```
sales = {
    "2025": {
        "Q1": {
            "Dhaka": {
                "Laptop": 20,
                "Phone": 50
            },
            "Chittagong": {
                "Laptop": 10,
                "Phone": 30
            }
        },

        "Q2": {
            "Dhaka": {
                "Laptop": 25,
                "Phone": 60
            },
            "Chittagong": {
                "Laptop": 15,
                "Phone": 35
            }
        }
    },

    "2026": {
        "Q1": {
            "Dhaka": {
                "Laptop": 30,
                "Phone": 70
            },
            "Chittagong": {
                "Laptop": 20,
                "Phone": 40
            }
        }
    }
}
```

Answer:

1.  Total sales of each product.

2.  Total sales per year.

3.  Total sales per quarter.

4.  Total sales per city.

5.  Best-performing city.

6.  Best-performing product.

7.  Best quarter.

8.  Product sales comparison between 2025 and 2026.

9.  Find cities selling every product.

10.  Create a flattened structure:

Python

```
[
    ("2025", "Q1", "Dhaka", "Laptop", 20),
    ("2025", "Q1", "Dhaka", "Phone", 50),
    ...
]
```

Then reconstruct the nested dictionary from the flattened data.

This one is **very important** for building dictionary skills.

---

## Level 7 — Employee Project Tracking

### 7\. Project Allocation System

Python

```
employees = {
    "E01": {
        "name": "Rahim",
        "skills": {"python", "sql", "docker"},
        "projects": {"P01", "P03"}
    },

    "E02": {
        "name": "Karim",
        "skills": {"python", "javascript", "react"},
        "projects": {"P02"}
    },

    "E03": {
        "name": "Nadia",
        "skills": {"python", "sql", "aws"},
        "projects": {"P01", "P02"}
    }
}

projects = {
    "P01": {
        "name": "Banking System",
        "required_skills": {"python", "sql"}
    },

    "P02": {
        "name": "E-commerce",
        "required_skills": {"python", "react"}
    },

    "P03": {
        "name": "Cloud Migration",
        "required_skills": {"aws", "docker"}
    }
}
```

Find:

-   Employees who have all skills required for each project.

-   Employees missing exactly one required skill.

-   Projects each employee can work on.

-   Skills shared by all employees.

-   Skills nobody else has.

-   Employees who work on projects together.

-   Employees who share at least two skills.

Then create:

Python

```
{
    "E01": {
        "name": "Rahim",
        "eligible_projects": ["P01", "P03"],
        "missing_skills": {...}
    }
}
```

---

## Level 8 — Banking Transactions

### 8\. Transaction Analysis

Python

```
transactions = [
    ("T001", "A101", "deposit", 500),
    ("T002", "A101", "withdraw", 100),
    ("T003", "A102", "deposit", 1000),
    ("T004", "A101", "deposit", 300),
    ("T005", "A102", "withdraw", 200),
    ("T006", "A103", "deposit", 700),
]
```

Account information:

Python

```
accounts = {
    "A101": {
        "name": "Rahim",
        "type": "savings"
    },
    "A102": {
        "name": "Karim",
        "type": "business"
    },
    "A103": {
        "name": "Nadia",
        "type": "savings"
    }
}
```

Build a report containing:

-   Total deposits per account.

-   Total withdrawals per account.

-   Current balance per account.

-   Largest transaction.

-   Most active account.

-   Accounts with only deposits.

-   Accounts with both deposits and withdrawals.

-   Total money deposited into the bank.

-   Total money withdrawn.

-   Transaction IDs belonging to each account.

Then generate:

Python

```
{
    "A101": {
        "name": "Rahim",
        "deposits": 800,
        "withdrawals": 100,
        "balance_change": 700,
        "transaction_ids": {"T001", "T002", "T004"}
    }
}
```

---

## Level 9 — Flight Booking System

### 9\. Airline Seat Management

Represent flights like this:

Python

```
flights = {
    "BG101": {
        "route": ("DAC", "DXB"),
        "seats": {
            "1A": "Rahim",
            "1B": None,
            "1C": "Karim",
            "2A": None,
            "2B": "Nadia",
            "2C": None
        }
    },

    "BG102": {
        "route": ("DAC", "SIN"),
        "seats": {
            "1A": "Nabil",
            "1B": None,
            "1C": None,
            "2A": None,
            "2B": "Rahim",
            "2C": None
        }
    }
}
```

Implement operations to:

-   Find all passengers.

-   Find available seats.

-   Count occupied seats.

-   Calculate occupancy percentage.

-   Find passengers traveling on multiple flights.

-   Find all destinations a passenger is traveling to.

-   Find passengers traveling to the same destination.

-   Find flights with more than 50% occupancy.

-   Produce passenger → flight mapping.

Use the tuple:

Python

```
("DAC", "DXB")
```

as the route representation.

---

## Level 10 — Inventory + Orders + Customers

### 10\. E-commerce Backend Simulation

Combine these:

Python

```
products = {
    "P01": {
        "name": "Laptop",
        "category": "electronics",
        "price": 800,
        "tags": {"computer", "work"}
    },
    "P02": {
        "name": "Mouse",
        "category": "electronics",
        "price": 20,
        "tags": {"computer", "accessory"}
    },
    "P03": {
        "name": "Desk",
        "category": "furniture",
        "price": 150,
        "tags": {"office", "work"}
    }
}
```

Python

```
customers = {
    "C01": {
        "name": "Rahim",
        "interests": {"computer", "work"}
    },
    "C02": {
        "name": "Karim",
        "interests": {"office", "gaming"}
    }
}
```

Python

```
orders = [
    {
        "customer": "C01",
        "items": [
            ("P01", 1),
            ("P02", 2)
        ]
    },
    {
        "customer": "C02",
        "items": [
            ("P03", 1)
        ]
    }
]
```

Build a complete analysis system.

Determine:

-   Customer spending.

-   Products purchased.

-   Categories purchased.

-   Customer interests.

-   Products whose tags match customer interests.

-   Recommended products for each customer.

-   Most purchased category.

-   Most profitable product.

-   Customers who bought products from multiple categories.

-   Customers who bought products matching **none** of their interests.

This exercise combines **all four structures** heavily.

---

## Level 11 — Multidimensional Attendance System

### 11\. School Attendance

Python

```
attendance = {
    "2026-01-01": {
        "S001": "present",
        "S002": "absent",
        "S003": "present"
    },

    "2026-01-02": {
        "S001": "late",
        "S002": "present",
        "S003": "present"
    },

    "2026-01-03": {
        "S001": "present",
        "S002": "absent",
        "S003": "late"
    }
}
```

Python

```
students = {
    "S001": ("Rahim", "CSE"),
    "S002": ("Karim", "CSE"),
    "S003": ("Nadia", "EEE")
}
```

Calculate:

-   Attendance percentage per student.

-   Number of absences.

-   Number of late arrivals.

-   Best attendance.

-   Worst attendance.

-   Students who were absent on the same dates.

-   Dates when everyone was present.

-   Department-level attendance.

-   Convert the data into:

Python

```
{
    "S001": {
        "name": "Rahim",
        "department": "CSE",
        "present": 2,
        "absent": 0,
        "late": 1
    }
}
```

---

## Level 12 — Real-World Capstone

## 12\. Food Delivery Analytics

This is your biggest exercise.

You have:

Python

```
restaurants = {
    "R01": {
        "name": "Food House",
        "cuisine": "Bangla",
        "menu": {
            "M01": {
                "name": "Biryani",
                "price": 180,
                "tags": {"rice", "spicy"}
            },
            "M02": {
                "name": "Kebab",
                "price": 250,
                "tags": {"meat", "spicy"}
            }
        }
    },

    "R02": {
        "name": "Pizza Hub",
        "cuisine": "Italian",
        "menu": {
            "M03": {
                "name": "Pizza",
                "price": 500,
                "tags": {"cheese", "bread"}
            },
            "M04": {
                "name": "Pasta",
                "price": 350,
                "tags": {"cheese", "pasta"}
            }
        }
    }
}
```

Customers:

Python

```
customers = {
    "C01": {
        "name": "Rahim",
        "favorite_tags": {"spicy", "meat"},
        "favorite_cuisines": {"Bangla"}
    },

    "C02": {
        "name": "Nadia",
        "favorite_tags": {"cheese"},
        "favorite_cuisines": {"Italian"}
    }
}
```

Orders:

Python

```
orders = [
    {
        "order_id": "O01",
        "customer": "C01",
        "restaurant": "R01",
        "items": [
            ("M01", 2),
            ("M02", 1)
        ]
    },

    {
        "order_id": "O02",
        "customer": "C02",
        "restaurant": "R02",
        "items": [
            ("M03", 1),
            ("M04", 2)
        ]
    }
]
```

Build an analytics system that determines:

### Customer analytics

-   Total amount spent by every customer.

-   Number of orders.

-   Restaurants visited.

-   Cuisines ordered.

-   Items ordered.

-   Favorite tags represented in their purchases.

-   Customers who ordered from multiple restaurants.

### Restaurant analytics

-   Total revenue.

-   Number of orders.

-   Number of unique customers.

-   Most popular menu item.

-   Total quantity sold per menu item.

-   Most profitable menu item.

### Recommendation system

For each customer:

-   Find restaurants matching their favorite cuisines.

-   Find menu items matching their favorite tags.

-   Rank menu items by number of matching tags.

-   Exclude items they have already ordered.

-   Produce something like:

Python

```
{
    "C01": [
        ("M02", 2),
        ("M01", 1)
    ],
    "C02": [
        ("M03", 2),
        ("M04", 1)
    ]
}
```

### Cross-analysis

Find:

-   Most popular cuisine.

-   Most popular food tag.

-   Customers who share favorite tags.

-   Menu items ordered by more than one customer.

-   Restaurants with customers from multiple preference groups.

-   Items that nobody has ordered.

-   Tags that exist in menus but have never appeared in an order.

-   The customer who has the widest variety of food.

-   The restaurant with the widest menu.

-   The restaurant that earns the most **per unique customer**.

---

## Bonus Challenge — Data Restructuring

For any one of the exercises above, give yourself this additional requirement:

> **You are not allowed to modify the original data.**

Take the original nested data and generate **three different views** of it.

For example:

### View 1 — Customer-centric

Python

```
{
    "Rahim": {
        "products": {...},
        "orders": [...],
        "total": ...
    }
}
```

### View 2 — Product-centric

Python

```
{
    "Laptop": {
        "customers": {"Rahim", "Nadia"},
        "quantity": 5,
        "revenue": 4000
    }
}
```

### View 3 — Flat records

Python

```
[
    ("Rahim", "Laptop", 2, 1600),
    ("Rahim", "Mouse", 3, 60),
    ...
]
```

This is **excellent dictionary practice** because you're learning to think:

> **"What shape should my data have?"**

rather than merely:

> "How do I loop through a dictionary?"

---

## Recommended Order

Don't jump directly to the capstone. I'd do them in this order:

```
1. E-commerce Order Analyzer
        ↓
2. Warehouse Inventory
        ↓
3. Student Performance
        ↓
4. Social Media Analytics
        ↓
5. Restaurant Analytics
        ↓
6. Multidimensional Sales
        ↓
7. Employee Projects
        ↓
8. Banking Transactions
        ↓
9. Flight Booking
        ↓
10. E-commerce Backend
        ↓
11. Attendance
        ↓
12. Food Delivery Capstone
```

### Your main dictionary skills to deliberately practice

While solving, pay special attention to these patterns:

Python

```
# dictionary → dictionary → dictionary
data[key1][key2][key3]
```

Python

```
# dictionary → list → tuple
data[key]["items"][0][1]
```

Python

```
# dictionary → set
data[key]["skills"]
```

Python

```
# list → dictionary → set
for item in items:
    for value in item["tags"]:
        ...
```

Python

```
# Building a dictionary dynamically
result = {}

for item in data:
    key = ...
    if key not in result:
        result[key] = ...
```

Python

```
# Dictionary aggregation
result[key] = result.get(key, 0) + value
```

And especially:

Python

```
dictionary
    ↓
dictionary
    ↓
list
    ↓
tuple
    ↓
set
    ↓
new dictionary
```

That ability to **navigate, transform, aggregate, and restructure nested data** is what will make you genuinely comfortable with dictionaries—not memorizing dictionary methods.