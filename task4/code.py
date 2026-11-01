# Employee Payroll and Deduction Analysis System

employees = []

# Function to calculate progressive deduction
def calculate_deduction(gross_salary):

    if gross_salary <= 20000:
        deduction = gross_salary * 0.05

    elif gross_salary <= 40000:
        deduction = gross_salary * 0.10

    else:
        deduction = gross_salary * 0.15

    return deduction


# Get number of employees
n = int(input("Enter number of employees: "))

# Process employee details
for i in range(n):

    print("\nEnter Details of Employee", i + 1)

    emp_id = input("Enter Employee ID: ")

    name = input("Enter Employee Name: ")

    basic = float(input("Enter Basic Pay: Rs. "))

    hra = float(input("Enter HRA: Rs. "))

    da = float(input("Enter DA: Rs. "))

    overtime_hours = float(
        input("Enter Overtime Hours: ")
    )

    overtime_rate = float(
        input("Enter Overtime Rate per Hour: Rs. ")
    )

    incentive = float(
        input("Enter Incentives: Rs. ")
    )

    # Validate inputs
    if (basic < 0 or hra < 0 or da < 0 or
        overtime_hours < 0 or overtime_rate < 0 or
        incentive < 0):

        print("Invalid Input! Values cannot be negative.")
        continue

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = (
        basic + hra + da + overtime_pay + incentive
    )

    # Calculate progressive deduction
    deduction = calculate_deduction(gross_salary)

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Store employee details
    employees.append({
        "id": emp_id,
        "name": name,
        "basic": basic,
        "hra": hra,
        "da": da,
        "overtime": overtime_pay,
        "incentive": incentive,
        "gross": gross_salary,
        "deduction": deduction,
        "net": net_salary
    })


# Display salary statements
print("\n==============================================")
print("          EMPLOYEE SALARY STATEMENT")
print("==============================================")

for emp in employees:

    print("\nEmployee ID:", emp["id"])
    print("Employee Name:", emp["name"])

    print("----------------------------------------------")

    print("Basic Pay          : Rs.", round(emp["basic"], 2))
    print("HRA                : Rs.", round(emp["hra"], 2))
    print("DA                 : Rs.", round(emp["da"], 2))
    print("Overtime Pay       : Rs.", round(emp["overtime"], 2))
    print("Incentives         : Rs.", round(emp["incentive"], 2))

    print("----------------------------------------------")

    print("Gross Salary       : Rs.", round(emp["gross"], 2))
    print("Total Deduction    : Rs.", round(emp["deduction"], 2))
    print("Net Salary         : Rs.", round(emp["net"], 2))

    print("==============================================")


# Calculate payroll summary
if len(employees) > 0:

    total_gross = sum(emp["gross"] for emp in employees)

    total_deduction = sum(
        emp["deduction"] for emp in employees
    )

    total_net = sum(emp["net"] for emp in employees)

    print("\n             PAYROLL SUMMARY")
    print("==============================================")

    print("Total Employees       :", len(employees))

    print("Total Gross Salary    : Rs.", round(total_gross, 2))

    print("Total Deductions      : Rs.", round(total_deduction, 2))

    print("Total Net Salary      : Rs.", round(total_net, 2))

    print("==============================================")

else:
    print("No valid employee records available.")
Here you have to write the code
