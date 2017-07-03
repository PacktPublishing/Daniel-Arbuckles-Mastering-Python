import asyncio

async def call_coro(coro):
    x = await coro()

async def call_coro_with_five_second_timeout(coro):
    x = await asyncio.wait_for(coro(), 5)

async def call_coro_with_timeout_and_handle_exception(coro):
    try:
        x = await asyncio.wait_for(coro(), 5)
    except asyncio.TimeoutError:
        print('Too slow')

