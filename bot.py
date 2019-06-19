import logging
import telegram
import forum
from settings import getBotSettings
from telegram.ext import Updater
from telegram.ext import CommandHandler
from utils import hyperlink


PROGRAMMERS_UNITE_CHAT_ID = -1001082853520
BOT_SETTINGS = {}

# Simple test function that tells us that the bot is running.


def command_test(bot, update):

    if update.message.chat_id != PROGRAMMERS_UNITE_CHAT_ID:
        return

    update.message.reply_text('I am up and running.')


# Searches a forum thread and fetches the url to be posted into the chat that will be hyperlinked.


def command_search(bot, update, args):

    if update.message.chat_id != PROGRAMMERS_UNITE_CHAT_ID:
        return

    if not args:
        update.message.reply_text('No search query specified.')
        return

    results = forum.search(args)

    if len(results) == 0:
        update.message.reply_text("No results found.")
        return

    reply = 'Here are some results:\n\n'

    for i in range(len(results)):
        reply += results[i]
        reply += '\n'

    update.message.reply_html(reply)


# This command will link to the forum thread about this thread that tells the people in the group chat what this bot is about.""
def command_help(bot, update):

    if update.message.chat_id != PROGRAMMERS_UNITE_CHAT_ID:
        return

    reply = 'Here\'s the link:\n\n'
    url = 'https://forum.symnet.moe/viewtopic.php?f=4&t=35'
    text = 'Introducing the Trial and Error bot for Telegram'
    linkedtext = hyperlink(url, text)
    update.message.reply_html(reply + linkedtext)


def command_announcments(bot, update):

    if update.message.chat_id != PROGRAMMERS_UNITE_CHAT_ID:
        return

    announcements = forum.getAnnouncements()

    if len(announcements) == 0:
        update.message.reply_text("No announcements found.")
        return

    reply = 'Recent Announcements:\n\n'

    for i in range(len(announcements)):
        reply += announcements[i]
        reply += '\n'

    update.message.reply_html(reply)


# Telegram chat id for programmers unite: -1001082853520
def startbot(ini):
    global BOT_SETTINGS
    BOT_SETTINGS = getBotSettings(ini)
    bottoken = BOT_SETTINGS.get('token')

    try:
        updater = Updater(token=bottoken)
    except telegram.error.InvalidToken:
        print ("Your bot token is invalid! Check your configuration file!")
        return

    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    startcommand = CommandHandler('test', command_test)
    helpcommand = CommandHandler('help', command_help)
    searchcommand = CommandHandler('search', command_search, pass_args=True)
    announcecommand = CommandHandler('announcements', command_announcments)

    dispatcher.add_handler(startcommand)
    dispatcher.add_handler(helpcommand)
    dispatcher.add_handler(searchcommand)
    dispatcher.add_handler(announcecommand)
    updater.start_polling()

    print ("Successully started the programmers unite bot.")
    updater.idle()
