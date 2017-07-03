import asyncio

async def using_queues():
    q = asyncio.Queue()

    q.put_nowait('Hello')

    await q.get()

    await q.put('world')

    q.get_nowait()


    pq = asyncio.PriorityQueue()

    stack = asyncio.LifoQueue()
