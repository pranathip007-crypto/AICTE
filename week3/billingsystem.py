TAX_RATE = 0.05  # 5% tax


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        """Return price * quantity for this product."""
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=TAX_RATE):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        """Add a product to the bill."""
        self.products.append(product)

    def calculate_subtotal(self):
        """Sum of all product subtotals before tax."""
        return sum(p.subtotal() for p in self.products)

    def calculate_tax(self):
        """Tax amount based on subtotal."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self):
        """Final total including tax."""
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        """Print the final bill in a tabular format."""
        if not self.products:
            print("No items in the bill.")
            return

        print("\n" + "=" * 55)
        print(f"{'BILL':^55}")
        print("=" * 55)
        print(f"{'Item':<20}{'Price':>10}{'Qty':>8}{'Subtotal':>17}")
        print("-" * 55)

        for p in self.products:
            print(f"{p.name:<20}{p.price:>10.2f}{p.quantity:>8}{p.subtotal():>17.2f}")

        print("-" * 55)
        print(f"{'Subtotal':<38}{self.calculate_subtotal():>17.2f}")
        print(f"{'Tax (' + str(int(self.tax_rate * 100)) + '%)':<38}{self.calculate_tax():>17.2f}")
        print(f"{'TOTAL':<38}{self.calculate_total():>17.2f}")
        print("=" * 55)


def show_menu():
    print("\n===== BILLING SYSTEM =====")
    print("1. Add Product")
    print("2. Display Bill")
    print("3. Finish & Show Final Bill")


def main():
    print("=== Billing System (OOP-based) ===")
    bill = Bill()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter price per unit: ").strip())
                quantity = int(input("Enter quantity: ").strip())
                if price < 0 or quantity < 0:
                    print("Price and quantity must be non-negative.")
                    continue
            except ValueError:
                print("Invalid price or quantity.")
                continue

            product = Product(name, price, quantity)
            bill.add_product(product)
            print(f"'{name}' added to the bill.")

        elif choice == "2":
            bill.display_bill()

        elif choice == "3":
            print("\nFinal Bill:")
            bill.display_bill()
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


if __name__ == "__main__":
    main()