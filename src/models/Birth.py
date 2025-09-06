from datetime import datetime
import math

class Birth:
    def __init__(self, birth_date: str):
        self.date = datetime.strptime(birth_date, '%d/%m/%Y')

    def age(self):
        today = datetime.today()
        diff = today - self.date
        return math.floor(diff.days / 365)

    def tostr(self):
        return self.date.strftime('%d/%m/%Y')