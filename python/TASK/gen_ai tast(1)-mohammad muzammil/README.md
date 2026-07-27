#  Python Product Catalog Management

A beginner-friendly Python project that demonstrates the use of Python's built-in data structures such as **Lists, Tuples, Sets, and Dictionaries**. The project performs basic product management operations like adding, updating, deleting, searching, and organizing product data into a catalog.

---

##  Features

### Task 1: List & Tuple Operations
- Store product names in a list.
- Access products using indexing.
- Add new products using `append()`.
- Convert a tuple into a list for modification.
- Update tuple values by converting back to a tuple.

### Task 2: Set Operations
- Create a list of product categories.
- Convert the list into a set to remove duplicate values.
- Add a new category.
- Check if a category exists.
- Count the total number of unique categories.

### Task 3: Dictionary Operations
- Store product prices using a dictionary.
- Add a new product.
- Update an existing product price.
- Delete a product.
- Handle deletion of a non-existing product safely.
- Calculate:
  - Total number of products
  - Average product price

### Task 4: Product Catalog
- Combine product name, price, and category into a catalog.
- Group products by category.
- Display all products belonging to the **Electronics** category.

---

## Technologies Used

- Python 3
- Lists
- Tuples
- Sets
- Dictionaries
- Loops
- Conditional Statements

---

##  Project Structure

```
main.py
README.md
```

---

##  How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open the project folder.
4. Run the program:

```bash
uv run main.py
```

---

##  Concepts Covered

- List Operations
- Tuple Conversion
- Set Operations
- Dictionary CRUD Operations
- Membership Checking
- Data Aggregation
- Loops
- Conditional Statements
- Data Organization

---

##  Sample Output

```text
laptop
keyboard

['phon', 'laptop', 'computer', 'chair', 'table', 'keyboard', 'tablet', 'charger']

('phon', 'smart', 25000)

True

3

Product not found

Average Price: 23000.0

Catalog:
[
 ('Laptop', 50000, 'Electronics'),
 ('Mouse', 500, 'Accessories'),
 ('Keyboard', 1200, 'Accessories'),
 ('Monitor', 10000, 'Electronics'),
 ('Phone', 25000, 'Electronics'),
 ('Tablet', 18000, 'Electronics')
]

{
 'Electronics': ['Laptop', 'Monitor', 'Phone', 'Tablet'],
 'Accessories': ['Mouse', 'Keyboard']
}

Products in Electronics:
Laptop
Monitor
Phone
Tablet
```

---

## Learning Objectives

This project helps beginners understand:

- How different Python data structures work.
- When to use Lists, Tuples, Sets, and Dictionaries.
- Basic CRUD (Create, Read, Update, Delete) operations.
- Organizing related data efficiently.
- Writing simple and clean Python programs.

---

##  Author

**Mohammad Muzammil**

Learning Python Data Structures and building beginner-friendly projects.