#!/bin/python3

import discord
from datetime import datetime
import os; import sys
import pydiscbotutils as utils

class PythonDiscordBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.config = utils.PyDiscBotConfig("main_channel", "bot_admin_channel", "Erhardt")

    # log in
    async def on_ready(self):
        self.print_message("login", "Logged in.")
        channel = client.get_channel(self.config.channels.bot_admin)
        await channel.send(self.config.name  + " got online.")
        return

    # handeling messages
    async def on_message(self, message):
        # ignoring own messages
        if message.author == client.user: return

        if lowercase(self.config.name) in lowercase(message.content):
            # the message is addressed to the bot ->
            # run message analysing code
            # runnning a command sent from bot admin
            if message.content == self.config.admin.shutdown_message:
                self.exit()
            return

    async def print_message(key, message):
        print(f"[{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}] [{upper(key)}] {message}")
        return

    async def exit():
        await client.logout()
        sys.exit(0)

myBot = PythonDiscordBot()
try:
    myBot.run(utils.secret.token())
except FileNotFoundError:
    myBot.print_message("error", "You need to create a secret.json file.")
    myBot.print_message("info", "Structure of this file: {'token': 'YOUR_BOT_TOKEN', 'adminPwd': 'A_PASSWORD_TO_MANAGE_YOUR_BOT'}.")
