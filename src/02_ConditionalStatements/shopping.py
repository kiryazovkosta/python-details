VIDEO_CARD_PRICE = 250
budget = float(input())
video_cards = int(input())
processors = int(input())
rams = int(input())

video_cards_price = video_cards * VIDEO_CARD_PRICE
single_processor_price = video_cards_price * 0.35
processors_price = processors * single_processor_price
single_ram_price = video_cards_price * 0.1
rams_price = rams * single_ram_price

total_price = video_cards_price + processors_price + rams_price
if video_cards > processors:
    total_price = total_price - (total_price * 0.15)

remaining_money = budget - total_price
if remaining_money >= 0:
    print(f"You have {remaining_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(remaining_money):.2f} leva more!")