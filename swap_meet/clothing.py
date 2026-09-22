from .item import Item
class Clothing(Item):
    def __init__(self, id=None, condition=0.0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        common_string = super().__str__()
        return f"{common_string} It is made from {self.fabric} fabric."