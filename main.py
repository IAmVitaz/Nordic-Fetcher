import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date

dateShift = 10

def dateToStr(date: datetime) -> str:
    return date.strftime('%Y-%m-%d')

today = datetime.today()
tomorrow = today + timedelta(days=dateShift)

datesToFetch = []

for i in range(dateShift):
    datesToFetch.append(dateToStr(today + timedelta(days=i+1)))

availableTimes = []

query = {'action':'availableTimes', 'showSelect':'0', 'fulldate':'1', 'owner':'18896876'}


for date in datesToFetch:
    data = {'type':'15360506', 'calendar':'3581411', 'date': date, 'ignoreAppointment':''}
    response = requests.post('https://sensea.as.me/schedule.php', params=query, data=data)

    # parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")


    times = soup.find_all("input", class_="time-selection")
    for time in times:
        availableTimes.append(time['value'])
        print(time['value'])




print(availableTimes)