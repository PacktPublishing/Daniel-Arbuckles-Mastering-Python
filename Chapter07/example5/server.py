import asyncio
import contextlib

async def serve(reader, writer):
    while True:
        try:
            request = await reader.readline()
        except ConnectionResetError:
            return
        if request == b'':
            return
        elif request == b'ping\n':
            writer.write(b'pong\n')
        else:
            writer.write(b'done\n')

async def launch(host, port):
    server = await asyncio.start_server(serve, host, port)
    await server.wait_closed()

main = asyncio.ensure_future(launch('127.0.0.1', 8899))
loop = asyncio.get_event_loop()

with contextlib.closing(loop):
    loop.run_until_complete(main)

