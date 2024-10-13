last_sector = input()
sector_rows = int(input())
odd_row_seats = int(input())

start_ascii = ord('A')
end_ascii = ord(last_sector) + 1
seat_start_ascii = ord('a')
counter = 0
for sector in range(start_ascii, end_ascii):
    for row in range(1, sector_rows + 1):
        seat_end_ascii = seat_start_ascii + odd_row_seats
        if row % 2 == 0:
            seat_end_ascii += 2
        for seat in range(seat_start_ascii, seat_end_ascii):
            print(f"{chr(sector)}{row}{chr(seat)}")
            counter += 1
    sector_rows += 1

print(counter)