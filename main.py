"""
ДЗ API
"""

import miem
import vk

miem.get_info_miem()
vk.get_info_vk()
exec(open("flask_server.py").read())

