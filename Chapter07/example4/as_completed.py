import asyncio
import random

async def delayed_value(value):
    await asyncio.sleep(random.randrange(5))
    return value

async def main():
    futures = [
        asyncio.ensure_future(delayed_value(1)),
        asyncio.ensure_future(delayed_value(2)),
        asyncio.ensure_future(delayed_value(3)),
        asyncio.ensure_future(delayed_value(4)),
        asyncio.ensure_future(delayed_value(5)),
    ]

    for future in asyncio.as_completed(futures):
        value = await future
        print(value)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(main()))
loop.close()
