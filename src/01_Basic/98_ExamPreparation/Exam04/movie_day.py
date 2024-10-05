time = int(input())
scenes = int(input())
scene_duration = int(input())

preparation = time * 0.15
total = scenes * scene_duration + preparation
diff = time - total
if time >= total:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(abs(diff))} minutes.")