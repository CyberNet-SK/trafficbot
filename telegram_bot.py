import requests
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# আপনার বট টোকেন ও চ্যাট আইডি
BOT_TOKEN = "8709721808:AAHj13RQOzOA0GY8pE3xxiZEFZVE_TW3NTE"
CHAT_ID = "7819937011"
RENDER_URL = "https://your-render-app.onrender.com/visit"  # Render লিংক দিন

# টার্গেট সাইট (যেখানে অ্যাড আছে)
TARGET_SITE = "https://your-target-site.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 সাইট ভিজিট শুরু করুন", callback_data='start_visit')],
        [InlineKeyboardButton("📊 স্ট্যাটাস", callback_data='status')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 স্বাগতম! নিচের বাটনে ক্লিক করে অ্যাড ভিউ জেনারেট করুন।",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'start_visit':
        # Render-এ রিকোয়েস্ট পাঠান
        try:
            response = requests.get(RENDER_URL, params={'url': TARGET_SITE}, timeout=10)
            if response.status_code == 200:
                await query.edit_message_text("✅ সাইট ভিজিট সফলভাবে ট্রিগার হয়েছে! অ্যাড লোড হচ্ছে...")
            else:
                await query.edit_message_text("❌ Render-এ সমস্যা হয়েছে। পরে চেষ্টা করুন।")
        except Exception as e:
            await query.edit_message_text(f"⚠️ ত্রুটি: {str(e)}")

    elif query.data == 'status':
        await query.edit_message_text("📊 বট চালু আছে। প্রতিবার ক্লিক করলে একটি নতুন ভিজিট যাবে।")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 বট চালু হয়েছে...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
