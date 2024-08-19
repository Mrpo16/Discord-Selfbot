import discord
from discord.ext import commands
#USE discord.py==1.7.3 OTHERWISE IT WILL NOT WORK
token = ""

client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_ready():
    print(f"Bot is ready. Logged in as {client.user} (ID: {client.user.id})")

@client.command()
async def ping(ctx):
    print("pong")
    await ctx.send("pong")


client.run(token, bot=False)
