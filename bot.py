import configparser
import datetime
import time
from os import listdir
from os.path import isfile, join
import threading

from telegram.ext import Updater, CommandHandler


def hello(update, context):
    now = datetime.datetime.now()
    user_name = update.message.from_user.username
    print("{}, {}: hello".format(user_name, now))
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


def cam(update, context):
    print('cam')
    only_files = [f for f in listdir(PIC_DIR) if isfile(join(PIC_DIR, f))]
    only_files.sort(reverse=True)
    fn = join(PIC_DIR, only_files[0])
    update.message.reply_text("0 is {}".format(fn))
    chat_id = update.effective_chat.id
    now = datetime.datetime.now()
    caption = str(now)
    with open(fn, 'rb') as f:
        context.bot.send_photo(chat_id=chat_id, caption=caption, photo=f)


if __name__ == "__main__":
    print("Begin")

    num_threads = threading.activeCount()
    print("Threads {}".format(num_threads))

    config = configparser.RawConfigParser()
    config.read('bot.properties')
    TOKEN = config.get('Bot', 'token')
    use_proxy = config.getboolean('Bot', 'use_proxy')
    PROXY = config.get('Bot', 'proxy')
    REQUEST_KWARGS = {
        'proxy_url': PROXY,
    }
    PIC_DIR = config.get('Bot', 'pic_dir')

    if use_proxy:
        print("Use proxy {}".format(PROXY))
        updater = Updater(TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
    else:
        updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('cam', cam))
    updater.start_polling()

    num_threads = threading.activeCount()
    print("Threads {}".format(num_threads))
    # updater.start_polling()
    # updater.idle()
    # while True:
    #     try:
    #         time.sleep(1)
    #     except:
    #         break
    # print("Stopping...")
    # updater.stop()
    # print("End")
