from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
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

# فقط دکمه کانال
channel_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("@wireguardas1")]
    ],
    resize_keyboard=True
)

# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام\n\n"
        "🌹 به ربات فروش VPN خوش اومدی.\n\n"
        "از منوی زیر یکی از گزینه‌ها را انتخاب کنید.",
        reply_markup=main_keyboard
    )

# دکمه‌ها
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 خرید پلن":
        await update.message.reply_text(
            "🛒 بخش خرید پلن به‌زودی فعال می‌شود."
        )

    elif text == "🔄 تمدید پلن":
        await update.message.reply_text(
            "🔄 بخش تمدید پلن به‌زودی فعال می‌شود."
        )

    elif text == "📋 لیست پلن":
        await update.message.reply_text(
            "📦 پلن‌های موجود\n\n"
            "🔹 اشتراک ۱ ماهه\n"
            "💰 قیمت: ۸۵۰,۰۰۰ تومان"
        )

    elif text == "📢 کانال WireGuard":
        with open("channel.jpg", "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=(
                    "📢 کانال رسمی WireGuard\n\n"
                    "برای اطلاع از:\n"
                    "✅ آموزش‌های WireGuard\n"
                    "✅ بروزرسانی‌ها\n"
                    "✅ تخفیف‌های ویژه\n"
                    "✅ اطلاعیه‌های مهم\n\n"
                    "👇 برای ورود روی دکمه زیر بزنید."
                ),
                reply_markup=channel_keyboard
            )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("🤖 Bot Started...")
app.run_polling()
