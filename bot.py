from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8887262089:AAFVwP3pZFoc4J-IdE-dDGEnAOcCeGpYKlk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛒 خرید پلن", "🔄 تمدید پلن"],
        ["📋 لیست پلن", "🛟 پشتیبانی"],
        ["📢 کانال WireGuard"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 سلام!\n\n"
        "به ربات فروش VPN خوش اومدی 🌹\n\n"
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
