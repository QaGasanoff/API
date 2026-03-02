class TestCreateUser:

    def test_register_status_code(self, registered_user):
        response, email = registered_user
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

    def test_register_success_message(self, registered_user):
        response, email = registered_user
        response_json = response.json()
        assert "message" in response_json, "Ключ 'message' отсутствует в ответе"
        assert response_json["message"] == "Успешная регистрация!", f"Неверное сообщение: {response_json['message']}"
