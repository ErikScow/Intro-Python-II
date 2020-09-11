# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return f"room name: {self.name}\n    description: {self.description}"

    def get_item(self, itemReceived):
        self.items.append(itemReceived)

    def remove_item(self, itemRemoved):
        for index, item in enumerate(self.items, start=0):
            if item.name == itemRemoved.name:
                del self.items[index]