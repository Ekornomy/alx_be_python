def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty. Please enter a valid item.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the shopping list.")
                else:
                    print(f"'{item}' was not found in the shopping list.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()