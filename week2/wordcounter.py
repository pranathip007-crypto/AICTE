import os


def count_stats(filepath):
    """Read a text file and return word, line, and character counts."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_chars = sum(len(line) for line in lines)
    num_words = sum(len(line.split()) for line in lines)

    return num_lines, num_words, num_chars


def create_sample_file(filepath):
    """Create a sample text file if the user doesn't have one."""
    sample_text = (
        "Python is a versatile programming language.\n"
        "It is widely used for web development, data science, and automation.\n"
        "Learning Python opens up many opportunities in technology.\n"
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(sample_text)
    print(f"Sample file created at '{filepath}'.")


def main():
    print("=== Word Counter from Text File ===")
    filepath = input("Enter path to text file: ").strip()

    if not os.path.exists(filepath):
        print("File not found.")
        choice = input("Create a sample file at this path instead? (y/n): ").strip().lower()
        if choice == "y":
            create_sample_file(filepath)
        else:
            print("Exiting program.")
            return

    lines, words, chars = count_stats(filepath)

    print("\n--- File Statistics ---")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")


if __name__ == "__main__":
    main()