from create_user import CreateUser
from auth_user import AuthUser
from notes_api import CreateNotes
from get_notes import GetNotes
from delete_notes import DeleteNotes

# --- Регистрация ---
newuser = CreateUser()
user = newuser.register_user("ramil706@ya.ru", "123456", "Ramil106")
print(f"Регистрация — статус: {user.status_code}")
print(f"Регистрация — ответ: {user.json()}")

# --- Логин ---
loginuser = AuthUser()
login_response = loginuser.login_user("ramil706@ya.ru", "123456")
_token = login_response.json()["token"]
print(f"Логин — статус: {login_response.status_code}")
print(f"Логин — токен: {_token}")

# --- Создание заметки ---
api = CreateNotes(_token)
add_notes1 = api.add_notes("Обучение", "Тестер")
print(f"Создание заметки — статус: {add_notes1.status_code}")
print(f"Создание заметки — ответ: {add_notes1.json()}")

# --- Получение заметок ---
notes = GetNotes(_token)
get_response = notes.get_notes()
print(f"Получение заметок — статус: {get_response.status_code}")
print(f"Получение заметок — ответ: {get_response.json()}")

# --- Удаление заметки ---
delete_api = DeleteNotes(_token)
delete_api.note_id = notes.note_id
get_result = delete_api.delete_notes()
print(f"Получение результата удаления: {get_result.status_code}")
print(f"Получение ответа процесса удаления: {get_result.text}")
