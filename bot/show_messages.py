import asyncio,logging,sys
from telethon import TelegramClient, events
from telethon.sessions import StringSession

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

API_ID = 5
API_HASH = "1c5c96d5edd401b1ed40db3fb5633e2d"
session_string = input("Enter StringSession: ")

client = TelegramClient(StringSession(session_string), API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    try:
        if not event.message.peer_id.user_id == 777000:
            return
    except:
        return
    print(event.message.message)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        print("session expired")
        sys.exit()
client.loop.run_until_complete(main())
client.run_until_disconnected()