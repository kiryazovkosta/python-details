from functools import total_ordering
from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker is None:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total = sum(w.salary for w in self.workers)
        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        result.append(f"----- {len(lions)} Lions:")
        [result.append(l.__repr__()) for l in lions]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        result.append(f"----- {len(tigers)} Tigers:")
        [result.append(t.__repr__()) for t in tigers]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        [result.append(c.__repr__()) for c in cheetahs]
        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        result.append(f"----- {len(keepers)} Keepers:")
        [result.append(k.__repr__()) for k in keepers]

        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        result.append(f"----- {len(caretakers)} Caretakers:")
        [result.append(c.__repr__()) for c in caretakers]

        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        result.append(f"----- {len(vets)} Vets:")
        [result.append(v.__repr__()) for v in vets]
        return '\n'.join(result)








