from base_api import BaseApi
import requests


class CreateUser(BaseApi):

    def register_user(self, email, password, username):
        data = {"email": email, "password": password, "username": username}
        response = requests.post(f"{self.ENDPOINT_REG}", json=data, headers=self.HEADERS)
        return response
