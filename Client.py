import requests
import secrets

class Client:

	__client_details = {}
	
	def __init__(self, credentials: dict):
		self.__client_details['id'] = credentials['client_id']
		self.__client_details['key'] = credentials['client_secret']
		self.__client_details['session'] = requests.Session()
	
	def __PKCE_settor(self):
		token = secrets.token_urlsafe(100)
		self.__client_details['code_verifier'] = token[:128]
		self.__client_details['code_challenge'] = token[:128]

	def __authorization(self) -> str:
		url = 'https://myanimelist.net/v1/oauth2/authorize'
		params = {
			'response_type':'code',
			'client_id': self.__client_details['id'],
			'state':'RequestID',
			'code_challenge': self.__client_details['code_challenge']
			}
		return self.__client_details['session'].get(url,params=params).url
	
	def __access_token(self, auth_url: str):
		url = 'https://myanimelist.net/v1/oauth2/token'
		code = auth_url[auth_url.index('=')-1:auth_url.index('&')]
		data = {
			'client_id': self.__client_details['id'],
			'client_secret': self.__client_details['key'],
			'grant_type': 'authorization_code',
			'code': code,
			'code_verifier': self.__client_details['code_verifier']
			}
		response = self.__client_details['session'].post(url,data=data)
		self.__client_details['tokenRefresh'] = response.json()
	
	def __refresh_token(self):
		url = 'https://myanimelist.net/v1/oauth2/token'
		data = {
			'client_id': self.__client_details['id'],
			'client_secret': self.__client_details['key'],
			'grant_type': 'refresh_token',
			'refresh_token': self.__client_details['tokenRefresh']['refresh_token']
			}
		response = self.__client_details['session'].post(url,data=data)
		self.__client_details['tokenRefresh'] = response.json()
	
	def _get_access_key(self) -> str:
		return self.__client_details['tokenRefresh']['access_token']