# Retail Billing with Multiple Discount Rules

products = []

# Category-specific tax rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "groceries": 3,
    "furniture": 12
}

# Discount rules
MAX_DISCOUNT = 2000

# Get number of products
n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products!")

else:

    # Enter product details
    for i in range(n):

        print("\nEnter Product Details", i + 1)

        name = input("Enter product name: ")

        category = input(
            "Enter category (Electronics/Clothing/Groceries/Furniture): "
        ).lower().strip()

        price = float(input("Enter product price: Rs. "))

        quantity = int(input("Enter quantity: "))

        # Validate product details
        if (category not in tax_rates or
            price < 0 or quantity <= 0):

            print("Invalid product details! Product skipped.")
            continue

        # Calculate subtotal
        subtotal = price * quantity

        # Calculate category-specific tax
        tax = subtotal * tax_rates[category] / 100

        # Store product information
        products.append({

            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal,
            "tax_rate": tax_rates[category],
            "tax": tax

        })

    # Calculate total purchase amount
    if products:

        total_subtotal = sum(
            p["subtotal"] for p in products
        )

        total_tax = sum(
            p["tax"] for p in products
        )

        # Apply threshold discount
        if total_subtotal > 10000:
            discount_rate = 10

        elif total_subtotal > 5000:
            discount_rate = 5

        else:
            discount_rate = 0

        # Calculate discount
        discount = total_subtotal * discount_rate / 100

        # Apply maximum discount limit
        discount = min(discount, MAX_DISCOUNT)

        # Calculate final bill
        final_bill = total_subtotal + total_tax - discount

        # Display itemized invoice
        print("\n==============================================")
        print("              RETAIL INVOICE")
        print("==============================================")

        print(
            f"{'Product':<15}"
            f"{'Category':<15}"
            f"{'Price':<10}"
            f"{'Qty':<6}"
            f"{'Subtotal':<12}"
        )

        print("----------------------------------------------")

        for p in products:

            print(
                f"{p['name']:<15}"
                f"{p['category']:<15}"
                f"{p['price']:<10.2f}"
                f"{p['quantity']:<6}"
                f"{p['subtotal']:<12.2f}"
            )

        print("----------------------------------------------")

        # Display tax details
        print("\nPRODUCT TAX DETAILS")

        for p in products:

            print(
                p["name"],
                "- Tax Rate:",
                str(p["tax_rate"]) + "%",
                "- Tax Amount: Rs.",
                round(p["tax"], 2)
            )

        print("\n==============================================")

        print("Total Product Amount: Rs.",
              round(total_subtotal, 2))

        print("Total Tax Amount: Rs.",
              round(total_tax, 2))

        print("Discount Percentage:", discount_rate, "%")

        print("Discount Amount: Rs.",
              round(discount, 2))

        print("----------------------------------------------")

        print("FINAL PAYABLE AMOUNT: Rs.",
              round(final_bill, 2))

        print("==============================================")

    else:

        print("No valid products available for billing.")
Here you have to write the code
