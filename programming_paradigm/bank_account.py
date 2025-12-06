class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Double underscore for name mangling
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
    
    # Optional: Add a getter method for read-only access
    def get_balance(self):
        return self.__account_balance


# Test the improved version
if __name__ == "__main__":
    account = BankAccount(100)
    
    # This will now raise an error or fail
    try:
        print(account.__account_balance)  # ❌ AttributeError
    except AttributeError:
        print("Good: Direct access prevented")
    
    # Proper usage
    account.deposit(50)
    account.display_balance()  # Shows $150
    
    # Withdraw validation
    result = account.withdraw(200)
    print(f"Withdraw $200: {'Success' if result else 'Failed'}")  # Failed
    
    result = account.withdraw(50)
    print(f"Withdraw $50: {'Success' if result else 'Failed'}")   # Success
    account.display_balance()  # Shows $100