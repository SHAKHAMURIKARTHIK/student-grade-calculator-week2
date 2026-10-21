# Student Grade Calculator

## About the project

This is a small Python program that lets a student enter their name and marks. It checks the marks, works out the grade, and displays a friendly message.

I made this project to practise Python functions, `if-elif-else`, loops, and input validation.

## Grade rules

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 0–59.99 | F |

Decimal marks are allowed. For example, 89.5 receives a B.

## What you need

- Python 3
- No extra Python packages

## How to run the program

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run `python grade_calculator.py`.
4. If your computer uses `python3`, run `python3 grade_calculator.py`.
5. Enter the student's name and marks when prompted.

## Example

```text
=== Student Grade Calculator ===
Enter the student's name: Priya
Enter marks (0-100): 85

--- Student Result ---
Name: Priya
Marks: 85/100
Grade: B
Message: Very good! Keep it up!
----------------------
```

## How it works

- `calculate_grade()` chooses a grade using simple conditions.
- `get_feedback()` selects a message for the grade.
- `ask_for_marks()` repeats the question if the input is invalid.
- `main()` collects the information and displays the result.

I kept the code in small functions to make it easier to understand and update.

## Project files

- `grade_calculator.py` — the Python program
- `test_cases.txt` — examples for checking the program
- `screenshots/` — a place to save screenshots of your own test runs

## Before submitting

Run the program, try the test cases, and save screenshots in the `screenshots` folder. Then upload the project to GitHub and submit it according to your course instructions.
