from urllib import response
import requests

rec = requests.get('https://oauth.vk.com/access_token?client_id=51461826&client_secret=OQxRqwIiV2muJFJCXYCe&redirect_uri=http://127.0.0.1&code=13b67e52e0d225f55b')


rec = rec.json()

token = rec.get('access_token')




#def get_access_token(clinet_id, client_secret, redirect_uri, code):
  
#token = get_access_token(51461826,'OQxRqwIiV2muJFJCXYCe', 'http://127.0.0.1' ,input())   
   
#token = '012f6b0b012f6b0b012f6b0bcd023e55c90012f012f6b0b627238b663c0a75980e960d8'


#https://oauth.vk.com/authorize?client_id=51461826&display=page&redirect_uri=http://127.0.0.1