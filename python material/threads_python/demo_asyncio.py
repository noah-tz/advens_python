import asyncio as ayo
import time

async def omelet():
    await ayo.sleep(3)
    print('1 omelet is ready')

async def toast():
    await ayo.sleep(2)
    print('1 toast is ready')

async def salad():
    await ayo.sleep(5)
    print('1 salad is ready')

async def breakfast(persons=1):
    await ayo.gather(
        *[toast() for _ in range(persons * 2)],
        *[salad() for _ in range(persons)],
        *[omelet() for _ in range(persons)],
    )
    print('Breakfast is ready')

def main():
    time_start = time.time()
    ayo.run(breakfast(20))
    time_end = time.time()
    print(f'Time elapsed: {time_end - time_start} seconds')

if __name__ == "__main__":
    main()
