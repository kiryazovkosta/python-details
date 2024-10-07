GELS = {
    "Watermelon": {"small": 56, "big": 28.70 },
    "Mango": {"small": 36.66, "big": 19.60 },
    "Pineapple": {"small": 42.10, "big": 24.80 },
    "Raspberry": {"small": 20, "big": 15.20 },
}

fruit = input()
size = input()
gels_count = int(input())
package_size = 2 if size == "small" else 5

gels_price = GELS[fruit][size] * gels_count * package_size
if gels_price > 1000:
    gels_price -= gels_price * 0.50
elif gels_price >= 400:
    gels_price -= gels_price * 0.15

print(f"{gels_price:.2f} lv.")