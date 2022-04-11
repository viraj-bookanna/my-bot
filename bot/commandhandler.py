import __main__,os,sys,time,datetime,sheller,util

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
    if command == 'shell':
        shell_msg = await event.get_reply_message()
        fileName = await util.uniqid("shell_output_")
        await util.file_put_contents(fileName, shell_msg.raw_text)
        os.system("bash -c \"exec nohup setsid python sheller.py '{0}' > /dev/null 2>&1 &\"".format(fileName))
        if len(args) > 1:
            if args[2] == 'out':
                await util.show_shell_output(event, fileName+".log")