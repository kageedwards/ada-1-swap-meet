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