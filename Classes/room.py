class room:
    def __init__(self, room_number, room_capacity):
        self._room_number = room_number
        self._room_capacity = room_capacity

    def get_room(self):
        return "Room: " + self._room_number + ", Capacity: " + self._room_capacity
    def get_room_number(self):
        return self._room_number

    def get_room_capacity(self):
        return self._room_capacity