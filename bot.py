import os
import time
from telegram import Bot
from weather import get_shanghai_weather

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

print("🌡 Shanghai Weather Alert Bot started...")

while True:
    temp = get_shanghai_weather()

    message = (
        f"🌡 Shanghai Weather Update\n\n"
        f"Forecast High: {temp}°C\n\n"
        f"Polymarket Weather Bot is watching."
    )

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    print("Alert sent:", temp)

    time.sleep(60)
