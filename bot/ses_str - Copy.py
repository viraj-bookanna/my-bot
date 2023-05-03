import telethon,os,urllib
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

api_id = input('TG_API_ID: ')
api_hash = input('TG_API_HASH: ')

#+16195918666
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())