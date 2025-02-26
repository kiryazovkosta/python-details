class Player:

    def __init__(self, name: str, hp: int, mp: int, guild: str = "Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = guild
        self.skills = {}

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = [f"Name: {self.name}",f"Guild: {self.guild}", f"HP: {self.hp}",f"MP: {self.mp}"]
        for k, v in self.skills.items():
            result.append(f"==={k} - {v}")
        return '\n'.join(result)
    