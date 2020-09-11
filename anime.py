from session import Session
from client import Client

class Anime(Session,Client):
    
    __header = {}

    def __init__(self):
        self.__header['Authorization'] = 'Bearer {}'.format(self._get_access_key())
    
    def get_anime_details(self,id, fields = None):
        params = {
            'fields': fields
        }
        self._get_access_key()
        url = 'https://api.myanimelist.net/v2/anime/{}'.format(id)
        return self._session.get(url,params=params,headers=self.__header)
    
    def get_anime_ranking(self,ranking_type,limit=None,offset=None,fields=None):
        params = {
            'ranking_type': ranking_type,
            'limit': limit,
            'offset': offset,
            'fields':fields
        }
        url = 'https://api.myanimelist.net/v2/anime/ranking'
        return self._session.get(url,params=params,headers=self.__header)
    
    def get_seasonal_anime(self,year,season,sort=None,limit=None,offset=None,fields=None):
        params = {
            'sort': sort,
            'limit': limit,
            'offset': offset,
            'fields': fields
        }
        url = 'https://api.myanimelist.net/v2/anime/season/{}/{}'.format(year,season)
        return self._session.get(url,params,headers=self.__header)
    
    def get_suggested_anime(self,limit=None,offset=None,fields=None):
        params = {
            'limit': limit,
            'offset': offset,
            'fields': fields
        }
        url = 'https://api.myanimelist.net/v2/anime/suggestions'
        return self._session.get(url,params,headers=self.__header)
