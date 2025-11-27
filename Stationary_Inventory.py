inventory = [
    
    {'name': 'Gel pens', 'quantity': 200, 'threshold': 50},
    {'name': 'Postal Colours Box', 'quantity':50 , 'threshold': 10},
    {'name': 'Canvas', 'quantity': 35 , 'threshold': 5}
]




def find_item_index(name):
     for i in range(len(inventory)):
        if inventory[i]['name'].lower() == name.lower():
            return i
   

def add_new_item():
    print("\n--- Add New Item ---")
    name = input("Enter Item Name: ").strip()
    if not name:
        return
    if find_item_index(name) is not None:
        print(f"Item '{name}' already exists. Use the update option.")
        return

    
    quantity = int(input("Enter Starting Quantity (number): "))
    if quantity is None or quantity < 0:
        print(" Quantity must be zero or positive.")
        return

    
    threshold = int(input("Enter Reorder Threshold (number): "))
    if threshold is None or threshold < 0:
        print(" Threshold must be zero or positive.")
        return

    
    new_item = {
        'name': name,
        'quantity': quantity,
        'threshold': threshold
    }
    
    inventory.append(new_item)
    print(f"\n Added '{name}'. Qty: {quantity}.")

def update_stock(operation):
    action = "Add Units" if operation == 'add' else "Deduct Units"
    print(f"\n--- {action} ---")
    
    name = input("Enter Item Name: ").strip()
    index = find_item_index(name)

    if index is None:
        print(f" Item '{name}' not found.")
        return

    
    amount = int(input(f"Enter Amount to {operation}: "))
    if amount is None or amount <= 0:
        print(" Amount must be a positive whole number.")
        return

    item = inventory[index]
    current_qty = item['quantity']
    
    
    if operation == 'add':
        item['quantity'] = current_qty + amount
        print(f"\n {amount} units added. New quantity: {item['quantity']}")
        
    elif operation == 'deduct':
        new_qty = current_qty - amount
        
        
        if new_qty < 0:
            print(f" Cannot deduct {amount}. Only {current_qty} units remain.")
            return
            
        item['quantity'] = new_qty
        print(f"\n {amount} units deducted. New quantity: {item['quantity']}")

def view_all_inventory():
    if not inventory:
        print("\n Inventory is empty.")
        return

    print("\n" + "=" * 60)
    print("{:<20} | {:<10} | {:<10} | {:<10}".format(
        "Item Name", "Quantity", "Threshold", "Status"))
    print("=" * 60)
    
   
    for item in inventory:
        status = "OK"
        
        if item['quantity'] <= item['threshold']:
            status = "LOW STOCK"
        elif item['quantity'] == 0:
            status = "OUT OF STOCK"
            
        print("{:<20} | {:<10} | {:<10} | {:<10}".format(
            item['name'][:20],
            item['quantity'],
            item['threshold'],
            status))
            
    print("=" * 60)

def generate_report():
    low_stock_list = []
    
    
    for item in inventory:
        if item['quantity'] <= item['threshold']:
            
            needed = item['threshold'] - item['quantity'] + 1 
            
            
            low_stock_list.append({
                'name': item['name'],
                'quantity': item['quantity'],
                'threshold': item['threshold'],
                'needed': needed
            })
            
    print("\n" + "=" * 80)
    print("\n LOW STOCK ALERT REPORT")
    print("=" * 80)
    
    if not low_stock_list:
        print("All items are currently above their reorder thresholds.")
        print("=" * 80)
        return
        
    print("{:<20} | {:<10} | {:<10} | {:<10}".format(
        "Item Name", "Qty", "Threshold", "Needed"))
    print("-" * 80)
    
    for item in low_stock_list:
        print("{:<20} | {:<10} | {:<10} | {:<10}".format(
            item['name'][:20],
            item['quantity'],
            item['threshold'],
            item['needed']))
            
    print("=" * 80)

def search_item_prompt():
    print("\n--- Search Item ---")
    name = input("Enter Item Name to Search: ").strip()
    if not name: return
    
    index = find_item_index(name)
    
    if index is not None:
        item = inventory[index]
        status = "OK"
        
        if item['quantity'] <= item['threshold']: status = "LOW STOCK"
        elif item['quantity'] == 0: status = "OUT OF STOCK"

        print(f"\n Item: {item['name']}")
        print(f"  > Current Quantity: {item['quantity']}")
        print(f"  > Reorder Threshold: {item['threshold']}")
        print(f"  > Status: {status}")
    else:
        print(f" Item '{name}' is not in inventory.")



def print_menu():
    print("\n" + "=" * 50)
    print("\n Stationary Shop Inventory and Stock Tracker ")
    print("=" * 50)
    print("1. Add New Item")
    print("2. Update Stock (Add Units)")
    print("3. Deduct Stock (Remove Units)")
    print("4. View All Inventory")
    print("5. Search Item by Name")
    print("6. Generate Low Stock Report")
    print("7. Exit (Data is not saved!)")
    print("=" * 50)


def main_loop():
     while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        
        if choice == '1':
            add_new_item()
        elif choice == '2':
            update_stock('add')
        elif choice == '3':
            update_stock('deduct')
        elif choice == '4':
            view_all_inventory()
        elif choice == '5':
            search_item_prompt()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            print("\n Exiting system. WARNING: Changes were NOT saved.")
            return
        else:
            print(" Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main_loop()