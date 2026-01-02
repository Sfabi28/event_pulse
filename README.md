# 💬 EventPulse - Live Q&A Wall

A **Real-Time** interaction platform for live events.
It allows the audience to send messages or questions from their smartphones directly to the stage's big screen, instantly and without installing any app.

![Status](https://img.shields.io/badge/Status-MVP-orange)
![Tech](https://img.shields.io/badge/Backend-FastAPI-green)
![Protocol](https://img.shields.io/badge/Protocol-WebSockets-blue)
![Mobile](https://img.shields.io/badge/UI-Responsive-purple)

## 🚀 How It Works

The system creates an instant "bridge" between the audience's devices and the speaker's screen using the local Wi-Fi network.

1.  **The Wall (Server):** The speaker's PC projects a dynamically generated **QR Code**.
2.  **Scan & Connect:** The attendee scans the QR code and is redirected to the chat web app (no login required).
3.  **Real-Time Action:** As soon as the attendee sends a message, it appears on the Wall in <100ms thanks to **WebSockets**.

## ✨ Key Features

* **⚡ WebSocket Communication:** Uses a persistent bidirectional channel instead of standard HTTP requests for near-zero latency.
* **🔍 Auto-IP Discovery:** The backend automatically detects the host machine's local IP address and generates the correct QR Code for mobile connection.
* **📱 Mobile First UI:** The sending interface is optimized for one-handed use on smartphones.
* **🎥 Wall Interface:** The projector interface features animations and high contrast for readability from a distance.

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI (Asynchronous framework).
* **Protocol:** WebSocket (Broadcast logic via custom Connection Manager).
* **Frontend:** HTML5, Vanilla JS (No heavy frameworks), Tailwind CSS.
* **Utils:** Python-QRCode (In-memory image streaming via byte buffers).

## 🤖 AI-Assisted Development

This project was developed using an **AI-First approach**, simulating a Senior/Junior pair programming workflow.

* **Role of AI:** Acted as a Technical Lead, providing architectural decisions (switching from HTTP to WebSockets), solving complex networking issues (local IP discovery logic), and guiding the UI design with Tailwind CSS.
* **Development Process:** The AI provided the roadmap and specific problem-solving strategies, while the implementation and assembly were carried out to ensure a deep understanding of the code.

## 🔌 Installation & Setup

Ensure your PC and smartphones are connected to the **same Wi-Fi network**.

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/event-pulse.git](https://github.com/YOUR_USERNAME/event-pulse.git)
    cd event-pulse
    ```

2.  **Setup the environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Start the Server (Public Mode)**
    It is crucial to use `0.0.0.0` to make the server visible on the local network.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## 🧪 How to Test It

1.  Open your PC browser at: `http://localhost:8000/static/wall.html`
2.  Scan the displayed **QR Code** with your smartphone.
3.  Type a message on your phone and hit **SEND**.
4.  Watch the message appear magically on your PC monitor!

## 📂 Project Structure

```text
event_pulse/
├── main.py            # Backend: WebSocket logic & IP Discovery
├── requirements.txt   # Python Dependencies
└── static/            # Frontend Files
    ├── wall.html      # Projector Page (Receiver)
    └── chat.html      # Smartphone Page (Transmitter)