from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import socket
from io import BytesIO
import qrcode
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- GESTORE CONNESSIONI (Il "Postino") ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                pass

manager = ConnectionManager()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def generate_image(data: str):
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")

@app.get("/connect-qr")
def connect_client():
    ip = get_local_ip()
    port = 8000
    
    url = f"http://{ip}:{port}/static/chat.html"
    
    print(f"QR generato per: {url}")
    return generate_image(url)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            print(f"Messaggio ricevuto: {data}")
            await manager.broadcast(data)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Un client si è disconnesso")