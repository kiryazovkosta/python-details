from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        if subscription is None:
            raise ValueError("Invalid subscription")

        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        if customer is None:
            raise ValueError("Invalid customer")

        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        if trainer is None:
            raise ValueError("Invalid trainer")

        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        if plan is None:
            raise ValueError("Invalid plan")

        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)
        if equipment is None:
            raise ValueError("Invalid equipment")

        output = [
            f"{subscription.__repr__()}",
            f"{customer.__repr__()}",
            f"{trainer.__repr__()}",
            f"{equipment.__repr__()}",
            f"{plan.__repr__()}"
        ]
        return '\n'.join(output)