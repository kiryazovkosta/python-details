import asyncio

commands = {
    "even": lambda numbers: [n for n in numbers if n % 2 == 0],
    "odd": lambda numbers: [n for n in numbers if n % 2 != 0],
}

async def even_odd(*args):
    if args[-1] not in commands:
        return "error"
    return commands[args[-1]](args[:-1])

async def main():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even = await even_odd(*n, "even")
    print(even)
    odd = await even_odd(*n, "odd")
    print(odd)

if __name__ == "__main__":
    asyncio.run(main())