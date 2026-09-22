from .item import Item
class Electronics(Item):
    def __init__(self, id=None, condition=0.0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        common_string = super().__str__()
        return f"{common_string} This is a {self.type} device."