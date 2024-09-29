visitors = int(input())

back_peoples = 0
chest_peoples = 0
legs_peoples = 0
abs_peoples = 0
shake_buyers = 0
bar_buyers = 0

for _ in range(0, visitors):
    action = input()
    if action == "Back":
        back_peoples += 1
    elif action == "Chest":
        chest_peoples += 1
    elif action == "Legs":
        legs_peoples += 1
    elif action == "Abs":
        abs_peoples += 1
    elif action == "Protein shake":
        shake_buyers += 1
    elif action == "Protein bar":
        bar_buyers += 1

training_peoples = back_peoples + chest_peoples + legs_peoples + abs_peoples
buying_peoples = shake_buyers + bar_buyers

print(f"{back_peoples} - back")
print(f"{chest_peoples} - chest")
print(f"{legs_peoples} - legs")
print(f"{abs_peoples} - abs")
print(f"{shake_buyers} - protein shake")
print(f"{bar_buyers} - protein bar")
print(f"{training_peoples/visitors * 100:.2f}% - work out")
print(f"{buying_peoples/visitors * 100:.2f}% - protein")