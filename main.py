from discord.ext import commands
import discord
import random

intents = discord.Intents.all()
# Change "!" to change the bot prefix
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

def get_random_cat(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines)

@bot.event
async def on_ready():
    # Change "custom status" to anything you want to change it's rich-presense
    # You can also change "watching" to all the other things
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='custom status'))
    print(f'{bot.user.name} is now online!')

@bot.command()
async def cat(ctx):
    random_cat = get_random_cat(Cats_list.txt)
    await ctx.send(random_cat)

# Replace "Your bot token" with your actual bot token
bot.run('Your bot token')
