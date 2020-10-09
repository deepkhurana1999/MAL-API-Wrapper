from interface import Interface

client_id = ''
client_key = ''
testObj = Interface(client_id: str, client_key: str)
testObj.start_session()
print(testObj.anime.get_anime_details(32281).json())
