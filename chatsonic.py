import os
import requests
from telegram.ext import Updater, MessageHandler, Filters

# 获取环境变量
telegram_token = os.environ.get('TELEGRAM_TOKEN')
chatsonic_url = os.environ.get('CHATSONIC_URL')

# 创建 Telegram Bot
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# 处理消息
def echo(update, context):
    message = update.message.text
    response = requests.post(chatsonic_url, json={"input": message})
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.json()['generated_text'])

# 注册消息处理器
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# 启动 Telegram Bot
updater.start_polling()
