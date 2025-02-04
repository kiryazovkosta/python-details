def sorting_cheeses(**kwargs):
    output = ""
    result = sorted(kwargs.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]) )
    for cheese_name, quantities in result:
        output += cheese_name + "\n"
        for quantity in sorted(quantities, reverse=True):
            output += f"{quantity}\n"
    return output
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)