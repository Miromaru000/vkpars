from requests import session
from auth_data import token
import vk_api

session = vk_api.VkApi(token=token)
vk1 = session.get_api()

def get_user_friends(user_id, fields):
    friends = session.method("friends.get", {"user_id": user_id, "fields": fields})
    print(friends)
    
get_user_friends(189907725, "nickname")

#189907725
#2097884