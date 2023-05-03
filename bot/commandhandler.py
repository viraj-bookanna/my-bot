import __main__,os,sys,time,datetime,util,subprocess,asyncio

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
        if shell_msg == None:
            return
        cwd = os.getcwd();
        fileName = await util.uniqid("shell_output_")
        await util.file_put_contents("{0}/bot/{1}".format(cwd, fileName), shell_msg.raw_text)
        subprocess.Popen("python sheller.py {0}".format(fileName).split(), shell=False, stdin=None, stdout=None, stderr=None, close_fds=True, creationflags=0x00000008, cwd="bot")
        if len(args) > 1:
            if args[1] == 'out':
                await event.edit("spawning...")
                logFile = "{0}/bot/{1}.log".format(cwd, fileName)
                await util.show_shell_output(event, logFile)