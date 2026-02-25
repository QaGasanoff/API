from base_api import BaseApi

import requests


class GetNotes(BaseApi):
    def __init__(self, token):
        self.token = token

    def get_all_notes(self):
        headers = {**self.HEADERS, "Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{self.ENDPOINT_NOTES}", headers=headers)
        return response

    def get_note_by_title(self, title):
        response = self.get_all_notes()
        for note in response.json():
            if note["title"] == title:
                self.note_id = note["id"]
                return note
        return None
