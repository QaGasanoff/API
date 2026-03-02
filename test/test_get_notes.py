class TestGetNotes:

    def test_get_all_notes_status_code(self, create_note, notes_api):
        response = notes_api.get_all_notes()
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    def test_get_all_notes_not_empty(self, create_note, notes_api):
        response = notes_api.get_all_notes()
        notes_list = response.json()
        assert len(notes_list) > 0, "Список заметок пуст"

    def test_get_note_by_title_found(self, create_note, notes_api):
        note = notes_api.get_note_by_title("Тестер")
        assert note is not None, "Заметка с title 'Тестер' не найдена"
        assert note["title"] == "Тестер", f"Неверный title: {note['title']}"

    def test_get_note_by_title_has_id(self, create_note, notes_api):
        notes_api.get_note_by_title("Тестер")
        assert notes_api.note_id != "", "note_id не установлен после поиска"

    def test_get_note_by_title_not_found(self, create_note, notes_api):
        note = notes_api.get_note_by_title("НесуществующийТитул")
        assert note is None, "Должен вернуть None для несуществующей заметки"
