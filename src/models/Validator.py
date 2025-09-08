from datetime import datetime
import re

class Validator:
    @staticmethod
    def password(password: str) -> bool:
        if len(password) < 5:
            return False
        return True
    
    @staticmethod
    def date(data: str) -> bool:
        try:
            date_valid = datetime.strptime(data, '%d/%m/%Y')
            today = datetime.today()
            if date_valid.year > today.year:
                raise ValueError()
            return True
        except ValueError:
            return False
        
    @staticmethod
    def mail(email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            return True
        else:
            return False