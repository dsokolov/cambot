#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import configparser
import logging
import os
from time import sleep

import telegram
from telegram.error import NetworkError, Unauthorized
from telegram.utils.request import Request

update_id = None
PIC_DIR = None


def main():
    global update_id, PIC_DIR

    config = configparser.RawConfigParser()
    config.read('bot.properties')
    TOKEN = config.get('Bot', 'token')
    use_proxy = config.getboolean('Bot', 'use_proxy')
    PROXY = config.get('Bot', 'proxy')
    REQUEST_KWARGS = {
        'proxy_url': PROXY,
    }
    PIC_DIR = config.get('Bot', 'pic_dir')

    """Run the bot."""

    request = Request(**REQUEST_KWARGS)
    bot = telegram.Bot(TOKEN, request=request)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
            sleep(1)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id, PIC_DIR
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            # update.message.reply_text(update.message.text)
            only_files = [f for f in os.listdir(PIC_DIR) if os.path.isfile(os.path.join(PIC_DIR, f))]
            only_files.sort(reverse=True)
            fn = os.path.join(PIC_DIR, only_files[0])
            with open(fn, 'rb') as f:
                update.message.reply_photo(f)


if __name__ == '__main__':
    main()
