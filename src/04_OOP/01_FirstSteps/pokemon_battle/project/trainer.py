from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name:str, pokemons: [Pokemon] = None):
        self.name = name
        self.pokemons = pokemons if pokemons is not None else []

    def add_pokemon(self, pokemon: Pokemon):
        pokemon_exists = any(p.name == pokemon.name for p in self.pokemons)
        if not pokemon_exists:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon:
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = [
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemons)}"
        ]

        for p in self.pokemons:
            result.append(f"- {p.pokemon_details()}")

        return '\n'.join(result)
