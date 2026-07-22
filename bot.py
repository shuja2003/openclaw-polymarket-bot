import os
import time
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

print("🚀 OpenClaw Alert Bot started...")

while True:
    bot.send_message(
        chat_id=CHAT_ID,
        text="✅ OpenClaw Bot is online and working!"
    )
    print("Message sent")
    time.sleep(3600)  # Send a message every hour
