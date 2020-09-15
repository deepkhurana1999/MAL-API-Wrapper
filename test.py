from interface import Interface

testObj = Interface('164eb4bdbc8bd15ad2bf122201981b9c','1dc3ceaba766c8c6b815c24606becbae1c87f4f876140c2799aba9921b73e243')
testObj.start_session()
print(testObj.get_anime_details(32281).json())