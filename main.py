from requests import session
import vk_api

session = vk_api.VkApi(token='4241c8084241c8084241c808e44150f6ca442414241c808211dea98b9fb21e3557ebf6c')
vk1 = session.get_api()

def get_user_friends(user_id):
    friends = session.method("friends.get", {"user_id": user_id})
    print(friends)
    
get_user_friends(96318884)