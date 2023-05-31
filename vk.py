"""
VK
"""

import json
import requests as rq

def get_info_vk():
    TOKEN_VK = "eef55838eef55838eef5583812ede65987eeef5eef558388afe1ca5cf2c2f8b753ceefe"
    URL_TO_VK = 'https://api.vk.com/method/users.get'

    req_vk = rq.get(
        URL_TO_VK, params={
        "access_token": TOKEN_VK, 
        "user_ids": "hate_u_d1", 
        "v": 5.131
        }
        )
    data_vk = req_vk.json()
    with open("vk.json", "w+", encoding='utf-8') as f:
        json.dump(data_vk, f, ensure_ascii=False, indent=4)
