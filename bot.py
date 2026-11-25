
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في Gold Guard 🥇\n"
        "بوت متابعة إشارات الذهب.\n\n"
        "استخدم /gold لطلب تحليل الذهب.\n"
        "استخدم /status لمعرفة حالة البوت.\n"
        "استخدم /help للمساعدة."
    )


async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🥇 GOLD GUARD\n\n"
        "لم يتم ربط مصدر أسعار الذهب بعد.\n"
        "لن نرسل إشارة شراء أو بيع قبل توفر بيانات موثوقة."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Gold Guard يعمل لاستقبال الأوامر.\n"
        "محرك تحليل الذهب: غير متصل حالياً."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - تشغيل البوت\n"
        "/gold - طلب تحليل الذهب\n"
        "/status - حالة البوت\n"
        "/help - المساعدة"
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is missing")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gold", gold))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()


if __name__ == "__main__":
    main()
