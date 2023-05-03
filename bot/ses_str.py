import telethon,os,urllib,sys,asyncio
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from qrcode import QRCode

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')

client = TelegramClient(StringSession(), api_id, api_hash)

async def main():
    await client.connect()
    while True:
        qr_login = await client.qr_login()
        qr = QRCode()
        print(qr_login.url)
        qr.add_data(qr_login.url)
        qr.print_ascii()
        try:
            await qr_login.wait()
            break
        except telethon.errors.SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))
            break
        except asyncio.exceptions.TimeoutError:
            continue
        except Exception as e:
            print(repr(e))
            continue
    print(client.session.save())
try:
    client.loop.run_until_complete(main())
except KeyboardInterrupt:
    print('user exit')
    sys.exit()