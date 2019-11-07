#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

#choice to continue
choice = "y"
while choice == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        tgc = round((cost_per_gallon * gallons_used), 2)
        cpm = round((cost_per_gallon * gallons_used / miles_driven), 1)
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", tgc)
        print("Cost Per Mile:             ", cpm)

    print()
    choice = input("Continue (y/n)?     ")
    print()

print()
print("Bye")
