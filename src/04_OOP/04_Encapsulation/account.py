class Account:
    """
    Create a class called Account. Upon initialization, it should receive an id, a balance, and a pin (all numbers).
    The pin and the id should be private instance attributes, and the balance should be a public attribute.
    Create two public instance methods:
        · get_id(pin) - if the given pin is correct, return the id, otherwise, return "Wrong pin"
        · change_pin(old_pin, new_pin) - if the old pin is correct, change it to the new one and return "Pin changed",
        otherwise return "Wrong pin"
    """
    def __init__(self, id: int, balance: int, pin: int):
        self.id = id
        self.balance = balance
        self.pin = pin

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    def get_id(self, pin: int):
        if self.pin == pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int):
        if self.pin == old_pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))