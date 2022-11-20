import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date
from typing import List
from flask_socketio import SocketIO

from appointment import Appointment

class TimeFetcher:
    def __init__(self):
        self._dateShift = 7

    def dateToStr(self, date: datetime) -> str:
        return date.strftime('%Y-%m-%d')

    def getAvailableTimeSlots(self, socketio: SocketIO, socketId: str) -> list[Appointment]:

        today = datetime.today()
        tomorrow = today + timedelta(days=self._dateShift)

        datesToFetch = []

        for i in range(self._dateShift):
            datesToFetch.append(self.dateToStr(today + timedelta(days=i)))

        availableAppointments = []

        query = {'action':'availableTimes', 'showSelect':'0', 'fulldate':'1', 'owner':'18896876'}

        numberOfDates = len(datesToFetch)
        currentDate = 1

        for date in datesToFetch:
            data = {'type':'15360506', 'calendar':'3581411', 'date': date, 'ignoreAppointment':''}
            response = requests.post('https://sensea.as.me/schedule.php', params=query, data=data)

            # parse the HTML
            soup = BeautifulSoup(response.text, "html.parser")

            times = soup.find_all("input", class_="time-selection")
            for dataPoint in times:
                date = dataPoint['data-readable-date']
                time = dataPoint['value'].split(" ").pop()
                spotsAvailable = dataPoint['data-available']
                appointment = Appointment(date=date, time=time, numberOfSpots=spotsAvailable)
                availableAppointments.append(appointment)
            if (socketio):
                socketio.emit("update progress", (currentDate / numberOfDates) * 100, to=socketId)
            currentDate += 1

        output = ""

        for apt in availableAppointments:
            output += "" + apt.date + " " + apt.time + " " + apt.numberOfSpots + "\n"
        
        print(output)
        return availableAppointments
