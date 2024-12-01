# Real-Time Chat Application Using Flask and Socket.IO

## Project Description

This project is a real-time chat application built as part of the assessment for **SPE 2404: Distributed & Network Programming**. It demonstrates key concepts of distributed systems, including client-server architecture, multi-threading, and message passing, implemented using Flask and Flask-SocketIO.

The application enables multiple users to communicate in real time by joining or creating chat rooms. It incorporates secure session management and scalable message handling with a memory-based storage system.

## Features

- **Real-Time Messaging:** Users can send and receive messages instantly in dedicated chat rooms.
- **Room Management:** Create unique rooms or join existing ones using a code.
- **Message History:** Chat history for each room is maintained and displayed upon joining.
- **Session Management:** User and room information are managed using Flask sessions.
- **Scalable Design:** Multi-user support using WebSocket communication via Flask-SocketIO.

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**  
   Use Python 3.7+ and a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Application:**  
   Start the Flask development server:

   ```bash
   flask run
   ```

4. **Access the Application:**  
   Open a browser and navigate to `http://127.0.0.1:5000`.

## Technologies Used

### Backend

- Flask
- Flask-SocketIO

### Frontend

- HTML, CSS
- JavaScript

### Development Tools

- Python 3.7+
- WebSockets (via Socket.IO)

## Key Concepts Demonstrated

1. **Client-Server Architecture:** Separation of user-facing interface and backend processing.
2. **Multi-threading:** Flask-SocketIO allows efficient handling of multiple WebSocket connections.
3. **Message Passing:** Real-time broadcasting and receiving of messages between users.

## Acknowledgments

Special thanks to the _SPE 2404 Distributed & Network Programming_ course instructors for providing this challenging and enriching project opportunity.
