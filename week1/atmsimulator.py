account = {
    "pin": "1234",
    "balance": 5000.0
}

MAX_LOGIN_ATTEMPTS = 3


def login():
    """Verify user PIN. Returns True if login succeeds, False otherwise."""
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == account["pin"]:
            print("Login successful!\n")
            return True
        else:
            attempts += 1
            remaining = MAX_LOGIN_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.\n")
            else:
                print("Too many incorrect attempts. Card blocked.")
    return False


def check_balance():
    """Display current balance."""
    print(f"Your current balance is: ₹{account['balance']:.2f}")


def deposit():
    """Deposit money into the account."""
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        account["balance"] += amount
        print(f"₹{amount:.2f} deposited successfully.")
        check_balance()
    except ValueError:
        print("Invalid amount entered.")


def withdraw():
    """Withdraw money from the account."""
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > account["balance"]:
            print("Insufficient balance.")
            return
        account["balance"] -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        check_balance()
    except ValueError:
        print("Invalid amount entered.")


def show_menu():
    """Display the ATM menu."""
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    print("=== Welcome to the Simple ATM Simulator ===")

    if not login():
        print("Exiting program.")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()