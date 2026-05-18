import asyncio
import websockets

async def chat():

    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:

        print("チャット開始")

        async def receive():

            while True:

                message = await websocket.recv()

                print(f"\n相手: {message}")

        async def send():

            while True:

                text = input("あなた: ")

                await websocket.send(text)

        await asyncio.gather(
            receive(),
            send()
        )

asyncio.run(chat())