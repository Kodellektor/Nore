import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#load environment variables and establish client 
load_dotenv()
current_channel = int(os.getenv('CHANNEL_ID_NUMBER'))
client = commands.Bot(command_prefix = '$', help_command=None, intents = discord.Intents.all())

#load cogs
cogs_directory = os.getenv('COGS_DIRECTORY')
COGS = []
with os.scandir(cogs_directory) as cogsdir:
    for entry in cogsdir:
        COGS.append(entry)
cogsdir.close()
for cog in COGS:
    client.load_extension(f'cog.{cog}')

#commands/actions called when bot is fully ready
@client.event
async def on_ready():
    """
    This function listens for the event of fully loaded
    bot, which is different from start-up. 
    """
    
    print(f'{client.user} has logged in!')
    
    welcome = await client.fetch_channel(current_channel)
    await welcome.send('Let your fortunes flow!')

client.run(os.getenv('AUTHENTICATION_TOKEN')) #establish client connection 