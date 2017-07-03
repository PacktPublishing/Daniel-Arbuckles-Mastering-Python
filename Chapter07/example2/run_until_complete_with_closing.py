import asyncio
import logging
import contextlib

async def coro1():
    while True:
        for i in range(100000):
            await asyncio.sleep(0.1)
        print('coro1')

async def coro2():
    for i in range(25):
        await asyncio.sleep(0.5)
        print(i)

logging.getLogger('asyncio').setLevel('CRITICAL')

asyncio.ensure_future(coro1())
f = asyncio.ensure_future(coro2())

with contextlib.closing(asyncio.get_event_loop()) as loop:
    loop.run_until_complete(f)
