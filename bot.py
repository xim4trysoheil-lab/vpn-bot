from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8887262089:AAFVwP3pZFoc4J-IdE-dDGEnAOcCeGpYKlk"

# منوی اصلی
main_keyboard = ReplyKeyboardMarkup(
    [
        ["🛒 خرید پلن", "🔄 تمدید پلن"],
        ["📋 لیست پلن"],
        ["📢 کانال WireGuard"]
    ],
    resize_keyboard=True
)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام\n\n"
        "🌹 به ربات فروش VPN خوش اومدی.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کن.",
        reply_markup=main_keyboard
    )

# مدیریت دکمه‌ها
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 خرید پلن":
        await update.message.reply_text(
            "🛒 خرید پلن\n\n"
            "این بخش به‌زودی فعال می‌شود."
        )

    elif text == "🔄 تمدید پلن":
        await update.message.reply_text(
            "🔄 تمدید پلن\n\n"
            "این بخش به‌زودی فعال می‌شود."
        )

    elif text == "📋 لیست پلن":
        await update.message.reply_text(
            "📦 پلن‌های موجود\n\n"
            "🔹 اشتراک ۱ ماهه\n"
            "💰 قیمت: ۸۵۰,۰۰۰ تومان"
        )

    elif text == "📢 کانال WireGuard":
        await update.message.reply_text(
            "📢 کانال رسمی WireGuard\n\n"
            "برای دریافت آموزش‌ها، اطلاعیه‌ها و اخبار:\n\n"
            "@wireguardas1"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("🤖 Bot Started...")
app.run_polling()
