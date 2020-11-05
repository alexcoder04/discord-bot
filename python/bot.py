#!/bin/python3

import discord
from datetime import datetime
import plugins
import os; import sys

class PythonDiscordBot(discord.Client):
    # log in
    async def on_ready(self):
        self.print_message("LOGIN", "Logged in.")
        self.read_config()
        self.config["secret"]["adminPwd"] = json.loads(open(os.path.join("..", "secret.json"), "r").read())["adminPwd"]
        channel = client.get_channel(self.config["mainChannelId"])
        await channel.send(self.config["botName"]  + " ist online XD")
        return

    # handeling messages
    async def on_message(self, message):
        # ignoring own messages
        if message.author == client.user:
            return

        if lowercase(self.config["name"]) in lowercase(message.content):
            # the message is addressed to the bot ->
            # run message analysing code
            # runnning a command sent from bot admin
            if message.content = (f"$sudo %{self.config['secret']['adminPwd']} shutdown"):
                self.exit()
            return

    async def run_admin_cmd(self, message):
        if "%" + self.config["secret"]["adminPwd"] in message.content:
            pass
        else:
            message.author.send("Sorry but you haven't the permissions to run commands on the bot.")
        return

    async def print_message(key, message):
        print(f"[{datetime.now()}] [{key}] {message}")
        return

    async def read_config():
        self.config = json.loads(open(os.path.join("..", "config.json"), "r").read())
        return

    async def exit():
        await client.logout()
        sys.exit(0)

myBot = PythonDiscordBot()
try:
    myBot.run(json.loads(open(os.path.join("..", "secret.json"), "r").read())["token"])
except FileNotFoundError:
    myBot.print_message("ERROR", "You need to create a secret.json file.")
    myBot.print_message("INFO", "Structure of this file: {'token': 'YOUR_BOT_TOKEN', 'adminPwd': 'A_PASSWORD_TO_MANAGE_YOUR_BOT'}.")
