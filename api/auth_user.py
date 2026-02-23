from base_api import BaseApi
import requests


class AuthUser(BaseApi):

    def login_user(self, email, password):
        data = {"email": email, "password": password}
        response = requests.post(f"{self.ENDPOINT_LOGIN}", json=data, headers=self.HEADERS)
        self.token = response.json()["token"]
        return response
