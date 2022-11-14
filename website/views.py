from flask import Blueprint, render_template, request, flash, jsonify
from timefetcher import TimeFetcher

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    fetcher = TimeFetcher()
    availableSpots = fetcher.getAvailableTimeSlots()
    availableSpots = availableSpots.replace("\n", " <br> ")

    return render_template("home.html", logs = availableSpots)
