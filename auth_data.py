import requests

rec = requests.get('https://oauth.vk.com/access_token?client_id=51461826&client_secret=OQxRqwIiV2muJFJCXYCe&redirect_uri=http://127.0.0.1&code=b6cba38a2bed6e0a3b')
rec = rec.json()

token = rec.get('access_token')



  
   
#token = '012f6b0b012f6b0b012f6b0bcd023e55c90012f012f6b0b627238b663c0a75980e960d8'


#https://oauth.vk.com/authorize?client_id=51461826&display=page&redirect_uri=http://127.0.0.1