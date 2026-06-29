from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8887262089:AAFVwP3pZFoc4J-IdE-dDGEnAOcCeGpYKlk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام!\n\n"
        "به ربات فروش VPN خوش اومدی 🌹"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
