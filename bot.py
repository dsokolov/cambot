import datetime

import cv2
from telegram.ext import Updater, CommandHandler
import configparser
import io


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def cam(update, context):
    now = datetime.datetime.now()
    print("cam", now, update.message.from_user.username)
    global frame
    if frame is not None:
        caption = str(now)
        chat_id = update.effective_chat.id
        file_name = "temp.png"
        cv2.imwrite(file_name, frame)
        with open(file_name, 'rb') as f:
            context.bot.send_photo(chat_id=chat_id, caption=caption, photo=f)


if __name__ == "__main__":
    print("Begin")

    config = configparser.RawConfigParser()
    config.read('bot.properties')
    TOKEN = config.get('Bot', 'api.token')

    frame = None
    cap = cv2.VideoCapture(0)
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('cam', cam))
    updater.start_polling()
    while True:
        try:
            ret, frame = cap.read()
        except KeyboardInterrupt:
            break
    cap.release()
    print("End")
