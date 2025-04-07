from project.clients.base_client import BaseClient

class BusinessClient(BaseClient):
    ZERO: float = 0.0
    DISCOUNT: float = 10.0
    ORDERS_COUNT_FOR_DISCOUNT = 2

    def update_discount(self):
        self.discount = self.DISCOUNT if self.total_orders >= self.ORDERS_COUNT_FOR_DISCOUNT else self.ZERO