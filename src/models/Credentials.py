from models.Password import Password

class Credentials:
    def __init__(self, email: str, password: Password):
        self.email = email
        self.password = password