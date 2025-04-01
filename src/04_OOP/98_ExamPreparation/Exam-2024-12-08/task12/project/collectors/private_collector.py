from project.collectors.base_collector import BaseCollector

class PrivateCollector(BaseCollector):
    MONEY = 5000.0
    INITIAL_MONEY = 25000.0
    INITIAL_SPACE = 3000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_MONEY, self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += self.MONEY


        