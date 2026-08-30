class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        """Divide a by b, raising an error for division by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        """Return a modulo b, raising an error for modulo by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulus by zero.")
        return a % b


def get_number(prompt):
    """Safely get a float input from the user, re-prompting on invalid entry."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_menu():
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")


def main():
    print("=== Calculator with Exception Handling ===")
    calc = Calculator()

    operations = {
        "1": ("Add", calc.add),
        "2": ("Subtract", calc.subtract),
        "3": ("Multiply", calc.multiply),
        "4": ("Divide", calc.divide),
        "5": ("Power", calc.power),
        "6": ("Modulus", calc.modulus),
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid option. Please choose between 1 and 7.")
            continue

        name, operation = operations[choice]
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            result = operation(a, b)
            print(f"Result of {name}: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()