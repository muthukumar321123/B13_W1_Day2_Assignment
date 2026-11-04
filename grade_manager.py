# List to store all student records
students = []


# Function 1: Convert mark to grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Function 2: Add student with try/except validation
def add_student():
    name = input("Enter name: ").strip()

    while True:
        try:
            mark = float(input(f"Enter mark for {name}: "))
            if 0 <= mark <= 100:
                break
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    grade = get_grade(mark)
    students.append({"name": name, "mark": mark, "grade": grade})


# Function 3: Show table and stats
def show_results():
    if not students:
        print("No students added yet!\n")
        return

    # Print Table
    print(f"{'Name':<12} {'Mark':<7} {'Grade':<5}")
    for s in students:
        # Display mark as an integer if it's a whole number
        m = int(s["mark"]) if s["mark"].is_integer() else s["mark"]
        print(f"{s['name']:<12} {m:<7} {s['grade']:<5}")

    # Calculate Stats
    marks = [s["mark"] for s in students]
    avg = sum(marks) / len(marks)
    highest = int(max(marks)) if max(marks).is_integer() else max(marks)
    lowest = int(min(marks)) if min(marks).is_integer() else min(marks)

    # Print Summary Line
    print(f"Average: {avg:.1f}    Highest: {highest}    Lowest: {lowest}\n")


# Function 4: Menu Loop
def main():
    while True:
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")
        choice = input("Option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()