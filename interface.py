from anime import Anime
from session import Session
from authenticator import Authenticator

class Interface(Authenticator,Anime):
    
    def __init__(self,client_id: str, client_secret: str):
        Authenticator.__init__(self,{'client_id':client_id,'client_secret':client_secret})
        Session.__init__(self)
    