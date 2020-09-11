class Client:
	_client_details = {}
	
	def _get_access_key(self) -> str:
		return self._client_details['tokenRefresh']['access_token']