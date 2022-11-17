from flask import Blueprint, render_template, request, flash, jsonify, Response, current_app
from timefetcher import TimeFetcher
from flask_socketio import emit
from asyncio import sleep
# from flask_socketio import SocketIO
from . import socketio

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    fetcher = TimeFetcher()
    availableSpots = []
    # availableSpots = fetcher.getAvailableTimeSlots()

    return render_template("home.html", appointments = availableSpots)

@views.route('/load_appointments/<socketId>', methods=['POST'])
async def load_appointments(socketId):

    for x in range(1,6):
        socketio.emit("update progress", x*20, to=socketId)
        await sleep(1)

    return Response(status=204)

