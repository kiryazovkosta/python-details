import sys
movies_count = int(input())

lowest_rating = sys.maxsize
lowest_name = ''
highest_rating = -sys.maxsize
highest_name = ''
total_ratings = 0

for _ in range(0, movies_count):
    name = input()
    rating = float(input())

    total_ratings += rating

    if rating < lowest_rating:
        lowest_rating = rating
        lowest_name = name

    if rating > highest_rating:
        highest_rating = rating
        highest_name = name

print(f"{highest_name} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_name} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {total_ratings/movies_count:.1f}")