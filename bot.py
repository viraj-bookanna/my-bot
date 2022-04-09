import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import asyncio
from telethon import TelegramClient, events

api_id = "8832090"
api_hash = "fdf52a23e014c0d7f3d1c7768eaf552a"
sess = "1AZWarzwBuytLYscrmRrtnQMO6IZUvW94NkYSZVsxuDz4AbbMViE6WMW7zC_3_D3-3kHX0BkVCOxWDrxYKdquxwMDXDJcSGR7wCQCbaUo9_DPRFckSbzMLB9ncbIaSv_3vOLgrXAEnoBbtx8IOpgteEIJaPtPbqCfL_Paqi0zDdEHFvpCuE9VBQHtajzotOj99wsy5qbPB8-r6IGvzz0BATQE5016WCzdb78bEqYEkpti1EF578dWAqSg_Et_k1rQjYnBbka5YYOHH4lCGwCa-Nb-CW0xxwENSHDYyhriKBguItPjOiQKhG4U5F94Kan9IevDeepcKtpyrZuhq0abcXldmj5e1d0="

async def main():
   async with TelegramClient(StringSession(sess), api_id, api_hash) as client:
      await client.send_message('me', 'Hello, myself!')
      print(await client.download_profile_photo('me'))

      @client.on(events.NewMessage(pattern='(?i).*Hello'))
      async def handler(event):
         await event.reply('Hey!')

      await client.run_until_disconnected()

asyncio.run(main())