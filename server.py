from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

import uvicorn
import json

app = FastAPI()

clients = []

@app.get("/")
async def get():

    return FileResponse("index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    clients.append(websocket)

    print("接続:", len(clients))

    try:

        while True:

            data = await websocket.receive_text()

            message = json.loads(data)

            text = message["text"]

            print("受信:", text)

            disconnected = []

            for client in clients:

                if client != websocket:

                    try:

                        await client.send_text(text)

                    except:

                        disconnected.append(client)

            for d in disconnected:

                clients.remove(d)

    except WebSocketDisconnect:

        if websocket in clients:

            clients.remove(websocket)

        print("切断")

if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )