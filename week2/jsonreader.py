import json
import os


SAMPLE_DATA = {
    "students": [
        {"name": "Aarav", "roll_no": 1, "marks": 85},
        {"name": "Diya", "roll_no": 2, "marks": 92},
        {"name": "Kabir", "roll_no": 3, "marks": 76}
    ]
}


def create_sample_json(filepath):
    """Create a sample JSON file if none exists."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(SAMPLE_DATA, f, indent=4)
    print(f"Sample JSON file created at '{filepath}'.")


def load_json(filepath):
    """Load JSON data from a file. Returns None on failure."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON.")
        return None


def print_formatted(data, indent=0):
    """Recursively print JSON data in a readable, indented format."""
    spacing = "  " * indent

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{spacing}{key}:")
                print_formatted(value, indent + 1)
            else:
                print(f"{spacing}{key}: {value}")

    elif isinstance(data, list):
        for i, item in enumerate(data, start=1):
            print(f"{spacing}Item {i}:")
            print_formatted(item, indent + 1)

    else:
        print(f"{spacing}{data}")


def main():
    print("=== JSON File Reader ===")
    filepath = input("Enter path to JSON file: ").strip()

    if not os.path.exists(filepath):
        print("File not found.")
        choice = input("Create a sample JSON file at this path instead? (y/n): ").strip().lower()
        if choice == "y":
            create_sample_json(filepath)
        else:
            print("Exiting program.")
            return

    data = load_json(filepath)
    if data is None:
        return

    print("\n--- Formatted JSON Output ---")
    print_formatted(data)

    print("\n--- Raw Pretty-Printed JSON ---")
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()