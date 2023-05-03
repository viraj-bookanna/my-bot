from telethon import TelegramClient, events
from telethon.sessions import StringSession
import msghandler,os

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
session_str = '1AZWarzcBu5d1TU20DfIIbsSw7aLsbAsp-1o5GufEP94wqJ-3Y-JKjp2hvxFt6rItRN0tJYVl6aFIA1DHrPlsmi4H7jpPo25HLnOJtzv6-8RLl7AFkUp3kXLm9agT384RToTPe_a5qkLHQ2TjVzsTVL0B5ULdDDEzaDlKlIZFWK8ev60uwI2kCqde5avzmbSoCI8S99Vdywypnpmj0u77DC6CuRRlZu4p6_kWRljGGmhGr_J5Zfp2LmlXSG6nRHyuXgIqRWJXUcCSZPSNEYEFBTU5jwMf2bwjbsQBweIXFrPHhkH7g7DiX8v7YaHyXKK3ElZvaJ-jCmr6SDXtPtOD2718DWjDhmc='#os.getenv('TG_STR_SESSION')
#session_str = '1AZWarzkBuxHgyz1Pwl28Y-6z7tiXa2CHTvtERb4qAmfTOTfWY7faXePzrEho-sdnhuNl3ueC56P_rlYjclzk37kHFWwwSIpGKo6xxlq-zAbTKGZzdUOtafh2i_Yy_QFs7udeB2yg8FCR9lLiE3NnpFaKflEuaIgi_0RSDsLM1tYjFZBvaLKrn84NBb2-CZUrk5eJGa2KwYYTx7HuhKwH3UjYBX1vd0v9Ev1p5T5NZxzP5PpQuYJ8rqPJrwX5yjDO-Ez2-XVlocC5auWmRB2Ei7u6-_faSgeE9uBuDRZOPX8Ef3-jDrY8jZZ-K1Srl3JXbwhWSq1MhVLqM_Ok4vXf3IdkOJ_Uhy8='#os.getenv('TG_STR_SESSION')

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    await msghandler.outgoing_msg_handler(event)
@client.on(events.NewMessage(pattern=r'(?i).*(heck|fuck(er|ing)?|sexy?|ponnaya)'))
async def handler(event):
    await event.delete()
    await event.respond("what's the problem bro?")
@client.on(events.NewMessage(pattern='/id'))
async def handler(event):
    await event.reply("Current chat id: {}".format(event.chat.id))

client.start()
client.run_until_disconnected()