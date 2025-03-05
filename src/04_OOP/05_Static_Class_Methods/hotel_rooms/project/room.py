class Room:
    def __init__(self, number: int, capacity: int, guests: int = 0, is_taken: bool = False):
        self.number = number
        self.capacity = capacity
        self.guests = guests
        self.is_taken = is_taken

    def take_room(self, people: int):
        if not self.is_taken:
            if self.guests + people > self.capacity:
                return f"Room number {self.number} cannot be taken"

            self.guests += people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"
