from telethon import events,TelegramClient

api_id = 28348074
api_hash = "ec034321b8e78b79e94efdab078de0af"
client = TelegramClient('donal', api_id, api_hash)

@client.on(events.MessageDeleted)
async def check_deleted_message(event):
    for msg_id in event.deleted_ids:
        print('Message', msg_id, 'was deleted in', event.chat_id)