from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import socket
from io import BytesIO
import qrcode
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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