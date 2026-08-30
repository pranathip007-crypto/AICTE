class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance:.2f}")


def show_menu():
    print("\n===== BANK ACCOUNT MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")


def main():
    print("=== Bank Account System ===")
    name = input("Enter account holder name: ").strip()

    try:
        initial_balance = float(input("Enter initial balance: ").strip())
        if initial_balance < 0:
            initial_balance = 0.0
    except ValueError:
        initial_balance = 0.0

    account = BankAccount(name, initial_balance)

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount entered.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount entered.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()