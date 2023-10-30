from discord.ext import commands
import Cats_list
import discord
import random

intents = discord.Intents.all()
# Change "!" to change the bot prefix
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    # Change "custom status" to anything you want to change it's rich-presense
    # You can also change "watching" to all the other things
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='custom status'))
    print(f'{bot.user.name} is now online!')

@bot.command()
async def random_cat(ctx):
    random_cat = random.choice(Cats_list.cats)
    await ctx.send(random_cat)

# Replace "Your bot token" with your actual bot token
bot.run('Your bot token')