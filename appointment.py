class Appointment:
  def __init__(self, date, time, numberOfSpots):
    self.date = date
    self.time = time
    self.numberOfSpots = numberOfSpots

  def to_dict(self):
    return {"date": self.date, "time": self.time, "numberOfSpots": self.numberOfSpots}

