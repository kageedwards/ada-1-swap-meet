from .item import Item
class Decor(Item):
    def __init__(self, id=None, width=0, length=0):
        super().__init__(id)
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"

    def __str__(self):
        common_string = super().__str__()
        return f"{common_string} It takes up a {self.width} by {self.length} sized space."