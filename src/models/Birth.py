from datetime import datetime
import math

class Birth:
    def __init__(self, birth_date: str):
        birth_at: datetime|None = self.valid_date(birth_date)
        if birth_at is None:
            raise Exception("Data inválida")

        self.date = birth_at

    def valid_date(self, data: str) -> datetime|None:
        try:
            date_valid = datetime.strptime(data, '%d/%m/%Y')
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