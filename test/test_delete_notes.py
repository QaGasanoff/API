class TestDeleteNote:

    def test_delete_note_status_code(self, create_note, notes_api, delete_api):
        notes_api.get_note_by_title("Тестер")
        delete_api.note_id = notes_api.note_id
        response = delete_api.delete_notes()
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    def test_note_not_found_after_delete(self, create_note, notes_api, delete_api):
        notes_api.get_note_by_title("Тестер")
        delete_api.note_id = notes_api.note_id
        delete_api.delete_notes()

        note = notes_api.get_note_by_title("Тестер")
        assert note is None, "Заметка не удалена — всё ещё найдена по title"
