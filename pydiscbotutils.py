#!/bin/python

import json
import os

def secret(key):
    return json.loads(open(os.path.join("..", "secret.json")).read())[key]

class PyDiscBotConfig:
    def __init__(self, main_channel, bot_admin_channel, name):
        self.channels = PyDiscBotChannels(main_channel, bot_admin_channel)
        self.name = name
        self.admin = PyDiscBotAdmin()

class PyDiscBotChannels:
    def __init__(self):
        self.main = main
        self.bot_admin = bot_admin

class PyDiscBotAdmin:
    def __init__(self):
        self.shutdown_message = "sudo shutdown now " + secret("bot-admin-pwd")
