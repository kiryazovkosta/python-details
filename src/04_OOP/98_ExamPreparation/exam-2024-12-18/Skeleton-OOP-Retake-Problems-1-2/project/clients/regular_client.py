from project.clients.base_client import BaseClient

class RegularClient(BaseClient):
    ZERO: float = 0.0
    DISCOUNT: float = 5.0
    ORDERS_COUNT_FOR_DISCOUNT = 1

    def update_discount(self):
        self.discount = self.DISCOUNT if self.total_orders >= self.ORDERS_COUNT_FOR_DISCOUNT else self.ZERO