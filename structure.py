# Name: Hiep Pham

# structure class
# Responsible for creating hash map to store key-value pairs
# This hash map will store packages, and the keys will be the package IDs hashed
class Structure:
    # PART E of scenario
    # Insert a new package value into the hash table based on key,
    # O(N) space-time complexity
    def add_key_and_value(self, key, value):
        # iterate through all the key value pairs in hash table
        for key_value_pair in self.list[int(key) % len(self.list)]:
            # if the key of the pair matches the inputted key
            if key_value_pair[0] == key:
                # set the value of the key to be the updated key value pair
                key_value_pair[1] = [key, value]
        # append the value of the key to the list at the hash location
        self.list[int(key) % len(self.list)].append([key, value])

    # Part F of scenario
    # Returns value from the hash table based on key if exists. If it doesn't exist, return None.
    # O(N) space-time complexity
    def obtain_value_based_on_key(self, key):
        # iterate through all key value pairs in hash table
        for key_value_pair in self.list[int(key) % len(self.list)]:
            # if the key in the key value pair matches inputted key
            if key_value_pair[0] == key:
                # return the value of the key value pair
                return key_value_pair[1]

    # Self constructor
    # O(N) space-time complexity
    def __init__(self, capacity_of_hash_map=30):
        # Initialize the hash table with empty list
        self.list = []
        # for each slot in hash table
        for iterator in range(capacity_of_hash_map):
            # add an empty list to contain a key value pair
            self.list.append([])


# Initialize hash table for use in program
parcel_hash_table = Structure()
