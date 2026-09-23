from .item import Item

class Vendor:
    """Represents a vendor with an inventory of items"""

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """Accepts param item, appends to inventory, returns item"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes an item from inventory (if present) and returns item, else retuns None"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None

    def get_by_id(self, id):
        """Returns item from inventory with matching id, else None"""
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        """Removes my_item from the Vendor's inventory, adds to other_vendor inventory"""
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)

        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)

        return True

    def swap_first_item(self, other_vendor):
        """
        Removes first item from inventory and adds the friend's first item,
        removes the first items from friend's inventory, add the inventory
        instance's first item. Returns False if either inventory is empty, else
        returns True.
        """
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_by_category(self, category):
        """Returns a list of objects in the inventory containing the category"""
        matching_category = []

        for item in self.inventory:
            if item.get_category() == category:
                matching_category.append(item)

        return matching_category

    def get_best_by_category(self, category):
        """
        Looks for item in inventory with matching category and highest condition
        Returns the item, or None if no matches are found.
        """
        def get_max_condition(items):
            best_item = None

            for item in items:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item

            return best_item

        matching_items = self.get_by_category(category)

        return get_max_condition(matching_items)
