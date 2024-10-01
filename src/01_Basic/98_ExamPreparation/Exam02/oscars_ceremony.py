rent = int(input())

statuettes = rent - rent * 0.3
catering = statuettes - statuettes * 0.15
sound = catering / 2
total = rent + statuettes + catering + sound
print(f"{total:.2f}")