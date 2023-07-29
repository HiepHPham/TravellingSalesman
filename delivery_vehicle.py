# Name: Hiep Pham

# import utilities (csv and datetime)
import csv
import datetime

# import hash map from parcel object class
from parcel import parcel_hash_table


# Vehicle "object" to instantiate for tracking vehicle purposes
class Vehicle:
    # Returns all relevant information about vehicle
    # O(1) space-time complexity
    def __str__(self):
        return f'Truck packages: {self.vehicle_parcels}\n' \
               f'Truck departure time: {self.vehicle_departure_time}\n' \
               f'Truck completion time: {self.vehicle_current_time}\n'

    # Constructor
    # O(N) space-time complexity
    def __init__(self, vehicle_name, vehicle_parcels, vehicle_departure_time):
        # vehicle name for print purposes
        self.vehicle_name = vehicle_name
        # vehicle's temporary load list
        self.vehicle_temp_load = []

        # vehicle's parcel list
        self.vehicle_parcels = vehicle_parcels
        # Iterate through all parcels in vehicle's parcels and adds to the temp load list
        # O(N) space-time complexity
        for parcel_id in self.vehicle_parcels:
            # Add the actual package object to the temp load list
            self.vehicle_temp_load.append(parcel_hash_table.obtain_value_based_on_key(parcel_id))

        # vehicle's departure time from hub
        self.vehicle_departure_time = vehicle_departure_time
        # vehicle's current time (used for delivered time tracking, initially set to vehicle's departure time)
        self.vehicle_current_time = vehicle_departure_time

        # vehicle's current address location
        self.vehicle_current_address = "4001 South 700 East"


# creating function to update vehicle status after a parcel delivery
# O(1)
def update_status_after_delivery(current_vehicle_instance, next_parcel):
    # Once we know the closest package, we can remove that package from the load
    current_vehicle_instance.vehicle_temp_load.remove(next_parcel)
    # Print that we have delivered the closest package, and stamp the time
    print(f'{current_vehicle_instance.vehicle_name} has just delivered package {next_parcel.parcel_id}')
    current_vehicle_instance.vehicle_current_time = current_vehicle_instance.vehicle_current_time + next_address_time
    # Print the details of the delivery: departure time and delivery time based on stamped time
    next_parcel.delivery_delivery_time = current_vehicle_instance.vehicle_current_time
    next_parcel.delivery_departure_time = current_vehicle_instance.vehicle_departure_time
    print(f'{current_vehicle_instance.vehicle_name} departed to deliver {next_parcel.parcel_id} at '
          f'{next_parcel.delivery_departure_time} and completed delivery at '
          f'{next_parcel.delivery_delivery_time}')


# creating function to update vehicle address after parcel delivery
def update_vehicle_address_after_delivery(current_vehicle_instance, next_parcel):
    # Set the new current address to be the current package's address (since we just delivered it after all), and
    # print that we will not depart from said address to deliver the next package
    current_vehicle_instance.vehicle_current_address = next_parcel.delivery_address
    print(f'{current_vehicle_instance.vehicle_name} will now depart from '
          f'{current_vehicle_instance.vehicle_current_address} to '
          f'deliver the next package.\n')


# create vehicle list to iterate through for delivery and print for user's situational awareness
vehicle_list = []
print("Vehicle fleet created")
print("\n---------------")
# Initialize package list, departure time, name, and combine all to create truck 1 object. Then append to fleet
vehicle1_name = "Truck 1"
print(f'Creating vehicle: {vehicle1_name}')
package_list_for_vehicle_1 = [1, 13, 14, 15, 16, 19, 20, 21, 22, 24, 26, 29, 31, 33, 34, 40]
print(f'Loading {vehicle1_name} with packages: {package_list_for_vehicle_1}')
vehicle1_departure = datetime.timedelta(hours=8, minutes=0)
print(f'Setting {vehicle1_name}\'s departure time as: {vehicle1_departure}')
vehicle1 = Vehicle(vehicle1_name, package_list_for_vehicle_1, vehicle1_departure)
print(f'{vehicle1_name} has been built.')
vehicle_list.append(vehicle1)
print(f'{vehicle1_name} has been added to the fleet.')
# Initialize package list, departure time, name, and combine all to create truck 2 object. Then append to fleet
print("\n---------------")
vehicle2_name = "Truck 2"
print(f'Creating vehicle: {vehicle2_name}')
package_list_for_vehicle_2 = [3, 6, 18, 23, 27, 30, 35, 36, 37, 38, 39]
print(f'Loading {vehicle2_name} with packages: {package_list_for_vehicle_2}')
vehicle2_departure = datetime.timedelta(hours=9, minutes=10)
print(f'Setting {vehicle2_name}\'s departure time as: {vehicle2_departure}')
vehicle2 = Vehicle(vehicle2_name, package_list_for_vehicle_2, vehicle2_departure)
print(f'{vehicle2_name} has been built.')
vehicle_list.append(vehicle2)
print(f'{vehicle2_name} has been added to the fleet.')
# Initialize package list, departure time, name, and combine all to create truck 3 object. Then append to fleet
print("\n---------------")
vehicle3_name = "Truck 3"
print(f'Creating vehicle: {vehicle3_name}')
package_list_for_vehicle_3 = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 25, 28, 32]
print(f'Loading {vehicle3_name} with packages: {package_list_for_vehicle_3}')
vehicle3_departure = datetime.timedelta(hours=10, minutes=5)
print(f'Setting {vehicle3_name}\'s departure time as: {vehicle3_departure}')
vehicle3 = Vehicle(vehicle3_name, package_list_for_vehicle_3, vehicle3_departure)
print(f'{vehicle3_name} has been built.')
vehicle_list.append(vehicle3)
print(f'{vehicle3_name} has been added to the fleet.')
print("\n---------------")
print(f'All trucks have been added to fleet. Current fleet information is as follows:')
# O(N)
for vehicle in vehicle_list:
    print(f'{str(vehicle)}')

