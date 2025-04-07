from collections import defaultdict

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS = ["Flower", "LeafPlant"]
    VALID_CLIENTS = ["RegularClient","BusinessClient"]

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data) if plant_type == self.VALID_PLANTS[0] \
            else LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        if any( c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")

        client_class = RegularClient if client_type == self.VALID_CLIENTS[0] else BusinessClient
        self.clients.append(client_class(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        plants = [p for p in self.plants if p.name == plant_name]
        if len(plants) == 0:
            raise ValueError("Plants not found!")

        if plant_quantity > len(plants):
            return f"Not enough plant quantity."

        order_amount: float = 0.0
        for index in range(plant_quantity):
            self.plants.remove(plants[index])
            income = plants[index].price - (plants[index].price * (client.discount * 0.01))
            self.income += income
            order_amount += income

        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"


    def remove_plant(self, plant_name: str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return f"No such plant name."

        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"


    def remove_clients(self):
        clients_with_no_orders = [c for c in self.clients if c.total_orders == 0]
        for client in clients_with_no_orders:
            self.clients.remove(client)

        return f"{len(clients_with_no_orders)} client/s removed."


    def shop_report(self):
        result = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {sum([c.total_orders for c in self.clients])}"
        ]

        unsold_plants = defaultdict(int)
        for p in self.plants:
            unsold_plants[p.name] += 1

        result.append(f"~~Unsold plants: {sum([up for up in unsold_plants.values()])}~~")
        for plant_name, count in sorted(unsold_plants.items(), key=lambda kvp:(-kvp[1], kvp[0])):
            result.append(f"{plant_name}: {count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted(self.clients, key=lambda k: (-k.total_orders, k.phone_number)):
            result.append(f"{client.client_details()}")

        return '\n'.join(result)
