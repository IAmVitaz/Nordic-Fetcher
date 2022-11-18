from flask import Blueprint, render_template, request, flash, jsonify, Response, current_app
from timefetcher import TimeFetcher
from flask_socketio import emit
from asyncio import sleep
# from flask_socketio import SocketIO
from . import socketio
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/load_appointments/<socketId>', methods=['POST'])
async def load_appointments(socketId):

    fetcher = TimeFetcher()
    availableSpots = fetcher.getAvailableTimeSlots(socketio=socketio, socketId=socketId)
    json_string = [obj.to_dict() for obj in availableSpots]
    return json_string
