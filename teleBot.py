from telegram import *
from telegram.ext import *
import requests as r 
bot_token = "5830822420:AAGvhHGM5UIEOKo6hUa4lPQkwoAdnW8i5eQ"
chat_id = "1221832086"
#{'first_name': 'AFPLUAAS', 'username': 'AFPLUAASbot', 'supports_inline_queries': False, 'id': 5584328065, 'can_read_all_group_messages': False, 'can_join_groups': True, 'is_bot': True}

def welcomeMessage(update: Update, context):
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    bot.send_message(chat_id="1221832086", text=f"New User for Telechat Bot \n User Name {first_name } {last_name}\n User ID {update.effective_chat.id} ")
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""
    Hello {first_name}! 🎉
    Welcome to our community!
 
    Your Chat ID is {update.effective_chat.id}.

    If you need assistance or have any questions, feel free to ask. 😊
    Enjoy your time and have a wonderful day! 😎

    Sign up : https://telechatbot.github.io/?type=signup&chatid={update.effective_chat.id}  to access additional features with a 4-digit PIN.

    Set your PIN to login easily and securely. Just 4 digits are enough!

    Remember your PIN for convenient logins. 💻📲

    We appreciate your support! 🙏
    """
    )

def send_to_chat(update: Update, context):
    message = update.message.text
    sender_name = update.message.from_user.first_name
    sender_id = update.message.from_user.id

    if "$" in message:
        command = message.split("$")

        if len(command) >= 3:
            command_mode = command[0].strip()
            reply_id = command[1].strip()
            reply_message = command[2]

            if command_mode.lower() == "reply":
                context.bot.send_message(chat_id=reply_id, text=reply_message)
                context.bot.send_message(chat_id=chat_id, text="send")
            else:
                reply = f"Message received from {sender_name} (ID: {sender_id}):\n\n{message}"
                context.bot.send_message(chat_id=chat_id, text=reply)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Invalid command format. Please use the correct format.")
    else:
        reply = f"Message received from {sender_name} (ID: {sender_id}):\n\n{message}"
        context.bot.send_message(chat_id=chat_id, text=reply)

def reply_message(update: Update, context):
     commands = update.message.text
     command = commands.split("$")
     reply_id = int(command[1].strip())
     reply_message = command[2]
     bot.send_message(
        chat_id=reply_id,
        text=reply_message)

bot = Bot(token=bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

start = CommandHandler("start", welcomeMessage)
reply_command = CommandHandler("reply",reply_message)

dispatcher.add_handler(start)
dispatcher.add_handler(MessageHandler(Filters.text, send_to_chat))
dispatcher.add_handler(reply_command)

print("Connected....")
updater.start_polling()
