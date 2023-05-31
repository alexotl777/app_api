"""
MIEM
"""

import json
import requests as rq

def get_info_miem():
    TOKEN_MIEM = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NzkwNzAyNTEsImV4cCI6MTY3OTE1NjY1MSwidXNlcm5hbWUiOiLQntGC0LvQuNCy0LDQvSDQlNC80LjRgtGA0LjQuSDQkNC70LXQutGB0LXQtdCy0LjRhyIsImVtYWlsIjoiZGFvdGxpdmFuQGVkdS5oc2UucnUiLCJzdGFmZiI6ZmFsc2UsInN0dWRlbnQiOnRydWV9.PFtKF0Ns6vOCaVXTf4-3r4oByTcuFNyjIvOXTEmJR9_YPFRnyPjb-uQks1HFHZ9jv7bk2cgwL0bBwesSzUTQ9X8k2UzE9bjg2NJkxfi4F2atB-tpgz7P7UBMrKIvEy1v4Wxmgl2HAFDPUeSnI5fIDcLL0FZwiJTwElAdJR722r7OrYVXMqjEIcveqQqhhF20j1sr31pmEiJ8-ofLwDMukVHwAvwEeia3pSLiB62fm0nRthj5l53tHWoD01cGp5evHyVHETzD3cgMTiLT6TN2C7C6Wh0evI68Io_iXLu7tY-rMf7YZvJem1cJvvkHRM570PgJ-KYTczBBBWrwgh_onWR8_H3o5izxjAyefiskyRyn25k0nXHm6v1bSxzcwpifExApHobdpBKcBsxixS0aYhhMgAIss2WOw8hI_vl9pFZjrbPBcilf9hLvpYcHFH9pLGh472gOHrahiaqoEPmC9EZL8RBov8HbcQPlZDvEJy9ou1vWyHB4FFAElZMTDSrsKWYd9W74zQQCGQXTlVPVTX1ch8Yn8sspal3Dt3dVI5WyJUbtdNfzKha6QrhqE0hXSNhMYP6oTY27QLEq9VEOZ3AxjmC9nESOHzhH-jCbZwDV5OQHtrI_iJKJzvjpBw0ddf79bNKoDVUzO8fwm8fi9MCPUyfnEyZ4FGAof82Mn6c"
    URL_TO_MIEM = 'https://cabinet.miem.hse.ru/api/student_profile'

    req_miem = rq.get(
        URL_TO_MIEM, 
        headers = {
        "x-auth-token": TOKEN_MIEM
        }
        )
    data_miem = req_miem.json()
    with open("miem.json", "w+", encoding='utf-8') as f:
        json.dump(data_miem, f, ensure_ascii=False, indent=4)
