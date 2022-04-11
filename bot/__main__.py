from telethon import TelegramClient, events
from telethon.sessions import StringSession
import msghandler,os

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
session_str = os.getenv('TG_STR_SESSION')

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    await msghandler.outgoing_msg_handler(event)
@client.on(events.NewMessage(pattern=r'(?i).*(heck|fuck(er|ing)?|sexy?|ponnaya)'))
async def handler(event):
    await event.delete()
    await event.respond("what's the problem bro?")

client.start()
client.run_until_disconnected()