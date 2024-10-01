def calc_month_tax():
    if contract_period == "one":
        if contract_type == "Small":
            month_tax = 9.98
        elif contract_type == "Middle":
            month_tax = 18.99
        elif contract_type == "Large":
            month_tax = 25.98
        else:
            month_tax = 35.99
    else:
        if contract_type == "Small":
            month_tax = 8.58
        elif contract_type == "Middle":
            month_tax = 17.09
        elif contract_type == "Large":
            month_tax = 23.59
        else:
            month_tax = 31.79
    return month_tax

def calc_discount():
    if mobile_internet == "yes":
        if tax <= 10.00:
            return 5.50
        elif tax <= 30.00:
            return 4.35
        else:
            return 3.85


contract_period = input()
contract_type = input()
mobile_internet = input()
months = int(input())

tax = calc_month_tax()
if mobile_internet == "yes":
    tax += calc_discount()
total_sum = months * tax
if contract_period == "two":
    total_sum -= total_sum * 0.0375
print(f"{total_sum:.2f} lv.")
