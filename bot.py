#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
from telethon import TelegramClient, events

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# الحصول على متغيرات البيئة
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# التحقق من وجود جميع المتغيرات
if not API_ID or not API_HASH or not BOT_TOKEN:
    logger.error("❌ خطأ: متغيرات البيئة غير مكتملة!")
    logger.error(f"API_ID: {'موجود' if API_ID else 'مفقود'}")
    logger.error(f"API_HASH: {'موجود' if API_HASH else 'مفقود'}")
    logger.error(f"BOT_TOKEN: {'موجود' if BOT_TOKEN else 'مفقود'}")
    sys.exit(1)

try:
    API_ID = int(API_ID)
except ValueError:
    logger.error("❌ خطأ: API_ID يجب أن يكون رقماً صحيحاً!")
    sys.exit(1)

# إنشاء العميل
bot = TelegramClient('bot_session', API_ID, API_HASH)

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    try:
        user = await event.get_sender()
        await event.reply(f'مرحباً {user.first_name}! أنا بوت يعمل 24/7. ✅')
        logger.info(f"رد على /start من: {user.first_name} (ID: {user.id})")
    except Exception as e:
        logger.error(f"خطأ في معالجة /start: {e}")

@bot.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    await event.reply('الأوامر المتاحة:\n/start - بدء البوت\n/help - عرض المساعدة')

@bot.on(events.NewMessage)
async def echo_handler(event):
    if event.is_private and not event.message.text.startswith('/'):
        await event.reply(f'📩 لقد أرسلت: {event.text}')

async def main():
    try:
        # بدء البوت
        await bot.start(bot_token=BOT_TOKEN)
        
        # الحصول على معلومات البوت
        me = await bot.get_me()
        logger.info(f"✅ البوت يعمل بنجاح: @{me.username} (ID: {me.id})")
        print("=" * 50)
        print(f"✅ البوت يعمل الآن: @{me.username}")
        print("=" * 50)
        
        # البقاء متصلاً
        await bot.run_until_disconnected()
    except Exception as e:
        logger.error(f"❌ خطأ فادح: {e}")
        raise

if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("البوت توقف يدوياً")
    except Exception as e:
        logger.error(f"خطأ غير متوقع: {e}")
