from api.create_notes import CreateNotes


class TestCreateNote:

    def test_create_note_status_code(self, auth_token):
        api = CreateNotes(auth_token)
        response = api.add_notes("Тестовый контент", "Тестовый заголовок")
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

    def test_create_note_success_message(self, auth_token):
        api = CreateNotes(auth_token)
        response = api.add_notes("Контент", "Заголовок")
        response_json = response.json()
        assert "message" in response_json, "Ключ 'message' отсутствует в ответе"
        assert response_json["message"] == "Заметка создана!", f"Неверное сообщение: {response_json['message']}"
