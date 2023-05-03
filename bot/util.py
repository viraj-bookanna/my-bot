import random,aiofiles,asyncio,os

async def uniqid(prefix=''):
    hexlist = "0123456789abcdef"
    prefix = str(prefix)
    uid = ""
    for i in range(17):
        rnd = random.randrange(16)
        uid += hexlist[rnd:rnd+1]
    return prefix+uid
async def file_get_contents(fName):
    try:
        async with aiofiles.open(fName, mode='r') as file:
            fdata = await file.read()
        return fdata
    except:
        return ""
async def file_put_contents(fName, fData):
    try:
        async with aiofiles.open(fName, mode='w') as file:
            await file.write(fData)
        return True
    except:
        return False
async def show_shell_output(event, logFile):
    await asyncio.sleep(2)
    last = ''
    while os.path.isfile(logFile):
        output = await file_get_contents(logFile)
        last = output
        if last != output and output != '':
            await event.edit(output)
        await asyncio.sleep(2)