# Student Grade Calculator
def calculate_grade(marks):
    """Return a grade based on the marks."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def get_feedback(grade):
    """Give the student a friendly message."""
    messages = {
        "A": "Excellent work! Keep shining!",
        "B": "Very good! Keep it up!",
        "C": "Good effort! Keep practicing!",
        "D": "You can improve. Keep working hard!",
        "F": "Don't give up. Learn from this and try again!",
    }
    return messages[grade]

def ask_for_marks():
    """Ask again until the marks are between 0 and 100."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Please enter marks from 0 to 100.")
        except ValueError:
            print("Please enter a valid number, such as 85.")


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter the student's name: ").strip()
    while not name:
        print("The name cannot be blank. Please try again.")
        name = input("Enter the student's name: ").strip()

    marks = ask_for_marks()
    grade = calculate_grade(marks)
    message = get_feedback(grade)

    if marks.is_integer():
        marks = int(marks)

    print("\n--- Student Result ---")
    print(f"Name: {name.title()}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("----------------------")


if __name__ == "__main__":
    main()
