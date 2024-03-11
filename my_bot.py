import os

import discord
from dotenv import load_dotenv

load_dotenv()
MY_TOKEN = os.getenv("DISCORD_TOKEN")
print(MY_TOKEN)
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.content == "oi":
            await message.channel.send(f"Oi {message.author.name}, tudo bem?")
        if message.content == "tchau":
            await message.channel.send(f"Tchau {message.author.name}, até mais!")


client = MyClient(intents=intents)
client.run(MY_TOKEN)
