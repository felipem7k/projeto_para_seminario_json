from datetime import datetime
import math

class Birth:
    def __init__(self, birth_date: str):
        self.date = datetime.strptime(birth_date, '%d/%m/%Y')

    def valid_date(self, data: str) -> datetime|None:
        try:
            date_valid = datetime.strptime(data, '%d/%m/%Y')
            today = datetime.today()
            if date_valid.year > today.year:
                raise ValueError()
            return date_valid
        except ValueError:
            print("🔴 Data de nascimento inválida. Siga o formato (dd/mm/aaaa)")
            return None
        
    def age(self):
        today = datetime.today()
        diff = today - self.date
        return math.floor(diff.days / 365)

    def tostr(self):
        return self.date.strftime('%d/%m/%Y')