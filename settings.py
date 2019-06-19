import os
import configparser


def genfiles(ini):
    bot = "Bot"
    webhook = "Webhook"

    if os.path.exists(ini):
        print ("Not generating configuration file %s because it already exists." % ini)
        return

    config = configparser.ConfigParser()
    config.add_section(bot)
    config.add_section(webhook)
    config.set(bot, 'enable-search', 'true')
    config.set(bot, 'token', 'BOTTOKEN')
    config.set(webhook, 'port', '1337')
    config.set(webhook, 'hostname', 'localhost')

    with open(ini, 'w') as configfile:
        config.write(configfile)
        print ("Generated configuration file %s." % ini)


def getBotSettings(ini):
    settings = dict()
    if os.path.exists(ini):
        iniconfig = configparser.ConfigParser()
        iniconfig.read(ini)
        options = iniconfig.options('Bot')
        for i in range(len(options)):
            setting = iniconfig.get('Bot', options[i])
            settings[options[i]] = setting
    else:
        print ("Failed to get bot settings from configuration file %s because it does not exist." % ini)
    return settings


def clean(ini):
    if os.path.exists(ini):
        os.remove(ini)
        print ("Deleted %s" % ini)
    else:
        print ("%s wasn't deleted because it does not exist." % ini)
