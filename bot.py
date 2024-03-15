import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
current_channel = int(os.getenv('CHANNEL_ID_NUMBER'))

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

client.run(os.getenv('BOT_TOKEN'))