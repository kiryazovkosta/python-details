from typing import List
from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return next((pr for pr in self.products if pr.name == product_name), None)

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{pr.name}: {pr.quantity}" for pr in self.products])

