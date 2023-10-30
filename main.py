from discord.ext import commands
import discord
import random
import os
import Cats_list  # Import the Cats_list module

intents = discord.Intents.all()
# Change "!" to change the bot prefix
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='cats meowing'))
    print(f'{bot.user.name} is now online!')

@bot.command()
async def cat(ctx):
    random_cat = random.choice(Cats_list.cats)
    await ctx.send(random_cat)

# Replace "Your bot token" with your actual bot token
bot.run('MTE2ODU4NTE2MzYxNDIwODA1MQ.G4rSws.5J6Dx5KgVr7NSndX-TbNxpK412WB51AT-yW56Q')