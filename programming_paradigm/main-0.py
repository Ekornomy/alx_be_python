import sys
from bank_account import BankAccount

def main():
    # Create account instance with initial balance of 100
    account = BankAccount(100)
    
    # Check if command line arguments exist
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        print("Examples:")
        print("  python main.py deposit:50")
        print("  python main.py withdraw:30")
        print("  python main.py display")
        return
    
    # Parse command line argument
    try:
        # Split the first argument by colon
        parts = sys.argv[1].split(':')
        command = parts[0].lower()
        
        # Extract amount if provided
        amount = float(parts[1]) if len(parts) > 1 else 0
        
        # Handle different commands
        if command == "deposit":
            account.deposit(amount)
            print(f"Deposited ${amount:.2f}")
            account.display_balance()
            
        elif command == "withdraw":
            if account.withdraw(amount):
                print(f"Withdrew ${amount:.2f}")
                account.display_balance()
            else:
                print(f"Insufficient funds to withdraw ${amount:.2f}")
                
        elif command == "display":
            account.display_balance()
            
        else:
            print(f"Invalid command: {command}")
            print("Valid commands: deposit, withdraw, display")
            
    except ValueError:
        print("Error: Amount must be a valid number")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

