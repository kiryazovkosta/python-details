def list_roman_emperors(*args, **kwargs) ->str:
    return f"Total number of emperors: {len(args)}"


print(list_roman_emperors(("Augustus", True),("Nero", False), Augustus=40, Nero=14))

print(list_roman_emperors(("Augustus", True),("Trajan", True), ("Nero",False), ("Caligula",False), ("Pertinax",False), ("Vespasian",True), Augustus=40,Trajan=19, Nero=14,Caligula=4, Pertinax=4,Vespasian=19))