import commandhandler

async def outgoing_msg_handler(event):
    if event.raw_text.startswith('.'):
        await commandhandler.handle_command(event)
