# Name: Hiep Pham

# import utilities (csv to read in files)
import csv
# import structure to create hash map to store packages in
from structure import parcel_hash_table


# parcel class
# Responsible for parcel instances to store into key value pairs
class Parcel:
    # Returns all relevant information on parcel
    # O(1) space-time complexity
    def __str__(self):
        return f'| PACKAGE: {self.parcel_id} ' \
               f'| WEIGHT: {self.parcel_weight} ' \
               f'| ADDRESS: {self.delivery_address} ' \
               f'| CITY: {self.delivery_city} ' \
               f'| ZIPCODE: {self.delivery_zip} ' \
               f'| DELIVERY: {self.delivery_delivery_time} ' \
               f'| DEADLINE: {self.delivery_deadline_time} ' \
               f'| STATUS: {self.delivery_status} '

    # constructor
    # O(1) space-time complexity
    def __init__(self, parcel_id, delivery_address, delivery_city, delivery_zip, delivery_deadline_time, parcel_weight):
        # parcel information
        # parcel id, will be hashed and become primary key in hash map
        self.parcel_id = parcel_id
        # parcel weight
        self.parcel_weight = parcel_weight

        # delivery information, based on csv file information
        # delivery address
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip

        # parcel delivery delivered time for status purposes
        self.delivery_delivery_time = None
        # delivery deadline time to be delivered by
        self.delivery_deadline_time = delivery_deadline_time
        # current delivery status to be updated by function set_delivery_status
        self.delivery_status = "Package is at hub awaiting carrier."
        # parcel delivery departure time for status purposes
        self.delivery_departure_time = None


# Loading parcels from package_file.csv into the newly created parcel hash table
# O(N) space-time complexity
with open("data_files/package_file.csv") as parcel_table_file:
    # for each parcel in the parcel table list
    for single_parcel in csv.reader(parcel_table_file):
        # inserts parcel into hash table
        parcel_hash_table.add_key_and_value(int(single_parcel[0]),
                                            Parcel(int(single_parcel[0]), single_parcel[1], single_parcel[2],
                                                   single_parcel[3], single_parcel[4], single_parcel[5]))
