from telethon import TelegramClient
import login
from time import sleep
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
api_id = 28348074
api_hash = "ec034321b8e78b79e94efdab078de0af"
msg = input("type in the message you wanna send:  ")
user_id = input("Enter user id")
number_of_messages = eval(input("Enter the number of messages: "))
with TelegramClient('donal',api_id,api_hash) as client:
    for i in range(number_of_messages):
        client.loop.run_until_complete(client.send_message(user_id,msg))
        sleep(5)
