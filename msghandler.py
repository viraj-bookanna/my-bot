import __main__,os,sys,time,datetime

async def outgoing_msg_handler(event):
    if event.raw_text.startswith('.'):
        await handle_command(event)

class Timer:
    def __init__(self, time_between=2):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

async def download_or_upload(event, msg):
    type_of = ""
    timer = Timer()

    async def progress_bar(current, total):
        if timer.can_send():
            await event.edit("{} {}%".format(type_of, round(current * 100 / total, 2)))

    if msg.media is not None:
        type_of = "download"
        await event.edit("downloading started")
        path = await event.client.download_media(message=msg, progress_callback=progress_bar)
        await event.edit("Finished downloading "+path)

    else:
        type_of = "upload"
        await event.edit("uploading started")
        with open(file_to_upload, "rb") as out:
            res = await upload_file(client, out, progress_callback=progress_bar)
            # result is InputFile()
            # you can add more data to it
            attributes, mime_type = utils.get_attributes(
                file_to_upload,
            )
            media = types.InputMediaUploadedDocument(
                file=res,
                mime_type=mime_type,
                attributes=attributes,
                # not needed for most files, thumb=thumb,
                force_file=False
            )
            await msg.edit("Finished uploading")
            await msg.reply(file=media)
            # or just send it as it is
            await msg.reply(file=res)

async def handle_command(event):
    args = event.raw_text[1:].split()
    command = args[0]
    if command == 'ping':
        await event.edit("pong !")
    if command == 'restart':
        await event.edit("restarting ....")
        os.execl(sys.executable, *([sys.executable]+sys.argv))
    if command == 'time':
        now = datetime.datetime.now()
        time = now.strftime("%H:%M:%S")
        await event.edit("It's now `"+time+"` in Sri Lanka")
    if command == 'id':
        await event.edit("Current Chat Id: `{0}`".format(event.chat.id))
    if command == 'dl':
        msg = await event.get_reply_message()
        if msg.media is not None:
            await event.edit("please wait ...")
            await download_or_upload(event, msg)
        else:
            await event.edit("no media found")