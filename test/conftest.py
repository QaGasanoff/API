import pytest
import uuid

from api.create_user import CreateUser
from api.auth_user import AuthUser
from api.create_notes import CreateNotes
from api.get_notes import GetNotes
from api.delete_notes import DeleteNotes


@pytest.fixture(scope="session")
def registered_user():
    email = f"test_{uuid.uuid4().hex[:8]}@mail.com"
    username = f"User_{uuid.uuid4().hex[:8]}"
    user_api = CreateUser()
    response = user_api.register_user(email, "123456", username)
    return response, email


@pytest.fixture(scope="session")
def auth_token(registered_user):
    response, email = registered_user  # распаковываем
    auth_api = AuthUser()
    auth_api.login_user(email, "123456")
    return auth_api.get_token()


@pytest.fixture()
def create_note(auth_token):
    api = CreateNotes(auth_token)
    response = api.add_notes("Обучение", "Тестер")
    return response


@pytest.fixture()
def notes_api(auth_token):
    return GetNotes(auth_token)


@pytest.fixture()
def delete_api(auth_token):
    return DeleteNotes(auth_token)
