
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    print("=== DateTime Exploration ===")
    
    print("\n--- Part 1: Current Date and Time ---")
    current_date = display_current_datetime()
    
    print("\n--- Part 2: Future Date Calculation ---")
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)
        
        if days < 0:
            print("Please enter a non-negative number of days.")
        else:
            future_date = calculate_future_date(days)
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
