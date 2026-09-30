class InvalidGradeError(Exception):
    """Custom exception raised for grades outside the 0-100 range."""
    pass


# --- Validation Logic ---
def validate_grade(value):
    try:
        numeric_grade = float(value)
    except (ValueError, TypeError):
        raise ValueError("Invalid numeric input! Please enter a valid number.")

    if numeric_grade < 0 or numeric_grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")

    return numeric_grade


# --- User-Interface Logic ---
def main():
    print("--- Interactive Grade Validator ---")
    while True:
        user_input = input("\nEnter a grade to validate: ").strip()

        try:
            validated_grade = validate_grade(user_input)
            print(f"✅ Success: Validated grade is {validated_grade}")
        except (ValueError, InvalidGradeError) as e:
            print(f"❌ Error: {e}")

        choice = input("Do you want to validate another grade? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
