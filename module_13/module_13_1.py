import time
import asyncio

async def start_strongman(name, power):
    num_balls = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(1, num_balls+1):
        await  asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    strongman_1 = asyncio.create_task(start_strongman('Иван', 10))
    strongman_2 = asyncio.create_task(start_strongman('Миша', 5))
    strongman_3 = asyncio.create_task(start_strongman('Петя', 1))

    await strongman_1
    await strongman_2
    await strongman_3

start = time.time()
asyncio.run(start_tournament())
end = time.time()
print(end-start)

