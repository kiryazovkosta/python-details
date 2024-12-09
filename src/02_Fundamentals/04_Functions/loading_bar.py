START_STEP = 1
END_STEP = 11
STEP = 10

number = int(input())

parts = int((number / 100) * STEP)

message = "["
for step in range(START_STEP, END_STEP):
    if step <= parts:
        message += "%"
    else:
        message += "."
message += "]"

if parts == 10:
    print(f"{number}% Complete!\n{message}")
else:
    print(f"{number}% {message}\nStill loading...")