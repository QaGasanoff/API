class BaseApi:

    BASE_URL = "http://185.240.103.201:8000"
    note_id = ""
    ENDPOINT_LOGIN = f"{BASE_URL}/api/login"
    ENDPOINT_REG = f"{BASE_URL}/api/register"
    ENDPOINT_NOTES = f"{BASE_URL}/api/notes"
    ENDPOINT_DEL_NOTES = f"{BASE_URL}/api/notes{note_id}"
    HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
    token = ""
