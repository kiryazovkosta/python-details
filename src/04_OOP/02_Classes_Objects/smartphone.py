class Smartphone:

    def __init__(self, memory: int, is_on: bool = False):
        self.memory = memory
        self.is_on = is_on
        self.apps = []

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on:
                self.memory -= app_memory
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())

phone = Smartphone(25)
phone.power()
