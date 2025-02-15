def list_roman_emperors(*args, **kwargs) ->str:
    successful = {name: kwargs[name] for name, value in args if value == True}
    unsuccessful = {name: kwargs[name] for name, value in args if value == False}

    result = [f"Total number of emperors: {len(args)}"]
    if successful:
        result.append("Successful emperors:")
        for name, years in sorted(successful.items(), key=lambda kvp: (-kvp[1], kvp[0])):
            result.append(f"****{name}: {years}")
    if unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, years in sorted(unsuccessful.items(), key=lambda kvp: (kvp[1], kvp[0])):
            result.append(f"****{name}: {years}")
    return "\n".join(result)


print(list_roman_emperors(("Augustus", True),("Nero", False), Augustus=40, Nero=14))

print(list_roman_emperors(("Augustus", True),("Trajan", True), ("Nero",False), ("Caligula",False), ("Pertinax",False), ("Vespasian",True), Augustus=40,Trajan=19, Nero=14,Caligula=4, Pertinax=4,Vespasian=19))

print(list_roman_emperors(("Augustus", True),("Trajan", True),("Claudius", True),Augustus=40, Trajan=19,Claudius=13,))