from itemLookup import ItemLookup
from stalkMarket import StalkMarket
import discord
import re

TOKEN = 'NjkyMDA0Nzc4NTEwOTA5NDgx.XnoN7g.F69NFfJcigVwsOTu7IN_J5uGz4o'

class MyClient(discord.Client):
    async def on_ready(self):
        import json
        masterData = None
        with open('./data/users.json') as f:
            masterData = json.load(f)
        write = False
        for user in client.get_all_members():
            if user.name + "#" + user.discriminator not in masterData.keys():
                print("Found a new user! %s" % user.name)
                masterData[user.name + "#" + user.discriminator] = {
                    "tag": user.name + "#" + user.discriminator,
                    "name": user.name,
                    "id": user.id
                }
                write = True
        if write == True:
            print("Writing new user data")
            with open('./data/users.json', 'w') as f:
                json.dump(masterData, f)
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # regText = re.findall(r'(\[\{.*\}\])', message.content)
        regText = re.findall(r'\[\{(.*?)\}\]', message.content)
        if len(regText) != 0:
            for match in regText:
                await message.channel.send(ItemLookup(match.lower()))

        if message.content[0] == "!":
            # TODO: Add daily event functionality
            if "!today" in message.content:
                await message.channel.send('TODO: ADD DAILY MESSAGE')
            elif "!help" in message.content:
                await message.channel.send("TODO: ADD HELP MESSAGE")
            elif "!turnip" in message.content:
                stalk = StalkMarket()
                await message.channel.send(stalk.Process(message, client))

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(TOKEN)