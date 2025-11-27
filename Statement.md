# Problem Statement
Small retail shops, such as stationery and art supply stores, face a continuous challenge in managing high-volume, low-margin inventory (e.g., pens, paper, and colors). The core problem is the lack of an automated system to accurately monitor stock levels and provide timely alerts when items drop below a safe reorder threshold. Reliance on manual counting leads to lost sales due to stockouts and unnecessary capital tied up in excess inventory. This project provides a localized, text-based solution to automate stock tracking and alerting.

# Scope of the Project
The scope is a single-user application that runs in the command line (CLI). It strictly uses core Python concepts (Lists, Dictionaries, and conditional logic) to manage the inventory data entirely in memory.
The project demonstrates the core functionalities of stock manipulation and automated reporting but does not include data persistence (i.e., data is not saved to a file), focusing instead on demonstrating the core logic of the system.

# Target Users
- Small stationery or art supply shop managers.
- Lab managers or educators tracking consumable supplies.
- Individuals managing specialized inventory collections.

# High-Level Features (Functional Modules)
The project includes the following three major functional modules:
1. **Inventory Management**: Allows users to add new items and update/deduct stock quantities using name lookups.
2. **Stock Alert & Analysis**: Automatically calculates the status of each item (OK, LOW STOCK, OUT OF STOCK) by comparing the current quantity against the predefined reorder threshold.
3. **Reporting**: Provides a detailed, filtered report of all items flagged as LOW STOCK, including the quantity needed to replenish.

# Functional Requirements
- Must store item data as a dictionary with keys: name, quantity, and threshold.
- Must prevent stock deduction if the resulting quantity would be negative.
- Must be able to search for an item based on its name (case-insensitive).

# Non-Functional Requirements 
- **Usability**: The CLI must present all data and menus using clear, aligned text formatting.
- **Reliability**: The code must enforce non-negative quantities during deductions.
- **Core Logic Demonstration**: The project must heavily utilize for loops, if/elif/else statements, and dictionary lookups, as requested.
- **Simplicity**: The entire program must be contained within a single file with no external imports (like csv or os), focusing on core Python concept
