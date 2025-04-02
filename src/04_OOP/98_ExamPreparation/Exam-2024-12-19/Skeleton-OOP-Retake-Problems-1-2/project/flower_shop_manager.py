from typing import List, Type
from collections import defaultdict

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.business_client import BusinessClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant

class FlowerShopManager:
    VALID_PLANTS: List[str] = ["Flower", "LeafPlant"]
    VALID_CLIENTS: List[str] = ["RegularClient", "BusinessClient"]

    def __init__(self):
        self.income = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float,
                  plant_water_needed: int, plant_extra_data: str) -> str:
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        if plant_type == self.VALID_PLANTS[0]:
            self.plants.append(Flower(plant_name, plant_price, plant_water_needed, plant_extra_data))
        else:
            self.plants.append(LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data))

        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        if any(c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")

        if client_type == self.VALID_CLIENTS[0]:
            self.clients.append(RegularClient(client_name, client_phone_number))
        else:
            self.clients.append(BusinessClient(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        plants = [p for p in self.plants if p.name == plant_name]
        if len(plants) == 0:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        order_amount = 0
        for index in range(plant_quantity):
            order_amount += (plants[index].price - (plants[index].price * (client.discount * 0.01)))
            self.plants.remove(plants[index])

        self.income += order_amount
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"


    def remove_plant(self, plant_name: str):
        plant = next((p for p in self.plants if p.name == plant_name), None)
        if plant is None:
            return "No such plant name."

        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"


    def remove_clients(self):
        clients = [c for c in self.clients if c.total_orders == 0]
        for c in clients:
            self.clients.remove(c)
        return f"{len(clients)} client/s removed."

    def shop_report(self):
        unsold_flowers = defaultdict(int)
        for p in self.plants:
            unsold_flowers[p.name] += 1
        sorted_plants = sorted(unsold_flowers.items(), key= lambda kvp: (-kvp[1], kvp[0]))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        result = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {sum(c.total_orders for c in self.clients)}",
            f"~~Unsold plants: {sum(v for k, v in sorted_plants)}~~"
        ]

        [result.append(f"{k}: {v}") for k, v in sorted_plants]
        result.append(f"~~Clients number: {len(sorted_clients)}~~")
        for c in sorted_clients:
            result.append(c.client_details())
        return '\n'.join(result)





