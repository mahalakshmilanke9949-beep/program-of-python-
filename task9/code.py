# Manufacturing Cost and Profitability Analysis

products = []

# Function to calculate manufacturing cost
def calculate_cost(quantity, material, labour,
                   wastage, machine, selling_price):

    # Material cost
    material_cost = quantity * material

    # Labour cost
    labour_cost = quantity * labour

    # Wastage cost
    wastage_cost = material_cost * wastage / 100

    # Machine cost
    machine_cost = quantity * machine

    # Total production cost
    total_cost = (
        material_cost +
        labour_cost +
        wastage_cost +
        machine_cost
    )

    # Total sales revenue
    revenue = quantity * selling_price

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    return (
        material_cost,
        labour_cost,
        wastage_cost,
        machine_cost,
        total_cost,
        revenue,
        profit,
        profit_percentage
    )


# Get number of products
n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products!")

else:

    # Process product details
    for i in range(n):

        print("\nEnter Product Details", i + 1)

        name = input("Enter product name: ")

        quantity = int(input("Enter quantity produced: "))

        material = float(
            input("Enter material cost per unit: Rs. ")
        )

        labour = float(
            input("Enter labour cost per unit: Rs. ")
        )

        wastage = float(
            input("Enter wastage percentage: ")
        )

        machine = float(
            input("Enter machine cost per unit: Rs. ")
        )

        selling_price = float(
            input("Enter selling price per unit: Rs. ")
        )

        target = float(
            input("Enter profit target percentage: ")
        )

        # Validate inputs
        if (quantity <= 0 or material < 0 or
            labour < 0 or wastage < 0 or
            wastage > 100 or machine < 0 or
            selling_price < 0 or target < 0):

            print("Invalid Input! Product skipped.")
            continue

        # Calculate manufacturing details
        result = calculate_cost(
            quantity,
            material,
            labour,
            wastage,
            machine,
            selling_price
        )

        (
            material_cost,
            labour_cost,
            wastage_cost,
            machine_cost,
            total_cost,
            revenue,
            profit,
            profit_percentage
        ) = result

        # Check profit target
        if profit < 0:
            status = "Loss"
        elif profit_percentage >= target:
            status = "Profit Target Achieved"
        else:
            status = "Profit Target Not Achieved"

        # Store product details
        products.append({

            "name": name,
            "quantity": quantity,
            "material": material_cost,
            "labour": labour_cost,
            "wastage": wastage_cost,
            "machine": machine_cost,
            "total": total_cost,
            "revenue": revenue,
            "profit": profit,
            "percentage": profit_percentage,
            "target": target,
            "status": status

        })


    # Display manufacturing report
    print("\n==============================================")
    print("    MANUFACTURING COST AND PROFIT REPORT")
    print("==============================================")

    for i, p in enumerate(products, start=1):

        print("\nProduct Number:", i)

        print("Product Name:", p["name"])

        print("Quantity Produced:", p["quantity"])

        print("----------------------------------------------")

        print("Material Cost: Rs.",
              round(p["material"], 2))

        print("Labour Cost: Rs.",
              round(p["labour"], 2))

        print("Wastage Cost: Rs.",
              round(p["wastage"], 2))

        print("Machine Cost: Rs.",
              round(p["machine"], 2))

        print("----------------------------------------------")

        print("Total Production Cost: Rs.",
              round(p["total"], 2))

        print("Total Sales Revenue: Rs.",
              round(p["revenue"], 2))

        print("Profit / Loss: Rs.",
              round(p["profit"], 2))

        print("Profit Percentage:",
              round(p["percentage"], 2), "%")

        print("Required Profit Target:",
              p["target"], "%")

        print("Production Status:", p["status"])

        print("----------------------------------------------")


    # Overall summary
    if products:

        total_cost = sum(p["total"] for p in products)

        total_revenue = sum(p["revenue"] for p in products)

        total_profit = total_revenue - total_cost

        if total_cost > 0:
            overall_percentage = (
                total_profit / total_cost
            ) * 100
        else:
            overall_percentage = 0

        print("\n==============================================")
        print("       OVERALL PRODUCTION SUMMARY")
        print("==============================================")

        print("Total Products:", len(products))

        print("Total Production Cost: Rs.",
              round(total_cost, 2))

        print("Total Sales Revenue: Rs.",
              round(total_revenue, 2))

        print("Overall Profit / Loss: Rs.",
              round(total_profit, 2))

        print("Overall Profit Percentage:",
              round(overall_percentage, 2), "%")

        print("==============================================")

    else:

        print("No valid product records available.")
Here you have to write the code
