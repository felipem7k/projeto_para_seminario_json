import re
import hashlib

class Credentials:
    def __init__(self, email: str, password: str):
        if not self.validate_mail(email):
            raise Exception()

        self.email = email
        self.password = password

    @staticmethod
    def password_hash(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    @staticmethod
    def password_equals(target_password: str, password: str) -> bool:
        return Credentials.password_hash(password) == target_password
    
    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) < 5:
            print("🔴 A senha deve conter no mínimo 5 caracteres.")
            return False
        return True

    def validate_mail(self, email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            return True
        else:
            print("🔴 E-mail inválido.")
            return False