from inspect import _void
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

    def save(self, user_list: list[list]) -> _void:
        with open(self.JSONPATH, "w") as json_file:
            json.dump(user_list, json_file, indent=3)

    def create_user(self, email: str, password: str, name: str, birth: Birth):
        user_list = self.users()

        if self.get_user_by_email(email) is not None:
            print("🔴 E-mail em uso.")
            return None

        user = User(
            Credentials(email, Credentials.password_hash(password)),
            PersonalData(name, birth)
        )

        user_list.append({
            "email": user.credentials.email,
            "password": user.credentials.password,
            "name": user.personal_data.name,
            "birth": user.personal_data.birth.tostr()
        })
        
        self.save(user_list)

        return user
    
    def get_user_by_email(self, email) -> User:
        user_list = self.users()
        for user_data in user_list:
            if user_data["email"] == email:
                return User(
                    Credentials(user_data["email"], user_data["password"]),
                    PersonalData(user_data["name"], Birth(user_data["birth"]))
                )
        return None