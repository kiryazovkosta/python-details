destination = ""
while destination != "End":
    destination = input()
    if destination == "End":
        break
        
    price = float(input())
    balance = 0.0
    while balance < price:
        balance += float(input())
    print(f"Going to {destination}!")