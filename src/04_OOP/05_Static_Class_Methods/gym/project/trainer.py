class Trainer:
    id = 1

    def __init__(self, name: str):
        self.id = Trainer.id
        self.name = name
        Trainer.id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id