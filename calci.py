def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def calculator():
    print("Welcome to the Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate (Power)")
        print("6. Modulus")
        print("7. Floor Division")
        print("8. Exit")

        # Take input from the user
        operation = input("Enter operation (1/2/3/4/5/6/7/8): ")

        if operation == '8':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop

        # Check if the operation is valid
        if operation in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue  # Continue to the next iteration of the loop

            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif operation == '5':
                print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
            elif operation == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif operation == '7':
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        else:
            print("Invalid operation! Please select a valid operation.")

if __name__ == "__main__":  # Corrected line
    calculator()
