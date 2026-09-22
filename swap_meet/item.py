import uuid
class Item:
    ## Optional future ID integrity storage
    ## beyond requirements and not
    ## compatible with current test suite
    # valid_id_store = set()

    def check_id_validity(self, new_id):
        return (
            ## Is an integer
            isinstance(new_id, int)
            ## is a positive number
            and new_id > 0
            ## is unique in our global valid_id_store
            # and new_id not in self.valid_id_store
        )

    def __init__(self, id=None, condition=0.0):
        # The `id` argument *might* be a good id
        id_candidate = id

        # Repeatedly generate a UUID if not unique
        # Should most certainly only run one or two iterations
        while True:
            # Current candidate is unique enough
            if self.check_id_validity(id_candidate):
                break

            # Generate an ID from a new UUID
            new_uuid = uuid.uuid4()
            id_candidate = int(new_uuid)

        # Return the final tested ID (int)
        self.id = id_candidate
        ## Optional fully unique IDs
        # self.valid_id_store.add(id_candidate)


        # Initialize the item's condition
        if condition <= 0.0:
            condition = 0.0
        elif condition >= 5.0:
            self.condition = 5.0
        else:
            self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return "Item"

    def condition_description(self):
        if self.condition <= 1.0:
            return "poor"
        elif self.condition <= 2.0:
            return "okay"
        elif self.condition <= 3.0:
            return "good"
        elif self.condition <= 4.0:
            return "very Good"
        else:
            return "amazing"