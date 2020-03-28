from itemLookup import ItemLookup
import discord
import re

TOKEN = 'NjkyMDA0Nzc4NTEwOTA5NDgx.XnoN7g.F69NFfJcigVwsOTu7IN_J5uGz4o'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # regText = re.findall(r'(\[\{.*\}\])', message.content)
        regText = re.findall(r'\[\{(.*?)\}\]', message.content)
        if len(regText) != 0:
            for match in regText:
                await message.channel.send(ItemLookup(match))

        if '!today' in message.content:
            # TODO: Add daily event functionality
            await message.channel.send('Today in Animal Crossing: New Horizons...')

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(TOKEN)