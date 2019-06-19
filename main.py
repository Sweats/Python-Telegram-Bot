from sys import argv
import argparse
import bot
import settings as ini
from settings import clean


def main():
    argc = len(argv)
    if argc < 2:
        print ("No arguments passed. To learn how to use this program, pass in -h or --help")
        return
    args = parse()
    if args.gen:
        ini.genfiles(args.config)
    if args.start:
        bot.startbot(args.config)
    if args.clean:
        clean(args.config)
        
def parse():
    defaultconfig = 'telegram-bot.ini'
    defaultlog = 'telegram-bot-log.log'
    parser = argparse.ArgumentParser(description='This bot is responsible for searching the Trial and Error forums and getting a thread url when someone in the Telegram chat requests it. To start using this bot, call this script with -g or --gen. Edit the configuration file then simply run this script with --start. Some of these command options are useless because I wanted to try making new things in order to get better at using the Python programming language.')
    parser.add_argument('-g', '--gen', help='Generates a configuration and log file to be used by the bot when loading it. If the the log and configuration parameters are not specified, then default names will be used for both.', action='store_true')
    parser.add_argument('-c', '--config', help='The configuration (ini) file that we want to use for the bot. If one is not specified, then a default name will be used', default=defaultconfig)
    parser.add_argument('-s', '--start', help='Starts the bot.', action='store_true')
    parser.add_argument('-cl', '--clean', help='Cleans the log and configuration file inside the working directory by removing them', action='store_true')
    return parser.parse_args()

if __name__ == "__main__":
    main()
