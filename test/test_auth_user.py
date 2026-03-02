from api.auth_user import AuthUser


class TestAuthUser:

    def test_login_status_code(self, auth_token):
        auth_api = AuthUser()
        response = auth_api.login_user("ramil_test@ya.ru", "123456")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    def test_login_returns_token(self, auth_token):
        assert auth_token is not None, "Токен не получен"
        assert len(auth_token) > 0, "Токен пустой"
