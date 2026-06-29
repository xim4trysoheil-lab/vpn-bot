from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8887262089:AAFVwP3pZFoc4J-IdE-dDGEnAOcCeGpYKlk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 سلام، خوش اومدی!\n\n"
        "🌐 به ربات رسمی فروش VPN خوش اومدی.\n\n"
        "از طریق من می‌تونی اشتراک VPN تهیه کنی و بعد از پرداخت، اطلاعات اتصال رو دریافت کنی.\n\n"
        "👇 از دکمه‌های زیر استفاده کن."
    )

    await update.message.reply_text(text)
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
