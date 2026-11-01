# Progressive Electricity Billing System

# Electricity slab rates
FIXED_CHARGE = 50
SURCHARGE_RATE = 5
REBATE = 20
INCREASE_LIMIT = 30

bills = []
units_list = []

# Function to calculate electricity charges
def calculate_bill(units):

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    # Add fixed charges
    amount = charge + FIXED_CHARGE

    # Calculate surcharge
    surcharge = amount * SURCHARGE_RATE / 100

    amount = amount + surcharge

    # Apply rebate
    if units <= 100:
        amount = amount - REBATE

    return amount


# Input number of months
n = int(input("Enter number of months: "))

# Monthly bill calculation
for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a non-negative value.")
        continue

    bill = calculate_bill(units)

    units_list.append(units)
    bills.append(bill)

    print("Electricity Bill: Rs.", round(bill, 2))


# Monthly bill comparison
print("\n====================================")
print(" PROGRESSIVE ELECTRICITY BILLING")
print("====================================")

total_bill = sum(bills)

for i in range(len(bills)):

    print("\nMonth", i + 1)
    print("Units Consumed:", units_list[i])
    print("Total Bill: Rs.", round(bills[i], 2))

    if i > 0:

        previous_bill = bills[i - 1]
        current_bill = bills[i]

        if previous_bill > 0:

            increase = (
                (current_bill - previous_bill)
                / previous_bill
            ) * 100

            if increase > INCREASE_LIMIT:
                print("Alert: Unusual increase detected!")
                print("Increase:", round(increase, 2), "%")

            elif increase > 0:
                print("Bill increased by:",
                      round(increase, 2), "%")

            elif increase < 0:
                print("Bill decreased by:",
                      round(abs(increase), 2), "%")

            else:
                print("No change in bill.")

        else:
            print("Previous bill is zero; percentage comparison unavailable.")

print("\n====================================")
print("Total Electricity Expenditure: Rs.",
      round(total_bill, 2))

print("Average Monthly Bill: Rs.",
      round(total_bill / len(bills), 2))

print("====================================")
Here you have to write the code
