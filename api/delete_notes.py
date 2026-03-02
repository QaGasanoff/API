from api.base_api import BaseApi
import requests


class DeleteNotes(BaseApi):
    def __init__(self, token):
        self.token = token

    def delete_notes(self):
        headers = {**self.HEADERS, "Authorization": f"Bearer {self.token}"}
        delete_notes = requests.delete(f"{self.ENDPOINT_NOTES}/{self.note_id}", headers=headers)
        return delete_notes
