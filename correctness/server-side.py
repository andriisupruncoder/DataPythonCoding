from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import asyncio

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the async request-reply service"})

@socketio.on('request')
async def handle_request(data):
    try:
        await asyncio.sleep(1)  # Simulate some processing time
        response = {"data": data, "processed": True}
        emit('reply', response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        emit('error', {"message": "An error occurred"})

if __name__ == '__main__':
    socketio.run(app, debug=True)