#!/usr/bin/env python3

# Display a welcome message
print("Welcome to the Future Value Calculator")
print()

#choice to continue
choice = "y"
while choice.lower() == "y":

    #Initialize Variables
    monthly_investment = 0
    monthly_interest_rate = 0
    years = 0
    monthly_interest_amount = 0

    # Get input from the user
    monthly_investment = int(input("Enter monthly investment: \t"))
    while monthly_investment <=0:
        print("Entry must be greater than 0. Please try again.\t")
        monthly_investment = int(input("Enter monthly investment: \t"))
        if monthly_investment >= 1:
            break

    yearly_interest_rate = int(input("Enter yearly interest rate: \t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        print("Entry must be greater than 0 and less than or equal to 15. Please try again.\t")
        yearly_interest_rate = int(input("Enter yearly interest rate: \t"))
        if yearly_interest_rate >= 1 and yearly_interest_rate <= 15:
            break

    years = int(input("Enter number of years\t\t"))
    while years <= 0 or years > 50:
        print("Entry must be greater than 0 and less than or equal to 50. Please try again.\t")
        years = int(input("Enter number of years: \t\t"))
        if years >=1 and years <= 50:
            break

    # Convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = 12

    future_value = 0
    # Calculate the future value & displays results
    print()
    years_count = 0
    for i in range(years):
        for i in range(months):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate
            future_value += monthly_interest_amount
        years_count += 1
        print("Years = : ",years_count, "Future Value = "+ str(round(future_value, 2)))

    # see if the user wants to continue
    print()
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
 
