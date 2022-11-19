from telethon import TelegramClient, events
from time import sleep

api_id = 28348074
api_hash = "ec034321b8e78b79e94efdab078de0af"
client = TelegramClient('donal', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi, how you doing')
        sleep(5)
        await event.delete()


client.start()
client.run_until_disconnected()
