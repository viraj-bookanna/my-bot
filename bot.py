from telethon import TelegramClient, events
from telethon.sessions import StringSession
import msghandler

api_id = "8832090"
api_hash = "fdf52a23e014c0d7f3d1c7768eaf552a"
sess = "1AZWarzwBuytLYscrmRrtnQMO6IZUvW94NkYSZVsxuDz4AbbMViE6WMW7zC_3_D3-3kHX0BkVCOxWDrxYKdquxwMDXDJcSGR7wCQCbaUo9_DPRFckSbzMLB9ncbIaSv_3vOLgrXAEnoBbtx8IOpgteEIJaPtPbqCfL_Paqi0zDdEHFvpCuE9VBQHtajzotOj99wsy5qbPB8-r6IGvzz0BATQE5016WCzdb78bEqYEkpti1EF578dWAqSg_Et_k1rQjYnBbka5YYOHH4lCGwCa-Nb-CW0xxwENSHDYyhriKBguItPjOiQKhG4U5F94Kan9IevDeepcKtpyrZuhq0abcXldmj5e1d0="
#client = TelegramClient('session', api_id, api_hash)
client = TelegramClient(StringSession(sess), api_id, api_hash)

# with TelegramClient(StringSession(), api_id, api_hash) as ultroid:
    # print(ultroid.session.save())

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    await msghandler.outgoing_msg_handler(event)
@client.on(events.NewMessage(pattern=r'(?i).*(heck|fuck(er|ing)?|sexy?|ponnaya)'))
async def handler(event):
    await event.delete()
    await event.respond("what's the problem bro?")

client.start()
client.run_until_disconnected()