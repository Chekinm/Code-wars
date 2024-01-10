import asyncio

async def counter(name: str):
    for i in range(0, 100):
        print(f"{name}: {i!s}")
        print(int(name[-1])%2)
        await asyncio.sleep(int(name[-1])%2 + 1)

async def main():
    tasks = []
    for n in range(0, 4):
        tasks.append(asyncio.create_task(counter(f"task{n}")))

    while True:
        tasks = [t for t in tasks if not t.done()]
        if len(tasks) == 0:
            return

        await tasks[0]

asyncio.run(main())