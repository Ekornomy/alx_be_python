# multiplication_table.py
# Generate multiplication table using for loop

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    print(f"\nMultiplication table for {number}:")
    print("-" * 25)
    
    # Generate and print the multiplication table using for loop
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the program
if __name__ == "__main__":
    main()