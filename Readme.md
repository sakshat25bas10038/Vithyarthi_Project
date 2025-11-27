# Stationary Shop Inventory and Stock Tracker

## Overview of the Project
This project is a simple, beginner-friendly Command-Line Interface (CLI) application designed to track the inventory of a small stationery shop. It is built to demonstrate mastery of foundational Python concepts, including defining functions (def), managing data in lists of dictionaries, and using loops (for/while) and complex conditional logic (if/elif/else) for stock management and alerts.   
**NOTE**: This version of the tracker is designed for maximum simplicity and does not save data to a file (persistence is disabled). The inventory resets every time the program is launched.


## Features
- **Add New Item**: Introduce new items (e.g., 'Markers') with a starting quantity and reorder threshold.
- **Update Stock**: Increase the quantity (e.g., after receiving a new shipment).
- **Deduct Stock**: Decrease the quantity (e.g., after a sale).
- **View All Inventory**: See a full list of items and their calculated status (OK, LOW STOCK, OUT OF STOCK).
- **Generate Low Stock Report**: Produces a filtered report of all items below their threshold, including the quantity needed.
- **Search Item**: Quickly find the status of a specific item by name

## Technologies/Tools Used
- Python 3.x
- Core Python Concepts Only: Lists, Dictionaries, Looping (for iteration and menu), and Conditional Logic (if/elif/else).

## Steps to Install & Run the Project
1. Save the Python code as a single file (e.g., stationary_inventory.py).
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the program using the command:
   - python : stationary_inventory.py

## Instructions for Testing
1. **Initial Status Check (Point 4)**: Verify 'Gel pens' are OK and 'Postal Colours Box' is LOW STOCK.
2. **Deduction (Point 3)**: Deduct 50 units from 'Gel pens'. The new quantity (150) should still show Status: OK.
3. **Threshold Test (Point 3)**: Deduct 150 units from 'Gel pens'. The system must print an error and block the transaction to prevent a negative quantity.
4. **Report Check (Point 6)**: Ensure the report accurately lists 'Postal Colours Box' and calculates the quantity needed.
