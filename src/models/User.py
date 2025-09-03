from models.Credentials import Credentials
from models.PersonalData import PersonalData

class User:
    def __init__(self, credentials: Credentials, personal_data: PersonalData):
        self.credentials = credentials
        self.personal_data = personal_data