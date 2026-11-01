# University Scholarship Allocation System

students = []

# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

# Input number of students
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate marks (%): "))

    subjects = int(input("Enter number of subjects: "))

    subject_marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j + 1}: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))

    income = float(input("Enter annual family income: "))

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subject_marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

        print("Status: Eligible")

    else:
        print("Status: Not Eligible")


# Sort eligible students
# Priority:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income

students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display scholarship results
print("\n========================================")
print(" UNIVERSITY SCHOLARSHIP ALLOCATION")
print("========================================")

if len(students) == 0:
    print("No students are eligible for scholarship.")

else:
    print("\nRank  Name       Aggregate  Attendance  Income")

    for rank, student in enumerate(students, start=1):

        print(
            f"{rank:<6}"
            f"{student['name']:<11}"
            f"{student['aggregate']:<11.2f}"
            f"{student['attendance']:<12.2f}"
            f"{student['income']:.2f}"
        )

    print("\nTotal Eligible Students:", len(students))
Here you have to write the code
