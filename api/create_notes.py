from api.base_api import BaseApi

import requests


class CreateNotes(BaseApi):
    def __init__(self, token):
        self.token = token

    def add_notes(self, content, title):
        data = {"content": content, "title": title}
        headers = {**self.HEADERS, "Authorization": f"Bearer {self.token}"}
        response_notes = requests.post(f"{self.ENDPOINT_NOTES}", json=data, headers=headers)
        return response_notes
