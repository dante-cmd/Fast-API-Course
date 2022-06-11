# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main=main())


async def printer(name: str, times: int) -> None:
    for i in range(times):
        print(name)
        await asyncio.sleep(1)

    async def main():
        await asyncio.gather(printer("A", 3), printer("B", 3))

    asyncio.run(main())

def goo():
    for _ in range(3):
        print(sum((x for x in range(20_000_000))))
        time.sleep(1)
        print('Two')

async def count():
    print(sum((x for x in range(20_000_000))))
    await asyncio.sleep(0.5)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    #goo()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")



def add_sum(x:int = 10) -> str:
    y = x + 8
    return y

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
