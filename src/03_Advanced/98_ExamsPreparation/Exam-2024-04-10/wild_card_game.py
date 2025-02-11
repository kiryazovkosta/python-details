def draw_cards(*args, **kwargs):

    monsters = [card[0] for card in args if card[1] == "monster"]
    spells = [card[0] for card in args if card[1] == "spell"]

    for key, value in kwargs.items():
        if value == "monster":
            monsters.append(key)
        elif value == "spell":
            spells.append(key)

    result = []
    if monsters:
        monsters.sort(reverse=True)
        result.append("Monster cards:")
        for name in monsters:
            result.append(f"  ***{name}")
    if spells:
        spells.sort()
        result.append("Spell cards:")
        for name in spells:
            result.append(f"  $$${name}")
    return '\n'.join(result)

print(draw_cards(("cyber dragon","monster"), freeze="spell",))
print("==========")
print(draw_cards(("celtic guardian", "monster"),("earthquake", "spell"),("fireball", "spell"), raigeki="spell", destroy="spell",))
print("==========")
print(draw_cards(("brave attack","spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
print("==========")