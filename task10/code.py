# Campus Event Financial Planning System

import math

# Get event details
print("CAMPUS EVENT FINANCIAL PLANNING")

participants = int(
    input("Enter expected number of participants: ")
)

venue_cost = float(
    input("Enter venue cost: Rs. ")
)

equipment_cost = float(
    input("Enter equipment cost: Rs. ")
)

transport_cost = float(
    input("Enter transportation cost: Rs. ")
)

catering_cost = float(
    input("Enter catering cost per participant: Rs. ")
)

certificate_cost = float(
    input("Enter certificate cost per participant: Rs. ")
)

registration_fee = float(
    input("Enter registration fee per participant: Rs. ")
)

sponsorship = float(
    input("Enter available sponsorship amount: Rs. ")
)


# Validate input
if (participants <= 0 or
    venue_cost < 0 or
    equipment_cost < 0 or
    transport_cost < 0 or
    catering_cost < 0 or
    certificate_cost < 0 or
    registration_fee < 0 or
    sponsorship < 0):

    print("\nInvalid Input! Please enter valid values.")

else:

    # Calculate fixed costs
    fixed_cost = (
        venue_cost +
        equipment_cost +
        transport_cost
    )

    # Calculate variable cost per participant
    variable_cost = (
        catering_cost +
        certificate_cost
    )

    # Calculate total variable cost
    total_variable_cost = (
        participants * variable_cost
    )

    # Calculate total event cost
    total_event_cost = (
        fixed_cost +
        total_variable_cost
    )

    # Calculate participant contributions
    participant_contribution = (
        participants * registration_fee
    )

    # Calculate total revenue
    total_revenue = (
        participant_contribution +
        sponsorship
    )

    # Calculate sponsorship shortfall
    sponsorship_shortfall = max(
        0,
        total_event_cost -
        participant_contribution -
        sponsorship
    )

    # Calculate break-even registrations
    remaining_fixed_cost = fixed_cost - sponsorship

    contribution_per_participant = (
        registration_fee - variable_cost
    )

    if remaining_fixed_cost <= 0:

        break_even = 0

    elif contribution_per_participant > 0:

        break_even = math.ceil(
            remaining_fixed_cost /
            contribution_per_participant
        )

    else:

        break_even = None

    # Determine event status
    if total_revenue >= total_event_cost:

        status = "Event is Financially Feasible"

    else:

        status = "Event is Running at a Loss"

    # Display financial report
    print("\n================================================")
    print("       CAMPUS EVENT FINANCIAL REPORT")
    print("================================================")

    print("\nEXPECTED PARTICIPANTS:", participants)

    print("\nEVENT EXPENSE DETAILS")

    print("-----------------------------------------------")

    print("Venue Cost: Rs.",
          round(venue_cost, 2))

    print("Equipment Cost: Rs.",
          round(equipment_cost, 2))

    print("Transportation Cost: Rs.",
          round(transport_cost, 2))

    print("Catering Cost: Rs.",
          round(total_variable_cost - participants *
                certificate_cost, 2))

    print("Certificate Cost: Rs.",
          round(participants * certificate_cost, 2))

    print("-----------------------------------------------")

    print("Total Fixed Cost: Rs.",
          round(fixed_cost, 2))

    print("Total Variable Cost: Rs.",
          round(total_variable_cost, 2))

    print("TOTAL EVENT COST: Rs.",
          round(total_event_cost, 2))

    print("\nREVENUE DETAILS")

    print("-----------------------------------------------")

    print("Registration Fee per Participant: Rs.",
          round(registration_fee, 2))

    print("Participant Contributions: Rs.",
          round(participant_contribution, 2))

    print("Available Sponsorship: Rs.",
          round(sponsorship, 2))

    print("Total Available Revenue: Rs.",
          round(total_revenue, 2))

    print("-----------------------------------------------")

    print("\nSPONSORSHIP ANALYSIS")

    print("Additional Sponsorship Required: Rs.",
          round(sponsorship_shortfall, 2))

    print("\nBREAK-EVEN ANALYSIS")

    if break_even is not None:

        print("Minimum Registrations Required:",
              break_even)

    else:

        print("Break-even cannot be achieved with the "
              "current registration fee.")

    print("Actual Expected Registrations:",
          participants)

    print("\nEVENT FINANCIAL STATUS:", status)

    if total_revenue >= total_event_cost:

        print("Event Surplus: Rs.",
              round(total_revenue - total_event_cost, 2))

    else:

        print("Financial Deficit: Rs.",
              round(total_event_cost - total_revenue, 2))

    print("================================================")
Here you have to write the code
