import asyncio

async def get_future_values(future1, future2):
    value1 = await future1
    value2 = future2.result() if future2.done() else None
    return value1, value2
