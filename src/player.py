# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self):
        return f"name: {self.name}\n    current room: {self.current_room}"

    def change_room(self, new_room):
        self.current_room = new_room

    def add_item(self, itemAdded):
        self.items.append(itemAdded)

    def drop_item(self, itemDropped):
        for index, item in enumerate(self.items, start=0):
            if item.name == itemDropped.name:
                del self.items[index]
