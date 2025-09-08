from models.Password import Password
from models.Credentials import Credentials
from models.PersonalData import PersonalData
from models.User import User
from models.Birth import Birth

import json
import os

class UserRepository:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSONPATH: str = os.path.join(BASE_DIR, '..', '..', 'json', 'users.json')

    def users(self) -> list[list]:
        user_list: list[list] = []
        with open(self.JSONPATH, "r") as json_file:
            user_list = json.load(json_file) or []
        return user_list

    def save(self, user_list: list[list]):
        with open(self.JSONPATH, "w") as json_file:
            json.dump(user_list, json_file, indent=3)

    def create_user(self, email: str, password_input: str, name: str, birth_input: str) -> User|None:
        user_list = self.users()

        if self.get_user_by_email(email) is not None:
            print("🔴 E-mail em uso.")
            return None

        user = User(
            Credentials(email, Password(Password.to_hash(password_input))),
            PersonalData(name, Birth(birth_input))
        )

        user_list.append({
            "email": user.credentials.email,
            "password": user.credentials.password.hash,
            "name": user.personal_data.name,
            "birth": user.personal_data.birth.tostr()
        })
        
        self.save(user_list)

        return user
    
    def get_user_by_email(self, email) -> User|None:
        user_list = self.users()
        for user_data in user_list:
            if user_data["email"] == email:
                return User(
                    Credentials(user_data["email"], Password(user_data["password"])),
                    PersonalData(user_data["name"], Birth(user_data["birth"]))
                )
        return None