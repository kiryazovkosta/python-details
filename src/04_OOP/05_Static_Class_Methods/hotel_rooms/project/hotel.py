from project.room import Room

class Hotel:
    def __init__(self, name: str, guests: int = 0):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = guests

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            take_result = room.take_room(people)
            if take_result is None:
                self.guests += people

    def free_room(self, room_number: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            current_quests = room.guests
            free_result = room.free_room()
            if free_result is None:
                self.guests -= current_quests

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
                f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")