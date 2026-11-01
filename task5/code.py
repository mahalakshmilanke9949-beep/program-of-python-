# Multi-Plan Telecommunications Cost Optimization

plans = []
eligible_plans = []

# Get number of mobile plans
n = int(input("Enter number of mobile plans: "))

# Get user requirements
print("\nEnter User Requirements")

required_data = float(input("Required Data (GB): "))
required_calls = float(input("Required Calling Minutes: "))
required_validity = int(input("Required Validity (Days): "))
budget = float(input("Maximum Budget (Rs.): "))

# Validate user requirements
if (required_data < 0 or required_calls < 0 or
    required_validity <= 0 or budget < 0):

    print("Invalid user requirements!")

else:

    # Enter mobile plan details
    for i in range(n):

        print("\nEnter Details of Plan", i + 1)

        name = input("Plan Name: ")

        cost = float(input("Plan Cost (Rs.): "))

        data = float(input("Data Limit (GB): "))

        calls = float(input("Calling Minutes: "))

        validity = int(input("Validity (Days): "))

        extra_data_rate = float(
            input("Extra Data Charge per GB: Rs. ")
        )

        extra_call_rate = float(
            input("Extra Calling Charge per Minute: Rs. ")
        )

        # Validate plan details
        if (cost < 0 or data < 0 or calls < 0 or
            validity <= 0 or extra_data_rate < 0 or
            extra_call_rate < 0):

            print("Invalid Plan Details! Plan skipped.")
            continue

        # Calculate excess usage
        excess_data = max(0, required_data - data)

        excess_calls = max(0, required_calls - calls)

        # Calculate additional charges
        data_charge = excess_data * extra_data_rate

        call_charge = excess_calls * extra_call_rate

        # Calculate total cost
        total_cost = cost + data_charge + call_charge

        # Store plan information
        plan = {
            "name": name,
            "cost": cost,
            "data": data,
            "calls": calls,
            "validity": validity,
            "excess_data": excess_data,
            "excess_calls": excess_calls,
            "data_charge": data_charge,
            "call_charge": call_charge,
            "total_cost": total_cost
        }

        plans.append(plan)

        # Check eligibility
        if (data >= required_data and
            calls >= required_calls and
            validity >= required_validity and
            total_cost <= budget):

            eligible_plans.append(plan)

    # Display all plan details
    print("\n==============================================")
    print("       TELECOMMUNICATION PLAN ANALYSIS")
    print("==============================================")

    for plan in plans:

        print("\nPlan Name:", plan["name"])

        print("Base Cost: Rs.", round(plan["cost"], 2))

        print("Data Limit:", plan["data"], "GB")

        print("Calling Minutes:", plan["calls"])

        print("Validity:", plan["validity"], "Days")

        print("Excess Data:", plan["excess_data"], "GB")

        print("Excess Calling Minutes:",
              plan["excess_calls"])

        print("Extra Data Charges: Rs.",
              round(plan["data_charge"], 2))

        print("Extra Calling Charges: Rs.",
              round(plan["call_charge"], 2))

        print("Total Cost: Rs.",
              round(plan["total_cost"], 2))

        if plan in eligible_plans:
            print("Status: Eligible")
        else:
            print("Status: Not Eligible")

        print("----------------------------------------------")

    # Find the most economical eligible plan
    if eligible_plans:

        best_plan = min(
            eligible_plans,
            key=lambda p: p["total_cost"]
        )

        print("\n==============================================")
        print("       MOST ECONOMICAL MOBILE PLAN")
        print("==============================================")

        print("Recommended Plan:", best_plan["name"])

        print("Plan Cost: Rs.",
              round(best_plan["cost"], 2))

        print("Total Cost: Rs.",
              round(best_plan["total_cost"], 2))

        print("Data Available:", best_plan["data"], "GB")

        print("Calling Minutes:", best_plan["calls"])

        print("Validity:", best_plan["validity"], "Days")

        print("\nTotal Eligible Plans:",
              len(eligible_plans))

        print("==============================================")

    else:

        print("\nNo suitable plan found!")
        print("Please increase your budget or modify your requirements.")
Here you have to write the code
