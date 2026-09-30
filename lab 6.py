import os


class DocumentReadError(Exception):
    """Custom exception raised when a document fails to read properly."""
    pass


def read_document():
    
    filename = input("Enter the filename to read: ").strip()

    try:

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()


    except FileNotFoundError:
        raise DocumentReadError(f"The file '{filename}' could not be found.")
    except PermissionError:
        raise DocumentReadError(f"Permission denied. You cannot read '{filename}'.")
    except UnicodeDecodeError:
        raise DocumentReadError(f"Encoding error. '{filename}' is not a valid UTF-8 text file.")


    else:
        print("\n--- File Content Success ---")
        print(content)
        print("----------------------------")


if __name__ == "__main__":
    try:
        read_document()
    except DocumentReadError as e:
        print(f"❌ Error: {e}")
