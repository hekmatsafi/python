class InvalidOperationError(Exception):
    """Custom exception raised for unsupported operators."""
    pass


def calculator():
    while True:
        print("\n--- New Calculation ---")
        try:
            # 1. Ask for two numeric values & handle invalid input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # 2. Ask for the operation
            operation = input("Enter an operation (+, -, *, /): ").strip()

            # 3. Check for supported operators or raise custom exception
            if operation not in ['+', '-', '*', '/']:
                raise InvalidOperationError(f"'{operation}' is not a valid operator.")

            # 4. Perform calculation and handle division by zero
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide a number by zero.")
                result = num1 / num2

            print(f"Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("Error: Invalid numeric input! Please enter valid numbers.")
        except InvalidOperationError as ioe:
            print(f"Error: {ioe}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")

        finally:
            # 5. Finally block to report completion of each attempt
            print("Calculation attempt completed.")

        # 6. Loop retry prompt
        choice = input("\nDo you want to try another calculation? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
