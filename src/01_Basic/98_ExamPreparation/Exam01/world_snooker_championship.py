phase = input()
ticket_type = input()
ticket_number = int(input())
picture = input()

ticket_price = 0.0

if phase == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif phase == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400.00

total_price = ticket_number * ticket_price
if total_price > 4000:
    total_price -= total_price * 0.25
else:
    if total_price > 2500:
        total_price -= total_price * 0.1

    if picture == "Y":
        total_price += ticket_number * 40

print(f"{total_price:.2f}")