import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date

from appointment import Appointment

dateShift = 10

def dateToStr(date: datetime) -> str:
    return date.strftime('%Y-%m-%d')

today = datetime.today()
tomorrow = today + timedelta(days=dateShift)

datesToFetch = []

for i in range(dateShift):
    datesToFetch.append(dateToStr(today + timedelta(days=i+1)))

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


for apt in availableAppointments:
    aptString = "" + apt.date + " " + apt.time + " " + apt.numberOfSpots
    print(aptString)
