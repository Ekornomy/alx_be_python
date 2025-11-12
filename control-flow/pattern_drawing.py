# pattern_drawing.py
# Draw a square pattern using while loop and nested for loop

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    print(f"\nSquare pattern of size {size}:")
    
    # Initialize row counter for while loop
    row = 0
    
    # Use while loop to iterate through each row
    while row < size:
        # Use for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        
        # Move to the next line after completing each row
        print()
        
        # Increment row counter
        row += 1

# Run the program
if __name__ == "__main__":
    main()