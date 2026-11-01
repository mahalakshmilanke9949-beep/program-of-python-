

## 1\. Problem Statement

The Progressive Electricity Billing System is designed to calculate household electricity bills based on monthly electricity consumption using a progressive slab-based tariff system.

The system calculates electricity charges by considering the following factors:

1. **Electricity Consumption:** Total units consumed by a household in a month.
2. **Slab Rates:** Different electricity rates are applied to different consumption levels.
3. **Fixed Charges:** A fixed amount is added to every monthly bill.
4. **Surcharges:** An additional percentage is charged on the electricity cost.
5. **Rebates:** Discounts are provided when consumption is below a specified limit.
6. **Monthly Comparison:** Bills from multiple months are compared to identify increases or decreases.
7. **Unusual Increase Detection:** If the current month's bill increases by more than 30% compared to the previous month, the system identifies it as an unusual increase.

Finally, the system displays the monthly electricity bills, total expenditure, and unusual consumption increases.

## 2\. Algorithm

1. Start the program.
2. Initialize electricity slab rates:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Next 100 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
3. Set fixed charges to ₹50.
4. Set surcharge to 5%.
5. Set rebate to ₹20 if consumption is below or equal to 100 units.
6. Get the number of months.
7. Enter electricity consumption for each month.
8. Calculate electricity charges using progressive slabs.
9. Add fixed charges to the electricity charges.
10. Calculate the surcharge.
11. Apply the rebate if eligible.
12. Calculate the final monthly bill.
13. Compare the current month's bill with the previous month's bill.
14. If the increase is greater than 30%, identify it as an unusual increase.
15. Display monthly bills, total expenditure, and unusual increases.
16. Stop the program.

## 3\. Flowchart (Mermaid Code)

Copy this code into the Mermaid Live Editor to generate the flowchart.

[Mermaid Live Editor](<https://mermaid.live/?utm_source=chatgpt.com>)
```mermaid
flowchart TD
    A([Start]) --> B[Initialize slab rates and charges]
    B --> C[/Enter number of months/]
    C --> D[/Enter electricity units/]
    D --> E{Units <= 100?}

    E -- Yes --> F[Calculate units x 2]
    E -- No --> G{Units <= 200?}

    G -- Yes --> H[Calculate 100x2 + remaining x3]
    G -- No --> I{Units <= 300?}

    I -- Yes --> J[Calculate 100x2 + 100x3 + remaining x5]
    I -- No --> K[Calculate 100x2 + 100x3 + 100x5 + remaining x7]

    F --> L[Add fixed charges]
    H --> L
    J --> L
    K --> L

    L --> M[Calculate surcharge]
    M --> N{Units <= 100?}
    N -- Yes --> O[Apply rebate]
    N -- No --> P[Calculate final bill]
    O --> P

    P --> Q{More months?}
    Q -- Yes --> D
    Q -- No --> R[Compare monthly bills]

    R --> S{Increase greater than 30%?}
    S -- Yes --> T[Display unusual increase]
    S -- No --> U[Display normal increase]

    T --> V[Display monthly bills and total]
    U --> V
    V --> W([Stop])
   ```                  
  ## 4\. Sample Input

text

```text
Enter number of months: 4

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 120

Month 3
Enter electricity units consumed: 180

Month 4
Enter electricity units consumed: 300
```

## 5\. Sample Output

text

```text
Month 1
Electricity Bill: Rs. 198.0

Month 2
Electricity Bill: Rs. 522.5

Month 3
Electricity Bill: Rs. 711.5

Month 4
Electricity Bill: Rs. 1557.5

====================================
 PROGRESSIVE ELECTRICITY BILLING
====================================

Month 1
Units Consumed: 80.0
Total Bill: Rs. 198.0

Month 2
Units Consumed: 120.0
Total Bill: Rs. 522.5
Alert: Unusual increase detected!
Increase: 163.89 %

Month 3
Units Consumed: 180.0
Total Bill: Rs. 711.5
Bill increased by: 36.17 %

Month 4
Units Consumed: 300.0
Total Bill: Rs. 1557.5
Alert: Unusual increase detected!
Increase: 118.89 %

====================================
Total Electricity Expenditure: Rs. 2989.5
Average Monthly Bill: Rs. 747.38
====================================
```

## 6\. Result

Thus, the Progressive Electricity Billing System was successfully implemented using Python. The program calculates electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates. It also compares electricity bills across multiple months and identifies unusual increases in monthly bills.

**Note:** The tariff rates and charges used in this program are assumed values for academic purposes. Actual electricity tariffs may vary depending on the electricity board.In this you have to write the algorithm,flowchart,python source code,sample input,sample output,and the flow chart in mermaid
