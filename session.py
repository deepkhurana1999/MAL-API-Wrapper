import requests

class Session:
    def __init__(self):
        self._session = requests.Session()
    