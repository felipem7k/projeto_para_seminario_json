from models.Birth import Birth
import re

class PersonalData:
    def __init__(self, name: str, birth: Birth):
        if not self.validade_name(name):
            raise Exception()

        self.name = name
        self.birth = birth

    def validade_name(self, name: str) -> bool:
        if not re.match("^[a-zA-ZÀ-ú\s-]{2,}$", name):
            print("🔴 Nome inválido.")
            return False

        return True