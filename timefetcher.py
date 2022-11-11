import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date

from appointment import Appointment

class TimeFetcher:
    def __init__(self):
        self._dateShift = 10

    def dateToStr(self, date: datetime) -> str:
        return date.strftime('%Y-%m-%d')

    def getAvailableTimeSlots(self) -> str:

        today = datetime.today()
        tomorrow = today + timedelta(days=self._dateShift)

        datesToFetch = []

        for i in range(self._dateShift):
            datesToFetch.append(self.dateToStr(today + timedelta(days=i+1)))

        availableAppointments = []

        query = {'action':'availableTimes', 'showSelect':'0', 'fulldate':'1', 'owner':'18896876'}


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

        output = ""

        for apt in availableAppointments:
            output += "" + apt.date + " " + apt.time + " " + apt.numberOfSpots + "\n"
        
        print(output)
        return output
