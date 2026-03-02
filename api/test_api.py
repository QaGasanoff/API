from api.create_user import CreateUser
from api.auth_user import AuthUser
from api.create_notes import CreateNotes
from api.get_notes import GetNotes
from api.delete_notes import DeleteNotes

# --- Регистрация ---
newuser = CreateUser()
user = newuser.register_user("testemi7771@ya.ru", "123456", "Emil117")
print(f"Регистрация — статус: {user.status_code}")
print(f"Регистрация — ответ: {user.json()}")

# --- Логин ---
loginuser = AuthUser()
login_response = loginuser.login_user("testemi7771@ya.ru", "123456")
_token = loginuser.get_token()
print(f"Логин — статус: {login_response.status_code}")
print(f"Логин — токен: {_token}")

# --- Создание заметки ---
api = CreateNotes(_token)
add_notes1 = api.add_notes("Обучение", "Тестер")
print(f"Создание заметки — статус: {add_notes1.status_code}")
print(f"Создание заметки — ответ: {add_notes1.json()}")

# --- Получение заметок ---
notes = GetNotes(_token)
all_notes = notes.get_all_notes()
print(f"Все заметки — статус: {all_notes.status_code}")
print(f"Все заметки — ответ: {all_notes.json()}")

# --- Поиск заметки по title ---
note = notes.get_note_by_title("Тестер")
print(f"Найденная заметка: {note}")
print(f"ID заметки: {notes.note_id}")

# --- Удаление заметки ---
delete_api = DeleteNotes(_token)
delete_api.note_id = notes.note_id
get_result = delete_api.delete_notes()
print(f"Удаление — статус: {get_result.status_code}")
print(f"Удаление — ответ: {get_result.text}")
