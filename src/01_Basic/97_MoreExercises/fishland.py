skumria_per_kg = float(input())
cace_per_kg = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_per_kg = skumria_per_kg + skumria_per_kg * 0.6
safrid_per_kg = cace_per_kg + cace_per_kg * 0.8

total = ( palamud * palamud_per_kg
          + safrid * safrid_per_kg
          + midi * 7.50)
print(f"{total:.2f}")