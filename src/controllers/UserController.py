from repository.UserRepository import UserRepository
from models.Birth import Birth
from models.Credentials import Credentials

class UserController:
    def __init__(self):
        self.users = []

    def account_creation(self):
        email = input("E-mail: ")
        password = input("Senha: ")

        name = input("Nome de usuário: ")
        birth_date = input("Data de nascimento (dd/mm/aaaa): ")

        if not email or not password or not Credentials.validate_password(password) or not name or not birth_date:
            return None

        try:
            user_repository = UserRepository()

            birth = Birth(birth_date)

            return user_repository.create_user(email, password, name, birth)
        except:
            return None
        
    def login(self):
        email = input("E-mail: ")
        password = input("Senha: ")

        if not email or not password:
            return None

        user_repository = UserRepository()
        user = user_repository.get_user_by_email(email)

        if user is None or not Credentials.password_equals(user.credentials.password, password):
            return None
        
        return user