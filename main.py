from flask import Flask, make_response, request
from star import Star, ShootingStar
from edge import Edge
import json
from flask_socketio import SocketIO
import asyncio
from time import sleep
from threading import Thread

maxStars = 100
stars = [Star.generateRandomStar() for i in range(100)]

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=["http://127.0.0.1:3000", "http://localhost:3000", "https://master.d1w0j5t2vbp7ry.amplifyapp.com/"])

def generate_response(data, status_code=200):
    res = make_response(data)
    res.status = status_code
    res.headers['Access-Control-Allow-Origin'] = "https://master.d1w0j5t2vbp7ry.amplifyapp.com/"
    res.headers['Access-Control-Allow-Credentials'] = "true"
    return res

@app.route("/")
def hello_world():
    print("here")
    return "<p>Hello, World!</p>"

@app.route("/refresh")
def refresh():
    global stars
    stars = [Star.generateRandomStar() for i in range(100)]
    socketio.emit("stars", ", ".join([f"{star}" for star in stars]))
    return generate_response("OK", 200)

@app.route("/get/stars")
def get_stars():
    return generate_response(", ".join(stars))

@app.route("/get/sstar")
def get_sstar():
    socketio.emit("sstar", f"{ShootingStar.generateRandomSStar()}")
    return generate_response("OK")

@app.route("/add-edge", methods=["POST"])
def add_edge():
    data = json.loads(request.get_data(as_text=True))
    if "start" not in data or "end" not in data:
        return generate_response("Bad request", 400)
    edge = Edge(data["start"], data["end"])
    socketio.emit("edge", f"{edge}")
    return generate_response("OK", 200)

@app.route("/add-star", methods=["POST"])
def add_star():
    data = json.loads(request.get_data(as_text=True))
    if "x" not in data or "y" not in data:
        return generate_response("Bad request", 400)
    star = Star(data['x'], data['y'])
    socketio.emit("star", f"{star}")
    return generate_response("OK", 200)

@app.route("/health", methods=["GET"])
def health_check():
    return generate_response("OK")

def sstarLoop():
    while True:
        # print("sending star")
        socketio.emit("sstar", f"{ShootingStar.generateRandomSStar()}")
        sleep(1)

@socketio.on("lol")
def refresh(data):  
    pass
    # print('refreshed')
    # socketio.emit("refresh", "hi")

if __name__ == "__main__":
    # sStarLoopThread = Thread(target=sstarLoop)
    # sStarLoopThread.start()
    socketio.run(app, port=5000, debug=True)
    # sStarLoopThread.join()