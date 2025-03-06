class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"