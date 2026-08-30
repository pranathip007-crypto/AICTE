def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


def is_prime(number):
    """Return True if number is prime, False otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print("=== Even/Odd & Prime Number Checker ===")

    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Even/Odd check
    if is_even(num):
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

    # Prime check
    if is_prime(num):
        print(f"{num} is Prime.")
    else:
        print(f"{num} is Not Prime.")


if __name__ == "__main__":
    main()