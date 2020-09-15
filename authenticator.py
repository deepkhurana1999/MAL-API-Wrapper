from session import Session
from client import Client
import secrets

class Authenticator(Session,Client):

	def __init__(self, credentials: dict):
		self._client_details['id'] = credentials['client_id']
		self._client_details['key'] = credentials['client_secret']
		
	
	def __PKCE_settor(self):
		token = secrets.token_urlsafe(100)
		self._client_details['code_verifier'] = token[:128]
		self._client_details['code_challenge'] = token[:128]

	def __authorization(self) -> str:
		url = 'https://myanimelist.net/v1/oauth2/authorize?'
		params = {
			'response_type':'code',
			'client_id': self._client_details['id'],
			'state':'RequestID',
			'code_challenge': self._client_details['code_challenge']
			}
		for key, value in params.items():
			temp = key+'='+value if (key=='response_type') else '&'+key+'='+value
			url = url + temp
		return url
	
	def __access_token(self, auth_url: str):
		url = 'https://myanimelist.net/v1/oauth2/token'
		code = auth_url[auth_url.index('=')+1:auth_url.index('&')]
		data = {
			'client_id': self._client_details['id'],
			'client_secret': self._client_details['key'],
			'grant_type': 'authorization_code',
			'code': code,
			'code_verifier': self._client_details['code_verifier']
			}
		response = self._session.post(url,data=data)
		self._client_details['tokenRefresh'] = response.json()
	
	def _refresh_token(self):
		url = 'https://myanimelist.net/v1/oauth2/token'
		data = {
			'client_id': self._client_details['id'],
			'client_secret': self._client_details['key'],
			'grant_type': 'refresh_token',
			'refresh_token': self._client_details['tokenRefresh']['refresh_token']
			}
		response = self._session.post(url,data=data)
		self._client_details['tokenRefresh'] = response.json()
	
	def start_session(self):
		self.__PKCE_settor()
		print('Visit the provided url for validation: ', self.__authorization())
		authUrl = input('Enter the generated url: ')
		self.__access_token(authUrl)