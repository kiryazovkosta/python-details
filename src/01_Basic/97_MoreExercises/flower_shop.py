from math import ceil, floor

MAGNOLIA_PRICE = 3.25
ZUMBUL_PRICE = 4
ROSE_PRICE = 3.50
CACTUS_PRICE = 8
TAXES = 0.05

def main():
    magnolias = int(input())
    zumbuls = int(input())
    roses = int(input())
    cactuses = int(input())
    gift_price = float(input())

    total = (magnolias * MAGNOLIA_PRICE
             + zumbuls * ZUMBUL_PRICE
             + roses * ROSE_PRICE
             + cactuses * CACTUS_PRICE)
    total -= total * TAXES
    difference = total - gift_price
    if difference >= 0:
        print(f"She is left with {floor(difference)} leva.")
    else:
        print(f"She will have to borrow {ceil(abs(difference))} leva.")


if __name__ == "__main__":
    main()