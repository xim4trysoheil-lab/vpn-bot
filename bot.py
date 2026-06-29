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

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام!\n\n"
        "🌹 به ربات فروش VPN خوش اومدی.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کن:",
        reply_markup=main_keyboard
    )

# مدیریت دکمه‌ها
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # خرید پلن
    if text == "🛒 خرید پلن":
        await update.message.reply_text(
            "🛒 بخش خرید پلن به‌زودی فعال می‌شود."
        )

    # تمدید پلن
    elif text == "🔄 تمدید پلن":
        await update.message.reply_text(
            "🔄 بخش تمدید پلن به‌زودی فعال می‌شود."
        )

    # لیست پلن
    elif text == "📋 لیست پلن":
        await update.message.reply_text(
            "📦 پلن‌های موجود:\n\n"
            "🔹 اشتراک ۱ ماهه\n"
            "💰 قیمت: ۸۵۰,۰۰۰ تومان"
        )

    # کانال
    elif text == "📢 کانال WireGuard":
        with open("channel.jpg", "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=(
                    "📢 کانال رسمی WireGuard\n\n"
                    "در کانال ما می‌توانید:\n"
                    "✅ اطلاعیه‌های مهم\n"
                    "✅ آموزش‌های WireGuard\n"
                    "✅ تخفیف‌های ویژه\n"
                    "✅ اخبار و بروزرسانی‌ها\n\n"
                    "👇 برای ورود روی آیدی زیر بزنید."
                ),
                reply_markup=channel_keyboard
            )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("🤖 Bot Started...")
app.run_polling()
