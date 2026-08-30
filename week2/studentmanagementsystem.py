import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["roll_no", "name", "marks"]


def initialize_file():
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all_students():
    """Read and return all student records from the CSV file as a list of dicts."""
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_all_students(students):
    """Overwrite the CSV file with the given list of student records."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    """Add a new student record and save it to the CSV file."""
    roll_no = input("Enter roll number: ").strip()

    students = read_all_students()
    if any(s["roll_no"] == roll_no for s in students):
        print(f"A student with roll number {roll_no} already exists.")
        return

    name = input("Enter name: ").strip()

    try:
        marks = float(input("Enter marks: ").strip())
    except ValueError:
        print("Invalid marks entered. Aborting.")
        return

    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    write_all_students(students)
    print(f"Student '{name}' (Roll No: {roll_no}) added successfully.")


def delete_student():
    """Delete a student record by roll number."""
    roll_no = input("Enter roll number to delete: ").strip()

    students = read_all_students()
    filtered = [s for s in students if s["roll_no"] != roll_no]

    if len(filtered) == len(students):
        print(f"No student found with roll number {roll_no}.")
        return

    write_all_students(filtered)
    print(f"Student with roll number {roll_no} deleted successfully.")


def search_student():
    """Search for a student by roll number or name."""
    query = input("Enter roll number or name to search: ").strip().lower()

    students = read_all_students()
    results = [
        s for s in students
        if s["roll_no"].lower() == query or s["name"].lower() == query
    ]

    if not results:
        print("No matching student found.")
        return

    print("\n--- Search Results ---")
    for s in results:
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Marks: {s['marks']}")


def list_students():
    """Display all student records."""
    students = read_all_students()
    if not students:
        print("No student records found.")
        return

    print("\n--- All Students ---")
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
    print("-" * 40)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['marks']:<10}")


def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. List All Students")
    print("5. Exit")


def main():
    print("=== Student Management System ===")
    initialize_file()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            list_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()