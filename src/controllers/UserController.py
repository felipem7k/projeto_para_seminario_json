from models.Validator import Validator
from repository.UserRepository import UserRepository
from models.Birth import Birth
from models.Password import Password

class UserController:
    def __init__(self):
        self.users = []

    def account_creation(self):
        email_input = input("E-mail: ")
        password_input = input("Senha: ")

        name = input("Nome de usuário: ")
        birth_input = input("Data de nascimento (dd/mm/aaaa): ")

        if not Validator.mail(email_input):
            print("🔴 E-mail inválido.")
            return None

        if not Validator.password(password_input):
            print("🔴 A senha deve conter no mínimo 5 caracteres.")
            return None

        if not name:
            print("🔴 Nome inválido")
            return None

        if not Validator.date(birth_input):
            print("🔴 Data de nascimento inválida. Siga o formato (dd/mm/aaaa)")
            return None

        return UserRepository().create_user(email_input, password_input, name, birth_input)
        
    def login(self):
        email = input("E-mail: ")
        password_input = input("Senha: ")

        if not email or not password_input:
            return None

        user_repository = UserRepository()
        user = user_repository.get_user_by_email(email)

        if user is None or not user.credentials.password.equals(password_input):
            return None
        
        return user