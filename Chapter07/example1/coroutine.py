import asyncio

async def example():
    x = await do_stuff()
    return 'Hello world', x

async def very_long():
    while True:
        await asyncio.sleep(0)

