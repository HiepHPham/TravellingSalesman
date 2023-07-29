# Name: Hiep Pham

# Import utilities datetime ValueError
import datetime
from builtins import ValueError
# Import hash table from parcel object class and delivery vehicle object class
from parcel import parcel_hash_table
import delivery_vehicle


# Main class
# Represents User interface
# O(N^2)
class Main:
    # Print total mileage for all vehicles from variable delivery_vehicle.vehicle_total_mileage
    print(f'Total mileage: {delivery_vehicle.vehicle_total_mileage}\n')
    # Initialize console_input to be = "start" for while loop
    console_input = "start"
    # While user does not input option to quit
    while console_input != "2":
        # (1) Inspect packages
        # O(N) space-time complexity
        if console_input == "1":
            # try block to handle invalid value error
            try:
                # Create formatted time to be user's requested time
                (hour, minute, second) = input("Enter time in HH:MM:SS format: ").split(":")
                formatted_time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
                # Iterate through all parcels (we know there are 40)
                for parcelID in range(1, 41):
                    # Update parcel's information based on time input. If delivery time is before input time
                    if parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_delivery_time < formatted_time:
                        # set status as delivered
                        parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_status = f'Delivered at: ' \
                                    f'{parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_delivery_time}'
                    # if departure time is before "current" time but delivery time is NOT before input time
                    elif parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_departure_time < formatted_time:
                        # update the status as en route to delivery and departed at {delivery_departure_time}
                        parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_status = f'En route. ' \
                                                                                                f'Departed at: ' \
                                    f'{parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_departure_time}'
                    # else (if "current" time is before both delivery and departure time)
                    else:
                        # update the status as at hub
                        parcel_hash_table.obtain_value_based_on_key(parcelID).delivery_status = "At the Hub."
                # Ask for user input on all packages or 1 package
                console_input = input("\n---------------------\n"
                                      "Select one of the following options to dive deeper by typing \"1\" or \"2\":\n"
                                      "(1) All packages\n"
                                      "(2) Specific package ID\n")
                # All packages
                if console_input == "1":
                    # Iterate through all parcels (we know there are 40)
                    for parcelID in range(1, 41):
                        # Print the string of hashtable value of parcel id in iteration
                        print(str(parcel_hash_table.obtain_value_based_on_key(parcelID)))
                # Single package
                elif console_input == "2":
                    # print string of hash table value of parcel id from input
                    print(str(parcel_hash_table.obtain_value_based_on_key(int(input("Enter package ID:")))))
                # all other inputs are invalid
                else:
                    # invalid option
                    print("Input not recognized. Try again")
            # When error caught, print "Invalid entry", then pass through and reiterate while loop
            except ValueError:
                print("Input not recognized. Try again")
        # (2) Quit program
        # O(1) space-time complexity
        elif console_input == "2":
            exit()
        # Initial pass through for the first iteration of while loop
        # O(1) space-time complexity
        elif console_input == "start":
            pass
        # If neither of 1, 2, 3, or start was passed, then print "Invalid entry", then iterate through while loop again
        # O(1) space-time complexity
        else:
            print("Input not recognized. Try again")
        # Set console_input for next while loop iteration
        console_input = input(
            "\n---------------------\n"
            "Select one of the following options to dive deeper by typing \"1\" or \"2\":\n"
            "(1) Inspect package(s) at a specified time\n"
            "(2) Quit\n")
    # Program complete print
    print("Program complete")
