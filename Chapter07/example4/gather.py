import asyncio
import random

async def delayed_print(value):
    await asyncio.sleep(random.randrange(5))
    print(value)

main = asyncio.gather(
    asyncio.ensure_future(delayed_print(1)),
    asyncio.ensure_future(delayed_print(2)),
    asyncio.ensure_future(delayed_print(3)),
    asyncio.ensure_future(delayed_print(4)),
    asyncio.ensure_future(delayed_print(5)),
)

loop = asyncio.get_event_loop()
loop.run_until_complete(main)
loop.close()
