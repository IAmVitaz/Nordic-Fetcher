from flask import Flask, render_template
from timefetcher import TimeFetcher
from datetime import datetime, timedelta, date\

app = Flask(__name__)

@app.route("/")
def index():

    fetcher = TimeFetcher()
    availableSpots = fetcher.getAvailableTimeSlots()
    availableSpots = availableSpots.replace("\n", " <br> ")

    timestamp = datetime.today().strftime('%d-%b %H:%M:%S')

    # Render HTML with count variable
    return render_template("index.html", logs = availableSpots, timestamp = timestamp)

if __name__ == "__main__":
    app.run()
