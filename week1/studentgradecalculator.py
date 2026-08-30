def get_marks(num_subjects):
    """Take marks input from the user for each subject."""
    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks


def calculate_average(marks):
    """Calculate the average of a list of marks."""
    return sum(marks) / len(marks)


def assign_grade(average):
    """Assign a grade based on the average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=== Student Grade Calculator ===")

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            print("Number of subjects must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    marks = get_marks(num_subjects)
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Result ---")
    print(f"Marks entered: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()