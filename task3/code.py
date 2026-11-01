# Hospital Billing and Patient Classification System

patients = []

# Function to calculate patient bill
def calculate_bill(age, consultation, diagnostic, treatment):

    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply conditional concession
    if age >= 60:
        discount = total * 0.10

    elif total > 15000:
        discount = total * 0.05

    else:
        discount = 0

    # Calculate final amount
    final_amount = total - discount

    return total, discount, final_amount


# Function to classify patients
def classify_patient(total):

    if total < 5000:
        return "Normal Patient"

    elif total <= 15000:
        return "Medium Expense Patient"

    else:
        return "High Expense Patient"


# Get number of patients
n = int(input("Enter number of patients: "))

# Process patient details
for i in range(n):

    print("\nEnter Details of Patient", i + 1)

    name = input("Enter patient name: ")

    age = int(input("Enter patient age: "))

    consultation = float(
        input("Enter consultation charges: Rs. ")
    )

    diagnostic = float(
        input("Enter diagnostic charges: Rs. ")
    )

    treatment = float(
        input("Enter treatment charges: Rs. ")
    )

    # Validate inputs
    if (age < 0 or consultation < 0 or
        diagnostic < 0 or treatment < 0):

        print("Invalid Input! Charges and age cannot be negative.")
        continue

    # Calculate bill
    total, discount, final_amount = calculate_bill(
        age,
        consultation,
        diagnostic,
        treatment
    )

    # Classify patient
    category = classify_patient(total)

    # Store patient details
    patients.append({
        "name": name,
        "age": age,
        "consultation": consultation,
        "diagnostic": diagnostic,
        "treatment": treatment,
        "total": total,
        "discount": discount,
        "final": final_amount,
        "category": category
    })


# Display billing report
print("\n==========================================")
print("       HOSPITAL BILLING REPORT")
print("==========================================")

if len(patients) == 0:
    print("No valid patient records available.")

else:

    for i, p in enumerate(patients, start=1):

        print("\nPatient Number:", i)
        print("Patient Name:", p["name"])
        print("Age:", p["age"])

        print("Consultation Charges: Rs.",
              round(p["consultation"], 2))

        print("Diagnostic Charges: Rs.",
              round(p["diagnostic"], 2))

        print("Treatment Charges: Rs.",
              round(p["treatment"], 2))

        print("------------------------------------------")

        print("Total Bill: Rs.",
              round(p["total"], 2))

        print("Concession: Rs.",
              round(p["discount"], 2))

        print("Final Payable Amount: Rs.",
              round(p["final"], 2))

        print("Patient Classification:",
              p["category"])

        print("------------------------------------------")

    # Calculate total hospital collection
    total_collection = sum(
        p["final"] for p in patients
    )

    print("\nTotal Number of Patients:", len(patients))

    print("Total Hospital Collection: Rs.",
          round(total_collection, 2))

print("\n==========================================")
print("          THANK YOU")
print("==========================================")
Here you have to write the code 
