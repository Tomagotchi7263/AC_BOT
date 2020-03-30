# Local Imports
from itemLookup import ItemLookup
from stalkMarket import StalkMarket
# PIP Imports
import discord
from discord.ext import commands, tasks
import asyncio
# Base Imports
import re
from datetime import datetime, date, timedelta

TOKEN = 'NjkyMDA0Nzc4NTEwOTA5NDgx.XnoN7g.F69NFfJcigVwsOTu7IN_J5uGz4o'
ANNOUNCEMENT_ID = 693870910448336956

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
        self.dailyMessage.start()
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
            if message.content.split(' ')[0] == "!today":
                await message.channel.send('TODO: ADD DAILY MESSAGE')
            elif message.content.split(' ')[0] == "!help":
                await message.channel.send("TODO: ADD HELP MESSAGE")
            elif message.content.split(' ')[0] == "!turnip":
                stalk = StalkMarket()
                await message.channel.send(stalk.Process(message, client))

        if message.content == 'ping':
            await message.channel.send('pong')
    
    @tasks.loop(hours=24)
    async def dailyMessage(self):
        messageChannel = client.get_channel(ANNOUNCEMENT_ID)
        await messageChannel.send("This a test of my automated daily message!")
        pass

    @dailyMessage.before_loop
    async def before(self):
        await client.wait_until_ready()
        now = datetime.now()
        tomorrow = date.today() + timedelta(days=1) 
        next = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 8, 0)
        diff = next - now
        print("Automated message goes out in " + str(diff.total_seconds()) + " seconds...")
        await asyncio.sleep(diff.total_seconds())

client = MyClient()
client.run(TOKEN)