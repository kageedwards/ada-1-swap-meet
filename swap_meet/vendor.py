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