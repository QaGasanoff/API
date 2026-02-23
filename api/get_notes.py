from base_api import BaseApi

import requests


class GetNotes(BaseApi):
    def __init__(self, token):
        self.token = token

    def get_notes(self):
        headers = {**self.HEADERS, "Authorization": f"Bearer {self.token}"}
        response_notes = requests.get(f"{self.ENDPOINT_NOTES}", headers=headers)
        print(f"Получение заметки - запрос: {response_notes}")
        self.note_id = response_notes.json()[0]["id"]
        return response_notes
