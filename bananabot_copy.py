import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True

# token
load_dotenv()
bot_token = os.getenv('')

# Create a bot instance with intents
bot = commands.Bot(command_prefix = '/', intents = intents)

# constants
wow_classes = {
    'warrior': '1',
    'druid': '11',
    'hunter': '3',
    'mage': '8',
    'paladin': '2',
    'priest': '5',
    'rogue': '4',
    'shaman': '7',
    'warlock': '9'
}


# when bot is launched
@bot.event
async def on_ready():
    print(f'BananaBot ON, User ID: {bot.user}')


# responding directly to messages
@bot.event
async def on_message(message):
    print(1)
    # avoid responding to itself!
    if message.author.id == bot.user.id:
        return

    # if Cloudfire posts in alerts channel
    if message.author.name == '.hochopepa' and message.channel.id == 1279029762022576129 and "fruit" in message.content.lower():
        await message.channel.send(f'{message.content}! Damn, too slow... :(')
        return

    # if someone mentions valzyr
    if "valzyr" in message.content.lower():
        r = random.random()
        if r < 0.33:
            await message.channel.send('Valzyr eww...')
        elif 0.33 < r < 0.66:
            await message.channel.send('Did someone say Valzyr? Yuck!')
        elif 0.66 < r < 1:
            await message.channel.send('Boooo for Valzyr!')

    # makes sure responds to commands in messages!
    await bot.process_commands(message)


# commands

# test
@bot.command()
async def test(ctx):
    await ctx.send({bot.user})


# greets author
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author}')


@bot.command()
async def values(ctx):
    user_message = ctx.message.content.lower()
    await ctx.send(f'can store these values: {user_message} and pass to function like this')


# lockpicking
@bot.command()
async def lockpicking(ctx):
    await ctx.send('https://forum.turtle-wow.org/viewtopic.php?t=401')


# addons
@bot.command()
async def addons(ctx):
    await ctx.send('https://turtle-wow.fandom.com/wiki/Addons')


# raid reset timers
@bot.command()
async def raidreset(ctx):
    await ctx.send('https://raidres.fly.dev/raid-resets')


# return link to talent tree
@bot.command()
async def talents(ctx):
    user_message = ctx.message.content.lower()
    for i in wow_classes:
        if i in user_message:
            await ctx.send(f'https://talents.turtle-wow.org/{i}')


# return link to spells
@bot.command()
async def spells(ctx):
    user_message = ctx.message.content.lower()
    for i in wow_classes:
        if i in user_message:
            await ctx.send(f'https://database.turtle-wow.org/?spells=7.{wow_classes[i]}')


# app loop
bot.run(bot_token)
