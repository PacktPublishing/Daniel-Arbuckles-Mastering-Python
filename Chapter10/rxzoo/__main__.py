import asyncio

from .animals import zoo


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(zoo())