# Initialize total mileage for all trucks
vehicle_total_mileage = 0.0
print(f'Total mileage for today has been reset to {vehicle_total_mileage}.\n'
      f'Deliveries will now begin:')
# Iterate through fleet list
# O(N^4)
for current_vehicle in vehicle_list:
    # Print truck delivery beginning for tracking purposes (and user situational awareness)
    print("------------\n")
    print(f'Beginning deliveries for {current_vehicle.vehicle_name}:\n')
    # while the temp load in the truck is not empty (temp load is actual packages)
    # O(N^3)
    while len(current_vehicle.vehicle_temp_load) != 0:
        # Instantiate a next_address_distance variable with large distance for initial comparison
        next_address_distance = 100
        # Nearest Neighbor Algorithm below
        # iterate through all parcels in load
        # O(N^2)
        for parcel_instance in current_vehicle.vehicle_temp_load:
            # Pull the vehicle address id and parcel address id from the address file csv
            with open("data_files/address_file.csv") as address_table_file_csv:
                # O(N)
                for entry in list(csv.reader(address_table_file_csv)):
                    # if the inputted address is equal to the address in the entry
                    if current_vehicle.vehicle_current_address in entry[2]:
                        # set the vehicle address id as the address id from that entry
                        vehicle_address_id = int(entry[0])
                    # if the inputted address is equal to the address in the entry
                    if parcel_instance.delivery_address in entry[2]:
                        # set the parcel address id as the address id from that entry
                        parcel_address_id = int(entry[0])
            # Check if the parcel is the nearest to the truck and save that parcel using distance file csv
            with open("data_files/distance_file.csv") as distance_table_file_csv:
                # Set variable distance_table as a list based on csv file information
                distance_table = list(csv.reader(distance_table_file_csv))
                # check if the cell exists; if not, set that cell to the flipped value (examine file for context)
                if distance_table[vehicle_address_id][parcel_address_id] == '':
                    # set the requested x, y coord to be the y, x coord (table is flipped)
                    distance_table[vehicle_address_id][parcel_address_id] = distance_table[parcel_address_id][
                        vehicle_address_id]
                #  if the package is closer than the currently set close package
                if float(distance_table[vehicle_address_id][parcel_address_id]) <= next_address_distance:
                    # set the next parcel
                    next_parcel_instance = parcel_instance
                    # set the address distance and time it takes for the truck to arrive
                    next_address_distance = float(distance_table[vehicle_address_id][parcel_address_id])
                    # we set the time as the distance divided by 18 because the truck moves at 18 mph
                    next_address_time = datetime.timedelta(hours=next_address_distance / 18)
        update_status_after_delivery(current_vehicle, next_parcel_instance)
        # Add to the total mileage to ensure we are meeting the below 140 miles requirement, and print total miles it
        # took to deliver the package
        vehicle_total_mileage = vehicle_total_mileage + next_address_distance
        print(f'Package {next_parcel_instance.parcel_id} took {next_address_distance} miles to deliver.')
        update_vehicle_address_after_delivery(current_vehicle, next_parcel_instance)
    # Once the entire load is empty, it will have meant that we finished delivery. Print details of the truck.
    print(f'{current_vehicle.vehicle_name} has just finished delivery: \n{current_vehicle}')
print("\n---------------")
print("Entire vehicle fleet has finished delivery.")
print(f'Current fleet information is as follows:')
# O(N)
for vehicle in vehicle_list:
    print(f'{str(vehicle)}')
