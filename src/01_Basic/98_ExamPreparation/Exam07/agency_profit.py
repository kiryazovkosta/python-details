company = input()
tickets_count = int(input())
kids_tickets = int(input())
ticket_price = float(input())
fee_tax = float(input())

kid_price = ticket_price - ticket_price * 0.7

profit = (tickets_count * ticket_price +
          kids_tickets * kid_price +
          (tickets_count + kids_tickets) * fee_tax)
print(f"The profit of your agency from {company} tickets is {profit * 0.2:.2f} lv.")