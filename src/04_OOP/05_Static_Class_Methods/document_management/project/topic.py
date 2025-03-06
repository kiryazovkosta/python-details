class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.id = id
        self.__topic = topic
        self.__storage_folder = storage_folder

    @property
    def topic(self):
        return self.__topic
    @topic.setter
    def topic(self, value):
        self.__topic = value

    @property
    def storage_folder(self):
        return self.__storage_folder
    @storage_folder.setter
    def storage_folder(self, value):
        self.__storage_folder = value

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"