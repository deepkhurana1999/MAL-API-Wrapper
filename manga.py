from session import Session
from client import Client

class Manga(Session,Client):

    def __header(self):
        return {'Authorization': 'Bearer {}'.format(self._client_details['tokenRefresh']['access_token'])}
    
    def get_manga_details(self,id, fields = None):
        params = {
            'fields': fields
        }
        url = 'https://api.myanimelist.net/v2/manga/{}'.format(id)
        return self._session.get(url,params=params,headers=self.__header())
    
    def get_manga_ranking(self,ranking_type,limit=None,offset=None,fields=None):
        params = {
            'ranking_type': ranking_type,
            'limit': limit,
            'offset': offset,
            'fields':fields
        }
        url = 'https://api.myanimelist.net/v2/manga/ranking'
        return self._session.get(url,params=params,headers=self.__header())
