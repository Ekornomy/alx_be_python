def main():
    print("Daily Task Reminder")
    print("===================")
    
    # Prompt for a single task
    task = input("Enter your task: ")
    
    # Prompt for priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter 'high', 'medium', or 'low'")
    
    # Prompt for time sensitivity with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")
    
    print("\n" + "="*50)
    print("REMINDER:")
    print("="*50)
    
    # Process the task based on priority using Match Case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"🚨 '{task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"⚠️ '{task}' is a HIGH priority task. Please complete it as soon as possible.")
        
        case "medium":
            if time_bound == "yes":
                print(f"📅 '{task}' is a MEDIUM priority task that should be completed today.")
            else:
                print(f"📋 '{task}' is a MEDIUM priority task. Consider completing it this week.")
        
        case "low":
            if time_bound == "yes":
                print(f"⏰ '{task}' is a LOW priority task with a time constraint. Try to complete it when possible.")
            else:
                print(f"💭 Note: '{task}' is a LOW priority task. Consider completing it when you have free time.")
    
    print("="*50)

# Run the program
if __name__ == "__main__":
    main()