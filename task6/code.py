# Railway Fare and Reservation Calculator

passengers = []

# Travel class fare rates
fare_rates = {
    "sleeper": 1.50,
    "ac 3-tier": 2.50,
    "ac 2-tier": 3.50
}

# Reservation fees
reservation_fees = {
    "sleeper": 20,
    "ac 3-tier": 40,
    "ac 2-tier": 60
}


# Function to calculate distance slab charge
def distance_charge(distance):

    if distance <= 100:
        return 0

    elif distance <= 300:
        return 50

    else:
        return 100


# Function to calculate age concession
def age_concession(age, fare):

    if age < 5:
        return fare

    elif age >= 60:
        return fare * 0.20

    else:
        return 0


# Function to calculate cancellation penalty
def cancellation_penalty(ticket_amount, hours):

    if hours <= 24:
        rate = 0.25

    elif hours <= 48:
        rate = 0.15

    else:
        rate = 0.05

    return ticket_amount * rate


# Get number of passengers
n = int(input("Enter number of passengers: "))

if n <= 0:
    print("Invalid number of passengers!")

else:

    # Process passenger details
    for i in range(n):

        print("\nEnter Passenger Details", i + 1)

        name = input("Enter passenger name: ")

        age = int(input("Enter passenger age: "))

        distance = float(
            input("Enter travel distance (KM): ")
        )

        travel_class = input(
            "Enter travel class (Sleeper/AC 3-Tier/AC 2-Tier): "
        ).lower().strip()

        # Validate details
        if (age < 0 or distance <= 0 or
            travel_class not in fare_rates):

            print("Invalid passenger details! Skipping passenger.")
            continue

        # Calculate basic fare
        basic_fare = distance * fare_rates[travel_class]

        # Calculate distance charge
        slab_charge = distance_charge(distance)

        # Calculate fare before concession
        subtotal = basic_fare + slab_charge

        # Calculate age concession
        concession = age_concession(age, subtotal)

        # Calculate reservation fee
        reservation_fee = reservation_fees[travel_class]

        # Calculate ticket amount
        ticket_amount = (
            subtotal - concession + reservation_fee
        )

        # Check cancellation status
        cancelled = input(
            "Is ticket cancelled? (yes/no): "
        ).lower().strip()

        penalty = 0
        refund = 0
        final_amount = ticket_amount

        if cancelled == "yes":

            hours = float(
                input("Enter hours before departure: ")
            )

            if hours < 0:
                print("Invalid cancellation time! Skipping passenger.")
                continue

            penalty = cancellation_penalty(
                ticket_amount, hours
            )

            refund = ticket_amount - penalty

            final_amount = 0

        elif cancelled != "no":

            print("Invalid cancellation status! Skipping passenger.")
            continue

        # Store passenger details
        passengers.append({

            "name": name,
            "age": age,
            "distance": distance,
            "class": travel_class,
            "basic": basic_fare,
            "slab": slab_charge,
            "concession": concession,
            "reservation": reservation_fee,
            "ticket": ticket_amount,
            "penalty": penalty,
            "refund": refund,
            "final": final_amount,
            "status": cancelled

        })


    # Display reservation statement
    print("\n==============================================")
    print("       RAILWAY RESERVATION STATEMENT")
    print("==============================================")

    for i, p in enumerate(passengers, start=1):

        print("\nPassenger Number:", i)

        print("Passenger Name:", p["name"])

        print("Age:", p["age"])

        print("Travel Distance:", p["distance"], "KM")

        print("Travel Class:", p["class"].upper())

        print("----------------------------------------------")

        print("Basic Fare: Rs.", round(p["basic"], 2))

        print("Distance Slab Charge: Rs.",
              round(p["slab"], 2))

        print("Age Concession: Rs.",
              round(p["concession"], 2))

        print("Reservation Fee: Rs.",
              round(p["reservation"], 2))

        print("Ticket Amount: Rs.",
              round(p["ticket"], 2))

        if p["status"] == "yes":

            print("Cancellation Penalty: Rs.",
                  round(p["penalty"], 2))

            print("Refund Amount: Rs.",
                  round(p["refund"], 2))

            print("Booking Status: Cancelled")

        else:

            print("Final Payable Amount: Rs.",
                  round(p["final"], 2))

            print("Booking Status: Confirmed")

        print("----------------------------------------------")


    # Calculate summary
    if passengers:

        total_collection = sum(
            p["final"] for p in passengers
        )

        total_refund = sum(
            p["refund"] for p in passengers
        )

        total_penalty = sum(
            p["penalty"] for p in passengers
        )

        print("\n==============================================")
        print("          RAILWAY BILL SUMMARY")
        print("==============================================")

        print("Total Passengers:", len(passengers))

        print("Confirmed Tickets:",
              sum(1 for p in passengers
                  if p["status"] == "no"))

        print("Cancelled Tickets:",
              sum(1 for p in passengers
                  if p["status"] == "yes"))

        print("Total Ticket Collection: Rs.",
              round(total_collection, 2))

        print("Total Cancellation Penalty: Rs.",
              round(total_penalty, 2))

        print("Total Refund Amount: Rs.",
              round(total_refund, 2))

        print("==============================================")

    else:

        print("No valid passenger records available.")
Here you have to write the code
