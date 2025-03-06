from project.dvd import DVD
from project.customer import Customer

class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        if customer is None:
            return "Non existing customer"
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if dvd is None:
            return "Non existing dvd"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        c_id = next((c.id for c in self.customers if any([d.id for d in c.rented_dvds if d.id == dvd.id ])), None)
        if c_id is not None and c_id != customer_id:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        if customer is None:
            return "Non existing customer"
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if dvd is None:
            return "Non existing dvd"

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        output = []
        [output.append(c.__repr__()) for c in self.customers]
        [output.append(d.__repr__()) for d in self.dvds]
        return '\n'.join(output)


