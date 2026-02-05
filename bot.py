#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
بوت تيليجرام يعمل 24/7 باستخدام Telethon
"""

import os
import logging
from telethon import TelegramClient, events

# 🔒 استخدم متغيرات البيئة بدلاً من كتابة البيانات في الكود
API_ID = int(os.getenv('API_ID', 0))  # ضع API_ID الحقيقي هنا أو في متغير البيئة
API_HASH = os.getenv('API_HASH', '')  # ضع API_HASH الحقيقي هنا أو في متغير البيئة
BOT_TOKEN = os.getenv('BOT_TOKEN', '')  # ضع BOT_TOKEN الحقيقي هنا أو في متغير البيئة

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# إنشاء العميل
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    user = await event.get_sender()
    await event.reply(f'مرحباً {user.first_name}! أنا بوت يعمل 24/7. 😊')

@bot.on(events.NewMessage)
async def echo_handler(event):
    # رد على جميع الرسائل
    if event.is_private:
        await event.reply(f'لقد أرسلت: {event.text}')

async def main():
    # ابدأ البوت
    await bot.start()
    print("✅ البوت يعمل الآن!")
    
    # ابقَ متصلاً
    await bot.run_until_disconnected()

if __name__ == '__main__':
    # تشغيل البوت
    import asyncio
    asyncio.run(main())
